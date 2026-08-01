# Registro dei claim. Capitolo 8

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-INFO-001` | La self-information di un evento con probabilità `p` è `-log p`; la base del logaritmo determina l'unità. | `SRC-INFO-001`, `SRC-INFO-002` | verificato |
| `CLM-INFO-002` | L'entropia discreta è il valore atteso della self-information. | `SRC-INFO-001`, `SRC-INFO-002` | verificato |
| `CLM-INFO-003` | Con log base due l'entropia è misurata in bit; con log naturale in nat. | `SRC-INFO-002` | verificato |
| `CLM-INFO-004` | Su un supporto finito fissato, la distribuzione uniforme massimizza l'entropia. | `SRC-INFO-002` | verificato |
| `CLM-INFO-005` | L'entropia congiunta e condizionata soddisfano `H(X,Y)=H(X)+H(Y|X)`. | `SRC-INFO-002` | verificato |
| `CLM-INFO-006` | La mutua informazione può essere scritta come `KL(p(x,y)||p(x)p(y))`. | `SRC-INFO-002` | verificato |
| `CLM-INFO-007` | La KL divergence è non negativa e vale zero quando le distribuzioni coincidono sul supporto rilevante. | `SRC-INFO-002` | verificato |
| `CLM-INFO-008` | La KL non è simmetrica e non è una metrica. | `SRC-INFO-002` | verificato |
| `CLM-INFO-009` | La cross-entropy soddisfa `H(q,p)=H(q)+KL(q||p)` quando le quantità sono finite. | `SRC-INFO-002`, `SRC-INFO-004` | verificato |
| `CLM-INFO-010` | Con target one-hot, la cross-entropy coincide con la negative log-probability della classe osservata. | derivazione; `SRC-INFO-004`, `SRC-INFO-007` | verificato |
| `CLM-INFO-011` | Minimizzare la negative log-likelihood equivale a massimizzare la likelihood sullo stesso dataset. | `SRC-INFO-004`, `SRC-INFO-005` | verificato |
| `CLM-INFO-012` | I logits sono punteggi non normalizzati; la softmax li trasforma in probabilità lungo una dimensione. | `SRC-INFO-005`, `SRC-INFO-007` | verificato |
| `CLM-INFO-013` | `log_softmax` è numericamente più stabile di `log(softmax(x))` calcolati separatamente. | `SRC-INFO-008` | verificato |
| `CLM-INFO-014` | `CrossEntropyLoss` con target come indici equivale a `LogSoftmax` seguito da `NLLLoss`. | `SRC-INFO-007`, `SRC-INFO-008` | verificato |
| `CLM-INFO-015` | `CrossEntropyLoss` accetta target probabilistici, ma PyTorch non verifica automaticamente che siano distribuzioni valide. | `SRC-INFO-007` | verificato |
| `CLM-INFO-016` | Per softmax più cross-entropy, il gradiente rispetto ai logits è `p-q`. | derivazione; `SRC-INFO-004`, `SRC-INFO-005` | verificato |
| `CLM-INFO-017` | Una previsione confidentemente errata riceve una negative log-likelihood elevata. | `SRC-INFO-004`, `SRC-INFO-006` | verificato |
| `CLM-INFO-018` | La loss media empirica stima il rischio atteso rispetto alla distribuzione dei dati, sotto le condizioni del protocollo. | `SRC-INFO-004`, `SRC-INFO-005` | verificato con condizioni |
| `CLM-INFO-019` | La MSE corrisponde, a costanti e varianza fissata, alla negative log-likelihood di un modello gaussiano. | `SRC-INFO-004`, `SRC-INFO-005` | verificato con condizioni |
| `CLM-INFO-020` | La L1 loss corrisponde, a costanti e scala fissata, alla negative log-likelihood di un modello laplaciano. | `SRC-INFO-004`, `SRC-INFO-005` | verificato con condizioni |
| `CLM-INFO-021` | `KLDivLoss` si aspetta input in log-probabilità; `batchmean` è la riduzione allineata alla definizione matematica sul batch. | `SRC-INFO-009` | verificato |
| `CLM-INFO-022` | Nel run, i logits `[2,0; 0,5; -1,0]` producono probabilità `[0,7856; 0,1753; 0,0391]` e loss `0,241311`. | `SNIP-INFO-001` | eseguito |
| `CLM-INFO-023` | Nel run, `H(q,p)=0,466311`, `H(q)=0,394398` e `KL(q||p)=0,071914`. | `SNIP-INFO-001` | eseguito |
| `CLM-INFO-024` | Nel run, logits confidentemente errati producono loss `3,241311`. | `SNIP-INFO-001` | eseguito |
| `CLM-INFO-025` | Nel run, la softmax ingenua di logits circa `1000` produce `nan`, mentre `log_softmax` restituisce valori finiti. | `SNIP-INFO-001` | eseguito |

## Claim esclusi

- entropia alta non significa maggiore intelligenza o comprensione;
- entropia bassa non garantisce correttezza;
- KL non è una distanza metrica;
- cross-entropy bassa non garantisce calibrazione, robustezza o sicurezza;
- accuratezza e cross-entropy non sono intercambiabili;
- target soft arbitrari non sono automaticamente distribuzioni valide;
- MSE non implica rumore gaussiano senza il relativo modello;
- una funzione obiettivo non rappresenta automaticamente tutti i costi reali;
- `mean` e `batchmean` di `KLDivLoss` non vengono trattati come equivalenti;
- stabilità numerica non elimina tutti gli errori di precisione finita.
