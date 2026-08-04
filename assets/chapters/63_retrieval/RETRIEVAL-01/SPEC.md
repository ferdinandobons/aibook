# Specifica visuale RETRIEVAL-01

- modello compositivo: retrieval_route
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Documenti, query e rilevanza a Dense retrieval nel capitolo 63?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: query e documenti ordinati per rilevanza
- input: query, corpus, termini e indice
- output: ranking con score e documento recuperato
- nodi locali: Documenti, query e rilevanza: Un sistema di retrieval ordina documenti rispetto a una query.; BM25: Tokenizzazione e campi modificano il punteggio.; Dense retrieval: Un bi-encoder mappa query e documenti in vettori e usa una similarità.
- limite visualizzato: rilevanza del ranking e correttezza della risposta sono misure separate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
