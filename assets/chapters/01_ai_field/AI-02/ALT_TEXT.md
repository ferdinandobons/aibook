# Alt text previsto per `AI-02`

Confronto orizzontale su sfondo bianco. Nel pannello `Training`, i dati e i target alimentano il modello e la loss; la loss produce gradienti, l'optimizer aggiorna i parametri da theta a theta primo e genera un checkpoint aggiornato. Nel pannello `Inference`, un nuovo input attraversa il modello con checkpoint fissato e produce un output, senza loss, gradienti o optimizer. Un footer chiarisce che `eval()` e `inference_mode()` hanno ruoli distinti in PyTorch.

Stato: testo previsto, da verificare sulla futura candidata.
