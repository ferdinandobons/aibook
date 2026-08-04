# Audit visuale `INFO-01`

- file esaminato: `candidate-v1.png`
- dimensioni: `1800 × 1000`
- decodifica PNG: superata
- sfondo: bianco puro
- contenimento del testo: superato
- composizione: due righe parallele con ordine logits → softmax → probabilità target → NLL
- esito tecnico: **validata tecnicamente**
- approvazione autoriale: aperta

La revisione raster conferma che il caso corretto e quello errato sono confrontabili senza sovrapposizioni. La differenza di loss è attribuita alla probabilità della classe target, non al solo colore.
