# AI Book

Repository canonico del libro **Intelligenza artificiale generativa**.

## Da dove iniziare

Una persona o un sistema AI che non conosce il progetto deve leggere per primo:

1. [`GUIDELINE.md`](GUIDELINE.md), entry point operativo completo;
2. [`docs/README.md`](docs/README.md), indice della documentazione canonica;
3. [`PROGRESS.md`](PROGRESS.md), stato corrente del lavoro.

`GUIDELINE.md` spiega come aggiungere una tecnica, aggiornare un capitolo, creare nuove sezioni, cambiare la maturità di un contenuto, eseguire una ricerca dello stato dell'arte e mantenere coerenti testo, immagini, codice, fonti e audit.

## Obiettivo

Costruire un manuale tecnico completo in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi di produzione, alla valutazione e alla sicurezza.

Il libro è organizzato per problemi, meccanismi e contratti tecnici. I singoli modelli vengono usati come studi di caso verificati. Il nome di un prodotto non determina da solo la struttura dell'opera.

## Forma dell'opera

Il repository contiene **una sola opera canonica e continua**. La stessa sorgente può essere esportata come:

- volume unico;
- più tomi editoriali;
- sito o knowledge base;
- corso modulare.

L'export non modifica l'ordine concettuale o l'identità dei contenuti.

## Parti stabili

| ID | Parte canonica |
|---|---|
| `P01` | Campo, metodo e storia dell'AI |
| `P02` | Matematica, informazione e calcolo |
| `P03` | Apprendimento, ottimizzazione e decisione |
| `P04` | Reti neurali e rappresentazioni |
| `P05` | Modellazione generativa |
| `P06` | Sequenze, linguaggio e contesto |
| `P07` | Dati, pretraining e scaling |
| `P08` | Progettazione delle architetture |
| `P09` | Adattamento, allineamento e ragionamento |
| `P10` | Multimodalità e modelli del mondo |
| `P11` | Conoscenza esterna, memoria e azione |
| `P12` | Efficienza, inference e sistemi |
| `P13` | Valutazione, interpretabilità, sicurezza e governance |
| `P14` | Laboratori, integrazione e osservatorio |

ID, nomi e ordine delle parti sono stabili. Le nuove tecniche vengono inserite nella parte che possiede l'oggetto modificato, senza rinominare l'opera in funzione della moda del momento.

La specifica completa è in [`docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`](docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md).

## Maturità dei contenuti

Ogni tecnica può essere classificata come:

- `CORE`, durevole e necessaria per numerosi sviluppi successivi;
- `ESTABLISHED`, verificata e rilevante, ma ancora in evoluzione o non universale;
- `FRONTIER`, recente, sperimentale o con evidenza ancora limitata.

La maturità può cambiare senza spostare la tecnica tra le parti. Il catalogo corrente è in [`docs/14_CATALOGO_STATO_ARTE.md`](docs/14_CATALOGO_STATO_ARTE.md).

## Ultima ricerca approfondita

- Data dell'ultima ricerca globale: **30 luglio 2026**
- Registro: [`docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`](docs/15_REGISTRO_RICERCHE_APPROFONDITE.md)
- Protocollo per le revisioni future: [`docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`](docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md)

La data indica il confine dell'ultima ricognizione globale. Ogni capitolo registra inoltre la propria data di verifica e la propria data di congelamento.

## Metodo di produzione

- produzione seriale controllata, un capitolo completo alla volta;
- fonti primarie, technical report, documentazione e repository ufficiali;
- nessuna affermazione fattuale basata su inferenza editoriale nella versione approvata;
- registro delle affermazioni portanti in `CLAIMS.md`;
- spiegazioni progressive conformi a `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- formule e derivazioni ricontrollate;
- snippet Python e PyTorch eseguiti e testati;
- immagini create con lo strumento immagini e sottoposte a review iterativa;
- controllo incrociato tra testo, formule, immagini e codice;
- revisione autoriale prima del congelamento del capitolo.

## Stile delle immagini tecniche

Tutte le figure tecniche seguono [`docs/17_STANDARD_VISIVO_CANONICO.md`](docs/17_STANDARD_VISIVO_CANONICO.md).

Regole essenziali:

- sfondo globale sempre bianco puro `#FFFFFF`;
- orientamento orizzontale o verticale scelto in base al contenuto;
- palette, box, frecce e gerarchia tipografica comuni;
- una domanda didattica principale per figura;
- nessun testo fuori dal proprio contenitore;
- nessuna figura tecnica sostituita da un mockup della pagina completa;
- ogni prima generazione è una bozza e viene revisionata integralmente.

La regola specifica contro overflow, clipping e padding insufficiente è in [`docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`](docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md).

## Come leggere `docs/`

Ordine consigliato:

1. `00_CONTRATTO_EDITORIALE.md`, obiettivi e vincoli globali;
2. `08_REGISTRO_DECISIONI.md`, decisioni correnti e sostituite;
3. `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`, parti, routing, maturità e identità;
4. `14_CATALOGO_STATO_ARTE.md`, tecniche censite e collocazione;
5. `10_INDICE_EDITORIALE.md`, struttura dei capitoli;
6. `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`, operazioni future;
7. `17_STANDARD_VISIVO_CANONICO.md`, grammatica delle figure tecniche;
8. i protocolli specialistici per testo, fonti, codice, visuali e workflow.

L'indice completo dei documenti è in [`docs/README.md`](docs/README.md).

## Struttura del repository

```text
/
  README.md
  GUIDELINE.md
  PROGRESS.md
  docs/
  chapters/
  assets/
  scripts/
  tests/
```

Ogni capitolo conserva testo, fonti, claim, audit, codice, output, ambiente e riferimenti alle visuali. La struttura dettagliata è in `docs/09_STRUTTURA_REPOSITORY.md`.

## Stato corrente

Il capitolo pilota è **Il meccanismo di attention**, attualmente identificato come capitolo 28 nell'edizione di lavoro. Lo stato aggiornato è registrato in [`PROGRESS.md`](PROGRESS.md).
