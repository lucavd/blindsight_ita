---
type: Session
title: "S2b: pilota alla cieca con un secondo modello (facoltativa)"
description: Ripete il pilota sugli stessi due blocchi con un secondo modello e prepara due EPUB anonimi, così il PI sceglie il modello leggendo, senza sapere quale ha scritto cosa.
model: fable
status: open
pi_approval: pending
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

# Cosa fa

Il PI sceglie il modello per traduzione e revisione sulla base di ciò che legge, non della reputazione del modello. Si apre solo se il PI l'ha chiesta alla fine di S2, con `claude --model fable`. Se Fable non compare tra i modelli disponibili in Claude Code, la sessione si salta e lo si registra.

# Dubbi ricevuti

La guida di stile e il glossario devono essere esattamente quelli usati in S2: controllare con `git log -- docs/style-guide.md docs/glossary.tsv docs/characters.md` che non siano cambiati dopo S2. Se sono cambiati, fermarsi e chiedere al PI.

Dal pilota (S2): il glossario è cambiato durante S2, non dopo. Dopo il blocco 01 è stata aggiunta la regola sulla maiuscola di Sintesi (decisione sulla maiuscola di Sintesi, D-28); dopo il blocco 18 sono entrate sette voci nuove (decisione sui termini del pilota, D-29). Sono solo aggiunte, con le rese trovate dai traduttori del pilota. Il secondo modello usa il glossario com'è alla chiusura di S2: le due versioni avranno gli stessi termini e il confronto sarà sulla prosa, che è ciò che il PI giudica. I commit di S2 su glossario e guida non sono quindi un motivo per fermarsi; lo è ogni commit successivo alla chiusura di S2. Il traduttore di S2b riceve nel prompt la stessa indicazione data in S2 sulle righe di attribuzione delle epigrafi (lineetta media e spazio prima del nome), salvo che il PI abbia deciso diversamente.

Decisioni del PI alla chiusura di S2 (decisione sulle scelte del pilota, D-30):

1. Il confronto si fa. Nel cloud la sessione si apre scegliendo Fable 5.2 nell'app; se il PI riapre la chat della sessione sulla sorgente, si lavora sul ramo `sessione-S2b` (decisione sulla chat cloud riaperta, D-27).
2. Lineetta media seguita da spazio nelle righe di attribuzione delle epigrafi («– Ted Bundy»): approvata. Il traduttore di S2b la riceve nel prompt. La regola si scrive nella guida di stile al punto 5 della procedura, dopo la scelta del PI; si scrive anche se il confronto viene saltato.
3. La lettura dell'EPUB di prova di S2 passa qui: la lettura e le domande su tono, dialoghi, termini e forme di cortesia si fanno qui, sulle due versioni anonime. In apertura chiedere al PI se ha aperto l'EPUB del pilota dopo la chiusura di S2: se sì, il confronto non è più alla cieca per una delle due versioni, e prima di procedere si chiede al PI come vuole continuare. Nel riassunto, oltre alla scelta, il PI risponde alle quattro domande di S2: tono del narratore, naturalezza dei dialoghi, termini o forme di cortesia stonati; le risposte si applicano alla guida al punto 5, e se cambiano scelte già presenti nei due blocchi della versione vincente si rilancia il redattore su quei blocchi.

# Procedura

Stessi blocchi e stessi passaggi di S2, con queste differenze:

1. Ogni sotto-agente riceve nel prompt i percorsi alternativi: prima stesura in `trial-b/draft/NN.md`, note in `trial-b/notes/NN.md`, revisione in `trial-b/review/NN-findings.tsv`, registro del redattore in `trial-b/review/NN-editor-log.md`, versione finale in `trial-b/final/NN.md`. Niente in `translation/` deve cambiare.
2. Controlli con la cartella alternativa: `check <NN> --stage draft --dir trial-b/draft`, `coverage <NN> --file trial-b/review/<NN>-findings.tsv`, `check <NN> --stage final --dir trial-b/final`.
3. Confronto: `python3 tools/blindsight.py blind --a translation/final --b trial-b/final --chunks 01,<NN>` produce `build/pilota-X.epub` e `build/pilota-Y.epub`. La chiave resta in `comparison/.key.json`: nessuno la apre prima della scelta, nemmeno l'agente.
4. Riassunto: solo conteggi e tempi per X e Y, senza nomi di modelli; ai tempi si aggiunge la nota che il tempo potrebbe tradire l'identità, quindi va letto dopo la scelta.
5. Quando il PI ha scelto (e detto perché, in una frase): `blind --reveal`, registrare la decisione con la sua motivazione, fissare il modello delle sessioni T e R in `docs/state.tsv`, applicare le indicazioni del PI raccolte in S2 e in S2b alla guida di stile. Se vince la versione in `trial-b/`, copiare i suoi file nelle cartelle di `translation/` e `review/` per i due blocchi.

