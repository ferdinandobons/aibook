# Specifica visuale INTEROPERA-01

- modello compositivo: protocol_handshake
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Contratti tra componenti a Agent-to-agent nel capitolo 68?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: un messaggio tra componenti con identità e versione
- input: capability, schema, token e policy
- output: messaggio accettato o errore di protocollo
- nodi locali: Contratti tra componenti: Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, serv.; Model Context Protocol: MCP organizza risorse, prompt e tool esposti da server.; Agent-to-agent: Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agen.
- limite visualizzato: compatibilità sintattica non garantisce semantica o autorizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
