# Specifica visuale QUANTIZATI-02

- modello compositivo: method_taxonomy
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Weight-only e activation quantization da Metodi per LLM?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un tensore reale e la sua rappresentazione quantizzata
- input: valori, scale, zero-point, dtype e calibrazione
- output: codici, tensore ricostruito, errore e memoria
- nodi locali: Weight-only e activation quantization: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kerne.; Metodi per LLM: I loro contratti non sono intercambiabili.
- limite visualizzato: scala e dominio di calibrazione fanno parte del risultato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
