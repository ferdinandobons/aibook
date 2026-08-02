# Registro dei claim. Capitolo 47

| ID | Claim | Prova |
|---|---|---|
| `CL-47-001` | PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. | `SRC-47-001` |
| `CL-47-002` | Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base. | `SRC-47-002` |
| `CL-47-003` | Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. | `SRC-47-003` |
| `CL-47-004` | Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. | `SRC-47-004` |
| `CL-47-005` | Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere. | `SRC-47-001` |
