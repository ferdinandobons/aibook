# Specifica visuale DECODING-01

- modello compositivo: decoding_tree
- domanda principale: Come si passa da «Greedy e beam search» a «Penalità e stop» mantenendo osservabile logits e spazio delle sequenze ammissibili?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: logits e spazio delle sequenze ammissibili
- input: logits, prefisso, temperatura e vincolo
- output: token scelto, sequenza e metrica di costo
- nodi locali: Greedy e beam search: Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e…; Sampling: Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e…; Penalità e stop: Repetition penalty, stop sequence e minimum length intervengono in punti differenti e…
- limite visualizzato: il decoding modifica la traiettoria, non corregge il modello a monte
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
