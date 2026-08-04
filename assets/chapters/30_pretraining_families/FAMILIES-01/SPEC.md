# Specifica visuale FAMILIES-01

- modello compositivo: architecture_taxonomy
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Encoder-only a Encoder-decoder nel capitolo 30?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una famiglia architetturale legata al proprio obiettivo
- input: sequenza, mask e target di pretraining
- output: rappresentazione o distribuzione predittiva
- nodi locali: Encoder-only: Modelli come BERT usano contesto bidirezionale e obiettivi masked.; Decoder-only: Un decoder causale predice token successivi e supporta generazione incrementale.; Encoder-decoder: T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-at.
- limite visualizzato: architettura e objective non possono essere scambiati senza cambiare il compito
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
