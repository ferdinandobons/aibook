# Specifica visuale SAFETY-01

- modello compositivo: trust_boundary
- domanda principale: Come si passa da «Least privilege» a «Human approval» mantenendo osservabile una decisione agentica su una risorsa reale?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una decisione agentica su una risorsa reale
- input: input non fidato, tool, scope e approvazione
- output: allow/deny, side effect o rollback auditabile
- nodi locali: Least privilege: Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere…; Sandbox: Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse…; Human approval: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario…
- limite visualizzato: l'enforcement deve stare fuori dal testo generato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
