# Specifica visuale PRUNING-02

- modello compositivo: quality_gate
- domanda principale: Quale controllo collega «Pruning» a «Recovery» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: pesi del teacher, student e struttura da comprimere
- input: logits teacher, target, pruning mask e budget
- output: student più piccolo con loss e regressioni misurate
- nodi locali: Pruning: Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione…; Recovery: Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve…
- limite visualizzato: compressione e accuratezza vanno misurate sullo stesso perimetro
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
