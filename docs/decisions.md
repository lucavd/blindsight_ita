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

## D-09 La sessione sulla sorgente (S0) si fa con Fable 5.2 invece di Sonnet

Decisione: la sessione che scarica la sorgente e la divide in blocchi (S0) si esegue con Fable 5.2, il modello della chat in cui il PI l'ha aperta, e non con Sonnet 5.5 come previsto dalla decisione sui modelli (D-05). È una deroga alla regola sul modello previsto e vale solo per S0: per tutte le altre sessioni resta il modello scritto in `docs/state.tsv`. Se S0 si interrompe, si può riprendere con Fable 5.2 o con Sonnet 5.5.

Motivazione: S0 non scrive una riga di italiano (scarica, divide, conta), quindi il modello non può cambiare la voce della traduzione, che è la ragione della regola. Il costo è un consumo maggiore dei limiti d'uso rispetto a Sonnet.

Deciso da: PI. Data: 2026-11-09. Stato: valida.

## D-10 Lavoro nel cloud: push a ogni commit, ambiente dedicato, EPUB consegnato come file

Decisione: quando una sessione gira in Claude Code nel cloud, e non sul Mac o sul server, valgono quattro adattamenti. A ogni commit segue un push sul ramo della sessione. Le sessioni si aprono nell'ambiente cloud `blindsight_ita`, che consente la rete verso `www.rifters.com` e `rifters.com` e installa epubcheck all'avvio. Il modello si sceglie nell'app al momento di aprire la sessione, perché il comando `claude --model ...` del README vale solo in locale. Gli EPUB, che non sono versionati, si consegnano al PI come file alla chiusura della sessione che li produce.

Motivazione: il contenitore cloud è temporaneo e ciò che non è sul repository si perde; l'ambiente predefinito non raggiunge il sito dell'autore e non ha epubcheck. L'ambiente è stato proposto dall'agente e approvato dal PI. Lo script di avvio è stato provato a mano in questa sessione ma non ancora in una sessione nuova.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-11 Sorgente dalla copia dell'Internet Archive se il sito dell'autore non risponde

Decisione: se la pagina non si riesce a scaricare da rifters.com, si usa la copia grezza della stessa pagina conservata dall'Internet Archive (`web.archive.org`, con la forma dell'indirizzo che restituisce i byte originali senza la barra dell'archivio). Nel registro si annotano l'indirizzo completo e la data della cattura.

Motivazione: dall'ambiente cloud la connessione a rifters.com cade prima di ricevere dati; la copia d'archivio è la stessa pagina a una data nota. Limite dichiarato al PI: dall'ambiente cloud non si può verificare che la cattura sia identica alla pagina di oggi.

Deciso da: PI. Data: 2026-11-10. Stato: superata dalla decisione sulla sorgente fornita dal PI (D-12). Non è mai stata eseguita: l'host dell'archivio non era consentito dalla rete dell'ambiente.

## D-12 La sorgente è il file HTML fornito dal PI

Decisione: la sorgente della traduzione è il file `Blindsight_html_format.htm` contenuto nello zip che il PI ha caricato nella chat il 2026-11-10. È salvato senza modifiche come `source/original/Blindsight.htm`, insieme alle tre immagini dello zip; lo zip originale è conservato in `reference/Blindsight.zip`. Non si scarica più nulla dal sito dell'autore né dall'Internet Archive.

Motivazione: dal cloud il sito dell'autore non risponde e l'archivio non è raggiungibile. Il file è l'esportazione HTML dell'autore (nei metadati: autore Peter Watts, ultima modifica 2006-12-09; nello zip ha la data 2007-09-03) e l'EPUB di confronto fornito dal PI dichiara di derivare dalla stessa pagina del sito.

Deciso da: PI. Data: 2026-11-10. Stato: valida. Provenienza riferita dal PI alla chiusura della sessione: il sito dell'autore (rifters.com), dalla pagina che offre il romanzo in formato HTML; l'indirizzo esatto non è annotato.

## D-13 L'EPUB di Ellen Herzfeld serve solo da confronto; la licenza è la 2.5

Decisione: l'EPUB `PeterWatts_Blindsight-v1.01-formatted-by-Ellen-Herzfeld.epub` fornito dal PI, conservato in `reference/`, non è sorgente: si usa solo per controllare che il testo dei blocchi sia completo. La licenza che vale per la traduzione è quella dichiarata nella pagina dell'autore, Creative Commons Attribution-NonCommercial-ShareAlike 2.5; la versione è stata aggiunta alla nota sulla traduzione e ai metadati dell'EPUB.

Motivazione: l'EPUB è un'edizione curata da terzi che interviene sulle note (voci rinumerate e duplicate, refusi corretti, indirizzi aggiornati) e dichiara per sé la versione 3.0 della stessa licenza; il progetto traduce il testo dell'autore.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-14 Confini del libro: cosa entra nei blocchi e cosa resta fuori