# Cancelli

1. `verify` superato; nessun file sotto `translation/` modificato fino al punto 5 (`git status`).
2. Gli stessi cancelli di S2 sui due blocchi della prova B.
3. Due EPUB costruiti.

# Previsioni

Quelle di S2, sui due blocchi della prova B.

# Apertura

Sessione aperta il 2026-11-10 con Fable 5.2 (modello previsto e modello in uso coincidono), sul ramo `sessione-S2b`. Sorgente integra (50 file). Pull request del pilota già unita, nessuna pull request aperta. Guida di stile, glossario e scheda dei personaggi non sono cambiati dopo la chiusura del pilota: l'ultimo commit che li tocca è 30b27e6, dentro il pilota.

Domanda al PI in apertura: ha aperto l'EPUB del pilota dopo la chiusura di S2? Risposta: no. Il confronto resta alla cieca.

Limite visto in apertura: il riassunto del pilota, che il PI ha letto, citava tre rese della versione A (il gioco sul titolo, i congiuntivi di Pag, una battuta di Szpindel). Controllo fatto a prova B finita, cercando le tre frasi alla lettera nelle due versioni finali: tutte e tre compaiono solo nella versione A, nessuna nella prova B (in apertura avevo scritto che la prima, legata al glossario, sarebbe stata uguale: non lo è). Se il PI le ricorda può riconoscere la versione A. Detto al PI nel messaggio di apertura e nel riassunto, con l'indicazione di non rileggere il riassunto del pilota prima di scegliere.

Ogni sotto-agente della prova B riceve nel prompt il divieto di aprire `translation/`, `review/`, `checks/`, `build/`, `docs/sessions/`, `docs/decisions.md` e `docs/log.md`, che contengono la versione A o ne citano le rese: la prova B deve essere indipendente.

Il controllo sui blocchi della prova B, lanciato con `--save`, scriveva in `checks/` con lo stesso nome dei risultati della versione A e li avrebbe sovrascritti. Corretto prima del primo controllo: con la cartella alternativa i risultati vanno in `trial-b/checks/` (decisione sui risultati dei controlli della prova B, D-32). I due EPUB anonimi hanno un titolo proprio, per distinguerli nel lettore (decisione sul titolo dei due EPUB del confronto, D-31).

Il PI ha precisato durante il lavoro di non avere scaricato nessun EPUB: i due file del confronto gli si consegnano entrambi in questa chat.

# Tempi misurati

| blocco | passaggio | inizio | fine | minuti |
|---|---|---|---|---|
| 01 | traduttore | 10:43:17 | 10:49:55 | 6,6 |
| 01 | revisore | 10:50:18 | 10:57:18 | 7,0 |
| 01 | redattore | 10:57:45 | 11:02:36 | 4,9 |
| 18 | traduttore | 11:03:32 | 11:13:15 | 9,7 |
| 18 | revisore | 11:13:33 | 11:23:49 | 10,3 |
| 18 | redattore | 11:24:14 | 11:31:42 | 7,5 |

Orari UTC del 2026-11-10, prova B. I minuti sono la durata del sotto-agente riportata dall'ambiente alla sua chiusura, come nel pilota: 397.624, 420.464 e 291.159 millisecondi per il blocco 01; 583.341, 616.007 e 447.700 per il blocco 18. L'inizio è l'ora annotata al lancio del sotto-agente, la fine è l'inizio più la durata. Nel pilota la fine era l'ora di scrittura dell'ultimo file e l'inizio la fine meno la durata; qui quella convenzione dava inizi precedenti al lancio, perché il sotto-agente lavora ancora dopo l'ultimo file. La colonna dei minuti è confrontabile fra le due prove, gli orari no.

