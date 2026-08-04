# Specifica visuale LM-02

- modello compositivo: training_evidence
- domanda principale: Quale controllo collega «Sampling» a «Limiti» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un piccolo language model dalla stringa ai logits
- input: corpus, tokenizer, batch di sequenze e target
- output: logits, loss, token generati e checkpoint
- nodi locali: Sampling: Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria.; Limiti: Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende…
- limite visualizzato: tokenizer, mask, target shift e sampling devono essere coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
