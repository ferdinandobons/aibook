# Specifica visuale VIDEO-01

- modello compositivo: video_grid
- domanda principale: Come si passa da «Spazio e tempo» a «Autoregressione» mantenendo osservabile una sequenza di frame condizionata nel tempo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una sequenza di frame condizionata nel tempo
- input: frame, latent video, testo e timestamp
- output: frame coerenti e misura di flicker
- nodi locali: Spazio e tempo: Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono…; Video diffusion: Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata…; Autoregressione: Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica…
- limite visualizzato: qualità del singolo frame non dimostra coerenza tra frame
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
