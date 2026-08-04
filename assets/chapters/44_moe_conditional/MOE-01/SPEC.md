# Specifica visuale MOE-01

- modello compositivo: expert_router
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale percorso collega Router top-k a Load balancing nel capitolo 44?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v45.png
- oggetto osservato: token e assegnazioni del router agli esperti
- input: logits del router, top-k e capacità per esperto
- output: carico, token restituiti e costo attivo
- nodi locali: Router top-k: Un router assegna probabilità agli esperti e attiva un sottoinsieme per token.; Capacità: Ogni esperto riceve un limite di token.; Load balancing: Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione.
- limite visualizzato: parametri totali e parametri attivi non sono la stessa quantità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
