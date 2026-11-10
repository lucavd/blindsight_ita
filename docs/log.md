---
type: Log
title: Registro delle modifiche
description: Cosa è cambiato nel progetto, per data, la voce più recente in alto.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

## 2026-11-10

La sessione sulla sorgente (S0) ha finito il lavoro e aspetta tre risposte del PI (provenienza dei file, copertina, modo di lavorare nel cloud). Sorgente: `Blindsight_html_format.htm`, dallo zip caricato dal PI nella chat, salvato come `source/original/Blindsight.htm` (1.268.419 byte, sha256 `c8cd6fbe0eb58d753ae526ce43404bb1a6fff96c082aae2c38468346e60e4a6f`; sha256 dello zip `7d0b2e95c1fff21bbfbdb84cec50cb472ab4829933ee6dce2cf0fa7446f3a7a6`). L'indirizzo da cui il PI ha preso lo zip non è ancora annotato. Licenza della sorgente in `source/original/LICENSE-source.txt`. Libro diviso in 41 blocchi (104.639 parole), tutti i cancelli superati; create le sessioni T1-T4 e R1-R6. Script adattato alla pagina reale (decisione sugli adattamenti dello script, D-15), collaudo portato a 38 controlli. In `reference/` lo zip, l'EPUB di confronto e l'immagine della sovraccoperta forniti dal PI.

Voci precedenti della stessa data, quando la sorgente non era ancora disponibile:

La sessione sulla sorgente (S0) è aperta ma ferma allo scarico: nessun file sorgente è stato scaricato. Dall'ambiente cloud la rete consente `www.rifters.com` e `rifters.com`, ma ogni connessione a `https://www.rifters.com/real/Blindsight.htm` cade dopo circa 11 secondi senza ricevere dati. I tentativi sono stati ripetuti tra le 05:32 e le 06:11 UTC, tutti con lo stesso esito (nel registro del proxy: `tunnel closed (code 1006) after 11s; 517 B sent, 39 B received`). Da qui non si distingue tra sito fermo e sito che respinge gli indirizzi del cloud.

Il PI ha scelto di prendere la copia dell'Internet Archive (decisione sulla sorgente d'archivio, D-11). Non è stato possibile farlo: `web.archive.org` non è tra i domini consentiti dell'ambiente e la richiesta dell'agente di aggiungerlo è stata rifiutata dal servizio. Cosa serve per ripartire è scritto nel file della sessione, sezione "Punto di ripresa".

Creato l'ambiente cloud `blindsight_ita` (decisione sul lavoro nel cloud, D-10). Su questa macchina epubcheck 4.2.6 è stato installato a mano e il collaudo degli script è stato rilanciato: 28 controlli superati.

## 2026-11-09

Pacchetto caricato sul repository `lucavd/blindsight_ita`, ramo `ccr-0a68a19e-9va3bz`. Il PI ha deciso che la sessione sulla sorgente si fa con Fable 5.2 invece di Sonnet (deroga sul modello di S0, D-09).

Il PI ha deciso che nella traduzione le lineette sono ammesse (D-08): aggiornati guida di stile, controlli automatici (resta vietata solo la lineetta lunga, per uniformità), punti da decidere in S1.

Pacchetto preparato: protocollo, piano delle sessioni, guida di stile, sotto-agenti, script con collaudo su un HTML sintetico (28 controlli superati). Il testo del romanzo non è incluso: lo scarica S0.
