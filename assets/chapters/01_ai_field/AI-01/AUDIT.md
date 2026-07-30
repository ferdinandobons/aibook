# Audit visuale `AI-01`

## Stato

- Esito: **validata tecnicamente**
- Approvazione tecnica: sì
- Approvazione autoriale: no
- File candidato: `candidate-v1.png`
- Generatore: `scripts/generate_book_visuals.py`
- Data: 30 luglio 2026

## Iterazioni respinte

| Tentativo | Output prodotto | Difetto bloccante | Decisione |
|---|---|---|---|
| 1 | schermata GitHub di una pull request | contenuto completamente diverso dalla tassonomia richiesta | respinta |
| 2 | schermata repository dopo un merge | contenuto completamente diverso | respinta |
| 3 | pagina GitHub con elenco di pull request | contenuto completamente diverso | respinta |
| 4 | dashboard `libro completato` | affermazioni false sullo stato del progetto e nessuno dei tre assi | respinta |
| 5 | dashboard sull'indice del libro | oggetto sbagliato, numerazione inventata, nessuna tassonomia | respinta |
| 6 | schermata GitHub scura | oggetto sbagliato e violazione dello sfondo canonico | respinta |
| 7 | confronto lineare da automazione a foundation model | falsa gerarchia e contenuto diverso dai tre aspetti indipendenti | respinta |
| 8 | pagina doppia con `AI-01` e `AI-02` | due domande nello stesso canvas e gerarchia implicita | respinta |

## Controlli della candidata `candidate-v1.png`

### Contenuto

- [x] una sola domanda didattica;
- [x] richiesta `Il pacco non è arrivato` al centro;
- [x] tre pannelli: meccanismo, obiettivo e ampiezza;
- [x] esempi coerenti con il Capitolo 1;
- [x] nessuna gerarchia tra i pannelli;
- [x] footer coerente con l'invariante editoriale.

### Geometria e leggibilità

- [x] sfondo globale `#FFFFFF`;
- [x] orientamento orizzontale adeguato;
- [x] pannelli della stessa importanza visiva;
- [x] testo e simboli integralmente nei box;
- [x] padding sufficiente;
- [x] nessuna freccia attraversa una label;
- [x] nessun collegamento tra i tre pannelli;
- [x] ordine di lettura unico.

### Coerenza

- [x] palette canonica rispettata;
- [x] terminologia allineata a `CHAPTER.md`;
- [x] nessun elemento relativo a GitHub o allo stato del progetto;
- [x] nessun watermark o branding;
- [x] alt text verificato sulla candidata;
- [x] PNG decodificato e verificato dal generatore.

## Difetti residui

Nessun difetto tecnico bloccante noto. La denominazione `candidate-v1.png` resta fino all'approvazione autoriale.

## Decisione

La figura può essere usata nella candidatura completa del Capitolo 1. Non viene rinominata `final.png` prima della revisione autoriale.
