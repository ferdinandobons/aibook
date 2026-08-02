# Claim

- `CL-AUTOREGR-001`. Fattorizzare una sequenza: La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti.
- `CL-AUTOREGR-002`. Teacher forcing: Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output.
- `CL-AUTOREGR-003`. Maschera causale: La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida.
- `CL-AUTOREGR-004`. Sampling e accumulo degli errori: Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training.
- `CL-AUTOREGR-005`. Immagini, audio e token discreti: L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti.
