# Specifica visuale LLM-01

- modello compositivo: behavior_boundary
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale percorso collega Distribuzione del token successivo a Decoding nel capitolo 31?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un prompt e la distribuzione del token successivo
- input: prefisso tokenizzato, esempi e temperatura dichiarati
- output: logits, risposta e confidenza misurabile
- nodi locali: Distribuzione del token successivo: Un LLM autoregressivo produce logits condizionati sul prefisso.; Prompt e dimostrazioni: Istruzioni ed esempi entrano nel contesto senza un optimizer step.; Decoding: Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria.
- limite visualizzato: probabilità, comportamento osservato e correttezza non sono sinonimi
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
