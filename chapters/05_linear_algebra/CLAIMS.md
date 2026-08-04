# Registro dei claim. Capitolo 5

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-LA-001` | Uno scalare è una singola quantità; un vettore è una sequenza ordinata; una matrice organizza quantità su due assi; un tensore generalizza a più assi. | `SRC-LA-001` | verificata |
| `CLM-LA-002` | La shape descrive la lunghezza di ciascun asse, mentre il significato dell'asse dipende dal problema e dalla convenzione adottata. | definizione e convenzione esplicita | verificata |
| `CLM-LA-003` | Somma elemento per elemento e prodotto matriciale sono operazioni differenti con condizioni di compatibilità differenti. | `SRC-LA-001`, derivazione | verificata |
| `CLM-LA-004` | Il prodotto scalare di due vettori reali è la somma dei prodotti delle componenti corrispondenti. | `SRC-LA-001`, derivazione | verificata |
| `CLM-LA-005` | Il prodotto `AB` è definito quando il numero di colonne di A coincide con il numero di righe di B. | `SRC-LA-001`, derivazione | verificata |
| `CLM-LA-006` | Una matrice può rappresentare una trasformazione lineare; l'aggiunta di un bias produce una trasformazione affine. | `SRC-LA-001`, `SRC-LA-002` | verificata |
| `CLM-LA-007` | In `XW^T+b`, l'asse feature viene contratto e il bias viene applicato a ogni riga dell'output. | derivazione; `SRC-LA-006`, `SRC-LA-007` | verificata |
| `CLM-LA-008` | Il broadcasting confronta le dimensioni dalla fine e richiede dimensioni uguali, pari a uno o assenti. | `SRC-LA-007` | verificata |
| `CLM-LA-009` | `torch.matmul` applica regole diverse a vettori, matrici e batch, e può broadcastare le dimensioni batch. | `SRC-LA-006` | verificata |
| `CLM-LA-010` | La matrice di Gram `XX^T` contiene prodotti scalari tra le righe di X. | derivazione | verificata |
| `CLM-LA-011` | Lo span di un insieme di vettori contiene le loro combinazioni lineari. | `SRC-LA-002` | verificata |
| `CLM-LA-012` | Vettori linearmente indipendenti non ammettono una combinazione lineare nulla con coefficienti non tutti nulli. | `SRC-LA-002` | verificata |
| `CLM-LA-013` | Il rango misura la dimensione dello spazio delle colonne e coincide con quella dello spazio delle righe. | `SRC-LA-002`, `SRC-LA-003` | verificata |
| `CLM-LA-014` | In aritmetica finita, `matrix_rank` usa una tolleranza per determinare quali valori singolari contano come non nulli. | `SRC-LA-008` | verificata |
| `CLM-LA-015` | La SVD reale ridotta scrive `A = U diag(S) V^T`, con colonne ortonormali e valori singolari non negativi in ordine decrescente. | `SRC-LA-009` | verificata |
| `CLM-LA-016` | Troncare la SVD conserva le componenti associate ai valori singolari scelti e produce una approssimazione a rango ridotto. | `SRC-LA-002`, `SRC-LA-003` | verificata |
| `CLM-LA-017` | Una trasposizione cambia l'ordine degli assi senza cambiare i valori matematici associati agli indici permutati. | derivazione; `SRC-LA-010` per view PyTorch | verificata |
| `CLM-LA-018` | Una view può condividere lo stesso storage con shape e stride differenti; alcune operazioni richiedono o producono layout contigui. | `SRC-LA-010` | verificata |
| `CLM-LA-019` | Nel run illustrativo, `X[3,4] @ W.T[4,3] + b[3]` produce score di shape `[3,3]`. | `SNIP-LA-001` | verificata |
| `CLM-LA-020` | Nel run illustrativo, la matrice A ha rango numerico 2 e la ricostruzione SVD completa ha errore massimo inferiore a `4e-15` in float64. | `SNIP-LA-001` | verificata |

## Claim esclusi

- un asse non possiede un significato universale indipendente dal problema;
- broadcasting non implica necessariamente una copia fisica dei dati;
- un valore singolare piccolo non è automaticamente irrilevante in ogni applicazione;
- il rango numerico dipende dalla tolleranza e dalla precisione;
- l'SVD non è l'unico strumento per compressione o riduzione dimensionale;
- la vicinanza nel prodotto scalare non equivale automaticamente a somiglianza semantica.
