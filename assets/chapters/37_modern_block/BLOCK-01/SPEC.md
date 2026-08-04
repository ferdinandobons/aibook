# Specifica visuale BLOCK-01

- famiglia: matrix
- domanda principale: Il diagramma segue il passaggio: Norm, attention, MLP e gating nell'ordine scelto. L'input è h di shape [batch, length, d] e norma misurata, l'output è h' con shape preservata e statistiche confrontabili; il vincolo da controllare è che ordine dei sottolayer e shape sono parte del blocco
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v47.png
- ordine di lettura: titolo, domanda, matrix, invariante o limite in chiusura
- nodi e contenuti: 1: Residual stream; 2: Pre-norm e post-norm; 3: RMSNorm; 4: SwiGLU; 5: Ordine e parallelismo
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: ordine dei sottolayer e shape sono parte del blocco
- fonti collegate: SRC-37-001 ... SRC-37-004
- alt text: Diagramma BLOCK-01 del Capitolo 37, famiglia matrix. Domanda: Il diagramma segue il passaggio: Norm, attention, MLP e gating nell'ordine scelto. L'input è h di shape [batch, length, d] e norma misurata, l'output è h' con shape preservata e statistiche confrontabili; il vincolo da controllare è che ordine dei sottolayer e shape sono parte del blocco La composizione usa i passaggi Residual stream, Pre-norm e post-norm, RMSNorm, SwiGLU, Ordine e parallelismo.
