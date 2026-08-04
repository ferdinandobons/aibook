# Specifica visuale INFERENCE-02

- modello compositivo: network_boundary
- domanda principale: Quale controllo collega «Routing» a «Fault tolerance» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una richiesta distribuita tra compute e comunicazioni
- input: shard, worker, rete, batch e fase prefill/decode
- output: risposta, trasferimenti e fault osservati
- nodi locali: Routing: Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una…; Fault tolerance: Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello…
- limite visualizzato: la comunicazione fa parte della latenza end-to-end
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
