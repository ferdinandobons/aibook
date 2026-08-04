# ATT-02. Specifica

- ID: `ATT-02`
- File candidato: `candidate-v2.png`
- Domanda unica: come una query produce un output tramite score, scaling, softmax e somma pesata?
- Input: `q=[1,0]`, tre key e tre value, `d_k=d_v=2`.
- Sequenza delle operazioni: `qK^T`, divisione per `sqrt(2)`, softmax, combinazione delle value.
- Output: `[0,802; 0,599]` con arrotondamento a tre decimali.
- Invariante: i pesi sono non negativi, sommano a 1 e l'output ha dimensione `d_v=2`.
- Provenienza: numeri illustrativi, verificati da `SNIP-ATT-001` e ricalcolo indipendente.
- Contenimento: ogni valore, formula e label deve restare integralmente nel proprio pannello o box.
- Produzione: composizione iterata con image generation; testo, valori e collegamenti rasterizzati con `scripts/render_attention_visuals.py`.
- Stato: `validata tecnicamente`, in attesa di revisione autoriale.
- domanda principale: Quale confronto o limite chiarisce «I tre ruoli: query, key e value»?
