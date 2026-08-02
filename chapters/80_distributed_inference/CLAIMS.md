# Registro dei claim. Capitolo 80

| ID | Claim | Prova |
|---|---|---|
| `CL-80-001` | Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo. | `SRC-80-001` |
| `CL-80-002` | MoE distribuisce esperti e usa all-to-all durante l'inference. | `SRC-80-002` |
| `CL-80-003` | Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete. | `SRC-80-003` |
| `CL-80-004` | Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi. | `SRC-80-004` |
| `CL-80-005` | Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione. | `SRC-80-001` |
