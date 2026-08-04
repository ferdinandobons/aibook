# Specifica visuale MEMORY-01

- modello compositivo: memory_layers
- domanda principale: Come si passa da «Tre risorse differenti» a «Quando recuperare» mantenendo osservabile la decisione tra contesto, retrieval e memoria?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la decisione tra contesto, retrieval e memoria
- input: segmento, query, budget e durata
- output: contesto scelto, memoria aggiornata e costo
- nodi locali: Tre risorse differenti: Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e…; Quando usare il contesto: Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e…; Quando recuperare: Retrieval seleziona un sottoinsieme aggiornabile e attribuibile. Può fallire per query,…
- limite visualizzato: memoria persistente e contesto temporaneo hanno politiche diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
