---
type: DecisionLog
title: Decisioni
description: Decisioni del PI e decisioni tecniche dell'agente, una sezione ciascuna, numerate in ordine; una decisione superata resta, con il rimando a quella che la sostituisce.
status: stable
generated:
  by: blindsight-agent/protocollo-v1
  at: "2026-11-09T23:30:00+01:00"
---

Formato di ogni voce: titolo con numero, poi Decisione, Motivazione, Deciso da (PI oppure agente), Data, Stato (valida, oppure superata da D-nn). Il numero si assegna al momento del commit: il primo libero.

Le decisioni da D-01 a D-07 sono state prese nella preparazione del pacchetto, prima della prima sessione. Il PI non ne ha riletto il testo. D-08 è del PI.

## D-01 Blocchi di circa 2.500 parole, tagliati dove il libro si interrompe da sé

Decisione: il testo si divide in blocchi di circa 2.500 parole. Un blocco nuovo comincia preferibilmente a un titolo di parte, all'epigrafe che apre un capitolo o a un separatore di scena; solo una scena molto lunga si taglia tra due paragrafi.

Motivazione: un sotto-agente deve poter leggere per intero il blocco, la guida, il glossario e la scheda dei personaggi senza diluire l'attenzione; un blocco più corto toglierebbe contesto narrativo, uno più lungo renderebbe la revisione meno accurata.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-02 Un sotto-agente per blocco, in sequenza, con il modello della sessione

Decisione: traduzione, revisione e redazione si fanno con un sotto-agente nuovo per ogni blocco, uno alla volta. I sotto-agenti hanno `model: inherit` (usano il modello della chat) ed `effort: high`.

Motivazione: un contesto nuovo per blocco evita che la chat principale si riempia e che errori di un blocco si trascinino nel successivo; la sequenza permette di passare al traduttore la fine del blocco precedente già tradotto.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-03 Tre passaggi per blocco e una lettura di coerenza finale

Decisione: prima stesura, revisione bilingue indipendente che non modifica il testo, redazione che applica i rilievi e cura l'italiano verificando ogni intervento sull'inglese; alla fine, una lettura di coerenza sull'intero libro e una controprova a campione.

Motivazione: la revisione bilingue trova soprattutto errori di senso e omissioni, la lettura solo in italiano trova soprattutto calchi e frasi che suonano tradotte; servono entrambe, e chi rivede non deve essere chi ha tradotto.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-04 Canzoni e poesie di autori reali restano in inglese

Decisione: le epigrafi tratte da canzoni o poesie di autori reali non si traducono; nei file di lavoro il paragrafo contiene solo `[[ORIGINALE]]` e lo script rimette il testo inglese nell'EPUB.

Motivazione: la licenza di Watts copre il suo testo, non i versi di altri autori; lasciarli in originale è anche una convenzione diffusa nelle traduzioni italiane.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-05 Sonnet per S0, Opus per il resto, un modello per passaggio

Decisione: Sonnet 5.5 per la sessione meccanica iniziale; Opus 5.5 per glossario, pilota, traduzione, revisione e coerenza, salvo che il confronto alla cieca facoltativo con Fable 5.2 faccia scegliere quest'ultimo. Il modello scelto vale per tutte le sessioni di un passaggio.

Motivazione: due modelli diversi in parti diverse del libro darebbero due voci diverse; per la scelta fra modelli vale ciò che il PI legge, non la reputazione del modello.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-06 Nota sulla traduzione in fondo, licenza nei metadati

Decisione: la nota sulla traduzione e sulla licenza va dopo l'ultimo capitolo; la licenza è anche nei metadati dell'EPUB.

Motivazione: in testa al libro la nota finirebbe nello stesso file della dedica e delle prime epigrafi; nei metadati resta comunque visibile in ogni lettore.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-07 Riassunto della trama per tutti i blocchi prima di tradurre

Decisione: il riassunto della trama blocco per blocco si scrive in S1, durante la lettura completa del libro, e non man mano che si traduce.

Motivazione: il secondo blocco del pilota sta a metà libro; senza un riassunto completo il traduttore lavorerebbe senza sapere cosa è successo prima.

Deciso da: agente. Data: 2026-11-09. Stato: valida.

## D-08 Lineette ammesse nella traduzione

Decisione: nel testo del romanzo le lineette sono ammesse e si usano dove le usa Watts. Il divieto di lineette come punteggiatura resta per i documenti di progetto e per la conversazione con il PI. La forma (lineetta media, U+2013, spaziata negli incisi e attaccata nel discorso interrotto) è una proposta da confermare in S1.

Motivazione: la regola del PI riguarda i testi scritti dall'agente, non la resa di un autore che fa delle lineette un tratto del suo ritmo; sostituirle cambierebbe lo stile dell'originale.

Deciso da: PI. Data: 2026-11-09. Stato: valida.

## D-09 La sessione sulla sorgente (S0) si fa con Fable 5.2 invece di Sonnet

Decisione: la sessione che scarica la sorgente e la divide in blocchi (S0) si esegue con Fable 5.2, il modello della chat in cui il PI l'ha aperta, e non con Sonnet 5.5 come previsto dalla decisione sui modelli (D-05). È una deroga alla regola sul modello previsto e vale solo per S0: per tutte le altre sessioni resta il modello scritto in `docs/state.tsv`. Se S0 si interrompe, si può riprendere con Fable 5.2 o con Sonnet 5.5.

Motivazione: S0 non scrive una riga di italiano (scarica, divide, conta), quindi il modello non può cambiare la voce della traduzione, che è la ragione della regola. Il costo è un consumo maggiore dei limiti d'uso rispetto a Sonnet.

Deciso da: PI. Data: 2026-11-09. Stato: valida.

## D-10 Lavoro nel cloud: push a ogni commit, ambiente dedicato, EPUB consegnato come file

Decisione: quando una sessione gira in Claude Code nel cloud, e non sul Mac o sul server, valgono quattro adattamenti. A ogni commit segue un push sul ramo della sessione. Le sessioni si aprono nell'ambiente cloud `blindsight_ita`, che consente la rete verso `www.rifters.com` e `rifters.com` e installa epubcheck all'avvio. Il modello si sceglie nell'app al momento di aprire la sessione, perché il comando `claude --model ...` del README vale solo in locale. Gli EPUB, che non sono versionati, si consegnano al PI come file alla chiusura della sessione che li produce.

Motivazione: il contenitore cloud è temporaneo e ciò che non è sul repository si perde; l'ambiente predefinito non raggiunge il sito dell'autore e non ha epubcheck. L'ambiente è stato proposto dall'agente e approvato dal PI. Lo script di avvio è stato provato a mano in questa sessione ma non ancora in una sessione nuova.

Deciso da: agente. Data: 2026-11-10. Stato: valida, salvo la parte sulla rete, superata dalla decisione sulla rete dell'ambiente cloud (D-38).

## D-11 Sorgente dalla copia dell'Internet Archive se il sito dell'autore non risponde

Decisione: se la pagina non si riesce a scaricare da rifters.com, si usa la copia grezza della stessa pagina conservata dall'Internet Archive (`web.archive.org`, con la forma dell'indirizzo che restituisce i byte originali senza la barra dell'archivio). Nel registro si annotano l'indirizzo completo e la data della cattura.

Motivazione: dall'ambiente cloud la connessione a rifters.com cade prima di ricevere dati; la copia d'archivio è la stessa pagina a una data nota. Limite dichiarato al PI: dall'ambiente cloud non si può verificare che la cattura sia identica alla pagina di oggi.

Deciso da: PI. Data: 2026-11-10. Stato: superata dalla decisione sulla sorgente fornita dal PI (D-12). Non è mai stata eseguita: l'host dell'archivio non era consentito dalla rete dell'ambiente.

## D-12 La sorgente è il file HTML fornito dal PI

Decisione: la sorgente della traduzione è il file `Blindsight_html_format.htm` contenuto nello zip che il PI ha caricato nella chat il 2026-11-10. È salvato senza modifiche come `source/original/Blindsight.htm`, insieme alle tre immagini dello zip; lo zip originale è conservato in `reference/Blindsight.zip`. Non si scarica più nulla dal sito dell'autore né dall'Internet Archive.

Motivazione: dal cloud il sito dell'autore non risponde e l'archivio non è raggiungibile. Il file è l'esportazione HTML dell'autore (nei metadati: autore Peter Watts, ultima modifica 2006-12-09; nello zip ha la data 2007-09-03) e l'EPUB di confronto fornito dal PI dichiara di derivare dalla stessa pagina del sito.

Deciso da: PI. Data: 2026-11-10. Stato: valida. Provenienza riferita dal PI alla chiusura della sessione: il sito dell'autore (rifters.com), dalla pagina che offre il romanzo in formato HTML; l'indirizzo esatto non è annotato.

## D-13 L'EPUB di Ellen Herzfeld serve solo da confronto; la licenza è la 2.5

Decisione: l'EPUB `PeterWatts_Blindsight-v1.01-formatted-by-Ellen-Herzfeld.epub` fornito dal PI, conservato in `reference/`, non è sorgente: si usa solo per controllare che il testo dei blocchi sia completo. La licenza che vale per la traduzione è quella dichiarata nella pagina dell'autore, Creative Commons Attribution-NonCommercial-ShareAlike 2.5; la versione è stata aggiunta alla nota sulla traduzione e ai metadati dell'EPUB.

Motivazione: l'EPUB è un'edizione curata da terzi che interviene sulle note (voci rinumerate e duplicate, refusi corretti, indirizzi aggiornati) e dichiara per sé la versione 3.0 della stessa licenza; il progetto traduce il testo dell'autore.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-14 Confini del libro: cosa entra nei blocchi e cosa resta fuori

Decisione: i blocchi vanno dalla dedica (paragrafo p00003) all'ultima nota finale (paragrafo p03946). Restano fuori tre cose. Titolo e nome dell'autore (p00001 e p00002), come previsto dalla procedura. L'indice della pagina web con il separatore che lo chiude (da p00005 a p00012). Il testo legale della licenza con il separatore che lo chiude (da p03758 a p03802). Le due esclusioni interne sono scritte in `source/excluded.tsv`. Le 144 note finali, che nella pagina vengono dopo il testo della licenza, seguono così direttamente il saggio a cui appartengono. Nessun titolo di parte è un'immagine, quindi nessun titolo è stato aggiunto a mano.

Motivazione: l'indice è navigazione della pagina, e l'EPUB ne genera uno proprio; il testo legale non è del romanzo e non si traduce, la licenza è indicata nella nota e nei metadati.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-15 Adattamenti dello script alla pagina reale

Decisione: lo script è stato adattato alla pagina dell'autore in sette punti, ciascuno coperto dal collaudo.

