# Specifica visuale VIDEO-01

- modello compositivo: video_grid
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Spazio e tempo a Autoregressione nel capitolo 60?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una sequenza di frame condizionata nel tempo
- input: frame, latent video, testo e timestamp
- output: frame coerenti e misura di flicker
- nodi locali: Spazio e tempo: Un video aggiunge una dimensione temporale alle immagini.; Video diffusion: Il denoiser opera su tensori spazio-temporali o latent compressi.; Autoregressione: Frame, patch o token video possono essere generati in ordine.
- limite visualizzato: qualità del singolo frame non dimostra coerenza tra frame
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
