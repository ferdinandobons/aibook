# Specifica visuale AUDIO-01

- modello compositivo: audio_pipeline
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Waveform e spettrogramma a TTS nel capitolo 59?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un segnale audio e la sua rappresentazione discreta
- input: waveform, sample rate, spettrogramma o codec
- output: testo, waveform o token audio
- nodi locali: Waveform e spettrogramma: Il segnale audio è campionato nel tempo.; ASR: Streaming e offline hanno vincoli diversi.; TTS: Sintesi vocale trasforma testo in acoustic representation e waveform.
- limite visualizzato: sample rate e durata fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
