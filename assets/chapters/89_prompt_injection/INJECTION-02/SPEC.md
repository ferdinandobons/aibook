# Specifica visuale INJECTION-02

- modello compositivo: data_control_plane
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Data exfiltration da Test e incident response?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: istruzioni e dati che entrano in un sistema con tool
- input: prompt, documento non fidato, tool e scope
- output: azione autorizzata o rifiuto con traccia
- nodi locali: Data exfiltration: Segreti, memoria e risultati dei tool devono essere separati per scope.; Test e incident response: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, cont.
- limite visualizzato: contenuto recuperato non diventa istruzione privilegiata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
