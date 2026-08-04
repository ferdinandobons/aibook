# Specifica visuale CACHE-01

- modello compositivo: cache_layout
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Prefill e decode a PagedAttention nel capitolo 78?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: blocchi di KV cache associati a una richiesta
- input: layer, token, KV dimension, dtype e prefix
- output: cache occupata, hit e latenza
- nodi locali: Prefill e decode: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache.; Layout: Layer, batch, KV head, token e head dimension determinano shape e byte.; PagedAttention: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare se.
- limite visualizzato: la cache deve rispettare ownership, posizione e validità del prefisso
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
