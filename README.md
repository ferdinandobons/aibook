# Intelligenza artificiale generativa

Repository sorgente di un manuale tecnico in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

## Stato

- Opera unica e continua.
- 14 parti stabili.
- 98 capitoli materializzati e revisionati come candidature tecniche.
- 12 appendici.
- Branch canonico: `main`.
- Stato corrente: revisione editoriale, autoriale e fattuale ancora aperta.
- Verifica locale: `464` test superati in `115` file di test e `267/267` file Python analizzati sintatticamente.
- Dossier fonti: `419` fonti uniche e `502` collegamenti fonte-claim nel report di verifica; `0` record richiedono ancora un URL o un record primario.
- Ultimo audit globale: 4 agosto 2026.

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

Tutti i 98 capitoli hanno testo, fonti, claim, visuali, alt text e audit dedicati. `94/98` includono codice eseguibile e test; i capitoli 20, 30, 93 e 98 registrano invece un'eccezione motivata, perché uno script giocattolo renderebbe fuorviante la prova concettuale, normativa o di frontiera. L'audit strutturale, editoriale e di allineamento semantico copre `98/98` capitoli. Le immagini PNG attive sono `196` per i capitoli e `208` includendo le appendici. Le 84 coppie revisionate usano 165 modelli semantici ricondotti a dieci primitive grafiche, senza grafici quantitativi inventati. Il report `docs/source_verification_2026-08-03.json` conserva l'ultima passata globale delle fonti; il 4 agosto sono state ricontrollate in modo mirato le fonti sensibili corrette nei capitoli 20, 68, 74 e 93.

La candidatura tecnica non equivale ancora ad approvazione editoriale: restano aperte lettura ad alta voce, verifica autoriale delle figure, ricontrollo fattuale delle fonti sensibili e congelamento. Le figure conservano il nome `candidate-vN.png` finché non vengono approvate dall'autore.

## Produzione visuale

Le immagini vengono progettate secondo [`docs/03_VISUALI.md`](docs/03_VISUALI.md). I generatori raster riproducibili e il workflow sono in:

```text
scripts/generate_book_visuals.py
scripts/generate_history_visuals.py
scripts/integrate_generated_visuals.py
scripts/rebuild_lessons_v2.py
scripts/generate_visuals_v2.py
scripts/build_visual_contact_sheets.py
.github/workflows/ci.yml
```

`rebuild_lessons_v2.py` è il compiler editoriale corrente per i capitoli 14-98, escluso il pilota 28. `generate_visuals_v2.py` deve essere eseguito dopo la ricostruzione testuale, perché riapre specifiche e audit delle figure. Gli altri generatori restano come strumenti storici o dedicati ai primi capitoli. Ogni figura usa sfondo bianco puro, testo contenuto, collegamenti non ambigui, alt text e audit dedicato.

## Accuratezza

Ogni affermazione portante deve essere collegata a una fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto. Una frase plausibile non viene accettata come fatto soltanto perché è comune nella letteratura secondaria.
