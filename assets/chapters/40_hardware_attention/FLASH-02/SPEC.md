# Specifica visuale FLASH-02

- modello compositivo: compute_memory_tradeoff
- domanda principale: Quale controllo collega «Backward e ricomputazione» a «Backend» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: il calcolo dell'attention e il suo movimento di dati
- input: tile di Q, K, V, dtype e device
- output: stesso contratto matematico con memoria e latenza misurate
- nodi locali: Backward e ricomputazione: Salvare meno intermedi scambia memoria con compute aggiuntivo.; Backend: FlashAttention, backend memory-efficient e math rispettano la stessa API entro…
- limite visualizzato: una misura hardware dipende da shape, backend e precisione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
