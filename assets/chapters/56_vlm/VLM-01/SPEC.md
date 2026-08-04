# Specifica visuale VLM-01

- modello compositivo: vlm_route
- domanda principale: Come si passa da «Patch e vision encoder» a «Projector» mantenendo osservabile patch visivi e token linguistici in un VLM?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: patch visivi e token linguistici in un VLM
- input: immagine, patch, testo e query
- output: token visivi, risposta e grounding
- nodi locali: Patch e vision encoder: Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e…; Dual encoder: CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano…; Projector: Architetture modulari proiettano feature visive nella dimensione del language model. Il…
- limite visualizzato: una risposta linguistica non certifica che il dettaglio sia nell'immagine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
