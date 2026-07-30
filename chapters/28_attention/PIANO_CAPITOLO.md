# Capitolo 28. Piano di esecuzione

## Titolo

**Il meccanismo di attention**

## Profilo

Componente, con sezioni di tecnica e implementazione.

## Oggetto continuo

Il capitolo userà una breve sequenza italiana dichiarata come **illustrativa** all’inizio della spiegazione. La sequenza verrà scelta per rendere visibili dipendenze diverse tra le posizioni, senza dipendere da file esterni o da una frase canonica di un altro progetto.

La stessa sequenza tokenizzata verrà portata attraverso:

1. embedding di input già noti;
2. costruzione di una query;
3. confronto con le key;
4. scaling;
5. mask, quando applicabile;
6. softmax;
7. combinazione pesata delle value;
8. ripetizione per tutte le query;
9. suddivisione in più head;
10. concatenazione e proiezione finale.

## Stato prima

Il lettore sa che una sequenza può essere rappresentata come un tensor di embedding, ma non dispone ancora di un’operazione che costruisca per ogni posizione una combinazione dipendente dalle altre posizioni.

## Gap

Una singola rappresentazione fissa o una trasformazione indipendente per posizione non permette di selezionare contributi diversi in funzione della query corrente.

## Stato dopo

Il lettore può calcolare, implementare e localizzare scaled dot-product attention e multi-head attention. Può inoltre distinguere self-attention, cross-attention e causal self-attention.

## Invarianti principali

- il numero di query determina il numero di righe dell’output;
- ogni riga dei pesi dopo softmax somma a 1, salvo dettagli numerici;
- una mask cambia quali score possono contribuire, non il numero di query;
- l’output di una singola head è una combinazione lineare delle righe di `V`;
- multi-head attention concatena output di head separate prima della proiezione finale.

## Confini

Il capitolo non spiegherà ancora in modo completo:

- positional encoding;
- residual connection;
- LayerNorm o RMSNorm;
- feed-forward network;
- KV cache end-to-end;
- FlashAttention a livello di kernel;
- MLA e compressione latente della KV cache.

Questi elementi saranno nominati solo dove servono a localizzare l’attention nel sistema più grande.

## Storyboard delle visuali

### ATT-01. Perché serve una selezione dipendente dalla query

- Tipo: process/comparison
- Domanda: perché una trasformazione uguale per tutte le posizioni non basta per produrre combinazioni dipendenti dalla query?
- Nuovo concetto: insieme di pesi dipendente dalla query.

### ATT-02. Una query, più key, più value

- Tipo: matrix-operation
- Domanda: come una query produce una singola riga di output?
- Nuovo concetto: score, softmax e somma pesata.

### ATT-03. Scaled dot-product attention con shape

- Tipo: tensor-shape
- Domanda: come si generalizza il calcolo a tutte le query?
- Nuovo concetto: operazioni matriciali `QK^T`, scaling, softmax e prodotto con `V`.

### ATT-04. Causal mask

- Tipo: matrix-operation
- Domanda: come si impedisce a una posizione di usare token futuri?
- Nuovo concetto: valori non ammessi portati a `-inf` prima della softmax.

### ATT-05. Multi-head attention

- Tipo: architecture/tensor-shape
- Domanda: come si eseguono proiezioni separate e si ricompone l’output?
- Nuovo concetto: split in head, attention parallela, concat e `W_O`.

### ATT-06. Self, cross e causal self-attention

- Tipo: comparison
- Domanda: da quali tensor provengono query, key e value nei tre casi?
- Nuovo concetto: differenza controllata nella provenienza degli input.

### ATT-07. MHA, MQA e GQA

- Tipo: comparison
- Domanda: quali head condividono key e value?
- Nuovo concetto: condivisione KV come trade-off di inference.

### ATT-08. Baseline e calcolo IO-aware

- Tipo: process
- Domanda: perché due implementazioni matematicamente esatte possono avere costi di memoria diversi?
- Nuovo concetto: materializzazione degli intermedi rispetto al tiling.

## Implementazioni previste

1. NumPy o PyTorch elementare per una singola query.
2. PyTorch da zero per batch e più head.
3. `torch.nn.functional.scaled_dot_product_attention`.
4. `torch.nn.MultiheadAttention` come confronto API.
5. Test di equivalenza numerica entro tolleranza.
6. Test delle mask e degli invarianti di shape.
7. Benchmark solo se ambiente, backend e hardware possono essere registrati.

## Protocollo di revisione delle visuali

Ogni visuale `ATT-01`–`ATT-08` seguirà almeno un ciclo di generazione e audit. La prima bozza non sarà inserita nel capitolo. Per ogni versione verranno controllati formula, shape, valori, sorgente e destinazione delle frecce, incroci, ordine di lettura, densità, leggibilità e coerenza con la prosa. Le versioni respinte verranno rigenerate o modificate. Nel repository entreranno la versione approvata e il relativo registro di audit.