1. I paragrafi allineati a destra sono epigrafi (tipo `q`): nella pagina le epigrafi non sono citazioni a blocco.
2. I caratteri scritti con il font Symbol (gradi, mu, epsilon, sigma) sono convertiti nel carattere Unicode che il font mostra, e i trattini morbidi invisibili sono tolti. Se un carattere di questo tipo resta senza conversione, il cancello di copertura fallisce.
3. Gli apici annidati (i richiami di nota) e gli apici con spazi sono scritti in modo che pandoc li legga.
4. L'impaginazione propria di un paragrafo (centrato, rientrato, colonna di una tabella) è registrata nel campo `layout` di `source/paragraphs.jsonl` e riportata nell'EPUB con classi del foglio di stile.
5. Le immagini che fanno parte del libro si elencano in `source/figures.tsv` e vengono inserite nell'EPUB. Oggi è una sola: il cubo dopo il paragrafo p00418.
6. `chunk --exclude` lascia fuori gli intervalli interni che non sono il libro.
7. Un blocco prende il nome di tutte le parti che tocca, e `source/SHA256SUMS` non elenca più due volte lo stesso file.

Motivazione: il pacchetto era stato scritto senza vedere la pagina. Senza questi adattamenti l'EPUB avrebbe avuto le epigrafi impaginate come testo normale, dieci caratteri illeggibili, segni `^` accanto ai numeri di nota, la figura mancante e i passi a più colonne appiattiti.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-16 Quattro sessioni di traduzione e sei di revisione

Decisione: le sessioni di traduzione sono T1 (blocchi 01-11), T2 (12-22), T3 (23-34), T4 (35-41). Le sessioni di revisione sono R1 (01-07), R2 (08-14), R3 (15-21), R4 (22-29), R5 (30-36), R6 (37-41). Il modello scritto in `docs/state.tsv` è provvisorio: lo conferma o lo cambia il pilota.

Motivazione: è il raggruppamento suggerito dallo script per circa 25.000 parole a sessione di traduzione e 16.000 a sessione di revisione, e coincide con la stima del piano.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-17 La copertina è il fronte della sovraccoperta fornita dal PI

Decisione: la copertina dell'EPUB è il fronte della sovraccoperta alternativa di Thomas Pringle che il PI ha caricato nella chat (`reference/jacket-alternate-thomas-pringle.jpg`). Il fronte è ritagliato dall'immagine (606 per 897 pixel) e salvato in `epub/cover.jpg`; lo script lo passa a pandoc quando il file esiste.

Motivazione: è l'immagine scelta dal PI, e sulla sovraccoperta stessa l'autore scrive che si può copiare senza limiti. Limite: la risoluzione è bassa per uno schermo ad alta densità; se il PI procura una versione più grande basta sostituire il file. L'EPUB di confronto usa un'altra copertina dello stesso artista, non questa.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-18 Si lavora nel cloud, con una pull request alla chiusura di ogni sessione

Decisione: le sessioni proseguono in Claude Code nel cloud. Alla chiusura di ogni sessione l'agente apre una pull request dal ramo della sessione al ramo principale e il PI la unisce prima di aprire la sessione successiva. Le regole sono nella sezione "Lavoro nel cloud" di `CLAUDE.md`, aggiunta con questa decisione; restano validi gli adattamenti tecnici già registrati (decisione sul lavoro nel cloud, D-10). Per la sessione sulla sorgente (S0) non c'è nulla da unire: il repository era vuoto e il ramo di quella chat è diventato il principale.

Motivazione: il PI vuole lanciare le sessioni dal telefono. Nel cloud ogni chat lavora su un ramo suo e la successiva parte dal ramo principale: senza unione la sessione successiva non vedrebbe il lavoro fatto e lo rifarebbe.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-19 La sessione sul glossario (S1) si fa nella chat di S0, su un ramo proprio

Decisione: la sessione sul glossario, i personaggi, le epigrafi e la tipografia (S1) si svolge nella stessa chat cloud della sessione sulla sorgente (S0), dopo che il PI ne ha svuotato la conversazione e ha portato il modello a Opus 5.5, il modello previsto. Poiché il ramo di quella chat è il ramo principale, il lavoro di S1 sta sul ramo `sessione-S1`, creato dal principale; alla chiusura si apre la pull request da `sessione-S1` al principale, come vuole la decisione sul lavoro nel cloud con pull request (D-18). Vale solo per S1.

Motivazione: la conversazione svuotata dà un contesto pulito e il modello è quello previsto, quindi le ragioni della regola su una sessione nuova sono soddisfatte; un ramo proprio conserva il passaggio di unione che il protocollo cloud prevede. Alternative scartate dal PI: lavorare direttamente sul principale senza pull request, oppure aprire una chat nuova e rilanciare l'esplorazione.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-20 Cancello sulle epigrafi che restano in inglese

Decisione: il controllo di un blocco tradotto (`check`) confronta i segnaposto con `docs/epigraphs.tsv`. Il cancello fallisce in due casi: un paragrafo che l'elenco delle epigrafi segna `original` non contiene il solo segnaposto `[[ORIGINALE]]`; un paragrafo contiene il segnaposto ma l'elenco non lo segna `original`. Il collaudo ha due casi nuovi, uno per errore (ora i controlli sono 41).

Motivazione: prima il controllo verificava solo che il segnaposto fosse scritto bene, non che stesse nei paragrafi giusti. Senza questo cancello un traduttore avrebbe potuto riscrivere i versi di una canzone di un autore reale, o lasciare in inglese un'epigrafe da tradurre, senza che nessuno script lo vedesse; è la regola sui testi di terzi del protocollo.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-21 Glossario: le voci tecniche decise dall'agente

