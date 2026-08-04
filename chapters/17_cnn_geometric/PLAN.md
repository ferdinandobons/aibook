# Piano interno. Capitolo 17

- Domanda centrale: quale contratto costruisce Convolutional network e apprendimento geometrico?
- Oggetto continuo: una griglia locale di feature; input guida: una matrice 3 x 3 e un kernel 2 x 2.
- Prerequisito stabile: Capitolo 16, Addestrare reti profonde.
- Gap: lo stesso kernel scorre posizioni definite da stride e padding.
- Output consegnato: una griglia di attivazioni con dimensioni calcolabili; consumer successivo: Capitolo 18, Reti ricorrenti e modelli sequenziali.
- Invariante principale: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Visuali: GEOMETRI-01 e GEOMETRI-02, con famiglie compositive variabili.
- Snippet: code/snip_17_contract.py; output: code/outputs/SNIP-17-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Condivisione locale dei pesi

- Ultima affermazione stabile: una griglia locale di feature.
- Concetto nuovo: Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora una ipotesi di regolarità locale.
- Input e shape: una matrice 3 x 3 e un kernel 2 x 2.
- Operazione: lo stesso kernel scorre posizioni definite da stride e padding.
- Output e shape: una griglia di attivazioni con dimensioni calcolabili.
- Che cosa cambia: il passaggio specifico di «Condivisione locale dei pesi».
- Invariante: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una singola finestra 2 x 2 calcolata a mano; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Stride, padding e receptive field.
- Prova: SRC-17-001 e sezione pubblica corrispondente.

## Transizione 2. Stride, padding e receptive field

- Ultima affermazione stabile: una griglia locale di feature.
- Concetto nuovo: Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione.
- Input e shape: una matrice 3 x 3 e un kernel 2 x 2.
- Operazione: lo stesso kernel scorre posizioni definite da stride e padding.
- Output e shape: una griglia di attivazioni con dimensioni calcolabili.
- Che cosa cambia: il passaggio specifico di «Stride, padding e receptive field».
- Invariante: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una singola finestra 2 x 2 calcolata a mano; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Equivarianza e invariance.
- Prova: SRC-17-002 e sezione pubblica corrispondente.

## Transizione 3. Equivarianza e invariance

- Ultima affermazione stabile: una griglia locale di feature.
- Concetto nuovo: La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance.
- Input e shape: una matrice 3 x 3 e un kernel 2 x 2.
- Operazione: lo stesso kernel scorre posizioni definite da stride e padding.
- Output e shape: una griglia di attivazioni con dimensioni calcolabili.
- Che cosa cambia: il passaggio specifico di «Equivarianza e invariance».
- Invariante: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una singola finestra 2 x 2 calcolata a mano; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Vision Transformer e ibridi.
- Prova: SRC-17-003 e sezione pubblica corrispondente.

## Transizione 4. Vision Transformer e ibridi

- Ultima affermazione stabile: una griglia locale di feature.
- Concetto nuovo: Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati.
- Input e shape: una matrice 3 x 3 e un kernel 2 x 2.
- Operazione: lo stesso kernel scorre posizioni definite da stride e padding.
- Output e shape: una griglia di attivazioni con dimensioni calcolabili.
- Che cosa cambia: il passaggio specifico di «Vision Transformer e ibridi».
- Invariante: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una singola finestra 2 x 2 calcolata a mano; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Grafi e message passing.
- Prova: SRC-17-004 e sezione pubblica corrispondente.

## Transizione 5. Grafi e message passing

- Ultima affermazione stabile: una griglia locale di feature.
- Concetto nuovo: Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate.
- Input e shape: una matrice 3 x 3 e un kernel 2 x 2.
- Operazione: lo stesso kernel scorre posizioni definite da stride e padding.
- Output e shape: una griglia di attivazioni con dimensioni calcolabili.
- Che cosa cambia: il passaggio specifico di «Grafi e message passing».
- Invariante: la condivisione dei pesi non implica invariance a ogni trasformazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una singola finestra 2 x 2 calcolata a mano; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reti ricorrenti e modelli sequenziali.
- Prova: SRC-17-001 e sezione pubblica corrispondente.
