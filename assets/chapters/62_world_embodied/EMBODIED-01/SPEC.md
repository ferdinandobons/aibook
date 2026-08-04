# Specifica visuale EMBODIED-01

- modello compositivo: embodied_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Modello della dinamica a Embodied perception nel capitolo 62?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato di un agente embodied nel mondo
- input: osservazione, stato, azione e dinamica
- output: azione, stato previsto e risultato fisico
- nodi locali: Modello della dinamica: Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azi.; Planning nel modello: Traiettorie candidate vengono simulate e valutate prima di agire.; Embodied perception: Un agente fisico collega camera, propriocezione, linguaggio e coordinate.
- limite visualizzato: sim-to-real richiede una misura sul sistema reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