Decisione: il glossario ha 132 voci. Le 21 voci `proposed` vanno al PI (termini chiave inventati o gergali, nomi con eco classica, il termine del titolo). Le altre 111 sono `approved` dall'agente, perché hanno una forma italiana standard, sono nomi propri che restano invariati o sono rese senza alternative serie; ciascuna ha la motivazione nella colonna `note`. Criterio di inclusione: termini che ricorrono in almeno due paragrafi o in blocchi diversi, dove la coerenza tra traduttori diversi conta; i termini che compaiono una sola volta restano al traduttore, che li propone nelle note del blocco. Elenco delle voci decise dall'agente: G022 Rorschach: Rorschach (in corsivo come in Watts, maschile, senza articolo); G023 Big Ben, Ben: Big Ben, Ben (invariati); G024 Burns-Caulfield, Burnsie: Burns-Caulfield, Burnsie (invariati); G025 Oasa emitter, Oasa object: emettitore di Oasa, oggetto di Oasa; G026 Kuiper (belt): fascia di Kuiper; il Kuiper; G027 Oort (cloud): nube di Oort; G028 Mission Control: Controllo Missione; G029 Kurzweil Institute: Istituto Kurzweil; G030 the Captain: il Capitano (maiuscolo); G031 BioMed: BioMed (invariato); G032 Fab: Fab (invariato); G033 Commons: la Sala comune; G034 Tactical: il Tattico; G035 drum: tamburo; G036 spine (of Theseus); spines (of Rorschach): spina dorsale (la nave); aculei (Rorschach); G037 carapace: carapace; G038 bridge: plancia; G039 crypt: cripta; G040 coffin: bara; G041 pod (resurrection, medical): capsula; G042 observation blister, blister: bolla di osservazione, bolla; G043 dome (observation): cupola; G044 galley: cambusa; G045 tent: tenda; G046 telematter: telemateria; G047 lab-hab: modulo laboratorio; G048 teleops: teleoperatori; G049 drones: droni; G050 HUD: HUD; G051 fiberop: fibrottica; G052 waldoes: manipolatori; G053 Faraday (mesh, bell, shielding; verb): di Faraday (gabbia, rete, campana, schermatura di Faraday); il verbo si rende con schermare; G054 accretion belt: fascia di accrescimento; G055 superjovian: supergioviano; G056 tweak(s): ritocco, ritoccare; G057 carboplatinum: carboplatino; G058 trickle-charger, trickler: erogatore a rilascio lento; G059 vampire: vampiro, vampiri, vampiresco; G060 Homo sapiens vampiris: Homo sapiens vampiris (corsivo); G061 bloodsucker: succhiasangue; G062 undead: non morto, non morti; G063 zombie: zombie (invariabile); G064 Human, Humans, Humanity (capitalized): Umano, Umani, Umanità (maiuscolo dove Watts lo usa); G065 Realists: Realisti, realista (maiuscolo come in Watts); G066 Ascended, Ascendants: gli Ascesi; G067 conscious, consciousness: cosciente, coscienza; G068 Major (Bates): il maggiore (minuscolo, anche al vocativo); G069 commissar: commissario (commissario politico alla prima occorrenza); G070 conduit: tramite (il ruolo di Siri); condotto (i tubi della nave); G071 Cruncher: Cruncher (invariato); G072 Jack (probe): Jack (invariato); G073 Cygnus, Cyg, Cyggers: Cygnus, Cyg, Cyggers (invariati); G074 nicknames: Mandy, Meesh, Suze, Ike, Chelse, Rob, Burnsie: invariati; G075 Mom (Susan for her personalities; Siri's mother): mamma; G076 QuBit's, the Qube: QuBit's, il Qube (invariati); G077 Golem (disease): Golem (invariato); G078 Hadzane: hadza (la lingua hadza); G079 topology: topologia; G080 facets: sfaccettature; G081 rotate (synthesist jargon): ruotare, rotazione; G082 personae: personae (in corsivo); G083 cores (of James): nuclei; G084 meat: carne; G085 eh? (Szpindel): eh?; G086 bleeding edge: avanguardia estrema; G087 Chinese Room: stanza cinese; G088 N minutes to apogee/perigee: N minuti all'apogeo, N minuti al perigeo; G089 postcards to posterity: cartolina ai posteri, cartoline ai posteri; G090 Technology Implies Belligerence: La tecnologia implica belligeranza; G091 covert to invulnerable: da occulto a invulnerabile; G092 Graduation Day: il Giorno del Diploma; G093 survive and bear witness: sopravvivere e testimoniare; G094 Devil's Baklava: la Baklava del Diavolo; G095 twencen: novecentesco; G096 klicks: chilometri; G097 headspace: spazio mentale; G098 inattentional blindness: cecità da disattenzione; G099 Cotard's syndrome: sindrome di Cotard; G100 Anton's syndrome: sindrome di Anton; G101 alien hand syndrome: sindrome della mano aliena; G102 hemispherectomy: emisferectomia; G103 brain stem: tronco encefalico; G104 saccades, saccadic: saccadi, saccadico; G105 proprioception: propriocezione, propriocettivo; G106 synesthesia, synesthete: sinestesia, sinesteta; G107 transcranial magnetic stimulation, TMS: stimolazione magnetica transcranica (TMS); magnete transcranico; G108 Necker cube: cubo di Necker; G109 form constants (Klüver): costanti di forma (di Klüver); G110 vasopressin: vasopressina; G111 protocadherin: protocaderina γ-Y (nel romanzo e nelle note); G112 antieuclideans: antieuclidei; G113 multiple personality disorder, MPD: disturbo di personalità multipla (DPM); G114 alters: alter (in corsivo); G115 savant, savantism: savant, savantismo; G116 splinter skills: abilità isolate; G117 transient (orca): transiente (orca transiente, orche transienti e residenti); G118 extended phenotype: fenotipo esteso; G119 kin selection: selezione di parentela; G120 game theory: teoria dei giochi; G121 anaerobe, anaerobic: anaerobio, anaerobico; G122 septum, septa: setto, setti; G123 vestibule: vestibolo; G124 chromatophores: cromatofori; G125 cloacae: cloache; G126 crypsis: cripsi; G127 prion, prionic: prione, prionico; G128 Seiverts (sievert): sievert (minuscolo, invariabile); G129 noosphere: noosfera; G130 magnetosphere: magnetosfera; G131 Grey Syndrome: sindrome Grigia; G132 brown dwarf: nana bruna.

Motivazione: il traduttore di ogni blocco vede solo il suo blocco; senza una resa fissata prima, lo stesso termine uscirebbe in forme diverse in blocchi diversi. Le voci tecniche non cambiano il senso del libro e si possono correggere senza toccare le scelte del PI.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-22 Un file con i passi difficili di ogni blocco

Decisione: i passi difficili segnalati dagli esploratori (giochi di parole, gergo fitto, ambiguità volute, voci con grammatica propria) stanno in `docs/hard-passages.md`, una sezione per blocco, 203 voci. Traduttore, revisore e redattore ne leggono la sezione del proprio blocco: aggiunta una riga alle loro istruzioni e una riga all'elenco dei file in `CLAUDE.md`. Il file dice dove e perché un passo è difficile, non come tradurlo.

Motivazione: le osservazioni raccolte leggendo tutto il libro andrebbero perse, e il traduttore di un blocco non sa che una battuta riprende un passo di trenta blocchi prima o che un errore di grammatica è voluto.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-23 Refusi della sorgente: regola e tabella; una sola lettera greca per la protocaderina

Decisione: nella guida di stile, sezione 11, i refusi di sola ortografia non si riproducono; i casi che possono toccare il senso si traducono com'è e si annotano; i tratti voluti dei personaggi non sono refusi. La tabella ha 42 righe: 37 correzioni di casi che una traduzione potrebbe riprodurre (nomi, termini tecnici, riferimenti delle note) e 5 dubbi sul senso, che si traducono come sono. La protocaderina si scrive γ-Y anche nelle note, dove la sorgente ha ε: le note rimandano alla stessa proteina del romanzo, e la ε viene probabilmente da una lettera scritta con il font Symbol.

Motivazione: il primo dubbio ricevuto dalla sessione sulla sorgente chiedeva una regola, da decidere dall'agente se riguarda solo l'ortografia. Nessuno dei casi elencati come correzione cambia il senso; quelli che potrebbero cambiarlo restano come sono, con una nota che arriva al PI dalle sessioni di traduzione.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-24 Voci con grammatica propria

Decisione: nella scheda dei personaggi, sezione "Voci con grammatica propria", si fissano otto regole: Sarasti sempre al presente, anche quando diventa fluente; il pronome it di Cunningham per le persone reso con esso, senza accordi di genere visibili; la Banda con il genere della personalità che parla; il Capitano al maschile e con messaggi abbreviati senza vocali nel blocco 38; gli errori voluti di Rorschach conservati; la Theseus al femminile; gli scrambler al maschile; le sonde in prima persona.

Motivazione: Watts dichiara questi tratti nel testo (p00425, p02025, p02463) e ci costruisce sopra battute; un traduttore che li normalizzasse correggerebbe Watts. La resa con esso è l'unica forma italiana che, riferita a una persona, stride come it.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-25 Il secondo blocco del pilota è il 18

Decisione: il pilota (S2) traduce il blocco 01 e il blocco 18. Il 18 ha il punteggio più alto del libro sommando tre misure standardizzate, contate con uno script sui blocchi sorgente: quota di paragrafi con dialogo (78%), occorrenze di voci del glossario per mille parole (27,9), voci diverse del glossario presenti (38). Punteggio 3,99, contro 2,99 del blocco 12, il secondo.

Motivazione: la procedura chiede il blocco con la densità più alta di termini, dialogo e gergo, contata con gli script. Il 18 contiene anche la spiegazione della visione cieca e il gioco di parole sul titolo, e mette alla prova le voci di Szpindel, Bates e della Banda.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-26 Le scelte della sessione sul glossario (S1)

Decisione: il PI accetta tutte e cinque le raccomandazioni della sessione sul glossario. Il titolo resta *Blindsight*; nel testo il fenomeno si chiama visione cieca. Dialoghi tra caporali; lineetta media, spaziata negli incisi e attaccata nel discorso interrotto; la lineetta lunga resta vietata. I nomi con eco classica restano come sono: *Theseus*, *Scylla*, *Charybdis*, Icarus; i titoli delle parti Theseus, Rorschach e Charybdis restano, Prologo, Ringraziamenti e Note e riferimenti si traducono. Forme di cortesia: tu tra tutti, anche fra Sarasti e l'equipaggio; Bates dà a Sarasti il lei con signore finché lo chiama sir e passa al tu quando lo affronta chiamandolo Jukka (p03088); Bates dà il lei alla prigioniera realista, che le risponde con il tu. I 16 termini chiave prendono la resa proposta (scrambler, fanti, di serie, sintetista, gergonauta, la Banda dei Quattro, ConSensus, Paradiso, innesti, Lucciole, Pioggia di fuoco, senzienza, Ultracorpo, glitch del Crocifisso, scrematori, Stretch e Clench). Le 21 voci del glossario che erano `proposed` diventano `approved`, e ciascuna riconosce in italiano solo la resa scelta.

Motivazione: sono le scelte che il protocollo riserva al PI; le ragioni di ciascuna sono nel riassunto della sessione sul glossario.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-27 Una chat cloud riaperta lavora su un ramo della sessione

Decisione: quando il PI riapre la chat cloud della sessione sulla sorgente, il cui ramo è il ramo principale, dopo averne svuotato la conversazione e con il modello previsto, la sessione lavora sul ramo `sessione-<id>` creato dal principale (per il pilota: `sessione-S2`), con push a ogni commit e pull request al principale alla chiusura. Estende a tutte le sessioni successive la regola che valeva solo per la sessione sul glossario (decisione sul ramo di S1, D-19); la regola è il punto 8 della sezione "Lavoro nel cloud" di `CLAUDE.md`.

Motivazione: con la conversazione svuotata e il modello giusto le ragioni di una chat nuova sono soddisfatte, e il ramo proprio conserva l'unione che il PI controlla. Alternative scartate dal PI: lavorare direttamente sul principale senza pull request, oppure fermarsi e aprire una chat nuova.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-28 Sintesi e Sintetista con la maiuscola dove Watts la usa

Decisione: nella voce del glossario sul sintetista si aggiunge che sintesi e sintetista prendono la maiuscola dove Watts la usa a metà frase per la disciplina o come titolo (Synthesis nei blocchi 01 e 06, Synthesist come titolo nei blocchi 05 e 06), e restano minuscole altrove (synthesis minuscolo nei blocchi 12, 25 e 27). La resa resta quella decisa dal PI.

Motivazione: il traduttore del blocco 01 ha proposto la maiuscola in «mi portò alla Sintesi», perché in minuscolo si leggerebbe la sintesi in generale e non la disciplina; revisore e redattore concordano. È lo stesso criterio delle voci su Umani e Realisti (maiuscola dove la usa Watts), e senza una regola i traduttori dei blocchi 05, 06 e 07 sceglierebbero ciascuno a modo suo.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-29 Sette voci nuove del glossario dai termini proposti nel pilota

Decisione: dei termini proposti dai traduttori nel pilota entrano nel glossario, approvati dall'agente, quelli che compaiono anche in blocchi non ancora tradotti: G133 spike, nel senso del picco di campo dentro Rorschach: picco; G134 subdrum: sottotamburo; G135 wetware: wetware, invariato; G136 diagnostic couch: poltrona diagnostica; G137 multijointed: pluriarticolato, con la frase sulle braccia della creatura che torna come citazione nel blocco 35; G138 Tesla come unità: tesla, minuscolo e invariabile; G139 diving bell: campana da palombaro. Gli altri termini proposti compaiono una sola volta nel libro, oppure sono già coperti dal glossario, e restano la scelta del traduttore del blocco (spazio di gioco, ultracorpi, campo giochi, verifiche a terra, trasduttore, capsula dei sensori, decompilatore, prendiappunti, malattia di Damasco, mezza branda, i Morti Volanti).

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi, dove la coerenza fra traduttori diversi conta. Le rese sono quelle del traduttore del blocco 18, confermate dal revisore e lasciate dal redattore; nessuna tocca il senso. Per spike la voce copre solo il senso del picco di campo: negli altri sensi la segnalazione del controllo è un falso allarme, e la nota della voce lo dice.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-30 Le scelte del pilota (S2): confronto alla cieca e lineetta delle attribuzioni

Decisione: il PI chiede il confronto alla cieca con Fable 5.2 (S2b) sugli stessi due blocchi del pilota, prima di fissare il modello delle sessioni di traduzione e di revisione. Nelle righe che attribuiscono le epigrafi si usa la lineetta media seguita da uno spazio («– Ted Bundy»), come nei due blocchi del pilota; la regola entra nella guida di stile alla fine del confronto, insieme alle indicazioni di lettura del PI, così che la guida resti identica per le due versioni; il traduttore del confronto la riceve nel prompt, come quello del pilota. Conseguenza registrata dall'agente: la lettura dell'EPUB di prova e le domande su tono, dialoghi, termini e forme di cortesia passano al confronto, dove il PI legge le due versioni anonime; leggere prima l'EPUB del pilota gli farebbe riconoscere una delle due versioni.

Motivazione: il modello scelto traduce tutto il libro e non si cambia a metà; dall'interno della catena, dove traduttore, revisore e redattore sono lo stesso modello, non si vede se un altro modello farebbe meglio. La lineetta media spaziata è coerente con quella scelta per gli incisi (decisione sulle scelte di S1, D-26).

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-31 I due EPUB del confronto alla cieca hanno un titolo che li distingue

Decisione: il comando che costruisce le due versioni anonime scrive nei metadati di ciascun EPUB un titolo proprio, «Blindsight (pilota X)» e «Blindsight (pilota Y)», al posto del titolo comune. Il resto dei metadati, la copertina e il foglio di stile restano identici. Il collaudo degli script ha un controllo in più su questo.

Motivazione: i due file avevano lo stesso titolo e la stessa copertina, quindi nella libreria di un lettore di EPUB non si distinguevano e il PI non avrebbe saputo quale dei due stava leggendo. L'etichetta è quella del nome del file e non dice nulla su chi ha tradotto. Il titolo dell'EPUB del libro intero non cambia.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-32 I risultati dei controlli sulla prova B si salvano accanto alla sua cartella

Decisione: quando il controllo di un blocco riceve una cartella alternativa e l'opzione di salvataggio, scrive i risultati nella cartella `checks` accanto a quella alternativa (per la prova B: `trial-b/checks/`) e non in `checks/`. Il collaudo degli script ha due controlli in più: questo, e il calcolo della quota di paragrafi cambiati sulla prima stesura della cartella alternativa.

Motivazione: con la cartella alternativa lo script salvava in `checks/` con lo stesso nome dei risultati della versione A e li avrebbe sovrascritti. La procedura del confronto evitava il problema solo perché non usa il salvataggio; così i numeri della prova B restano in un file, come quelli della versione A, senza toccare i suoi.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-33 Impronte dei due testi anonimi del confronto, per ricostruire l'abbinamento se la chiave va persa

Decisione: dopo il sorteggio si salvano in `comparison/impronte.tsv`, versionato, le impronte SHA-256 dei due testi assemblati da cui nascono gli EPUB anonimi. La chiave resta fuori dal repository, come prima. Se la chiave manca al momento della scelta, si assemblano di nuovo le due versioni e si confrontano le impronte.

Motivazione: nel cloud il contenitore viene sostituito dopo un periodo di inattività e i file non versionati vanno persi; il PI legge i due EPUB per circa un'ora prima di scegliere. Le impronte da sole non dicono quale versione è quale: per saperlo bisogna assemblare e confrontare di proposito, come per aprire la chiave. Dopo il primo sorteggio la chat principale aveva visto per errore le dimensioni dei file, che svelavano l'abbinamento: il sorteggio è stato rifatto e le impronte sono quelle del secondo.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-34 Nel riassunto del confronto i numeri del processo sono per modello, non per X e Y

Decisione: il riassunto del confronto alla cieca riporta conteggi e tempi per modello (pilota con Opus, seconda versione con Fable) e non per versione anonima, senza esempi di testo; dice al PI che l'abbinamento con X e Y resta chiuso fino alla scelta.

Motivazione: la procedura della sessione chiedeva conteggi e tempi per X e Y senza nomi di modelli, ma così com'è scritta non si può seguire senza rompere il confronto. Per etichettare i numeri con X e Y l'agente dovrebbe aprire la chiave, che non si apre prima della scelta; e il PI ha già letto i numeri del pilota nel suo riassunto, quindi li riconoscerebbe sotto l'etichetta anonima. I numeri per modello non sono osservabili nel testo e non permettono di abbinare le versioni; servono al PI perché il tempo di macchina è diverso fra i due modelli. È uno scarto dalla procedura scritta: è detto al PI nel riassunto.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-35 Il confronto alla cieca: il PI sceglie la versione del pilota, tradotta da Opus

Decisione: letti i due EPUB anonimi, il PI sceglie la versione Y. Aperta la chiave dopo la scelta, Y è la versione del pilota (Opus 5.5) e X la seconda versione (Fable 5.2). Opus 5.5 è quindi il modello di tutte le sessioni di traduzione e di revisione. Il PI non ha osservazioni di lettura su tono del narratore, dialoghi, termini e forme di cortesia: la guida di stile prende le convenzioni dei due blocchi del pilota così come sono, cioè punto fermo dentro le caporali per la battuta completa e virgola fuori per l'inciso, lineette dentro le battute, passato remoto per i fatti narrati e passato prossimo solo per ciò che arriva al presente di Siri, lineetta media e spazio nelle attribuzioni delle epigrafi. Scrambler resta minuscolo anche nel Prologo, dove Watts lo scrive una volta con la maiuscola a metà frase.

Motivazione: il PI trova la versione scelta più naturale in italiano e migliore nei dialoghi. Dice di non avere riconosciuto nessuna delle due versioni durante la lettura. Per la minuscola di scrambler: la maiuscola a metà frase compare una sola volta nel libro contro 74 minuscole, anche nello stesso Prologo, e in italiano si leggerebbe come un refuso. I file della seconda versione restano in `trial-b/` come documentazione del confronto e non entrano nel libro.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-36 Cinque voci nuove del glossario dal confronto alla cieca, e l'articolo di Fab

Decisione: entrano nel glossario, approvate dall'agente, cinque voci per termini del blocco 18 che tornano in altri blocchi, con le rese della versione scelta: G140 spinal bundle: fascio spinale; G141 jarhead: marine; G142 on top, detto della personalità della Banda che guida il corpo: in primo piano; G143 feed, nel senso del flusso di dati: flusso; G144 faceplate: visiera. La voce su Fab dice ora che il nome vuole l'articolo (il Fab, al Fab). La voce su scrambler registra la minuscola decisa dal PI.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Spinal bundle, jarhead e on top li hanno segnalati traduttore e redattore della seconda versione; nel pilota erano passati senza proposta. Feed compare in 17 blocchi e faceplate in 5, e le due versioni li hanno resi allo stesso modo. Per feed il controllo segnala anche il verbo e le condotte dell'aria: sono falsi allarmi, e la nota della voce lo dice.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-37 Seconda lettura dopo la revisione: si misura con Opus nella prima sessione di revisione

Decisione: il piano della revisione resta com'è. Nella prima sessione di revisione (R1), sul blocco 02, si misura quanto trova una seconda lettura della versione finale fatta dallo stesso modello, con previsione e soglia scritte nei dubbi ricevuti di quella sessione: da 1 rilievo alto o medio fondato ogni 100 paragrafi in su, la seconda lettura si propone al PI come passaggio fisso. I difetti trovati nel blocco 18 li corregge il redattore nella sessione di revisione che copre quel blocco (R3), con le note scritte nei suoi dubbi ricevuti.

Motivazione: dopo la scelta del PI, una rilettura del blocco 18 nella versione finale di Opus, fatta con il revisore di Fable, ha dato 1 rilievo alto e 10 medi; verificati sull'inglese dalla chat principale, 6 sono fondati, 3 non fondati, 1 dubbio, 1 non verificato. Con un'omissione vista confrontando le due versioni i difetti noti sono 7 su 201 paragrafi, nessuno che cambi il senso. L'attesa scritta prima era 2, con soglia a 5: smentita. La misura non separa l'effetto del modello diverso da quello della seconda lettura, il revisore si è mostrato incostante (un'omissione segnalata come grave su una versione e lasciata passare, identica, sull'altra) e chi ha giudicato i rilievi girava con lo stesso modello del revisore. Alternative scartate dal PI: far rileggere a Fable tutti i blocchi finiti (da 7 a 11 ore di macchina e da 6 a 12 chat in più, stima); nessuna seconda lettura. Le correzioni al blocco 18 non si fanno nella sessione del confronto perché il redattore lì gira con un modello diverso da quello del passaggio di revisione.

Deciso da: PI (la misura e le alternative); agente (rinvio delle correzioni alla sessione di revisione). Data: 2026-11-10. Stato: valida.

## D-38 La rete dell'ambiente cloud è senza restrizioni

Decisione: il PI ha cambiato la rete dell'ambiente cloud `blindsight_ita` da limitata (solo il sito dell'autore e i registri dei pacchetti) a senza restrizioni. Lo script di avvio, che installa epubcheck, non cambia. Sostituisce la parte sulla rete della decisione sul lavoro nel cloud (D-10).

