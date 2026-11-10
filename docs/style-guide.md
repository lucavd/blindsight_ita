---
type: Guide
title: Guida di stile della traduzione
description: Regole vincolanti per tradurre Blindsight in italiano con la massima fedeltà, valide per traduttore, revisore e redattore.
status: draft
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

La guida passa a `status: stable` quando il PI ha deciso i punti segnati "da decidere in S1". Fino ad allora valgono i valori proposti.

# 1. Il principio

La traduzione rende in italiano ciò che Watts dice, come lo dice, e l'effetto che ha sul lettore inglese. Fedeltà al senso, al registro, al ritmo, alle immagini e al grado di difficoltà; non alla sintassi inglese. Il lettore italiano deve fare la stessa fatica, e provare lo stesso disagio, del lettore inglese: né di più né di meno.

Watts non si migliora, non si chiarisce e non si attenua. Se una frase è oscura in inglese, resta oscura in italiano. Se è brutale, resta brutale.

# 2. Cosa non si fa mai

1. Omettere frasi, incisi, aggettivi, avverbi, interiezioni o battute, anche quando sembrano ridondanti o difficili.
2. Aggiungere spiegazioni, note del traduttore, sinonimi esplicativi, connettivi logici che il testo non ha.
3. Unire o dividere paragrafi, o spostare contenuto da un paragrafo all'altro: ogni paragrafo resta sotto il suo marcatore.
4. Normalizzare frasi frammentarie, ellittiche o sgrammaticate di proposito.
5. Ammorbidire volgarità, crudezza, cinismo o ironia.
6. Sciogliere ambiguità volute. Quando l'italiano obbliga a scegliere (genere, numero, tu o lei, tempo verbale, soggetto sottinteso), si sceglie la lettura più probabile alla luce dell'intero libro e si annota il dubbio nelle note del blocco.
7. Riscrivere i versi di canzoni o poesie di autori reali (vedi sezione 9).

# 3. Il formato dei file

Ogni blocco è un file Markdown. Ogni paragrafo è preceduto da un marcatore, per esempio `<!-- p01234 t -->`, dove `t` è testo, `q` citazione o epigrafe, `s` separatore di scena, `h1`... `h6` titolo.

