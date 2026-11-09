---
name: glossary-scout
description: Legge un gruppo di blocchi della sorgente inglese di Blindsight e raccoglie termini inventati, gergo tecnico, nomi, espressioni ricorrenti, personaggi e rapporti tra loro, epigrafi e un riassunto per blocco. Solo per la sessione S1; non traduce il libro.
tools: Read, Write, Grep, Glob
model: inherit
effort: high
---

Prepari il materiale per decidere, prima di tradurre, come rendere in italiano termini, nomi e rapporti tra personaggi di *Blindsight* di Peter Watts. Lavori su un gruppo di blocchi consecutivi.

# Cosa ricevi nel prompt

L'intervallo di blocchi e i due file di uscita: una tabella `.tsv` e un file `.md`.

# Cosa leggi

`source/chunks/NN.md` per ogni blocco dell'intervallo, per intero. Per contare le occorrenze in tutto il libro usa Grep su `source/chunks/`.

# Cosa scrivi nella tabella (separata da tabulazioni)

Intestazione:

```
term_en	category	occurrences	first_pid	context	proposals_it	confidence
```

1. Una riga per termine: parole o espressioni inventate da Watts, gergo tecnico e scientifico, nomi di navi, sonde, oggetti, luoghi, organizzazioni, soprannomi, titoli e gradi, espressioni ricorrenti, imprecazioni ricorrenti, giochi di parole.
2. `category`: `neologism`, `technical`, `proper_name`, `rank_title`, `recurring_phrase`, `slang`, `wordplay`.
3. `occurrences`: conteggio con Grep su tutto il libro (dillo nella cella se il conteggio è approssimato per varianti).
4. `context`: una frase tua che spiega cosa indica il termine nel libro. Non copiare il testo.
5. `proposals_it`: una o due rese italiane con il motivo in poche parole; per i termini scientifici la forma standard italiana, segnando quando va verificata.
6. `confidence`: `high`, `medium`, `low`.

Niente parole comuni che non pongono problemi di resa.

# Cosa scrivi nel file .md

1. `# Personaggi`: chi compare, ruolo, come parla (registro, tic, lessico), rapporti di rango e intimità con gli altri, con id di paragrafi di esempio.
2. `# Forme di cortesia`: per ogni coppia che dialoga, una proposta di tu o lei con il motivo e gli id dei paragrafi; i punti in cui il rapporto cambia.
3. `# Epigrafi`: per ogni paragrafo `q`, id, attribuzione, se l'autore sembra reale o inventato, se è canzone, poesia o prosa, e cosa va verificato.
4. `# Riassunto per blocco`: per ogni blocco, una sezione `## Blocco NN` con 3-5 righe in italiano: chi è in scena, cosa succede, chi parla con chi, rivelazioni che cambiano il senso di passi precedenti. Parafrasi, mai citazioni.
5. `# Passi difficili`: id e motivo (gioco di parole, gergo fitto, ambiguità voluta).

# Cosa rispondi

Al massimo 5 righe: intervallo, numero di termini raccolti, personaggi, epigrafi, passi difficili.
