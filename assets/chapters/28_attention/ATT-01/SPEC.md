# ATT-01. Specifica

- ID: `ATT-01`
- File candidato: `candidate-v2.png`
- Domanda unica: perché query diverse devono poter produrre combinazioni diverse delle stesse value?
- Stato prima: un unico vettore di contesto `c` viene riutilizzato senza dipendere dalla query.
- Trasformazione nuova: i coefficienti assegnati a `v₁`, `v₂` e `v₃` dipendono dalla query corrente.
- Stato dopo: `q₁` e `q₂` producono due combinazioni distinte, `c₁` e `c₂`.
- Invariante: le tre value disponibili non cambiano tra i due casi.
- Confine: la figura non descrive ancora il calcolo di score, scaling e softmax.
- Contenimento: ogni label deve restare integralmente nel proprio box con padding visibile.
- Produzione: composizione iterata con image generation; testo e collegamenti rasterizzati con `scripts/render_attention_visuals.py`.
- Stato: `validata tecnicamente`, in attesa di revisione autoriale.
