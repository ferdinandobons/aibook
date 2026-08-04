# Registro dei claim. Capitolo 6

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-CALC-001` | La derivata di una funzione scalare descrive il limite del rapporto tra variazione dell'output e variazione dell'input. | definizione matematica; `SRC-CALC-001` | verificata |
| `CLM-CALC-002` | Una derivata parziale varia una coordinata mantenendo fisse le altre nella definizione locale. | `SRC-CALC-001` | verificata |
| `CLM-CALC-003` | Il gradiente raccoglie le derivate parziali di una funzione scalare rispetto alle coordinate dell'input. | `SRC-CALC-001` | verificata |
| `CLM-CALC-004` | La Jacobiana raccoglie le derivate parziali di un output vettoriale rispetto a un input vettoriale. | `SRC-CALC-003`, `SRC-CALC-004` | verificata |
| `CLM-CALC-005` | La regola della catena compone le derivate locali lungo le dipendenze del calcolo. | `SRC-CALC-001`, `SRC-CALC-004` | verificata |
| `CLM-CALC-006` | Un grafo computazionale rende espliciti valori intermedi e dipendenze tra operazioni. | `SRC-CALC-003`, `SRC-CALC-005` | verificata |
| `CLM-CALC-007` | Il reverse mode propaga prodotti vettore-Jacobiana dall'output agli input. | `SRC-CALC-003`, `SRC-CALC-007` | verificata |
| `CLM-CALC-008` | Per una loss scalare con molti parametri, il reverse mode calcola tutti i gradienti rispetto ai parametri in una singola traversata inversa del grafo, a fattori costanti dipendenti dalle operazioni. | `SRC-CALC-003`, `SRC-CALC-004` | verificato con limite |
| `CLM-CALC-009` | Backpropagation è una applicazione del reverse-mode automatic differentiation a grafi di reti neurali; non è l'optimizer step. | `SRC-CALC-002`, `SRC-CALC-003` | verificata |
| `CLM-CALC-010` | Automatic differentiation applica regole locali esatte alle operazioni eseguite dal programma, entro l'aritmetica numerica usata. | `SRC-CALC-003` | verificata |
| `CLM-CALC-011` | Le differenze finite approssimano una derivata attraverso valutazioni perturbate e dipendono dalla scelta del passo. | `SRC-CALC-003`, `SRC-CALC-008` | verificata |
| `CLM-CALC-012` | PyTorch autograd costruisce durante il forward un grafo delle operazioni che richiedono gradienti e lo attraversa all'indietro usando la regola della catena. | `SRC-CALC-005` | verificata |
| `CLM-CALC-013` | `Tensor.backward` accumula i gradienti nei tensori foglia interessati; chiamate ripetute richiedono azzeramento o gestione esplicita. | `SRC-CALC-006` | verificata |
| `CLM-CALC-014` | Un output non scalare richiede un gradiente esterno compatibile oppure una riduzione a scalare prima di `backward`. | `SRC-CALC-006`, `SRC-CALC-007` | verificata |
| `CLM-CALC-015` | `torch.autograd.grad` restituisce gradienti o prodotti vettore-Jacobiana rispetto agli input richiesti senza usare lo stesso contratto di accumulo di `.backward()`. | `SRC-CALC-007` | verificata |
| `CLM-CALC-016` | `gradcheck` confronta autograd con differenze finite ed è progettato con default adatti alla doppia precisione. | `SRC-CALC-008` | verificata |
| `CLM-CALC-017` | `no_grad` evita la registrazione delle operazioni nel grafo; `inference_mode` applica ulteriori ottimizzazioni e restrizioni. | `SRC-CALC-009` | verificata |
| `CLM-CALC-018` | Nel run illustrativo, `z=2,5`, `h=tanh(z)=0,986614`, `y_hat=-0,490630` e la loss è `0,396611`. | `SNIP-CALC-001` | verificata |
| `CLM-CALC-019` | Nel run illustrativo, i gradienti manuali, autograd e finite difference coincidono entro le tolleranze registrate. | `SNIP-CALC-001`, test automatici | verificata |
| `CLM-CALC-020` | Nel run illustrativo, `dL/dw1=0,033157`, `dL/db1=0,016579`, `dL/dw2=-0,878708`, `dL/db2=-0,890630`. | `SNIP-CALC-001` | verificata |

## Claim esclusi

- una derivata locale non descrive automaticamente una variazione finita grande;
- il gradiente non è un aggiornamento dei parametri;
- backpropagation non garantisce convergenza dell'ottimizzazione;
- differenze finite non sono sempre accurate vicino a discontinuità o con un passo inadeguato;
- autograd non rende differenziabile una operazione matematicamente non differenziabile;
- `retain_graph=True` non è una soluzione predefinita ai problemi di progettazione del grafo;
- l'assenza di errore in gradcheck non prova la correttezza di un intero modello o training loop.
