---
type: Plan
title: Piano delle sessioni
description: Sequenza delle sessioni con modello, compiti, prodotti, tempi stimati e lavoro richiesto al PI.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

# Il lavoro in tre passaggi

Ogni blocco di circa 2.500 parole passa per tre mani diverse, ciascuna un sotto-agente nuovo che non ha visto il lavoro precedente.

1. Il traduttore scrive la prima stesura, con guida di stile, glossario, scheda dei personaggi, riassunto della trama e la fine del blocco precedente come contesto.
2. Il revisore confronta ogni paragrafo italiano con l'inglese e registra omissioni, errori di senso, sfumature perse, registro, terminologia, forme di cortesia, calchi. Non tocca il testo.
3. Il redattore legge prima il blocco solo in italiano, come un lettore; poi applica i rilievi del revisore (accettando o respingendo con una ragione) e i propri interventi di lingua, controllando ognuno sull'inglese prima di applicarlo.

Dopo ogni passaggio girano i controlli automatici. Alla fine una sessione di coerenza sull'intero libro e la costruzione dell'EPUB.

# Sessioni

Una sessione è una chat di Claude Code, aperta nella cartella del progetto con il modello indicato. Il numero esatto delle sessioni di traduzione e di revisione lo fissa S0 dopo aver diviso il testo; qui sotto la stima per circa 100 mila parole e 40 blocchi.

| sessione | modello | cosa fa | cosa produce | tempo macchina | cosa fai tu |
|---|---|---|---|---|---|
| S0 | Sonnet 5.5 (`claude --model sonnet`) | scarica la sorgente, la divide in blocchi, verifica che non si perda nulla, crea le sessioni di traduzione e revisione | blocchi, indice, impronte | 30-45 minuti | nulla, leggi il riassunto |
| S1 | Opus 5.5 (`claude --model opus`) | legge tutto il libro, costruisce glossario, scheda dei personaggi, elenco delle epigrafi; propone le scelte tipografiche | glossario, personaggi, epigrafi, guida completa | 1,5-2,5 ore | decidi 4-6 punti (30 minuti) |
| S2 | Opus 5.5 | pilota: due blocchi con l'intero ciclo, uno facile e il più difficile del libro | due blocchi finiti, EPUB di prova | 1-1,5 ore | leggi l'EPUB di prova e dai indicazioni (1 ora) |
| S2b (facoltativa) | Fable 5.2 (`claude --model fable`), se il tuo piano lo include | stessi due blocchi con l'altro modello; confronto alla cieca | due EPUB anonimi da confrontare | 1-1,5 ore | li leggi senza sapere chi è chi e scegli (1 ora) |
| T1-T4 | Opus 5.5, scelto dal PI nel confronto alla cieca | prima stesura, circa 25 mila parole per sessione | prime stesure | 1,3-1,7 ore ciascuna (misura del pilota) | nulla, salvo decisioni rare |
| R1-R6 | Opus 5.5, scelto dal PI nel confronto alla cieca | revisione bilingue e redazione, circa 16 mila parole per sessione | versioni finali | 1,1-1,4 ore ciascuna (misura del pilota) | nulla, salvo decisioni rare |
| F | Opus 5.5 | coerenza sull'intero libro (termini, nomi, tu e lei), EPUB, controllo del formato | l'EPUB | 1-2 ore | leggi il libro |
| C (facoltativa) | Opus 5.5 | correzioni dalle tue note di lettura | EPUB corretto | dipende dalle note | annoti mentre leggi |

Totale stimato: tra 15 e 25 ore di macchina in 14 sessioni (16 con le facoltative). Non è una giornata. La stima iniziale veniva da ipotesi sul tempo di un sotto-agente per blocco; il pilota l'ha misurata, come sotto.

Tempi misurati nel pilota (S2), su 2 blocchi (il 01, 1.655 parole, e il 18, 3.532 parole: 5.187 parole in tutto), con Opus 5.5. Durata dei sotto-agenti: traduttore 5,5 e 7,8 minuti, revisore 3,1 e 4,6, redattore 2,7 e 4,6; i tre passaggi insieme 11,3 e 17,1 minuti per blocco. Per mille parole: 2,6 minuti di traduttore e 2,9 di revisore più redattore. Il coordinamento della chat principale (controlli, spiegazione delle segnalazioni, commit) ha aggiunto circa un minuto per passaggio e per blocco. Da qui le stime della tabella: una sessione di traduzione (da 22 a 29 mila parole, da 7 a 12 blocchi) richiede da 1,3 a 1,7 ore, contando un quarto d'ora per apertura e chiusura (stima, non misura); una di revisione (da 14 a 18 mila parole, da 5 a 8 blocchi) da 1,1 a 1,4 ore. Per il resto del libro (99.452 parole, 39 blocchi) le sessioni di traduzione e di revisione fanno circa 14 ore, più la sessione finale: il totale resta dentro la stima iniziale, verso il basso. Due blocchi sono pochi: la stima vale per blocchi simili a questi e va rivista dopo la prima sessione di traduzione.

