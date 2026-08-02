# Registro dei claim. Capitolo 81

| ID | Claim | Prova |
|---|---|---|
| `CL-81-001` | Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. | `SRC-81-001` |
| `CL-81-002` | Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. | `SRC-81-002` |
| `CL-81-003` | Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. | `SRC-81-003` |
| `CL-81-004` | Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break. | `SRC-81-004` |
| `CL-81-005` | Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati. | `SRC-81-001` |
