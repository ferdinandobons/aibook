# Specifica visuale VQ-01

- modello compositivo: latent_bottleneck
- domanda principale: Come si passa da «Inferenza approssimata» a «Reparameterization trick» mantenendo osservabile una variabile osservata e il suo codice latente?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una variabile osservata e il suo codice latente
- input: x, media, log-varianza e rumore epsilon
- output: ricostruzione, KL e codice latente
- nodi locali: Inferenza approssimata: Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella…; ELBO: L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO…; Reparameterization trick: Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo…
- limite visualizzato: la ricostruzione non elimina il costo KL né dimostra disentanglement
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
