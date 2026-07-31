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
- Unità corrente: `CH-P02-NUMERICS-HARDWARE`, Capitolo 9

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
| 7 | `CH-P02-PROBABILITY` | `0.2.0-rc1` | revisione autoriale |
| 28 | `CH-P06-ATTENTION` | `0.6.0-rc6` | revisione autoriale |

## Capitolo 8. Teoria dell'informazione e funzioni obiettivo

Completato:

- testo, fonti, venticinque claim e codice;
- cross-entropy, NLL, KL divergence, entropia condizionale e mutual information;
- `SNIP-INFO-001` con sei test superati;
- specifiche, audit e alt text di `INFO-01` e `INFO-02`;
- review didattica, editoriale e linguistica.

Aperto:

- materializzazione dei due PNG candidati nel branch;
- controllo incrociato sul raster pubblicato;
- revisione autoriale e congelamento.

## Capitolo 9. Calcolo numerico, precisione e hardware

Completato:

- piano, fonti e ventinove claim;
- testo completo su floating point, range, precisione, non associatività, overflow, stabilità, dtype, mixed precision, hardware e riproducibilità;
- `SNIP-NUM-001` con output registrato;
- sette test superati;
- renderer raster per `NUM-01` e `NUM-02`;
- due iterazioni di review visuale;
- specifiche, audit e alt text;
- review fattuale, numerica, didattica, editoriale e linguistica della bozza.

Aperto:

- materializzazione dei PNG `NUM-01` e `NUM-02` nel branch;
- sostituzione dei commenti nel capitolo con i riferimenti alle immagini;
- nuova lettura integrale con le figure;
- revisione autoriale;
- promozione a release candidate e congelamento.

## Tooling visuale

Il workflow comprende generatori raster per i Capitoli 1-9 e il pilota. Le figure hanno sfondo bianco puro, controllo del contenimento e file `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`. Le candidate image-gen che ignorano la specifica o inventano lo stato del progetto vengono respinte e registrate negli audit.

## Sequenza successiva

```text
chiusura visuale Capitolo 8
-> chiusura visuale Capitolo 9
-> Capitolo 10, ricerca e pianificazione
-> prosecuzione dell'indice canonico
```

Non vengono prodotti render raster delle pagine complete. Gli artefatti sono Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit.
