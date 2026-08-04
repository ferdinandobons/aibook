# Specifica visuale GEOMETRI-02

- modello compositivo: vision_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Vision Transformer e ibridi da Grafi e message passing?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: una griglia locale di feature
- input: una matrice 3 x 3 e un kernel 2 x 2
- output: una griglia di attivazioni con dimensioni calcolabili
- nodi locali: Vision Transformer e ibridi: Patch embedding e attention offrono una geometria diversa.; Grafi e message passing: Su un grafo, i vicini non sono disposti in una griglia regolare.
- limite visualizzato: la condivisione dei pesi non implica invariance a ogni trasformazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
