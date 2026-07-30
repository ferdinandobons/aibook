# Piano interno. Capitolo 28

## Identità

- `chapter_id`: `CH-P06-ATTENTION`
- Versione candidata: `0.5.0-rc5`
- Stato: review di accessibilità per lettore non esperto superata, controllo visuale riaperto
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

1. esempio linguistico sulla frase `Il pacco non è arrivato`;
2. token spiegato come parola o parte di parola;
3. vettore spiegato come lista di numeri;
4. limite di una combinazione fissa;
5. combinazioni diverse per posizioni diverse;
6. ruoli di query, key e value;
7. prodotto scalare e score;
8. scaling con motivazione intuitiva;
9. softmax come trasformazione in coefficienti che sommano a uno;
10. combinazione delle value;
11. pseudocodice;
12. formula matriciale e shape;
13. self-attention, cross-attention e causalità;
14. causal mask;
15. implementazione PyTorch minima;
16. complessità e confini;
17. ponte verso la multi-head attention.

La versione destinata al lettore raccoglie i passaggi da 7 a 10 in un'unica sezione narrativa. La derivazione sulla varianza è un approfondimento e non interrompe il percorso principale.

## Superficie editoriale adottata

La versione `0.5.0-rc5` usa otto sezioni principali:

1. perché una combinazione fissa non basta;
2. query, key e value;
3. il calcolo completo su una query;
4. forma matriciale;
5. causal mask;
6. PyTorch;
7. costo, limiti e multi-head;
8. riepilogo.

Regole applicate:

- apertura con una frase naturale prima dei vettori;
- definizione immediata di token, vettore e shape;
- query, key e value presentate come ruoli, non come tre oggetti misteriosi;
- prodotto scalare spiegato come moltiplicazione e somma;
- softmax spiegata in parole prima della formula;
- derivazione sul fattore di scala separata come approfondimento;
- rimosso dal flusso principale il caveat sul dropout dopo la softmax;
- formule matriciali introdotte come compressione di passaggi già eseguiti;
- self-attention, cross-attention e causalità spiegate con tre frasi distinte;
- un solo snippet mostrato integralmente nel capitolo;
- confronti API e mask mantenuti negli artefatti del codice e richiamati in prosa;
- costo quadratico spiegato prima come numero di celle `n^2`;
- review linguistica e lettura lineare senza dipendere dalle formule.

## Visuali incluse

- `ATT-01`: differenza tra contesto fisso e coefficienti dipendenti dalla posizione.
- `ATT-02`: esempio numerico completo per una query.

Ogni visuale viene introdotta, attraversata e conclusa nella prosa.

Controlli riaperti:

- coerenza delle label con il lessico accessibile;
- eventuale sostituzione di `consumer 1/2` con `posizione 1/2` in `ATT-01`;
- leggibilità del nuovo testo numerico di `ATT-02` rispetto alla prosa;
- approvazione autoriale.

## Codice incluso

- `SNIP-ATT-001`: singola query e valori numerici, mostrato nel capitolo.
- `SNIP-ATT-002`: formula matriciale e confronto API, richiamato dal capitolo.
- `SNIP-ATT-003`: causal mask e coefficienti futuri nulli, richiamato dal capitolo.

Il codice è invariato rispetto alla versione testata. La superficie del capitolo mostra soltanto il blocco necessario a riconoscere score, softmax e prodotto con `V`.

## Materiale differito

- formula completa della multi-head attention;
- concatenazione e proiezione finale;
- shape per head;
- meccanismo interno di FlashAttention;
- varianti KV e cache;
- dettagli completi sulle differenze tra convenzioni booleane delle API.

## Gate di completamento

- problema intuitivo prima della rappresentazione vettoriale;
- termini introdotti dopo i referenti;
- ogni simbolo accompagnato da un significato in parole;
- esempio e pseudocodice prima della formula;
- matematica avanzata separata dal percorso minimo;
- codice dopo il meccanismo;
- varianti come confini o rinvii;
- prosa non frammentata;
- metadati separati dal manuale;
- italiano idiomatico;
- possibilità di spiegare l'attention senza formula prima di formalizzarla;
- review `EDIT-ATT-01` fino a `EDIT-ATT-04` registrate;
- controllo incrociato visuale ripetuto;
- revisione autoriale prima del congelamento.
