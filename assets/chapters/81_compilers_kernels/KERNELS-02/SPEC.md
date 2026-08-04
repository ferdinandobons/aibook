# Specifica visuale KERNELS-02

- modello compositivo: kernel_fusion
- domanda principale: Quale controllo collega «torch.compile e graph break» a «Autotuning e portabilità» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un grafo di operatori trasformato dal compiler
- input: grafo, shape, dtype, target e kernel
- output: kernel eseguito, latenza e fallback
- nodi locali: torch.compile e graph break: Tracing e guard permettono specializzazione dinamica. Python side effect o shape non…; Autotuning e portabilità: Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede…
- limite visualizzato: ottimizzazione del grafo e correttezza numerica devono essere confrontate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
