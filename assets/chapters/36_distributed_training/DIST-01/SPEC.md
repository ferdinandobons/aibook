# Specifica visuale DIST-01

- famiglia: architecture
- domanda principale: Il diagramma segue il passaggio: All-reduce, sharding, pipeline e recovery. L'input è microbatch, worker, shard e topologia, l'output è gradiente ridotto, stato sincronizzato e fault osservato; il vincolo da controllare è che la riduzione e il conteggio del batch devono essere dichiarati
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, architecture, invariante o limite in chiusura
- nodi e contenuti: 1: Data parallelism; 2: ZeRO e FSDP; 3: Tensor e pipeline parallelism; 4: Topologia e fault tolerance; 5: Continued pretraining
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: la riduzione e il conteggio del batch devono essere dichiarati
- fonti collegate: SRC-36-001 ... SRC-36-004
- alt text: Diagramma DIST-01 del Capitolo 36, famiglia architecture. Domanda: Il diagramma segue il passaggio: All-reduce, sharding, pipeline e recovery. L'input è microbatch, worker, shard e topologia, l'output è gradiente ridotto, stato sincronizzato e fault osservato; il vincolo da controllare è che la riduzione e il conteggio del batch devono essere dichiarati La composizione usa i passaggi Data parallelism, ZeRO e FSDP, Tensor e pipeline parallelism, Topologia e fault tolerance, Continued pretraining.
