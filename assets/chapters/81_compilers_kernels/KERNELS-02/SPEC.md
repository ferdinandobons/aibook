# Specifica visuale KERNELS-02

- modello compositivo: kernel_fusion
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale failure o confronto separa torch.compile e graph break da Autotuning e portabilità?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un grafo di operatori trasformato dal compiler
- input: grafo, shape, dtype, target e kernel
- output: kernel eseguito, latenza e fallback
- nodi locali: torch.compile e graph break: Tracing e guard permettono specializzazione dinamica.; Autotuning e portabilità: Tile, num warps e schedule ottimali dipendono dall'hardware.
- limite visualizzato: ottimizzazione del grafo e correttezza numerica devono essere confrontate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
