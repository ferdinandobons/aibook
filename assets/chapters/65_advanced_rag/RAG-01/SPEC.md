# Specifica visuale RAG-01

- modello compositivo: multi_query_graph
- domanda principale: Come si passa da «Query transformation» a «Corrective RAG» mantenendo osservabile una query instradata tra retriever e grafo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una query instradata tra retriever e grafo
- input: domanda multi-hop, nodi, archi e documenti
- output: sottoquery, percorso e contesto selezionato
- nodi locali: Query transformation: Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni…; Retrieval adattivo: Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un…; Corrective RAG: Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e…
- limite visualizzato: un router può sbagliare anche quando il generatore è corretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
