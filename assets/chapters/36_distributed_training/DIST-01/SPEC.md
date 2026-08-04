# Specifica visuale DIST-01

- modello compositivo: parallel_topology
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Data parallelism a Tensor e pipeline parallelism nel capitolo 36?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: gradienti e stato distribuiti tra worker
- input: microbatch, worker, shard e topologia
- output: gradiente ridotto, stato sincronizzato e fault osservato
- nodi locali: Data parallelism: Repliche elaborano sotto-batch e aggregano gradienti.; ZeRO e FSDP: Parametri, gradienti e optimizer state vengono shardati tra worker.; Tensor e pipeline parallelism: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- limite visualizzato: la riduzione e il conteggio del batch devono essere dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
