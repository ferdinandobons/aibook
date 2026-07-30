# ATT-01. Specifica

- Domanda unica: perché due query devono poter produrre combinazioni diverse della stessa sorgente?
- Stato prima: un unico vettore viene riutilizzato dai consumer.
- Trasformazione nuova: coefficienti dipendenti dalla query.
- Stato dopo: due combinazioni diverse della stessa sequenza.
- Invariante: i quattro elementi sorgente non cambiano.
- Confine: la figura non descrive il calcolo di score e softmax.
- Stato: `da modificare`, presentata per review autoriale del concetto e non approvata come figura finale.
