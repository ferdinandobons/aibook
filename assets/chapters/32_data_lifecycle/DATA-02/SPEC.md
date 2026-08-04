# Specifica visuale DATA-02

- modello compositivo: dataset_gate
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Deduplicazione e contaminazione da Split, tokenizzazione e manifest?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un record di dataset dalla sorgente al manifest
- input: testo grezzo, metadati, split e digest
- output: record ammesso, conteggi e manifest
- nodi locali: Deduplicazione e contaminazione: Hash esatti e similarità approssimata rilevano forme differenti di duplicazione.; Split, tokenizzazione e manifest: Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato d.
- limite visualizzato: ogni trasformazione deve restare ricostruibile e ordinata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
