# Specifica visuale AUDIO-01

- modello compositivo: audio_pipeline
- domanda principale: Come si passa da «Waveform e spettrogramma» a «TTS» mantenendo osservabile un segnale audio e la sua rappresentazione discreta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un segnale audio e la sua rappresentazione discreta
- input: waveform, sample rate, spettrogramma o codec
- output: testo, waveform o token audio
- nodi locali: Waveform e spettrogramma: Il segnale audio è campionato nel tempo. STFT e mel filterbank producono…; ASR: Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o…; TTS: Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e…
- limite visualizzato: sample rate e durata fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
