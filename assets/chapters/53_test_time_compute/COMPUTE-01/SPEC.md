# Specifica visuale COMPUTE-01

- modello compositivo: sample_and_vote
- domanda principale: Come si passa da «Più compute dopo il training» a «Tree search» mantenendo osservabile un budget di compute aggiunto durante l'inferenza?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un budget di compute aggiunto durante l'inferenza
- input: prompt, numero di campioni, token e deadline
- output: risposta, costo, latenza e qualità
- nodi locali: Più compute dopo il training: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca…; Best-of-n: Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla…; Tree search: Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget…
- limite visualizzato: qualità e costo devono essere riportati insieme
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
