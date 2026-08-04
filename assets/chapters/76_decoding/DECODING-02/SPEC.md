# Specifica visuale DECODING-02

- modello compositivo: sampling_controls
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Constrained decoding da Metriche?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: logits e spazio delle sequenze ammissibili
- input: logits, prefisso, temperatura e vincolo
- output: token scelto, sequenza e metrica di costo
- nodi locali: Constrained decoding: Grammar, automi e schema limitano i token ammessi.; Metriche: Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere.
- limite visualizzato: il decoding modifica la traiettoria, non corregge il modello a monte
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
