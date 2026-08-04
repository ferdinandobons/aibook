# Specifica visuale SYSTEMS-01

- modello compositivo: agent_graph
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale percorso collega Browser agent a Code agent nel capitolo 70?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una traiettoria composta da agenti e strumenti
- input: task, ruoli, browser, codice e handoff
- output: risultato con responsabilità e log per componente
- nodi locali: Browser agent: L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istru.; Computer use: Screenshot, coordinate e azioni di input formano un loop percettivo.; Code agent: Repository, test, shell e diff definiscono l'ambiente.
- limite visualizzato: più agenti ampliano anche superficie e costo dell'errore
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
