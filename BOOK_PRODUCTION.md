# Piano operativo per la produzione completa del libro

## Stato

- Branch di produzione: `feature/full-book-production`
- Branch canonico: `main`
- Pull request: `#2`, draft
- Commit di partenza: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Opera pianificata: 98 capitoli e 12 appendici
- Modalità: produzione seriale controllata
- Unità corrente: `CH-P03-SUPERVISED`, Capitolo 12, stato `research`
- Data di apertura del branch: 30 luglio 2026
- Ultimo aggiornamento: 31 luglio 2026

## Documenti operativi

- governance: `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- indice: `docs/01_INDICE_EDITORIALE.md`;
- stile e QA del testo: `docs/02_STILE_E_QA_TESTO.md`;
- visuali: `docs/03_VISUALI.md`;
- fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- workflow e repository: `docs/05_WORKFLOW_E_REPOSITORY.md`;
- catalogo: `docs/14_CATALOGO_STATO_ARTE.md`;
- ricerca globale: `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`.

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
-> review per lettore non esperto
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

Una candidatura può lasciare l'unità corrente quando claim, testo, codice e visuali hanno superato i gate interni ed è disponibile per la revisione autoriale. `final.png` e congelamento richiedono approvazione.

## Quadro dell'opera

| Parte | Intervallo | Stato |
|---|---:|---|
| `P01` Campo, metodo e storia dell'AI | 1-4 | quattro candidature complete |
| `P02` Matematica, informazione e calcolo | 5-9 | Capitoli 5-7 completi; 8-9 in finalizzazione visuale |
| `P03` Apprendimento, ottimizzazione e decisione | 10-14 | Capitoli 10-11 in finalizzazione visuale; Capitolo 12 in ricerca |
| `P04` Reti neurali e rappresentazioni | 15-19 | `planned` |
| `P05` Modellazione generativa | 20-25 | `planned` |
| `P06` Sequenze, linguaggio e contesto | 26-31 | Capitolo 28 completo; altri `planned` |
| `P07` Dati, pretraining e scaling | 32-36 | `planned` |
| `P08` Progettazione delle architetture | 37-45 | `planned` |
| `P09` Adattamento, allineamento e ragionamento | 46-54 | `planned` |
| `P10` Multimodalità e modelli del mondo | 55-62 | `planned` |
| `P11` Conoscenza esterna, memoria e azione | 63-72 | `planned` |
| `P12` Efficienza, inference e sistemi | 73-82 | `planned` |
| `P13` Valutazione, interpretabilità, sicurezza e governance | 83-93 | `planned` |
| `P14` Laboratori, integrazione e osservatorio | 94-98 | `planned` |

## Candidature complete in revisione autoriale

| Capitolo | chapter_id | Versione | Visuali | Test |
|---:|---|---|---:|---:|
| 1 | `CH-P01-AI-FIELD` | `0.4.0-rc3` | 2 | 3 |
| 2 | `CH-P01-HISTORY` | `0.2.0-rc1` | 2 | 3 |
| 3 | `CH-P01-LIFECYCLE` | `0.2.0-rc1` | 2 | 4 |
| 4 | `CH-P01-CRITICAL-EVALUATION` | `0.2.0-rc1` | 2 | 4 |
| 5 | `CH-P02-LINEAR-ALGEBRA` | `0.2.0-rc1` | 2 | 4 |
| 6 | `CH-P02-CALCULUS-BACKPROP` | `0.2.0-rc1` | 2 | 5 |
| 7 | `CH-P02-PROBABILITY` | `0.2.0-rc1` | 2 | 6 |
| 28 | `CH-P06-ATTENTION` | `0.6.0-rc6` | 2 | 3 |

## Pacchetti completi salvo materializzazione dei PNG

| Capitolo | chapter_id | Test | Visuali locali |
|---:|---|---:|---:|
| 8 | `CH-P02-INFORMATION-THEORY` | 7 | 2 |
| 9 | `CH-P02-NUMERICS-HARDWARE` | 7 | 2 |
| 10 | `CH-P03-SEARCH-PLANNING` | 6 | 2 |
| 11 | `CH-P03-KNOWLEDGE-LOGIC` | 7 | 2 |

I quattro capitoli hanno testo, fonti, claim, codice, audit, review e generatori. I commit effettuati tramite il connettore non hanno avviato GitHub Actions nelle ultime sessioni, quindi i PNG generati localmente non sono ancora presenti nei rispettivi percorsi del branch.

## Unità corrente. Capitolo 12

```text
CH-P03-SUPERVISED
Apprendimento supervisionato
```

Il piano interno è aperto. La produzione prevista comprende:

- coppie input-target;
- classificazione e regressione;
- rischio empirico e generalizzazione;
- logistic regression e soglie;
- overfitting, bias, varianza e regolarizzazione;
- alberi, margini ed ensemble come famiglie alternative;
- class imbalance e analisi per slice;
- snippet PyTorch con split, baseline e test.

## Tooling visuale

Il workflow include generatori raster per i Capitoli 1-11 e il pilota. Le visuali candidate sono PNG con sfondo bianco, controllo del contenimento e artefatti `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`.

Quando image-gen ignora la specifica o inventa informazioni sul progetto, la candidata viene respinta e il difetto viene registrato. Per grafi, formule e connessioni che richiedono precisione viene usato il renderer raster deterministico, mai SVG come artefatto principale.

## Aggiornamento del piano

Dopo ogni unità si aggiornano questo file, `PROGRESS.md`, la pull request, lo stato del capitolo e gli eventuali riferimenti in indice e catalogo.
