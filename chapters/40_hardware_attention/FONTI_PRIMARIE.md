# Fonti primarie e autorevoli. Capitolo 40

- Data di consultazione: 3 agosto 2026
- Routing semantico: capitolo 40 -> tema `flash`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-40-001

- Titolo o riferimento: Dao et al., FlashAttention.
- Autori o organizzazione: Dao et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2205.14135
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; FlashAttention : Fast and Memory-Efficient Exact Attention with IO-Awareness; 2.2 Standard Attention Implementation; 3 FlashAttention : Algorithm, Analysis, and Extensions.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Lo stesso operatore può avere traffico di memoria molto diverso. FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-40-002

- Titolo o riferimento: Dao, FlashAttention-2.
- Autori o organizzazione: Dao.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2307.08691
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; FlashAttention-2 : Faster Attention with Better Parallelism and Work Partitioning; 2.2 Standard Attention Implementation; 2.3 FlashAttention.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-40-003

- Titolo o riferimento: Shah et al., FlashAttention-3.
- Autori o organizzazione: Shah et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2407.08608
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision; 2 Background: Multi-Head Attention and GPU Characteristics; 2.1 Multi-Head Attention.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Massimo, denominatore e numeratore vengono aggiornati blocco per blocco.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-40-004

- Titolo o riferimento: PyTorch, Scaled Dot Product Attention.
- Autori o organizzazione: PyTorch.
- Tipo: standard o documentazione ufficiale.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-partial; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Salvare meno intermedi scambia memoria con compute aggiuntivo.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
