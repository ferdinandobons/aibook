# Specifica visuale QUANTIZATI-01

- modello compositivo: quantization_map
- domanda principale: Come si passa da «Scala e zero point» a «QAT» mantenendo osservabile un tensore reale e la sua rappresentazione quantizzata?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un tensore reale e la sua rappresentazione quantizzata
- input: valori, scale, zero-point, dtype e calibrazione
- output: codici, tensore ricostruito, errore e memoria
- nodi locali: Scala e zero point: Una mappa affine converte valori floating point in interi. La granularità per tensor o…; PTQ: Post-training quantization usa calibration senza riaddestrare completamente. La…; QAT: Quantization-aware training simula arrotondamento e clipping durante il training per…
- limite visualizzato: scala e dominio di calibrazione fanno parte del risultato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
