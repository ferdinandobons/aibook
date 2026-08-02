# Claim

- `CL-RECURREN-001`. Uno stato che attraversa la sequenza: Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo.
- `CL-RECURREN-002`. Backpropagation through time: Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere.
- `CL-RECURREN-003`. LSTM e GRU: Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente.
- `CL-RECURREN-004`. Bidirezionalità e causalità: Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming.
- `CL-RECURREN-005`. RNN, attention e stato: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari.
