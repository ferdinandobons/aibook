# Specifica visuale CACHE-01

- modello compositivo: cache_layout
- domanda principale: Come si passa da «Prefill e decode» a «PagedAttention» mantenendo osservabile blocchi di KV cache associati a una richiesta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: blocchi di KV cache associati a una richiesta
- input: layer, token, KV dimension, dtype e prefix
- output: cache occupata, hit e latenza
- nodi locali: Prefill e decode: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la…; Layout: Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e…; PagedAttention: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare…
- limite visualizzato: la cache deve rispettare ownership, posizione e validità del prefisso
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
