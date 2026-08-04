# Fonti primarie e autorevoli. Capitolo 80

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 80 -> tema `distributed_inference`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-80-001

- Titolo o riferimento: Shoeybi et al., Megatron-LM.
- Autori o organizzazione: Shoeybi et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1909.08053
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo. Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-80-002

- Titolo o riferimento: Rajbhandari et al., ZeRO.
- Autori o organizzazione: Rajbhandari et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1910.02054
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; ZeRO: Memory Optimizations Toward Training Trillion Parameter Models; 2.1 Data, Model and Pipeline Parallelism; 3.1 Model States: Optimizer States, Gradients and Parameters.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: MoE distribuisce esperti e usa all-to-all durante l'inference.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-80-003

- Titolo o riferimento: Kang et al., DistServe.
- Autori o organizzazione: Kang et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2401.09670
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving; 2.2 LLM Serving Optimization; 6.3 Latency Breakdown.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-80-004

- Titolo o riferimento: DeepSpeed, Inference Documentation.
- Autori o organizzazione: DeepSpeed.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://www.deepspeed.ai/inference/
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Inference Overview and Features.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Modello, adapter, lunghezza e stato della cache guidano il placement.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
