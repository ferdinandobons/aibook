# Specifica visuale RECIPE-02

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Forward, backward, update, schedule e recovery. L'input è batch, learning rate, seed, optimizer e checkpoint, l'output è loss, parametri e checkpoint ripristinabile; il vincolo da controllare è che un checkpoint deve includere lo stato necessario a continuare il run
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: Batch di token; 2: Inizializzazione; 3: AdamW; 4: Warmup e schedule; 5: Checkpoint e recovery
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: un checkpoint deve includere lo stato necessario a continuare il run
- fonti collegate: SRC-35-001 ... SRC-35-004
- alt text: Diagramma RECIPE-02 del Capitolo 35, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Forward, backward, update, schedule e recovery. L'input è batch, learning rate, seed, optimizer e checkpoint, l'output è loss, parametri e checkpoint ripristinabile; il vincolo da controllare è che un checkpoint deve includere lo stato necessario a continuare il run La composizione usa i passaggi Batch di token, Inizializzazione, AdamW, Warmup e schedule, Checkpoint e recovery.
