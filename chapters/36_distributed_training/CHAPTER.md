<!--
chapter_id: CH-P07-DISTRIBUTED-TRAINING
part_id: P07
order_key: 360
title: Training distribuito e continued pretraining
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 36. Training distribuito e continued pretraining

Training distribuito e continued pretraining viene letto come un sistema: «Data parallelism» e «Continued pretraining» restano collegati da confini e decisioni osservabili. L'oggetto osservato è gradienti e stato distribuiti tra worker. Il contratto locale dichiara input, microbatch, worker, shard e topologia; operazione, all-reduce, sharding, pipeline e recovery; output, gradiente ridotto, stato sincronizzato e fault osservato. Il caso di partenza è Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Il limite da non nascondere è: la riduzione e il conteggio del batch devono essere dichiarati.

## Data parallelism

Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti. [SRC-36-001]

La riduzione dei gradienti deve essere coerente con worker, batch e loss reduction.

**Caso da seguire.** Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata.

**Controllo.** Per «Data parallelism», registra richiesta, decisione, stato e output finale. Nel caso «Data parallelism», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## ZeRO e FSDP

Parametri, gradienti e optimizer state vengono shardati tra worker. [SRC-36-002]

**Caso da seguire.** Due worker con gradienti diversi e media esplicita.

**Controllo.** Ripeti «ZeRO e FSDP» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La relazione centrale può essere scritta come:

$$
g = (1 / W) sum_w g_w
$$

La riduzione dei gradienti deve essere coerente con worker, batch e loss reduction. [SRC-36-001]


![Training distribuito e continued pretraining: architecture](../../assets/chapters/36_distributed_training/DIST-01/candidate-v48.png)

La prima figura segue il percorso da «Data parallelism» a «Tensor e pipeline parallelism».


## Tensor e pipeline parallelism

Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. [SRC-36-003]

**Caso da seguire.** Un caso in cui la riduzione e il conteggio del batch devono essere dichiarati.

**Controllo.** Per «Tensor e pipeline parallelism», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Topologia e fault tolerance

Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. [SRC-36-004]

**Caso da seguire.** Due ricette con budget di token dichiarato, compute comparabile e loss osservata nello stesso intervallo.

**Controllo.** Per «Topologia e fault tolerance», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Continued pretraining

Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate. [SRC-36-001]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Continued pretraining».

**Controllo.** Per «Continued pretraining», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Continued pretraining», il risultato resta limitato da: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.


![Training distribuito e continued pretraining: graph](../../assets/chapters/36_distributed_training/DIST-02/candidate-v48.png)

La seconda figura mette a confronto «Topologia e fault tolerance» e il limite discusso in «Continued pretraining».


## Esempio Python eseguito

Per rendere osservabile training distribuito e continued pretraining, il capitolo conserva qui l'artefatto Python eseguito. Per «Training distribuito e continued pretraining», il caso di default usa valori piccoli per isolare il meccanismo. Il test rifiuta anche un caso non documentato di «training distribuito e continued pretraining».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    worker_gradients = [[1.0, 3.0], [3.0, 1.0]]
    workers = len(worker_gradients)
    reduced = [sum(row[index] for row in worker_gradients) / workers for index in range(2)]
    return {"workers": workers, "reduced_gradient": reduced, "invariant": "all workers contribute to the same declared reduction"}
```

Esecuzione con `python snip_36_contract.py`:

```text
{"invariant": "all workers contribute to the same declared reduction", "reduced_gradient": [2.0, 2.0], "workers": 2}
```

Il test associato è [`code/test_36_contract.py`](code/test_36_contract.py); l'output versionato è [`code/outputs/SNIP-36-001.txt`](code/outputs/SNIP-36-001.txt).


## Come si collegano i passaggi

- **Da «Data parallelism» a «ZeRO e FSDP».** Repliche elaborano sotto-batch e aggregano gradienti. Parametri, gradienti e optimizer state vengono shardati tra worker. «Data parallelism» nomina il confine e «ZeRO e FSDP» implementa il percorso senza ereditare autorizzazioni implicite. Il passaggio successivo rende misurabile «ZeRO e FSDP». [SRC-36-001; SRC-36-002]

- **Da «ZeRO e FSDP» a «Tensor e pipeline parallelism».** Parametri, gradienti e optimizer state vengono shardati tra worker. Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. Componendo «ZeRO e FSDP» e «Tensor e pipeline parallelism» diventa necessario conservare stato, identità e decisione. Da «ZeRO e FSDP» a «Tensor e pipeline parallelism» cambia la domanda osservabile. [SRC-36-002; SRC-36-003]

- **Da «Tensor e pipeline parallelism» a «Topologia e fault tolerance».** Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. «Topologia e fault tolerance» introduce failure e recovery prima di un side effect o di una perdita di stato. Il passaggio successivo rende misurabile «Topologia e fault tolerance». [SRC-36-003; SRC-36-004]

- **Da «Topologia e fault tolerance» a «Continued pretraining».** Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate. La chiusura su «Continued pretraining» valuta il sistema completo, non soltanto il componente iniziale. Da «Topologia e fault tolerance» a «Continued pretraining» cambia la domanda osservabile. [SRC-36-004; SRC-36-001]

La catena completa produce gradiente ridotto, stato sincronizzato e fault osservato a partire da microbatch, worker, shard e topologia. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la riduzione e il conteggio del batch devono essere dichiarati.


## Prove sui confini del sistema

1. Ricostruisci «Data parallelism» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «ZeRO e FSDP», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Tensor e pipeline parallelism» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Topologia e fault tolerance» che produca una failure riconoscibile.
5. Per «Continued pretraining», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «microbatch, worker, shard e topologia» e arriva fino a «gradiente ridotto, stato sincronizzato e fault osservato». Il limite da conservare è questo: la riduzione e il conteggio del batch devono essere dichiarati. Il confine di «Continued pretraining» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
