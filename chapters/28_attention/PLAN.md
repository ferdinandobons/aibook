# Piano interno. Capitolo 28

## Identità

- `chapter_id`: `CH-P06-ATTENTION`
- Versione candidata: `0.6.0-rc6`
- Stato: candidatura completa in revisione autoriale
- Domanda centrale: come una posizione costruisce una combinazione dei vettori disponibili in funzione dei confronti con le key?
- Oggetto continuo: una frase intuitiva, poi una query e tre coppie key-value con `d_k=d_v=2`
- Stato finale: intuizione linguistica, esempio numerico, pseudocodice, formula, shape, causal mask e implementazione diretta
- Concetti differiti: informazione posizionale, multi-head attention completa, varianti KV, cache e implementazioni hardware-aware

## Prerequisiti

- idea generale di sequenza e vettore;
- prodotto scalare e matrici utili per il secondo livello della spiegazione;
- Python e PyTorch soltanto per eseguire gli snippet.

Il problema e il meccanismo di base devono restare comprensibili anche a chi salta la derivazione e il codice.

## Progressione didattica interna

1. frase concreta e contributi diversi nelle diverse posizioni;
2. limite di un contesto fisso;
3. ruoli di query, key e value;
4. prodotto scalare e score;
5. scaling;
6. softmax;
7. combinazione delle value;
8. pseudocodice;
9. formula matriciale e shape;
10. self-attention, cross-attention e causalità;
11. causal mask;
12. implementazione PyTorch;
13. costo e limiti;
14. ponte verso la multi-head attention.

La versione destinata al lettore raccoglie score, scaling, softmax e somma pesata in un'unica sezione narrativa. Lo scaffold resta verificabile senza determinare il numero dei titoli.

## Superficie editoriale adottata

La candidatura usa otto sezioni principali:

1. perché una combinazione fissa non basta;
2. query, key e value;
3. il calcolo completo su una query;
4. forma matriciale;
5. causal mask;
6. PyTorch;
7. costo, limiti e multi-head;
8. riepilogo.

Regole applicate:

- problema concreto prima dei vettori;
- token, vettore, shape e prodotto scalare spiegati nel punto d'uso;
- query, key e value presentate come ruoli;
- formula compatta dopo esempio e pseudocodice;
- derivazione sulla varianza in un approfondimento;
- dettagli API confinati in nota;
- un solo snippet completo nel corpo;
- costo quadratico spiegato prima con le `n²` celle;
- metadati e audit fuori dal testo del manuale;
- italiano idiomatico e seconda lettura completa.

## Visuali incluse

### `ATT-01`. Perché servono pesi dipendenti dalla query

- File: `assets/chapters/28_attention/ATT-01/candidate-v3.png`.
- Funzione: confrontare contesto fisso e combinazioni dipendenti dalla posizione.
- Correzione: `consumer 1/2` sostituito con `Posizione 1/2`.
- Stato: validata tecnicamente, approvazione autoriale aperta.

### `ATT-02`. Esempio numerico completo

- File: `assets/chapters/28_attention/ATT-02/candidate-v2.png`.
- Funzione: seguire input, score, scaling, softmax, somma pesata e output.
- Stato: validata tecnicamente, approvazione autoriale aperta.

Ogni visuale viene introdotta, attraversata e conclusa nella prosa.

## Codice incluso

- `SNIP-ATT-001`: singola query e valori numerici.
- `SNIP-ATT-002`: formula matriciale e confronto API.
- `SNIP-ATT-003`: causal mask e coefficienti futuri nulli.

Il codice è invariato rispetto alla versione testata. La prosa descrive gli stessi input, lo stesso ordine e gli stessi output.

## Materiale differito

- formula completa della multi-head attention;
- concatenazione e proiezione finale;
- shape per head;
- meccanismo interno di FlashAttention;
- varianti KV e cache.

## Gate di completamento

- [x] termini introdotti dopo i referenti;
- [x] esempio e pseudocodice prima della formula;
- [x] codice dopo il meccanismo;
- [x] varianti come confini o rinvii;
- [x] prosa non frammentata;
- [x] metadati separati dal manuale;
- [x] italiano idiomatico;
- [x] chiarezza per lettore non esperto;
- [x] controllo incrociato visuale ripetuto;
- [x] alt text verificati;
- [ ] approvazione autoriale;
- [ ] rinomina delle figure in `final.png`;
- [ ] congelamento prima dell'aggiornamento di `main`.
