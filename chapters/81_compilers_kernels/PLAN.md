# Piano interno. Capitolo 81

- Domanda centrale: quale contratto costruisce Compiler, kernel e runtime?
- Oggetto continuo: un grafo di operatori trasformato dal compiler; input guida: grafo, shape, dtype, target e kernel.
- Prerequisito stabile: Capitolo 80, Serving disaggregato e inference distribuita.
- Gap: lowering, fusion, autotuning e gestione dei graph break.
- Output consegnato: kernel eseguito, latenza e fallback; consumer successivo: Capitolo 82, LLMOps, edge, costo ed energia.
- Invariante principale: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Visuali: KERNELS-01 e KERNELS-02, con famiglie compositive variabili.
- Snippet: code/snip_81_contract.py; output: code/outputs/SNIP-81-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Grafo e operatori

- Ultima affermazione stabile: un grafo di operatori trasformato dal compiler.
- Concetto nuovo: Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation.
- Input e shape: grafo, shape, dtype, target e kernel.
- Operazione: lowering, fusion, autotuning e gestione dei graph break.
- Output e shape: kernel eseguito, latenza e fallback.
- Che cosa cambia: il passaggio specifico di «Grafo e operatori».
- Invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due operatori fusi con output numericamente equivalente; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Kernel fusion.
- Prova: SRC-81-001 e sezione pubblica corrispondente.

## Transizione 2. Kernel fusion

- Ultima affermazione stabile: un grafo di operatori trasformato dal compiler.
- Concetto nuovo: Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso.
- Input e shape: grafo, shape, dtype, target e kernel.
- Operazione: lowering, fusion, autotuning e gestione dei graph break.
- Output e shape: kernel eseguito, latenza e fallback.
- Che cosa cambia: il passaggio specifico di «Kernel fusion».
- Invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due operatori fusi con output numericamente equivalente; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Triton e kernel custom.
- Prova: SRC-81-002 e sezione pubblica corrispondente.

## Transizione 3. Triton e kernel custom

- Ultima affermazione stabile: un grafo di operatori trasformato dal compiler.
- Concetto nuovo: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA.
- Input e shape: grafo, shape, dtype, target e kernel.
- Operazione: lowering, fusion, autotuning e gestione dei graph break.
- Output e shape: kernel eseguito, latenza e fallback.
- Che cosa cambia: il passaggio specifico di «Triton e kernel custom».
- Invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due operatori fusi con output numericamente equivalente; provare anche una condizione incoerente e osservare il controllo.
- Consumer: torch.compile e graph break.
- Prova: SRC-81-003 e sezione pubblica corrispondente.

## Transizione 4. torch.compile e graph break

- Ultima affermazione stabile: un grafo di operatori trasformato dal compiler.
- Concetto nuovo: Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break.
- Input e shape: grafo, shape, dtype, target e kernel.
- Operazione: lowering, fusion, autotuning e gestione dei graph break.
- Output e shape: kernel eseguito, latenza e fallback.
- Che cosa cambia: il passaggio specifico di «torch.compile e graph break».
- Invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due operatori fusi con output numericamente equivalente; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Autotuning e portabilità.
- Prova: SRC-81-004 e sezione pubblica corrispondente.

## Transizione 5. Autotuning e portabilità

- Ultima affermazione stabile: un grafo di operatori trasformato dal compiler.
- Concetto nuovo: Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati.
- Input e shape: grafo, shape, dtype, target e kernel.
- Operazione: lowering, fusion, autotuning e gestione dei graph break.
- Output e shape: kernel eseguito, latenza e fallback.
- Che cosa cambia: il passaggio specifico di «Autotuning e portabilità».
- Invariante: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due operatori fusi con output numericamente equivalente; provare anche una condizione incoerente e osservare il controllo.
- Consumer: LLMOps, edge, costo ed energia.
- Prova: SRC-81-001 e sezione pubblica corrispondente.
