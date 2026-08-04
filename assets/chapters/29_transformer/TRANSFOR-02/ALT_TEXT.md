# Testo alternativo

TRANSFOR-02, Il Transformer da zero. Quale controllo collega «Multi-head attention» a «Residual stream e output» senza superare il limite dichiarato? La composizione tensor route collega «Multi-head attention», «Residual stream e output». L'input è tokenizzati di shape [batch, length] e vettori [batch, length, d]; l'output è stato contestuale e logits. Il limite esplicito è: mask, shape e percorso residuale devono essere compatibili.
