# Specifica visuale SAFETY-02

- modello compositivo: least_privilege
- domanda principale: Quale controllo collega «Rollback e audit» a «Prompt injection» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una decisione agentica su una risorsa reale
- input: input non fidato, tool, scope e approvazione
- output: allow/deny, side effect o rollback auditabile
- nodi locali: Rollback e audit: Transaction log, snapshot e operazioni compensative permettono di ricostruire e…; Prompt injection: Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di…
- limite visualizzato: l'enforcement deve stare fuori dal testo generato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
