# Intelligenza artificiale generativa

Repository sorgente di un manuale tecnico in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

## Stato

- Opera unica e continua.
- 14 parti stabili.
- 98 capitoli materializzati e revisionati come candidature tecniche.
- 12 appendici.
- Branch canonico: `main`.
- Stato corrente: revisione editoriale, autoriale e fattuale ancora aperta.
- Verifica locale: `616` test superati in `166` file di test e `311/311` file Python compilati in memoria.
- Dossier fonti: `419` fonti uniche e `502` collegamenti fonte-claim nel report di verifica; `0` record richiedono ancora un URL o un record primario.
- Ultimo audit globale: 3 agosto 2026.

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
4. [`BOOK_PRODUCTION.md`](BOOK_PRODUCTION.md), workflow e stato della produzione;
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

Tutti i 98 capitoli hanno testo, fonti, claim, codice, test, due visuali candidate, alt text e audit dedicati. L'audit strutturale, editoriale e di allineamento semantico copre `98/98` capitoli; le immagini PNG attive sono `196` per i capitoli e `208` includendo le 12 appendici, tutte referenziate. Le composizioni coprono famiglie diverse in base al concetto, tra cui pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist. Il report `docs/source_verification_2026-08-03.json` conserva l'esito dell'accesso alle fonti e i relativi locator.

La candidatura tecnica non equivale ancora ad approvazione editoriale: restano aperte lettura ad alta voce, verifica autoriale delle figure, ricontrollo fattuale delle fonti sensibili e congelamento. Le figure conservano il nome `candidate-vN.png` finché non vengono approvate dall'autore.

## Produzione visuale

Le immagini vengono progettate secondo [`docs/03_VISUALI.md`](docs/03_VISUALI.md). I generatori raster riproducibili e il workflow sono in:

```text
scripts/generate_book_visuals.py
scripts/generate_history_visuals.py
scripts/integrate_generated_visuals.py
.github/workflows/ci.yml
```

Ogni figura usa sfondo bianco puro, testo contenuto, collegamenti non ambigui, alt text e audit dedicato.

## Accuratezza

Ogni affermazione portante deve essere collegata a una fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto. Una frase plausibile non viene accettata come fatto soltanto perché è comune nella letteratura secondaria.
