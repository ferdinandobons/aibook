# Specifica visuale VQ-02

- modello compositivo: codebook_lookup
- orientamento: a blocchi, tensor a sinistra e trasformazione a destra
- domanda principale: Quale failure o confronto separa Posterior collapse da VQ-VAE?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una variabile osservata e il suo codice latente
- input: x, media, log-varianza e rumore epsilon
- output: ricostruzione, KL e codice latente
- nodi locali: Posterior collapse: Un decoder molto potente può ignorare z e avvicinare il posterior al prior.; VQ-VAE: La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook.
- limite visualizzato: la ricostruzione non elimina il costo KL né dimostra disentanglement
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
