# Piano operativo per la produzione completa del libro

## Stato

- Branch di produzione: `feature/full-book-production`
- Branch canonico: `main`
- Pull request: `#2`
- Commit di partenza: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Opera pianificata: 98 capitoli e 12 appendici
- Modalità: produzione seriale controllata
- Capitolo pilota in `main`: `CH-P06-ATTENTION`, versione `0.3.0-rc3`
- Revisione editoriale del pilota nel branch: `0.4.0-rc4`
- Unità corrente: `CH-P01-AI-FIELD`, versione `0.2.0-rc1`
- Stato corrente: review editoriale superata, visuali aperte
- Data di apertura: 30 luglio 2026

## Documenti operativi

- governance: `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- indice: `docs/01_INDICE_EDITORIALE.md`;
- stile e QA del testo: `docs/02_STILE_E_QA_TESTO.md`;
- visuali: `docs/03_VISUALI.md`;
- fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- workflow e repository: `docs/05_WORKFLOW_E_REPOSITORY.md`;
- catalogo: `docs/14_CATALOGO_STATO_ARTE.md`;
- ricerca globale: `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`.

## Scopo

Questo branch raccoglie la stesura dell'opera **Intelligenza artificiale generativa**. Non accumula capitoli non revisionati. Ogni unità attraversa ricerca, claim, piano, prosa, codice, visuali e review prima che inizi la successiva.

Gli artefatti del libro sono:

- testo Markdown in prosa da manuale;
- formule e tabelle;
- immagini tecniche con sfondo bianco;
- snippet eseguiti e testati;
- fonti e claim;
- audit tecnici, didattici, editoriali e visuali.

Non vengono prodotti render raster delle pagine, mockup editoriali o screenshot dell'impaginazione.

Metadati, audit, branch, commit e dettagli operativi restano fuori dal testo destinato al lettore.

## Stati

```text
planned
research
draft
technical-review
didactic-review
editorial-review
author-review
approved
suspended
```

## Quadro dell'opera

| Parte | Intervallo | Capitoli | Stato |
|---|---:|---:|---|
| `P01` Campo, metodo e storia dell'AI | 1-4 | 4 | capitolo 1, visuali aperte; altri `planned` |
| `P02` Matematica, informazione e calcolo | 5-9 | 5 | `planned` |
| `P03` Apprendimento, ottimizzazione e decisione | 10-14 | 5 | `planned` |
| `P04` Reti neurali e rappresentazioni | 15-19 | 5 | `planned` |
| `P05` Modellazione generativa | 20-25 | 6 | `planned` |
| `P06` Sequenze, linguaggio e contesto | 26-31 | 6 | capitolo 28 approvato in `main`, review editoriale riaperta nel branch |
| `P07` Dati, pretraining e scaling | 32-36 | 5 | `planned` |
| `P08` Progettazione delle architetture | 37-45 | 9 | `planned` |
| `P09` Adattamento, allineamento e ragionamento | 46-54 | 9 | `planned` |
| `P10` Multimodalità e modelli del mondo | 55-62 | 8 | `planned` |
| `P11` Conoscenza esterna, memoria e azione | 63-72 | 10 | `planned` |
| `P12` Efficienza, inference e sistemi | 73-82 | 10 | `planned` |
| `P13` Valutazione, interpretabilità, sicurezza e governance | 83-93 | 11 | `planned` |
| `P14` Laboratori, integrazione e osservatorio | 94-98 | 5 | `planned` |

## Sequenza di produzione

```text
ricerca
-> claim
-> piano interno
-> stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit
-> audit fattuale, matematico e algoritmico
-> controllo incrociato e temporale
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> lettura ad alta voce
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

## Gate prima del capitolo successivo

Un capitolo lascia l'unità corrente quando:

- le affermazioni portanti sono verificate;
- formule e numeri sono corretti;
- il codice previsto è eseguito e testato;
- le visuali incluse sono validate;
- la review didattica è superata;
- il gate anti-template è superato;
- la review linguistica e la lettura ad alta voce sono superate;
- ogni difetto bloccante è seguito da una nuova review integrale;
- testo, formule, immagini e codice sono coerenti;
- la candidatura è disponibile per la revisione autoriale oppure il capitolo è formalmente sospeso.

## Unità corrente

### `CH-P01-AI-FIELD`. Che cos'è l'intelligenza artificiale

Versione: `0.2.0-rc1`.

Completato:

- fonti e 18 claim;
- testo riscritto come manuale;
- codice e tre test;
- review fattuale e didattica;
- gate anti-template;
- review editoriale e linguistica;
- lettura ad alta voce.

Aperto:

- `AI-01`;
- `AI-02`;
- controllo incrociato dopo le visuali;
- revisione autoriale.

## Revisione del Capitolo 28

La versione `0.4.0-rc4` nel branch:

- riduce la frammentazione;
- riunisce il calcolo numerico;
- separa metadati e manuale;
- alleggerisce i dettagli API;
- supera la review linguistica interna;
- riapre il controllo incrociato di `ATT-01` e `ATT-02`.

## Aggiornamento del piano

Dopo ogni capitolo si aggiornano:

- questo file;
- `PROGRESS.md`;
- stato e versione;
- date di verifica;
- commit o pull request;
- eventuali cambiamenti del catalogo e dell'indice.