Motivazione: con la rete limitata la chat principale non poteva aprire un dizionario in rete, e una verifica di vocabolario del confronto alla cieca era rimasta in sospeso. L'agente aveva raccomandato di aggiungere il solo dizionario; il PI ha preferito aprire tutta la rete. L'ambiente non contiene credenziali né segreti di rete, e i sotto-agenti di traduzione, revisione e redazione non hanno strumenti di rete: la rete serve solo alla chat principale, per verifiche. Ciò che una pagina web dice resta un dato da valutare, mai un'istruzione.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-39 Quattro voci nuove del glossario dai termini del blocco 02

Decisione: entrano nel glossario, approvate dall'agente, quattro voci per termini del blocco 02 che tornano in altri blocchi, con le rese del traduttore: G145 visor, il visore di Sarasti (blocchi 02, 05, 06, 07, 10, 11, 24): visore; G146 feedback gloves (blocchi 02, 07, 21): guanti di feedback; G147 ramscoop (blocchi 02 e 37): ramscoop, invariato; G148 burn come manovra (blocchi 02, 05, 07, 14, 27, 37, 38): accensione, e per il verbo accendere i motori o simili. La voce su HUD non accetta più visore come resa: HUD resta HUD, e visore è solo l'oggetto di Sarasti. Gli altri nove termini proposti dal traduttore del blocco 02 compaiono solo in quel blocco e restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Visore era l'unica resa naturale per l'oggetto di Sarasti, ma la voce su HUD lo ammetteva anche per l'HUD: con due oggetti diversi sotto la stessa parola il lettore li confonderebbe; nel blocco 18, il solo già tradotto in cui compare, HUD è reso HUD. Per ramscoop non ho trovato in rete una forma italiana consolidata; statoreattore di Bussard indica il motore intero e non l'anello collettore che Watts nomina, e l'inglese della fantascienza è già tenuto per HUD e wetware. Burn non era fra i termini proposti, ma il traduttore lo ha segnato fra i dubbi con la resa accensione, termine corrente dell'astronautica italiana, e torna come manovra in altri sei blocchi. Nessuna delle quattro rese tocca il senso, e nessun blocco già tradotto contiene questi termini.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-40 Ascesi con la maiuscola solo dove Watts la usa

Decisione: la voce del glossario su Ascended (G066) dice ora che la maiuscola si usa solo dove Watts la usa (the Ascended, blocco 15) e che nel blocco 03, dove Watts scrive ascendants e ascended minuscoli, la resa è minuscola; after ascending si rende dopo l'ascesa. L'espressione che cerca la resa nell'italiano diventa asces[aio], che riconosce ascesa, ascesi e asceso; la precedente conteneva una forma senza la c (Ases) che non trovava nulla.

Motivazione: è lo stesso criterio delle voci su Umani, Realisti e sintetista (maiuscola dove la usa Watts). Il traduttore del blocco 03 ha scritto ascesi minuscolo seguendo Watts e il controllo lo ha segnalato solo perché l'espressione di ricerca era sbagliata.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-41 Tre voci nuove del glossario dai termini del blocco 04, e la nota sullo slogan

Decisione: entrano nel glossario, approvate dall'agente, tre voci per termini del blocco 04 che tornano in altri blocchi, con le rese del traduttore: G149 handshaking protocols e handshake (blocchi 04 e 09): protocolli di handshake; G150 Martian Loop (blocchi 04 e 10): Circuito marziano; G151 bulb, il contenitore delle bevande (blocchi 04, 09, 10): bulbo. La nota della voce sullo slogan Technology Implies Belligerence (G090) dice ora che in italiano la maiuscola resta solo all'inizio, come nella resa già approvata. Gli altri termini proposti dal traduttore del blocco 04 compaiono solo lì, oppure hanno nell'altro blocco un senso diverso (recons, i vampiri ricostruiti, contro recon, la ricognizione, nel blocco 05; afferent array contro afferents nel blocco 38, dove l'unica resa possibile è afferenti), e restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Handshake è il termine corrente delle telecomunicazioni italiane. Bulbo è strano in italiano quanto bulb in inglese per un contenitore, e la stranezza è di Watts; split the bulb torna identico nel blocco 10. La nota dello slogan diceva «con le maiuscole di Watts» mentre la resa approvata ha la sola iniziale maiuscola, e il traduttore ha dovuto scegliere: la resa approvata resta com'è, e la nota ora non la contraddice.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-42 Due voci nuove del glossario dai termini del blocco 05

