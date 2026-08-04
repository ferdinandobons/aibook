# Specifica visuale FOUNDATION-02

- modello compositivo: alignment_space
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale failure o confronto separa Missing modality da Valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: rappresentazioni di modalità differenti
- input: testo, immagine, audio e maschere di modalità
- output: spazio condiviso o output condizionato
- nodi locali: Missing modality: Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autoriz.; Valutazione: Comprensione, retrieval, grounding e generazione richiedono benchmark distinti.
- limite visualizzato: allineamento misurato non equivale a comprensione generale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
