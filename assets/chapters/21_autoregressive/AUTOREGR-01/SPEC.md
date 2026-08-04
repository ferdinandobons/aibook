# Specifica visuale AUTOREGR-01

- modello compositivo: causal_sequence
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Fattorizzare una sequenza a Maschera causale nel capitolo 21?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: la sequenza di token e la distribuzione del prossimo elemento
- input: un prefisso di tre token e una mask causale
- output: logits, token scelto e traiettoria
- nodi locali: Fattorizzare una sequenza: La chain rule scompone la probabilità con un ordine.; Teacher forcing: Durante il training il modello riceve il prefisso reale e predice il passo successivo.; Maschera causale: La causal mask impedisce a una posizione di usare target futuri.
- limite visualizzato: nessuna posizione futura entra nella predizione causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
