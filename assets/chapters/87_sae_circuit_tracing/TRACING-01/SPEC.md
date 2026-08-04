# Specifica visuale TRACING-01

- modello compositivo: sparse_features
- domanda principale: Come si passa da «Superposition» a «Dead e splitting features» mantenendo osservabile un'attivazione scomposta in feature sparse?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un'attivazione scomposta in feature sparse
- input: attivazione, dizionario, sparsità e ricostruzione
- output: feature, errore di ricostruzione e circuito candidato
- nodi locali: Superposition: Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre…; Sparse autoencoder: Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual…; Dead e splitting features: Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità.
- limite visualizzato: interpretabilità di una feature richiede valutazione e controlli indipendenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
