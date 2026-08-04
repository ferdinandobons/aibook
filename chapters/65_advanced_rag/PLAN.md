# Piano editoriale. Capitolo 65

## Obiettivo didattico

Seguire **RAG adattivo, correttivo e basato su grafi** da domanda multi-hop, nodi, archi e documenti a sottoquery, percorso e contesto selezionato, osservando query transformation, routing e corrective retrieval senza oltrepassare questo limite: un router può sbagliare anche quando il generatore è corretto.

## Prerequisiti reali

- Capitolo 63: Information retrieval
- Capitolo 64: Retrieval-Augmented Generation

## Percorso della lezione

1. **Query transformation.** Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni trasformazione può migliorare recall o introdurre drift. Prova: SRC-65-001.
2. **Retrieval adattivo.** Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un componente da valutare, non un comportamento gratuito del modello. Prova: SRC-65-002.
3. **Corrective RAG.** Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e web fallback richiedono soglie e autorizzazioni. Prova: SRC-65-003.
4. **Graph RAG.** Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da estrazione, normalizzazione e aggiornamento. Prova: SRC-65-004.
5. **RAG agentico.** Un agente può pianificare retrieval successivi. Più step aumentano copertura e contemporaneamente costo, errori e superficie di attacco. Prova: SRC-65-001.

## Prove e artefatti

- riferimento minimo: `code/snip_65_contract.py`; test: `code/test_65_contract.py`; output: `code/outputs/SNIP-65-001.txt`.
- visuali candidate: RAG-01, RAG-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
