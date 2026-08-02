# Registro dei claim. Capitolo 51

| ID | Claim | Prova |
|---|---|---|
| `CL-51-001` | Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori. | `SRC-51-001` |
| `CL-51-002` | La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking. | `SRC-51-002` |
| `CL-51-003` | Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità. | `SRC-51-003` |
| `CL-51-004` | Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale. | `SRC-51-004` |
| `CL-51-005` | Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore. | `SRC-51-001` |
