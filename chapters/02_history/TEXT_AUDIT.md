# Audit del testo. Capitolo 2

## Stato

- Versione corrente: `0.2.0-rc1`
- Data: 30 luglio 2026
- Protocollo: `docs/02_STILE_E_QA_TESTO.md`
- Fonti e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale: **superato**
- Esito didattico: **superato dopo revisione**
- Esito editoriale e linguistico: **superato**
- Esito di chiarezza per lettore non esperto: **superato**
- Codice: **eseguito, tre test superati**
- Visuali: **validate tecnicamente**
- Controllo incrociato: **superato**
- Review autoriale: aperta

## `DID-HIST-01`. Prima lettura della stesura completa

- Versione: `0.1.0-draft1`
- Esito: **respinta per revisione**

Difetti individuati:

1. la ricerca in ampiezza usava una coda nel codice senza spiegarne il ruolo nella prosa;
2. la frase sulle support-vector network suonava poco naturale in italiano;
3. ImageNet e GPU venivano nominati senza una spiegazione sufficiente per un lettore nuovo;
4. `fine-tuning` compariva senza definizione;
5. `compute` veniva usato nel testo dove era preferibile `risorse di calcolo`;
6. lo stato editoriale non rifletteva ancora visuali e codice completati.

Correzioni:

- spiegato che la ricerca in ampiezza mantiene una coda ed esplora prima i percorsi con meno transizioni;
- riscritta la frase sulle support-vector network;
- definito ImageNet come benchmark di immagini etichettate e le GPU come unità di calcolo parallelo;
- definito il fine-tuning come ulteriore addestramento;
- sostituito `compute` con `risorse di calcolo` nel testo;
- allineati stato, versione e artefatti.

## `EDIT-HIST-02`. Seconda lettura completa

- Versione: `0.2.0-rc1`
- Profili: lettore non esperto, lettore tecnico, lettore che riprende il capitolo
- Esito: **superato**

### Lettore non esperto

- [x] stesso caso concreto usato dall'inizio alla fine;
- [x] storia presentata come cambiamento dei colli di bottiglia;
- [x] simbolo, stato, azione e goal spiegati prima del codice;
- [x] sistema esperto spiegato attraverso regole del dominio;
- [x] parametro e feature collegati al Capitolo 1;
- [x] backpropagation spiegata come aggiornamento dei pesi per ridurre l'errore;
- [x] ImageNet, GPU e fine-tuning definiti nel punto d'uso;
- [x] foundation model descritto come base riutilizzabile e non come prodotto completo;
- [x] riepilogo comprensibile senza memorizzare le date.

### Lettore tecnico

- [x] date e attribuzioni collegate a fonti primarie;
- [x] Dartmouth non presentato come unica nascita assoluta;
- [x] physical symbol system hypothesis attribuita a Newell e Simon;
- [x] MYCIN trattato come studio di caso;
- [x] paper del 1986 non presentato come unica origine della backpropagation;
- [x] AlexNet attribuito alla ricetta e al protocollo, non a una causa unica;
- [x] scaling law descritte come relazioni empiriche condizionate;
- [x] GPT-3 descritto con limiti zero-shot e few-shot del paper;
- [x] foundation model marcato come categoria proposta dagli autori.

### Lettore che riprende il capitolo

- [x] sette sezioni semantiche;
- [x] timeline `HIST-01` per localizzare le transizioni;
- [x] confronto `HIST-02` per localizzare i paradigmi;
- [x] quattro risorse finali: rappresentazione, conoscenza, calcolo e riuso;
- [x] riepilogo collegato alle tre domande del Capitolo 1.

### Controllo linguistico

- [x] italiano scritto direttamente;
- [x] periodi alternati e non uniformi;
- [x] termini inglesi mantenuti soltanto quando standard o storici;
- [x] nessun em dash;
- [x] nessuna successione di schede separate;
- [x] cautele storiche integrate senza interrompere ogni paragrafo;
- [x] lettura completa ad alta voce superata.

## Audit delle fonti

- [x] Turing 1950 verificato sulla pubblicazione di Mind;
- [x] proposta Dartmouth datata 31 agosto 1955 verificata nell'archivio e nella riproduzione AI Magazine;
- [x] Rosenblatt 1958 verificato tramite DOI e metadati della rivista;
- [x] Newell e Simon 1976 verificato tramite archivio e riferimento CACM;
- [x] MYCIN verificato nel volume degli autori;
- [x] Rumelhart, Hinton e Williams 1986 verificato su Nature;
- [x] Cortes e Vapnik 1995 verificato sulla pubblicazione originale;
- [x] LeCun et al. 1998 verificato su Proceedings of the IEEE;
- [x] Krizhevsky et al. 2012 verificato nei proceedings NeurIPS;
- [x] Vaswani et al. 2017 verificato nei proceedings NeurIPS;
- [x] BERT verificato nell'ACL Anthology;
- [x] scaling law, GPT-3 e foundation model verificati nei rispettivi paper e report originali;
- [x] nessuna fonte secondaria sostiene un claim portante.

## Audit del codice

- [x] breadth-first search implementata con coda FIFO;
- [x] percorso minimo noto di due transizioni;
- [x] goal raggiunto;
- [x] nessuno stato ripetuto;
- [x] goal irraggiungibile gestito con errore;
- [x] tre test superati;
- [x] output e ambiente registrati;
- [x] snippet dichiarato illustrativo e non attribuito a un sistema storico specifico.

## Audit visuale

### `HIST-01`

- [x] cinque pannelli paralleli;
- [x] date orientative;
- [x] nessuna freccia di progresso lineare;
- [x] rappresentazione e collo di bottiglia distinti;
- [x] testo contenuto;
- [x] sfondo bianco puro.

### `HIST-02`

- [x] input comune identico;
- [x] quattro pannelli non gerarchici;
- [x] rappresentazione, calcolo e output distinti;
- [x] foundation model separato dal sistema;
- [x] frecce non ambigue;
- [x] testo contenuto;
- [x] sfondo bianco puro.

## Controllo incrociato

- [x] timeline collocata dopo la spiegazione della periodizzazione;
- [x] confronto collocato dopo Transformer, pretraining e foundation model;
- [x] figure, prosa e claim usano gli stessi confini;
- [x] codice localizzato nella sezione su simboli e ricerca;
- [x] nessuna visuale inventa numeri o prestazioni;
- [x] rilettura completa eseguita dopo l'integrazione.

## Elementi aperti

- approvazione autoriale del testo;
- approvazione di `HIST-01/candidate-v1.png`;
- approvazione di `HIST-02/candidate-v1.png`;
- rinomina delle figure in `final.png`;
- congelamento con commit e data.

## Esito

La candidatura `0.2.0-rc1` supera i gate fattuali, didattici, anti-template, editoriali, linguistici, di accessibilità, codice e visuali. Il capitolo è pronto per la revisione autoriale.
