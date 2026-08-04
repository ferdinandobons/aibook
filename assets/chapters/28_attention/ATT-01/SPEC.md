# ATT-01. Specifica

- ID: `ATT-01`
- File candidato: `candidate-v4.png`
- Domanda unica: perché posizioni diverse devono poter produrre combinazioni diverse degli stessi vettori disponibili?
- Stato prima: un unico vettore di contesto `c` viene riutilizzato senza dipendere dalla posizione corrente.
- Trasformazione nuova: i coefficienti assegnati a `v₁`, `v₂` e `v₃` dipendono dalla query corrente.
- Stato dopo: `q₁` e `q₂` producono due combinazioni distinte, `c₁` e `c₂`.
- Invariante: i tre vettori sorgente non cambiano tra i due casi.
- Confine: la figura non descrive ancora il calcolo di score, scaling e softmax.
- Contenimento: ogni label deve restare integralmente nel proprio box con padding visibile.
- Correzione v4: raster ricostruito dal generatore code-native; q₂ usa `0,05`, `0,15`, `0,80`, coerentemente con l'audit e con la prosa.
- Produzione: composizione visuale iterata e rasterizzazione deterministica tramite `scripts/render_attention_visuals.py`.
- Stato: `validata tecnicamente`, in attesa di revisione autoriale.
- domanda principale: Quale trasformazione centrale rende osservabile «Perché una combinazione fissa non basta» nel capitolo 28?
