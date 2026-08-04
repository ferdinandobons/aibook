# Piano interno. Capitolo 61

- Domanda centrale: quale contratto costruisce 3D, spazio e rappresentazione delle scene?
- Oggetto continuo: punti e coordinate che descrivono una scena 3D; input guida: punti, camera, raggi e profondità.
- Prerequisito stabile: Capitolo 60, Generazione video.
- Gap: proiezione, rendering, splatting o ricostruzione.
- Output consegnato: immagine, campo radiance o geometria; consumer successivo: Capitolo 62, World model, embodied AI e vision-language-action.
- Invariante principale: una vista proiettata non determina da sola la scena completa.
- Visuali: 3D-01 e 3D-02, con famiglie compositive variabili.
- Snippet: code/snip_61_contract.py; output: code/outputs/SNIP-61-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Coordinate e camera

- Ultima affermazione stabile: punti e coordinate che descrivono una scena 3D.
- Concetto nuovo: Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering.
- Input e shape: punti, camera, raggi e profondità.
- Operazione: proiezione, rendering, splatting o ricostruzione.
- Output e shape: immagine, campo radiance o geometria.
- Che cosa cambia: il passaggio specifico di «Coordinate e camera».
- Invariante: una vista proiettata non determina da sola la scena completa.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due punti proiettati con camera e profondità dichiarate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: NeRF.
- Prova: SRC-61-001 e sezione pubblica corrispondente.

## Transizione 2. NeRF

- Ultima affermazione stabile: punti e coordinate che descrivono una scena 3D.
- Concetto nuovo: Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi.
- Input e shape: punti, camera, raggi e profondità.
- Operazione: proiezione, rendering, splatting o ricostruzione.
- Output e shape: immagine, campo radiance o geometria.
- Che cosa cambia: il passaggio specifico di «NeRF».
- Invariante: una vista proiettata non determina da sola la scena completa.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due punti proiettati con camera e profondità dichiarate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Gaussian splatting.
- Prova: SRC-61-002 e sezione pubblica corrispondente.

## Transizione 3. Gaussian splatting

- Ultima affermazione stabile: punti e coordinate che descrivono una scena 3D.
- Concetto nuovo: Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi.
- Input e shape: punti, camera, raggi e profondità.
- Operazione: proiezione, rendering, splatting o ricostruzione.
- Output e shape: immagine, campo radiance o geometria.
- Che cosa cambia: il passaggio specifico di «Gaussian splatting».
- Invariante: una vista proiettata non determina da sola la scena completa.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due punti proiettati con camera e profondità dichiarate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Mesh, point cloud e voxel.
- Prova: SRC-61-003 e sezione pubblica corrispondente.

## Transizione 4. Mesh, point cloud e voxel

- Ultima affermazione stabile: punti e coordinate che descrivono una scena 3D.
- Concetto nuovo: Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering.
- Input e shape: punti, camera, raggi e profondità.
- Operazione: proiezione, rendering, splatting o ricostruzione.
- Output e shape: immagine, campo radiance o geometria.
- Che cosa cambia: il passaggio specifico di «Mesh, point cloud e voxel».
- Invariante: una vista proiettata non determina da sola la scena completa.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due punti proiettati con camera e profondità dichiarate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Generazione e grounding spaziale.
- Prova: SRC-61-004 e sezione pubblica corrispondente.

## Transizione 5. Generazione e grounding spaziale

- Ultima affermazione stabile: punti e coordinate che descrivono una scena 3D.
- Concetto nuovo: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.
- Input e shape: punti, camera, raggi e profondità.
- Operazione: proiezione, rendering, splatting o ricostruzione.
- Output e shape: immagine, campo radiance o geometria.
- Che cosa cambia: il passaggio specifico di «Generazione e grounding spaziale».
- Invariante: una vista proiettata non determina da sola la scena completa.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due punti proiettati con camera e profondità dichiarate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: World model, embodied AI e vision-language-action.
- Prova: SRC-61-001 e sezione pubblica corrispondente.
