# Fonti primarie e autorevoli. Capitolo 36

- Data di consultazione: 3 agosto 2026
- Routing semantico: capitolo 36 -> tema `distributed_training`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-36-001

- Titolo o riferimento: Shoeybi et al., Megatron-LM.
- Autori o organizzazione: Shoeybi et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1909.08053
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Repliche elaborano sotto-batch e aggregano gradienti. Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-36-002

- Titolo o riferimento: Rajbhandari et al., ZeRO.
- Autori o organizzazione: Rajbhandari et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1910.02054
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; ZeRO: Memory Optimizations Toward Training Trillion Parameter Models; 2.1 Data, Model and Pipeline Parallelism; 3.1 Model States: Optimizer States, Gradients and Parameters.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Parametri, gradienti e optimizer state vengono shardati tra worker.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-36-003

- Titolo o riferimento: PyTorch, Fully Sharded Data Parallel.
- Autori o organizzazione: PyTorch.
- Tipo: standard o documentazione ufficiale.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://pytorch.org/docs/stable/fsdp.html
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-partial; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-36-004

- Titolo o riferimento: Narayanan et al., Efficient Large-Scale Language Model Training on GPU Clusters.
- Autori o organizzazione: Narayanan et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2104.04473
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2. Modes of Parallelism; 2.1. Data Parallelism; 2.2. Pipeline Model Parallelism.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
