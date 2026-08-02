# Registro dei claim. Capitolo 76

| ID | Claim | Prova |
|---|---|---|
| `CL-76-001` | Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza. | `SRC-76-001` |
| `CL-76-002` | Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità. | `SRC-76-002` |
| `CL-76-003` | Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire. | `SRC-76-003` |
| `CL-76-004` | Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti. | `SRC-76-004` |
| `CL-76-005` | Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme. | `SRC-76-001` |
