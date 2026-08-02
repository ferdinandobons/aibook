# Registro dei claim. Capitolo 48

| ID | Claim | Prova |
|---|---|---|
| `CL-48-001` | Dati di confronto ordinano risposte alla stessa richiesta. Il protocollo deve registrare istruzioni ai valutatori, accordo e slice. | `SRC-48-001` |
| `CL-48-002` | Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. Lo score è una stima del dataset di preferenze, non una misura universale di qualità. | `SRC-48-002` |
| `CL-48-003` | PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento. | `SRC-48-003` |
| `CL-48-004` | Il termine KL limita lo spostamento della policy. Un reward imperfetto può essere sfruttato senza migliorare l'obiettivo umano. | `SRC-48-004` |
| `CL-48-005` | Win rate, reward e giudizi automatici devono essere affiancati da controlli indipendenti, red teaming e analisi di regressione. | `SRC-48-001` |
