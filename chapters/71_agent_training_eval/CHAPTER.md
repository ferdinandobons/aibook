<!--
chapter_id: CH-P11-AGENT-TRAINING-EVAL
part_id: P11
order_key: 710
title: Training e valutazione degli agenti
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 71. Training e valutazione degli agenti

La domanda guida di questa lezione è come collegare «Traiettorie come dati» e «Evaluation harness» senza perdere il contratto tecnico di training e valutazione degli agenti. L'oggetto osservato è traiettorie agentiche usate come dati e valutazione. Il contratto locale è: input, task, trace, policy, outcome e costo; operazione, SFT, RL, benchmark e harness; output, score di task, violazioni e failure per step. Il caso guida è questo: Due traiettorie hanno lo stesso successo, ma soltanto una ha zero violazioni di policy. Il confine da mantenere esplicito è: task riuscito e traiettoria sicura sono criteri distinti.

## Traiettorie come dati

Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento. [SRC-71-001]

L'eval deve distinguere compito riuscito, traiettoria e violazione di policy.

**Caso da seguire.** Due traiettorie hanno lo stesso successo, ma soltanto una ha zero violazioni di policy.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Imitation e SFT

Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire. [SRC-71-002]

**Caso da seguire.** Due traiettorie con stesso esito ma una violazione di policy.

**Controllo.** Ripeti «Imitation e SFT» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Training e valutazione degli agenti: chart](../../assets/chapters/71_agent_training_eval/EVAL-01/candidate-v48.png)

La prima figura segue il percorso da «Traiettorie come dati» a «RL in ambienti».


## RL in ambienti

Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker. [SRC-71-003]

**Caso da seguire.** Un caso in cui task riuscito e traiettoria sicura sono criteri distinti.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Benchmark agentici

Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting. [SRC-71-004]

**Caso da seguire.** Quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Evaluation harness

Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale. [SRC-71-001]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Evaluation harness» e all'output score di task, violazioni e failure per step.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale.


![Training e valutazione degli agenti: funnel](../../assets/chapters/71_agent_training_eval/EVAL-02/candidate-v50.png)

La seconda figura mette a confronto «Benchmark agentici» e il limite discusso in «Evaluation harness».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    traces = [{"success": True, "violations": 0}, {"success": True, "violations": 1}]
    safe_success = sum(trace["success"] and trace["violations"] == 0 for trace in traces)
    return {"task_success": sum(trace["success"] for trace in traces), "safe_success": safe_success, "invariant": "task completion and policy compliance are separate metrics"}
```

Esecuzione con `python snip_71_contract.py`:

```text
{"invariant": "task completion and policy compliance are separate metrics", "safe_success": 1, "task_success": 2}
```

Il test associato è [`code/test_71_contract.py`](code/test_71_contract.py); l'output versionato è [`code/outputs/SNIP-71-001.txt`](code/outputs/SNIP-71-001.txt).


## Come si collegano i passaggi

- **Da «Traiettorie come dati» a «Imitation e SFT».** Osservazioni, azioni, tool result e reward formano esempi sequenziali. Traiettorie riuscite possono essere imitate. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-71-001; SRC-71-002]

- **Da «Imitation e SFT» a «RL in ambienti».** Traiettorie riuscite possono essere imitate. Reward verificabili o simulati aggiornano policy multi-step. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-71-002; SRC-71-003]

- **Da «RL in ambienti» a «Benchmark agentici».** Reward verificabili o simulati aggiornano policy multi-step. Success rate, step, costo e side effect devono essere misurati. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-71-003; SRC-71-004]

- **Da «Benchmark agentici» a «Evaluation harness».** Success rate, step, costo e side effect devono essere misurati. Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-71-004; SRC-71-001]

La catena completa produce score di task, violazioni e failure per step a partire da task, trace, policy, outcome e costo. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: task riuscito e traiettoria sicura sono criteri distinti.


## Prove sui confini del sistema

1. Ricostruisci «Traiettorie come dati» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Imitation e SFT», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «RL in ambienti» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Benchmark agentici» che produca una failure riconoscibile.
5. Per «Evaluation harness», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «task, trace, policy, outcome e costo» e arriva fino a «score di task, violazioni e failure per step». Il limite da conservare è questo: task riuscito e traiettoria sicura sono criteri distinti. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
