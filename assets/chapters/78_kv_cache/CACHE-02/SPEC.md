# Specifica visuale CACHE-02

- modello compositivo: eviction_lifecycle
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Prefix caching da Compressione ed eviction?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: blocchi di KV cache associati a una richiesta
- input: layer, token, KV dimension, dtype e prefix
- output: cache occupata, hit e latenza
- nodi locali: Prefix caching: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi son.; Compressione ed eviction: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano preci.
- limite visualizzato: la cache deve rispettare ownership, posizione e validità del prefisso
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
