#!/usr/bin/env python3
"""Tools for a personal Italian translation of Peter Watts's Blindsight.

The source is the CC BY-NC-SA text the author publishes online. Every
paragraph gets a stable id (p00001...) that survives translation, so that
omissions, merges and reorderings are caught mechanically.

Subcommands
  extract   HTML source -> source/paragraphs.jsonl (gate: no text lost)
            right-aligned paragraphs are epigraphs (kind q); centred, indented
            and table-column paragraphs keep a "layout" field used by build;
            images are listed with their position (see source/figures.tsv)
  chunk     id range -> source/chunks/NN.md, index.tsv, SHA256SUMS (gate: round trip)
            --exclude leaves out ranges inside the interval that are not the book
  verify    check SHA256SUMS (the source must never change after S0)
  check     gates and flags on a translated chunk (draft or final)
  coverage  the review table of a chunk must cover every paragraph
  glossary  occurrences of every glossary entry (gate: each entry matches the source)
  status    one line per chunk, plus a suggested grouping into sessions
  build     assemble the book and write the EPUB with pandoc; images listed
            in source/figures.tsv (after_id, file) are placed in the text
  blind     blind A/B files and EPUBs for the pilot model comparison

Python 3.9+, beautifulsoup4 and lxml. pandoc for build. epubcheck optional.
"""

import argparse
import hashlib
import json
import random
import re
import shutil
import statistics
import subprocess
import sys
import zipfile
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = TOOLS_DIR.parent

BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "body", "center", "dd", "div",
    "dl", "dt", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4",
    "h5", "h6", "header", "hr", "li", "main", "nav", "ol", "p", "pre", "section",
    "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
}
SKIP_TAGS = {"head", "noscript", "script", "style", "template", "title"}
HEADING_LEVEL = {"h%d" % i: i for i in range(1, 7)}
EMPH_TAGS = {"cite", "dfn", "em", "i", "var"}
STRONG_TAGS = {"b", "strong"}

BR = "\x00"
MARKER_RE = re.compile(r"^<!-- (p\d{5}) (t|q|s|h[1-6]) -->\s*$")
CHUNK_HEADER_RE = re.compile(r"^<!-- chunk ")
SCENE_RE = re.compile(r"^(?:[*•·∗⁎]\s*)+$|^#$|^~+$|^o\s*o\s*o$")
MD_SPECIAL_RE = re.compile(r"([\\`*_\[\]<>^~$@])")
LINE_START_RE = re.compile(r"^(#|[-+] |:|\||\()")
LIST_MARKER_RE = re.compile(r"^(\d+|[A-Za-z]|[ivxlcdmIVXLCDM]+)([.)])(?= |$)")
SCENE_MD = "* * *"
PLACEHOLDER = "[[ORIGINALE]]"

# Quirks of the author's page (an OpenOffice export), found in S0.
# Glyphs typed in the Symbol font are exported as private-use code points:
# they are mapped to the Unicode character the font shows. Soft hyphens are
# invisible layout hints and are dropped.
SYMBOL_PUA = {"\uf0b0": "\u00b0", "\uf06d": "\u03bc", "\uf065": "\u03b5", "\uf073": "\u03c3"}
SOFT_HYPHEN = "\u00ad"
PUA_RE = re.compile("[\ue000-\uf8ff]")
# Epigraphs are right-aligned paragraphs, not blockquotes. Centred and
# indented paragraphs and the cells of a multi-column table keep their
# layout in the field "layout" of source/paragraphs.jsonl.
RIGHT_ALIGN_RE = re.compile(r"text-align:\s*right", re.I)
CENTER_ALIGN_RE = re.compile(r"text-align:\s*center", re.I)
INDENT_RE = re.compile(r"margin-left:\s*(\d*\.?\d+)in", re.I)
ALIGNED_TAGS = {"p", "div", "center", "td", "th", "li", "blockquote"}
INDENT_MIN_IN = 0.5


# ----------------------------------------------------------------- utilities

def die(msg, code=2):
    print("ERRORE: " + msg, file=sys.stderr)
    sys.exit(code)


def paths(root):
    root = Path(root)
    return {
        "root": root,
        "original": root / "source" / "original",
        "paragraphs": root / "source" / "paragraphs.jsonl",
        "chunks": root / "source" / "chunks",
        "index": root / "source" / "index.tsv",
        "sums": root / "source" / "SHA256SUMS",
        "figures": root / "source" / "figures.tsv",
        "draft": root / "translation" / "draft",
        "final": root / "translation" / "final",
        "notes": root / "translation" / "notes",
        "review": root / "review",
        "checks": root / "checks",
        "build": root / "build",
        "epub": root / "epub",
        "glossary": root / "docs" / "glossary.tsv",
        "epigraphs": root / "docs" / "epigraphs.tsv",
        "config": root / "tools" / "config.json",
        "comparison": root / "comparison",
    }


def load_config(p):
    cfg_path = p["config"]
    if not cfg_path.exists():
        cfg_path = TOOLS_DIR / "config.json"
    with open(cfg_path, encoding="utf-8") as fh:
        return json.load(fh)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def read_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def plain_from_md(md):
    """Text without markdown emphasis and escapes, for counts and ratios."""
    s = re.sub(r"(?<!\\)\*", "", md)
    s = re.sub(r"(?<!\\)[\^~]", "", s)
    s = s.replace("\\\n", "\n")
    s = re.sub(r"\\(.)", r"\1", s)
    return s


def normalize_source_text(s):
    """Symbol-font glyphs to Unicode, soft hyphens dropped (see SYMBOL_PUA)."""
    for a, b in SYMBOL_PUA.items():
        s = s.replace(a, b)
    return s.replace(SOFT_HYPHEN, "")


def word_count(text):
    return len(re.findall(r"\w+(?:['’]\w+)*", text))


def count_emphasis(md):
    return len(re.findall(r"(?<!\\)\*", md))


def chunk_ids(p):
    return sorted(f.stem for f in p["chunks"].glob("*.md"))


def normalize_chunk_id(raw, p):
    ids = chunk_ids(p)
    if not ids:
        die("nessun blocco in source/chunks: va prima eseguito 'chunk'")
    width = len(ids[0])
    cid = str(raw).zfill(width)
    if cid not in ids:
        die("blocco %s inesistente (blocchi: %s-%s)" % (raw, ids[0], ids[-1]))
    return cid


