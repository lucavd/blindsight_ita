#!/usr/bin/env python3
"""End-to-end self test of tools/blindsight.py on tests/fixture.htm.

Builds a throw-away project in a temporary directory, runs the whole
pipeline with a fake "translation", and checks that the gates catch the
errors they exist for. Usage: python3 tests/selftest.py
"""

import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
spec = importlib.util.spec_from_file_location("bt", PROJECT / "tools" / "blindsight.py")
bt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bt)

failures = []


def run(root, *args):
    r = subprocess.run([sys.executable, str(root / "tools" / "blindsight.py"),
                        "--root", str(root)] + list(args), capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        failures.append(name)
        if detail:
            print("     " + detail.strip().replace("\n", "\n     ")[:1500])


def fake_translate(md, pid):
    if pid == "p00019":
        return bt.PLACEHOLDER
    md = re.sub(r'"([^"]*)"', "«\\1»", md)
    md = md.replace("\u2014", ", ")
    return "[IT] " + md if md and not md.startswith(("\\", "*", ">")) else md


def main():
    tmp = Path(tempfile.mkdtemp(prefix="bt-selftest-"))
    try:
        for d in ("tools", "epub", "docs"):
            shutil.copytree(PROJECT / d, tmp / d)
        (tmp / "source" / "original").mkdir(parents=True)
        shutil.copy(HERE / "fixture.htm", tmp / "source" / "original" / "Blindsight.htm")
        (tmp / "docs" / "glossary.tsv").write_text(
            "id\tterm_en\tmatch_en\trendering_it\tmatch_it\tstatus\tnote\n"
            "G01\tparagraph\t\\bparagraph\tparagrafo\t\\bparagraf\tapproved\ttest\n",
            encoding="utf-8")

        code, out = run(tmp, "extract", str(tmp / "source/original/Blindsight.htm"))
        expect("extract: coverage gate passes", code == 0 and "superato" in out, out)
        expect("extract: image reported", "rorschach.gif" in out, out)
        rows = [__import__("json").loads(l) for l in
                (tmp / "source/paragraphs.jsonl").read_text(encoding="utf-8").splitlines()]
        pid_of = lambda txt: next(r["id"] for r in rows if r["plain"].startswith(txt))
        row_of = lambda txt: next(r for r in rows if r["plain"].startswith(txt))
        expect("extract: right-aligned paragraph is an epigraph",
               row_of("A right-aligned epigraph")["kind"] == "q", out)
        expect("extract: centred, indented and column layout recorded",
               row_of("For Somebody").get("layout") == "center"
               and row_of("An indented line").get("layout") == "indent"
               and row_of("Left voice").get("layout") == "col1"
               and row_of("Right voice").get("layout") == "col3", out)
        expect("extract: Symbol glyph converted, soft hyphen dropped",
               "sign 5\u00b0 and a softhyphen" in row_of("An indented line")["plain"]
               and "Symbol convertiti: 1" in out and "rimossi: 1" in out, out)
        expect("extract: nested superscripts marked once, inner spaces escaped",
               row_of("Nested note markers")["md"]
               == "Nested note markers^1^^,^ ^2^ and a spaced one^a\\ b^.",
               row_of("Nested note markers")["md"])
        excluded_pid = pid_of("1984. This line")
        expect("extract: image position reported", "dopo il paragrafo p000" in out, out)
        import struct, zlib
        def png_chunk(tag, data):
            return (struct.pack(">I", len(data)) + tag + data
                    + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))
        (tmp / "source" / "original" / "figure.png").write_bytes(
            b"\x89PNG\r\n\x1a\n" + png_chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 0, 0, 0, 0))
            + png_chunk(b"IDAT", zlib.compress(b"\x00\x00")) + png_chunk(b"IEND", b""))
        (tmp / "source" / "figures.tsv").write_text(
            "after_id\tfile\n%s\tfigure.png\n" % pid_of("It started with a sentence"),
            encoding="utf-8")
        start, end = pid_of("For Somebody"), pid_of("Smith, J.")
        third = pid_of("An invented epigraph opening a chapter")
        (tmp / "source" / "headings-added.tsv").write_text(
            "before_id\tlevel\ttext\n%s\t2\tRorschach\n" % third, encoding="utf-8")
        code, out = run(tmp, "chunk", "--start", start, "--end", end, "--words", "60",
                        "--add-headings", str(tmp / "source/headings-added.tsv"))
        expect("chunk: round trip gate passes", code == 0, out)
        index = (tmp / "source/index.tsv").read_text(encoding="utf-8")
        expect("chunk: added heading starts a part", "\tRorschach\t" in index, index)
        second_epi = pid_of("A second invented epigraph")
        expect("chunk: a chapter epigraph starts a chunk", "\t%s\t" % second_epi in index, index)
        code, out = run(tmp, "glossary", "--stage", "draft")
        expect("glossary: entry found in source", code == 0 and "G01\tapproved" in out, out)
        code, out = run(tmp, "verify")
        expect("verify: clean source passes", code == 0, out)

        # fake draft and final
        for stage in ("draft", "final"):
            (tmp / "translation" / stage).mkdir(parents=True, exist_ok=True)
        for f in sorted((tmp / "source" / "chunks").glob("*.md")):
            pars, _ = bt.parse_chunk_file(f)
            draft = [(pid, k, fake_translate(md, pid)) for pid, k, md in pars]
            bt.write_chunk(tmp / "translation" / "draft" / f.name, "<!-- draft -->", draft)
            final = [(pid, k, md.replace("[IT]", "[IT2]") if pid in ("p00008", "p00020") else md)
                     for pid, k, md in draft]
            bt.write_chunk(tmp / "translation" / "final" / f.name, "<!-- final -->", final)

        code, out = run(tmp, "check", "all", "--stage", "draft", "--save")
        expect("check draft: gates pass on a clean fake translation", code == 0, out)
        expect("check draft: glossary miss flagged (fake text keeps English)",
               "glossary_misses" in out, out)
        expect("check draft: identical paragraphs flagged", "identical_to_source" in out, out)
        code, out = run(tmp, "check", "1", "--stage", "final")
        expect("check final: share of changed paragraphs reported",
               "quota di paragrafi cambiati" in out, out)

        # negative cases on a copy of chunk 01
        f01 = tmp / "translation" / "draft" / "01.md"
        good = f01.read_text(encoding="utf-8")

        f01.write_text(good.replace("<!-- p00010 t -->", "<!-- p00011 t -->", 1), encoding="utf-8")
        code, out = run(tmp, "check", "01", "--stage", "draft")
        expect("gate: duplicated marker detected", code == 1 and "markers" in out, out)

        f01.write_text(re.sub(r"<!-- p00009 t -->\n[^\n]*\n", "", good), encoding="utf-8")
        code, out = run(tmp, "check", "01", "--stage", "draft")
        expect("gate: missing paragraph detected", code == 1 and "p00009" in out, out)

        f01.write_text(good.replace("Then she", "Then\u2014she"), encoding="utf-8")
        code, out = run(tmp, "check", "01", "--stage", "draft")
        expect("gate: forbidden dash detected", code == 1 and "forbidden_chars" in out, out)

        f01.write_text(good.replace("<!-- p00010 t -->", "<!-- p0010 t -->"), encoding="utf-8")
        code, out = run(tmp, "check", "01", "--stage", "draft")
        expect("gate: malformed marker detected", code == 1 and "malformato" in out, out)

        f01.write_text(re.sub(r"(<!-- p00011 t -->\n)[^\n]*", r"\1", good), encoding="utf-8")
        code, out = run(tmp, "check", "01", "--stage", "draft")
        expect("gate: empty paragraph detected", code == 1 and "empty" in out, out)
        f01.write_text(good, encoding="utf-8")

        gl = tmp / "docs" / "glossary.tsv"
        gl_good = gl.read_text(encoding="utf-8")
        gl.write_text(gl_good + "G02\tnonexistent\t\\bzzqx\tzzqx\tzzqx\tproposed\t\n", encoding="utf-8")
        code, out = run(tmp, "glossary")
        expect("glossary: entry absent from source fails the gate", code == 1, out)
        gl.write_text(gl_good, encoding="utf-8")

        # review coverage
        rv = tmp / "review"
        rv.mkdir()
        rows = ["pid\tverdict\ttype\tseverity\tproblem\tproposal"]
        rows += ["%s\tok\t\t\t\t" % pid for pid in ("p00018", "p00019", "p00020")]
        (rv / "03-findings.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
        code, out = run(tmp, "coverage", "3")
        expect("coverage: unreviewed paragraph detected", code == 1 and "p00021" in out, out)
        rows.append("p00021\tissue\tmeaning\thigh\tx\ty")
        (rv / "03-findings.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
        code, out = run(tmp, "coverage", "3")
        expect("coverage: complete review passes", code == 0 and "high=1" in out, out)

        # build
        if shutil.which("pandoc"):
            code, out = run(tmp, "build")
            expect("build: EPUB written", code == 0 and (tmp / "build/Blindsight-it.epub").exists(), out)
            book = (tmp / "build" / "Blindsight-it.md").read_text(encoding="utf-8")
            expect("build: placeholder replaced by the original lines",
                   "An epigraph quoting a song" in book and bt.PLACEHOLDER not in book, book[:800])
            expect("build: part headings shifted to level 1", "\n# [IT] Prologue" in book, book[:800])
            expect("build: no HTML comments left", "<!--" not in book)
            expect("build: layout of the source carried into the book",
                   "::: {.center}\n*For Somebody*\n:::" in book, book[:800])
            expect("build: translator note placed after the novel",
                   book.index("Nota sulla traduzione") > book.index("Notes and References"))
            html = subprocess.run(["pandoc", str(tmp / "build/Blindsight-it.md"), "-f",
                                   "markdown-smart", "-t", "html"],
                                  capture_output=True, text=True).stdout
            expect("build: escaped list markers stay text", "<ol" not in html and "<ul" not in html, html)
            expect("build: no math or citations parsed", "math" not in html and "citation" not in html, html)
            expect("build: layout becomes a styled block", 'class="center"' in html, html[:800])
            import zipfile
            with zipfile.ZipFile(tmp / "build" / "Blindsight-it.epub") as z:
                media = [n for n in z.namelist() if n.endswith(".png")]
                names = z.namelist()
            expect("build: figure of the book placed in the text and packed in the EPUB",
                   "![](figure.png)" in book and len(media) == 1, book[:600])
            expect("build: cover image packed in the EPUB",
                   any("cover" in n.lower() for n in names), "\n".join(names))
            code, out = run(tmp, "blind", "--a", str(tmp / "translation/final"),
                            "--b", str(tmp / "translation/draft"), "--chunks", "1,3")
            expect("blind: two pilot EPUBs written",
                   code == 0 and (tmp / "build/pilota-X.epub").exists()
                   and (tmp / "build/pilota-Y.epub").exists(), out)
        else:
            print("skip build tests: pandoc not installed")

        # source tampering
        c2 = tmp / "source" / "chunks" / "02.md"
        c2.write_text(c2.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        code, out = run(tmp, "verify")
        expect("verify: modified source chunk detected", code == 1 and "CAMBIATO" in out, out)

        # ranges inside the interval that are not the book
        (tmp / "source" / "excluded.tsv").write_text(
            "first_id\tlast_id\treason\n%s\t%s\ttest\n" % (excluded_pid, excluded_pid),
            encoding="utf-8")
        code, out = run(tmp, "chunk", "--start", start, "--end", end, "--words", "60", "--force",
                        "--add-headings", str(tmp / "source/headings-added.tsv"),
                        "--exclude", str(tmp / "source/excluded.tsv"))
        chunks_text = "".join(f.read_text(encoding="utf-8")
                              for f in sorted((tmp / "source" / "chunks").glob("*.md")))
        expect("chunk: excluded range left out, round trip still passes",
               code == 0 and "Esclusi in tutto: 1 paragrafi" in out
               and excluded_pid not in chunks_text, out)
        code, out = run(tmp, "verify")
        sums = (tmp / "source" / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
        expect("verify: passes after exclusions, no file listed twice",
               code == 0 and len(sums) == len(set(sums)), out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d test falliti" % len(failures) if failures else "\nTutti i test superati.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
