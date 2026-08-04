# Specifica visuale GENERATION-02

- modello compositivo: quality_lenses
- domanda principale: Quale controllo collega «Editing e inpainting» a «Controllo e provenienza» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un contenuto immagine e la condizione che lo modifica
- input: latent, prompt, mask e rumore
- output: immagine, score e metadati di provenienza
- nodi locali: Editing e inpainting: Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da…; Controllo e provenienza: ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati…
- limite visualizzato: controllo dell'immagine e verità del contenuto sono proprietà diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
