# Specifica visuale RAG-01

- modello compositivo: rag_route
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Una pipeline in due fasi a Prompt con fonti nel capitolo 64?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la pipeline che collega query, contesto e risposta
- input: query, chunk, fonti e prompt
- output: risposta con evidenza e score end-to-end
- nodi locali: Una pipeline in due fasi: Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata su.; Chunking: Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto.; Prompt con fonti: Documenti, istruzioni e domanda devono avere confini espliciti.
- limite visualizzato: contesto recuperato e testo generato devono restare distinguibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