Decisione: i blocchi vanno dalla dedica (paragrafo p00003) all'ultima nota finale (paragrafo p03946). Restano fuori tre cose. Titolo e nome dell'autore (p00001 e p00002), come previsto dalla procedura. L'indice della pagina web con il separatore che lo chiude (da p00005 a p00012). Il testo legale della licenza con il separatore che lo chiude (da p03758 a p03802). Le due esclusioni interne sono scritte in `source/excluded.tsv`. Le 144 note finali, che nella pagina vengono dopo il testo della licenza, seguono così direttamente il saggio a cui appartengono. Nessun titolo di parte è un'immagine, quindi nessun titolo è stato aggiunto a mano.

Motivazione: l'indice è navigazione della pagina, e l'EPUB ne genera uno proprio; il testo legale non è del romanzo e non si traduce, la licenza è indicata nella nota e nei metadati.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-15 Adattamenti dello script alla pagina reale

Decisione: lo script è stato adattato alla pagina dell'autore in sette punti, ciascuno coperto dal collaudo.

1. I paragrafi allineati a destra sono epigrafi (tipo `q`): nella pagina le epigrafi non sono citazioni a blocco.
2. I caratteri scritti con il font Symbol (gradi, mu, epsilon, sigma) sono convertiti nel carattere Unicode che il font mostra, e i trattini morbidi invisibili sono tolti. Se un carattere di questo tipo resta senza conversione, il cancello di copertura fallisce.
3. Gli apici annidati (i richiami di nota) e gli apici con spazi sono scritti in modo che pandoc li legga.
4. L'impaginazione propria di un paragrafo (centrato, rientrato, colonna di una tabella) è registrata nel campo `layout` di `source/paragraphs.jsonl` e riportata nell'EPUB con classi del foglio di stile.
5. Le immagini che fanno parte del libro si elencano in `source/figures.tsv` e vengono inserite nell'EPUB. Oggi è una sola: il cubo dopo il paragrafo p00418.
6. `chunk --exclude` lascia fuori gli intervalli interni che non sono il libro.
7. Un blocco prende il nome di tutte le parti che tocca, e `source/SHA256SUMS` non elenca più due volte lo stesso file.

Motivazione: il pacchetto era stato scritto senza vedere la pagina. Senza questi adattamenti l'EPUB avrebbe avuto le epigrafi impaginate come testo normale, dieci caratteri illeggibili, segni `^` accanto ai numeri di nota, la figura mancante e i passi a più colonne appiattiti.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-16 Quattro sessioni di traduzione e sei di revisione

Decisione: le sessioni di traduzione sono T1 (blocchi 01-11), T2 (12-22), T3 (23-34), T4 (35-41). Le sessioni di revisione sono R1 (01-07), R2 (08-14), R3 (15-21), R4 (22-29), R5 (30-36), R6 (37-41). Il modello scritto in `docs/state.tsv` è provvisorio: lo conferma o lo cambia il pilota.

Motivazione: è il raggruppamento suggerito dallo script per circa 25.000 parole a sessione di traduzione e 16.000 a sessione di revisione, e coincide con la stima del piano.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-17 La copertina è il fronte della sovraccoperta fornita dal PI

Decisione: la copertina dell'EPUB è il fronte della sovraccoperta alternativa di Thomas Pringle che il PI ha caricato nella chat (`reference/jacket-alternate-thomas-pringle.jpg`). Il fronte è ritagliato dall'immagine (606 per 897 pixel) e salvato in `epub/cover.jpg`; lo script lo passa a pandoc quando il file esiste.

Motivazione: è l'immagine scelta dal PI, e sulla sovraccoperta stessa l'autore scrive che si può copiare senza limiti. Limite: la risoluzione è bassa per uno schermo ad alta densità; se il PI procura una versione più grande basta sostituire il file. L'EPUB di confronto usa un'altra copertina dello stesso artista, non questa.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-18 Si lavora nel cloud, con una pull request alla chiusura di ogni sessione

Decisione: le sessioni proseguono in Claude Code nel cloud. Alla chiusura di ogni sessione l'agente apre una pull request dal ramo della sessione al ramo principale e il PI la unisce prima di aprire la sessione successiva. Le regole sono nella sezione "Lavoro nel cloud" di `CLAUDE.md`, aggiunta con questa decisione; restano validi gli adattamenti tecnici già registrati (decisione sul lavoro nel cloud, D-10). Per la sessione sulla sorgente (S0) non c'è nulla da unire: il repository era vuoto e il ramo di quella chat è diventato il principale.

Motivazione: il PI vuole lanciare le sessioni dal telefono. Nel cloud ogni chat lavora su un ramo suo e la successiva parte dal ramo principale: senza unione la sessione successiva non vedrebbe il lavoro fatto e lo rifarebbe.

Deciso da: PI. Data: 2026-11-10. Stato: valida.
