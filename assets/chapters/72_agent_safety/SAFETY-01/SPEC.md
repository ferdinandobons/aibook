# Specifica visuale SAFETY-01

- modello compositivo: trust_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale percorso collega Least privilege a Human approval nel capitolo 72?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una decisione agentica su una risorsa reale
- input: input non fidato, tool, scope e approvazione
- output: allow/deny, side effect o rollback auditabile
- nodi locali: Least privilege: Ogni tool riceve soltanto gli scope necessari.; Sandbox: Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitat.; Human approval: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario esplic.
- limite visualizzato: l'enforcement deve stare fuori dal testo generato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