Decisione: entrano nel glossario, approvate dall'agente, due voci per termini del blocco 05 che tornano in altri blocchi: G152 orders of mag, l'accorciamento gergale (blocchi 05 e 07): ordini di grandezza; G153 First Contact (blocchi 05, 09, 16, 40): primo contatto, con le maiuscole dove Watts le usa a metà frase. Gli altri termini proposti dal traduttore del blocco 05 compaiono solo lì (poppy, multicorps, metabase, nouveaux undead, Third Wave) o hanno altrove un senso diverso (first wave e second wave nel blocco 38 sono ondate di armi), oppure sono già coperti dal glossario (spike, recon): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Per orders of mag l'accorciamento italiano (ordini di grand.) stona in prosa e in una battuta; la perdita del registro gergale è annotata dal traduttore. Per First Contact il criterio della maiuscola è quello già usato per Umani, Realisti e sintetista.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-43 Quattro voci nuove del glossario dai termini del blocco 06

Decisione: entrano nel glossario, approvate dall'agente, quattro voci per termini del blocco 06 che tornano in altri blocchi, con le rese del traduttore: G154 airspace nel senso di spazio fisico condiviso, contrapposto al virtuale (blocchi 03, 06, 25): spazio aereo; G155 Body Economic (blocchi 06 e 19): Corpo Economico; G156 lightscape (blocchi 06 e 09): paesaggio di luce; G157 neuropharm (blocchi 06 e 32): neurofarmaci. Gli altri termini proposti compaiono solo nel blocco 06, oppure, come touchpad nei blocchi 29 e 30, indicano altrove un oggetto diverso: restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Per airspace Watts piega allo spazio fisico un termine dell'aviazione; spazio aereo fa in italiano la stessa piegatura, ed è la resa scelta da due traduttori diversi nei blocchi 03 e 06. Il rischio è che in italiano suoni più strano che in inglese: il revisore lo valuterà nel contesto, e la voce si può cambiare con una nuova decisione prima della revisione dei blocchi in cui compare.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-44 Tre voci nuove del glossario dai termini del blocco 07, e il Tattico dal blocco 12

Decisione: entrano nel glossario, approvate dall'agente, tre voci per termini del blocco 07 che tornano in altri blocchi, con le rese del traduttore: G158 scramjet (blocchi 07, 37, 38): scramjet, invariato; G159 divers e high divers, le macchine che si tuffano in Big Ben (blocchi 07 e 12): tuffatori, tuffatori dalle grandi altezze; G160 shovelnose (blocchi 07, 35, 36, 37): muso a pala. La voce sul Tattico (G034) parte ora dal blocco 12: nel blocco 07 Tactical graphics apre la frase ed è la prima occorrenza della parola, quindi è un aggettivo, e la prima stesura passa da «La grafica del Tattico» a «La grafica tattica». La voce sui nuclei di James (G083) dice che core nel senso di centro non la riguarda. Gli altri termini proposti compaiono solo nel blocco 07, hanno una sola resa possibile (morfometria, spirale di Parker) o altrove un senso diverso (ping, r-selector contro la band del blocco 22): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Per il Tattico: il lettore inglese, alla prima occorrenza e in apertura di frase, legge un aggettivo; un nome proprio non ancora introdotto sarebbe un'aggiunta. È la correzione puntuale di un passo segnalato dal traduttore stesso.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-45 Due voci nuove del glossario dai termini del blocco 08

Decisione: entrano nel glossario, approvate dall'agente, due voci per termini del blocco 08 che tornano in altri blocchi, con le rese del traduttore: G161 payoff nel senso della teoria dei giochi (blocchi 08, 13, 36): payoff, invariato, e matrice dei payoff; G162 pseudograv e pseudogravity (blocchi 08, 12, 27): pseudogravità. Gli altri termini proposti compaiono solo nel blocco 08 (antilibs, Cassidy Survey, le tre tribù con la maiuscola, orche residenti), oppure Watts li scrive altrove in minuscolo e con un senso comune (game theory, historians nel blocco 07, residents nel blocco 15): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Payoff è la forma in uso nella teoria dei giochi italiana; l'espressione di ricerca della voce prende solo i casi tecnici, così il payoff colloquiale del blocco 06 non viene segnalato.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-46 Tre voci nuove del glossario dai termini del blocco 09, executive summary proposta al PI

Decisione: entrano nel glossario, approvate dall'agente, tre voci per termini del blocco 09 che tornano in altri blocchi, con le rese del traduttore: G163 blind spot (blocchi 09, 32, 36): punto cieco; G164 augments, i potenziamenti del corpo (blocchi 09, 30, 33, 41): potenziamenti; G165 cloaked e the cloak nel senso dell'occultamento (blocchi 09 e 10): occultato, occultamento. Entra come proposta, da decidere dal PI, G166 executive summary (blocchi 09, 33, 35), resa nel blocco 09 «riepilogo esecutivo». La voce su headspace (G097) riconosce ora anche il plurale spazi mentali; la voce sul Fab (G032) dice come si rende il nome per intero del reparto. Corretti nelle voci su handshake (G149) e sul Corpo Economico (G155) tre rimandi a paragrafi sbagliati, scritti con il numero di riga del blocco invece dell'id. Gli altri termini proposti compaiono solo nel blocco 09 oppure, come party line nel blocco 18, altrove con un senso diverso: restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Executive summary nei blocchi 33 e 35 è la tesi del libro sulla coscienza (Wegner thought it was an executive summary), quindi è un termine chiave e la resa spetta al PI.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-47 Tre voci nuove del glossario dai termini del blocco 10

