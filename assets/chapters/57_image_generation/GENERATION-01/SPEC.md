# Specifica visuale GENERATION-01

- modello compositivo: image_generation
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Latent diffusion a Classifier-free guidance nel capitolo 57?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un contenuto immagine e la condizione che lo modifica
- input: latent, prompt, mask e rumore
- output: immagine, score e metadati di provenienza
- nodi locali: Latent diffusion: Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente.; Conditioning: Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenaz.; Classifier-free guidance: Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off ri.
- limite visualizzato: controllo dell'immagine e verità del contenuto sono proprietà diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
