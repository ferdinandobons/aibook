# Specifica visuale RAG-02

- modello compositivo: reranking_funnel
- domanda principale: Quale controllo collega «Graph RAG» a «RAG agentico» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una query instradata tra retriever e grafo
- input: domanda multi-hop, nodi, archi e documenti
- output: sottoquery, percorso e contesto selezionato
- nodi locali: Graph RAG: Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da…; RAG agentico: Un agente può pianificare retrieval successivi. Più step aumentano copertura e…
- limite visualizzato: un router può sbagliare anche quando il generatore è corretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
