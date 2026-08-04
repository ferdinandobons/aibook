# Piano interno. Capitolo 53

- Domanda centrale: quale contratto costruisce Test-time compute, ricerca e controllo del budget?
- Oggetto continuo: un budget di compute aggiunto durante l'inferenza; input guida: prompt, numero di campioni, token e deadline.
- Prerequisito stabile: Capitolo 52, Addestrare e distillare il reasoning.
- Gap: best-of-n, tree search e adaptive compute.
- Output consegnato: risposta, costo, latenza e qualità; consumer successivo: Capitolo 54, Aggiornamento, merging ed editing del modello.
- Invariante principale: qualità e costo devono essere riportati insieme.
- Visuali: COMPUTE-01 e COMPUTE-02, con famiglie compositive variabili.
- Snippet: code/snip_53_contract.py; output: code/outputs/SNIP-53-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Più compute dopo il training

- Ultima affermazione stabile: un budget di compute aggiunto durante l'inferenza.
- Concetto nuovo: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta.
- Input e shape: prompt, numero di campioni, token e deadline.
- Operazione: best-of-n, tree search e adaptive compute.
- Output e shape: risposta, costo, latenza e qualità.
- Che cosa cambia: il passaggio specifico di «Più compute dopo il training».
- Invariante: qualità e costo devono essere riportati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro campioni con un budget massimo di token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Best-of-n.
- Prova: SRC-53-001 e sezione pubblica corrispondente.

## Transizione 2. Best-of-n

- Ultima affermazione stabile: un budget di compute aggiunto durante l'inferenza.
- Concetto nuovo: Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla diversità e dalla qualità del ranking.
- Input e shape: prompt, numero di campioni, token e deadline.
- Operazione: best-of-n, tree search e adaptive compute.
- Output e shape: risposta, costo, latenza e qualità.
- Che cosa cambia: il passaggio specifico di «Best-of-n».
- Invariante: qualità e costo devono essere riportati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro campioni con un budget massimo di token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Tree search.
- Prova: SRC-53-002 e sezione pubblica corrispondente.

## Transizione 3. Tree search

- Ultima affermazione stabile: un budget di compute aggiunto durante l'inferenza.
- Concetto nuovo: Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget definiscono il costo.
- Input e shape: prompt, numero di campioni, token e deadline.
- Operazione: best-of-n, tree search e adaptive compute.
- Output e shape: risposta, costo, latenza e qualità.
- Che cosa cambia: il passaggio specifico di «Tree search».
- Invariante: qualità e costo devono essere riportati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro campioni con un budget massimo di token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Adaptive compute.
- Prova: SRC-53-003 e sezione pubblica corrispondente.

## Transizione 4. Adaptive compute

- Ultima affermazione stabile: un budget di compute aggiunto durante l'inferenza.
- Concetto nuovo: Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. La stima di difficoltà può essere errata.
- Input e shape: prompt, numero di campioni, token e deadline.
- Operazione: best-of-n, tree search e adaptive compute.
- Output e shape: risposta, costo, latenza e qualità.
- Che cosa cambia: il passaggio specifico di «Adaptive compute».
- Invariante: qualità e costo devono essere riportati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro campioni con un budget massimo di token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metriche costo-qualità.
- Prova: SRC-53-004 e sezione pubblica corrispondente.

## Transizione 5. Metriche costo-qualità

- Ultima affermazione stabile: un budget di compute aggiunto durante l'inferenza.
- Concetto nuovo: Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier.
- Input e shape: prompt, numero di campioni, token e deadline.
- Operazione: best-of-n, tree search e adaptive compute.
- Output e shape: risposta, costo, latenza e qualità.
- Che cosa cambia: il passaggio specifico di «Metriche costo-qualità».
- Invariante: qualità e costo devono essere riportati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro campioni con un budget massimo di token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Aggiornamento, merging ed editing del modello.
- Prova: SRC-53-001 e sezione pubblica corrispondente.
