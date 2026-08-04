# Specifica visuale KERNELS-01

- modello compositivo: compiler_graph
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Grafo e operatori a Triton e kernel custom nel capitolo 81?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un grafo di operatori trasformato dal compiler
- input: grafo, shape, dtype, target e kernel
- output: kernel eseguito, latenza e fallback
- nodi locali: Grafo e operatori: Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout trans.; Kernel fusion: Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressur.; Triton e kernel custom: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta ri.
- limite visualizzato: ottimizzazione del grafo e correttezza numerica devono essere confrontate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
