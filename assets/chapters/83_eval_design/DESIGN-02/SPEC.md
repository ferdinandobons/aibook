# Specifica visuale DESIGN-02

- modello compositivo: selection_funnel
- domanda principale: Quale controllo collega «Giudici modello» a «Report» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un claim valutativo e il protocollo che lo rende misurabile
- input: task, dataset, predizioni, riferimento e metriche
- output: stima, intervallo, errori e decisione
- nodi locali: Giudici modello: LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e…; Report: Intervalli, fallimenti, costi e limiti accompagnano il punteggio. Una leaderboard non…
- limite visualizzato: una metrica risponde solo alla domanda per cui è stata progettata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
