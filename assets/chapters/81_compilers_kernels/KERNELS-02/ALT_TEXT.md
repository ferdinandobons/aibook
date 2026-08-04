# Alt text KERNELS-02

Diagramma KERNELS-02 del Capitolo 81, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Lowering, fusion, autotuning e gestione dei graph break. L'input è grafo, shape, dtype, target e kernel, l'output è kernel eseguito, latenza e fallback; il vincolo da controllare è che ottimizzazione del grafo e correttezza numerica devono essere confrontate La composizione usa i passaggi Grafo e operatori, Kernel fusion, Triton e kernel custom, torch.compile e graph break, Autotuning e portabilità.
