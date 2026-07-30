# ATT-02. Specifica

- Domanda unica: come una query produce un output tramite score, scaling, softmax e somma pesata?
- Input: `q=[1,0]`, tre key e tre value, `d_k=d_v=2`.
- Output: `[0,802; 0,599]` con arrotondamento a tre decimali.
- Invariante: i pesi sono non negativi, sommano a 1 e l'output ha dimensione `d_v=2`.
- Provenienza: numeri illustrativi, verificati da `SNIP-ATT-001`.
- Stato: `validata tecnicamente`, in attesa di review autoriale.
