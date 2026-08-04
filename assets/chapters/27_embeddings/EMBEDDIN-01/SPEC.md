# Specifica visuale EMBEDDIN-01

- modello compositivo: embedding_geometry
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Da ID a vettore a Embedding contestuale nel capitolo 27?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un ID e il vettore che lo rappresenta
- input: due ID, due vettori e una query
- output: embedding, ranking o predizione
- nodi locali: Da ID a vettore: Una embedding table seleziona una riga per token.; Word embedding: Word2vec e GloVe usano statistiche distributive con obiettivi differenti.; Embedding contestuale: In un Transformer, la rappresentazione di un token cambia con il contesto.
- limite visualizzato: la similarità dipende da training, metrica e normalizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
