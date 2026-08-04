# Testo alternativo

INFERENCE-01, Serving disaggregato e inference distribuita. Come si passa da «Tensor e pipeline parallelism» a «Prefill-decode disaggregation» mantenendo osservabile una richiesta distribuita tra compute e comunicazioni? La composizione sharding topology collega «Tensor e pipeline parallelism», «Expert parallelism», «Prefill-decode disaggregation». L'input è shard, worker, rete, batch e fase prefill/decode; l'output è risposta, trasferimenti e fault osservati. Il limite esplicito è: la comunicazione fa parte della latenza end-to-end.
