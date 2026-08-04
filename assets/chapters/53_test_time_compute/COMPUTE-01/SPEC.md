# Specifica visuale COMPUTE-01

- modello compositivo: sample_and_vote
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Più compute dopo il training a Tree search nel capitolo 53?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un budget di compute aggiunto durante l'inferenza
- input: prompt, numero di campioni, token e deadline
- output: risposta, costo, latenza e qualità
- nodi locali: Più compute dopo il training: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima.; Best-of-n: Un proposer genera n candidate e un verifier seleziona.; Tree search: Stati parziali vengono espansi, valutati e potati.
- limite visualizzato: qualità e costo devono essere riportati insieme
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
