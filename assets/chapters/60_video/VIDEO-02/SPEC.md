# Specifica visuale VIDEO-02

- modello compositivo: temporal_generation
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Coerenza da Condizionamento e editing?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una sequenza di frame condizionata nel tempo
- input: frame, latent video, testo e timestamp
- output: frame coerenti e misura di flicker
- nodi locali: Coerenza: Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità.; Condizionamento e editing: Testo, immagine iniziale, traiettoria o maschere guidano il video.
- limite visualizzato: qualità del singolo frame non dimostra coerenza tra frame
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
