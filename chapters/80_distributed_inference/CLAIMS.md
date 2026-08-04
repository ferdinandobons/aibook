# Registro dei claim. Capitolo 80

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `distributed_inference` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-80-01

- Affermazione esatta: Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset (claim collegato alla sezione «Tensor e pipeline parallelism» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-80-02

- Affermazione esatta: MoE distribuisce esperti e usa all-to-all durante l'inference.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ZeRO: Memory Optimizations Toward Training Trillion Parameter Models; 2.1 Data, Model and Pipeline Parallelism; 3.1 Model States: Optimizer States, Gradients and Parameters (claim collegato alla sezione «Expert parallelism» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-80-03

- Affermazione esatta: Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving; 2.2 LLM Serving Optimization; 6.3 Latency Breakdown (claim collegato alla sezione «Prefill-decode disaggregation» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-80-04

- Affermazione esatta: Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Inference Overview and Features (claim collegato alla sezione «Routing» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-80-05

- Affermazione esatta: Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset (claim collegato alla sezione «Fault tolerance» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-80-CODE

- Affermazione esatta: lo snippet snip_80_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_80_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
