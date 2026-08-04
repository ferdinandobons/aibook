# Piano interno. Capitolo 80

- Domanda centrale: quale contratto costruisce Serving disaggregato e inference distribuita?
- Oggetto continuo: una richiesta distribuita tra compute e comunicazioni; input guida: shard, worker, rete, batch e fase prefill/decode.
- Prerequisito stabile: Capitolo 79, Serving, batching e scheduling.
- Gap: parallelismo, disaggregazione, routing e recovery.
- Output consegnato: risposta, trasferimenti e fault osservati; consumer successivo: Capitolo 81, Compiler, kernel e runtime.
- Invariante principale: la comunicazione fa parte della latenza end-to-end.
- Visuali: INFERENCE-01 e INFERENCE-02, con famiglie compositive variabili.
- Snippet: code/snip_80_contract.py; output: code/outputs/SNIP-80-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Tensor e pipeline parallelism

- Ultima affermazione stabile: una richiesta distribuita tra compute e comunicazioni.
- Concetto nuovo: Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo.
- Input e shape: shard, worker, rete, batch e fase prefill/decode.
- Operazione: parallelismo, disaggregazione, routing e recovery.
- Output e shape: risposta, trasferimenti e fault osservati.
- Che cosa cambia: il passaggio specifico di «Tensor e pipeline parallelism».
- Invariante: la comunicazione fa parte della latenza end-to-end.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con una sincronizzazione e un timeout; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Expert parallelism.
- Prova: SRC-80-001 e sezione pubblica corrispondente.

## Transizione 2. Expert parallelism

- Ultima affermazione stabile: una richiesta distribuita tra compute e comunicazioni.
- Concetto nuovo: MoE distribuisce esperti e usa all-to-all durante l'inference.
- Input e shape: shard, worker, rete, batch e fase prefill/decode.
- Operazione: parallelismo, disaggregazione, routing e recovery.
- Output e shape: risposta, trasferimenti e fault osservati.
- Che cosa cambia: il passaggio specifico di «Expert parallelism».
- Invariante: la comunicazione fa parte della latenza end-to-end.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con una sincronizzazione e un timeout; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prefill-decode disaggregation.
- Prova: SRC-80-002 e sezione pubblica corrispondente.

## Transizione 3. Prefill-decode disaggregation

- Ultima affermazione stabile: una richiesta distribuita tra compute e comunicazioni.
- Concetto nuovo: Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete.
- Input e shape: shard, worker, rete, batch e fase prefill/decode.
- Operazione: parallelismo, disaggregazione, routing e recovery.
- Output e shape: risposta, trasferimenti e fault osservati.
- Che cosa cambia: il passaggio specifico di «Prefill-decode disaggregation».
- Invariante: la comunicazione fa parte della latenza end-to-end.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con una sincronizzazione e un timeout; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Routing.
- Prova: SRC-80-003 e sezione pubblica corrispondente.

## Transizione 4. Routing

- Ultima affermazione stabile: una richiesta distribuita tra compute e comunicazioni.
- Concetto nuovo: Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi.
- Input e shape: shard, worker, rete, batch e fase prefill/decode.
- Operazione: parallelismo, disaggregazione, routing e recovery.
- Output e shape: risposta, trasferimenti e fault osservati.
- Che cosa cambia: il passaggio specifico di «Routing».
- Invariante: la comunicazione fa parte della latenza end-to-end.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con una sincronizzazione e un timeout; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fault tolerance.
- Prova: SRC-80-004 e sezione pubblica corrispondente.

## Transizione 5. Fault tolerance

- Ultima affermazione stabile: una richiesta distribuita tra compute e comunicazioni.
- Concetto nuovo: Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione.
- Input e shape: shard, worker, rete, batch e fase prefill/decode.
- Operazione: parallelismo, disaggregazione, routing e recovery.
- Output e shape: risposta, trasferimenti e fault osservati.
- Che cosa cambia: il passaggio specifico di «Fault tolerance».
- Invariante: la comunicazione fa parte della latenza end-to-end.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con una sincronizzazione e un timeout; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Compiler, kernel e runtime.
- Prova: SRC-80-001 e sezione pubblica corrispondente.
