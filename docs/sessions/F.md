---
type: Session
title: "F: coerenza sull'intero libro ed EPUB"
description: Controlla che termini, nomi, forme di cortesia e voce siano coerenti dall'inizio alla fine, fa una controprova a campione sull'originale e costruisce l'EPUB definitivo.
model: opus
status: open
pi_approval: pending
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

# Cosa fa

Ogni blocco è stato rivisto da solo. Questa sessione guarda il libro intero: le incoerenze che un revisore di blocco non può vedere (un personaggio che passa dal tu al lei senza motivo, un termine reso in due modi in parti diverse, un nome scritto in due modi), poi costruisce l'EPUB.

# Dubbi ricevuti

Dalla sessione sulla sorgente (S0), da chiudere qui perché richiedono l'EPUB finito:

1. Copertina. Per decisione del PI (decisione sulla copertina, D-17) la copertina è `epub/cover.jpg`, il fronte della sovraccoperta fornita dal PI, e lo script la inserisce da solo. Misura 606 per 897 pixel, poco per uno schermo ad alta densità. Per chiuderlo: guardarla nell'EPUB finale e chiedere al PI se gli va bene così o se vuole procurare un'immagine più grande.
2. Impaginazione riportata dalla pagina. 58 paragrafi hanno un'impaginazione propria (dedica e scritte centrate, messaggi rientrati, il passo a tre colonne nel blocco 04) e c'è una figura nel blocco 06. In S0 la resa è stata controllata in un browser, sul testo inglese. Per chiuderlo: guardarla nell'EPUB finale e dire al PI di controllarla sul suo lettore.

# Procedura

