# Specifica visuale CACHE-02

- modello compositivo: eviction_lifecycle
- domanda principale: Quale controllo collega «Prefix caching» a «Compressione ed eviction» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: blocchi di KV cache associati a una richiesta
- input: layer, token, KV dimension, dtype e prefix
- output: cache occupata, hit e latenza
- nodi locali: Prefix caching: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi…; Compressione ed eviction: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano…
- limite visualizzato: la cache deve rispettare ownership, posizione e validità del prefisso
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
