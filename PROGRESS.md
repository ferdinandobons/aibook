# Avanzamento del libro

## Stato corrente

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di produzione: `feature/full-book-production`
- Pull request: `#2`, draft
- Opera pianificata: 98 capitoli e 12 appendici
- Produzione: candidature seriali con congelamento dopo revisione autoriale
- Ultima ricerca globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 31 luglio 2026
- Unità corrente: `CH-P03-SUPERVISED`, Capitolo 12, stato `research`

## Documentazione canonica

- `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- `docs/01_INDICE_EDITORIALE.md`;
- `docs/02_STILE_E_QA_TESTO.md`;
- `docs/03_VISUALI.md`;
- `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- `docs/05_WORKFLOW_E_REPOSITORY.md`;
- `docs/14_CATALOGO_STATO_ARTE.md`;
- `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`.

## Gate attivi

Ogni capitolo attraversa ricerca, claim, stesura, codice, visuali, audit tecnico, review didattica, gate anti-template, review editoriale e linguistica, verifica per lettore non esperto, controllo incrociato e revisione autoriale. `final.png` e congelamento richiedono approvazione.

## Candidature complete in revisione autoriale

| Capitolo | chapter_id | Versione |
|---:|---|---|
| 1 | `CH-P01-AI-FIELD` | `0.4.0-rc3` |
| 2 | `CH-P01-HISTORY` | `0.2.0-rc1` |
| 3 | `CH-P01-LIFECYCLE` | `0.2.0-rc1` |
| 4 | `CH-P01-CRITICAL-EVALUATION` | `0.2.0-rc1` |
| 5 | `CH-P02-LINEAR-ALGEBRA` | `0.2.0-rc1` |
| 6 | `CH-P02-CALCULUS-BACKPROP` | `0.2.0-rc1` |
| 7 | `CH-P02-PROBABILITY` | `0.2.0-rc1` |
| 28 | `CH-P06-ATTENTION` | `0.6.0-rc6` |

## Candidature con testo e codice completi, visuali da materializzare

### Capitolo 8. Teoria dell'informazione e funzioni obiettivo

- testo, fonti, claim e codice completi;
- sette test superati;
- `INFO-01` e `INFO-02` validate localmente;
- generatori, specifiche, audit e alt text presenti;
- PNG ancora assenti dal branch.

### Capitolo 9. Calcolo numerico, precisione e hardware

- testo, fonti, ventinove claim e codice completi;
- sette test superati;
- `NUM-01` e `NUM-02` revisionate in più iterazioni;
- generatori, specifiche, audit e alt text presenti;
- PNG ancora assenti dal branch.

### Capitolo 10. Ricerca, pianificazione e giochi

- testo, fonti, ventitré claim e codice completi;
- sei test rieseguiti in un processo pulito;
- `SEARCH-01` revisionata instradando i collegamenti lunghi fuori dai nodi;
- `SEARCH-02` revisionata mantenendo leggibile la foglia potata;
- `REVIEW.md`, `CHANGELOG.md` e audit completi;
- PNG ancora assenti dal branch.

### Capitolo 11. Conoscenza, logica e modelli probabilistici

- testo completo su logica, Horn clauses, RDF, OWL, reti bayesiane, Markov network e factor graph;
- quindici fonti e trentuno claim;
- `SNIP-KNOW-001` con forward chaining e rete bayesiana;
- sette test superati;
- `KNOW-01` corretta dopo un problema di overflow;
- `KNOW-02` corretta dopo una relazione grafica ambigua tra prior e variabili;
- generatori, specifiche, audit, alt text e review presenti;
- PNG ancora assenti dal branch.

## Unità corrente. Capitolo 12

```text
CH-P03-SUPERVISED
Apprendimento supervisionato
```

Il piano interno è aperto. I prossimi artefatti sono fonti, claim, testo, snippet, test e visuali.

## Tooling visuale

Il workflow comprende generatori raster per i Capitoli 1-11 e il pilota. Le figure usano sfondo bianco puro, controlli di contenimento e file `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`.

Le candidate image-gen che ignorano la specifica o inventano lo stato del progetto vengono respinte. I generatori raster costituiscono la procedura di fallback per formule, grafi e collegamenti che richiedono precisione deterministica.

I commit prodotti tramite il connettore non hanno avviato il workflow durante le ultime sessioni. Per questo i PNG dei Capitoli 8-11 restano da materializzare, benché script e audit siano presenti.

## Sequenza successiva

```text
Capitolo 12
-> Capitolo 13
-> Capitolo 14
-> Parte P04
-> prosecuzione seriale dell'indice canonico
```

Non vengono prodotti render raster delle pagine complete. Gli artefatti sono Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit.