1. `python3 tools/blindsight.py check all --stage final`: tutti i cancelli superati su tutti i blocchi.
2. `python3 tools/blindsight.py glossary --stage final`: per ogni voce approvata, i paragrafi tradotti che contengono il termine inglese devono contenere la resa italiana. Spiegare o correggere ogni scarto.
3. Lettura di coerenza. Per ciascuna parte del libro lanciare un sotto-agente `reviewer` in modalità coerenza (istruzioni nel prompt: leggere solo l'italiano dei blocchi finali della parte, con `docs/characters.md` e il glossario; registrare in `review/coherence-<parte>.tsv` incoerenze di forme di cortesia, nomi, termini, tempi verbali del narratore, ripetizioni di formule; non proporre riscritture di stile). Poi, per ogni rilievo, un sotto-agente `editor` sul blocco interessato applica la correzione verificandola sull'inglese.
4. Controprova a campione: 20 paragrafi scelti a caso con un seme fissato (per esempio `python3 -c "import random; random.seed(20261109); ..."` sugli id dei paragrafi di testo), letti dall'agente in inglese e in italiano. Ogni errore trovato è un dubbio da chiudere; più di 2 errori di senso su 20 riaprono la revisione delle parti coinvolte.
5. `python3 tools/blindsight.py build`: EPUB definitivo in `build/Blindsight-it.epub`, con `epubcheck`.
6. Controllo dell'EPUB: indice con le parti nell'ordine giusto, epigrafi in originale al loro posto, nota sulla traduzione in fondo, nessun marcatore o segnaposto rimasto (`unzip -p build/Blindsight-it.epub | grep -c "ORIGINALE\|<!-- p"` deve dare 0).
7. Riassunto e chiusura. Messaggio finale con il percorso dell'EPUB e come copiarlo sull'e-reader.

# Precisazioni prima di cominciare

Scritte e committate il 2026-11-13, prima della lettura di coerenza e della controprova (decisione sulla lettura di coerenza e sulla controprova di F, D-86).

1. Lettura di coerenza in quattro gruppi di blocchi, non cinque parti: dal 01 al 14 (Prologue e Theseus), dal 15 al 26 (prima metà di Rorschach), dal 27 al 39 (seconda metà di Rorschach e Charybdis), 40 e 41 (Acknowledgments, Notes and References). Rorschach da sola è più di metà del libro, Prologue e Charybdis sono un blocco ciascuno. I quattro lettori lavorano in parallelo: leggono e scrivono solo file propri, la traduzione non la toccano.
2. Ogni lettore legge solo l'italiano, come chiede la procedura, e scrive due file: `review/coherence-<blocchi>.tsv` con i rilievi (colonne `pid`, `type`, `severity`, `problem`, `related`, `proposal`) e `review/coherence-<blocchi>-inventory.tsv` con l'inventario di ciò che deve restare uguale in tutto il libro (forme di cortesia osservate, chi a chi, con i paragrafi; termini ricorrenti fuori dal glossario; formule ripetute; nomi e soprannomi). Per l'inventario dei termini il lettore può aprire l'inglese, solo per sapere quale parola inglese sta dietro una resa. Un lettore che vede una parte sola non può accorgersi che un termine cambia da una parte all'altra: il confronto fra parti lo fa la chat principale unendo i quattro inventari.
3. Il lettore delle note (blocchi 40 e 41) controlla anche che i concetti e le frasi del romanzo citati nel saggio abbiano la stessa resa che hanno nel romanzo, cercandoli nella versione finale degli altri blocchi.
4. Controlli meccanici della chat principale sull'intero libro, che completano la lettura: frasi e spezzoni di almeno sei parole che Watts ripete in paragrafi lontani (devono avere la stessa resa, salvo un motivo nel testo), grafie dei nomi propri, segni tipografici, caporali aperte e chiuse. Sono stati fatti prima di scrivere queste precisioni, e i loro rilievi entrano nel conto come quelli dei lettori.
5. Conto della previsione sulle incoerenze. Si contano le incoerenze confermate dopo la verifica sull'inglese: la stessa cosa resa in due modi senza un motivo nel testo, o una resa che si discosta dalla scheda dei personaggi, dal glossario o dalla guida. Un'incoerenza che tocca più paragrafi conta una volta. I rilievi non fondati si contano a parte e si dicono nel riassunto. I refusi e gli errori di lingua trovati leggendo (accordi, lettere) si correggono ma non sono incoerenze e si contano a parte.
6. Correzioni: un sotto-agente `editor` per ogni blocco con rilievi fondati, uno alla volta, che modifica solo i paragrafi indicati verificandoli sull'inglese e aggiunge al registro del redattore del blocco una sezione sulla coerenza; poi il controllo del blocco e il commit.
7. Controprova a campione. Seme 20261109. Popolazione: i paragrafi di testo (tipo `t`) dei blocchi dal 01 al 41, senza titoli, separatori, epigrafi, segnaposto `[[ORIGINALE]]` e senza i paragrafi della versione finale identici all'inglese (i riferimenti bibliografici che restano in inglese per regola). Estrazione: `random.seed(20261109); random.sample(sorted(ids), 20)`. Errore di senso: l'italiano dice una cosa diversa dall'inglese, omette o aggiunge contenuto (la gravità alta della revisione bilingue); gli altri rilievi (sfumature, ritmo) si contano a parte. Se un paragrafo estratto cambia dopo per la coerenza, si rilegge nella versione nuova.

# Cancelli

1. `verify` superato.
2. `check all --stage final` superato su tutti i blocchi.
3. `build` superato, `epubcheck` senza errori.
4. Nessun marcatore o segnaposto nell'EPUB.

# Previsioni

| quantità | atteso | intervallo di rilevanza | se è fuori |
|---|---|---|---|
| errori di senso nella controprova a campione | 0 | da 0 a 2 su 20 | sopra: si riapre la revisione delle parti coinvolte |
| incoerenze trovate nella lettura di coerenza, sull'intero libro | 15 | da 0 a 40 | sopra: un problema sistematico (glossario o forme di cortesia non applicati), da capire prima di correggere |

# In breve

(da scrivere alla chiusura)

# Dubbi rinviati

(nessuno finora)

# Da dove vengono i numeri del riassunto

(da compilare)
