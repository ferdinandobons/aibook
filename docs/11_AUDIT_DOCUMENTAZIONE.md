# Audit di completezza e coerenza della documentazione

## Stato

- Data dell'audit: **30 luglio 2026**
- Repository: `ferdinandobons/aibook`
- Branch verificato: `review/chapter-28-pilot`
- Esito: **approvato per l'uso dell'architettura evolutiva e dello standard visivo canonico**

## Scopo

Verificare che le decisioni concordate siano presenti nel repository e che una persona o un sistema AI senza contesto precedente possa:

- comprendere lo scopo del libro;
- leggere la documentazione nell'ordine corretto;
- aggiungere una nuova tecnica;
- aggiornare un capitolo;
- cambiare la maturità di una voce;
- creare, dividere o unire capitoli;
- eseguire una ricerca approfondita;
- creare immagini con una grammatica visiva comune;
- mantenere coerenti testo, immagini, codice, fonti e audit.

## Entry point e root

- [x] `../GUIDELINE.md` presente come entry point operativo.
- [x] `../README.md` rinvia a `GUIDELINE.md`.
- [x] `../README.md` descrive scopo, parti, maturità e ricerca globale.
- [x] `../PROGRESS.md` resta il registro sintetico dello stato.

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
- [x] `EXPLANATION_STYLE_AND_VISUALS.md`.
- [x] archivio `source/`.

## Architettura dell'opera

- [x] La divisione canonica in due volumi è stata sostituita.
- [x] Il repository contiene una sola opera continua.
- [x] Volume unico, tomi, sito e corso sono definiti come export.
- [x] Le parti `P01`-`P14` hanno ID, nomi e ordine stabili.
- [x] Le parti non dipendono da modelli, prodotti o periodi temporali.
- [x] La modifica delle parti richiede ricerca, migrazione e approvazione esplicita.
- [x] L'indice dell'edizione di lavoro usa 98 capitoli pianificati.
- [x] Il Capitolo 28 mantiene il ruolo di pilota.

## Routing e identità

- [x] La collocazione dipende dal problema risolto e dall'oggetto modificato.
- [x] Ogni tecnica ha una collocazione primaria.
- [x] I collegamenti secondari usano tag e cross-reference.
- [x] `chapter_id` è distinto dal numero visualizzato.
- [x] `order_key`, prerequisiti, successori e alias sono definiti.
- [x] Split e merge richiedono mappa di migrazione.

## Maturità

- [x] `CORE`, `ESTABLISHED` e `FRONTIER` sono definiti.
- [x] La maturità è separata dalla collocazione.
- [x] La promozione richiede nuove prove.
- [x] Una promozione non sposta automaticamente la voce.
- [x] Le voci frontier restano nella parte funzionale pertinente.
- [x] `P14` non è un contenitore generico per tutte le novità.

## Catalogo e ricerca

- [x] `14_CATALOGO_STATO_ARTE.md` registra le principali famiglie censite.
- [x] Ogni voce ha ID, parte, maturità, destinazione e data.
- [x] Il catalogo non dichiara completezza assoluta.
- [x] `15_REGISTRO_RICERCHE_APPROFONDITE.md` registra la ricerca del 30 luglio 2026.
- [x] Copertura, criteri, fonti seme, esiti e limiti sono dichiarati.
- [x] È prevista una revisione frontier almeno ogni 90 giorni durante la produzione attiva.
- [x] È prevista una nuova ricerca globale prima di ogni edizione.

## Aggiornamenti futuri

- [x] Il protocollo U1-U8 è definito.
- [x] Esiste una procedura per nuove tecniche.
- [x] Esiste una procedura per nuova evidenza.
- [x] Esiste una procedura per API e implementazioni.
- [x] Esiste una procedura per promozione e demozione.
- [x] Esiste una procedura per nuovi capitoli.
- [x] Esiste una procedura per split e merge.
- [x] Esiste una procedura per correzioni tecniche.
- [x] Esiste una procedura per nuove edizioni.

## Accuratezza

- [x] Fonti primarie e ufficiali hanno priorità.
- [x] Le inferenze fattuali editoriali sono escluse.
- [x] `CLAIMS.md` è obbligatorio.
- [x] La review frase per frase è obbligatoria.
- [x] L'audit matematico è obbligatorio.
- [x] L'audit architetturale e temporale è obbligatorio.
- [x] Paper, implementazione, checkpoint e prodotto restano distinti.
- [x] Risultati quantitativi richiedono setup e provenienza.

## Visuali

### Produzione e review

