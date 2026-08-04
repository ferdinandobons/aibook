# Specifica visuale TRANSFOR-01

- modello compositivo: transformer_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale percorso collega La mappa completa a Decoder nel capitolo 29?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato nascosto che attraversa il blocco Transformer
- input: tokenizzati di shape [batch, length] e vettori [batch, length, d]
- output: stato contestuale e logits
- nodi locali: La mappa completa: Ogni componente mantiene un contratto di shape.; Encoder: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizio.; Decoder: Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attenti.
- limite visualizzato: mask, shape e percorso residuale devono essere compatibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
