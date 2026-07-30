# Audit di completezza e coerenza della documentazione

## Stato

- Data dell'audit: **30 luglio 2026**
- Repository: `ferdinandobons/aibook`
- Branch verificato: `review/chapter-28-pilot`
- Esito: **approvato per l'architettura evolutiva, lo standard visivo e la struttura logica in prosa**

## Scopo

Verificare che una persona o un sistema AI senza contesto precedente possa:

- comprendere lo scopo del libro;
- leggere i documenti nell'ordine corretto;
- aggiungere o aggiornare tecniche e capitoli;
- applicare fonti, claim, codice e visuali;
- usare uno scaffold didattico rigoroso senza trasformarlo in una struttura editoriale ripetitiva;
- ripetere le review finché non restano difetti bloccanti.

## Entry point e root

- [x] `../GUIDELINE.md` è presente e aggiornato.
- [x] `../README.md` rinvia alla documentazione canonica.
- [x] `../PROGRESS.md` registra la candidatura corrente.

## Documenti canonici controllati

- [x] `README.md`.
- [x] `00_CONTRATTO_EDITORIALE.md`.
- [x] `01_TEMPLATE_CAPITOLO.md`.
- [x] `02_TEMPLATE_VISUALE.md`.
- [x] `03_PROTOCOLLO_QA_VISUALE.md`.
- [x] `04_PROTOCOLLO_QA_TESTO.md`.
- [x] `05_STANDARD_SNIPPET_CODICE.md`.
- [x] `06_WORKFLOW_CAPITOLO.md`.
- [x] `07_POLITICA_FONTI_CITAZIONI.md`.
- [x] `08_REGISTRO_DECISIONI.md`.
- [x] `09_STRUTTURA_REPOSITORY.md`.
- [x] `10_INDICE_EDITORIALE.md`.
- [x] `11_AUDIT_DOCUMENTAZIONE.md`.
- [x] `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`.
- [x] `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.
- [x] `14_CATALOGO_STATO_ARTE.md`.
- [x] `15_REGISTRO_RICERCHE_APPROFONDITE.md`.
- [x] `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`.
- [x] `17_STANDARD_VISIVO_CANONICO.md`.
- [x] `18_PROTOCOLLO_QA_DIDATTICO.md`.
- [x] `19_STRUTTURA_LOGICA_IN_PROSA.md`.
- [x] `EXPLANATION_STYLE_AND_VISUALS.md`.
- [x] archivio `source/`.

## Architettura dell'opera

- [x] Il repository contiene una sola opera continua.
- [x] Volume, tomi, sito e corso sono export.
- [x] Le parti `P01`-`P14` hanno ID, nomi e ordine stabili.
- [x] La modifica delle parti richiede governance e migrazione.
- [x] L'indice di lavoro usa ID semantici.

## Routing, maturità e identità

- [x] La collocazione dipende dal problema e dall'oggetto modificato.
- [x] Ogni tecnica ha una collocazione primaria.
- [x] `CORE`, `ESTABLISHED` e `FRONTIER` sono separati dalla collocazione.
- [x] `chapter_id` è distinto dal numero visualizzato.
- [x] Split e merge richiedono alias e mappa di migrazione.

## Accuratezza

- [x] Fonti primarie e ufficiali hanno priorità.
- [x] Le inferenze fattuali editoriali sono escluse.
- [x] `CLAIMS.md` è obbligatorio.
- [x] Audit fattuale, matematico, algoritmico e temporale sono obbligatori.
- [x] Paper, implementazione, checkpoint e prodotto restano distinti.
- [x] Risultati quantitativi richiedono setup e provenienza.

## Struttura didattica

### Scaffold interno

- [x] `PLAN.md` registra oggetto continuo, stato del lettore, transizioni, invarianti e confini.
- [x] `TEXT_AUDIT.md` registra le review e i difetti.
- [x] Il blocco atomico resta verificabile per ogni giunzione critica.
- [x] La catena dei sette punti resta obbligatoria nel significato.

### Superficie editoriale

- [x] `19_STRUTTURA_LOGICA_IN_PROSA.md` distingue scaffold e capitolo pubblicato.
- [x] `01_TEMPLATE_CAPITOLO.md` non prescrive più una sequenza rigida di intestazioni.
- [x] I titoli destinati al lettore sono semantici e dipendono dal contenuto.
- [x] Stato, trasformazione, invariante e confine vengono incorporati nella prosa.
- [x] Shape e condizioni restano esplicite anche senza titoli metacognitivi.
- [x] Il gate anti-template respinge lezioni che sembrano checklist compilate.
- [x] Capitoli di profilo diverso possono avere superfici editoriali diverse.

### Review iterativa

- [x] Ogni capitolo riceve almeno una review didattica completa.
- [x] Un difetto bloccante riapre lo stato `revisione didattica`.
- [x] Dopo una correzione viene eseguita una nuova review integrale.
- [x] Il ciclo continua finché `TEXT_AUDIT.md` non indica un esito positivo.
- [x] Una modifica strutturale successiva riapre il gate.

## Capitolo pilota

- [x] La versione `0.3.0-rc3` usa prosa continua e titoli semantici.
- [x] Il caso numerico resta l'oggetto continuo.
- [x] I termini tecnici compaiono dopo i referenti concreti.
- [x] Il pseudocodice precede la formula generale.
- [x] Il codice compare dopo il meccanismo.
- [x] Le visuali sono introdotte, attraversate e concluse nella prosa.
- [x] La multi-head attention resta differita.
- [x] `TEXT_AUDIT.md` registra quattro review, incluse una review anti-template respinta e una nuova review completa superata.

## Visuali

### Produzione e review

- [x] Le immagini vengono create con lo strumento immagini.
- [x] Gli SVG non sono l'artefatto principale.
- [x] La prima generazione è una bozza.
- [x] Formule, numeri, shape e collegamenti vengono verificati.
- [x] Ogni correzione richiede un nuovo audit.
- [x] Alt text ed equivalente testuale sono obbligatori.

### Stile canonico

- [x] Sfondo bianco puro `#FFFFFF`.
- [x] Orientamento orizzontale o verticale in base al contenuto.
- [x] Palette, box, frecce e tipografia coerenti.
- [x] Nessun render completo della pagina usato come figura tecnica.
- [x] Il colore non è l'unico portatore di significato.
- [x] Branding di terzi escluso.

