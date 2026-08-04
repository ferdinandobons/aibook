# Specifica visuale DESIGN-01

- modello compositivo: evaluation_matrix
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Decisione e claim a Metriche nel capitolo 83?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un claim valutativo e il protocollo che lo rende misurabile
- input: task, dataset, predizioni, riferimento e metriche
- output: stima, intervallo, errori e decisione
- nodi locali: Decisione e claim: Una valutazione parte dalla decisione che deve sostenere.; Task e dataset: Prompt, input, reference e rubric devono rappresentare l'uso previsto.; Metriche: Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti.
- limite visualizzato: una metrica risponde solo alla domanda per cui è stata progettata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
