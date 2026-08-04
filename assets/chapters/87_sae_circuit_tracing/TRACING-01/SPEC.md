# Specifica visuale TRACING-01

- modello compositivo: sparse_features
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Superposition a Dead e splitting features nel capitolo 87?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un'attivazione scomposta in feature sparse
- input: attivazione, dizionario, sparsità e ricostruzione
- output: feature, errore di ricostruzione e circuito candidato
- nodi locali: Superposition: Più feature possono condividere le stesse dimensioni di attivazione.; Sparse autoencoder: Loss e sparsity coefficient determinano il dizionario.; Dead e splitting features: Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità.
- limite visualizzato: interpretabilità di una feature richiede valutazione e controlli indipendenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
