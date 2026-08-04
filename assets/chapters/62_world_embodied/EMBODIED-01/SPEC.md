# Specifica visuale EMBODIED-01

- modello compositivo: embodied_loop
- domanda principale: Come si passa da «Modello della dinamica» a «Embodied perception» mantenendo osservabile lo stato di un agente embodied nel mondo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato di un agente embodied nel mondo
- input: osservazione, stato, azione e dinamica
- output: azione, stato previsto e risultato fisico
- nodi locali: Modello della dinamica: Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e…; Planning nel modello: Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello…; Embodied perception: Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e…
- limite visualizzato: sim-to-real richiede una misura sul sistema reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