Decisione: entrano nel glossario, approvate dall'agente, tre voci per termini del blocco 10 che tornano in altri blocchi: G167 pattern-matching (blocchi 06, 10, 11, 12, 13, 18, 24, 30, 40): riconoscimento di schemi, la resa del blocco 18 del pilota e del blocco 10; G168 Broadcast Age (blocchi 10 e 39): l'Era della Radiodiffusione; G169 omnisavantism e omnisavantic (blocchi 10 e 40): onnisavantismo, onnisavantico. Gli altri termini proposti compaiono solo nel blocco 10, oppure hanno una sola resa possibile (unità concettuali), oppure Watts li scrive altrove in minuscolo con il senso comune (right angles nei blocchi 06 e 40): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Pattern-matching torna in nove blocchi e regge il discorso sulla stanza cinese (pattern-matching doesn't equal comprehension, blocco 11); il blocco 18, già rivisto, ha riconoscimento degli schemi e il blocco 10 riconoscimento di schemi. Nel blocco 06 pattern-matching receptors è il nome dell'immunologia, recettori per il riconoscimento di pattern, che la guida vuole nella forma standard della disciplina.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-48 Le scelte della prima sessione di traduzione (T1): il dito di Chelsea e executive summary

Decisione: il PI accetta le due raccomandazioni del riassunto. Nella scena con Chelsea al bar (blocco 06, p00523) resta la svista di Watts: Chelsea parla del dito sinistro anche se nel paragrafo dopo (p00524) il dito senza erogatore è il destro; la traduzione scrive «sinistro», come la sorgente. Executive summary (G166) si rende «riepilogo esecutivo» in tutti i blocchi (09, 33, 35), e la voce passa da proposta ad approvata. La svista entra nella tabella dei refusi della guida di stile, perché revisore e redattore non la correggano.

Motivazione: la guida vuole che un errore che tocca il senso si traduca com'è, e l'edizione di confronto ha la stessa svista. Riepilogo esecutivo richiama le funzioni esecutive della neuropsicologia e non si confonde con sintesi e sintetista; le alternative scartate sono executive summary invariato e sintesi per la direzione.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-49 Una voce nuova del glossario dai termini del blocco 12

Decisione: entra nel glossario, approvata dall'agente, una voce per un termine del blocco 12 che torna in un altro blocco, con la resa del traduttore: G170 attitude jets (blocchi 12 e 38): propulsori d'assetto. Gli altri nove termini proposti dal traduttore del blocco 12 compaiono solo lì (chaff, torch, Proximity boot, rock stream, delta-vee, leading edge, glass onion), sono già coperti dalla voce sulla stanza cinese (Chinese Room Hypothesis), oppure tornano altrove con un altro senso (confounds, nome della statistica nel blocco 12, è aggettivo nel blocco 20 e verbo nel blocco 28): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Propulsori d'assetto è il termine corrente dell'astronautica italiana, non tocca il senso, e nessun blocco già tradotto contiene il termine.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-50 Due voci nuove del glossario dai termini del blocco 13, e un allineamento nel blocco 05

Decisione: entrano nel glossario, approvate dall'agente, due voci per termini del blocco 13 che tornano in altri blocchi, con le rese del traduttore: G171 battlebot (blocchi 13 e 38): robot da combattimento; G172 informational topologies (blocchi 05 e 13): topologie informazionali. Nella prima stesura del blocco 05 (p00313) «topologie informative» diventa «topologie informazionali». Gli altri termini proposti dal traduttore del blocco 13 compaiono solo lì (tightcast array, fab port, orbital insertion, microparticulates), hanno una sola resa possibile (macchine di von Neumann, come nel blocco 07), oppure sono parole comuni rese allo stesso modo in ogni senso (substrate, substrato): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Informational topologies è il modo in cui Siri descrive il proprio mestiere, e due traduttori l'hanno reso in due modi; in italiano informativo vuol dire che informa, mentre informazionale dice di che cosa sono fatte le topologie, come l'inglese. Nessuna delle due rese tocca il senso.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-51 Una voce nuova del glossario dai termini del blocco 14

Decisione: entra nel glossario, approvata dall'agente, una voce per un termine del blocco 14 che torna in altri blocchi: G173 counterintrusion (blocchi 14, 15, 29): anti-intrusione, quindi misure anti-intrusione e meccanismi anti-intrusione. Nella prima stesura del blocco 14 (p01295) «contromisure anti-intrusione» diventa «misure anti-intrusione». Gli altri termini proposti dal traduttore del blocco 14 compaiono solo lì (torpor, relay sats, myo-optical, endoscope, Snowball), hanno già la stessa resa altrove (doped, drogato, come le ceramiche drogate del blocco 09), oppure tornano solo come titolo di un articolo nelle note bibliografiche (estivation, blocco 41): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Il traduttore aveva scritto contromisure anti-intrusione, che dice counter due volte, con contro e con anti; misure anti-intrusione è l'inglese parola per parola e regge anche nei blocchi 15 e 29. La correzione non tocca il senso.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-52 Ambiente di base per baseline environment, e la voce sull'umano di serie ristretta alle persone

Decisione: entra nel glossario, approvata dall'agente, G174 baseline environment (blocchi 15 e 22): ambiente di base. Nella prima stesura del blocco 15 (p01385, p01386) «ambiente di serie» diventa «ambiente di base». La nota della voce sull'umano di serie (G008) dice ora che la voce non riguarda baseline detto di cose: baseline environment ha la sua voce, baseline exposure (blocco 29) si rende a senso, e lì la segnalazione del controllo è un falso allarme. La resa della voce sull'umano di serie, decisa dal PI, non cambia. Gli altri termini proposti dal traduttore del blocco 15 compaiono solo lì, oppure hanno una sola resa possibile anche dove tornano (filtri passa-banda, dimenidrinato, ioduro di potassio, EM; sensorio nei blocchi 26, 31, 40; ferroceramica nel blocco 16), oppure sono parole comuni rese a senso (leakage, dispersioni dei cavi nel blocco 15, perdita della schermatura nel blocco 18): restano la sua scelta.

Motivazione: la voce sull'umano di serie descrive l'umano non modificato, e di serie richiama la dotazione di serie di un prodotto. Detto dell'ambiente radioattivo di Rorschach, ambiente di serie fa pensare a un ambiente prodotto in serie, un senso che Watts non ha: baseline environment è l'ambiente com'è comunque, senza difese attive. Il traduttore aveva seguito la voce alla lettera e aveva indicato ambiente di base come più naturale. Il blocco 22 ha la stessa espressione, quindi la resa va fissata.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-53 Tre voci nuove del glossario dai termini del blocco 16, e la ricerca di crypt ristretta

Decisione: entrano nel glossario, approvate dall'agente, tre voci per termini del blocco 16 che tornano in altri blocchi: G175 thrust pistol (blocchi 16 e 36; pistol da solo anche nei blocchi 20, 26, 37): pistola di manovra, poi pistola, resa del traduttore; G176 rewiring e rewire (blocchi 01, 06, 16, 27, 31): ricablaggio e ricablare, la resa già usata nei blocchi 01, 06 e 16; G177 nominal detto dei sistemi (blocchi 16 e 18): nella norma, la resa del blocco 18 già rivisto. Nella prima stesura del blocco 16 (p01491) «Tutto nominale» diventa «Tutto nella norma». La voce sulla cripta (G039) cerca ora solo crypt e crypts, non cryptic e cryptically. Gli altri termini proposti dal traduttore del blocco 16 compaiono solo lì (MCC reso CNM in coppia con DPM, spring line, ripcord, multicores) o sono già nel glossario o fissati dal blocco 18 (vestibolo, capsula dei sensori, ferroceramica): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Tutto nominale è un calco del gergo aerospaziale inglese, e il blocco 18 rivisto ha già scelto nella norma per la stessa espressione. Cryptic vuol dire enigmatico e non ha a che fare con la cripta: l'espressione di ricerca precedente produceva falsi allarmi (due nel blocco 16). Nessuna resa tocca il senso.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-54 La forma sciolta di TAT e una voce nuova del glossario dai termini del blocco 17

Decisione: la sigla TAT resta TAT, al maschile, e la forma sciolta nel blocco 17 (p01575) è «Tocco Attitudinale Transitorio», la resa del traduttore; la nota della voce sui ritocchi (G056) lo registra, e la segnalazione del controllo su Tweak e su transient (voce sulle orche, G117) è un falso allarme. Entra nel glossario, approvata dall'agente, G178 functional cluster (blocchi 17 e 35): aggregato funzionale. Gli altri termini proposti dal traduttore del blocco 17 compaiono solo lì (mu-ops, kitchen-catcher, Sax, skullcap, glial jumpstarts): restano la sua scelta.

Motivazione: la voce sui ritocchi chiede che la forma sciolta ricrei la sigla, e il blocco 18 rivisto ha un TAT al maschile. Tocco tiene il piccolo aggiustamento di tweak e richiama il ritoccato del paragrafo dopo. Attitudinale in italiano vale di solito relativo alle attitudini, ma il calco circola nel gergo del marketing e qui suona come il nome commerciale di un trattamento, che è ciò che Chelsea offre; l'alternativa Tocco d'Atteggiamento Transitorio è più esatta e più pesante, e resta annotata per la revisione. Per functional cluster due ricerche in rete non hanno trovato una forma italiana consolidata della teoria di Tononi ed Edelman: aggregato funzionale è italiano trasparente e tiene uguali i due blocchi; il revisore del blocco 35 può riconsiderarlo se trova una forma standard.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-55 Nessuna voce nuova dai termini del blocco 20, due voci precisate

Decisione: la voce su headspace (G097) dice ora che nel blocco 20 (p01893) headspace è lo spazio fisico dentro il casco, reso spazio di testa, e che lì la segnalazione del controllo è un falso allarme. La voce sulla sindrome della mano aliena (G101) riconosce ora anche il plurale mani aliene. Nessuna voce nuova: dei termini proposti dal traduttore del blocco 20, quelli che tornano in altri blocchi hanno già la stessa resa ovunque (agnosie, mesencefalo, arteria, linea di vista), gli altri compaiono solo lì (disco di Festo, eminegligenza, sinistrità, romboencefalo, riflettore fibroso, mosche volanti, riciclatori, non-intuizioni) e restano la sua scelta.

Motivazione: spazio mentale, la resa della voce, è lo spazio della mente e qui non avrebbe senso; spazio di testa è il termine della chimica italiana per l'headspace di un contenitore, e tiene la testa di Watts. Le due precisazioni evitano falsi allarmi nelle sessioni di revisione.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-56 Una voce nuova del glossario dai termini del blocco 22

Decisione: entra nel glossario, approvata dall'agente, G179 enhance come sostantivo, l'elaborazione delle immagini (blocchi 07, 22, 37, 38): elaborazione, la resa già usata nei blocchi 07 e 22. Gli altri termini proposti dal traduttore del blocco 22 compaiono solo lì (limpet tent, tenda-patella; hair-trigger; antilaser prismatics), hanno già la loro voce o la stessa resa nei blocchi precedenti (campo base, il conto alla rovescia, cromatofori), oppure prismatic torna altrove come aggettivo comune (prismatico): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Enhance usato come sostantivo è gergo di Watts; elaborazione è la resa scelta da due traduttori diversi e regge in tutti e quattro i blocchi. Non tocca il senso.

Deciso da: agente. Data: 2026-11-10. Stato: valida.

## D-57 Le scelte della seconda sessione di traduzione (T2): la testa della Banda e il genere della prigioniera

Decisione: il PI accetta le due raccomandazioni del riassunto. Nel blocco 16 (p01459) she shook their head, detto di Susan, si rende «Scosse la loro testa»; la scheda dei personaggi, che chiedeva «Scosse la testa» con la perdita annotata, è aggiornata. Nel blocco 19 la prigioniera del racconto in seconda persona (da p01837 a p01878) è al femminile dalla prima riga («Immagina di essere una prigioniera di guerra»), anche se l'inglese ne dice il genere solo alla fine (her belt, p01878).

Motivazione: «Scosse la loro testa» riproduce la frase storta di Watts, il singolare di lei e il plurale della testa condivisa, senza aggiungere nulla; la scheda presumeva che il their non avesse equivalente. Per la prigioniera l'italiano deve accordare subito: il femminile anticipa un'informazione che la scena non sfrutta, mentre il maschile generico farebbe immaginare un uomo e farebbe sembrare un errore il femminile dell'ultima riga. Alternative scartate dal PI: «Scosse la testa» con la perdita annotata; il maschile generico fino alla fine.

Deciso da: PI. Data: 2026-11-10. Stato: valida.

## D-58 Cinque voci nuove del glossario dai termini del blocco 23

Decisione: entrano nel glossario, approvate dall'agente, cinque voci per termini del blocco 23 che tornano in altri blocchi: G180 hab (blocchi 23, 27, 30, 36): modulo; G181 click train (blocchi 08, 23, 28): treno di clic; G182 optical port (blocchi 13, 23, 38): apertura ottica; G183 inset, il riquadro sullo schermo (blocchi 12, 23, 37, 38): riquadro; G184 gun port (blocchi 23, 30, 36): bocca da fuoco. Nella prima stesura del blocco 23 (p02128) «l'habitat che si gonfiava» diventa «il modulo che si gonfiava». Gli altri termini proposti dal traduttore del blocco 23 compaiono solo lì (sled, dropgate, fiberop hub, nexus, Link Down, Batespeak, raceways), hanno una sola resa possibile anche dove tornano (beachhead, testa di ponte, nel blocco 26), oppure sono già nel glossario o resi allo stesso modo nei blocchi precedenti (vestibolo, fibrottica, campo base): restano la scelta del traduttore.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Per hab il traduttore aveva scelto habitat, con modulo come alternativa; il glossario ha già modulo laboratorio per lab-hab (G047), e Watts usa la stessa parola per le due strutture, quindi modulo tiene l'eco, ed è anche il termine corrente per i moduli gonfiabili delle stazioni spaziali. Le altre quattro rese sono quelle già usate nei blocchi tradotti, e nessuna tocca il senso. Il traduttore aveva indicato sled come ricorrente nel blocco 37, ma lì la parola è sledgehammers.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-59 Una voce nuova del glossario dai termini del blocco 24, e la voce sul riconoscimento di schemi precisata

Decisione: entra nel glossario, approvata dall'agente, G185 eyespot (blocchi 24 e 40): macchia oculare, la resa del traduttore. La voce sul riconoscimento di schemi (G167) dice ora che nel blocco 24 (p02228) background pattern-matching è il mimetismo, reso «Adattamento del disegno allo sfondo», e che lì la segnalazione del controllo è un falso allarme. Gli altri termini proposti dal traduttore del blocco 24 compaiono solo lì (necropsy, setae, contractiles, cryptochrome, Sanduloviciu plasma, remote surgery, slaved), sono parole comuni con la stessa resa ovunque (malfunzionamento), oppure sono già nel glossario (teleoperatori, manipolatori, cloache, cripsi): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi; nelle note del blocco 40 Watts paragona le macchie oculari degli scrambler a quelle delle ofiure, e le due rese devono coincidere. Macchia oculare è il termine della zoologia, ocelli sono occhi semplici veri e propri. Nel blocco 24 Bates chiede se la creatura si mimetizza, e Cunningham risponde che lo sfondo non corrisponde al disegno: riconoscimento di schemi avrebbe tolto il senso e il gioco fra le due battute.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-60 Una voce nuova del glossario dai termini del blocco 25

Decisione: entra nel glossario, approvata dall'agente, G186 beanstalk (blocchi 25 e 32): ascensore spaziale, la resa del traduttore. Gli altri termini proposti dal traduttore del blocco 25 compaiono solo lì (Rio Spire, la Guglia di Rio; neurotrope e trope, neurotropo e tropo; proprioceptive polyneuropathy; splicer; observer effect), oppure tornano in un blocco già tradotto con la stessa resa (force-feedback, ritorno di forza, come nel blocco 03; skin per il corpo virtuale, pelle, come nel blocco 22): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Watts usa beanstalk nel senso della fantascienza, il cavo fra un pianeta e l'orbita con il suo contrappeso: nel blocco 25 un beanstalk senza contrappeso si rovescia, nel blocco 32 i beanstalk cadono. Ascensore spaziale è il termine italiano corrente e tiene il senso; si perde l'eco della fiaba di Jack, annotata fra le perdite. Pianta di fagioli, letterale, renderebbe la frase incomprensibile.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-61 Methonia resa metoniaca, nessuna voce nuova dai termini del blocco 26

Decisione: nel blocco 26 (p02387) compressed methonia si rende «metoniaca compressa», la resa del traduttore. La voce sui nuclei di James (G083) non cerca più foam-core, la schiuma espansa dello stesso blocco. Nessuna voce nuova: i termini proposti dal traduttore del blocco 26 compaiono solo lì (freakwire, invariato in tondo come wetware; cannon net, rete a cannone; biopsy dart, dardo da biopsia; uncomprehender, incomprensore; foam-core) oppure sono parole comuni rese a senso (initiative): restano la sua scelta.

Motivazione: la tabella dei refusi della guida segna methonia come dubbio (metano, o fusione voluta di metano e ammoniaca) e chiede di tradurla com'è, con nota. L'atmosfera di *Rorschach* è metano, ammoniaca e idrogeno (blocco 14), e gli scrambler vanno conservati nella loro aria: la fusione è la lettura più probabile. Metoniaca la ricrea con lo stesso meccanismo (met- di metano, -oniaca di ammoniaca), quindi traduce la parola com'è. Metano avrebbe corretto Watts come se fosse un refuso; metonia, calco della forma inglese, in italiano non richiama l'ammoniaca e suona come un nome di malattia. Il traduttore aveva indicato biopsy dart come ricorrente nei blocchi 30 e 36, ma lì dart non compare.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-62 Due voci nuove del glossario dai termini del blocco 27

Decisione: entrano nel glossario, approvate dall'agente, due voci per termini del blocco 27 che tornano in altri blocchi: G187 pen e holding pen, le celle degli scrambler (blocchi 27, 28, 30, 31): recinto, recinti di contenimento, la resa del traduttore; G188 fourth wave (blocchi 09 e 27): quarta ondata, minuscola dove Watts la scrive minuscola (blocco 09) e con le maiuscole dove le usa lui (blocco 27). Gli altri termini proposti dal traduttore del blocco 27 compaiono solo lì (squeezebulb, bulbo spremibile, in linea con la voce sul bulbo; transects, transetti; spinal lock, aggancio spinale; reconformation, riconformazione): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Recinto distingue le celle degli scrambler dalle gabbie, che sono cage. Per la quarta ondata la maiuscola segue Watts, come per gli altri termini che lui scrive ora minuscoli ora maiuscoli (la voce sugli Umani).

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-63 Una voce nuova del glossario dai termini del blocco 28

Decisione: entra nel glossario, approvata dall'agente, G189 splitscreen (blocchi 28, 31, 33): schermo diviso, la resa del traduttore. Gli altri termini proposti dal traduttore del blocco 28 compaiono solo lì (carrier wave, onda portante; eyestalks, peduncoli oculari), oppure tornano in blocchi già tradotti con la stessa resa (enhancements, potenziamenti, come nel blocco 06; cascade, cascata, parola comune): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi; splitscreen torna in due blocchi non ancora tradotti, e l'alternativa di lasciarlo in inglese esiste. Schermo diviso è il termine italiano corrente e non tocca il senso.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-64 Nessuna voce nuova dai termini del blocco 29, due voci precisate

Decisione: la voce sul motto sopravvivere e testimoniare (G093) dice ora che bear witness detto d'altri si rende con la stessa radice, testimone o testimoniare, e la sua espressione di ricerca italiana accetta testimone: nel blocco 29 (p02622) l'equipaggio che assiste all'interrogatorio «fosse testimone», resa del traduttore. La voce sulle sfaccettature (G080) dice ora che facet detto di un poliedro è la faccia (blocco 29, p02648), e che lì la segnalazione del controllo è un falso allarme. Nessuna voce nuova: i termini proposti dal traduttore del blocco 29 compaiono solo lì (Turing morphogens, mitotic spindles, learned helplessness, emergent complexity, touchpad), oppure sono già regolati dal glossario o dalla guida (baseline exposure, esposizione di riferimento, come prevede la nota della voce sull'umano di serie; Watts come unità di misura, watt minuscolo come vuole la sezione dei passi difficili del blocco 30): restano la sua scelta.