- [x] Le immagini vengono create con lo strumento immagini.
- [x] Gli SVG non sono l'artefatto editoriale principale.
- [x] La prima generazione è sempre una bozza.
- [x] Formula, numeri, shape e collegamenti vengono verificati.
- [x] Una linea ambigua blocca l'approvazione.
- [x] Ogni correzione richiede un nuovo audit completo.
- [x] Alt text ed equivalente testuale sono obbligatori.

### Stile canonico

- [x] `17_STANDARD_VISIVO_CANONICO.md` definisce la grammatica comune.
- [x] Lo sfondo globale è sempre bianco puro `#FFFFFF`.
- [x] Gradienti, texture e carta simulata sono esclusi.
- [x] L'orientamento può essere orizzontale o verticale in funzione del contenuto.
- [x] L'orientamento deve ridurre incroci, densità e rischio di overflow.
- [x] Famiglie visuali, palette, box, frecce e gerarchia tipografica sono definite.
- [x] Una figura tecnica non è una renderizzazione completa della pagina del libro.
- [x] Il colore non è l'unico portatore di significato.
- [x] Watermark, firme e branding di terzi sono esclusi.

### Contenimento

- [x] `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` è vincolante.
- [x] Testo fuori box, tagliato o sovrapposto è un difetto bloccante.
- [x] Padding interno e zona di sicurezza sono obbligatori.
- [x] Il controllo viene svolto sul raster reale e alla dimensione editoriale.
- [x] L'orientamento alternativo viene valutato quando il contenuto non entra correttamente.

## Codice

- [x] Ogni capitolo tecnico include codice eseguibile, salvo eccezione motivata.
- [x] Python e PyTorch sono predefiniti.
- [x] NumPy è ammesso per controlli indipendenti.
- [x] Pseudocodice e codice eseguibile restano distinti.
- [x] Le API vengono verificate sulla documentazione ufficiale.
- [x] Il codice viene eseguito in un processo pulito.
- [x] Gli invarianti vengono testati.
- [x] Gli output `Eseguito` hanno log o test associati.

## Metodo didattico

- [x] Oggetto continuo.
- [x] Catena dei sette punti.
- [x] Stati del lettore.
- [x] Blocco atomico di spiegazione.
- [x] Gate del termine, dell'astrazione, delle frecce, della matematica, del codice e delle varianti.
- [x] Niente metafore o personificazioni.
- [x] Italiano calmo, preciso e progressivo.
- [x] Una trasformazione principale per paragrafo.
- [x] Ricostruzione, localizzazione, confine, trasferimento e variazione.

## Decisioni sostituite controllate

- [x] SVG come strumento principale sostituito.
- [x] Dipendenza da `LEARN_GOVERNANCE.md` sostituita.
- [x] Inferenze fattuali etichettate sostituite dall'esclusione.
- [x] Due volumi come struttura canonica sostituiti dall'opera unica.

## Controllo incrociato

- [x] Il contratto rinvia all'architettura evolutiva.
- [x] Il registro delle decisioni contiene le decisioni architetturali.
- [x] L'indice usa le quattordici parti stabili.
- [x] La struttura del repository include `GUIDELINE.md` e i documenti evolutivi.
- [x] Il protocollo di aggiornamento rinvia al catalogo e al registro delle ricerche.
- [x] Il README root e il README docs indicano lo stesso ordine di lettura.
- [x] Il template visuale applica lo standard canonico.
- [x] Il protocollo QA visuale verifica sfondo, orientamento, palette e contenimento.
- [x] Non risultano conflitti noti tra opera unica, parti, maturità, numerazione e stile visuale.

## Elementi operativi non bloccanti

- Le versioni esatte di Python e PyTorch vengono fissate all'apertura del capitolo relativo.
- Ogni voce del catalogo viene riaperta con fonti puntuali quando entra in un capitolo.
- La numerazione visualizzata resta modificabile fino al congelamento dell'edizione.
- La sequenza illustrativa del capitolo attention viene scelta nel piano del capitolo.
- Le proporzioni esatte di ogni canvas vengono decise nello storyboard della figura.

Questi elementi appartengono al workflow e non rappresentano decisioni globali mancanti.

## Verdetto

La documentazione è sufficiente per trasferire il contesto operativo a un sistema AI privo della conversazione originaria.

L'architettura è stabile rispetto all'inserimento di nuove tecniche. Catalogo, maturità, ID semantici, routing e procedure di aggiornamento permettono l'evoluzione del libro senza modificare automaticamente i nomi o l'ordine delle parti.

Lo standard visivo è ora esplicito e adattabile. Le figure possono cambiare orientamento e composizione in base al contenuto, ma conservano sfondo bianco, palette semantica, tipografia, box, frecce, contenimento e processo di review comuni.
