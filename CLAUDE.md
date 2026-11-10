---
type: Playbook
title: "Blindsight in italiano: come si lavora una sessione"
description: Protocollo di ogni sessione del progetto di traduzione italiana di Blindsight di Peter Watts per uso personale, con un modello per sessione, controlli automatici, revisione indipendente e chiusura senza riserve.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
sources:
  - id: watts2006
    resource: https://www.rifters.com/real/Blindsight.htm
    title: "Peter Watts (2006). Blindsight. Testo online con licenza Creative Commons BY-NC-SA"
---

# Scopo

Traduzione italiana integrale e fedele di *Blindsight* di Peter Watts, dal testo che l'autore distribuisce online con licenza Creative Commons Attribuzione - Non commerciale - Condividi allo stesso modo[^watts2006], per uso personale del PI (Luca Vedovelli). Il prodotto finale è un EPUB.

Fedeltà vuol dire rendere in italiano il senso, il registro, il ritmo e le immagini di Watts, non la sintassi inglese. Watts non si migliora, non si chiarisce e non si attenua. Le regole di traduzione stanno in `docs/style-guide.md`; questo file dice come si lavora.

# Dove sta tutto

```
CLAUDE.md                  questo protocollo (si carica da solo a ogni chat)
README.md                  istruzioni per il PI
docs/plan.md               piano delle sessioni, modelli, tempi
docs/state.tsv             stato di ogni sessione: da qui si ricava dove siamo
docs/sessions/<id>.md      una sessione per file: attese, procedura, riassunto
docs/style-guide.md        regole di traduzione (vincolanti)
docs/glossary.tsv          glossario (le voci approved sono vincolanti)
docs/characters.md         personaggi, registro, forme di cortesia
docs/epigraphs.tsv         epigrafi: chi le ha scritte, si traducono o no
docs/plot-summary.md       riassunto della trama blocco per blocco (continuità)
docs/decisions.md          decisioni del PI e decisioni tecniche
docs/log.md                registro delle modifiche, la più recente in alto
source/original/           pagina HTML scaricata (sola lettura)
source/chunks/NN.md        il testo inglese diviso in blocchi (sola lettura)
source/SHA256SUMS          impronte della sorgente
source/excluded.tsv        intervalli della pagina che non sono il libro (sola lettura)
source/figures.tsv         figure del libro e paragrafo dopo cui vanno (sola lettura)
reference/                 file forniti dal PI: zip della sorgente, EPUB di confronto, sovraccoperta
translation/draft/NN.md    prima stesura
translation/notes/NN.md    dubbi del traduttore, termini proposti, riassunto del blocco
review/NN-findings.tsv     revisione bilingue, una riga almeno per paragrafo
review/NN-editor-log.md    cosa ha accettato o respinto il redattore, e perché
translation/final/NN.md    versione finale
checks/                    risultati dei controlli automatici (checks/S0: controlli sulla sorgente)
build/                     EPUB (non versionato)
docs/reading-notes.md      note di lettura del PI (sessione C, se serve)
tools/blindsight.py        tutti gli script; tools/config.json soglie e caratteri vietati
tests/selftest.py          collaudo degli script su un HTML sintetico (tests/fixture.htm)
epub/                      metadati, foglio di stile, nota sulla traduzione, copertina
setup/claude-settings.json permessi proposti per Claude Code (li installa il PI)
.claude/agents/            traduttore, revisore, redattore, esploratore del glossario
```

Comandi degli script: `python3 tools/blindsight.py --help`.

# Regole non negoziabili

1. La sorgente non si tocca dopo la prima sessione. `python3 tools/blindsight.py verify` si lancia in apertura di ogni sessione; se fallisce ci si ferma.
2. Un modello per sessione, e lo stesso modello per un intero passaggio (tutte le sessioni di traduzione con lo stesso modello, tutte quelle di revisione con lo stesso modello). Il modello previsto è in `docs/state.tsv`. In apertura l'agente confronta il modello con cui sta girando con quello previsto: se non coincidono, si ferma e dice al PI con quale comando riaprire la chat. I sotto-agenti del progetto hanno `model: inherit` e non lo cambiano; non si passa mai un modello diverso quando li si lancia.
3. Niente omissioni e niente aggiunte. Ogni paragrafo inglese ha il suo marcatore e il suo paragrafo italiano; nessuna nota del traduttore dentro il testo.
4. Il glossario è vincolante per le voci `approved`. Un termine nuovo non si inventa in silenzio: si propone nelle note del blocco e si decide prima di chiudere la sessione.
5. Numeri dai file. Ogni conteggio citato in un riassunto viene dall'output degli script, rilanciati nella stessa sessione. Un numero senza fonte non entra.
6. Testi di terzi. Le epigrafi tratte da canzoni o poesie di autori reali non si traducono: il paragrafo contiene solo `[[ORIGINALE]]` e il testo inglese viene reinserito dallo script al momento di costruire l'EPUB. Nessun agente riscrive quei versi.
7. Una sola chat alla volta sul progetto. Si fa un commit dopo ogni blocco completato e alla chiusura della sessione.
8. Contesto pulito. La chat principale coordina: lancia i sotto-agenti, legge i risultati dei controlli e solo i paragrafi segnalati. Non carica nel proprio contesto blocchi interi se non serve.

