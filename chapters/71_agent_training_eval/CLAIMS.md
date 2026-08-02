# Registro dei claim. Capitolo 71

| ID | Claim | Prova |
|---|---|---|
| `CL-71-001` | Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento. | `SRC-71-001` |
| `CL-71-002` | Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire. | `SRC-71-002` |
| `CL-71-003` | Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker. | `SRC-71-003` |
| `CL-71-004` | Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting. | `SRC-71-004` |
| `CL-71-005` | Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale. | `SRC-71-001` |
