# Specifica visuale VLM-01

- modello compositivo: vlm_route
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Patch e vision encoder a Projector nel capitolo 56?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: patch visivi e token linguistici in un VLM
- input: immagine, patch, testo e query
- output: token visivi, risposta e grounding
- nodi locali: Patch e vision encoder: Una immagine viene trasformata in patch o feature.; Dual encoder: CLIP allinea immagine e testo con una loss contrastiva.; Projector: Architetture modulari proiettano feature visive nella dimensione del language model.
- limite visualizzato: una risposta linguistica non certifica che il dettaglio sia nell'immagine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
