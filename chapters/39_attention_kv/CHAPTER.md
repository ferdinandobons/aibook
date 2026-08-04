<!--
chapter_id: CH-P08-ATTENTION-KV
part_id: P08
order_key: 390
title: Varianti dell'attention e gestione KV
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 39. Varianti dell'attention e gestione KV

Per entrare in varianti dell'attention e gestione kv, seguiamo il passaggio che unisce «MHA» a «MLA e cache». L'oggetto osservato è le teste di query e key-value che alimentano l'attention. Il contratto locale dichiara input, Q con h_q teste e KV con h_kv teste; operazione, MHA, MQA, GQA, località o sparsità; output, score, cache e pattern di comunicazione. Il primo esempio osservabile è Un caso minimo con input Q con h_q teste e KV con h_kv teste e output «score, cache e pattern di comunicazione». Il limite da non nascondere è: raggruppamento delle teste e costo della KV cache restano espliciti.

## MHA

Ogni query head possiede key e value dedicate. [SRC-39-001]

Numero di KV head e pattern di attenzione cambiano memoria e connettività.

**Caso da seguire.** Un caso minimo con input Q con h_q teste e KV con h_kv teste e output «score, cache e pattern di comunicazione».

**Controllo.** Per «MHA», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «MHA», il vincolo da conservare è: Ogni query head possiede key e value dedicate.


## MQA

Tutte le query head condividono una singola coppia key-value, riducendo la cache. [SRC-39-002]

**Caso da seguire.** Quattro query head condividono due KV head.

**Controllo.** Per «MQA», ricalcola il caso a mano e con lo snippet. Nel caso «MQA», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
M = softmax(Q K^T / sqrt(d_k)) V
$$

Numero di KV head e pattern di attenzione cambiano memoria e connettività. [SRC-39-001]


![Varianti dell'attention e gestione KV: matrix](../../assets/chapters/39_attention_kv/KV-01/candidate-v47.png)

La prima figura segue il percorso da «MHA» a «GQA».


## GQA

Gruppi di query head condividono un numero intermedio di KV head. [SRC-39-003]

**Caso da seguire.** Un caso in cui raggruppamento delle teste e costo della KV cache restano espliciti.

**Controllo.** Per «GQA», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «GQA».


## Local e sparse attention

Finestre e pattern selezionati riducono le coppie ma cambiano la connettività. [SRC-39-004]

**Caso da seguire.** Un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup.

**Controllo.** Per «Local e sparse attention», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Local e sparse attention», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

La prova locale di varianti dell'attention e gestione kv parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Varianti dell'attention e gestione KV», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «varianti dell'attention e gestione kv» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    query_heads = 4
    kv_heads = 2
    group_size = query_heads // kv_heads
    return {"query_heads": query_heads, "kv_heads": kv_heads, "queries_per_kv": group_size, "invariant": "the head grouping is declared before cache accounting"}
```

Esecuzione con `python snip_39_contract.py`:

```text
{"invariant": "the head grouping is declared before cache accounting", "kv_heads": 2, "queries_per_kv": 2, "query_heads": 4}
```

Il test associato è [`code/test_39_contract.py`](code/test_39_contract.py); l'output versionato è [`code/outputs/SNIP-39-001.txt`](code/outputs/SNIP-39-001.txt).


## MLA e cache

Compressione latente e numero di KV head sono strategie differenti. La memoria dipende anche da layer, dtype, batch e lunghezza. [SRC-39-001]

**Caso da seguire.** Un prefill che scrive key e value e un decode che aggiunge una sola posizione senza ricomputare il prefisso.

**Controllo.** Per «MLA e cache», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «MLA e cache» non si applica.


![Varianti dell'attention e gestione KV: compare](../../assets/chapters/39_attention_kv/KV-02/candidate-v47.png)

La seconda figura mette a confronto «Local e sparse attention» e il limite discusso in «MLA e cache».


## Come si collegano i passaggi

- **Da «MHA» a «MQA».** Ogni query head possiede key e value dedicate. Tutte le query head condividono una singola coppia key-value, riducendo la cache. Tra «MHA» e «MQA» l'ingresso viene fissato prima della regola che produce il valore. Da «MHA» a «MQA» cambia la domanda osservabile. [SRC-39-001; SRC-39-002]

- **Da «MQA» a «GQA».** Tutte le query head condividono una singola coppia key-value, riducendo la cache. Gruppi di query head condividono un numero intermedio di KV head. Nel caso «GQA» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «GQA». [SRC-39-002; SRC-39-003]

- **Da «GQA» a «Local e sparse attention».** Gruppi di query head condividono un numero intermedio di KV head. Finestre e pattern selezionati riducono le coppie ma cambiano la connettività. Dopo «GQA», la variante di «Local e sparse attention» cambia una proprietà alla volta. Da «GQA» a «Local e sparse attention» cambia la domanda osservabile. [SRC-39-003; SRC-39-004]

- **Da «Local e sparse attention» a «MLA e cache».** Finestre e pattern selezionati riducono le coppie ma cambiano la connettività. Compressione latente e numero di KV head sono strategie differenti. Da «MLA e cache» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «MLA e cache». [SRC-39-004; SRC-39-001]

La catena completa produce score, cache e pattern di comunicazione a partire da Q con h_q teste e KV con h_kv teste. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: raggruppamento delle teste e costo della KV cache restano espliciti.


## Esercizi sul meccanismo

1. Ricostruisci «MHA» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «MQA», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «GQA» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Local e sparse attention» che produca una failure riconoscibile.
5. Per «MLA e cache», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «Q con h_q teste e KV con h_kv teste» e arriva fino a «score, cache e pattern di comunicazione». Il limite da conservare è questo: raggruppamento delle teste e costo della KV cache restano espliciti. La formula e il codice collegati a «MLA e cache» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
