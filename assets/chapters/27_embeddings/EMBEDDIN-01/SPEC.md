# Specifica visuale EMBEDDIN-01

- modello compositivo: embedding_geometry
- domanda principale: Come si passa da «Da ID a vettore» a «Embedding contestuale» mantenendo osservabile un ID e il vettore che lo rappresenta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un ID e il vettore che lo rappresenta
- input: due ID, due vettori e una query
- output: embedding, ranking o predizione
- nodi locali: Da ID a vettore: Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta…; Word embedding: Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità…; Embedding contestuale: In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa…
- limite visualizzato: la similarità dipende da training, metrica e normalizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
