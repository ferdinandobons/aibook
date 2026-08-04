# Specifica visuale QUANTIZATI-02

- modello compositivo: method_taxonomy
- domanda principale: Quale controllo collega «Weight-only e activation quantization» a «Metodi per LLM» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un tensore reale e la sua rappresentazione quantizzata
- input: valori, scale, zero-point, dtype e calibrazione
- output: codici, tensore ricostruito, errore e memoria
- nodi locali: Weight-only e activation quantization: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i…; Metodi per LLM: GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e…
- limite visualizzato: scala e dominio di calibrazione fanno parte del risultato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
