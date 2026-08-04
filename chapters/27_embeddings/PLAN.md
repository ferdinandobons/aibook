# Piano editoriale. Capitolo 27

## Obiettivo didattico

Seguire **Embedding e spazio semantico** da due ID, due vettori e una query a embedding, ranking o predizione, osservando lookup, pooling, similarità e normalizzazione senza oltrepassare questo limite: la similarità dipende da training, metrica e normalizzazione.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 8: Teoria dell'informazione e funzioni obiettivo
- Capitolo 26: Il testo come dato

## Percorso della lezione

1. **Da ID a vettore.** Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale. Prova: SRC-27-001.
2. **Word embedding.** Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo. Prova: SRC-27-002.
3. **Embedding contestuale.** In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi. Prova: SRC-27-003.
4. **Sentence embedding.** Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto. Prova: SRC-27-004.
5. **Ricerca e anisotropia.** Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking. Prova: SRC-27-001.

## Prove e artefatti

- riferimento minimo: `code/snip_27_contract.py`; test: `code/test_27_contract.py`; output: `code/outputs/SNIP-27-001.txt`.
- visuali candidate: EMBEDDIN-01, EMBEDDIN-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
