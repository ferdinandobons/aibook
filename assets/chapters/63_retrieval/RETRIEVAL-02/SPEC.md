# Specifica visuale RETRIEVAL-02

- modello compositivo: index_layers
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Indici ANN da Reranking?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: query e documenti ordinati per rilevanza
- input: query, corpus, termini e indice
- output: ranking con score e documento recuperato
- nodi locali: Indici ANN: Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo.; Reranking: Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicat.
- limite visualizzato: rilevanza del ranking e correttezza della risposta sono misure separate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
