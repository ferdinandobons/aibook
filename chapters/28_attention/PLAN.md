# Piano interno. Capitolo 28

## Identità

- `chapter_id`: `CH-P06-ATTENTION`
- Versione candidata: `0.4.0-rc4`
- Stato: review editoriale superata, controllo visuale riaperto
- Domanda centrale: come una posizione costruisce una combinazione dei vettori disponibili in funzione dei confronti con le key?
- Oggetto continuo: una query e tre coppie key-value con `d_k=d_v=2`.
- Stato finale: esempio numerico, pseudocodice, formula, shape, causal mask, implementazione diretta e confronto API.
- Concetti differiti: informazione posizionale, multi-head attention, varianti KV, cache e implementazioni hardware-aware.

## Progressione didattica interna

1. limite di un contesto fisso;
2. combinazioni diverse per posizioni diverse;
3. ruoli di query, key e value;
4. prodotti scalari e score;
5. scaling;
6. softmax;
7. combinazione delle value;
8. pseudocodice;
9. formula matriciale e shape;
10. self-attention, cross-attention e causalità;
11. causal mask;
12. implementazione PyTorch;
13. complessità e confini;
14. ponte verso la multi-head attention.

La versione destinata al lettore raccoglie i passaggi da 4 a 7 in un'unica sezione narrativa. Lo scaffold resta verificabile senza determinare il numero dei titoli.

## Superficie editoriale adottata

La versione `0.4.0-rc4` usa otto sezioni principali:

1. perché una combinazione fissa non basta;
2. query, key e value;
3. il calcolo completo su una query;
4. forma matriciale;
5. causal mask;
6. PyTorch;
7. costo, limiti e multi-head;
8. riepilogo.

Regole applicate:

- metadati in commento non renderizzato;
- nessun registro di approvazione nel manuale;
- score, scaling, softmax e somma pesata in un unico movimento;
- identità numerica di `K` e `V` dichiarata come scelta illustrativa;
- dettagli API raccolti in una nota;
- fonti e artefatti condensati;
- review linguistica e lettura ad alta voce.

## Visuali incluse

- `ATT-01`: differenza tra contesto fisso e coefficienti dipendenti dalla posizione.
- `ATT-02`: esempio numerico completo per una query.

Ogni visuale viene introdotta, attraversata e conclusa nella prosa.

Controlli riaperti:

- coerenza delle label con il nuovo lessico;
- eventuale sostituzione di `consumer 1/2` con `posizione 1/2` in `ATT-01`;
- leggibilità nel nuovo flusso;
- approvazione autoriale.

## Codice incluso

- `SNIP-ATT-001`: singola query e valori numerici.
- `SNIP-ATT-002`: formula matriciale e confronto API.
- `SNIP-ATT-003`: causal mask e coefficienti futuri nulli.

Il codice è invariato rispetto alla versione testata. La prosa è stata riallineata allo stesso ordine e agli stessi output.

## Materiale differito

- formula completa della multi-head attention;
- concatenazione e proiezione finale;
- shape per head;
- meccanismo interno di FlashAttention;
- varianti KV e cache.

## Gate di completamento

- termini introdotti dopo i referenti;
- esempio e pseudocodice prima della formula;
- codice dopo il meccanismo;
- varianti come confini o rinvii;
- prosa non frammentata;
- metadati separati dal manuale;
- italiano idiomatico;
- lettura ad alta voce superata;
- review `EDIT-ATT-01` e `EDIT-ATT-02` registrate;
- controllo incrociato visuale ripetuto;
- revisione autoriale prima del congelamento.