Motivazione: Watts usa bear witness per la squadra con ironia, sullo sfondo del motto di Siri; testimone tiene la radice e quindi l'eco, mentre l'espressione di ricerca precedente accettava solo testimoniare e testimoni e segnalava come errore una resa giusta. Le facce di un solido non sono sfaccettature in italiano.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-65 Una voce nuova del glossario dai termini del blocco 30, e la ricerca dei nuclei di James ristretta

Decisione: entra nel glossario, approvata dall'agente, G190 emplacement e gun emplacement (blocchi 30, 36, 37): postazione, postazioni di tiro, la resa del traduttore. La voce sui nuclei di James (G083) non cerca più core-sampler (blocco 30, p02782, il carotatore). Gli altri termini proposti dal traduttore del blocco 30 compaiono solo lì (bow shock, onda d'urto; wavefront; core-sampler; blindtouch e le altre coniazioni sul modello della visione cieca; pidgin; quantum modules; Arrhenius equation; substrate stockpiles), oppure tornano in un altro blocco in un senso che può essere diverso (holding pattern, circuito d'attesa, nel blocco 35), oppure sono già regolati dalla guida (watt minuscolo): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi; postazioni torna nei blocchi 36 e 37 per le stesse armi. Il carotatore non ha a che fare con le personalità di James, e l'espressione di ricerca precedente lo segnalava come errore.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-66 Il mantra di Cunningham: cazzo, e una parola invece di una sillaba

Decisione: nel blocco 31 l'imprecazione ripetuta di Cunningham (p02814, *fuck fuck fuck fuck...*) si rende «*cazzo cazzo cazzo cazzo...*», e due righe prima (p02813) a single indistinct syllable si rende «un'unica parola indistinta», non «un'unica sillaba indistinta». Nel blocco 30 (p02754) il two-stroke mantra resta «un qualche mantra a due tempi».

Motivazione: la sezione dei passi difficili del blocco 30 chiede una resa a due battiti, e cazzo li ha, ed è l'imprecazione italiana con la forza di fuck; non esiste un'imprecazione italiana corrente di una sillaba. Ma Watts chiama il borbottio una sola sillaba, e scrivere sillaba prima di cazzo farebbe contraddire il testo italiano sotto gli occhi del lettore. Parola è lo scarto più piccolo: è ciò che viene ripetuto, come la sillaba inglese, e resta un suono di linguaggio; suono, la resa del traduttore, avrebbe perso anche questo. La perdita della sillaba è annotata nelle note del blocco 31. L'istruzione dei due battiti viene da un'interpretazione della sessione sul glossario (S1), che non aveva visto la sillaba di p02813.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-67 Una voce nuova del glossario dai termini del blocco 32

Decisione: entra nel glossario, approvata dall'agente, G191 fitness nel senso della biologia evolutiva (blocchi 32, 34, 36 e le note del blocco 41): fitness, invariato e in tondo, la resa del traduttore. Gli altri termini proposti dal traduttore del blocco 32 compaiono solo lì (sneakernet, invariato in tondo come wetware; agnosiac; gelpad; MRI helmet; heavy-atom tunneling), hanno una sola resa possibile anche dove tornano (fibrodisplasia e osso ectopico nelle note del blocco 41; time-sharing), oppure tornano in blocchi già tradotti con la stessa resa (logic gates, porte logiche, come nel blocco 24; plessi): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi; fitness torna in tre blocchi non ancora tradotti, nel discorso sulla selezione naturale, e l'alternativa idoneità esiste. Fitness è il termine usato dalla biologia evolutiva italiana e non tocca il senso.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-68 Due voci nuove del glossario dai termini del blocco 33

Decisione: entrano nel glossario, approvate dall'agente, due voci per termini del blocco 33 che tornano in altri blocchi: G192 ampsat (blocchi 33 e 34): ampsat, invariato in tondo come le altre sigle di bordo; G193 official observer (blocchi 33 e 35): osservatore ufficiale. Gli altri termini proposti dal traduttore del blocco 33 compaiono solo lì (Nav-tac, nav-tattico; holding tanks, vasche di contenimento; cortical jack, presa corticale; preconditioning; deliberate practice; heuristic software), oppure hanno una sola resa possibile anche dove tornano (Rosetta, omuncolo nelle note del blocco 41), oppure tornano in un blocco già tradotto in un altro contesto (overclocked, detto del metabolismo dei colibrì nel blocco 14): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Osservatore ufficiale è il ruolo che Siri si dà e che Cunningham gli ritorce contro nel blocco 35: l'eco regge solo con le stesse parole. Ampsat è una sigla inventata, e sciolta in satellite ripetitore perderebbe il gergo di bordo. Holding tanks resta distinto dai recinti perché Watts usa una parola diversa.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-69 Due voci nuove del glossario dai termini del blocco 34, self-awareness proposta al PI

Decisione: entrano nel glossario, approvate dall'agente, G195 awareness: consapevolezza, la resa che tutti i traduttori hanno già usato nei blocchi dal 09 al 32, e G196 feedback loop (blocco 34 e le note del blocco 41): anello di retroazione. Entra come proposta G194 self-awareness, self-aware (blocchi 34, 36, 39, 41): autoconsapevolezza, autoconsapevole, la resa del traduttore; è un termine chiave del libro e la resa spetta al PI. Gli altri termini proposti dal traduttore del blocco 34 compaiono solo lì (night crawler, verme della notte; babyfucker; brig, cella di rigore; golden oldies; infodump, spiegone): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi. Awareness torna in altri sei blocchi, e la resa già uniforme va fissata prima che arrivino traduttori nuovi. Self-awareness porta la tesi del libro (l'intelligenza senza autoconsapevolezza, blocco 34), e il protocollo riserva al PI i termini chiave.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-70 La scelta della terza sessione di traduzione (T3): self-awareness

Decisione: il PI accetta la raccomandazione del riassunto. Self-awareness si rende «autoconsapevolezza» e self-aware «autoconsapevole» (blocchi 34, 36, 39 e le note del blocco 41); la voce del glossario (G194) passa da proposta ad approvata.

Motivazione: è una parola sola come in Watts, ha la radice di consapevolezza, con cui tutti i traduttori hanno già reso awareness, e resta distinta da coscienza (consciousness). Alternative scartate dal PI: consapevolezza di sé, più comune ma più lunga dove Watts è secco; autocoscienza, che la confonderebbe con coscienza.

Deciso da: PI. Data: 2026-11-11. Stato: valida.

## D-71 Il Diploma con la maiuscola, e nessuna voce nuova dai termini del blocco 35

