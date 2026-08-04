# Specifica visuale VLM-02

- modello compositivo: grounding_grid
- domanda principale: Quale controllo collega «Q-Former e cross-attention» a «Grounding e hallucination» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: patch visivi e token linguistici in un VLM
- input: immagine, patch, testo e query
- output: token visivi, risposta e grounding
- nodi locali: Q-Former e cross-attention: Query apprese possono estrarre un insieme compatto di feature. Altre architetture…; Grounding e hallucination: Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e…
- limite visualizzato: una risposta linguistica non certifica che il dettaglio sia nell'immagine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
