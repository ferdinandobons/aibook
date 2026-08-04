# Specifica visuale INFERENCE-02

- famiglia: queue
- domanda principale: Il diagramma segue il passaggio: Parallelismo, disaggregazione, routing e recovery. L'input è shard, worker, rete, batch e fase prefill/decode, l'output è risposta, trasferimenti e fault osservati; il vincolo da controllare è che la comunicazione fa parte della latenza end-to-end
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, queue, invariante o limite in chiusura
- nodi e contenuti: 1: Tensor e pipeline parallelism; 2: Expert parallelism; 3: Prefill-decode disaggregation; 4: Routing; 5: Fault tolerance
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: la comunicazione fa parte della latenza end-to-end
- fonti collegate: SRC-80-001 ... SRC-80-004
- alt text: Diagramma INFERENCE-02 del Capitolo 80, famiglia queue. Domanda: Il diagramma segue il passaggio: Parallelismo, disaggregazione, routing e recovery. L'input è shard, worker, rete, batch e fase prefill/decode, l'output è risposta, trasferimenti e fault osservati; il vincolo da controllare è che la comunicazione fa parte della latenza end-to-end La composizione usa i passaggi Tensor e pipeline parallelism, Expert parallelism, Prefill-decode disaggregation, Routing, Fault tolerance.
