# Specifica visuale MOE-02

- modello compositivo: capacity_gate
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Expert parallelism da Parametri totali e attivi?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v45.png
- oggetto osservato: token e assegnazioni del router agli esperti
- input: logits del router, top-k e capacità per esperto
- output: carico, token restituiti e costo attivo
- nodi locali: Expert parallelism: Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti di.; Parametri totali e attivi: Un MoE può avere molti parametri totali e pochi parametri attivi per token.
- limite visualizzato: parametri totali e parametri attivi non sono la stessa quantità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