# ------------------------------------------------------- HTML -> paragraphs

def _wrap(inner, mark):
    """Wrap each line segment in emphasis marks, keeping spaces outside."""
    out = []
    for seg in inner.split(BR):
        core = seg.strip()
        if not core:
            out.append(seg)
            continue
        lead = seg[: len(seg) - len(seg.lstrip())]
        trail = seg[len(seg.rstrip()):]
        if mark in ("^", "~"):
            # pandoc reads a superscript or subscript only if its spaces are escaped
            core = core.replace(" ", "\\ ")
        out.append(lead + mark + core + mark + trail)
    return BR.join(out)


def _conv(node):
    """Inline node -> (markdown, plain). BR stands for <br>."""
    from bs4 import NavigableString, Tag  # imported lazily
    if isinstance(node, NavigableString):
        text = re.sub(r"\s+", " ", normalize_source_text(str(node)))
        return MD_SPECIAL_RE.sub(r"\\\1", text), text
    if not isinstance(node, Tag):
        return "", ""
    name = (node.name or "").lower()
    if name in SKIP_TAGS or name == "img":
        return "", ""
    if name == "br":
        return BR, BR
    md_parts, pl_parts = [], []
    for child in node.children:
        m, t = _conv(child)
        md_parts.append(m)
        pl_parts.append(t)
    md, pl = "".join(md_parts), "".join(pl_parts)
    # a tag nested in one of its own kind (the page has <sup><a><sup>1</sup></a></sup>)
    # is marked once, by the outer tag: doubled marks would be printed as they are
    for group, mark in ((EMPH_TAGS, "*"), (STRONG_TAGS, "**"), ({"sup"}, "^"), ({"sub"}, "~")):
        if name in group:
            if node.find_parent(list(group)) is None:
                md = _wrap(md, mark)
            break
    return md, pl


def _split_paragraphs(s):
    return re.split(r"[ \t]*" + BR + r"[ \t]*" + BR + r"[ \t" + BR + r"]*", s)


def _finish_lines(md_par, pl_par):
    md_lines = [line.strip() for line in md_par.split(BR)]
    pl_lines = [line.strip() for line in pl_par.split(BR)]
    pairs = [(m, t) for m, t in zip(md_lines, pl_lines) if t]
    if not pairs:
        return None, None
    fixed = []
    for m, _ in pairs:
        # keep pandoc from reading a line as a heading, list or table
        if LINE_START_RE.match(m):
            m = "\\" + m
        m = LIST_MARKER_RE.sub(r"\1\\\2", m)
        fixed.append(m)
    return "\\\n".join(fixed), "\n".join(t for _, t in pairs)


def extract_blocks(html_text):
    from bs4 import BeautifulSoup, Comment, Tag

    soup = BeautifulSoup(html_text, "lxml")
    images = [(im.get("src", ""), im.get("alt", "")) for im in soup.find_all("img")]
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for t in soup.find_all(list(SKIP_TAGS)):
        t.decompose()
    body = soup.body or soup
    blocks = []
    placed = []  # (number of paragraphs emitted before the image, src)

    def emit(kind, md, plain, layout=""):
        b = {"kind": kind, "md": md, "plain": plain}
        if layout and kind == "t":
            b["layout"] = layout
        blocks.append(b)

    def is_epigraph(tag, name):
        if name not in ("p", "div"):
            return False
        return bool(RIGHT_ALIGN_RE.search(tag.get("style") or "")
                    or (tag.get("align") or "").lower() == "right")

    def block_layout(tag, name, inherited):
        tokens = inherited.split()
        if name not in ALIGNED_TAGS:
            return inherited
        style = tag.get("style") or ""
        if name in ("td", "th"):
            row = tag.find_parent("tr")
            cells = row.find_all(["td", "th"], recursive=False) if row else []
            if len(cells) > 1:
                col = next(i for i, c in enumerate(cells) if c is tag) + 1
                tokens = [t for t in tokens if not t.startswith("col")] + ["col%d" % col]
        centred = (name == "center" or (tag.get("align") or "").lower() == "center"
                   or CENTER_ALIGN_RE.search(style))
        if centred and "center" not in tokens:
            tokens.append("center")
        m = INDENT_RE.search(style)
        if m and float(m.group(1)) >= INDENT_MIN_IN and "indent" not in tokens:
            tokens.append("indent")
        return " ".join(tokens)

    def emit_run(run, quote, layout=""):
        if not run:
            return
        for n in run:
            if isinstance(n, Tag):
                found = [n] if (n.name or "").lower() == "img" else n.find_all("img")
                for im in found:
                    placed.append((len(blocks), im.get("src", "")))
        md = "".join(_conv(n)[0] for n in run)
        pl = "".join(_conv(n)[1] for n in run)
        md_pars, pl_pars = _split_paragraphs(md), _split_paragraphs(pl)
        if len(md_pars) != len(pl_pars):
            raise RuntimeError("divisione dei paragrafi incoerente")
        for m_par, p_par in zip(md_pars, pl_pars):
            m, t = _finish_lines(m_par, p_par)
            if m is None:
                continue
            if SCENE_RE.match(t.strip()):
                emit("s", SCENE_MD, t.strip())
            else:
                emit("q" if quote else "t", m, t, layout)

    def has_block_child(tag):
        return any((d.name or "").lower() in BLOCK_TAGS for d in tag.find_all(True))

    def walk(container, quote, layout=""):
        run = []
        for child in list(container.children):
            if isinstance(child, Tag):
                name = (child.name or "").lower()
                if name in BLOCK_TAGS:
                    emit_run(run, quote, layout)
                    run = []
                    if name == "hr":
                        emit("s", SCENE_MD, "")
                    elif name in HEADING_LEVEL:
                        m, t = _conv(child)
                        m = re.sub(r"\s+", " ", m.replace(BR, " ")).strip()
                        t = re.sub(r"\s+", " ", t.replace(BR, " ")).strip()
                        if t:
                            emit("h%d" % HEADING_LEVEL[name], m, t)
                    else:
                        q = quote or name == "blockquote" or is_epigraph(child, name)
                        lay = block_layout(child, name, layout)
                        if has_block_child(child):
                            walk(child, q, lay)
                        else:
                            emit_run(list(child.children), q, lay)
                    continue
            run.append(child)
        emit_run(run, quote, layout)

    raw_text = body.get_text("")
    stats = {"symbol": {c: raw_text.count(c) for c in SYMBOL_PUA if c in raw_text},
             "soft_hyphens": raw_text.count(SOFT_HYPHEN)}
    walk(body, False)
    reference = re.sub(r"\s+", "", normalize_source_text(raw_text))
    stats["pua_left"] = sorted({"U+%04X" % ord(c) for c in PUA_RE.findall(reference)})
    stats["placed"] = placed
    return blocks, reference, images, stats


