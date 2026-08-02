# Registro dei claim. Capitolo 72

| ID | Claim | Prova |
|---|---|---|
| `CL-72-001` | Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant. | `SRC-72-001` |
| `CL-72-002` | Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. | `SRC-72-002` |
| `CL-72-003` | Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. | `SRC-72-003` |
| `CL-72-004` | Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. | `SRC-72-004` |
| `CL-72-005` | Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati. | `SRC-72-001` |
