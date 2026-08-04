# Specifica visuale GENERATION-02

- modello compositivo: quality_lenses
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Editing e inpainting da Controllo e provenienza?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un contenuto immagine e la condizione che lo modifica
- input: latent, prompt, mask e rumore
- output: immagine, score e metadati di provenienza
- nodi locali: Editing e inpainting: Una mask stabilisce regioni modificabili.; Controllo e provenienza: ControlNet, adapter e reference image aggiungono vincoli.
- limite visualizzato: controllo dell'immagine e verità del contenuto sono proprietà diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
