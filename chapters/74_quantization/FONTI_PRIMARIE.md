# Fonti primarie e autorevoli. Capitolo 74

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 74 -> tema `quantization`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-74-001

- Titolo o riferimento: Jacob et al., Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.
- Autori o organizzazione: Benoit Jacob et al.
- Tipo: paper peer-reviewed.
- Data: 2018.
- Versione, revisione o commit: CVPR 2018, pagina e PDF negli atti ufficiali consultati il 4 agosto 2026.
- URL o identificatore: https://openaccess.thecvf.com/content_cvpr_2018/html/Jacob_Quantization_and_Training_CVPR_2018_paper.html
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract, paper e sezione sulla training quantization controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: integer-only inference; affine quantization; training quantization; fake-quantization operations; weights and activations.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: una mappa affine collega valori reali e interi tramite scale e zero-point; la quantization-aware training inserisce operazioni che simulano la quantizzazione durante il training.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-002

- Titolo o riferimento: Xiao et al., SmoothQuant.
- Autori o organizzazione: Xiao et al..
- Tipo: paper o report tecnico.
- Data: 2022.
- Versione, revisione o commit: arXiv 2211.10438, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2211.10438
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models; 3 Review of Quantization Difficulty; Migrate the quantization difficulty from activations to weights..
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: SmoothQuant è una soluzione post-training training-free per W8A8 che usa statistiche di attivazione e migra parte della difficoltà di quantizzazione dalle attivazioni ai pesi.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-003

- Titolo o riferimento: Lin et al., AWQ.
- Autori o organizzazione: Lin et al..
- Tipo: paper o report tecnico.
- Data: 2023.
- Versione, revisione o commit: arXiv 2306.00978, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2306.00978
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2 AWQ: Activation-aware Weight Quantization; 2.1 Improving LLM Quantization by Preserving 1% Salient Weights; 2.2 Protecting Salient Weights by Activation-aware Scaling.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: AWQ è un metodo post-training weight-only che usa statistiche delle attivazioni per identificare e proteggere canali salienti; non usa backpropagation o ricostruzione.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-74-004

- Titolo o riferimento: Frantar et al., GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers.
- Autori o organizzazione: Elias Frantar et al.
- Tipo: paper o report tecnico.
- Data: 2022.
- Versione, revisione o commit: arXiv 2210.17323, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2210.17323
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: abstract; post-training weight quantization; procedura GPTQ.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: GPTQ è un metodo post-training per quantizzare i pesi dei modelli generativi preaddestrati; il suo contratto non coincide con AWQ o SmoothQuant.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
