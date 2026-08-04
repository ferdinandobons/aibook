# Alt text INFERENCE-01

Diagramma INFERENCE-01 del Capitolo 80, famiglia architecture. Domanda: Il diagramma segue il passaggio: Parallelismo, disaggregazione, routing e recovery. L'input è shard, worker, rete, batch e fase prefill/decode, l'output è risposta, trasferimenti e fault osservati; il vincolo da controllare è che la comunicazione fa parte della latenza end-to-end La composizione usa i passaggi Tensor e pipeline parallelism, Expert parallelism, Prefill-decode disaggregation, Routing, Fault tolerance.
