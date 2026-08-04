# Specifica visuale INFERENCE-01

- modello compositivo: sharding_topology
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Tensor e pipeline parallelism a Prefill-decode disaggregation nel capitolo 80?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una richiesta distribuita tra compute e comunicazioni
- input: shard, worker, rete, batch e fase prefill/decode
- output: risposta, trasferimenti e fault osservati
- nodi locali: Tensor e pipeline parallelism: Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo.; Expert parallelism: MoE distribuisce esperti e usa all-to-all durante l'inference.; Prefill-decode disaggregation: Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cac.
- limite visualizzato: la comunicazione fa parte della latenza end-to-end
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
