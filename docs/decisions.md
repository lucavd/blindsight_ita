---
type: DecisionLog
title: Decisioni
description: Decisioni del PI e decisioni tecniche dell'agente, una sezione ciascuna, numerate in ordine; una decisione superata resta, con il rimando a quella che la sostituisce.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

Formato di ogni voce: titolo con numero, poi Decisione, Motivazione, Deciso da (PI oppure agente), Data, Stato (valida, oppure superata da D-nn). Il numero si assegna al momento del commit: il primo libero.

Le decisioni da D-01 a D-07 sono state prese nella preparazione del pacchetto, prima della prima sessione. Il PI non ne ha riletto il testo. D-08 è del PI.

## D-01 Blocchi di circa 2.500 parole, tagliati dove il libro si interrompe da sé

Decisione: il testo si divide in blocchi di circa 2.500 parole. Un blocco nuovo comincia preferibilmente a un titolo di parte, all'epigrafe che apre un capitolo o a un separatore di scena; solo una scena molto lunga si taglia tra due paragrafi.

Motivazione: un sotto-agente deve poter leggere per intero il blocco, la guida, il glossario e la scheda dei personaggi senza diluire l'attenzione; un blocco più corto toglierebbe contesto narrativo, uno più lungo renderebbe la revisione meno accurata.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-02 Un sotto-agente per blocco, in sequenza, con il modello della sessione

Decisione: traduzione, revisione e redazione si fanno con un sotto-agente nuovo per ogni blocco, uno alla volta. I sotto-agenti hanno `model: inherit` (usano il modello della chat) ed `effort: high`.

Motivazione: un contesto nuovo per blocco evita che la chat principale si riempia e che errori di un blocco si trascinino nel successivo; la sequenza permette di passare al traduttore la fine del blocco precedente già tradotto.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-03 Tre passaggi per blocco e una lettura di coerenza finale

Decisione: prima stesura, revisione bilingue indipendente che non modifica il testo, redazione che applica i rilievi e cura l'italiano verificando ogni intervento sull'inglese; alla fine, una lettura di coerenza sull'intero libro e una controprova a campione.

Motivazione: la revisione bilingue trova soprattutto errori di senso e omissioni, la lettura solo in italiano trova soprattutto calchi e frasi che suonano tradotte; servono entrambe, e chi rivede non deve essere chi ha tradotto.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-04 Canzoni e poesie di autori reali restano in inglese

Decisione: le epigrafi tratte da canzoni o poesie di autori reali non si traducono; nei file di lavoro il paragrafo contiene solo `[[ORIGINALE]]` e lo script rimette il testo inglese nell'EPUB.

Motivazione: la licenza di Watts copre il suo testo, non i versi di altri autori; lasciarli in originale è anche una convenzione diffusa nelle traduzioni italiane.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-05 Sonnet per S0, Opus per il resto, un modello per passaggio

Decisione: Sonnet 5.5 per la sessione meccanica iniziale; Opus 5.5 per glossario, pilota, traduzione, revisione e coerenza, salvo che il confronto alla cieca facoltativo con Fable 5.2 faccia scegliere quest'ultimo. Il modello scelto vale per tutte le sessioni di un passaggio.

Motivazione: due modelli diversi in parti diverse del libro darebbero due voci diverse; per la scelta fra modelli vale ciò che il PI legge, non la reputazione del modello.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-06 Nota sulla traduzione in fondo, licenza nei metadati

Decisione: la nota sulla traduzione e sulla licenza va dopo l'ultimo capitolo; la licenza è anche nei metadati dell'EPUB.

Motivazione: in testa al libro la nota finirebbe nello stesso file della dedica e delle prime epigrafi; nei metadati resta comunque visibile in ogni lettore.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-07 Riassunto della trama per tutti i blocchi prima di tradurre

Decisione: il riassunto della trama blocco per blocco si scrive in S1, durante la lettura completa del libro, e non man mano che si traduce.

Motivazione: il secondo blocco del pilota sta a metà libro; senza un riassunto completo il traduttore lavorerebbe senza sapere cosa è successo prima.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-08 Lineette ammesse nella traduzione

Decisione: nel testo del romanzo le lineette sono ammesse e si usano dove le usa Watts. Il divieto di lineette come punteggiatura resta per i documenti di progetto e per la conversazione con il PI. La forma (lineetta media, U+2013, spaziata negli incisi e attaccata nel discorso interrotto) è una proposta da confermare in S1.

Motivazione: la regola del PI riguarda i testi scritti dall'agente, non la resa di un autore che fa delle lineette un tratto del suo ritmo; sostituirle cambierebbe lo stile dell'originale.

Deciso da: PI. Data: 2026-11-09. Stato: valida.
