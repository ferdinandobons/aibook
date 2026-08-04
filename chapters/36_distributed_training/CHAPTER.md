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

La domanda guida di questa lezione è come collegare «Data parallelism» e «Continued pretraining» senza perdere il contratto tecnico di training distribuito e continued pretraining. L'oggetto osservato è gradienti e stato distribuiti tra worker. Il contratto locale è: input, microbatch, worker, shard e topologia; operazione, all-reduce, sharding, pipeline e recovery; output, gradiente ridotto, stato sincronizzato e fault osservato. Il caso guida è questo: Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Il confine da mantenere esplicito è: la riduzione e il conteggio del batch devono essere dichiarati.

## Data parallelism

Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti. [SRC-36-001]

La riduzione dei gradienti deve essere coerente con worker, batch e loss reduction.

**Caso da seguire.** Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## ZeRO e FSDP

Parametri, gradienti e optimizer state vengono shardati tra worker. [SRC-36-002]

**Caso da seguire.** Due worker con gradienti diversi e media esplicita.

**Controllo.** Ripeti «ZeRO e FSDP» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Training distribuito e continued pretraining: architecture](../../assets/chapters/36_distributed_training/DIST-01/candidate-v48.png)

La prima figura segue il percorso da «Data parallelism» a «Tensor e pipeline parallelism».


## Tensor e pipeline parallelism

Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. [SRC-36-003]

**Caso da seguire.** Un caso in cui la riduzione e il conteggio del batch devono essere dichiarati.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Topologia e fault tolerance

Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. [SRC-36-004]

**Caso da seguire.** Due ricette con budget di token dichiarato, compute comparabile e loss osservata nello stesso intervallo.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Continued pretraining

Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate. [SRC-36-001]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Continued pretraining».

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.


![Training distribuito e continued pretraining: graph](../../assets/chapters/36_distributed_training/DIST-02/candidate-v48.png)

La seconda figura mette a confronto «Topologia e fault tolerance» e il limite discusso in «Continued pretraining».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
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

- **Da «Data parallelism» a «ZeRO e FSDP».** Repliche elaborano sotto-batch e aggregano gradienti. Parametri, gradienti e optimizer state vengono shardati tra worker. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-36-001; SRC-36-002]

- **Da «ZeRO e FSDP» a «Tensor e pipeline parallelism».** Parametri, gradienti e optimizer state vengono shardati tra worker. Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-36-002; SRC-36-003]

- **Da «Tensor e pipeline parallelism» a «Topologia e fault tolerance».** Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-36-003; SRC-36-004]

- **Da «Topologia e fault tolerance» a «Continued pretraining».** Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-36-004; SRC-36-001]

La catena completa produce gradiente ridotto, stato sincronizzato e fault osservato a partire da microbatch, worker, shard e topologia. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la riduzione e il conteggio del batch devono essere dichiarati.


## Prove sui confini del sistema

1. Ricostruisci «Data parallelism» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «ZeRO e FSDP», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Tensor e pipeline parallelism» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Topologia e fault tolerance» che produca una failure riconoscibile.
5. Per «Continued pretraining», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «microbatch, worker, shard e topologia» e arriva fino a «gradiente ridotto, stato sincronizzato e fault osservato». Il limite da conservare è questo: la riduzione e il conteggio del batch devono essere dichiarati. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