### Contenimento

- [x] Overflow, clipping e sovrapposizioni sono difetti bloccanti.
- [x] Padding e zona di sicurezza sono obbligatori.
- [x] Il controllo viene svolto sul raster reale.

## Codice

- [x] Ogni capitolo tecnico include codice eseguibile, salvo eccezione motivata.
- [x] Python e PyTorch sono predefiniti.
- [x] Pseudocodice e codice eseguibile restano distinti.
- [x] Le API vengono verificate sulla documentazione ufficiale.
- [x] Il codice viene eseguito in un processo pulito.
- [x] Gli invarianti vengono testati.
- [x] Gli output `Eseguito` hanno log o test associati.
- [x] Il contratto completo resta negli artefatti del codice e viene introdotto naturalmente nella prosa.

## Decisioni registrate

- [x] `DEC-045`: contenimento del testo nelle visuali.
- [x] `DEC-046`: review didattica iterativa.
- [x] `DEC-047`: struttura logica implicita nella prosa.
- [x] L'interpretazione del blocco atomico come struttura visibile standard è marcata come sostituita.

## Controllo incrociato

- [x] `GUIDELINE.md`, `docs/README.md` e i protocolli indicano lo stesso ordine di lettura.
- [x] `EXPLANATION_STYLE_AND_VISUALS.md`, `18_PROTOCOLLO_QA_DIDATTICO.md` e `19_STRUTTURA_LOGICA_IN_PROSA.md` sono coerenti.
- [x] Il template distingue chiaramente artefatti interni e superficie pubblicata.
- [x] Il Capitolo 28 applica le regole aggiornate.
- [x] Non risultano conflitti noti tra accuratezza, didattica, immagini e codice.

## Elementi non bloccanti

- La numerazione visualizzata resta modificabile fino al congelamento dell'edizione.
- Le versioni esatte delle librerie vengono fissate nei singoli capitoli.
- Le figure candidate attendono l'approvazione autoriale prima della rinomina in `final.png`.

## Verdetto

La documentazione trasferisce il contesto operativo a un sistema AI privo della conversazione originaria.

La logica didattica resta rigorosa e revisionabile, ma non impone più lezioni visibilmente identiche. La prosa può adattarsi al contenuto conservando oggetto continuo, progressione, invarianti, confini, fonti, codice e visuali verificabili.