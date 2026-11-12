---
type: Guide
title: Guida di stile della traduzione
description: Regole vincolanti per tradurre Blindsight in italiano con la massima fedeltà, valide per traduttore, revisore e redattore.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

I punti di tipografia, il titolo, i nomi con eco classica e i termini chiave sono stati decisi dal PI alla chiusura della sessione sul glossario (decisione sulle scelte di S1, D-26). La punteggiatura delle battute, le lineette dentro le battute, i tempi della narrazione e la riga di attribuzione delle epigrafi sono quelli dei due blocchi del pilota, che il PI ha scelto alla cieca e confermato senza osservazioni alla chiusura del confronto (decisione sulla scelta del confronto alla cieca, D-35).

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

# 4. Tipografia

1. Dialoghi tra caporali: «Così», disse. Citazioni dentro un dialogo tra virgolette alte: “così”. Mai virgolette dritte.
2. Lineette (decisione del PI: ammesse nella traduzione). Dove Watts usa una lineetta, la traduzione usa una lineetta: è un tratto del suo ritmo e non si sostituisce con virgole o parentesi. Forma decisa dal PI, secondo la convenzione editoriale italiana più diffusa: lineetta media (carattere Unicode U+2013), spaziata prima e dopo negli incisi, attaccata alla parola nel discorso interrotto. La lineetta lunga (U+2014) non si usa, per avere una sola forma in tutto il libro. Lo script di controllo la segnala come carattere vietato. Esempi dal libro: `"Where's—" James croaked` diventa `«Dov'è–» gracchiò James`; `that half—or, like, part of you` diventa `quella metà – o, tipo, una parte di te`.
3. Puntini: tre punti nei file di lavoro (diventano il carattere unico al momento dell'EPUB).
4. Apostrofo dritto `'` nei file di lavoro (diventa tipografico nell'EPUB).
5. Numeri: virgola decimale (3,5), punto per le migliaia (10.000), spazio tra numero e unità di misura (12 km). Numeri in cifre o in lettere come nel testo inglese.
6. Maiuscole all'italiana: minuscola per gradi e titoli davanti al nome (il maggiore Bates), giorni, mesi, nazionalità, aggettivi derivati da nomi propri. Restano maiuscole le entità trattate come nomi propri nel libro (da glossario).
7. Corsivo per titoli di opere, parole straniere non adattate, nomi scientifici in latino, enfasi come nell'originale.
8. Punteggiatura delle battute. Il punto fermo, il punto interrogativo e l'esclamativo stanno dentro le caporali quando chiudono una battuta che è una frase completa: «A un metro circa.» La virgola che precede l'inciso del narratore sta fuori: «A ore otto», dissi.
9. Lineette dentro le battute, a completamento del punto 2. Inciso dentro la battuta: lineetta spaziata, come nella narrazione (`«... le apparenze politiche – non che *questa* sia chissà che novità – e io non sono un marine»`). Frase che si interrompe, esita o cambia direzione e poi riprende nella stessa battuta: lineetta attaccata alla parola che precede e seguita da uno spazio (`«Tu– esisti?»`, `«Come– come ha mai potuto credere...»`). Battuta troncata: lineetta attaccata all'ultima parola, subito prima della caporale (`«Dov'è–»`). Balbettio dentro una parola: lineetta senza spazi (`«...N–no.»`). Battuta che riprende dopo un inciso del narratore: la lineetta si attacca alla parola che riprende (`«Gli effetti della TMS–» Szpindel schioccò le dita «–sono *appiccicosi*, eh?»`).

# 5. Voce e registro

1. Il narratore è Siri Keeton, un sintetista: osserva le persone dall'esterno, come sistemi. Voce fredda, clinica, precisa, con ironia asciutta e momenti di dolore trattenuto. Lessico tecnico esatto. Non si riscalda il tono e non si aggiunge empatia.
2. Le frasi brevi di Watts restano brevi; i periodi lunghi restano lunghi, ma con una sintassi italiana leggibile. Si spezza un periodo solo se in italiano diventerebbe ambiguo; non si uniscono mai frasi che Watts tiene separate.
3. Dialoghi: parlato credibile, con le contrazioni e le scorciatoie del parlato italiano quando l'inglese è colloquiale. Ogni personaggio mantiene registro e tic indicati in `docs/characters.md`.
4. Volgarità: stessa forza e stessa frequenza, con equivalenti naturali in italiano. Niente eufemismi, niente rafforzamenti.
5. Ironia e giochi di parole: prima si cerca un equivalente italiano che funzioni con lo stesso meccanismo. Se non c'è, si rende il senso e si annota la perdita nelle note del blocco, mai nel testo.
6. Non si sovra-italianizza: niente modi di dire regionali, niente forme letterarie o arcaiche (giacché, codesto, egli, ella), niente espressioni idiomatiche italiane che portino immagini assenti nell'originale.
7. Tempi della narrazione. I fatti narrati vanno al passato remoto, con l'imperfetto e il trapassato dove servono, anche quando Siri li rievoca dalla cornice: «La sua osservazione seminale mise in moto tutto», «Tornò utile soprattutto quando gli alieni veri vennero a farci visita». Il passato prossimo si usa solo per ciò che arriva fino al presente di Siri che racconta, cioè bilanci e stati che durano ancora: «Non è cominciata qui», «sono cresciuto *obiettivo*». Nelle battute vale l'uso del parlato, quindi il passato prossimo: «L'hai quasi presa.»

# 6. Terminologia

1. Il glossario è vincolante per le voci `approved`. Le voci `proposed` si usano come proposta finché il PI non decide.
2. Un termine non presente nel glossario e ricorrente, tecnico o inventato non si rende a piacere: si propone nelle note del blocco con la resa scelta e le alternative.
3. Termini scientifici: la forma standard della letteratura scientifica italiana (neuroanatomia, neuropsicologia, biologia, fisica). Le sindromi e i fenomeni neurologici hanno spesso un nome italiano consolidato: lo si usa; se il nome consolidato in italiano è quello inglese, si tiene l'inglese.
4. Nomi scientifici latini invariati, in corsivo.

# 7. Nomi propri

Nomi di persona invariati. Nomi di navi, sonde, oggetti, luoghi e parti del libro secondo il glossario. I nomi con eco classica restano come sono, in corsivo quando sono navi: *Theseus*, *Scylla*, *Charybdis*, e la schiera Icarus (decisione sulle scelte di S1, D-26). Titoli delle parti: Theseus, Rorschach e Charybdis restano; Prologue diventa Prologo, Acknowledgments diventa Ringraziamenti, Notes and References diventa Note e riferimenti. Il titolo del libro resta *Blindsight*; nel testo il fenomeno si chiama visione cieca.

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
4. Righe di attribuzione tradotte: si traducono solo le parole di raccordo e i titoli di opere inventate; i nomi restano. I nomi classici e biblici prendono la forma italiana corrente (Aristotele, Gesù il Nazoreo, 1 Samuele 10,6). I nomi di gruppi musicali e di album restano come sono anche se inventati (The r-selectors, *Trunclade*).
5. Citazioni bibliche e parodie di versetti: si traduce il testo di Watts. La formulazione italiana corrente (CEI) si usa solo se coincide nel senso con quella di Watts (Avete occhi e non vedete, p01957; Conoscerete la verità..., parodiato in p02964). Watts cita a volte versioni inglesi parafrastiche che la CEI non segue (1 Samuele 10,6 in p01453): lì vale il suo testo.
6. Le epigrafi in versi di autori inventati si traducono in versi, cercando di tenere rima e metro (sezione 5, punto 5); la canzone dei r-selectors (p02066-p02073) ha otto versi rimati alternati e volgari, uno per paragrafo. Se la rima obbliga a cambiare un'immagine, prevale il senso e la perdita si annota.
7. Riga di attribuzione: lineetta media seguita da uno spazio, poi il nome (`– Ted Bundy`), anche quando il paragrafo è una citazione. Decisa dal PI alla chiusura del pilota (decisione sulle scelte del pilota, D-30).

# 10. Note e riferimenti

1. La prosa si traduce con le stesse regole del romanzo.
2. I riferimenti bibliografici restano come sono: autori, titoli di articoli e libri, riviste, anni, pagine, indirizzi web.
3. Un'opera citata nella prosa si cita con il titolo dell'edizione italiana solo se esiste ed è certo; altrimenti con il titolo originale in corsivo.

# 11. Refusi della sorgente

1. Un refuso evidente del testo inglese che riguarda solo l'ortografia non si riproduce: la traduzione usa la forma corretta. Sono refusi di questo tipo le lettere scambiate, mancanti o in più, due parole attaccate, un nome proprio reale scritto male, una virgoletta che si apre o si chiude senza la compagna. Vale anche per i riferimenti bibliografici delle note, che per il resto restano come sono.
2. La correzione di un nome proprio, di un termine scientifico o di un riferimento bibliografico si annota nelle note del blocco, con l'id del paragrafo. I refusi di parole comuni (murmered, occured, though per through) la traduzione li assorbe da sé e non si annotano.
3. Un errore che può toccare il senso non è un refuso: un numero, una data, un nome che potrebbe essere voluto, una parola storpiata o una frase sgrammaticata in bocca a un personaggio. Si traduce com'è e, se il dubbio resta, si annota nelle note del blocco per il PI. Non sono refusi, e non si correggono, i tratti voluti descritti nella scheda dei personaggi: il presente di Sarasti (We stop racing long ago, p03084), il pronome it di Cunningham (p02463, p03209), gli errori di Rorschach (p00925).
4. I paragrafi che restano in inglese (segnaposto `[[ORIGINALE]]`) vengono reinseriti dallo script così come sono nella sorgente, refusi compresi.
5. I refusi già trovati sono nella tabella qui sotto (raccolti in S1 dalla lettura di tutto il libro); il traduttore ne aggiunge altri nelle note del blocco. La tabella elenca solo i casi che una traduzione potrebbe riprodurre: nomi, termini tecnici, riferimenti bibliografici, e i dubbi che toccano il senso.

| pid | sorgente | resa |
|---|---|---|
| p00066 | Susanne Vega | resta così: il paragrafo è `[[ORIGINALE]]` |
| p00167, p01357 | vassopressin | vasopressina |
| p00523 | your left finger (svista di Watts: nel paragrafo dopo, p00524, il dito senza erogatore è il destro; uguale nell'edizione di confronto) | resta «sinistro», come la sorgente (decisione del PI, D-48) |
| p00062 | the Scramblers (maiuscola a metà frase, unica nel libro; 74 volte minuscolo) | gli scrambler, minuscolo come nel glossario (decisione del PI, D-35) |
| p00299 | Kurzweill | Kurzweil |
| p00332 | Burns-Caufield | Burns-Caulfield |
| p00401 | Robert Paglini | Robert Paglino |
| p00432 | tap lucidum | tapetum lucidum |
| p00951, p03708 | protocadherin γ-Y nel romanzo, ε-Protocadherin Y nelle note | protocaderina γ-Y in entrambi (glossario) |
| p01504, p01905 | Grey Syndrome e Gray Syndrome | sindrome Grigia, una sola forma (glossario) |
| p01516, p01965 e altri | Seiverts, Seivert | sievert (glossario) |
| p02253 | Cunningam's | Cunningham |
| p02620 | Fibonnaccis | Fibonacci |
| p03149, p03742, p03917 | Nirretranders, Norretranders, Nrretranders | Nørretranders |
| p03311, p03718 | Proprioreceptive, propioreception | propriocettivo, propriocezione |
| p03424 | Principle-component | componenti principali |
| p03514 | hanger | hangar (non gruccia) |
| p03680 | O'Neils | O'Neill, come in p00234 |
| p03706 | anasakid | anisakidi |
| p03716, p03739, p03824 | Saks | Sacks (Oliver Sacks) |
| p03721 | dog seguito dal rimando e.g. in apice (nella pagina doge.g.) | dog, con il rimando alla nota 45 |
| p03728 | saggital | sagittale |
| p03741 | anterious | anteriore |
| p03804 | Pennish | Pennisi |
| p03807 | Ehat | What |
| p03824 | Shuster | Schuster |
| p03837 | An Odd Kind of Fame Stories: of Phineas Gage | An Odd Kind of Fame: Stories of Phineas Gage |
| p03839 | Gottleib | Gottlieb |
| p03852 | Blacstone | Blackstone, come in p03722 |
| p03854 | Pittburgh | Pittsburgh |
| p03872 | Astrophysics Journal Letters | Astrophysical Journal Letters |
| p03873 | overacheiving | overachieving |
| p03898 | Prigonine, Nicholis | Prigogine, Nicolis |
| p03903 | Emporer | Emperor |
| p03919 | SCience | Science |
| p03926 | concensus | consensus |
| p03931 | Keiffer | Kieffer |
| p03945 | Americal | American |
| p03946 | Gaithersberg | Gaithersburg |
| p00800 | spin-against-spam | dubbio sul senso (forse span o spin): si traduce com'è, con nota |
| p01717 | pyronometers | dubbio (pirometri o piranometri): si sceglie la lettura più probabile, con nota |
| p02387 | methonia | dubbio (metano, o fusione voluta di metano e ammoniaca): si traduce com'è, con nota |
| p02874 | cryonic (in bocca a un personaggio) | si traduce com'è (crionico) |
| p03726 | trans-Newtonian comet (2000 CR105 è transnettuniano) | errore di fatto dell'autore: si traduce com'è, con nota per il PI |
| p03725 | a good billions times | «un buon miliardo di volte»: la fonte di Watts (nota 77, il comunicato NASA del luglio 2000 sulla nana bruna LP 944-20) dice a billion times (decisione sui termini del blocco 40, D-73) |
| p03726 | 2000 Cr105 | 2000 CR105, la designazione dell'oggetto |

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
