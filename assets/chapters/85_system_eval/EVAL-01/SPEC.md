# Specifica visuale EVAL-01

- modello compositivo: system_trace
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Contesto lungo a Multimodalità nel capitolo 85?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un sistema composto da modello, contesto, tool e interfaccia
- input: task, componenti, trace e policy
- output: score di sistema, failure e regressione
- nodi locali: Contesto lungo: Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto cap.; RAG: Retrieval recall, context precision, attribution e risposta finale compongono una pipeline.; Multimodalità: Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche.
- limite visualizzato: misurare il modello isolato non misura il comportamento del sistema
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
