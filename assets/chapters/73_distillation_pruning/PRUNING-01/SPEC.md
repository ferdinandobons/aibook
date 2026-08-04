# Specifica visuale PRUNING-01

- modello compositivo: distill_prune
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale percorso collega Teacher e student a Sequence distillation nel capitolo 73?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: pesi del teacher, student e struttura da comprimere
- input: logits teacher, target, pruning mask e budget
- output: student più piccolo con loss e regressioni misurate
- nodi locali: Teacher e student: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi p.; Temperature e loss: Una temperatura più alta rivela relazioni tra classi o token.; Sequence distillation: Per modelli generativi, risposte del teacher diventano un nuovo dataset.
- limite visualizzato: compressione e accuratezza vanno misurate sullo stesso perimetro
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
