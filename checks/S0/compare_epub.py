"""One-off S0 check: the novel in the chunks against the reference EPUB
(reference/PeterWatts_Blindsight-v1.01-formatted-by-Ellen-Herzfeld.epub).

Counts letters and digits part by part: word counts depend on how inline
tags split words, letter counts do not. Usage:
    python3 checks/S0/compare_epub.py <project root>
"""
import json, re, sys, warnings, zipfile
from pathlib import Path
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")
root = Path(sys.argv[1])
rows = [json.loads(l) for l in open(root / "source" / "paragraphs.jsonl", encoding="utf-8")]
idx = {r["id"]: i for i, r in enumerate(rows)}
z = zipfile.ZipFile(root / "reference" / "PeterWatts_Blindsight-v1.01-formatted-by-Ellen-Herzfeld.epub")
ours = lambda a, b: " ".join(r["plain"] for r in rows[idx[a]:idx[b] + 1])
def theirs(*names):
    return " ".join(BeautifulSoup(z.read("OEBPS/" + n).decode("utf-8"), "lxml").body.get_text(" ")
                    for n in names)
parts = [
    ("dedica ed epigrafi iniziali", ours("p00003", "p00004") + " " + ours("p00013", "p00016"),
     theirs("00-dedication.xhtml", "00-epigraph.xhtml")),
    ("Prologue", ours("p00017", "p00064"), theirs("00-prologue.xhtml")),
    ("Theseus", ours("p00065", "p01313"), theirs("01-theseus.xhtml")),
    ("Rorschach", ours("p01314", "p03649"), theirs("02a-rorschach.xhtml", "02b-rorschach.xhtml")),
    ("Charybdis", ours("p03650", "p03694"), theirs("03-charybdis.xhtml")),
    ("Acknowledgments", ours("p03695", "p03699"), theirs("04-acknowledgments.xhtml")),
    ("Notes and References", ours("p03700", "p03756") + " " + ours("p03803", "p03946"),
     theirs("05-notes-references.xhtml")),
]
letters = lambda s: len(re.sub(r"[^A-Za-z]", "", s))
digits = lambda s: len(re.sub(r"[^0-9]", "", s))
print("%-28s %9s %9s %7s | %6s %6s" % ("parte", "lettere", "EPUB", "scarto", "cifre", "EPUB"))
same = 0
for name, a, b in parts:
    d = letters(a) - letters(b)
    same += d == 0
    print("%-28s %9d %9d %+7d | %6d %6d" % (name, letters(a), letters(b), d, digits(a), digits(b)))
print("parti con lo stesso numero di lettere: %d su %d" % (same, len(parts)))
notes = [r for r in rows[idx["p03803"]:idx["p03946"] + 1]]
print("note finali nei blocchi: %d, la piu' corta di %d parole"
      % (len(notes), min(r["words"] for r in notes)))
w = lambda a, b: sum(r["words"] for r in rows[idx[a]:idx[b] + 1])
print("ultimo blocco: fine del saggio (p03740-p03756) %d parole, note finali (p03803-p03946) %d parole"
      % (w("p03740", "p03756"), w("p03803", "p03946")))
