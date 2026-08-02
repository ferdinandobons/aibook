# Registro dei claim. Capitolo 64

| ID | Claim | Prova |
|---|---|---|
| `CL-64-001` | Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati. | `SRC-64-001` |
| `CL-64-002` | Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica. | `SRC-64-002` |
| `CL-64-003` | Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto. | `SRC-64-003` |
| `CL-64-004` | Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti. | `SRC-64-004` |
| `CL-64-005` | Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme. | `SRC-64-001` |
