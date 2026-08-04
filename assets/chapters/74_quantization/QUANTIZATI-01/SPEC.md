# Specifica visuale QUANTIZATI-01

- modello compositivo: quantization_map
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Scala e zero point a QAT nel capitolo 74?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un tensore reale e la sua rappresentazione quantizzata
- input: valori, scale, zero-point, dtype e calibrazione
- output: codici, tensore ricostruito, errore e memoria
- nodi locali: Scala e zero point: Una mappa affine converte valori floating point in interi.; PTQ: Post-training quantization usa calibration senza riaddestrare completamente.; QAT: Quantization-aware training simula arrotondamento e clipping durante il training per adatt.
- limite visualizzato: scala e dominio di calibrazione fanno parte del risultato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
