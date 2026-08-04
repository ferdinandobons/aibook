# Piano editoriale. Capitolo 17

## Obiettivo didattico

Seguire **Convolutional network e apprendimento geometrico** da una matrice 3 x 3 e un kernel 2 x 2 a una griglia di attivazioni con dimensioni calcolabili, osservando lo stesso kernel scorre posizioni definite da stride e padding senza oltrepassare questo limite: la condivisione dei pesi non implica invariance a ogni trasformazione.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 15: Dal percettrone alle reti multilayer

## Percorso della lezione

1. **Condivisione locale dei pesi.** Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora una ipotesi di regolarità locale. Prova: SRC-17-001.
2. **Stride, padding e receptive field.** Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione. Prova: SRC-17-002.
3. **Equivarianza e invariance.** La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance. Prova: SRC-17-003.
4. **Vision Transformer e ibridi.** Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati. Prova: SRC-17-004.
5. **Grafi e message passing.** Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate. Prova: SRC-17-001.

## Prove e artefatti

- riferimento minimo: `code/snip_17_contract.py`; test: `code/test_17_contract.py`; output: `code/outputs/SNIP-17-001.txt`.
- visuali candidate: GEOMETRI-01, GEOMETRI-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
