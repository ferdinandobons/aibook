# Testo alternativo

BLOCK-02, Anatomia del blocco moderno. Quale controllo collega «SwiGLU» a «Ordine e parallelismo» senza superare il limite dichiarato? La composizione residual stack collega «SwiGLU», «Ordine e parallelismo». L'input è h di shape [batch, length, d] e norma misurata; l'output è h' con shape preservata e statistiche confrontabili. Il limite esplicito è: ordine dei sottolayer e shape sono parte del blocco.
