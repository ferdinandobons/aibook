# Specifica visuale RETRIEVAL-02

- modello compositivo: index_layers
- domanda principale: Quale controllo collega «Indici ANN» a «Reranking» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: query e documenti ordinati per rilevanza
- input: query, corpus, termini e indice
- output: ranking con score e documento recuperato
- nodi locali: Indici ANN: Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall,…; Reranking: Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene…
- limite visualizzato: rilevanza del ranking e correttezza della risposta sono misure separate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