# Chi decide

Il PI decide: titolo, convenzioni tipografiche, forme di cortesia tra personaggi, resa dei termini chiave del glossario, modello da usare nei passaggi di traduzione e revisione, ogni scelta che cambia il senso di un passo, ogni deroga a questo protocollo. Gli si portano al massimo 3 opzioni per decisione, con una raccomandazione.

Il resto lo decide l'agente e lo registra in `docs/decisions.md` come decisione tecnica (`deciso da: agente`), con una riga di motivazione.

# Attese: cancelli e previsioni

Ogni file di sessione elenca, prima del lavoro, cancelli e previsioni. Si scrivono e si committano prima di cominciare e dopo il risultato non si cambiano, né si cambia il lavoro per far tornare un numero.

I cancelli sono controlli binari: se uno fallisce, il blocco o la sessione non sono validi finché non si corregge. Sono quelli degli script (marcatori, paragrafi vuoti, separatori, caratteri vietati, segnaposto, copertura della revisione, integrità della sorgente, formato dell'EPUB).

Le previsioni hanno un valore atteso e un intervallo di rilevanza: lo scarto oltre il quale qualcosa nel lavoro va cambiato. Esito confermata (dentro l'intervallo) o smentita (fuori: è un risultato e apre un dubbio da spiegare). L'unità è il blocco: con molti blocchi si giudica prima la mediana, poi si contano i blocchi fuori intervallo e si spiega ciascuno.

| quantità | atteso | intervallo di rilevanza | se è fuori |
|---|---|---|---|
| rapporto di lunghezza italiano/inglese, mediana dei paragrafi del blocco | 1,15 | da 1,00 a 1,35 | sotto: cercare omissioni; sopra: cercare aggiunte o parafrasi |
| quota di paragrafi cambiati dal redattore | 0,35 | da 0,15 a 0,70 | sotto: revisione superficiale; sopra: prima stesura debole o redattore che riscrive |
| rilievi di gravità alta della revisione bilingue, per blocco | 1 | da 0 a 4 | sopra: la prima stesura non è affidabile, si rivedono le istruzioni del traduttore prima di proseguire |

Le segnalazioni degli script (paragrafi fuori dai limiti di lunghezza, parole inglesi rimaste, voci del glossario non rispettate, corsivi diversi, paragrafi identici all'inglese) non bloccano da sole, ma sono dubbi: ognuna va spiegata o corretta prima di chiudere la sessione.

# Chiusura della sessione

1. Verdetto: chiusa o non chiusa. "Chiusa con riserve" non esiste.
2. È chiusa quando non resta alcun dubbio aperto e il PI ha letto il riassunto senza sollevarne di nuovi. Dubbio: cancello fallito, previsione smentita non spiegata, segnalazione non spiegata, anomalia vista durante il lavoro, scelta che spetta al PI.
3. L'agente prova per primo a chiudere ogni dubbio: legge i paragrafi coinvolti, corregge se è un errore, spiega se non lo è. Porta al PI solo le scelte che gli spettano.
4. Rinvio: ammesso solo quando chiuderlo richiede il lavoro di una sessione successiva. Si scrive nella sezione "Dubbi ricevuti" del file della sessione che lo riceve (cosa, perché, cosa serve per chiuderlo) e lì si legge per primo.

# Come si lavora una sessione

1. Apertura, pochi minuti.
   1. `git status -sb && git log --oneline -n 5`. Lavoro non committato vuol dire un'altra chat attiva o una sessione interrotta a metà blocco: fermarsi e chiedere al PI.
   2. `python3 tools/blindsight.py verify` (salvo in S0, quando la sorgente non esiste ancora).
   3. Leggere `docs/state.tsv`. La sessione corrente è la prima con stato `open` (interrotta: si riprende dal primo blocco non completato, visibile con `python3 tools/blindsight.py status`) oppure, se non ce ne sono, la prima `todo`. Le sessioni `optional` si aprono solo se il PI le ha chieste.
   4. Se la sessione precedente ha `pi_approval` uguale a `pending`, mostrare il suo riassunto e chiedere l'ok prima di aprire la nuova.
   5. Controllare il modello (regola 2).
   6. Leggere il file della sessione, prima i dubbi ricevuti; poi `docs/decisions.md` per le decisioni successive all'ultima chiusura.
   7. Dire al PI in 5 righe: dove siamo, cosa fa questa sessione, quanto dovrebbe durare, cosa gli verrà chiesto alla fine.
2. Lavoro, secondo il file della sessione. Nelle sessioni a blocchi: un sotto-agente alla volta, si aspetta che finisca, si lanciano i controlli, si corregge un cancello fallito prima di passare al blocco successivo (rilanciando lo stesso tipo di sotto-agente con l'output del controllo), si fa il commit del blocco.
3. Chiusura: riassunto «In breve» nel file della sessione; `docs/state.tsv` aggiornato (stato, `pi_approval: pending`); voce in `docs/log.md`; commit e `git log --oneline -n 1`.
4. Messaggio al PI: il riassunto «In breve» così com'è. Se la sessione è chiusa, l'ultima riga dice quale sessione viene dopo e con quale comando aprirla, per esempio: "Sessione T1 chiusa: per la successiva apri una nuova chat nella cartella del progetto con `claude --model opus` e scrivi «sessione Blindsight»."

Quando il PI approva il riassunto, si scrive `pi_approval: yes` in `docs/state.tsv` e nel file della sessione, con la data, e si fa il commit.

# Lavoro nel cloud

Questa sezione vale quando la sessione gira in Claude Code nel cloud e non sul Mac o sul server (decisione del PI sul lavoro nel cloud, D-18). Il resto del protocollo non cambia.

1. Si apre una sessione nuova sul repository, nell'ambiente cloud `blindsight_ita`, scegliendo nell'app il modello previsto. Il comando `claude --model ...` nel cloud non esiste: dove il protocollo lo cita, si intende questa scelta.
2. In apertura, prima di ogni altro passo, si controlla che il ramo principale contenga il lavoro dell'ultima sessione: si guardano i rami remoti (`git ls-remote --heads origin`) e le pull request aperte. Una pull request aperta, o un ramo di sessione con commit che il ramo principale non ha, vuol dire che la sessione precedente non è stata unita: fermarsi e dirlo al PI, perché ripartire da lì rifarebbe lavoro già fatto.
3. In apertura si controlla anche `epubcheck --version`: lo installa lo script di avvio dell'ambiente. Se manca, dirlo al PI.
4. A ogni commit segue un push sul ramo della sessione.
5. In chiusura, dopo il commit di chiusura e il push, si apre una pull request dal ramo della sessione al ramo principale, con il riassunto «In breve» come descrizione. L'ultima riga del messaggio al PI dice di unirla prima di aprire la sessione successiva, e con quale ambiente e modello aprirla.
6. Se il PI approva il riassunto nella stessa chat, l'approvazione si registra e si spinge sullo stesso ramo prima dell'unione. Se la pull request è già stata unita, l'approvazione si registra in apertura della sessione successiva.
7. Gli EPUB non sono versionati: si consegnano al PI come file nella chat che li produce.

# Il riassunto «In breve»

È la prima cosa che il PI legge di una sessione, spesso l'unica: deve bastare per capire cosa è successo e per decidere. Si scrive per ultimo, a numeri verificati, nella sezione `# In breve` del file della sessione.

Struttura, sempre questa:

1. Titolo: `## In breve: <la domanda della sessione, in parole semplici>?`
2. A cosa serviva: due o tre frasi.
3. Cosa abbiamo trovato: al massimo 5 punti numerati. La prima frase di ogni punto dice da sola il risultato, così chi legge solo le prime frasi ha il messaggio; sotto, solo il dettaglio che serve a capirlo.
4. Cosa devi decidere: un punto per decisione (da 0 a 5 in S1, da 0 a 3 altrove). La prima frase contiene la domanda e la raccomandazione; poi le ragioni; poi le alternative, ciascuna con la sua conseguenza sul libro o sul lavoro.
5. Comunque: cosa si farà in ogni caso, compreso ciò che passa a una sessione successiva.
6. Riga di chiusura: "Appena decidi questi N punti, la sessione è chiusa." Con un punto: "Appena decidi questo punto, la sessione è chiusa." Senza decisioni: "Non c'è nulla da decidere: se non hai dubbi, la sessione è chiusa." Se un cancello è fallito la sessione non si chiude: lo dice il primo dei risultati e la riga di chiusura dice cosa serve.

Regole del riassunto: nessun codice interno (niente numeri di decisione, niente nomi di file o di colonne, niente id di paragrafo); i blocchi si nominano con la parte del libro ("i blocchi dal 5 al 14, da metà della parte Theseus all'inizio di Rorschach"); esempi di traduzione brevi, una frase inglese e la sua resa, solo se servono a decidere; numeri solo se servono, in unità concrete ("3 paragrafi su 80").

In appendice al file della sessione va la tabella "Da dove vengono i numeri del riassunto": frase, comando o file, valore letto.

# Linguaggio

Documenti di progetto e conversazione in italiano, con gli accenti giusti; codice e nomi di colonne in inglese. Frasi brevi, un'idea per frase, prima la conclusione e poi il dettaglio. Nei documenti di progetto niente lineette lunghe o medie come punteggiatura (si usano virgole, parentesi o si riscrive la frase) e niente elenchi in cui ogni voce si apre con un'etichetta in grassetto. Questo divieto vale per i documenti di progetto e per la conversazione, non per il romanzo: nella traduzione le lineette sono ammesse e seguono la guida di stile (decisione del PI sulle lineette nella traduzione, D-08).

Un codice interno (decisione D-nn, sessione, blocco) nei documenti si scrive sempre insieme a cosa è: "la decisione sulle lineette nella traduzione (D-08)", mai "D-08" da solo.

[^watts2006]: Peter Watts, *Blindsight*, Tor 2006; testo online sul sito dell'autore.
