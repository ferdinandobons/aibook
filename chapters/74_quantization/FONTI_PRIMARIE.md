# Fonti primarie e autorevoli. Capitolo 74

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 74 -> tema `quantization`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-74-001

- Titolo o riferimento: Frantar et al., GPTQ.
- Autori o organizzazione: Frantar et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2210.17323
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Una mappa affine converte valori floating point in interi. GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e outlier delle attivazioni.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-002

- Titolo o riferimento: Xiao et al., SmoothQuant.
- Autori o organizzazione: Xiao et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2211.10438
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models; 3 Review of Quantization Difficulty; Migrate the quantization difficulty from activations to weights..
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Post-training quantization usa calibration senza riaddestrare completamente.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-003

- Titolo o riferimento: Lin et al., AWQ.
- Autori o organizzazione: Lin et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2306.00978
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2 AWQ: Activation-aware Weight Quantization; 2.1 Improving LLM Quantization by Preserving 1% Salient Weights; 2.2 Protecting Salient Weights by Activation-aware Scaling.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-004

- Titolo o riferimento: Dettmers et al., QLoRA.
- Autori o organizzazione: Dettmers et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2305.14314
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; QLoRA : Efficient Finetuning of Quantized LLMs; Low-rank Adapters; Memory Requirement of Parameter-Efficient Finetuning.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
