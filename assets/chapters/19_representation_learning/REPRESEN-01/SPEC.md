# Specifica visuale REPRESEN-01

- modello compositivo: latent_geometry
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Che cosa rappresenta un vettore a Metric e contrastive learning nel capitolo 19?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: un vettore prodotto per un compito successivo
- input: u = [1, 2, 0] e v = [2, 1, 0]
- output: un vettore, una similarità o una predizione downstream
- nodi locali: Che cosa rappresenta un vettore: Il significato dipende da obiettivo e dati.; Bottleneck e autoencoder: Un autoencoder comprime e ricostruisce.; Metric e contrastive learning: Obiettivi contrastivi avvicinano coppie positive e separano alternative.
- limite visualizzato: la geometria dipende da dati, obiettivo e normalizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
