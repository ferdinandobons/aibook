# Piano editoriale. Capitolo 80

## Obiettivo didattico

Seguire **Serving disaggregato e inference distribuita** da shard, worker, rete, batch e fase prefill/decode a risposta, trasferimenti e fault osservati, osservando parallelismo, disaggregazione, routing e recovery senza oltrepassare questo limite: la comunicazione fa parte della latenza end-to-end.

## Prerequisiti reali

- Capitolo 36: Training distribuito e continued pretraining
- Capitolo 79: Serving, batching e scheduling

## Percorso della lezione

1. **Tensor e pipeline parallelism.** Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo. Prova: SRC-80-001.
2. **Expert parallelism.** MoE distribuisce esperti e usa all-to-all durante l'inference. Prova: SRC-80-002.
3. **Prefill-decode disaggregation.** Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete. Prova: SRC-80-003.
4. **Routing.** Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi. Prova: SRC-80-004.
5. **Fault tolerance.** Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione. Prova: SRC-80-001.

## Prove e artefatti

- riferimento minimo: `code/snip_80_contract.py`; test: `code/test_80_contract.py`; output: `code/outputs/SNIP-80-001.txt`.
- visuali candidate: INFERENCE-01, INFERENCE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
