# Specifica visuale SAFETY-02

- modello compositivo: least_privilege
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Rollback e audit da Prompt injection?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una decisione agentica su una risorsa reale
- input: input non fidato, tool, scope e approvazione
- output: allow/deny, side effect o rollback auditabile
- nodi locali: Rollback e audit: Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere.; Prompt injection: Contenuti esterni possono tentare di cambiare il piano.
- limite visualizzato: l'enforcement deve stare fuori dal testo generato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
