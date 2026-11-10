"""One-off S0 check: every source paragraph, rendered by pandoc exactly as the
build would, must show the same text as the HTML page (no stray markup)."""
import json, re, subprocess, sys
from pathlib import Path
from bs4 import BeautifulSoup
root = Path(sys.argv[1])
sys.path.insert(0, str(root / "tools"))
import blindsight as bt
src = {r["id"]: r for r in bt.read_jsonl(root / "source" / "paragraphs.jsonl")}
pars = []
for f in sorted((root / "source" / "chunks").glob("*.md")):
    p, err = bt.parse_chunk_file(f)
    assert not err, err
    pars += p
doc = []
for pid, kind, md in pars:
    if kind == "s":
        continue
    doc.append("::: {#%s}\n%s\n:::\n" % (pid, md))
html = subprocess.run(["pandoc", "-f", "markdown-smart", "-t", "html"],
                      input="\n".join(doc), capture_output=True, text=True, check=True).stdout
soup = BeautifulSoup(html, "lxml")
squash = lambda s: re.sub(r"\s+", "", s)
bad, n = [], 0
for pid, kind, md in pars:
    if kind == "s":
        continue
    n += 1
    div = soup.find(id=pid)
    got = squash(div.get_text("")) if div else None
    want = squash(src[pid]["plain"])
    if got != want:
        bad.append((pid, want[:60], (got or "MANCA")[:60]))
tags = {}
for t in soup.find_all(True):
    tags[t.name] = tags.get(t.name, 0) + 1
print("paragrafi controllati: %d; diversi dal testo della pagina: %d" % (n, len(bad)))
for b in bad[:15]:
    print("  %s\n    pagina: %s\n    pandoc: %s" % b)
print("tag prodotti da pandoc:", dict(sorted(tags.items())))
sys.exit(1 if bad else 0)
