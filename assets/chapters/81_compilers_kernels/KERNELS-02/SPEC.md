# Specifica visuale KERNELS-02

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Lowering, fusion, autotuning e gestione dei graph break. L'input è grafo, shape, dtype, target e kernel, l'output è kernel eseguito, latenza e fallback; il vincolo da controllare è che ottimizzazione del grafo e correttezza numerica devono essere confrontate
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: Grafo e operatori; 2: Kernel fusion; 3: Triton e kernel custom; 4: torch.compile e graph break; 5: Autotuning e portabilità
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate
- fonti collegate: SRC-81-001 ... SRC-81-004
- alt text: Diagramma KERNELS-02 del Capitolo 81, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Lowering, fusion, autotuning e gestione dei graph break. L'input è grafo, shape, dtype, target e kernel, l'output è kernel eseguito, latenza e fallback; il vincolo da controllare è che ottimizzazione del grafo e correttezza numerica devono essere confrontate La composizione usa i passaggi Grafo e operatori, Kernel fusion, Triton e kernel custom, torch.compile e graph break, Autotuning e portabilità.
