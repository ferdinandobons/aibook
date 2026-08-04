# Specifica visuale UPDATE-01

- modello compositivo: model_edit
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Continued adaptation a TIES e DARE nel capitolo 54?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: versioni di pesi e modifiche localizzate del modello
- input: base model, delta, task e rollback point
- output: versione nuova, diff e test di regressione
- nodi locali: Continued adaptation: Nuovi dati e obiettivi aggiornano il checkpoint.; Task arithmetic: Differenze tra checkpoint possono essere combinate come vettori.; TIES e DARE: Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione.
- limite visualizzato: un merge senza valutazione può introdurre regressioni invisibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
