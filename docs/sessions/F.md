---
type: Session
title: "F: coerenza sull'intero libro ed EPUB"
description: Controlla che termini, nomi, forme di cortesia e voce siano coerenti dall'inizio alla fine, fa una controprova a campione sull'originale e costruisce l'EPUB definitivo.
model: opus
status: closed
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

# Risultati

## Cancelli

| cancello | esito | fonte |
|---|---|---|
| `verify` | superato (50 file) | `python3 tools/blindsight.py verify`, in apertura |
| `check all --stage final` | superato su 41 blocchi, prima e dopo le correzioni di coerenza | `checks/F/check-all-final.txt`, `checks/F/check-all-final-after.txt` |
| `build` ed `epubcheck` | superato: 0 errori, 0 avvisi | `python3 tools/blindsight.py build`, EPUB in `build/Blindsight-it.epub` |
| marcatori e segnaposto nell'EPUB | 0 | `unzip -p build/Blindsight-it.epub \| grep -a -c "ORIGINALE\|<!-- p"` |

## Previsioni

| quantità | atteso | intervallo | valore | esito |
|---|---|---|---|---|
| errori di senso nella controprova a campione | 0 | da 0 a 2 su 20 | 0 su 20 | confermata |
| incoerenze confermate sull'intero libro | 15 | da 0 a 40 | 17 | confermata |

Controprova (`checks/F/sample.tsv`): 20 paragrafi su una popolazione di 3.633, letti dalla chat principale in inglese e in italiano. Nessun errore di senso e nessun altro rilievo; quattro paragrafi hanno una nota che spiega perché la resa regge (accordo di «Scartata» con la fabbrica, «rotazione-contro-spam» che ricalca una parola strana già nell'inglese, l'errore voluto di Rorschach ricreato, «ribatteva» in una lite a parole). Il p02650, cambiato dopo dalla coerenza («in BioMed»), è stato riletto: resta corretto.

Incoerenze (`review/coherence-corrections.tsv`): 17, in 21 paragrafi di 14 blocchi; 4 di gravità media, 13 bassa, nessuna alta. I quattro lettori ne hanno segnalate 13, tutte fondate (01-14: 1; 15-26: 6; 27-39: 2; 40-41: 4); i controlli meccanici della chat principale 6, di cui 2 trovate anche da un lettore. Rilievi non fondati: 0. Refusi ed errori di lingua: 0. Forme di cortesia: nessuna incoerenza; gli inventari delle quattro parti coincidono fra loro e con la scheda dei personaggi. Le 17 correzioni sono state applicate tutte dai redattori, uno per blocco, nessuna respinta.

| voce | gravità | cosa | blocchi |
|---|---|---|---|
| I01 | bassa | mission-critical: «critico per la missione» ovunque (era anche vitale, cruciale, essenziale) | 02, 07, 29 |
| I02 | bassa | We're taking you first: «Prenderemo te per prima» anche nel ricordo di Susan | 20 |
| I03 | bassa | tactical overlays: «sovrimpressioni», come nel resto del libro | 12 |
| I04 | media | la *Scylla* con l'articolo, come la *Theseus* e la *Charybdis* | 16 |
| I05 | bassa | big picture: «quadro generale» anche in minuscolo | 15 |
| I06 | bassa | flickering at the edge of vision: «guizzava», come la prima volta | 23 |
| I07 | media | il motto delle prede uguale nell'epigrafe e nella citazione: «per salvarsi la vita» | 18 |
| I08 | bassa | in–visibile di Michelle senza spazio, come nella ripresa | 20 |
| I09 | media | breaking and entering: «scasso» anche nella ripresa | 22 |
| I10 | bassa | «in BioMed» | 29 |
| I11 | bassa | una sola grafia, «scoregge» | 27, 40 |
| I12 | bassa | think rings around: «col pensiero ti stracciano» | 34 |
| I13 | bassa | «tamburo» minuscolo nei ringraziamenti | 40 |
| I14 | bassa | «Leu-encefalina» nel saggio, come nel romanzo | 40 |
| I15 | bassa | richiamo di nota «per es.» in apice, come nel resto del saggio (spazio protetto perché pandoc lo legga come apice) | 40 |
| I16 | media | heavy-atom tunnelling: «effetto tunnel» nel saggio, come nel romanzo | 40 |
| I17 | bassa | «potenziamenti di carboplatino» nel saggio, come nel romanzo | 41 |

