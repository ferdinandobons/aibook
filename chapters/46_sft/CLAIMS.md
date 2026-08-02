# Registro dei claim. Capitolo 46

| ID | Claim | Prova |
|---|---|---|
| `CL-46-001` | Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate. | `SRC-46-001` |
| `CL-46-002` | Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. | `SRC-46-002` |
| `CL-46-003` | Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile. | `SRC-46-003` |
| `CL-46-004` | Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati. | `SRC-46-004` |
| `CL-46-005` | Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili. | `SRC-46-001` |
