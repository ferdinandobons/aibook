# Specifica visuale DECODING-01

- modello compositivo: draft_verify
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Draft e target a Speedup nel capitolo 77?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: draft e target durante il decoding speculativo
- input: token proposti, logits draft e logits target
- output: token accettati, velocità e distribuzione preservata
- nodi locali: Draft e target: Un modello economico propone più token; il modello target li verifica in parallelo.; Acceptance: La regola di accettazione conserva esattamente la distribuzione target nel metodo speculat.; Speedup: Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware.
- limite visualizzato: lo speedup richiede verifica senza cambiare il contratto di output
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
