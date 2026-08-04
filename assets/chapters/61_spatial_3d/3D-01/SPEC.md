# Specifica visuale 3D-01

- modello compositivo: coordinate_frames
- domanda principale: Come si passa da «Coordinate e camera» a «Gaussian splatting» mantenendo osservabile punti e coordinate che descrivono una scena 3D?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: punti e coordinate che descrivono una scena 3D
- input: punti, camera, raggi e profondità
- output: immagine, campo radiance o geometria
- nodi locali: Coordinate e camera: Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera.…; NeRF: Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering…; Gaussian splatting: Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da…
- limite visualizzato: una vista proiettata non determina da sola la scena completa
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
