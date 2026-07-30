# Avanzamento del libro

## Stato corrente

- Repository operativo: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di review: `review/chapter-28-pilot`
- Pull request: `#1`
- Modalità: produzione seriale controllata
- Capitolo pilota: `CH-P06-ATTENTION`, numero di lavoro 28
- Versione candidata: `0.1.0-rc1`
- Stato: **revisione autoriale aperta**
- Ultima ricerca approfondita globale: 30 luglio 2026
- Ultima verifica delle fonti del capitolo: 30 luglio 2026

## Pacchetto disponibile

Il branch di review contiene:

- capitolo Markdown completo;
- fonti primarie e documentazione ufficiale;
- registro delle affermazioni;
- audit fattuale, matematico, algoritmico e didattico;
- quattro snippet Python/PyTorch;
- quattro test superati;
- ambiente e output registrati;
- due immagini tecniche candidate con specifiche, alt text e audit;
- renderer raster riproducibile per le visuali;
- checklist per la revisione dell'autore.

Non contiene render delle pagine, mockup editoriali o screenshot di impaginazioni.

## Stato delle visuali

- `ATT-01/candidate-v2.png`: `validata tecnicamente`; approvazione autoriale aperta.
- `ATT-02/candidate-v2.png`: `validata tecnicamente`; approvazione autoriale aperta.
- Le versioni `candidate-v1.png` sono state rimosse perché corrotte e non revisionabili.
- Nessuna immagine è denominata `final.png` prima dell'approvazione.

## Regola aggiunta

Il contenimento del testo è ora un gate obbligatorio. Una visuale viene respinta quando un testo:

- oltrepassa o tocca il bordo del proprio contenitore;
- viene tagliato;
- invade un box o una cella adiacente;
- si sovrappone a frecce, linee o altro testo;
- non conserva un padding interno leggibile.

Riferimenti:

- `docs/02_TEMPLATE_VISUALE.md`;
- `docs/03_PROTOCOLLO_QA_VISUALE.md`;
- `docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`.

## Prossimo gate

1. review del capitolo e degli artefatti nella pull request dedicata;
2. commenti e correzioni;
3. riapertura degli audit interessati;
4. approvazione del formato pilota e delle due visuali;
5. rinomina delle figure approvate in `final.png`;
6. congelamento del capitolo e merge;
7. avvio seriale dei capitoli successivi.
