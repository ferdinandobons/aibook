# Claim

- `CL-EMBEDDIN-001`. Da ID a vettore: Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale.
- `CL-EMBEDDIN-002`. Word embedding: Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo.
- `CL-EMBEDDIN-003`. Embedding contestuale: In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi.
- `CL-EMBEDDIN-004`. Sentence embedding: Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto.
- `CL-EMBEDDIN-005`. Ricerca e anisotropia: Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking.
