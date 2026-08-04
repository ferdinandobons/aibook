# Testo alternativo

KERNELS-01, Compiler, kernel e runtime. Come si passa da «Grafo e operatori» a «Triton e kernel custom» mantenendo osservabile un grafo di operatori trasformato dal compiler? La composizione compiler graph collega «Grafo e operatori», «Kernel fusion», «Triton e kernel custom». L'input è grafo, shape, dtype, target e kernel; l'output è kernel eseguito, latenza e fallback. Il limite esplicito è: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
