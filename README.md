# AI Book

Repository canonico del libro **Intelligenza artificiale generativa**.

## Da dove iniziare

Una persona o un sistema AI che non conosce il progetto deve leggere:

1. [`GUIDELINE.md`](GUIDELINE.md), entry point operativo;
2. [`docs/README.md`](docs/README.md), indice della documentazione canonica;
3. [`PROGRESS.md`](PROGRESS.md), stato corrente del lavoro.

## Obiettivo

Costruire un manuale tecnico completo in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi di produzione, alla valutazione e alla sicurezza.

Il libro è organizzato per problemi, meccanismi e contratti tecnici. I singoli modelli vengono usati come studi di caso verificati; il nome di un prodotto non determina da solo la struttura dell'opera.

## Forma dell'opera

Il repository contiene **una sola opera canonica e continua**. La stessa sorgente può essere esportata come volume unico, più tomi, sito, knowledge base o corso modulare. L'export non modifica l'identità dei contenuti.

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

ID, nomi e ordine delle parti sono stabili. Le nuove tecniche vengono inserite nella parte che possiede l'oggetto modificato.

La specifica è in [`docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`](docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md).

## Maturità dei contenuti

Ogni tecnica può essere classificata come:

- `CORE`, durevole e necessaria per numerosi sviluppi;
- `ESTABLISHED`, verificata e rilevante, ma ancora in evoluzione o non universale;
- `FRONTIER`, recente, sperimentale o con evidenza limitata.

La maturità può cambiare senza spostare la tecnica tra le parti. Il catalogo è in [`docs/14_CATALOGO_STATO_ARTE.md`](docs/14_CATALOGO_STATO_ARTE.md).

## Ultima ricerca approfondita

- Data dell'ultima ricerca globale: **30 luglio 2026**
- Registro: [`docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`](docs/15_REGISTRO_RICERCHE_APPROFONDITE.md)
- Protocollo futuro: [`docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`](docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md)

Ogni capitolo registra anche la propria data di verifica e congelamento.

## Metodo di produzione

- produzione seriale controllata, un capitolo completo alla volta;
- fonti primarie, technical report, documentazione e repository ufficiali;
- nessun fatto basato su inferenza editoriale nella versione approvata;
- registro delle affermazioni in `CLAIMS.md`;
- formule e derivazioni ricontrollate;
- snippet Python e PyTorch eseguiti e testati;
- immagini create con lo strumento immagini e sottoposte a review iterativa;
- controllo incrociato tra testo, formule, immagini e codice;
- revisione autoriale prima del congelamento.

## Stile delle lezioni

La metodologia interna registra stato, problema, input, trasformazione, output, invariante, confine e passaggio successivo. Questi elementi non vengono però ripetuti come una sequenza fissa di intestazioni nel testo destinato al lettore.

`PLAN.md` e `TEXT_AUDIT.md` conservano lo scaffold esplicito. `CHAPTER.md` usa titoli semantici e prosa tecnica naturale, adattata al profilo del contenuto.

Riferimenti:

- [`docs/EXPLANATION_STYLE_AND_VISUALS.md`](docs/EXPLANATION_STYLE_AND_VISUALS.md);
- [`docs/18_PROTOCOLLO_QA_DIDATTICO.md`](docs/18_PROTOCOLLO_QA_DIDATTICO.md);
- [`docs/19_STRUTTURA_LOGICA_IN_PROSA.md`](docs/19_STRUTTURA_LOGICA_IN_PROSA.md).

Ogni capitolo riceve almeno una review didattica completa. Quando emerge un difetto bloccante, il capitolo viene corretto e revisionato integralmente di nuovo. Il gate anti-template respinge lezioni che sembrano checklist compilate.

## Stile delle immagini tecniche

Tutte le figure seguono [`docs/17_STANDARD_VISIVO_CANONICO.md`](docs/17_STANDARD_VISIVO_CANONICO.md):

- sfondo bianco puro `#FFFFFF`;
- orientamento orizzontale o verticale in base al contenuto;
- palette, box, frecce e gerarchia tipografica comuni;
- una domanda principale per figura;
- nessun testo fuori dal proprio contenitore;
- nessun mockup della pagina completa usato come figura tecnica;
- prima generazione sempre trattata come bozza.

La regola contro overflow e clipping è in [`docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`](docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md).

## Come leggere `docs/`

Ordine consigliato:

1. `00_CONTRATTO_EDITORIALE.md`;
2. `08_REGISTRO_DECISIONI.md`;
3. `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
4. `14_CATALOGO_STATO_ARTE.md`;
5. `10_INDICE_EDITORIALE.md`;
6. `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
7. `EXPLANATION_STYLE_AND_VISUALS.md`;
8. `19_STRUTTURA_LOGICA_IN_PROSA.md`;
9. `18_PROTOCOLLO_QA_DIDATTICO.md`;
10. protocolli specialistici per testo, codice e visuali.

L'indice completo è in [`docs/README.md`](docs/README.md).

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

Ogni capitolo conserva testo, fonti, claim, audit, codice, output, ambiente e visuali.

## Stato corrente

Il capitolo pilota è **Il meccanismo di attention**, identificato come capitolo 28 nell'edizione di lavoro. Lo stato aggiornato è in [`PROGRESS.md`](PROGRESS.md).