# Specifica visuale COMPUTE-02

- modello compositivo: search_tree
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale failure o confronto separa Adaptive compute da Metriche costo-qualità?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un budget di compute aggiunto durante l'inferenza
- input: prompt, numero di campioni, token e deadline
- output: risposta, costo, latenza e qualità
- nodi locali: Adaptive compute: Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy.; Metriche costo-qualità: Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti d.
- limite visualizzato: qualità e costo devono essere riportati insieme
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
