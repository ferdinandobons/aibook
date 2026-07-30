# Piano operativo per la produzione completa del libro

## Stato

- Branch di produzione: `feature/full-book-production`
- Branch canonico: `main`
- Commit di partenza: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Opera pianificata: 98 capitoli e 12 appendici
- Modalità: produzione seriale controllata
- Capitolo pilota approvato e unito: `CH-P06-ATTENTION`
- Unità corrente: `CH-P01-AI-FIELD`
- Data di apertura della produzione completa: 30 luglio 2026

## Scopo

Questo branch raccoglie la stesura completa dell'opera **Intelligenza artificiale generativa**. La produzione segue senza eccezioni i documenti canonici della cartella `docs/`.

Il progetto non genera tutti i capitoli in una singola passata non revisionata. Ogni capitolo attraversa ricerca, claim, piano interno, prosa, formule, codice, visuali, audit e revisione prima che inizi il successivo. Questa regola è necessaria per mantenere verificabilità, coerenza e qualità editoriale sull'intera opera.

## Artefatti destinati al libro

Ogni capitolo integra, quando pertinenti:

1. testo Markdown in prosa tecnica naturale;
2. formule e tabelle;
3. immagini tecniche con sfondo bianco e audit iterativo;
4. snippet Python o PyTorch eseguiti e testati;
5. fonti primarie e documentazione ufficiale;
6. registro delle affermazioni;
7. audit fattuale, matematico, algoritmico, temporale, didattico, visuale e del codice.

Non vengono prodotte renderizzazioni raster delle pagine, mockup editoriali o screenshot dell'impaginazione.

## Stati ammessi

- `planned`: presente nell'indice, non aperto;
- `research`: fonti e claim in costruzione;
- `draft`: prima stesura in corso;
- `technical-review`: audit tecnico in corso;
- `didactic-review`: review didattica e gate anti-template;
- `author-review`: candidatura pronta per la revisione autoriale;
- `approved`: congelato con data e commit;
- `suspended`: lavoro fermato con problemi documentati.

## Quadro dell'opera

| Parte | Intervallo di lavoro | Capitoli | Stato iniziale |
|---|---:|---:|---|
| `P01` Campo, metodo e storia dell'AI | 1-4 | 4 | capitolo 1 in `research` |
| `P02` Matematica, informazione e calcolo | 5-9 | 5 | `planned` |
| `P03` Apprendimento, ottimizzazione e decisione | 10-14 | 5 | `planned` |
| `P04` Reti neurali e rappresentazioni | 15-19 | 5 | `planned` |
| `P05` Modellazione generativa | 20-25 | 6 | `planned` |
| `P06` Sequenze, linguaggio e contesto | 26-31 | 6 | capitolo 28 approvato; altri `planned` |
| `P07` Dati, pretraining e scaling | 32-36 | 5 | `planned` |
| `P08` Progettazione delle architetture | 37-45 | 9 | `planned` |
| `P09` Adattamento, allineamento e ragionamento | 46-54 | 9 | `planned` |
| `P10` Multimodalità e modelli del mondo | 55-62 | 8 | `planned` |
| `P11` Conoscenza esterna, memoria e azione | 63-72 | 10 | `planned` |
| `P12` Efficienza, inference e sistemi | 73-82 | 10 | `planned` |
| `P13` Valutazione, interpretabilità, sicurezza e governance | 83-93 | 11 | `planned` |
| `P14` Laboratori, integrazione e osservatorio | 94-98 | 5 | `planned` |

L'identità e l'ordine semantico dei capitoli sono definiti in `docs/10_INDICE_EDITORIALE.md`. I numeri visualizzati restano specifici dell'edizione; gli ID semantici sono stabili.

## Sequenza di produzione

L'ordine predefinito segue l'indice, salvo dipendenze tecniche documentate:

```text
CH-P01-AI-FIELD
-> CH-P01-HISTORY
-> CH-P01-LEARNING-OVERVIEW
-> CH-P01-CRITICAL-EVALUATION
-> P02 ... P14
```

Il capitolo pilota `CH-P06-ATTENTION` rimane il riferimento già approvato per tono, rigore, codice, visuali e audit, senza imporre una sagoma visibile identica agli altri capitoli.

## Gate prima di passare al capitolo successivo

Un capitolo può lasciare l'unità corrente soltanto quando:

- le affermazioni portanti sono verificate;
- le formule e i numeri sono corretti;
- il codice previsto è eseguito e testato;
- le visuali incluse sono validate tecnicamente;
- la prosa supera almeno una review didattica completa;
- ogni difetto bloccante trovato è corretto e seguito da una nuova review integrale;
- il gate anti-template è superato;
- testo, formule, immagini e codice sono coerenti;
- la candidatura è disponibile per la revisione autoriale oppure il capitolo è formalmente sospeso.

## Unità corrente

### `CH-P01-AI-FIELD`. Che cos'è l'intelligenza artificiale

Stato: `research`.

Perimetro:

- AI, machine learning, deep learning e AI generativa;
- sistemi simbolici, statistici e neurali;
- modelli discriminativi e generativi;
- foundation model, modelli generalisti e specialistici;
- training, inference, parametri e dati.

Output previsti:

- capitolo completo in prosa;
- dossier delle fonti e registro dei claim;
- almeno una visuale tassonomica e una visuale training/inference;
- uno snippet PyTorch minimo che separa aggiornamento dei parametri e inferenza;
- test, output e audit.

## Aggiornamento del piano

Dopo ogni capitolo si aggiornano:

- questo file;
- `PROGRESS.md`;
- lo stato del capitolo;
- le date di verifica;
- il commit o la pull request di revisione;
- eventuali cambiamenti del catalogo e dell'indice.
