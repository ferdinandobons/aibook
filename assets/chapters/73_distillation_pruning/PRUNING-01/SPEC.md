# Specifica visuale PRUNING-01

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Distillazione, pruning e recovery. L'input è logits teacher, target, pruning mask e budget, l'output è student più piccolo con loss e regressioni misurate; il vincolo da controllare è che compressione e accuratezza vanno misurate sullo stesso perimetro
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: Teacher e student; 2: Temperature e loss; 3: Sequence distillation; 4: Pruning; 5: Recovery
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: compressione e accuratezza vanno misurate sullo stesso perimetro
- fonti collegate: SRC-73-001 ... SRC-73-004
- alt text: Diagramma PRUNING-01 del Capitolo 73, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Distillazione, pruning e recovery. L'input è logits teacher, target, pruning mask e budget, l'output è student più piccolo con loss e regressioni misurate; il vincolo da controllare è che compressione e accuratezza vanno misurate sullo stesso perimetro La composizione usa i passaggi Teacher e student, Temperature e loss, Sequence distillation, Pruning, Recovery.
