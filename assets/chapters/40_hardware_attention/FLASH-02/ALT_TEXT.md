# Testo alternativo

FLASH-02, Attention hardware-aware. Quale controllo collega «Backward e ricomputazione» a «Backend» senza superare il limite dichiarato? La composizione compute memory tradeoff collega «Backward e ricomputazione», «Backend». L'input è tile di Q, K, V, dtype e device; l'output è stesso contratto matematico con memoria e latenza misurate. Il limite esplicito è: una misura hardware dipende da shape, backend e precisione.
