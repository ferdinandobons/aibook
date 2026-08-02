# Registro dei claim. Capitolo 95

| ID | Claim | Prova |
|---|---|---|
| `CL-95-001` | Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili. | `SRC-95-001` |
| `CL-95-002` | Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape. | `SRC-95-002` |
| `CL-95-003` | AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU. | `SRC-95-003` |
| `CL-95-004` | Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria. | `SRC-95-001` |
| `CL-95-005` | Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto. | `SRC-95-002` |
