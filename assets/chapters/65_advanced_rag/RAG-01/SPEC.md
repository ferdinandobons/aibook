# Specifica visuale RAG-01

- modello compositivo: multi_query_graph
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale percorso collega Query transformation a Corrective RAG nel capitolo 65?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una query instradata tra retriever e grafo
- input: domanda multi-hop, nodi, archi e documenti
- output: sottoquery, percorso e contesto selezionato
- nodi locali: Query transformation: Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval.; Retrieval adattivo: Il sistema decide se recuperare, quante volte e con quale sorgente.; Corrective RAG: Documenti vengono valutati, filtrati o sostituiti prima della generazione.
- limite visualizzato: un router può sbagliare anche quando il generatore è corretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
