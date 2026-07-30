# Avanzamento del libro

## Stato corrente

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di produzione: `feature/full-book-production`
- Pull request di produzione: `#2`, draft
- Opera pianificata: 98 capitoli e 12 appendici
- Produzione: seriale controllata
- Ultima ricerca globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 30 luglio 2026
- Unità corrente: `CH-P01-LIFECYCLE`, Capitolo 3, stato `research`

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

Ogni capitolo attraversa:

1. ricerca e claim;
2. stesura e verifica tecnica;
3. codice e test, quando pertinenti;
4. visuali e audit;
5. review didattica e gate anti-template;
6. review editoriale e linguistica;
7. verifica per un lettore non esperto;
8. controllo incrociato;
9. revisione autoriale;
10. congelamento.

Un capitolo può lasciare l'unità corrente quando la candidatura completa è disponibile per la revisione autoriale. Il congelamento e la rinomina delle figure in `final.png` richiedono approvazione.

## Capitolo 1. Che cos'è l'intelligenza artificiale

- `chapter_id`: `CH-P01-AI-FIELD`
- Versione: `0.4.0-rc3`
- Stato: candidatura completa in revisione autoriale

Completato:

- testo verificato e riscritto per un lettore non esperto;
- 18 claim e fonti primarie;
- snippet PyTorch e tre test;
- `AI-01/candidate-v1.png`;
- `AI-02/candidate-v1.png`;
- audit delle visuali e controllo incrociato;
- review fattuale, didattica, editoriale, linguistica e di accessibilità.

Aperto:

- approvazione autoriale del testo e delle due figure;
- rinomina in `final.png`;
- congelamento.

## Capitolo 2. Dai simboli ai foundation model

- `chapter_id`: `CH-P01-HISTORY`
- Versione: `0.2.0-rc1`
- Stato: candidatura completa in revisione autoriale

Completato:

- quattordici fonti primarie e diciotto claim;
- testo completo con oggetto continuo;
- snippet di ricerca simbolica;
- tre test superati;
- `HIST-01/candidate-v1.png`;
- `HIST-02/candidate-v1.png`;
- audit fattuale, didattico, editoriale, linguistico, visuale e del codice;
- controllo incrociato completo.

Aperto:

- approvazione autoriale;
- rinomina delle figure in `final.png`;
- congelamento.

## Capitolo 3. Il ciclo di vita di un sistema di AI

- `chapter_id`: `CH-P01-LIFECYCLE`
- Stato: `research`

Completato:

- piano interno;
- oggetto continuo;
- visuali e snippet pianificati;
- gate specifici definiti.

Prossimi artefatti:

- `FONTI_PRIMARIE.md`;
- `CLAIMS.md`;
- prima stesura;
- snippet con split train, validation e test;
- visuali `LIFE-01` e `LIFE-02`.

## Capitolo 28. Il meccanismo di attention

- `chapter_id`: `CH-P06-ATTENTION`
- Versione nel branch: `0.6.0-rc6`
- Stato: candidatura completa in revisione autoriale

Completato:

- riscrittura per un lettore non esperto;
- `ATT-01/candidate-v3.png` con `Posizione 1/2`;
- `ATT-02/candidate-v2.png` ricontrollata;
- alt text di `ATT-01` corretto;
- tre snippet e tre test invariati;
- controllo incrociato testo, formule, visuali e codice.

Aperto:

- approvazione autoriale delle due figure e del testo;
- rinomina in `final.png`;
- nuovo congelamento prima dell'aggiornamento di `main`.

## Tooling visuale

Sono presenti:

- `scripts/generate_book_visuals.py`;
- `scripts/generate_history_visuals.py`;
- `scripts/integrate_generated_visuals.py`;
- `.github/workflows/generate-book-visuals.yml`.

Il workflow genera PNG raster su sfondo bianco, verifica che siano decodificabili e committa i candidati nel feature branch. La prima immagine resta sempre una bozza e la denominazione `final.png` è riservata agli asset approvati.

## Sequenza successiva

```text
Capitolo 3
-> Capitolo 4
-> Parte P02
-> prosecuzione seriale dell'indice canonico
```

Non vengono prodotti render raster delle pagine complete. Gli artefatti sono Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit.
