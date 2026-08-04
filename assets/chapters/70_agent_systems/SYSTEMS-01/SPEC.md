# Specifica visuale SYSTEMS-01

- modello compositivo: agent_graph
- domanda principale: Come si passa da «Browser agent» a «Code agent» mantenendo osservabile una traiettoria composta da agenti e strumenti?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una traiettoria composta da agenti e strumenti
- input: task, ruoli, browser, codice e handoff
- output: risultato con responsabilità e log per componente
- nodi locali: Browser agent: L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da…; Computer use: Screenshot, coordinate e azioni di input formano un loop percettivo. Risoluzione, focus…; Code agent: Repository, test, shell e diff definiscono l'ambiente. Modifiche devono essere limitate,…
- limite visualizzato: più agenti ampliano anche superficie e costo dell'errore
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
