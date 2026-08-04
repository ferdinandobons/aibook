# Specifica visuale GEOMETRI-01

- modello compositivo: receptive_field
- domanda principale: Come si passa da «Condivisione locale dei pesi» a «Equivarianza e invariance» mantenendo osservabile una griglia locale di feature?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: una griglia locale di feature
- input: una matrice 3 x 3 e un kernel 2 x 2
- output: una griglia di attivazioni con dimensioni calcolabili
- nodi locali: Condivisione locale dei pesi: Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione…; Stride, padding e receptive field: Stride e padding determinano la griglia dell'output. Il receptive field cresce con…; Equivarianza e invariance: La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e…
- limite visualizzato: la condivisione dei pesi non implica invariance a ogni trasformazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
