---
type: Session
title: "F: coerenza sull'intero libro ed EPUB"
description: Controlla che termini, nomi, forme di cortesia e voce siano coerenti dall'inizio alla fine, fa una controprova a campione sull'originale e costruisce l'EPUB definitivo.
model: opus
status: todo
pi_approval: pending
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

# Cosa fa

Ogni blocco è stato rivisto da solo. Questa sessione guarda il libro intero: le incoerenze che un revisore di blocco non può vedere (un personaggio che passa dal tu al lei senza motivo, un termine reso in due modi in parti diverse, un nome scritto in due modi), poi costruisce l'EPUB.

# Dubbi ricevuti

(compilati dalle sessioni precedenti)

# Procedura

1. `python3 tools/blindsight.py check all --stage final`: tutti i cancelli superati su tutti i blocchi.
2. `python3 tools/blindsight.py glossary --stage final`: per ogni voce approvata, i paragrafi tradotti che contengono il termine inglese devono contenere la resa italiana. Spiegare o correggere ogni scarto.
3. Lettura di coerenza. Per ciascuna parte del libro lanciare un sotto-agente `reviewer` in modalità coerenza (istruzioni nel prompt: leggere solo l'italiano dei blocchi finali della parte, con `docs/characters.md` e il glossario; registrare in `review/coherence-<parte>.tsv` incoerenze di forme di cortesia, nomi, termini, tempi verbali del narratore, ripetizioni di formule; non proporre riscritture di stile). Poi, per ogni rilievo, un sotto-agente `editor` sul blocco interessato applica la correzione verificandola sull'inglese.
4. Controprova a campione: 20 paragrafi scelti a caso con un seme fissato (per esempio `python3 -c "import random; random.seed(20261109); ..."` sugli id dei paragrafi di testo), letti dall'agente in inglese e in italiano. Ogni errore trovato è un dubbio da chiudere; più di 2 errori di senso su 20 riaprono la revisione delle parti coinvolte.
5. `python3 tools/blindsight.py build`: EPUB definitivo in `build/Blindsight-it.epub`, con `epubcheck`.
6. Controllo dell'EPUB: indice con le parti nell'ordine giusto, epigrafi in originale al loro posto, nota sulla traduzione in fondo, nessun marcatore o segnaposto rimasto (`unzip -p build/Blindsight-it.epub | grep -c "ORIGINALE\|<!-- p"` deve dare 0).
7. Riassunto e chiusura. Messaggio finale con il percorso dell'EPUB e come copiarlo sull'e-reader.

# Cancelli

1. `verify` superato.
2. `check all --stage final` superato su tutti i blocchi.
3. `build` superato, `epubcheck` senza errori.
4. Nessun marcatore o segnaposto nell'EPUB.

# Previsioni

| quantità | atteso | intervallo di rilevanza | se è fuori |
|---|---|---|---|
| errori di senso nella controprova a campione | 0 | da 0 a 2 su 20 | sopra: si riapre la revisione delle parti coinvolte |
| incoerenze trovate nella lettura di coerenza, sull'intero libro | 15 | da 0 a 40 | sopra: un problema sistematico (glossario o forme di cortesia non applicati), da capire prima di correggere |

# In breve

(da scrivere alla chiusura)

# Dubbi rinviati

(nessuno finora)

# Da dove vengono i numeri del riassunto

(da compilare)
