# Intelligenza artificiale generativa

Repository sorgente di un manuale tecnico in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

## Stato

- Opera unica e continua.
- 14 parti stabili.
- 98 capitoli pianificati.
- 12 appendici.
- Branch canonico: `main`.
- Produzione: `feature/full-book-production`, pull request `#2`.
- Ultima ricerca approfondita globale: 30 luglio 2026.

## Artefatti

Il progetto contiene:

- capitoli Markdown scritti come manuale;
- formule e tabelle;
- immagini tecniche su sfondo bianco;
- codice eseguito e testato;
- fonti primarie e claim;
- audit tecnici, didattici, editoriali e visuali.

Non contiene render raster delle pagine complete o mockup dell'impaginazione.

## Come orientarsi

1. [`GUIDELINE.md`](GUIDELINE.md), entry point operativo;
2. [`docs/README.md`](docs/README.md), mappa della documentazione;
3. [`PROGRESS.md`](PROGRESS.md), stato corrente;
4. [`BOOK_PRODUCTION.md`](BOOK_PRODUCTION.md), piano seriale;
5. [`docs/01_INDICE_EDITORIALE.md`](docs/01_INDICE_EDITORIALE.md), indice completo.

## Documentazione canonica

- [`docs/00_GOVERNANCE_E_ARCHITETTURA.md`](docs/00_GOVERNANCE_E_ARCHITETTURA.md)
- [`docs/01_INDICE_EDITORIALE.md`](docs/01_INDICE_EDITORIALE.md)
- [`docs/02_STILE_E_QA_TESTO.md`](docs/02_STILE_E_QA_TESTO.md)
- [`docs/03_VISUALI.md`](docs/03_VISUALI.md)
- [`docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`](docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md)
- [`docs/05_WORKFLOW_E_REPOSITORY.md`](docs/05_WORKFLOW_E_REPOSITORY.md)
- [`docs/14_CATALOGO_STATO_ARTE.md`](docs/14_CATALOGO_STATO_ARTE.md)
- [`docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`](docs/15_REGISTRO_RICERCHE_APPROFONDITE.md)

## Stato dei capitoli

- Capitolo 1, `CH-P01-AI-FIELD`: candidatura completa `0.4.0-rc3`.
- Capitolo 2, `CH-P01-HISTORY`: candidatura completa `0.2.0-rc1`.
- Capitolo 3, `CH-P01-LIFECYCLE`: ricerca aperta.
- Capitolo 28, `CH-P06-ATTENTION`: candidatura completa `0.6.0-rc6`.

Le candidature complete hanno testo, fonti, codice, visuali e audit. Le figure conservano il nome `candidate-vN.png` finché non vengono approvate dall'autore.

## Produzione visuale

Le immagini vengono progettate secondo [`docs/03_VISUALI.md`](docs/03_VISUALI.md). I generatori raster riproducibili e il workflow sono in:

```text
scripts/generate_book_visuals.py
scripts/generate_history_visuals.py
scripts/integrate_generated_visuals.py
.github/workflows/generate-book-visuals.yml
```

Ogni figura usa sfondo bianco puro, testo contenuto, collegamenti non ambigui, alt text e audit dedicato.

## Accuratezza

Ogni affermazione portante deve essere collegata a una fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto. Una frase plausibile non viene accettata come fatto soltanto perché è comune nella letteratura secondaria.
