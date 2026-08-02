# Registro dei claim. Capitolo 79

| ID | Claim | Prova |
|---|---|---|
| `CL-79-001` | Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano. | `SRC-79-001` |
| `CL-79-002` | Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse. | `SRC-79-002` |
| `CL-79-003` | Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency. | `SRC-79-003` |
| `CL-79-004` | Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema. | `SRC-79-004` |
| `CL-79-005` | TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta. | `SRC-79-001` |
