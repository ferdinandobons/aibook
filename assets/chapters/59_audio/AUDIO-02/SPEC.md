# Specifica visuale AUDIO-02

- modello compositivo: time_frequency_map
- domanda principale: Quale controllo collega «Neural codec» a «Musica e dialogo» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un segnale audio e la sua rappresentazione discreta
- input: waveform, sample rate, spettrogramma o codec
- output: testo, waveform o token audio
- nodi locali: Neural codec: Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio…; Musica e dialogo: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche…
- limite visualizzato: sample rate e durata fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
