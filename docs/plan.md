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
| T1-T4 | il modello scelto nel pilota | prima stesura, circa 25 mila parole per sessione | prime stesure | 1-1,5 ore ciascuna | nulla, salvo decisioni rare |
| R1-R6 | il modello scelto nel pilota | revisione bilingue e redazione, circa 16 mila parole per sessione | versioni finali | 1,5-2 ore ciascuna | nulla, salvo decisioni rare |
| F | Opus 5.5 | coerenza sull'intero libro (termini, nomi, tu e lei), EPUB, controllo del formato | l'EPUB | 1-2 ore | leggi il libro |
| C (facoltativa) | Opus 5.5 | correzioni dalle tue note di lettura | EPUB corretto | dipende dalle note | annoti mentre leggi |

Totale stimato: tra 15 e 25 ore di macchina in 14 sessioni (16 con le facoltative). Non è una giornata. La stima viene da ipotesi sul tempo di un sotto-agente per blocco (lettura di circa 30 mila token, scrittura di circa 7 mila), non da misure: la prima misura vera arriva dal pilota, e S2 aggiorna questa tabella.

# Perché questi modelli

Sonnet 5.5 solo per S0, che è lavoro meccanico (scaricare, dividere, contare) dove un modello più grande non cambia il risultato.

Opus 5.5 per tutto ciò che richiede giudizio linguistico. Fable 5.2 è un modello di fascia superiore, ma non ho elementi per dire che traduca meglio questo libro, né so se il tuo piano lo include in Claude Code: per questo il pilota prevede un confronto alla cieca facoltativo. Il modello che vince il confronto si usa per tutte le sessioni di traduzione e di revisione, senza cambiarlo a metà, perché due modelli diversi in parti diverse del libro darebbero due voci diverse.

# Il vincolo vero: i limiti d'uso

Il tempo di macchina conta meno dei limiti d'uso del tuo piano, che non conosco. Se una sessione si interrompe, si riprende in una nuova chat con lo stesso modello: il protocollo riparte dal primo blocco non completato, perché ogni blocco finito ha il suo commit.
