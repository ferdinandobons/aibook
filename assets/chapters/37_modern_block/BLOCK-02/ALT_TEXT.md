# Alt text BLOCK-02

Diagramma BLOCK-02 del Capitolo 37, famiglia architecture. Domanda: Il diagramma segue il passaggio: Norm, attention, MLP e gating nell'ordine scelto. L'input è h di shape [batch, length, d] e norma misurata, l'output è h' con shape preservata e statistiche confrontabili; il vincolo da controllare è che ordine dei sottolayer e shape sono parte del blocco La composizione usa i passaggi Residual stream, Pre-norm e post-norm, RMSNorm, SwiGLU, Ordine e parallelismo.
