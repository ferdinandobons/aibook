# Registro dei claim. Capitolo 75

| ID | Claim | Prova |
|---|---|---|
| `CL-75-001` | Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine. | `SRC-75-001` |
| `CL-75-002` | BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel. | `SRC-75-002` |
| `CL-75-003` | Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione. | `SRC-75-003` |
| `CL-75-004` | Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati. | `SRC-75-004` |
| `CL-75-005` | Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo. | `SRC-75-001` |