1. I marcatori si copiano identici, uno per paragrafo, nello stesso ordine. La riga di intestazione del blocco (`<!-- chunk ... -->`) si copia identica.
2. Le citazioni (`q`) mantengono `> ` all'inizio di ogni riga; i titoli mantengono i loro `#`; i separatori restano `* * *`.
3. Corsivo `*così*` e grassetto `**così**` si mantengono sulle parole che corrispondono a quelle enfatizzate in inglese.
4. Un `\` a fine riga è un a capo forzato (versi, messaggi, epigrafi): si mantiene nella stessa posizione.
5. I caratteri preceduti da `\` (`\*`, `\_`, `\[`, `\$`, `\@`, `\#`, `1984\.`) sono simboli letterali protetti: se il simbolo resta nella traduzione, resta anche la `\`.

# 4. Tipografia (da decidere in S1; valori proposti)

1. Dialoghi tra caporali: «Così», disse. Citazioni dentro un dialogo tra virgolette alte: “così”. Mai virgolette dritte.
2. Lineette (decisione del PI: ammesse nella traduzione). Dove Watts usa una lineetta, la traduzione usa una lineetta: è un tratto del suo ritmo e non si sostituisce con virgole o parentesi. Forma proposta, secondo la convenzione editoriale italiana più diffusa: lineetta media (carattere Unicode U+2013), spaziata prima e dopo negli incisi, attaccata alla parola nel discorso interrotto. La lineetta lunga (U+2014) non si usa, per avere una sola forma in tutto il libro. Lo script di controllo la segnala come carattere vietato. La forma si conferma in S1.
3. Puntini: tre punti nei file di lavoro (diventano il carattere unico al momento dell'EPUB).
4. Apostrofo dritto `'` nei file di lavoro (diventa tipografico nell'EPUB).
5. Numeri: virgola decimale (3,5), punto per le migliaia (10.000), spazio tra numero e unità di misura (12 km). Numeri in cifre o in lettere come nel testo inglese.
6. Maiuscole all'italiana: minuscola per gradi e titoli davanti al nome (il maggiore Bates), giorni, mesi, nazionalità, aggettivi derivati da nomi propri. Restano maiuscole le entità trattate come nomi propri nel libro (da glossario).
7. Corsivo per titoli di opere, parole straniere non adattate, nomi scientifici in latino, enfasi come nell'originale.

# 5. Voce e registro

1. Il narratore è Siri Keeton, un sintetista: osserva le persone dall'esterno, come sistemi. Voce fredda, clinica, precisa, con ironia asciutta e momenti di dolore trattenuto. Lessico tecnico esatto. Non si riscalda il tono e non si aggiunge empatia.
2. Le frasi brevi di Watts restano brevi; i periodi lunghi restano lunghi, ma con una sintassi italiana leggibile. Si spezza un periodo solo se in italiano diventerebbe ambiguo; non si uniscono mai frasi che Watts tiene separate.
3. Dialoghi: parlato credibile, con le contrazioni e le scorciatoie del parlato italiano quando l'inglese è colloquiale. Ogni personaggio mantiene registro e tic indicati in `docs/characters.md`.
4. Volgarità: stessa forza e stessa frequenza, con equivalenti naturali in italiano. Niente eufemismi, niente rafforzamenti.
5. Ironia e giochi di parole: prima si cerca un equivalente italiano che funzioni con lo stesso meccanismo. Se non c'è, si rende il senso e si annota la perdita nelle note del blocco, mai nel testo.
6. Non si sovra-italianizza: niente modi di dire regionali, niente forme letterarie o arcaiche (giacché, codesto, egli, ella), niente espressioni idiomatiche italiane che portino immagini assenti nell'originale.

# 6. Terminologia

1. Il glossario è vincolante per le voci `approved`. Le voci `proposed` si usano come proposta finché il PI non decide.
2. Un termine non presente nel glossario e ricorrente, tecnico o inventato non si rende a piacere: si propone nelle note del blocco con la resa scelta e le alternative.
3. Termini scientifici: la forma standard della letteratura scientifica italiana (neuroanatomia, neuropsicologia, biologia, fisica). Le sindromi e i fenomeni neurologici hanno spesso un nome italiano consolidato: lo si usa; se il nome consolidato in italiano è quello inglese, si tiene l'inglese.
4. Nomi scientifici latini invariati, in corsivo.

# 7. Nomi propri

Nomi di persona invariati. Nomi di navi, sonde, oggetti, luoghi e parti del libro secondo il glossario (decisione del PI in S1 per quelli con eco classica o simbolica).

# 8. Calchi da evitare

La resa corretta dipende sempre dal contesto; la colonna di destra indica le soluzioni più frequenti.

| inglese | calco | di solito |
|---|---|---|
| realize | realizzare | rendersi conto, capire |
| actually | attualmente | in realtà, veramente |
| eventually | eventualmente | alla fine, prima o poi |
| assume | assumere | supporre, dare per scontato |
| support | supportare | sostenere, reggere, appoggiare |
| address (a problem) | indirizzare | affrontare |
| sensible | sensibile | sensato, ragionevole |
| consistent | consistente | coerente, costante |
| evidence | evidenza | prove, indizi, dati |
| library | libreria | biblioteca |
| argument | argomento | discussione, lite, argomentazione |
| terrific | terrificante | straordinario |
| control | controllare | dominare, gestire (controllare solo per verificare) |
| make sense | fare senso | avere senso |
| I guess | indovino | credo, immagino |
| Oh my God | oh mio Dio | Dio mio, oddio |

Calchi di struttura:

1. possessivi superflui (he raised his hand: alzò la mano);
2. pronomi soggetto espliciti dove l'italiano li sottintende;
3. passivo inglese dove l'italiano preferisce l'attivo o il si impersonale;
4. articolo indeterminativo per ogni a/an;
5. catene di gerundi, di relative con che, di avverbi in -mente;
6. genitivo e aggettivi in sequenza ricalcati sull'ordine inglese;
7. maiuscole inglesi in titoli e nomi comuni.

Il rimedio a un calco non è mai un'omissione: se una parola sembra di troppo in italiano, si cerca la costruzione che la assorbe senza perderne il contributo.

# 9. Epigrafi

1. Ogni epigrafe ha una riga in `docs/epigraphs.tsv` con l'attribuzione e la decisione.
2. Canzoni e poesie di autori reali: non si traducono. Il paragrafo contiene solo `[[ORIGINALE]]`; lo script rimette il testo inglese nell'EPUB. Lo stesso per la riga di attribuzione, se fa parte dello stesso paragrafo.
3. Prosa di autori reali (discorsi, saggi, interviste) e citazioni di autori o opere inventati da Watts: si traducono.
4. Righe di attribuzione tradotte: si traducono solo le parole di raccordo e i titoli di opere inventate; i nomi restano.

# 10. Note e riferimenti

1. La prosa si traduce con le stesse regole del romanzo.
2. I riferimenti bibliografici restano come sono: autori, titoli di articoli e libri, riviste, anni, pagine, indirizzi web.
3. Un'opera citata nella prosa si cita con il titolo dell'edizione italiana solo se esiste ed è certo; altrimenti con il titolo originale in corsivo.

# 11. Refusi della sorgente

1. Un refuso evidente del testo inglese che riguarda solo l'ortografia non si riproduce: la traduzione usa la forma corretta. Sono refusi di questo tipo le lettere scambiate, mancanti o in più, due parole attaccate, un nome proprio reale scritto male, una virgoletta che si apre o si chiude senza la compagna. Vale anche per i riferimenti bibliografici delle note, che per il resto restano come sono.
2. Ogni correzione si annota nelle note del blocco, con l'id del paragrafo.
3. Un errore che può toccare il senso non è un refuso: un numero, una data, un nome che potrebbe essere voluto, una parola storpiata o una frase sgrammaticata in bocca a un personaggio. Si traduce com'è e, se il dubbio resta, si annota nelle note del blocco per il PI.
4. I paragrafi che restano in inglese (segnaposto `[[ORIGINALE]]`) vengono reinseriti dallo script così come sono nella sorgente, refusi compresi.
5. I refusi già trovati sono nella tabella qui sotto; il traduttore ne aggiunge altri nelle note del blocco.

| pid | sorgente | resa |
|---|---|---|

# 12. Lista di controllo del traduttore

Prima di consegnare un blocco:

1. Marcatori copiati identici, nello stesso ordine, nessun paragrafo vuoto.
2. Ogni paragrafo riletto accanto all'inglese: nessuna frase, inciso, aggettivo o battuta mancante o aggiunta.
3. Glossario rispettato; termini nuovi proposti nelle note.
4. Forme di cortesia come in `docs/characters.md`.
5. Corsivi, grassetti e a capo forzati come nell'inglese.
6. Tipografia secondo la sezione 4 (nessun carattere vietato).
7. Nessuna parola inglese rimasta per distrazione.
8. Il blocco riletto solo in italiano suona come un libro italiano, non come una traduzione.
