# Alt text RECIPE-02

Diagramma RECIPE-02 del Capitolo 35, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Forward, backward, update, schedule e recovery. L'input è batch, learning rate, seed, optimizer e checkpoint, l'output è loss, parametri e checkpoint ripristinabile; il vincolo da controllare è che un checkpoint deve includere lo stato necessario a continuare il run La composizione usa i passaggi Batch di token, Inizializzazione, AdamW, Warmup e schedule, Checkpoint e recovery.