def cmd_extract(args):
    p = paths(args.root)
    src = Path(args.html)
    if not src.exists():
        die("file sorgente non trovato: %s" % src)
    raw = src.read_bytes()
    try:
        html_text = raw.decode("utf-8")
    except UnicodeDecodeError:
        html_text = raw.decode("cp1252")
        print("Nota: sorgente non in UTF-8, letta come Windows-1252.")
    blocks, reference, images, stats = extract_blocks(html_text)
    for i, b in enumerate(blocks, 1):
        b["id"] = "p%05d" % i
        b["words"] = word_count(b["plain"])
    p["paragraphs"].parent.mkdir(parents=True, exist_ok=True)
    with open(p["paragraphs"], "w", encoding="utf-8") as fh:
        for b in blocks:
            row = {k: b[k] for k in ("id", "kind", "md", "plain", "words")}
            if b.get("layout"):
                row["layout"] = b["layout"]
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    kinds = {}
    for b in blocks:
        kinds[b["kind"]] = kinds.get(b["kind"], 0) + 1
    print("Paragrafi estratti: %d  (%s)" % (len(blocks), ", ".join(
        "%s=%d" % kv for kv in sorted(kinds.items()))))
    print("Parole totali: %d" % sum(b["words"] for b in blocks))
    layouts = {}
    for b in blocks:
        if b.get("layout"):
            layouts[b["layout"]] = layouts.get(b["layout"], 0) + 1
    if layouts:
        print("Paragrafi con impaginazione propria: %d  (%s)" % (sum(layouts.values()), ", ".join(
            "%s=%d" % kv for kv in sorted(layouts.items()))))
    if stats["symbol"]:
        print("Caratteri del font Symbol convertiti: %d  (%s)" % (
            sum(stats["symbol"].values()), ", ".join("U+%04X->%s x%d" % (
                ord(c), SYMBOL_PUA[c], n) for c, n in sorted(stats["symbol"].items()))))
    if stats["soft_hyphens"]:
        print("Trattini morbidi (invisibili) rimossi: %d" % stats["soft_hyphens"])
    print("\nTitoli:")
    for b in blocks:
        if b["kind"].startswith("h"):
            print("  %s %s  %s" % (b["id"], b["kind"], b["plain"][:70]))
    if images:
        print("\nImmagini nella pagina (%d): il loro contenuto NON entra nel testo." % len(images))
        after = {src_img: (blocks[n - 1]["id"] if n else "-") for n, src_img in stats["placed"]}
        for src_img, alt in images[:30]:
            print("  src=%s  alt=%s  dopo il paragrafo %s" % (
                src_img, alt or "-", after.get(src_img, "?")))
        print("  Un'immagine che fa parte del libro va elencata in source/figures.tsv "
              "(after_id, file).")
    n_show = args.show
    print("\nPrimi %d paragrafi:" % n_show)
    for b in blocks[:n_show]:
        print("  %s %-2s %s" % (b["id"], b["kind"], b["plain"][:70].replace("\n", " / ")))
    print("\nUltimi %d paragrafi:" % n_show)
    for b in blocks[-n_show:]:
        print("  %s %-2s %s" % (b["id"], b["kind"], b["plain"][:70].replace("\n", " / ")))

    extracted = re.sub(r"\s+", "", "".join(b["plain"] for b in blocks))
    if stats["pua_left"]:
        print("\nCANCELLO copertura: FALLITO. Caratteri di un font speciale senza "
              "conversione: %s (vanno aggiunti a SYMBOL_PUA)." % ", ".join(stats["pua_left"]))
        return 1
    if extracted == reference:
        print("\nCANCELLO copertura: superato (il testo estratto coincide con il testo "
              "visibile dell'HTML, %d caratteri senza spazi)." % len(reference))
        return 0
    k = next((i for i, (a, b) in enumerate(zip(extracted, reference)) if a != b),
             min(len(extracted), len(reference)))
    print("\nCANCELLO copertura: FALLITO. Prima differenza al carattere %d." % k)
    print("  HTML:     ..." + reference[max(0, k - 40):k + 40])
    print("  estratto: ..." + extracted[max(0, k - 40):k + 40])
    return 1


# --------------------------------------------------------- chunk files

def render_par(kind, md):
    if kind == "s":
        return SCENE_MD
    if kind == "q":
        return "\n".join("> " + line for line in md.split("\n"))
    if kind.startswith("h"):
        return "#" * int(kind[1]) + " " + md
    return md


def unrender_par(kind, text):
    if kind == "q":
        return "\n".join(re.sub(r"^> ?", "", line) for line in text.split("\n"))
    if kind.startswith("h"):
        return re.sub(r"^#+\s*", "", text)
    return text


def parse_chunk_file(path):
    """Return [(id, kind, md)] and a list of format errors."""
    pars, errors = [], []
    cur, buf = None, []

    def close():
        if cur is None:
            stray = [line for line in buf if line.strip()
                     and not re.match(r"^\s*<!--.*-->\s*$", line)]
            if stray:
                errors.append("testo prima del primo marcatore")
            return
        text = "\n".join(buf).strip("\n").strip()
        pars.append((cur[0], cur[1], unrender_par(cur[1], text)))

    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh.read().split("\n"), 1):
            m = MARKER_RE.match(line)
            if m:
                close()
                cur, buf = (m.group(1), m.group(2)), []
            elif line.startswith("<!-- p") and line.rstrip().endswith("-->"):
                errors.append("riga %d: marcatore malformato: %s" % (n, line.strip()))
                buf.append(line)
            elif CHUNK_HEADER_RE.match(line):
                continue
            else:
                buf.append(line)
    close()
    return pars, errors


