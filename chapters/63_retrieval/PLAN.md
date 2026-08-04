# Piano editoriale. Capitolo 63

## Obiettivo didattico

Seguire **Information retrieval** da query, corpus, termini e indice a ranking con score e documento recuperato, osservando BM25, dense retrieval, ANN e reranking senza oltrepassare questo limite: rilevanza del ranking e correttezza della risposta sono misure separate.

## Prerequisiti reali

- Capitolo 10: Ricerca, pianificazione e giochi
- Capitolo 26: Il testo come dato
- Capitolo 27: Embedding e spazio semantico

## Percorso della lezione

1. **Documenti, query e rilevanza.** Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal bisogno informativo e dalle label disponibili. Prova: SRC-63-001.
2. **BM25.** La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza. Tokenizzazione e campi modificano il punteggio. Prova: SRC-63-002.
3. **Dense retrieval.** Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento dipende da positivi, negativi e in-batch sampling. Prova: SRC-63-003.
4. **Indici ANN.** Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall, memoria e latenza dipendono dalla struttura e dai parametri. Prova: SRC-63-004.
5. **Reranking.** Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo. Prova: SRC-63-001.

## Prove e artefatti

- riferimento minimo: `code/snip_63_contract.py`; test: `code/test_63_contract.py`; output: `code/outputs/SNIP-63-001.txt`.
- visuali candidate: RETRIEVAL-01, RETRIEVAL-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
