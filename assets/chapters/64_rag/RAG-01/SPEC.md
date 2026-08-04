# Specifica visuale RAG-01

- modello compositivo: rag_route
- domanda principale: Come si passa da «Una pipeline in due fasi» a «Prompt con fonti» mantenendo osservabile la pipeline che collega query, contesto e risposta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la pipeline che collega query, contesto e risposta
- input: query, chunk, fonti e prompt
- output: risposta con evidenza e score end-to-end
- nodi locali: Una pipeline in due fasi: Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata…; Chunking: Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un…; Prompt con fonti: Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare,…
- limite visualizzato: contesto recuperato e testo generato devono restare distinguibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
