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

# In breve

(da scrivere alla chiusura)

# Dubbi rinviati

(nessuno finora)
