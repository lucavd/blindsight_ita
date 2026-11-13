---
type: Session
title: "C: correzioni dalle note di lettura (facoltativa)"
description: Applica le osservazioni che il PI annota leggendo l'EPUB, verificando ciascuna sull'inglese, e ricostruisce il libro.
model: opus
status: optional
pi_approval: pending
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

# Cosa fa

Il PI legge il libro e annota ciò che non lo convince in `docs/reading-notes.md`, una nota per riga, nella forma più comoda: la frase italiana (o un pezzo riconoscibile) e il commento. Questa sessione trova ogni passo, lo verifica sull'inglese e corregge.

Se il PI legge sul Kindle, porta le evidenziazioni e le note esportate dal Kindle (il contenuto del file `My Clippings.txt`, incollato in chat). La sessione, come primo passo, le trascrive in `docs/reading-notes.md`, una per riga, tenendo solo quelle di Blindsight; un'evidenziazione senza nota vale «rivedere questo passo» (decisione sulle note di lettura dal Kindle, D-90).

# Procedura

1. Per ogni nota: trovare il paragrafo con `grep` nei blocchi finali; leggere inglese e italiano.
2. Classificare: errore di traduzione, scelta di stile del PI, oppure nota su Watts (non c'è niente da correggere: dirlo).
3. Le correzioni si fanno con il sotto-agente `editor` sul blocco, passandogli le note di quel blocco. Se una nota riguarda un termine del glossario o una forma di cortesia, la correzione si estende a tutto il libro e si registra come decisione del PI.
4. `check` sui blocchi toccati, `build`, riassunto con una riga per nota (cosa si è fatto), chiusura.

# Cancelli

1. `verify` superato.
2. `check --stage final` superato sui blocchi toccati.
3. `build` superato.

# In breve

(da scrivere alla chiusura)
