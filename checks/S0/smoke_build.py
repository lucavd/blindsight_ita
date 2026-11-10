"""One-off S0 check: build an EPUB from the whole English text, to prove that
the build works on the real book (figure, layouts, epubcheck) before any
translation exists. Only the characters forbidden in a translation are
replaced. In the project it writes only in build/, which is not versioned. Usage:
    python3 checks/S0/smoke_build.py <project root> <empty work directory>
"""
import re, subprocess, sys
from pathlib import Path
root, work = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(root / "tools"))
import blindsight as bt
fake = work / "fake"
fake.mkdir(parents=True, exist_ok=True)
for f in sorted((root / "source" / "chunks").glob("*.md")):
    pars, err = bt.parse_chunk_file(f)
    assert not err, err
    new = []
    for pid, kind, md in pars:
        if kind != "s":
            md = re.sub(r'"([^"]*)"', "«\\1»", md).replace('"', "»")
            md = md.replace("—", "–").replace("…", "...")
        new.append((pid, kind, md))
    bt.write_chunk(fake / f.name, "<!-- smoke test -->", new)
r = subprocess.run([sys.executable, str(root / "tools" / "blindsight.py"), "--root", str(root),
                    "build", "--dir", str(fake), "--out", str(work / "smoke.epub")],
                   capture_output=True, text=True)
print("\n".join(l for l in (r.stdout + r.stderr).splitlines() if "JAVA_TOOL_OPTIONS" not in l))
sys.exit(r.returncode)
