# Claim

- `CL-FAMILIES-001`. Encoder-only: Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione.
- `CL-FAMILIES-002`. Decoder-only: Un decoder causale predice token successivi e supporta generazione incrementale.
- `CL-FAMILIES-003`. Encoder-decoder: T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention.
- `CL-FAMILIES-004`. Masked, causal e span corruption: Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss.
- `CL-FAMILIES-005`. Architettura e obiettivo: La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti.
