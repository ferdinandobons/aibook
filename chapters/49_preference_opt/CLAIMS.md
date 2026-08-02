# Registro dei claim. Capitolo 49

| ID | Claim | Prova |
|---|---|---|
| `CL-49-001` | DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata. | `SRC-49-001` |
| `CL-49-002` | Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie. | `SRC-49-002` |
| `CL-49-003` | Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie. | `SRC-49-003` |
| `CL-49-004` | Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili. | `SRC-49-004` |
| `CL-49-005` | L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie. | `SRC-49-001` |