Tre passaggi insieme: 18,5 minuti per il blocco 01 (1.109 secondi) e 27,5 per il blocco 18 (1.647 secondi); 45,9 minuti sui due blocchi, contro i 28,3 del pilota (676 e 1.024 secondi). Per mille parole della sorgente (5.187 nei due blocchi): 3,15 minuti di traduttore e 5,70 di revisore più redattore, contro 2,6 e 2,9 del pilota. Con la formula del piano (tempo per mille parole sulle 99.452 parole dei 39 blocchi rimasti, un minuto di coordinamento per passaggio e blocco, un quarto d'ora per sessione) il resto del libro richiede 6,9 ore di traduzione e 12,3 di revisione, 19,1 in tutto, contro le 13,5 stimate nel pilota.

# Segnalazioni spiegate

| blocco | paragrafo | segnalazione | spiegazione o correzione |
|---|---|---|---|
| 01 | p00058 | glossario: pod, atteso capsula | Falso allarme, lo stesso del pilota. Pod people sono gli ultracorpi del film, non le capsule di ibernazione: resa «ultracorpi». |
| 01 | p00060 | glossario: drum, atteso tamburo | Falso allarme, lo stesso del pilota. È il verbo to drum up, reso «mobilitare l'indignazione del quartiere»; non è il tamburo della nave. |
| 18 | p01649 | glossario: pod, atteso capsula | Falso allarme. Qui pod è il sensore applicato alla parete della tenda (il sensor pod che Bates attacca alla tenda nel blocco 16), reso «sensore» su proposta del revisore; la voce del glossario riguarda le capsule di risveglio e mediche. Compare dopo la redazione: nella prima stesura c'era «capsula», che il revisore ha giudicato fuorviante. |
| 18 | p01650 | glossario: transient, atteso transiente | Falso allarme, lo stesso del pilota. È l'aggettivo di un fronte di bassa pressione passeggero, reso «fronte transitorio»; non è l'orca transiente. |

# Termini proposti dai traduttori

Valgono per la prova B. Se la prova B vince il confronto, i termini che tornano in altri blocchi si decidono al punto 5 della procedura, prima della chiusura; se perde, restano nei file della prova e non toccano il glossario.

| blocco | termine | decisione |
|---|---|---|
| 01 | optimized, mongrel, polly, sandbox buddy, sentry, seizures, wiring e rewiring, algorithms, engineered superboys, radical hemispherectomy, krill, checklists | Parole comuni o usi singoli: restano le rese del traduttore, confermate dal revisore. Polly resta invariato in corsivo: è un insulto opaco anche in inglese. |
| 01 | pod people | Ultracorpi, minuscolo, dalla voce del glossario sul soprannome di Siri. Nessuna voce nuova. |
| 01 | gamespace | Spazio di gioco. Compare solo qui. |
| 01 | playground | Parco giochi. Compare anche nel blocco 13: da uniformare al punto 5 se vince la prova B. |
| 01 | Scramblers con la maiuscola a metà frase (p00062) | Il traduttore aveva tenuto la maiuscola della sorgente; revisore e redattore hanno applicato la minuscola del glossario. Nella sorgente la maiuscola a metà frase c'è solo qui (conteggio sui blocchi sorgente: 12 maiuscole, 11 a inizio frase o in un titolo; 74 minuscole). Serve una regola nel glossario: si scrive al punto 5, per non cambiare il glossario durante il confronto. |
| 18 | spinal bundle | Fascio spinale. Torna nei blocchi 05, 11 e 31 (conteggio sui blocchi sorgente): voce nuova del glossario al punto 5, con la resa della versione scelta. Il traduttore del pilota non l'aveva proposto. |
| 18 | jarhead | Marine. Torna nel blocco 07: voce nuova del glossario al punto 5, con la resa della versione scelta. Il traduttore del pilota non l'aveva proposto. |
| 18 | on top, detto della personalità al comando nella Banda | In cima («con James in cima»). Torna nel blocco 36: voce nuova del glossario al punto 5, con la resa della versione scelta. Segnalato dal redattore. |
| 18 | feed, faceplate | Flusso e visiera. Sono parole che tornano in molti blocchi (feed in 17 blocchi sorgente, faceplate in 5) e non sono nel glossario. Se vince la prova B si decide al punto 5 se servono due voci; se vince la versione A si guarda come le ha rese. |
| 18 | ground truths, Damascus Disease, decompiler, transducer, glow-globes, test pattern, synopsis, fight-flight, pattern, surfaces, gauge, le parti della campana, wet sample | Usi singoli o parole comuni: restano le rese del traduttore, confermate dal revisore (verità a terra, morbo di Damasco, decompilatore, trasduttore, globi luminosi, figura di prova, sinossi, attacco-o-fuga, schema, superfici, indicatore, campione umido). |
| 18 | Klüver constant | Costante di Klüver: già coperta dalla voce del glossario sulle costanti di forma. |
| 18 | punto dentro le caporali, lineetta nelle battute | La guida non le fissa. Le due versioni mettono entrambe il punto dentro le caporali (conteggio sui file finali: 13 e 100 casi in ciascuna, nessuno fuori) e la virgola fuori (6 e 27 casi). Sulla lineetta dentro le battute applicano la regola della guida in modo un po' diverso. Regole da scrivere al punto 5, sentito il PI. |
| 01 | tempo della narrazione | La guida di stile non ha una regola. La prova B usa il passato prossimo per la cornice (Siri che parla dalla bara) e il passato remoto per l'infanzia. È una scelta che vincola tutto il libro: entra nelle domande di lettura per il PI, e la scelta della versione vincente diventa regola della guida al punto 5. |

# Esiti delle previsioni per blocco

| blocco | quantità | valore | esito |
|---|---|---|---|
| 01 | rapporto di lunghezza mediano, prima stesura | 1,086 | confermata |
| 01 | rapporto di lunghezza mediano, versione finale | 1,106 | confermata |
| 01 | quota di paragrafi cambiati dal redattore | 0,278 (15 su 54) | confermata |
| 01 | rilievi di gravità alta | 0 | confermata |
| 01 | tempo di macchina, tre passaggi | 18,5 minuti | confermata |
| 18 | rapporto di lunghezza mediano, prima stesura | 1,110 | confermata |
| 18 | rapporto di lunghezza mediano, versione finale | 1,114 | confermata |
| 18 | quota di paragrafi cambiati dal redattore | 0,164 (33 su 201, separatori esclusi) | confermata, vicino al limite basso |
| 18 | rilievi di gravità alta | 1 | confermata |
| 18 | tempo di macchina, tre passaggi | 27,5 minuti | confermata |

Dieci previsioni su dieci confermate; nessun cancello fallito.

Rilievi della revisione sul blocco 01: 15 rilievi veri (2 medi, 13 bassi) più 30 righe di parere sui 29 dubbi del traduttore (2 medie, 28 basse). I medi: in p00013 «peculiare» era un falso amico di peculiar, ora «singolare»; in p00027 «Non ero estraneo agli scherni» ricalcava I was no stranger to e si poteva leggere come se Siri partecipasse agli scherni; in p00044 un imperfetto faceva di un'ipotesi un'abitudine; in p00062 la maiuscola di Scrambler. Il redattore ha accettato 14 rilievi veri su 15 e ne ha respinto 1, basso (p00059, «spremuto fuori» resta); dei 30 pareri ne ha accolti 29 (25 sono conferme senza modifica) e ne ha respinto 1 (p00064, «a farci visita» resta). Nessun intervento redazionale proprio.

Rilievi della revisione sul blocco 18: 27 rilievi veri (1 alto, 2 medi, 24 bassi) più 48 righe di parere sui 31 dubbi del traduttore (3 medie, 45 basse). L'alto: in p01655 You reached for it era reso «Hai allungato la mano», senza for it; ora «Hai allungato la mano per prenderla». Verificato dalla chat principale sull'inglese: fondato, anche se è un'omissione di due parole. I cinque medi, dal rapporto del revisore: «capsula» per il sensore della tenda (p01649), «discretamente distante» che si legge come abbastanza distante (p01721), la frase sulle braccia pluriarticolate che non reggeva in italiano (p01785, ora «braccia pluriarticolate che partivano da una massa centrale»), possibly omesso (p01812), «Mandy mi va benissimo» troppo forte per Like Mandy fine (p01831). Il redattore ha accettato 26 rilievi veri su 27 e ne ha respinto 1, basso (p01749, «pentagrammi» resta: pentacolo è un talismano, non un sinonimo); dei 48 pareri ne ha accolti 47 e ne ha respinto 1 in parte (p01734, «in cima» resta per on top). 5 interventi redazionali propri (p01719, p01720, p01732, p01761, p01823), ciascuno verificato sull'inglese secondo il registro.

# Confronto dei numeri per modello

I numeri della versione A vengono dai file del pilota, riletti in questa sessione. La tabella è per modello e non per X e Y: l'abbinamento è nella chiave, che resta chiusa.

| quantità | versione A, pilota (Opus 5.5) | prova B (Fable 5.2) |
|---|---|---|
| rapporto di lunghezza mediano, versione finale, blocchi 01 e 18 | 1,102 e 1,106 | 1,106 e 1,114 |
| rilievi di gravità alta, blocchi 01 e 18 | 0 e 2 | 0 e 1 |
| rilievi veri della revisione | 13 e 26, 39 in tutto | 15 e 27, 42 in tutto |
| rilievi veri respinti dal redattore | 2 | 2 |
| righe di parere sui dubbi del traduttore | 17 e 36 | 30 e 48 |
| quota di paragrafi cambiati dal redattore | 0,148 (8 su 54) e 0,154 (31 su 201) | 0,278 (15 su 54) e 0,164 (33 su 201) |
| tempo dei tre passaggi | 11,3 e 17,1 minuti | 18,5 e 27,5 minuti |
| previsioni confermate | 9 su 10 | 10 su 10 |
| parole della versione finale, due blocchi | 5.320 | 5.368 |

# Incidente sul sorteggio

Dopo il primo sorteggio la chat principale ha elencato la cartella di costruzione con le dimensioni dei file. Il testo assemblato di una delle due versioni anonime aveva la stessa dimensione in byte del testo assemblato del pilota, rimasto nella cartella dalla sessione precedente: l'abbinamento era quindi leggibile senza aprire la chiave. La chiave non è stata aperta. Rimedio: sorteggio rifatto con lo stesso comando, senza mostrare l'output né le dimensioni; i due EPUB consegnati al PI sono quelli del secondo sorteggio, che è indipendente dal primo. Da allora la chat principale non elenca le dimensioni dei file di `build/` e non apre i due testi assemblati. Detto al PI in chat e nel riassunto.

Impronte dei due testi assemblati in `comparison/impronte.tsv` (decisione sulle impronte del confronto, D-33): se il contenitore cloud viene sostituito prima della scelta, la chiave, che non è versionata, va persa; in quel caso l'abbinamento si ricostruisce assemblando di nuovo le due versioni e confrontando le impronte.

# Limiti del confronto

1. Due blocchi su 41: 5.187 parole su 104.639, il 5% del libro.
2. Ogni versione è stata tradotta, rivista e redatta dal proprio modello: il confronto è fra due catene intere, non fra due traduttori.
3. La prova B ha lavorato con il glossario alla chiusura del pilota, che contiene 8 regole nate dai traduttori della versione A (deciso alla chiusura del pilota). Il traduttore del blocco 01 della prova B ha ricevuto nel prompt l'indicazione sulla lineetta delle attribuzioni, che nel pilota era nata dal traduttore di quel blocco.
4. I prompt dati ai sotto-agenti del pilota non sono conservati nel repository: quelli della prova B hanno gli stessi contenuti previsti dalla procedura (blocco, percorsi, lineetta delle attribuzioni) più il divieto di leggere la versione A e, per il blocco 18, il richiamo a trattare tutti i 203 paragrafi. Non posso garantire che siano identici parola per parola.
5. Le tre frasi citate nel riassunto del pilota compaiono alla lettera solo nella versione A (sezione Apertura).
6. I tempi sono misurati in ore diverse della stessa giornata, su due blocchi: la differenza fra i modelli (62% in più per la prova B) è un ordine di grandezza, non una misura fine.

# Da fare dopo la scelta del PI

Stato al momento del riassunto: lavoro sui due blocchi finito, EPUB consegnati, sessione aperta in attesa della scelta. Se la chat riparte in un contenitore nuovo, si riprende da qui.

1. Aprire la chiave con `blind --reveal`. Se la chiave manca: `build --chunks 01,18 --out build/a.epub`, `build --chunks 01,18 --dir trial-b/final --out build/b.epub`, poi confrontare l'impronta SHA-256 di `build/a.md` e `build/b.md` con `comparison/impronte.tsv`.
2. Registrare la scelta del PI con la sua motivazione come decisione; fissare il modello delle sessioni T e R in `docs/state.tsv` e nei file delle sessioni; aggiornare il piano (modello e, se vince la prova B, i tempi: 19,1 ore invece di 13,5).
3. Se vince la prova B: copiare i suoi file per i blocchi 01 e 18 in `translation/` e `review/`, rilanciare i controlli con salvataggio, aggiornare nei dubbi ricevuti della seconda sessione di traduzione (T2) la nota sui «sussurratori», che cita la resa della versione A.
4. Guida di stile: lineetta media e spazio nelle attribuzioni delle epigrafi (già approvata dal PI); punto fermo dentro le caporali per la battuta completa e virgola fuori per l'inciso; lineetta dentro le battute; tempo della narrazione; indicazioni di lettura del PI. Se cambiano scelte già presenti nei due blocchi della versione vincente, rilanciare il redattore su quei blocchi.
5. Glossario: voci nuove per spinal bundle, jarhead e on top con la resa della versione scelta; decidere su feed e faceplate; nota sulla maiuscola di scrambler secondo la decisione del PI.
6. Dubbi da passare alla seconda sessione di traduzione (T2), che traduce i blocchi 13, 16 e 17: la sigla TAT del blocco 18 (p01790) deve coincidere con quella ricreata nel blocco 17; la battuta di Bates citata in p01829 deve coincidere parola per parola con la versione finale del blocco 13; haunted mansion (p01717) va allineato a Haunted del blocco 16 (p01510); the pod di p01649 a sensor pod del blocco 16 (p01542). Alla sessione finale di coerenza: Fab con o senza articolo (p01822).
7. Chiusura: riga di chiusura nel riassunto, `docs/state.tsv`, registro, commit, push, pull request.

# Dopo la scelta del PI

Scelta del PI, 2026-11-10: versione Y; «scrambler» minuscolo anche nel Prologo. Chiave aperta dopo la scelta: X è la prova B (Fable 5.2), Y è la versione A, il pilota (Opus 5.5). Verifica indipendente dalla chiave: il testo assemblato di Y è identico a quello del pilota, e le impronte dei due testi coincidono con quelle salvate. Motivazione del PI: italiano più naturale e dialoghi migliori. Domande di lettura: niente da segnalare, la guida prende le convenzioni della versione scelta. Il PI dice di non avere riconosciuto nessuna delle due versioni durante la lettura.

Controllo fatto dalla chat principale dopo la scelta: i 9 paragrafi in cui il revisore della prova B aveva trovato rilievi alti o medi sulla propria stesura, riletti nella versione A finale accanto all'inglese (p00013, p00027, p00044, p01649, p01655, p01721, p01785, p01812, p01831; il decimo rilievo, la maiuscola di p00062, è deciso dal PI). In due la versione A ha lo stesso difetto, e il revisore del pilota non l'aveva segnalato: p01655, You reached for it reso «Hai allungato la mano», senza for it (riga `ok` nella revisione del pilota); p01721, discreetly distant reso «discretamente distante», che si legge come abbastanza distante. Negli altri sette la versione A è a posto.

## Controllo aggiunto: revisione incrociata del blocco 18

Domanda: quanti difetti restano nella versione finale di Opus che un revisore di un altro modello trova? È la misura che il pilota aveva lasciato aperta (traduttore, revisore e redattore sono lo stesso modello). Il confronto alla cieca non la dava, perché confronta due catene intere.

Procedura: il sotto-agente `reviewer` di questa sessione (Fable 5.2) rilegge `translation/final/18.md` contro l'inglese, senza vedere la revisione del pilota né i file della prova B, e scrive `trial-b/review/18-cross-findings.tsv`. La chat principale verifica sull'inglese ogni rilievo alto o medio. Nessun file sotto `translation/` cambia: le correzioni fondate passano alla sessione di revisione che copre il blocco, fatta con il modello scelto.

Cancello: copertura della revisione superata sul file della revisione incrociata.

Previsione, scritta prima di lanciare:

| quantità | atteso | intervallo di rilevanza | se è fuori |
|---|---|---|---|
| rilievi alti o medi fondati sulla versione finale di Opus del blocco 18 (201 paragrafi), verificati sull'inglese | 2 (i due già noti) | da 0 a 5 | sopra: la revisione con lo stesso modello lascia passare troppo, e si propone al PI una revisione fatta da un modello diverso da quello che traduce |

Limite dichiarato prima: chi giudica se un rilievo è fondato è la chat principale, che gira con lo stesso modello del revisore incrociato. I rilievi alti e medi fondati si elencano uno per uno, così il PI può giudicarli da sé.

# In breve

## In breve: quale delle due versioni vuoi per tutto il libro?

### A cosa serviva

Il modello scelto ora traduce e rivede tutto il libro, e non si cambia a metà. Questa sessione ha rifatto con Fable 5.2 gli stessi due blocchi del pilota, il Prologo e l'inizio di Rorschach, e ti consegna due versioni anonime. Scegli leggendo, senza sapere chi ha scritto cosa.

### Cosa abbiamo trovato

1. Le due versioni sono pronte e anonime: due EPUB validi, «pilota X» e «pilota Y», e nessuno sa quale è quale, nemmeno io. L'abbinamento è stato sorteggiato dallo script e la chiave resta chiusa fino alla tua scelta. Un incidente: dopo il primo sorteggio ho visto per errore le dimensioni dei file, che svelavano l'abbinamento. Ho rifatto il sorteggio senza più guardarle; i file che hai ricevuto sono quelli del secondo sorteggio.
2. Anche la seconda versione ha superato tutti i controlli, e le sue dieci previsioni sono tutte confermate. Nessun paragrafo manca e nessun file del pilota è stato toccato. In entrambe le versioni l'italiano è tra il 10 e l'11% più lungo dell'inglese, come ci si aspetta da una traduzione senza tagli né aggiunte.
3. Nei numeri del processo le due catene si somigliano, tranne che nel tempo: Fable impiega il 60% in più. I tre passaggi sui due blocchi hanno richiesto 28 minuti con Opus e 46 con Fable; sul resto del libro vuol dire circa 19 ore di macchina invece di 14. Errori gravi trovati dal revisore nella prima stesura: 2 con Opus, 1 con Fable, tutti corretti. Paragrafi cambiati dal redattore: nel Prologo 8 su 54 con Opus e 15 su 54 con Fable; nel blocco di Rorschach 31 e 33 su 201. Questi numeri sono per modello e non per X e Y: per abbinarli dovrei aprire la chiave, e tu conosci già quelli del pilota.
4. Il confronto non è perfettamente alla cieca, e ha altri tre limiti. Il riassunto del pilota citava tre frasi tradotte: le ho cercate, e compaiono alla lettera solo in una delle due versioni. Se le ricordi la riconosci; se ti succede leggendo, dimmelo insieme alla scelta. Poi: sono due blocchi, il 5% del libro. Ogni versione è stata tradotta, rivista e redatta dal proprio modello, quindi confronti due catene intere e non due traduttori. La seconda versione ha lavorato con un glossario che contiene già 8 regole nate dalla prima, come deciso alla chiusura del pilota: i termini sono gli stessi e la differenza sta nella prosa.
5. Sono emerse quattro cose che la guida di stile non fissa e che vanno fissate prima di tradurre il resto, chiunque vinca. Il tempo della narrazione, fra passato remoto e passato prossimo. Il punto fermo dentro le caporali, che le due versioni usano allo stesso modo. La lineetta dentro le battute, che le due versioni applicano in modo un po' diverso. Tre espressioni inglesi che tornano in altri blocchi e mancano nel glossario: "spinal bundle", "jarhead" e "on top", detto della personalità che in quel momento guida la Banda.

### Cosa devi decidere

1. Quale versione vuoi per tutto il libro, X o Y: non posso raccomandarne una, perché non so quale è quale; raccomando di leggerle entrambe per intero e, se non vedi una differenza netta, di dirmelo. In quel caso la scelta giusta è Opus, che costa circa 5 ore e mezza di macchina in meno. Ogni versione è lunga circa 5.300 parole. Per non favorire quella che leggi per prima, alterna: il Prologo prima in X e poi in Y, il blocco di Rorschach prima in Y e poi in X. Dimmi la scelta e il perché in una frase. Alternative: X oppure Y, e il modello che l'ha scritta traduce e rivede tutto il libro; «nessuna differenza netta», e si prosegue con Opus.
2. Le domande di lettura rimaste dal pilota: raccomando di rispondere sulla versione che scegli, indicando il passo e cosa ti disturba. Il tono freddo e preciso del narratore è giusto? I dialoghi suonano naturali, in particolare Szpindel, Bates e la Banda? Qualcosa stona nei termini o nel tu e lei? Il tempo della narrazione e le lineette dentro le battute ti convincono? Ogni risposta diventa una regola della guida prima di tradurre il resto. Alternativa: «niente da segnalare», e la guida prende le convenzioni della versione scelta così come sono.
3. La maiuscola di «Scramblers» nel Prologo: raccomando la minuscola, come nel glossario e come hanno fatto entrambe le versioni. Watts scrive "our disastrous encounter with the Scramblers" con la maiuscola a metà frase una sola volta in tutto il libro; le altre 74 volte fuori da un inizio di frase usa la minuscola, anche nello stesso Prologo. In italiano una maiuscola isolata si leggerebbe come un refuso. Alternativa: «gli Scrambler» con la maiuscola in quel solo punto, fedele alla lettera di Watts, al prezzo di un'incoerenza visibile.

### Comunque

1. Dopo la tua scelta apro la chiave, fisso il modello di tutte le sessioni di traduzione e di revisione e scrivo nella guida le regole che mancano: la lineetta delle attribuzioni che hai già approvato, il punto dentro le caporali, la lineetta nelle battute e il tempo della narrazione, più le tue indicazioni. Se le tue indicazioni cambiano scelte già presenti nei due blocchi, rifaccio la redazione di quei blocchi.
2. Se vince la versione di Fable, i suoi due blocchi prendono il posto di quelli del pilota e il piano dei tempi passa da circa 14 a circa 19 ore, tutte con Fable. Se il tuo piano non le regge, dimmelo dopo l'apertura della chiave e si resta su Opus.
3. Le tre espressioni inglesi del punto 5 entrano nel glossario con la resa della versione scelta.
4. Alla sessione che tradurrà la prima parte di Rorschach passano quattro allineamenti fra blocchi segnalati dai redattori: una sigla, una battuta di Bates che Siri cita a memoria, e due termini della prima incursione.
5. Prima di scegliere non aprire il file di questa sessione, la cartella della seconda versione, il riassunto del pilota e la sua pull request: contengono frasi che ti farebbero riconoscere le versioni.

Appena decidi questi 3 punti, la sessione è chiusa.

# Dubbi rinviati

Si scrivono nei file delle sessioni che li ricevono dopo la scelta del PI, perché citano le rese della versione scelta: l'elenco è al punto 6 della sezione «Da fare dopo la scelta del PI».

# Da dove vengono i numeri del riassunto

| frase | comando o file | valore letto |
|---|---|---|
| due EPUB validi | `blind --a translation/final --b trial-b/final --chunks 01,18`, poi `epubcheck` su ciascuno dei due file | 0 errori e 0 avvisi per entrambi; titoli «Blindsight (pilota X)» e «Blindsight (pilota Y)» letti nei metadati |
| ha superato tutti i controlli | `verify` in apertura e prima del sorteggio; `check 01 --stage draft --dir trial-b/draft`, `coverage 01 --file trial-b/review/01-findings.tsv`, `check 01 --stage final --dir trial-b/final`, gli stessi per il 18 | 50 file; cancelli superati su 54 e 203 paragrafi; copertura 54 e 201 paragrafi |
| dieci previsioni tutte confermate | sezione «Esiti delle previsioni per blocco» | 10 su 10 |
| nessun file del pilota è stato toccato | `git diff` fra il ramo principale e il ramo della sessione su `translation`, `review`, `checks`, `source` | 0 righe |
| tra il 10 e l'11% più lungo | `checks/01-final.json`, `checks/18-final.json`, `trial-b/checks/01-final.json`, `trial-b/checks/18-final.json`, campo `ratio_median` | 1,102 e 1,106; 1,106 e 1,114 |
| 28 minuti con Opus e 46 con Fable, il 60% in più | file della sessione del pilota (676 e 1.024 secondi); durate riportate dall'ambiente in questa sessione (sezione «Tempi misurati») | 1.700 secondi e 2.756 secondi; rapporto 1,62 |
| circa 19 ore invece di 14 | formula di `docs/plan.md` con i tempi per mille parole delle due prove (sezione «Tempi misurati») | 19,1 e 13,5 ore |
| errori gravi: 2 con Opus, 1 con Fable | `coverage 01`, `coverage 18`; gli stessi con `--file trial-b/review/...` | alti: 0 e 2; 0 e 1 |
| paragrafi cambiati dal redattore | campo `changed_share` dei quattro file dei controlli finali; conteggio dei paragrafi diversi fra prima stesura e versione finale della prova B | 0,148 (8 su 54) e 0,154 (31 su 201); 0,278 (15 su 54) e 0,164 (33 su 201) |
| tre frasi compaiono alla lettera solo in una versione | ricerca delle tre frasi nei file finali delle due versioni | 1, 1, 1 occorrenze in una; 0, 0, 0 nell'altra |
| il 5% del libro | `status` | 5.187 parole su 104.639 |
| 8 regole nate dalla prima | file della sessione del pilota; decisioni sulla maiuscola di Sintesi (D-28) e sui termini del pilota (D-29) | 1 + 7 |
| il punto dentro le caporali allo stesso modo | conteggio di punto e caporale nei file finali delle due versioni | 13 e 100 casi dentro, 0 fuori, in ciascuna |
| circa 5 ore e mezza di macchina in meno | differenza fra le due stime | 19,1 meno 13,5 = 5,6 |
| circa 5.300 parole | conteggio delle parole dei file finali senza marcatori | 5.320 e 5.368 |
| una sola volta a metà frase, 74 minuscole | ricerca di Scrambler e scrambler nei blocchi sorgente | 12 maiuscole, 11 a inizio frase o in un titolo; 74 minuscole |
| entrambe le versioni usano la minuscola | ricerca nei file finali del blocco 01 delle due versioni | 2 minuscole e nessuna maiuscola a metà frase in ciascuna |
| tre espressioni che tornano in altri blocchi | ricerca nei blocchi sorgente | spinal bundle nei blocchi 05, 11, 18, 31; jarhead in 07 e 18; on top, in questo senso, in 18 e 36 |
