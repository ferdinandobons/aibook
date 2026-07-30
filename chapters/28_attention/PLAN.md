# Piano del capitolo 28

- `chapter_id`: `CH-P06-ATTENTION`
- Domanda centrale: come una query costruisce una combinazione delle value dipendente dalla compatibilità con le key?
- Oggetto continuo: `q`, `K`, `V` con `d_k=d_v=2`.
- Stato finale: formula, shape, mask, codice da zero, API e passaggio a multi-head.
- Concetti differiti: posizione, kernel IO-aware, cache e varianti KV.

## Visuali incluse nella candidatura

- `ATT-01`: requisito dei pesi dipendenti dalla query.
- `ATT-02`: esempio numerico per una query.

## Visuali non incluse

- flusso matriciale completo: non necessario nella candidatura perché formula, tabella shape e codice coprono la relazione senza aggiungere ambiguità;
- causal mask: coperta da matrice e snippet, candidata a visuale dopo feedback dell'autore;
- multi-head: candidata al capitolo successivo o a una seconda revisione del pilota.

## Codice

- `SNIP-ATT-001`: singola query.
- `SNIP-ATT-002`: formula matriciale e API.
- `SNIP-ATT-003`: causal mask.
- `SNIP-ATT-004`: shape multi-head.
