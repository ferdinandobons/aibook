# Specifica visuale RAG-02

- modello compositivo: citation_trace
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Attribution da Valutazione end-to-end?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la pipeline che collega query, contesto e risposta
- input: query, chunk, fonti e prompt
- output: risposta con evidenza e score end-to-end
- nodi locali: Attribution: Una risposta supportata deve essere collegabile a passaggi recuperati.; Valutazione end-to-end: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono ess.
- limite visualizzato: contesto recuperato e testo generato devono restare distinguibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
