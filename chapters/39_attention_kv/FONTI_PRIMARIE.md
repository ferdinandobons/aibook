# Fonti primarie e autorevoli. Capitolo 39

- Data di consultazione: 3 agosto 2026
- Routing semantico: capitolo 39 -> tema `attention_variants`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-39-001

- Titolo o riferimento: Shazeer, Fast Transformer Decoding: One Write-Head is All You Need.
- Autori o organizzazione: Shazeer.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1911.02150
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2 Background: Neural Attention; 2.1 Dot-Product Attention; 2.2 Multi-head Attention.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Ogni query head possiede key e value dedicate. Compressione latente e numero di KV head sono strategie differenti.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-39-002

- Titolo o riferimento: Ainslie et al., GQA: Training Generalized Multi-Query Transformer Models.
- Autori o organizzazione: Ainslie et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2305.13245
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; GQA : Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints; 2.2 Grouped-query attention.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Tutte le query head condividono una singola coppia key-value, riducendo la cache.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-39-003

- Titolo o riferimento: DeepSeek-AI, DeepSeek-V2.
- Autori o organizzazione: DeepSeek-AI.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2405.04434
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2.1 Multi-Head Latent Attention: Boosting Inference Efficiency; 2.1.1 Preliminaries: Standard Multi-Head Attention; Appendix D Ablation of Attention Mechanisms.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Gruppi di query head condividono un numero intermedio di KV head.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-39-004

- Titolo o riferimento: Beltagy, Peters and Cohan, Longformer.
- Autori o organizzazione: Beltagy.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2004.05150
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-partial; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 3.1 Attention Pattern; 4.1 Attention Pattern.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
