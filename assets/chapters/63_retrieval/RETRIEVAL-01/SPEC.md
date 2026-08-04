# Specifica visuale RETRIEVAL-01

- modello compositivo: retrieval_route
- domanda principale: Come si passa da «Documenti, query e rilevanza» a «Dense retrieval» mantenendo osservabile query e documenti ordinati per rilevanza?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: query e documenti ordinati per rilevanza
- input: query, corpus, termini e indice
- output: ranking con score e documento recuperato
- nodi locali: Documenti, query e rilevanza: Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal…; BM25: La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione…; Dense retrieval: Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento…
- limite visualizzato: rilevanza del ranking e correttezza della risposta sono misure separate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