Tempi misurati nel confronto alla cieca (S2b), sugli stessi 2 blocchi, con Fable 5.2. Durata dei sotto-agenti: traduttore 6,6 e 9,7 minuti, revisore 7,0 e 10,3, redattore 4,9 e 7,5; i tre passaggi insieme 18,5 e 27,5 minuti per blocco, il 62% in più del pilota. Per mille parole: 3,15 minuti di traduttore e 5,70 di revisore più redattore. Con la stessa formula il resto del libro avrebbe richiesto circa 19 ore invece di 14. Il PI ha scelto la versione di Opus, quindi la stima del piano resta quella del pilota.

Tempi misurati nella prima sessione di traduzione (T1), su 10 blocchi (dal 02 all'11, 26.466 parole), con Opus 5.5. Durata del traduttore da 5,7 a 9,3 minuti per blocco, 74,5 minuti in tutto: 2,8 minuti per mille parole, contro i 2,6 del pilota. Dal primo lancio all'ultimo controllo sono passati 89 minuti, quindi il coordinamento della chat principale (controlli, segnalazioni, voci del glossario, commit) ha preso circa 14 minuti, poco più di un minuto per blocco come nel pilota. Con apertura e chiusura la sessione resta dentro la stima di 1,3-1,7 ore; la stima per le altre tre sessioni di traduzione non cambia.

Tempi misurati nella seconda sessione di traduzione (T2), su 10 blocchi (dal 12 al 22 senza il 18, 22.667 parole), con Opus 5.5. Durata del traduttore da 4,2 a 7,9 minuti per blocco, 62,9 minuti in tutto: 2,8 minuti per mille parole, come in T1. Dal primo lancio all'ultimo controllo sono passati 75 minuti, quindi il coordinamento ha preso circa 13 minuti, poco più di un minuto per blocco. La stima per le ultime due sessioni di traduzione non cambia.

Tempi misurati nella terza sessione di traduzione (T3), su 12 blocchi (dal 23 al 34, 28.540 parole), con Opus 5.5. Durata del traduttore da 5,2 a 7,6 minuti per blocco, 74,7 minuti in tutto: 2,6 minuti per mille parole, un po' meno dei 2,8 di T1 e T2. Dal primo lancio all'ultimo controllo sono passati 88 minuti, quindi il coordinamento ha preso circa 13 minuti, poco più di un minuto per blocco. La stima per l'ultima sessione di traduzione non cambia.

Tempi misurati nell'ultima sessione di traduzione (T4), su 7 blocchi (dal 35 al 41, 21.779 parole), con Opus 5.5. Durata del traduttore da 6,1 a 9,5 minuti per blocco, 55,3 minuti in tutto: 2,5 minuti per mille parole, ma il blocco 41 è quasi tutto note bibliografiche da ricopiare; senza di lui 2,8, come in T1 e T2. Dal primo lancio all'ultimo controllo sono passati 64 minuti, quindi il coordinamento ha preso circa 9 minuti, poco più di un minuto per blocco. La stima per le sessioni di revisione resta quella del pilota.

Tempi misurati nella prima sessione di revisione (R1), su 6 blocchi (dal 02 al 07, 16.338 parole), con Opus 5.5. Revisore da 2,8 a 4,1 minuti per blocco, redattore da 2,3 a 3,2; insieme 37,1 minuti, 2,3 minuti per mille parole (nel pilota 2,9). Dal primo lancio all'ultimo controllo 45 minuti, compresa una seconda lettura del blocco 02 (revisore sulla versione finale, verifica dei rilievi medi, redattore sui fondati) che è costata 4,6 minuti, 1,4 minuti per mille parole. Una sessione di revisione dura quindi meno della stima del pilota; con la seconda lettura come passaggio fisso resterebbe dentro la stima.

# Perché questi modelli

Sonnet 5.5 solo per S0, che è lavoro meccanico (scaricare, dividere, contare) dove un modello più grande non cambia il risultato.

Opus 5.5 per tutto ciò che richiede giudizio linguistico. Fable 5.2 è un modello di fascia superiore, ma non ho elementi per dire che traduca meglio questo libro, né so se il tuo piano lo include in Claude Code: per questo il pilota prevede un confronto alla cieca facoltativo. Il modello che vince il confronto si usa per tutte le sessioni di traduzione e di revisione, senza cambiarlo a metà, perché due modelli diversi in parti diverse del libro darebbero due voci diverse. Il confronto è stato fatto: il PI ha letto le due versioni anonime e ha scelto quella di Opus 5.5, più naturale in italiano e migliore nei dialoghi (decisione sulla scelta del confronto alla cieca, D-35).

# Il vincolo vero: i limiti d'uso

Il tempo di macchina conta meno dei limiti d'uso del tuo piano, che non conosco. Se una sessione si interrompe, si riprende in una nuova chat con lo stesso modello: il protocollo riparte dal primo blocco non completato, perché ogni blocco finito ha il suo commit.
