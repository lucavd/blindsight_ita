# Blindsight in italiano

Pacchetto per tradurre con Claude Code *Blindsight* di Peter Watts in italiano, per uso personale, e ottenerne un EPUB. Il testo del romanzo non è incluso: lo scarica la prima sessione dal sito dell'autore, che lo distribuisce con licenza Creative Commons BY-NC-SA (opere derivate ammesse senza scopo di lucro, con attribuzione e stessa licenza).

## Cosa serve

1. Claude Code.
2. Python 3.9 o successivo con `beautifulsoup4` e `lxml` (`python3 -m pip install beautifulsoup4 lxml`).
3. pandoc (`brew install pandoc` sul Mac).
4. epubcheck, consigliato per il controllo finale del formato (`brew install epubcheck`).
5. git.

Va bene il Mac o il server, purché la macchina raggiunga rifters.com.

## Permessi (facoltativo, consigliato)

Le sessioni di traduzione e revisione lanciano decine di volte gli stessi script e scrivono molti file. Per non dover approvare ogni passaggio, copia i permessi preparati nella configurazione del progetto prima della prima sessione:

```
mkdir -p .claude && cp setup/claude-settings.json .claude/settings.json
```

Consentono lettura e scrittura di file nella cartella del progetto, gli script del progetto, git (senza push), grep, pandoc, epubcheck e unzip. Nient'altro: lo scarico iniziale con curl e le ricerche web di S1 chiederanno comunque il tuo consenso. Claude Code applica questi permessi solo dopo che hai dato fiducia alla cartella.

## Come si lancia una sessione

```
cd blindsight-it
claude --model sonnet        # il modello lo dice la sessione: vedi sotto
```

Poi scrivi «sessione Blindsight». Claude legge `CLAUDE.md` da solo, ricava da `docs/state.tsv` a che punto siamo, controlla di girare con il modello giusto e ti dice in cinque righe cosa farà. Alla fine ti dà un riassunto e il comando esatto per la sessione successiva. Una sessione per chat; non serve cambiare modello dentro una chat.

| ordine | sessione | comando |
|---|---|---|
| 1 | S0, sorgente e blocchi | `claude --model sonnet` |
| 2 | S1, glossario e scelte | `claude --model opus` |
| 3 | S2, pilota | `claude --model opus` |
| 4 | S2b, confronto alla cieca (facoltativa) | `claude --model fable` |
| 5 | T1-T4, traduzione | il modello scelto nel pilota |
| 6 | R1-R6, revisione | il modello scelto nel pilota |
| 7 | F, coerenza ed EPUB | `claude --model opus` |
| 8 | C, correzioni dalle tue note (facoltativa) | `claude --model opus` |

Il numero esatto delle sessioni T e R lo fissa S0. Dettagli, tempi e motivi delle scelte in `docs/plan.md`.

## Quanto ci vuole

Tra 15 e 25 ore di macchina, stimate e non ancora misurate (la prima misura arriva dal pilota). Il limite pratico sono i limiti d'uso del tuo piano: se una sessione si interrompe, apri una nuova chat con lo stesso modello e scrivi di nuovo «sessione Blindsight»; riparte dal primo blocco non finito.

## Cosa fai tu

1. Dopo S1: decidi 4-6 punti (titolo, segni del dialogo e forma della lineetta, nomi, forme di cortesia, termini chiave). Circa mezz'ora.
2. Dopo S2: leggi `build/pilota.epub` (due blocchi) e dici cosa non va. Se vuoi confrontare due modelli, dopo S2b leggi due EPUB anonimi e scegli.
3. Dopo F: leggi il libro. Se annoti qualcosa in `docs/reading-notes.md`, la sessione C lo corregge.

## Collaudo degli script

`python3 tests/selftest.py` esegue l'intera catena su un HTML sintetico e verifica che i controlli scattino quando devono (paragrafo mancante, marcatore duplicato, carattere vietato, sorgente modificata, e altri). Lo lancia anche S0.
