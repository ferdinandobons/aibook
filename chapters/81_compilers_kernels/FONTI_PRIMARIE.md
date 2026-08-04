# Fonti primarie e autorevoli. Capitolo 81

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 81 -> tema `compiler`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-81-001

- Titolo o riferimento: Tillet et al., Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations.
- Autori o organizzazione: Tillet et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2107.03374
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Evaluating Large Language Models Trained on Code; 1 Introduction; 2 Evaluation Framework.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. Tile, num warps e schedule ottimali dipendono dall'hardware.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-81-002

- Titolo o riferimento: PyTorch, torch.compile.
- Autori o organizzazione: PyTorch.
- Tipo: standard o documentazione ufficiale.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://pytorch.org/docs/stable/torch.compiler.html
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-partial; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-81-003

- Titolo o riferimento: Tian et al., XLA: Compiling Graphs of Operations.
- Autori o organizzazione: Tian et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://openxla.org/xla
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-partial; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; XLA Stay organized with collections Save and categorize content based on your preferences.; Key benefits; Documentation.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-81-004

- Titolo o riferimento: PyTorch, Performance Tuning Guide.
- Autori o organizzazione: PyTorch.
- Tipo: standard o documentazione ufficiale.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Intel OpenMP Runtime Library ( libiomp ) #.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Tracing e guard permettono specializzazione dinamica.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
