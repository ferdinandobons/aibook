# Specifica visuale VQ-01

- modello compositivo: latent_bottleneck
- orientamento: a blocchi, tensor a sinistra e trasformazione a destra
- domanda principale: Quale percorso collega Inferenza approssimata a Reparameterization trick nel capitolo 22?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una variabile osservata e il suo codice latente
- input: x, media, log-varianza e rumore epsilon
- output: ricostruzione, KL e codice latente
- nodi locali: Inferenza approssimata: Il VAE introduce un encoder q(z|x) per approssimare il posterior.; ELBO: L'evidence lower bound combina ricostruzione e KL verso il prior.; Reparameterization trick: Un campione gaussiano viene scritto come trasformazione di rumore indipendente.
- limite visualizzato: la ricostruzione non elimina il costo KL né dimostra disentanglement
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
