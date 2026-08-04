# Testo alternativo

CACHE-02, KV cache e riuso del contesto. Quale controllo collega «Prefix caching» a «Compressione ed eviction» senza superare il limite dichiarato? La composizione eviction lifecycle collega «Prefix caching», «Compressione ed eviction». L'input è layer, token, KV dimension, dtype e prefix; l'output è cache occupata, hit e latenza. Il limite esplicito è: la cache deve rispettare ownership, posizione e validità del prefisso.
