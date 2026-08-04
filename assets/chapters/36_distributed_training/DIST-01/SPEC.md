# Specifica visuale DIST-01

- modello compositivo: parallel_topology
- domanda principale: Come si passa da «Data parallelism» a «Tensor e pipeline parallelism» mantenendo osservabile gradienti e stato distribuiti tra worker?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: gradienti e stato distribuiti tra worker
- input: microbatch, worker, shard e topologia
- output: gradiente ridotto, stato sincronizzato e fault osservato
- nodi locali: Data parallelism: Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono…; ZeRO e FSDP: Parametri, gradienti e optimizer state vengono shardati tra worker.; Tensor e pipeline parallelism: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- limite visualizzato: la riduzione e il conteggio del batch devono essere dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
