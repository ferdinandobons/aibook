# Piano editoriale. Capitolo 81

## Obiettivo didattico

Seguire **Compiler, kernel e runtime** da grafo, shape, dtype, target e kernel a kernel eseguito, latenza e fallback, osservando lowering, fusion, autotuning e gestione dei graph break senza oltrepassare questo limite: ottimizzazione del grafo e correttezza numerica devono essere confrontate.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 29: Il Transformer da zero
- Capitolo 40: Attention hardware-aware

## Percorso della lezione

1. **Grafo e operatori.** Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. Prova: SRC-81-001.
2. **Kernel fusion.** Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. Prova: SRC-81-002.
3. **Triton e kernel custom.** Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. Prova: SRC-81-003.
4. **torch.compile e graph break.** Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break. Prova: SRC-81-004.
5. **Autotuning e portabilità.** Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati. Prova: SRC-81-001.

## Prove e artefatti

- riferimento minimo: `code/snip_81_contract.py`; test: `code/test_81_contract.py`; output: `code/outputs/SNIP-81-001.txt`.
- visuali candidate: KERNELS-01, KERNELS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
