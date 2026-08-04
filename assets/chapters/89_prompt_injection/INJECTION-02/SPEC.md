# Specifica visuale INJECTION-02

- modello compositivo: data_control_plane
- domanda principale: Quale controllo collega «Data exfiltration» a «Test e incident response» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: istruzioni e dati che entrano in un sistema con tool
- input: prompt, documento non fidato, tool e scope
- output: azione autorizzata o rifiuto con traccia
- nodi locali: Data exfiltration: Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL…; Test e incident response: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento,…
- limite visualizzato: contenuto recuperato non diventa istruzione privilegiata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