Segnalazioni dei controlli: identiche, paragrafo per paragrafo, a quelle già spiegate nelle sessioni di revisione (confronto fra `checks/F/check-all-final.txt` e `checks/F/check-all-final-after.txt` senza differenze, a parte la quota di paragrafi cambiati). Il controllo del glossario sulla versione finale dà lo stesso risultato prima e dopo le correzioni: 76 paragrafi non conformi in 26 voci, gli stessi spiegati nelle sessioni di revisione.

EPUB: indice nell'ordine Blindsight (dedica ed epigrafi iniziali), Prologo, Theseus, Rorschach, Charybdis, Ringraziamenti, Note e riferimenti, Nota sulla traduzione; le 5 epigrafi d'autore reinserite in inglese al loro posto; identificativo fisso (decisione sull'identificativo dell'EPUB, D-87). Impaginazione speciale guardata in Chromium sulle pagine dell'EPUB: dedica ed epigrafi centrate, il passo a tre colonne del blocco 04, i messaggi centrati e rientrati, la figura del cubo di Necker nel blocco 06; tutto al suo posto.

## Dubbi ricevuti

1. Copertina: guardata nell'EPUB finale. Misura 606 per 897 pixel; nitida in miniatura, un po' morbida a tutto schermo su un lettore ad alta densità. Scelta del PI, nel riassunto.
2. Impaginazione riportata dalla pagina: guardata nell'EPUB finale (sopra), corretta. Il PI la controlla sul suo lettore; è scritto nel riassunto.

## Tempi

Lettura di coerenza: quattro lettori in parallelo, da 6,5 a 9,8 minuti ciascuno, 33,1 minuti di sotto-agenti, circa 10 minuti di orologio. Correzioni: 15 lanci di redattore (14 blocchi e una ripresa per lo spazio nell'apice), 4,5 minuti in tutto. Sotto-agenti 37,7 minuti; dalla prima verifica all'EPUB finale circa 35 minuti di orologio, controlli meccanici, controprova e costruzione comprese.

# In breve

## In breve: il libro è coerente dall'inizio alla fine, e l'EPUB è pronto?

Questa era l'ultima sessione prevista. Ogni blocco era già stato tradotto e rivisto da solo; qui si guardava il libro intero, per trovare ciò che un revisore di blocco non può vedere: una cosa detta in due modi in parti diverse, un personaggio che cambia forma di cortesia, il saggio finale che chiama un concetto in modo diverso dal romanzo. Poi si costruiva l'EPUB definitivo.

Cosa abbiamo trovato:

1. L'EPUB è pronto e passa tutti i controlli di formato. Nessun errore e nessun avviso dal controllo ufficiale del formato, nessun segno di lavoro rimasto nel testo, l'indice ha le parti nell'ordine giusto, le epigrafi tratte da canzoni e poesie sono in inglese al loro posto e la nota sulla traduzione chiude il libro. Il file ha ora un'identità fissa: se lo rifacciamo dopo le tue note di lettura, il lettore lo riconosce come lo stesso libro, senza doppioni e senza perdere il segno.
2. Forme di cortesia, nomi e voci dei personaggi sono coerenti in tutto il libro. Quattro lettori hanno letto ciascuno una parte del libro, solo in italiano, e hanno annotato chi dà del tu, del lei o del voi a chi. Le quattro parti coincidono fra loro e con le scelte fatte all'inizio: il solo cambio è quello voluto, Bates che passa al tu con Sarasti quando lo affronta.
3. Le incoerenze erano 17, tutte piccole, e sono corrette; ne avevamo previste 15. Nessuna cambiava il senso; 4 si notavano. Il motto «Predators run for their dinner. Prey run for their lives» era reso in due modi a un capitolo di distanza, ora è sempre «Le prede corrono per salvarsi la vita». La navetta era «Scylla» in un capitolo e «la Scylla» negli altri, ora ha sempre l'articolo come la Theseus. Il «breaking and entering» di Bates era «scasso» nella battuta e «effrazione» quando Siri lo ricorda. Nel saggio finale c'era «tunneling» dove il romanzo dice «effetto tunnel». Le altre 13 erano minime: la stessa espressione resa con parole vicine ma diverse, una maiuscola, una preposizione. Tutte le segnalazioni dei lettori erano fondate.
4. La controprova a caso conferma la traduzione. Ho confrontato io con l'inglese 20 paragrafi estratti a caso da tutto il libro: nessun errore di senso, nessuna sfumatura persa.
5. L'impaginazione speciale è al suo posto: la dedica, le epigrafi, il passo a tre colonne con le notizie dopo la Pioggia di fuoco, i messaggi centrati, la figura del cubo. L'ho guardata in un browser, che non è un e-reader: va controllata anche sul tuo lettore. La sessione ha preso circa 35 minuti.

Cosa devi decidere:

1. La copertina resta quella di adesso? Ti consiglio di sì. È il fronte della sovraccoperta che mi hai dato, pulita e leggibile; misura 606 per 897 pixel, quindi nella libreria del lettore è nitida, mentre a tutto schermo su un lettore ad alta densità si vede un po' morbida. L'alternativa è che tu mi dia un'immagine più grande, almeno 1.600 pixel di altezza: la sostituisco e rifaccio l'EPUB in pochi minuti, senza toccare il testo, in questa chat o insieme alle tue note di lettura.

Comunque:

1. Quando leggi, guarda sul tuo lettore le pagine speciali: la dedica con le epigrafi all'inizio; nella prima parte di Theseus il passo a tre colonne con le notizie dopo la Pioggia di fuoco e, subito dopo, i messaggi centrati della chiamata del padre; qualche capitolo più avanti la figura del cubo.
2. Per copiare l'EPUB sul lettore: con un Kobo o un altro lettore EPUB basta collegarlo al computer e copiare il file, oppure usare Calibre; con un Kindle si usa Send to Kindle (dall'app o dal sito di Amazon), che accetta gli EPUB; sul telefono si apre con Apple Libri o Google Play Libri.
3. Se annoti errori o dubbi mentre leggi, la sessione facoltativa di correzioni li applica e rifà l'EPUB.

