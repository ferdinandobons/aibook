# Registro dei claim. Capitolo 12

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-SUP-001` | Un dataset supervisionato contiene coppie input-target usate per apprendere un predittore. | `SRC-SUP-002`, `SRC-SUP-003`, `SRC-SUP-004` | verificato |
| `CLM-SUP-002` | Il target è un valore osservato secondo una procedura e non coincide automaticamente con il concetto reale di interesse. | metodologia del capitolo; `SRC-SUP-002`, `SRC-SUP-004` | verificato con limite |
| `CLM-SUP-003` | La classificazione usa target discreti, mentre la regressione produce quantità numeriche secondo il contratto del problema. | `SRC-SUP-003`, `SRC-SUP-004` | verificato |
| `CLM-SUP-004` | Il rischio empirico medio è la media della loss sugli esempi del campione. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-005` | Ridurre il rischio empirico non dimostra da solo un basso rischio sui casi futuri. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-006` | Una baseline semplice rende visibile la difficoltà che il modello deve superare. | metodologia sperimentale; `SRC-SUP-002` | verificato |
| `CLM-SUP-007` | La logistic regression binaria usa una trasformazione affine e la funzione logistica per modellare una probabilità condizionata. | `SRC-SUP-001`, `SRC-SUP-003`, `SRC-SUP-004` | verificato |
| `CLM-SUP-008` | Con soglia 0,50 la frontiera della logistic regression è `w^T x + b = 0`; con soglia generica `τ` è `w^T x+b=log(τ/(1-τ))`. | derivazione dalla sigmoide | verificato |
| `CLM-SUP-009` | `BCEWithLogitsLoss` combina sigmoid e binary cross-entropy in una forma numericamente più stabile del calcolo separato standard. | `SRC-SUP-011` | verificato |
| `CLM-SUP-010` | Una penalità L2 modifica la funzione obiettivo e rende costosi pesi grandi. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-011` | Training, validation e test hanno ruoli differenti nel protocollo. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-012` | Usare il test per scegliere ripetutamente configurazioni riduce la sua indipendenza come valutazione finale. | `SRC-SUP-002`, `SRC-SUP-003`; continuità con Capitoli 3 e 4 | verificato |
| `CLM-SUP-013` | Lo split deve rispettare gruppi, tempo e informazione disponibile nel caso d'uso. | `SRC-SUP-002`, `SRC-SUP-003` | verificato con contesto |
| `CLM-SUP-014` | Cambiare la soglia modifica la decisione senza modificare i parametri del modello. | derivazione e `SNIP-SUP-001` | verificato |
| `CLM-SUP-015` | Precision e recall dipendono da componenti differenti della confusion matrix. | definizioni; `SRC-SUP-003`, `SRC-SUP-010` | verificato |
| `CLM-SUP-016` | Nei dataset molto sbilanciati, la lettura precision-recall rende più visibile il comportamento sulla classe positiva rispetto alla sola accuracy. | `SRC-SUP-010` | verificato con limite |
| `CLM-SUP-017` | Overfitting descrive un comportamento che si adatta al campione senza trasferirsi adeguatamente ai casi di interesse. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-018` | L'overfitting non dipende soltanto dal numero di parametri. | `SRC-SUP-002`, `SRC-SUP-003` | verificato |
| `CLM-SUP-019` | La decomposizione bias-varianza quadratica richiede condizioni specifiche e non si trasferisce automaticamente a ogni loss di classificazione. | `SRC-SUP-005`, `SRC-SUP-003` | verificato con limite |
| `CLM-SUP-020` | Early stopping usa un segnale di validation e richiede una regola di arresto dichiarata. | `SRC-SUP-009`, `SRC-SUP-002` | verificato |
| `CLM-SUP-021` | Una support-vector network costruisce una superficie decisionale in uno spazio di feature e il paper del 1995 tratta anche dati non separabili. | `SRC-SUP-006` | verificato |
| `CLM-SUP-022` | Una random forest combina predittori ad albero con casualità e il suo comportamento dipende da forza e correlazione dei predittori. | `SRC-SUP-007` | verificato |
| `CLM-SUP-023` | Il gradient boosting può essere formulato come discesa per stadi nello spazio delle funzioni. | `SRC-SUP-008` | verificato |
| `CLM-SUP-024` | Class weight, resampling e soglia agiscono in punti differenti del protocollo e non sono equivalenti. | derivazione dei contratti; `SRC-SUP-011`, `SRC-SUP-002` | verificato |
| `CLM-SUP-025` | In `BCEWithLogitsLoss`, `pos_weight` modifica il contributo dei target positivi secondo il contratto dell'API. | `SRC-SUP-011` | verificato |
| `CLM-SUP-026` | Le metriche per slice possono rivelare concentrazioni di errore nascoste dalla media complessiva. | metodologia; continuità con Capitolo 4 | verificato |
| `CLM-SUP-027` | Un risultato sul test storico non garantisce comportamento invariato dopo uno shift della distribuzione o del processo di labeling. | `SRC-SUP-002`, `SRC-SUP-003`; continuità con Capitolo 3 | verificato |
| `CLM-SUP-028` | Nel run, l'obiettivo regolarizzato scende da `0,778276` a `0,313711`. | `SNIP-SUP-001` | eseguito |
| `CLM-SUP-029` | Nel run, la soglia selezionata sulla validation è `0,30`. | `SNIP-SUP-001` | eseguito |
| `CLM-SUP-030` | Nel run, soglia `0,30` e soglia `0,50` ottengono entrambe accuracy `0,900` sul test, ma costi pesati `13` e `21`. | `SNIP-SUP-001`, test | eseguito |
| `CLM-SUP-031` | Nel run, la baseline maggioritaria ha accuracy `0,540`, recall `0` e costo `115`. | `SNIP-SUP-001` | eseguito |
| `CLM-SUP-032` | Nel run, la slice con tracking disponibile ha recall `1,000` e costo `3`, mentre la slice con tracking mancante ha recall `0,778` e costo `10`. | `SNIP-SUP-001` | eseguito |
| `CLM-SUP-033` | Gli otto test automatici del capitolo risultano superati nell'ambiente registrato. | `code/outputs/TESTS.txt` | eseguito |

## Claim esclusi

- le label sintetiche non rappresentano un processo aziendale reale;
- la soglia `0,30` non è raccomandata fuori dall'esempio;
- la logistic regression non viene presentata come modello universalmente migliore;
- il miglior costo del run non dimostra calibrazione delle probabilità;
- il vantaggio osservato sul test non viene generalizzato a nuovi seed o distribuzioni;
- una accuracy uguale non implica equivalenza operativa;
- class weight, resampling o early stopping non garantiscono generalizzazione;
- le descrizioni di SVM, random forest e gradient boosting non costituiscono benchmark comparativi;
- le metriche di una slice con 16 esempi non sono trattate come stime precise;
- il test sintetico non sostiene claim su fairness, sicurezza o impatto reale.
