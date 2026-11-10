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

Limite visto in apertura: il riassunto del pilota, che il PI ha letto, citava tre rese della versione A (il gioco sul titolo, i congiuntivi di Pag, una battuta di Szpindel). La prima è fissata dal glossario ed è uguale nelle due versioni; le altre due, se il PI le ricorda, possono fargli riconoscere la versione A. Detto al PI nel messaggio di apertura, con l'indicazione di non rileggere quel riassunto prima di scegliere.

Ogni sotto-agente della prova B riceve nel prompt il divieto di aprire `translation/`, `review/`, `checks/`, `build/`, `docs/sessions/`, `docs/decisions.md` e `docs/log.md`, che contengono la versione A o ne citano le rese: la prova B deve essere indipendente.

Il controllo sui blocchi della prova B, lanciato con `--save`, scriveva in `checks/` con lo stesso nome dei risultati della versione A e li avrebbe sovrascritti. Corretto prima del primo controllo: con la cartella alternativa i risultati vanno in `trial-b/checks/` (decisione sui risultati dei controlli della prova B, D-32). I due EPUB anonimi hanno un titolo proprio, per distinguerli nel lettore (decisione sul titolo dei due EPUB del confronto, D-31).

Il PI ha precisato durante il lavoro di non avere scaricato nessun EPUB: i due file del confronto gli si consegnano entrambi in questa chat.

# Tempi misurati

| blocco | passaggio | inizio | fine | minuti |
|---|---|---|---|---|
| 01 | traduttore | 10:43:12 | 10:49:50 | 6,6 |
| 01 | revisore | 10:50:06 | 10:57:07 | 7,0 |
| 01 | redattore | 10:57:39 | 11:02:31 | 4,9 |

Orari UTC del 2026-11-10, prova B. Stessa convenzione del pilota: i minuti sono la durata del sotto-agente riportata dall'ambiente alla sua chiusura; la fine è l'ora di scrittura dell'ultimo file del passaggio, l'inizio è la fine meno la durata.

# Segnalazioni spiegate

| blocco | paragrafo | segnalazione | spiegazione o correzione |
|---|---|---|---|
| 01 | p00058 | glossario: pod, atteso capsula | Falso allarme, lo stesso del pilota. Pod people sono gli ultracorpi del film, non le capsule di ibernazione: resa «ultracorpi». |
| 01 | p00060 | glossario: drum, atteso tamburo | Falso allarme, lo stesso del pilota. È il verbo to drum up, reso «mobilitare l'indignazione del quartiere»; non è il tamburo della nave. |

# Termini proposti dai traduttori

Valgono per la prova B. Se la prova B vince il confronto, i termini che tornano in altri blocchi si decidono al punto 5 della procedura, prima della chiusura; se perde, restano nei file della prova e non toccano il glossario.

| blocco | termine | decisione |
|---|---|---|
| 01 | optimized, mongrel, polly, sandbox buddy, sentry, seizures, wiring e rewiring, algorithms, engineered superboys, radical hemispherectomy, krill, checklists | Parole comuni o usi singoli: restano le rese del traduttore, confermate dal revisore. Polly resta invariato in corsivo: è un insulto opaco anche in inglese. |
| 01 | pod people | Ultracorpi, minuscolo, dalla voce del glossario sul soprannome di Siri. Nessuna voce nuova. |
| 01 | gamespace | Spazio di gioco. Compare solo qui. |
| 01 | playground | Parco giochi. Compare anche nel blocco 13: da uniformare al punto 5 se vince la prova B. |
| 01 | Scramblers con la maiuscola a metà frase (p00062) | Il traduttore aveva tenuto la maiuscola della sorgente; revisore e redattore hanno applicato la minuscola del glossario. Nella sorgente la maiuscola a metà frase c'è solo qui (conteggio sui blocchi sorgente: 12 maiuscole, 11 a inizio frase o in un titolo; 74 minuscole). Serve una regola nel glossario: si scrive al punto 5, per non cambiare il glossario durante il confronto. |
| 01 | tempo della narrazione | La guida di stile non ha una regola. La prova B usa il passato prossimo per la cornice (Siri che parla dalla bara) e il passato remoto per l'infanzia. È una scelta che vincola tutto il libro: entra nelle domande di lettura per il PI, e la scelta della versione vincente diventa regola della guida al punto 5. |

# Esiti delle previsioni per blocco

| blocco | quantità | valore | esito |
|---|---|---|---|
| 01 | rapporto di lunghezza mediano, prima stesura | 1,086 | confermata |
| 01 | rapporto di lunghezza mediano, versione finale | 1,106 | confermata |
| 01 | quota di paragrafi cambiati dal redattore | 0,278 (15 su 54) | confermata |
| 01 | rilievi di gravità alta | 0 | confermata |
| 01 | tempo di macchina, tre passaggi | 18,5 minuti | confermata |

Rilievi della revisione sul blocco 01: 15 rilievi veri (2 medi, 13 bassi) più 30 righe di parere sui 29 dubbi del traduttore (2 medie, 28 basse). I medi: in p00013 «peculiare» era un falso amico di peculiar, ora «singolare»; in p00027 «Non ero estraneo agli scherni» ricalcava I was no stranger to e si poteva leggere come se Siri partecipasse agli scherni; in p00044 un imperfetto faceva di un'ipotesi un'abitudine; in p00062 la maiuscola di Scrambler. Il redattore ha accettato 14 rilievi veri su 15 e ne ha respinto 1, basso (p00059, «spremuto fuori» resta); dei 30 pareri ne ha accolti 29 (25 sono conferme senza modifica) e ne ha respinto 1 (p00064, «a farci visita» resta). Nessun intervento redazionale proprio.

# In breve

(da scrivere alla chiusura)

# Dubbi rinviati

(nessuno finora)
