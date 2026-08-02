# Claim

- `CL-MLP-001`. Una decisione lineare: Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature.
- `CL-MLP-002`. Strati nascosti: Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine.
- `CL-MLP-003`. Attivazioni: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione.
- `CL-MLP-004`. Capacità ed espressività: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile.
- `CL-MLP-005`. Dal forward al training: Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici.