Appena decidi questo punto, la sessione è chiusa.

# Dubbi rinviati

Nessuno.

# Da dove vengono i numeri del riassunto

| frase | comando o file | valore letto |
|---|---|---|
| nessun errore e nessun avviso dal controllo del formato | `python3 tools/blindsight.py build` (epubcheck 4.2.6) | 0 fatals / 0 errors / 0 warnings / 0 infos |
| nessun segno di lavoro rimasto | `unzip -p build/Blindsight-it.epub \| grep -a -c "ORIGINALE\|<!-- p"` | 0 |
| l'indice ha le parti nell'ordine giusto | `EPUB/nav.xhtml` nell'EPUB | Blindsight, Prologo, Theseus, Rorschach, Charybdis, Ringraziamenti, Note e riferimenti, Nota sulla traduzione |
| le epigrafi in inglese al loro posto | script di confronto fra segnaposto e testo dell'EPUB | 5 segnaposto, 0 mancanti |
| identità fissa | `EPUB/content.opf` di tre costruzioni | urn:uuid:a16cd47e-8f58-43f4-8247-dad9a8c4854e in tutte |
| quattro lettori | `review/coherence-*-inventory.tsv` | 4 file, righe di forme di cortesia: 37, 44, 32 e 1 |
| il solo cambio è quello di Bates con Sarasti | `review/coherence-27-39-inventory.tsv`, riga Bates -> Sarasti | lei, poi tu da p03088 |
| 17 incoerenze, 4 che si notavano, 13 minime | `review/coherence-corrections.tsv` | 17 voci distinte in 21 righe (una per paragrafo); voci di gravità media 4, bassa 13 |
| ne avevamo previste 15 | sezione Previsioni di questo file | 15, intervallo da 0 a 40 |
| tutte le segnalazioni dei lettori erano fondate | `review/coherence-01-14.tsv`, `-15-26.tsv`, `-27-39.tsv`, `-40-41.tsv` | 13 rilievi, 13 nell'elenco delle correzioni |
| 20 paragrafi, nessun errore di senso | `checks/F/sample.tsv` | 20 righe, 20 ok |
| circa 35 minuti | orari dei comandi e dei commit della sessione | dalle 12.47 alle 13.20 circa |
| 606 per 897 pixel | `epub/cover.jpg`, letto con PIL | (606, 897) |