def write_chunk(path, header, pars):
    lines = [header, ""]
    for pid, kind, md in pars:
        lines.append("<!-- %s %s -->" % (pid, kind))
        lines.append(render_par(kind, md))
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def split_into_chunks(rows, target):
    chunks, cur, words = [], [], 0
    for r in rows:
        k = r["kind"]
        if cur:
            prev = cur[-1]["kind"]
            starts_part = k.startswith("h") and words >= 0.3 * target
            starts_chapter = (k == "q" and prev not in ("q",) and not prev.startswith("h")
                              and words >= 0.6 * target)
            scene_cut = k == "s" and words >= 0.8 * target
            too_long = words >= 1.6 * target and k == "t"
            if starts_part or starts_chapter or scene_cut or too_long:
                chunks.append(cur)
                cur, words = [], 0
        cur.append(r)
        words += r["words"]
    if cur:
        if chunks and words < 0.25 * target:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
    return chunks


def insert_headings(sel, tsv):
    """Insert headings missing from the HTML (e.g. part titles drawn as images).

    TSV columns: before_id, level, text. Inserted ids are p9NNNN, so they can
    never collide with extracted ids and are easy to recognise.
    """
    if not tsv.exists():
        die("file dei titoli aggiunti non trovato: %s" % tsv)
    adds = {}
    for n, line in enumerate(tsv.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("before_id"):
            continue
        cells = line.split("\t")
        if len(cells) != 3 or not cells[1].strip().isdigit():
            die("%s riga %d: servono 3 colonne (before_id, level, text)" % (tsv.name, n))
        adds.setdefault(cells[0].strip(), []).append((int(cells[1]), cells[2].strip()))
    ids = {r["id"] for r in sel}
    unknown = [k for k in adds if k not in ids]
    if unknown:
        die("titoli aggiunti prima di id inesistenti: " + ", ".join(unknown))
    out, k = [], 0
    for r in sel:
        for level, text in adds.get(r["id"], []):
            k += 1
            out.append({"id": "p9%04d" % k, "kind": "h%d" % level,
                        "md": MD_SPECIAL_RE.sub(r"\\\1", text), "plain": text,
                        "words": word_count(text)})
        out.append(r)
    return out


def drop_excluded(sel, tsv):
    """Leave out id ranges that lie inside the interval but are not the book
    (the page's own table of contents, the licence text).

    TSV columns: first_id, last_id, reason.
    """
    if not tsv.exists():
        die("file delle esclusioni non trovato: %s" % tsv)
    ids = [r["id"] for r in sel]
    drop = set()
    for n, line in enumerate(tsv.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("first_id"):
            continue
        cells = line.split("\t")
        if len(cells) != 3:
            die("%s riga %d: servono 3 colonne (first_id, last_id, reason)" % (tsv.name, n))
        a, b = cells[0].strip(), cells[1].strip()
        if a not in ids or b not in ids or ids.index(a) > ids.index(b):
            die("%s riga %d: intervallo %s-%s non valido o fuori da --start/--end" % (
                tsv.name, n, a, b))
        part = sel[ids.index(a):ids.index(b) + 1]
        print("Escluso %s-%s: %d paragrafi, %d parole (%s)" % (
            a, b, len(part), sum(r["words"] for r in part), cells[2].strip()))
        drop.update(r["id"] for r in part)
    if sel[0]["id"] in drop or sel[-1]["id"] in drop:
        die("un'esclusione comprende --start o --end: vanno spostati i confini")
    kept = [r for r in sel if r["id"] not in drop]
    print("Esclusi in tutto: %d paragrafi, %d parole." % (
        len(drop), sum(r["words"] for r in sel if r["id"] in drop)))
    return kept


def write_sums(p):
    files = sorted(p["original"].glob("*")) + [p["paragraphs"], p["index"]]
    files += sorted((p["root"] / "source").glob("*.tsv"))
    files += sorted(p["chunks"].glob("*.md"))
    files = list(dict.fromkeys(files))
    lines = ["%s  %s" % (sha256(f), f.relative_to(p["root"]).as_posix())
             for f in files if f.is_file()]
    p["sums"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def cmd_chunk(args):
    p = paths(args.root)
    if not p["paragraphs"].exists():
        die("manca source/paragraphs.jsonl: va prima eseguito 'extract'")
    rows = read_jsonl(p["paragraphs"])
    ids = [r["id"] for r in rows]
    if args.start not in ids or args.end not in ids:
        die("--start o --end non trovati tra gli id dei paragrafi")
    i0, i1 = ids.index(args.start), ids.index(args.end)
    if i0 > i1:
        die("--start viene dopo --end")
    sel = rows[i0:i1 + 1]
    if args.exclude:
        sel = drop_excluded(sel, Path(args.exclude))
    if args.add_headings:
        sel = insert_headings(sel, Path(args.add_headings))
    chunks = split_into_chunks(sel, args.words)
    width = max(2, len(str(len(chunks))))
    if p["chunks"].exists():
        if any(p["chunks"].iterdir()) and not args.force:
            die("source/chunks non è vuota: usa --force per rigenerare (solo in S0)")
        shutil.rmtree(p["chunks"])
    p["chunks"].mkdir(parents=True)

    part = ""
    index_lines = ["chunk\tpart\tfirst_id\tlast_id\tparagraphs\twords"]
    for n, ch in enumerate(chunks, 1):
        cid = str(n).zfill(width)
        heads = [r for r in ch if r["kind"].startswith("h")]
        # a chunk is named after every part it touches; the chunks that follow
        # belong to the last part opened
        label = " / ".join(h["plain"] for h in heads) if heads else part
        if heads:
            part = heads[-1]["plain"]
        w = sum(r["words"] for r in ch)
        header = "<!-- chunk %s | part: %s | %s-%s | %d words -->" % (
            cid, label or "-", ch[0]["id"], ch[-1]["id"], w)
        write_chunk(p["chunks"] / (cid + ".md"), header,
                    [(r["id"], r["kind"], r["md"]) for r in ch])
        index_lines.append("%s\t%s\t%s\t%s\t%d\t%d" % (
            cid, label or "-", ch[0]["id"], ch[-1]["id"], len(ch), w))
    p["index"].write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    rebuilt, errors = [], []
    for f in sorted(p["chunks"].glob("*.md")):
        pars, errs = parse_chunk_file(f)
        rebuilt.extend(pars)
        errors.extend("%s: %s" % (f.name, e) for e in errs)
    expected = [(r["id"], r["kind"], r["md"]) for r in sel]
    words = [sum(r["words"] for r in ch) for ch in chunks]
    print("Blocchi: %d  parole per blocco: min %d, mediana %d, max %d; totale %d" % (
        len(chunks), min(words), int(statistics.median(words)), max(words), sum(words)))
    n_sums = write_sums(p)
    print("SHA256SUMS: %d file registrati." % n_sums)
    if rebuilt == expected and not errors:
        print("CANCELLO andata e ritorno: superato (%d paragrafi identici)." % len(expected))
        return 0
    print("CANCELLO andata e ritorno: FALLITO.")
    for e in errors[:10]:
        print("  " + e)
    for a, b in zip(rebuilt, expected):
        if a != b:
            print("  primo paragrafo diverso: %s\n    file:  %r\n    jsonl: %r" % (
                b[0], a[2][:120], b[2][:120]))
            break
    return 1


def cmd_verify(args):
    p = paths(args.root)
    if not p["sums"].exists():
        die("manca source/SHA256SUMS")
    bad = 0
    lines = [l for l in p["sums"].read_text(encoding="utf-8").splitlines() if l.strip()]
    for line in lines:
        digest, rel = line.split("  ", 1)
        f = p["root"] / rel
        if not f.exists():
            print("MANCANTE  " + rel)
            bad += 1
        elif sha256(f) != digest:
            print("CAMBIATO  " + rel)
            bad += 1
    listed = {l.split("  ", 1)[1] for l in lines}
    for f in sorted(p["chunks"].glob("*.md")):
        rel = f.relative_to(p["root"]).as_posix()
        if rel not in listed:
            print("IN PIÙ    " + rel)
            bad += 1
    if bad:
        print("CANCELLO integrità della sorgente: FALLITO (%d file)." % bad)
        return 1
    print("CANCELLO integrità della sorgente: superato (%d file)." % len(lines))
    return 0


# ----------------------------------------------------------------- checks

def load_glossary(p):
    rows = []
    g = p["glossary"]
    if not g.exists():
        return rows
    lines = g.read_text(encoding="utf-8").splitlines()
    if not lines:
        return rows
    head = lines[0].split("\t")
    for n, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        cells = line.split("\t")
        row = dict(zip(head, cells + [""] * (len(head) - len(cells))))
        if row.get("status", "").strip() != "approved":
            continue
        me, mi = row.get("match_en", "").strip(), row.get("match_it", "").strip()
        if not me or not mi:
            continue
        try:
            row["_re_en"] = re.compile(me, re.I)
            row["_re_it"] = re.compile(mi, re.I)
        except re.error as e:
            die("glossario riga %d: espressione non valida (%s)" % (n, e))
        rows.append(row)
    return rows


def load_epigraph_decisions(p):
    """pid -> decision from docs/epigraphs.tsv; None if the file does not exist."""
    path = p["epigraphs"]
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return {}
    head = lines[0].split("\t")
    if "pid" not in head or "decision" not in head:
        die("docs/epigraphs.tsv: mancano le colonne pid e decision")
    out = {}
    for line in lines[1:]:
        if line.strip():
            row = dict(zip(head, line.split("\t")))
            out[row["pid"].strip()] = row.get("decision", "").strip()
    return out


def check_chunk(p, cid, stage, cfg, glossary, translation_dir=None):
    src_pars, src_err = parse_chunk_file(p["chunks"] / (cid + ".md"))
    tdir = Path(translation_dir) if translation_dir else p[stage]
    tpath = tdir / (cid + ".md")
    res = {"chunk": cid, "stage": stage, "file": str(tpath), "gates": {}, "flags": {}}
    if src_err:
        die("blocco sorgente %s malformato: %s" % (cid, src_err[0]))
    if not tpath.exists():
        res["gates"]["file"] = ["manca %s" % tpath]
        res["ok"] = False
        return res
    tgt_pars, tgt_err = parse_chunk_file(tpath)
    gates = res["gates"]
    flags = res["flags"]
    gates["format"] = tgt_err

    src_keys = [(a, b) for a, b, _ in src_pars]
    tgt_keys = [(a, b) for a, b, _ in tgt_pars]
    if src_keys != tgt_keys:
        s_ids, t_ids = [k[0] for k in src_keys], [k[0] for k in tgt_keys]
        missing = [i for i in s_ids if i not in t_ids]
        extra = [i for i in t_ids if i not in s_ids]
        msgs = []
        if missing:
            msgs.append("paragrafi mancanti: " + ", ".join(missing[:20]))
        if extra:
            msgs.append("paragrafi in più o duplicati: " + ", ".join(extra[:20]))
        dup = sorted({i for i in t_ids if t_ids.count(i) > 1})
        if dup:
            msgs.append("marcatori duplicati: " + ", ".join(dup[:20]))
        if not msgs:
            wrong_kind = [t[0] for s, t in zip(src_keys, tgt_keys) if s != t]
            msgs.append("ordine o tipo diverso, dal paragrafo " + (wrong_kind or ["?"])[0])
        gates["markers"] = msgs
    else:
        gates["markers"] = []

    tgt_map = {a: (b, c) for a, b, c in tgt_pars}
    empty, scene, forb, placeholder_bad = [], [], [], []
    placeholders, ratios, ratio_out, english, gloss_miss = [], [], [], [], []
    epi = load_epigraph_decisions(p)
    epi_bad = []
    emph, identical = [], []
    forbidden = cfg.get("forbidden_chars", {})
    eng_words = set(cfg.get("english_markers", []))
    lo, hi = cfg.get("ratio_bounds", [0.75, 1.8])
    min_chars = cfg.get("ratio_min_chars", 80)

    for pid, kind, smd in src_pars:
        if pid not in tgt_map:
            continue
        tkind, tmd = tgt_map[pid]
        if kind == "s":
            if tmd.strip() != SCENE_MD:
                scene.append(pid)
            continue
        if not tmd.strip():
            empty.append(pid)
            continue
        if tmd.strip() == PLACEHOLDER:
            placeholders.append(pid)
            if epi is not None and epi.get(pid) != "original":
                epi_bad.append("%s: segnaposto, ma in docs/epigraphs.tsv la decisione è %s"
                               % (pid, epi.get(pid) or "assente"))
            continue
        if epi is not None and epi.get(pid) == "original":
            epi_bad.append("%s: decisione original in docs/epigraphs.tsv, manca il segnaposto" % pid)
        if PLACEHOLDER in tmd:
            placeholder_bad.append(pid)
        for ch, label in forbidden.items():
            if ch in tmd:
                forb.append("%s: %s" % (pid, label))
        splain, tplain = plain_from_md(smd), plain_from_md(tmd)
        if len(splain) >= min_chars:
            r = len(tplain) / max(1, len(splain))
            ratios.append(r)
            if r < lo or r > hi:
                ratio_out.append("%s: %.2f" % (pid, r))
        toks = re.findall(r"[a-z]+", tplain.lower())
        n_eng = sum(1 for t in toks if t in eng_words)
        if n_eng >= cfg.get("english_flag_threshold", 3):
            english.append("%s: %d parole inglesi frequenti" % (pid, n_eng))
        if tmd.strip() == smd.strip() and len(splain) > 20:
            identical.append(pid)
        if count_emphasis(smd) != count_emphasis(tmd):
            emph.append(pid)
        for g in glossary:
            if g["_re_en"].search(splain) and not g["_re_it"].search(tplain):
                gloss_miss.append("%s: %s -> atteso %s" % (
                    pid, g.get("term_en", "?"), g.get("rendering_it", "?")))

    gates["empty"] = empty
    gates["scene_breaks"] = scene
    gates["forbidden_chars"] = forb
    gates["placeholder_misuse"] = placeholder_bad
    gates["epigraph_decisions"] = epi_bad
    flags["ratio_out_of_bounds"] = ratio_out
    flags["english_residue"] = english
    flags["glossary_misses"] = gloss_miss
    flags["emphasis_count_differs"] = emph
    flags["identical_to_source"] = identical
    res["placeholders"] = placeholders
    res["ratio_median"] = round(statistics.median(ratios), 3) if ratios else None
    res["paragraphs"] = len(src_pars)

    if stage == "final":
        dpath = tdir.parent / "draft" / (cid + ".md")
        if dpath.exists():
            dpars, _ = parse_chunk_file(dpath)
            dmap = {a: c for a, b, c in dpars}
            text_pids = [a for a, b, _ in src_pars if b != "s"]
            changed = sum(1 for pid in text_pids
                          if pid in dmap and pid in tgt_map and dmap[pid] != tgt_map[pid][1])
            res["changed_share"] = round(changed / max(1, len(text_pids)), 3)
    res["ok"] = not any(v for v in gates.values())
    return res


def print_check(res):
    print("Blocco %s (%s): %s" % (res["chunk"], res["stage"],
                                  "cancelli superati" if res["ok"] else "CANCELLI FALLITI"))
    for k, v in res["gates"].items():
        if v:
            print("  cancello %s: %d problemi" % (k, len(v)))
            for item in v[:8]:
                print("    " + item)
    if "paragraphs" not in res:
        return
    print("  paragrafi: %d; rapporto di lunghezza mediano IT/EN: %s" % (
        res["paragraphs"], res["ratio_median"]))
    if "changed_share" in res:
        print("  quota di paragrafi cambiati dalla bozza: %.0f%%" % (100 * res["changed_share"]))
    if res.get("placeholders"):
        print("  segnaposto [[ORIGINALE]]: " + ", ".join(res["placeholders"]))
    for k, v in res["flags"].items():
        if v:
            print("  da guardare, %s: %d" % (k, len(v)))
            for item in v[:8]:
                print("    " + str(item))


def cmd_check(args):
    p = paths(args.root)
    cfg = load_config(p)
    glossary = load_glossary(p)
    if args.chunk == "all":
        tdir = Path(args.dir) if args.dir else p[args.stage]
        cids = [c for c in chunk_ids(p) if (tdir / (c + ".md")).exists()]
        if not cids:
            die("nessun blocco tradotto in %s" % tdir)
    else:
        cids = [normalize_chunk_id(args.chunk, p)]
    all_ok, medians = True, []
    for cid in cids:
        res = check_chunk(p, cid, args.stage, cfg, glossary, args.dir)
        print_check(res)
        all_ok &= res["ok"]
        if res.get("ratio_median"):
            medians.append(res["ratio_median"])
        if args.save:
            p["checks"].mkdir(parents=True, exist_ok=True)
            out = p["checks"] / ("%s-%s.json" % (cid, args.stage))
            out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    if len(cids) > 1:
        lo, hi = cfg.get("ratio_median_expected", [1.0, 1.35])
        med = statistics.median(medians) if medians else None
        print("\nRiepilogo: %d blocchi, cancelli %s; mediana dei rapporti %s "
              "(intervallo atteso %.2f-%.2f)." % (
                  len(cids), "tutti superati" if all_ok else "NON tutti superati",
                  "%.3f" % med if med else "n.d.", lo, hi))
    return 0 if all_ok else 1


def cmd_coverage(args):
    p = paths(args.root)
    cid = normalize_chunk_id(args.chunk, p)
    src_pars, _ = parse_chunk_file(p["chunks"] / (cid + ".md"))
    f = Path(args.file) if args.file else p["review"] / (cid + "-findings.tsv")
    if not f.exists():
        die("manca %s" % f)
    lines = f.read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t") if lines else []
    if not head or head[0] != "pid":
        die("%s: la prima colonna dell'intestazione deve essere 'pid'" % f.name)
    seen, counts = set(), {}
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = dict(zip(head, line.split("\t")))
        seen.add(cells.get("pid", "").strip())
        if cells.get("verdict", "").strip() == "issue":
            sev = cells.get("severity", "?").strip() or "?"
            counts[sev] = counts.get(sev, 0) + 1
    needed = [pid for pid, kind, _ in src_pars if kind != "s"]
    missing = [pid for pid in needed if pid not in seen]
    print("Rilievi per gravità: " + (", ".join("%s=%d" % kv for kv in sorted(counts.items()))
                                     or "nessuno"))
    if missing:
        print("CANCELLO copertura della revisione: FALLITO, %d paragrafi non esaminati: %s" % (
            len(missing), ", ".join(missing[:20])))
        return 1
    print("CANCELLO copertura della revisione: superato (%d paragrafi esaminati)." % len(needed))
    return 0


def cmd_glossary(args):
    """Occurrences of every glossary entry in the source and, if present, in the translation."""
    p = paths(args.root)
    g = p["glossary"]
    if not g.exists():
        die("manca docs/glossary.tsv")
    lines = g.read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t")
    for col in ("id", "term_en", "match_en", "rendering_it", "match_it", "status"):
        if col not in head:
            die("glossario: manca la colonna %s" % col)
    src = []
    for f in sorted(p["chunks"].glob("*.md")):
        pars, _ = parse_chunk_file(f)
        src += [(f.stem, pid, plain_from_md(md)) for pid, kind, md in pars]
    tdir = p[args.stage]
    tgt = {}
    for f in sorted(tdir.glob("*.md")):
        pars, _ = parse_chunk_file(f)
        for pid, kind, md in pars:
            tgt[pid] = plain_from_md(md)
    bad = 0
    print("id\tstatus\tsource_pars\tfirst_chunk\ttranslated_pars\tmatching_it\tterm")
    for n, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        cells = line.split("\t")
        row = dict(zip(head, cells + [""] * (len(head) - len(cells))))
        try:
            re_en = re.compile(row["match_en"], re.I) if row["match_en"].strip() else None
            re_it = re.compile(row["match_it"], re.I) if row["match_it"].strip() else None
        except re.error as e:
            print("riga %d: espressione non valida (%s)" % (n, e))
            bad += 1
            continue
        if re_en is None:
            print("riga %d (%s): manca match_en" % (n, row["id"]))
            bad += 1
            continue
        hits = [(c, pid) for c, pid, t in src if re_en.search(t)]
        done = [pid for c, pid in hits if pid in tgt]
        ok_it = sum(1 for pid in done if re_it and re_it.search(tgt[pid]))
        print("%s\t%s\t%d\t%s\t%d\t%d\t%s" % (row["id"], row["status"], len(hits),
                                           hits[0][0] if hits else "-", len(done), ok_it,
                                           row["term_en"]))
        if not hits:
            bad += 1
    if bad:
        print("CANCELLO glossario: FALLITO (%d voci senza occorrenze o non valide)." % bad)
        return 1
    print("CANCELLO glossario: superato (ogni voce trova il termine nella sorgente).")
    return 0


def cmd_status(args):
    p = paths(args.root)
    if not p["index"].exists():
        die("manca source/index.tsv")
    rows = [l.split("\t") for l in p["index"].read_text(encoding="utf-8").splitlines()[1:] if l]
    print("chunk  words  draft final review  part")
    for cid, part, _, _, _, w in rows:
        flags = []
        for key in ("draft", "final"):
            flags.append("x" if (p[key] / (cid + ".md")).exists() else ".")
        rv = "x" if (p["review"] / (cid + "-findings.tsv")).exists() else "."
        print("%-5s  %5s    %s     %s     %s     %s" % (cid, w, flags[0], flags[1], rv, part))
    if args.per_session:
        print("\nRaggruppamento suggerito (circa %d parole per sessione):" % args.per_session)
        groups, cur, words = [], [], 0
        for cid, part, _, _, _, w in rows:
            if cur and words + int(w) > args.per_session * 1.15:
                groups.append((cur, words))
                cur, words = [], 0
            cur.append(cid)
            words += int(w)
        if cur:
            groups.append((cur, words))
        for n, (g, w) in enumerate(groups, 1):
            print("  sessione %d: blocchi %s-%s (%d blocchi, %d parole)" % (
                n, g[0], g[-1], len(g), w))
    return 0


# ------------------------------------------------------------------ build

def typography(md):
    md = md.replace("...", "…")
    md = re.sub(r"(?<!\\)'", "’", md)
    return md


def load_figures(p):
    """source/figures.tsv: images that belong to the book (after_id, file)."""
    figs = {}
    if not p["figures"].exists():
        return figs
    for n, line in enumerate(p["figures"].read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("after_id"):
            continue
        cells = line.split("\t")
        if len(cells) != 2:
            die("figures.tsv riga %d: servono 2 colonne (after_id, file)" % n)
        if not (p["original"] / cells[1].strip()).is_file():
            die("figures.tsv riga %d: manca source/original/%s" % (n, cells[1].strip()))
        figs.setdefault(cells[0].strip(), []).append(cells[1].strip())
    return figs


def assemble(p, cids, translation_dir, allow_draft, cfg, glossary):
    src_map = {}
    for r in read_jsonl(p["paragraphs"]):
        src_map[r["id"]] = r
    figures = load_figures(p)
    out_pars = []
    for cid in cids:
        candidates = []
        if translation_dir:
            candidates.append((Path(translation_dir), "final"))
        else:
            candidates.append((p["final"], "final"))
            if allow_draft:
                candidates.append((p["draft"], "draft"))
        chosen = None
        for d, stage in candidates:
            if (d / (cid + ".md")).exists():
                chosen = (d, stage)
                break
        if not chosen:
            die("blocco %s: nessuna traduzione disponibile" % cid)
        res = check_chunk(p, cid, chosen[1], cfg, glossary, chosen[0])
        if not res["ok"]:
            print_check(res)
            die("blocco %s: cancelli falliti, EPUB non costruito" % cid, 1)
        pars, _ = parse_chunk_file(chosen[0] / (cid + ".md"))
        for pid, kind, md in pars:
            if md.strip() == PLACEHOLDER:
                md = src_map[pid]["md"]
            elif kind != "s":
                md = typography(md)
            layout = src_map.get(pid, {}).get("layout", "") if kind == "t" else ""
            out_pars.append((kind, md, layout))
            for fig in figures.get(pid, []):
                out_pars.append(("img", fig, ""))
    levels = [int(k[1]) for k, _, _ in out_pars if k.startswith("h")]
    shift = (min(levels) - 1) if levels else 0
    lines = []
    for kind, md, layout in out_pars:
        if kind.startswith("h"):
            lines.append("#" * (int(kind[1]) - shift) + " " + md)
        elif kind == "q":
            lines.append("\n".join("> " + l for l in md.split("\n")))
        elif kind == "s":
            lines.append(SCENE_MD)
        elif kind == "img":
            lines.append("::: {.center .figure}\n![](%s)\n:::" % md)
        elif layout:
            # pandoc fenced div: the classes are styled in epub/style.css
            lines.append("::: {%s}\n%s\n:::" % (
                " ".join("." + t for t in layout.split()), md))
        else:
            lines.append(md)
        lines.append("")
    note = p["epub"] / "note.md"
    if note.exists():
        lines.append(note.read_text(encoding="utf-8").strip())
        lines.append("")
    return "\n".join(lines)


def run_pandoc(book_md, out, p):
    if not shutil.which("pandoc"):
        die("pandoc non installato")
    ver = subprocess.run(["pandoc", "--version"], capture_output=True, text=True).stdout
    m = re.search(r"pandoc\S*\s+(\d+)\.(\d+)", ver)
    major = int(m.group(1)) if m else 2
    split_flag = "--split-level=1" if major >= 3 else "--epub-chapter-level=1"
    cmd = ["pandoc", str(book_md), "-f", "markdown-smart", "-t", "epub3",
           "--toc", "--toc-depth=1", split_flag, "-o", str(out),
           "--resource-path", str(p["original"])]
    cover = p["epub"] / "cover.jpg"
    if cover.exists():
        cmd += ["--epub-cover-image", str(cover)]
    meta = p["epub"] / "metadata.yaml"
    css = p["epub"] / "style.css"
    if meta.exists():
        cmd += ["--metadata-file", str(meta)]
    if css.exists():
        cmd += ["--css", str(css)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr)
        die("pandoc ha restituito un errore", 1)
    if r.stderr.strip():
        print("Avvisi di pandoc:\n" + r.stderr.strip())


def epub_gate(out):
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        bad = z.testzip()
    if bad or names[0] != "mimetype":
        print("CANCELLO formato: FALLITO (archivio EPUB non valido)")
        return 1
    if shutil.which("epubcheck"):
        r = subprocess.run(["epubcheck", str(out)], capture_output=True, text=True)
        tail = (r.stdout + r.stderr).strip().splitlines()[-6:]
        print("epubcheck:\n  " + "\n  ".join(tail))
        if r.returncode != 0:
            print("CANCELLO formato: FALLITO (epubcheck)")
            return 1
        print("CANCELLO formato: superato (epubcheck senza errori).")
        return 0
    print("Nota: epubcheck non installato. Archivio valido, ma il cancello del formato "
          "non è verificato del tutto.")
    return 0


def cmd_build(args):
    p = paths(args.root)
    cfg = load_config(p)
    glossary = load_glossary(p)
    cids = chunk_ids(p)
    if args.chunks:
        cids = [normalize_chunk_id(c, p) for c in args.chunks.split(",")]
    book = assemble(p, cids, args.dir, args.allow_draft, cfg, glossary)
    p["build"].mkdir(parents=True, exist_ok=True)
    stem = Path(args.out).stem if args.out else "Blindsight-it"
    book_md = p["build"] / (stem + ".md")
    book_md.write_text(book, encoding="utf-8")
    out = Path(args.out) if args.out else p["build"] / "Blindsight-it.epub"
    run_pandoc(book_md, out, p)
    print("EPUB scritto: %s (%d blocchi)" % (out, len(cids)))
    return epub_gate(out)


def cmd_blind(args):
    p = paths(args.root)
    key_path = p["comparison"] / ".key.json"
    if args.reveal:
        if not key_path.exists():
            die("nessuna chiave: il confronto non è stato preparato")
        print(key_path.read_text(encoding="utf-8"))
        return 0
    if not (args.a and args.b and args.chunks):
        die("servono --a, --b e --chunks")
    cfg, glossary = load_config(p), load_glossary(p)
    cids = [normalize_chunk_id(c, p) for c in args.chunks.split(",")]
    p["comparison"].mkdir(parents=True, exist_ok=True)
    rng = random.SystemRandom()
    swap = rng.random() < 0.5
    mapping = {"X": args.b if swap else args.a, "Y": args.a if swap else args.b}
    p["build"].mkdir(parents=True, exist_ok=True)
    for label, d in mapping.items():
        book = assemble(p, cids, d, False, cfg, glossary)
        md = p["build"] / ("pilota-%s.md" % label)
        md.write_text(book, encoding="utf-8")
        run_pandoc(md, p["build"] / ("pilota-%s.epub" % label), p)
    key_path.write_text(json.dumps(mapping, indent=1), encoding="utf-8")
    print("Scritti build/pilota-X.epub e build/pilota-Y.epub. La chiave è in "
          "comparison/.key.json: non aprirla prima di aver scelto.")
    return 0


# ------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help="project root")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("extract")
    s.add_argument("html")
    s.add_argument("--show", type=int, default=25)
    s.set_defaults(fn=cmd_extract)

    s = sub.add_parser("chunk")
    s.add_argument("--start", required=True)
    s.add_argument("--end", required=True)
    s.add_argument("--words", type=int, default=2500)
    s.add_argument("--force", action="store_true")
    s.add_argument("--add-headings", help="TSV of headings missing from the HTML")
    s.add_argument("--exclude", help="TSV of id ranges inside the interval that are not the book")
    s.set_defaults(fn=cmd_chunk)

    s = sub.add_parser("verify")
    s.set_defaults(fn=cmd_verify)

    s = sub.add_parser("check")
    s.add_argument("chunk", help="chunk number or 'all'")
    s.add_argument("--stage", choices=["draft", "final"], required=True)
    s.add_argument("--dir", help="alternative translation directory (pilot B)")
    s.add_argument("--save", action="store_true")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("coverage")
    s.add_argument("chunk")
    s.add_argument("--file")
    s.set_defaults(fn=cmd_coverage)

    s = sub.add_parser("glossary")
    s.add_argument("--stage", choices=["draft", "final"], default="final")
    s.set_defaults(fn=cmd_glossary)

    s = sub.add_parser("status")
    s.add_argument("--per-session", type=int, default=0)
    s.set_defaults(fn=cmd_status)

    s = sub.add_parser("build")
    s.add_argument("--chunks", help="comma-separated chunk numbers (default: all)")
    s.add_argument("--dir", help="take every chunk from this directory")
    s.add_argument("--allow-draft", action="store_true")
    s.add_argument("--out")
    s.set_defaults(fn=cmd_build)

    s = sub.add_parser("blind")
    s.add_argument("--a")
    s.add_argument("--b")
    s.add_argument("--chunks")
    s.add_argument("--reveal", action="store_true")
    s.set_defaults(fn=cmd_blind)

    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
