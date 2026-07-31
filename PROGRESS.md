# Avanzamento del libro

## Stato corrente

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di produzione: `feature/full-book-production`
- Pull request: `#2`, draft
- Opera pianificata: 98 capitoli e 12 appendici
- Produzione: seriale controllata
- Ultima ricerca globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 31 luglio 2026
- Unità corrente: `CH-P02-PROBABILITY`, Capitolo 7, stato `research`

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

## Candidature complete

| Capitolo | chapter_id | Versione | Stato |
|---:|---|---|---|
| 1 | `CH-P01-AI-FIELD` | `0.4.0-rc3` | revisione autoriale |
| 2 | `CH-P01-HISTORY` | `0.2.0-rc1` | revisione autoriale |
| 3 | `CH-P01-LIFECYCLE` | `0.2.0-rc1` | revisione autoriale |
| 4 | `CH-P01-CRITICAL-EVALUATION` | `0.2.0-rc1` | revisione autoriale |
| 5 | `CH-P02-LINEAR-ALGEBRA` | `0.2.0-rc1` | revisione autoriale |
| 6 | `CH-P02-CALCULUS-BACKPROP` | `0.2.0-rc1` | revisione autoriale |
| 28 | `CH-P06-ATTENTION` | `0.6.0-rc6` | revisione autoriale |

## Capitolo 6. Calcolo differenziale e backpropagation

Completato:

- testo completo su derivata, gradiente, Jacobiana, chain rule, reverse mode e backpropagation;
- fonti e venti claim;
- `SNIP-CALC-001` con derivazione manuale, autograd, differenze finite e `gradcheck`;
- cinque test superati;
- `CALC-01/candidate-v1.png`;
- `CALC-02/candidate-v2.png`;
- specifiche, audit e alt text;
- doppia review didattica, matematica, editoriale e linguistica;
- controllo incrociato dei valori.

Aperto:

- revisione autoriale;
- eventuali correzioni;
- rinomina delle figure in `final.png`;
- congelamento.

## Unità corrente. Capitolo 7

```text
CH-P02-PROBABILITY
Probabilità, statistica e inferenza
```

Obiettivo immediato:

- definire oggetto continuo e perimetro;
- verificare fonti;
- costruire claim;
- produrre testo, snippet e visuali;
- completare le review prima di passare al Capitolo 8.

## Tooling visuale

Il workflow include generatori raster per i Capitoli 1-6 e il pilota. Le figure hanno sfondo bianco puro, controlli di contenimento e file `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`. Le candidate image-gen che rappresentano un soggetto diverso dalla specifica vengono respinte.

## Sequenza successiva

```text
Capitolo 7
-> Capitolo 8
-> Capitolo 9
-> Parte P03
-> prosecuzione seriale dell'indice canonico
```

Non vengono prodotti render raster delle pagine complete. Gli artefatti sono Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit.
