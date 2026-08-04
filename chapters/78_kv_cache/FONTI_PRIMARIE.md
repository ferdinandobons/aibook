# Fonti primarie e autorevoli. Capitolo 78

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 78 -> tema `kv_cache`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-78-001

- Titolo o riferimento: Kwon et al., Efficient Memory Management for Large Language Model Serving with PagedAttention.
- Autori o organizzazione: Kwon et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2309.06180
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Efficient Memory Management for Large Language Model Serving with PagedAttention; 3. Memory Challenges in LLM Serving; 3.1. Memory Management in Existing Systems.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente. Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-78-002

- Titolo o riferimento: Xiao et al., Efficient Streaming Language Models with Attention Sinks.
- Autori o organizzazione: Xiao et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2309.17453
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 3.2 Rolling KV Cache with Attention Sinks.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Layer, batch, KV head, token e head dimension determinano shape e byte.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-78-003

- Titolo o riferimento: Zheng et al., SGLang.
- Autori o organizzazione: Zheng et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2312.07104
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Efficiently Programming Large Language Models using SGLang; 1 Introduction; 2 Background.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-78-004

- Titolo o riferimento: Dao et al., FlashAttention.
- Autori o organizzazione: Dao et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2205.14135
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; FlashAttention : Fast and Memory-Efficient Exact Attention with IO-Awareness; 2.2 Standard Attention Implementation; 3 FlashAttention : Algorithm, Analysis, and Extensions.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
