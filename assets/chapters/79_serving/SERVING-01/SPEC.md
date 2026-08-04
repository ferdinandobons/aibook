# Specifica visuale SERVING-01

- modello compositivo: serving_queue
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Richieste eterogenee a Throughput e latency nel capitolo 79?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: richieste eterogenee in una coda di serving
- input: prompt, deadline, lunghezza, memoria e priorità
- output: throughput, latency p50/p99 e richieste ammesse
- nodi locali: Richieste eterogenee: Prompt e output hanno lunghezze differenti.; Continuous batching: Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse.; Throughput e latency: Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token laten.
- limite visualizzato: throughput e latenza devono essere misurati insieme
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
