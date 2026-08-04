<!--
chapter_id: CH-P06-TRANSFORMER
part_id: P06
order_key: 290
title: Il Transformer da zero
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 29. Il Transformer da zero

La domanda guida di questa lezione è come collegare «La mappa completa» e «Residual stream e output» senza perdere il contratto tecnico di il transformer da zero. L'oggetto osservato è lo stato nascosto che attraversa il blocco Transformer. Il contratto locale è: input, tokenizzati di shape [batch, length] e vettori [batch, length, d]; operazione, embedding, attention, MLP e residuo; output, stato contestuale e logits. Il caso guida è questo: Un caso minimo con input tokenizzati di shape [batch, length] e vettori [batch, length, d] e output «stato contestuale e logits». Il confine da mantenere esplicito è: mask, shape e percorso residuale devono essere compatibili.

## La mappa completa

Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape. [SRC-29-001]

La shape esplicita separa score, pesi e combinazione delle value.

**Caso da seguire.** Un caso minimo con input tokenizzati di shape [batch, length] e vettori [batch, length, d] e output «stato contestuale e logits».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Ogni componente mantiene un contratto di shape.


## Encoder

L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni. [SRC-29-002]

**Caso da seguire.** Un blocco con due token e due dimensioni nascoste.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
Attention(Q,K,V)=softmax(QK^T/\sqrt{d_k})V
$$

La shape esplicita separa score, pesi e combinazione delle value. [SRC-29-001]


![Il Transformer da zero: branch](../../assets/chapters/29_transformer/TRANSFOR-01/candidate-v48.png)

La prima figura segue il percorso da «La mappa completa» a «Decoder».


## Decoder

Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder. [SRC-29-003]

**Caso da seguire.** Un caso in cui mask, shape e percorso residuale devono essere compatibili.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Decoder».


## Multi-head attention

Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello. [SRC-29-004]

**Caso da seguire.** Un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract():
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[2.0, 0.0], [0.0, 3.0]]
    scores = [[sum(q[i][d] * k[j][d] for d in range(2)) for j in range(2)] for i in range(2)]
    weights = [normalize(row) for row in scores]
    output = [[sum(weights[i][j] * v[j][d] for j in range(2)) for d in range(2)] for i in range(2)]
    return {"scores": scores, "output": [[round(value, 6) for value in row] for row in output], "invariant": "queries read keys and values through the declared attention matrix"}
```

Esecuzione con `python snip_29_contract.py`:

```text
{"invariant": "queries read keys and values through the declared attention matrix", "output": [[1.462117, 0.806824], [0.537883, 2.193176]], "scores": [[1.0, 0.0], [0.0, 1.0]]}
```

Il test associato è [`code/test_29_contract.py`](code/test_29_contract.py); l'output versionato è [`code/outputs/SNIP-29-001.txt`](code/outputs/SNIP-29-001.txt).


## Residual stream e output

Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario. [SRC-29-001]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Residual stream e output».

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Residual stream e output» non si applica.


![Il Transformer da zero: matrix](../../assets/chapters/29_transformer/TRANSFOR-02/candidate-v48.png)

La seconda figura mette a confronto «Multi-head attention» e il limite discusso in «Residual stream e output».


## Come si collegano i passaggi

- **Da «La mappa completa» a «Encoder».** Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-29-001; SRC-29-002]

- **Da «Encoder» a «Decoder».** L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni. Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-29-002; SRC-29-003]

- **Da «Decoder» a «Multi-head attention».** Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder. Le head applicano proiezioni differenti e vengono concatenate. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-29-003; SRC-29-004]

- **Da «Multi-head attention» a «Residual stream e output».** Le head applicano proiezioni differenti e vengono concatenate. Layer ripetuti aggiornano il residual stream. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-29-004; SRC-29-001]

La catena completa produce stato contestuale e logits a partire da tokenizzati di shape [batch, length] e vettori [batch, length, d]. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: mask, shape e percorso residuale devono essere compatibili.


## Esercizi sul meccanismo

1. Ricostruisci «La mappa completa» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Encoder», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Decoder» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Multi-head attention» che produca una failure riconoscibile.
5. Per «Residual stream e output», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «tokenizzati di shape [batch, length] e vettori [batch, length, d]» e arriva fino a «stato contestuale e logits». Il limite da conservare è questo: mask, shape e percorso residuale devono essere compatibili. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
