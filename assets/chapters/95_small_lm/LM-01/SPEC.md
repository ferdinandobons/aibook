# Specifica visuale LM-01

- modello compositivo: small_lm_stack
- domanda principale: Come si passa da «Corpus e tokenizer» a «Training» mantenendo osservabile un piccolo language model dalla stringa ai logits?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un piccolo language model dalla stringa ai logits
- input: corpus, tokenizer, batch di sequenze e target
- output: logits, loss, token generati e checkpoint
- nodi locali: Corpus e tokenizer: Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split…; Decoder Transformer: Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati…; Training: AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o…
- limite visualizzato: tokenizer, mask, target shift e sampling devono essere coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
