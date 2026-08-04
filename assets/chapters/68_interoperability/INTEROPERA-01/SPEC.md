# Specifica visuale INTEROPERA-01

- modello compositivo: protocol_handshake
- domanda principale: Come si passa da «Contratti tra componenti» a «Agent-to-agent» mantenendo osservabile un messaggio tra componenti con identità e versione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: un messaggio tra componenti con identità e versione
- input: capability, schema, token e policy
- output: messaggio accettato o errore di protocollo
- nodi locali: Contratti tra componenti: Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client,…; Model Context Protocol: MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il…; Agent-to-agent: Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra…
- limite visualizzato: compatibilità sintattica non garantisce semantica o autorizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
