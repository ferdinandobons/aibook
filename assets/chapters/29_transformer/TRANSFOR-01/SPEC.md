# Specifica visuale TRANSFOR-01

- modello compositivo: transformer_stack
- domanda principale: Come si passa da «La mappa completa» a «Decoder» mantenendo osservabile lo stato nascosto che attraversa il blocco Transformer?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato nascosto che attraversa il blocco Transformer
- input: tokenizzati di shape [batch, length] e vettori [batch, length, d]
- output: stato contestuale e logits
- nodi locali: La mappa completa: Il Transformer combina embedding, posizione, attention, feed-forward, residual e…; Encoder: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le…; Decoder: Il decoder usa self-attention causale e, nelle architetture encoder-decoder,…
- limite visualizzato: mask, shape e percorso residuale devono essere compatibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
