# Specifica visuale AUDIO-02

- modello compositivo: time_frequency_map
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale failure o confronto separa Neural codec da Musica e dialogo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un segnale audio e la sua rappresentazione discreta
- input: waveform, sample rate, spettrogramma o codec
- output: testo, waveform o token audio
- nodi locali: Neural codec: Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language.; Musica e dialogo: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche spe.
- limite visualizzato: sample rate e durata fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
