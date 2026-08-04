# Specifica visuale DECODING-02

- modello compositivo: sampling_controls
- domanda principale: Quale controllo collega «Constrained decoding» a «Metriche» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: logits e spazio delle sequenze ammissibili
- input: logits, prefisso, temperatura e vincolo
- output: token scelto, sequenza e metrica di costo
- nodi locali: Constrained decoding: Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce…; Metriche: Qualità, diversità, latency, token per secondo e probabilità della sequenza devono…
- limite visualizzato: il decoding modifica la traiettoria, non corregge il modello a monte
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
