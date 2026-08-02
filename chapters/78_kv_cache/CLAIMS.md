# Registro dei claim. Capitolo 78

| ID | Claim | Prova |
|---|---|---|
| `CL-78-001` | Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente. | `SRC-78-001` |
| `CL-78-002` | Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel. | `SRC-78-002` |
| `CL-78-003` | Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa. | `SRC-78-003` |
| `CL-78-004` | Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili. | `SRC-78-004` |
| `CL-78-005` | Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile. | `SRC-78-001` |
