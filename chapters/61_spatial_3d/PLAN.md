# Piano editoriale. Capitolo 61

## Obiettivo didattico

Seguire **3D, spazio e rappresentazione delle scene** da punti, camera, raggi e profondità a immagine, campo radiance o geometria, osservando proiezione, rendering, splatting o ricostruzione senza oltrepassare questo limite: una vista proiettata non determina da sola la scena completa.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 17: Convolutional network e apprendimento geometrico
- Capitolo 55: Fondamenti della multimodalità

## Percorso della lezione

1. **Coordinate e camera.** Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering. Prova: SRC-61-001.
2. **NeRF.** Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi. Prova: SRC-61-002.
3. **Gaussian splatting.** Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. Prova: SRC-61-003.
4. **Mesh, point cloud e voxel.** Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. Prova: SRC-61-004.
5. **Generazione e grounding spaziale.** Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate. Prova: SRC-61-001.

## Prove e artefatti

- riferimento minimo: `code/snip_61_contract.py`; test: `code/test_61_contract.py`; output: `code/outputs/SNIP-61-001.txt`.
- visuali candidate: 3D-01, 3D-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