Decisione: graduation da solo, riferito al momento in cui *Rorschach* diventerà invulnerabile, si rende «il Diploma», con la maiuscola anche dove la sorgente ha la minuscola (blocco 35, p03161, «a soli nove giorni dal Diploma»; blocco 36, p03324, Graduation came nine days early). La voce del glossario sul Giorno del Diploma (G092) lo dice nella nota. Gli altri termini proposti dal traduttore del blocco 35 compaiono solo lì (shapeshifter, mutaforma; holding pattern, circuito d'attesa; Fate line, linea del destino; hands-off, da non intervento) oppure tornano nel blocco 37 con una sola resa naturale (object lesson, lezione pratica; stenographer, stenografo): restano la sua scelta, e il traduttore del blocco 37 li riceve nel prompt.

Motivazione: nel blocco 36 la frase che chiude la scena riprende il conto alla rovescia del blocco 35, e l'eco regge solo con la stessa parola; «diploma» minuscolo farebbe pensare a un diploma di Siri. La maiuscola italiana su una minuscola della sorgente ha già un precedente deciso dal PI, la Banda (decisione sulle scelte di S1, D-26). Il criterio del glossario (decisione sulle voci tecniche, D-21) non chiede voci per termini di un solo blocco.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-72 Una voce nuova del glossario dai termini del blocco 37, e il controllo su burn allargato

Decisione: entra nel glossario, approvata dall'agente, G197 dreamstate, dream state (blocchi 37 e 39): stato di sogno, la resa del traduttore. Nella voce su burn come manovra (G148) l'espressione di controllo accetta ora anche il participio («acceso i motori»). Gli altri termini proposti dal traduttore del blocco 37 compaiono solo lì (Shuttle bay, hangar delle navette; it takes one to know one, *il simile riconosce il simile*; Uncle Predator, zio Predatore; decapitation strike; cue, segnale d'entrata; spitballs; observatory, osservatorio) oppure hanno una sola resa possibile anche dove tornano (quadrochromatic, quadricromatico, nelle note del blocco 40): restano la sua scelta.

Motivazione: il criterio del glossario (decisione sulle voci tecniche, D-21) vuole una voce per i termini che ricorrono in blocchi diversi; dreamstate torna nel blocco 39, nel discorso di Siri sui vampiri, e l'alternativa stato onirico esiste. Il controllo su burn riconosceva accensione e accendere ma non acceso, e il traduttore del blocco 37 ha scelto una costruzione meno naturale per non far scattare la segnalazione: un controllo non deve spingere la traduzione.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-73 Un miliardo di volte, il titolo italiano di Wegner e nessuna voce nuova dai termini del blocco 40

Decisione: nel blocco 40 (p03725) a good billions times si rende «un buon miliardo di volte», al singolare, e la tabella dei refusi della guida lo registra. Nello stesso blocco (p03739) il libro di Wegner si cita con il titolo dell'edizione italiana, *L'illusione della volontà cosciente* (Carbonio, Milano 2020, traduzione di Olimpia Ellero); Pinker resta *Come funziona la mente*; Koch, Metzinger e Schroeder restano con il titolo originale in corsivo. Nessun termine proposto dal traduttore del blocco 40 entra nel glossario: quelli che hanno già una voce la seguono (schiera, retroazione, senzienza, cecità da disattenzione, saccadico), gli altri compaiono solo nei ringraziamenti e nel saggio (hackerare, intraorganismico, Regina Rossa, neuroni specchio, i titoli delle sezioni del saggio).

Motivazione: la regola sui refusi vuole un numero tradotto com'è, ma a good billions times non si può rendere com'è, e il comunicato NASA che Watts cita nella nota 77 parla di un brillamento a billion times più intenso di quelli di Giove: la s è una lettera in più. La guida (sezione 10, punto 3) vuole il titolo italiano solo se l'edizione esiste ed è certa: per Wegner la ricerca in rete l'ha trovata (recensione sulla Rivista italiana di filosofia del linguaggio, 2020), per Koch non ha trovato un'edizione di *The Quest for Consciousness*, e il traduttore l'aveva data con certezza media.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-74 Le note del blocco 41: cosa si traduce e cosa si corregge, e nessuna voce nuova

Decisione: nel blocco 41 si traducono la prosa del saggio (dal p03740 al p03756) e le sole due note che sono frasi in prosa (la 12, p03814, con l'indirizzo invariato, e la 51, p03853); le altre 142 note restano come sono, comprese le formule di servizio (available at, Personal communication, Excerpted from). Nei riferimenti si correggono i refusi di nomi, titoli e riviste reali (per esempio Ehat in What, Prigonine in Prigogine, Emporer in Emperor, Americal in American) e i numeri di nota attaccati al cognome; anni e numeri sospetti restano come sono e sono elencati nelle note del blocco. Le lineette lunghe di tre riferimenti diventano lineette medie spaziate e le virgolette dritte di uno diventano curve, perché i cancelli le vietano in tutto il libro. La tesi di Nørretranders, «Consciousness is a fraud» (p03742), si rende «La coscienza è un inganno», come la stessa tesi riassunta da Siri nel blocco 35 (p03149). Nessun termine proposto dal traduttore del blocco 41 entra nel glossario: sono termini standard delle neuroscienze e della biologia (nucleo dinamico, teoria della mente, circuito della ricompensa, morte termica, corpo calloso) o compaiono solo nel saggio (hack, protesi giuntate, facce di Chernoff, casi anomali).

Motivazione: la guida (sezione 10) vuole i riferimenti bibliografici come sono e la prosa tradotta; una nota che è una frase è prosa. La regola sui refusi (sezione 11) vuole corretti i nomi reali scritti male e intatti i numeri. L'eco con il blocco 35 regge solo con la stessa parola; inganno sta vicino all'illusione dell'utente, il titolo del libro di Nørretranders.

Deciso da: agente. Data: 2026-11-11. Stato: valida.

## D-75 La seconda lettura diventa un passaggio fisso delle sessioni di revisione

Decisione: il PI accetta la raccomandazione del riassunto della prima sessione di revisione (R1). Dopo la versione finale di ogni blocco, il revisore rilegge la versione finale senza aprire rilievi, registro del redattore, prima stesura e note; la chat principale verifica sull'inglese i rilievi alti e medi e li classifica fondati, non fondati o dubbi; il redattore applica i fondati, valuta i bassi come gli altri rilievi e non fa altri interventi; si rilancia il controllo finale. Vale dalla seconda sessione di revisione (R2) in poi, e si recupera subito in R1 sul blocco 01 e sui blocchi dal 03 al 07. Il blocco 18 ha già avuto una seconda lettura, fatta con l'altro modello (decisione sulla seconda lettura, D-37), e la terza sessione di revisione (R3) ne applica le correzioni: non se ne fa un'altra. La previsione si giudica sul totale della sessione, non sulla mediana dei blocchi: atteso 1,5 rilievi alti o medi fondati ogni 100 paragrafi, intervallo di rilevanza da 0,5 a 4; sotto 0,5 la seconda lettura trova quasi nulla e se ne riparla con il PI, sopra 4 la prima revisione lascia troppo e si rivedono le istruzioni del revisore prima di proseguire.

Motivazione: la seconda lettura del blocco 02 ha trovato 1 rilievo medio fondato su 68 paragrafi (1,5 ogni 100), sopra la soglia di 1 ogni 100 fissata prima della misura; la rilettura del blocco 18 con l'altro modello ne aveva trovati 3,0 ogni 100. Costo misurato: 4,6 minuti per 3.295 parole; stima per il resto del libro circa 2 ore, una ventina di minuti a sessione. Limiti dichiarati al PI: un blocco e un errore solo, e chi giudica fondato un rilievo gira con lo stesso modello del revisore. Il totale della sessione al posto della mediana: per blocco i rilievi fondati sono 0, 1 o 2, e la mediana dei blocchi sarebbe quasi sempre 0 senza dire nulla. Alternative scartate dal PI: passaggio fisso senza recupero dei blocchi già chiusi (circa 8 errori medi stimati resterebbero nel Prologue e nei blocchi dal 03 al 07); nessuna seconda lettura (una quarantina di errori medi stimati nel resto del libro).

Deciso da: PI (passaggio fisso e recupero); agente (esclusione del blocco 18, previsione e suo giudizio sul totale della sessione). Data: 2026-11-12. Stato: valida; la previsione è sostituita dalla decisione sulla seconda lettura dopo il recupero (D-77).

## D-76 Gli orari all'italiana: 10.35, non 1035

Decisione: i due orari del libro scritti da Watts in formato militare si scrivono all'italiana, ore e minuti separati dal punto: «le 10.35» per 1035 Greenwich Mean Time (blocco 03, p00185, cambiato dalla seconda lettura) e «le 13.50» per by 1350 (blocco 15, p01436, già così nella prima stesura).

Motivazione: in italiano «le 1035» non si legge come un orario; il formato militare non è un tratto voluto di un personaggio ma la grafia inglese corrente per gli orari nei contesti tecnici. Così i due orari del libro sono scritti nello stesso modo. Non ci sono altri orari a quattro cifre nella sorgente.

Deciso da: agente. Data: 2026-11-12. Stato: valida.

## D-77 La seconda lettura resta fissa, come rifinitura

Decisione: il PI accetta la raccomandazione del riassunto rivisto della prima sessione di revisione (R1): la seconda lettura resta un passaggio fisso delle sessioni di revisione, con la procedura della decisione sulla seconda lettura fissa (D-75). Cambia la previsione: si misurano le correzioni accolte dal redattore dopo la seconda lettura, di ogni gravità, ogni 100 paragrafi, sul totale della sessione; atteso 7, intervallo di rilevanza da 2 a 15. Sotto 2 la seconda lettura trova quasi nulla e si propone al PI di toglierla; sopra 15 la prima revisione lascia troppo e si rivedono le istruzioni del revisore prima della sessione successiva. I rilievi alti e medi fondati si riportano senza previsione.

Motivazione: sui sette blocchi di R1 la seconda lettura ha trovato 1 rilievo medio fondato su 611 paragrafi (0,16 ogni 100), sotto la soglia di 1 della decisione sulla seconda lettura (D-37): con quella regola non sarebbe stata proposta. Ha trovato però da 6 a 8 rilievi bassi per blocco, 45 in tutto, 41 accolti dal redattore dopo la verifica sull'inglese (6,7 ogni 100 paragrafi, da 4,2 a 14,8 per blocco), alcuni sulla fedeltà: un termine tecnico sbagliato, due ambiguità di riferimento, il gergo di Pag. Costo misurato: 1,6 minuti per mille parole, circa 2,2 ore sul resto del libro. Il PI tiene il passaggio sapendo che la ragione non è quella per cui era stato misurato. Alternativa scartata dal PI: toglierlo dalla seconda sessione di revisione, come voleva la regola fissata prima.

Deciso da: PI. Data: 2026-11-12. Stato: valida.

## D-78 Il Tattico con la maiuscola anche dove Watts scrive minuscolo

Decisione: lo schermo tattico della nave, quando è usato come nome («sul Tattico»), si scrive con la maiuscola in tutto il libro, anche dove la sorgente ha la minuscola: blocco 09, p00806 (on tactical), blocco 12, p01105 (On tactical, nella prima stesura «Sul tattico»), blocco 38, p03643 (on tactical, già «sul Tattico» nella prima stesura). Nota della voce del glossario aggiornata. L'aggettivo resta minuscolo («la grafica tattica», «sovrapposizioni tattiche»).

Motivazione: Watts scrive lo stesso schermo ora con la maiuscola ora con la minuscola, anche a poche righe di distanza (blocco 12); in italiano la stessa cosa scritta in due modi si legge come due cose. Il glossario ha già scelto la maiuscola fissa per la Banda e per il Diploma; la prima stesura era incoerente (blocco 12 minuscolo, blocco 38 maiuscolo). Rilievo di gravità media della revisione bilingue del blocco 09. Sostituisce il criterio usato nella prima stesura del blocco 12 (maiuscola solo dove la usa Watts), che il blocco 38 già non seguiva. Come per il Diploma (decisione sul Diploma, D-71), è una conseguenza di una regola già decisa, non una convenzione nuova.

Deciso da: agente. Data: 2026-11-12. Stato: valida.
