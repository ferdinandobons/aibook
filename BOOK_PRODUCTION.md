# Piano operativo per la produzione completa del libro

## Stato

- Branch di produzione: `feature/full-book-production`
- Branch canonico: `main`
- Pull request di produzione: `#2`
- Commit di partenza: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Opera pianificata: 98 capitoli e 12 appendici
- Modalità: produzione seriale controllata
- Capitolo pilota in `main`: `CH-P06-ATTENTION`, versione `0.3.0-rc3`
- Revisione editoriale del pilota nel branch: `0.4.0-rc4`
- Unità corrente: `CH-P01-AI-FIELD`, versione `0.2.0-rc1`
- Stato dell'unità corrente: review editoriale superata, visuali bloccate
- Data di apertura della produzione completa: 30 luglio 2026

## Scopo

Questo branch raccoglie la stesura completa dell'opera **Intelligenza artificiale generativa**. La produzione segue i documenti canonici della cartella `docs/`.

Il progetto non accumula capitoli non revisionati. Ogni unità attraversa ricerca, claim, piano, prosa, codice, visuali e review prima che inizi la successiva.

## Artefatti destinati al libro

Ogni capitolo integra, quando pertinenti:

1. testo Markdown in prosa tecnica naturale;
2. formule e tabelle;
3. immagini tecniche con sfondo bianco e audit iterativo;
4. snippet Python o PyTorch eseguiti e testati;
5. fonti primarie e documentazione ufficiale;
6. registro delle affermazioni;
7. audit fattuale, matematico, algoritmico, temporale, didattico, editoriale, visuale e del codice.

Non vengono prodotte renderizzazioni raster delle pagine, mockup editoriali o screenshot dell'impaginazione.

Metadati, audit, branch, commit e dettagli operativi restano fuori dal testo destinato al lettore.

## Stati ammessi

- `planned`: presente nell'indice, non aperto;
- `research`: fonti e claim in costruzione;
- `draft`: prima stesura;
- `technical-review`: audit tecnico;
- `didactic-review`: sequenza e gate;
- `editorial-review`: voce, ritmo e italiano;
- `author-review`: candidatura pronta per l'autore;
- `approved`: congelato con data e commit;
- `suspended`: lavoro fermato con problemi documentati.

## Quadro dell'opera

| Parte | Intervallo | Capitoli | Stato corrente |
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

L'identità e l'ordine semantico sono definiti in `docs/10_INDICE_EDITORIALE.md`.

## Voce editoriale

Ogni capitolo deve leggersi come un manuale, non come una specifica o un audit.

Regole:

- scaffold interno in `PLAN.md` e `TEXT_AUDIT.md`;
- prosa continua in `CHAPTER.md`;
- titoli semantici;
- sezioni abbastanza ampie;
- italiano idiomatico;
- ritmo variato;
- esempio continuo;
- metadati nascosti;
- dettagli di riproducibilità negli artefatti;
- lettura ad alta voce.

Riferimento: `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

## Sequenza di produzione

```text
ricerca
-> claim
-> piano interno
-> prima stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit
-> audit fattuale e matematico
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> lettura ad alta voce
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

## Gate prima del capitolo successivo

Un capitolo può lasciare l'unità corrente quando:

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

Stato: review editoriale superata, gate visuale bloccato.

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
- stato e versione del capitolo;
- date di verifica;
- commit o pull request;
- eventuali cambiamenti del catalogo e dell'indice.
