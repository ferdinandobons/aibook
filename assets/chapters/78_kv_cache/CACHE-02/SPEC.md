# Specifica visuale CACHE-02

- famiglia: timeline
- domanda principale: Il diagramma segue il passaggio: Prefill, decode, paging, caching ed eviction. L'input è layer, token, KV dimension, dtype e prefix, l'output è cache occupata, hit e latenza; il vincolo da controllare è che la cache deve rispettare ownership, posizione e validità del prefisso
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, timeline, invariante o limite in chiusura
- nodi e contenuti: 1: Prefill e decode; 2: Layout; 3: PagedAttention; 4: Prefix caching; 5: Compressione ed eviction
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: la cache deve rispettare ownership, posizione e validità del prefisso
- fonti collegate: SRC-78-001 ... SRC-78-004
- alt text: Diagramma CACHE-02 del Capitolo 78, famiglia timeline. Domanda: Il diagramma segue il passaggio: Prefill, decode, paging, caching ed eviction. L'input è layer, token, KV dimension, dtype e prefix, l'output è cache occupata, hit e latenza; il vincolo da controllare è che la cache deve rispettare ownership, posizione e validità del prefisso La composizione usa i passaggi Prefill e decode, Layout, PagedAttention, Prefix caching, Compressione ed eviction.
