# Specifica visuale RAG-02

- modello compositivo: citation_trace
- domanda principale: Quale controllo collega «Attribution» a «Valutazione end-to-end» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la pipeline che collega query, contesto e risposta
- input: query, chunk, fonti e prompt
- output: risposta con evidenza e score end-to-end
- nodi locali: Attribution: Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione…; Valutazione end-to-end: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono…
- limite visualizzato: contesto recuperato e testo generato devono restare distinguibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
