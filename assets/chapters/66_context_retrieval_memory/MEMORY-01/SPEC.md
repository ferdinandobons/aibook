# Specifica visuale MEMORY-01

- modello compositivo: memory_layers
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale percorso collega Tre risorse differenti a Quando recuperare nel capitolo 66?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la decisione tra contesto, retrieval e memoria
- input: segmento, query, budget e durata
- output: contesto scelto, memoria aggiornata e costo
- nodi locali: Tre risorse differenti: Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiorna.; Quando usare il contesto: Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e cost.; Quando recuperare: Retrieval seleziona un sottoinsieme aggiornabile e attribuibile.
- limite visualizzato: memoria persistente e contesto temporaneo hanno politiche diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
