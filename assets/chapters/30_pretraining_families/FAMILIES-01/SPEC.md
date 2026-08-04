# Specifica visuale FAMILIES-01

- modello compositivo: architecture_taxonomy
- domanda principale: Come si passa da «Encoder-only» a «Encoder-decoder» mantenendo osservabile una famiglia architetturale legata al proprio obiettivo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una famiglia architetturale legata al proprio obiettivo
- input: sequenza, mask e target di pretraining
- output: rappresentazione o distribuzione predittiva
- nodi locali: Encoder-only: Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per…; Decoder-only: Un decoder causale predice token successivi e supporta generazione incrementale.; Encoder-decoder: T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con…
- limite visualizzato: architettura e objective non possono essere scambiati senza cambiare il compito
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
