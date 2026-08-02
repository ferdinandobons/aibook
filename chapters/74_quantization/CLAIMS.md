# Registro dei claim. Capitolo 74

| ID | Claim | Prova |
|---|---|---|
| `CL-74-001` | Una mappa affine converte valori floating point in interi. Granularità per tensor, channel o group cambia errore e metadata. | `SRC-74-001` |
| `CL-74-002` | Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale. | `SRC-74-002` |
| `CL-74-003` | Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. | `SRC-74-003` |
| `CL-74-004` | Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. | `SRC-74-004` |
| `CL-74-005` | GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti. | `SRC-74-001` |
