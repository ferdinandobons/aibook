# Specifica visuale TRACING-02

- modello compositivo: circuit_graph
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale failure o confronto separa Circuit tracing da Valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un'attivazione scomposta in feature sparse
- input: attivazione, dizionario, sparsità e ricostruzione
- output: feature, errore di ricostruzione e circuito candidato
- nodi locali: Circuit tracing: Feature e attribution graph possono collegare input, computazione e output.; Valutazione: Interpretabilità automatica, causal intervention e coverage devono essere misurate.
- limite visualizzato: interpretabilità di una feature richiede valutazione e controlli indipendenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
