# Specifica visuale 3D-02

- modello compositivo: scene_stack
- domanda principale: Quale controllo collega «Mesh, point cloud e voxel» a «Generazione e grounding spaziale» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: punti e coordinate che descrivono una scena 3D
- input: punti, camera, raggi e profondità
- output: immagine, campo radiance o geometria
- nodi locali: Mesh, point cloud e voxel: Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering.; Generazione e grounding spaziale: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica…
- limite visualizzato: una vista proiettata non determina da sola la scena completa
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
