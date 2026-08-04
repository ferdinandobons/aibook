<!--
chapter_id: CH-P12-LLMOPS
part_id: P12
order_key: 820
title: LLMOps, edge, costo ed energia
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 82. LLMOps, edge, costo ed energia

La domanda guida di questa lezione è come collegare «Dalla versione al deployment» e «Energia e sostenibilità» senza perdere il contratto tecnico di llmops, edge, costo ed energia. L'oggetto osservato è un servizio LLM dalla versione al consumo. Il contratto locale è: input, modello, richieste, device, energia e monitor; operazione, deploy, osservabilità, edge routing e cost accounting; output, versione attiva, costo per richiesta e alert. Il caso guida è questo: Un record associa versione del modello, token, energia e costo per richiesta. Il confine da mantenere esplicito è: un costo locale non descrive l'intero ciclo di vita.

## Dalla versione al deployment

Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema. [SRC-82-001]

Costo e consumo dipendono dall'intero servizio e dall'intensità d'uso.

**Caso da seguire.** Un record associa versione del modello, token, energia e costo per richiesta.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Osservabilità

Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario. [SRC-82-002]

**Caso da seguire.** Costo per richiesta con energia e quota hardware separate.

**Controllo.** Ripeti «Osservabilità» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![LLMOps, edge, costo ed energia: checklist](../../assets/chapters/82_llmops/LLMOPS-01/candidate-v48.png)

La prima figura segue il percorso da «Dalla versione al deployment» a «Edge».


## Edge

Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Offline e privacy possono motivare il deployment locale. [SRC-82-003]

**Caso da seguire.** Un caso in cui un costo locale non descrive l'intero ciclo di vita.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Costo

Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e batching modificano l'allocazione. [SRC-82-004]

**Caso da seguire.** Un batch di richieste eterogenee in cui throughput, coda e time-to-first-token vengono misurati separatamente.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Energia e sostenibilità

Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono dichiarare confini e metodologia. [SRC-82-001]

**Caso da seguire.** Per «Energia e sostenibilità» si mantiene l'input del capitolo e si isola questa condizione: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Stime devono dichiarare confini e metodologia.


![LLMOps, edge, costo ed energia: chart](../../assets/chapters/82_llmops/LLMOPS-02/candidate-v48.png)

La seconda figura mette a confronto «Costo» e il limite discusso in «Energia e sostenibilità».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    request = {"model": "v1", "tokens": 20, "energy_wh": 0.4}
    cost = request["energy_wh"] * 0.30
    return {"model": request["model"], "cost": round(cost, 6), "invariant": "an operational metric records model version and measurement boundary"}
```

Esecuzione con `python snip_82_contract.py`:

```text
{"cost": 0.12, "invariant": "an operational metric records model version and measurement boundary", "model": "v1"}
```

Il test associato è [`code/test_82_contract.py`](code/test_82_contract.py); l'output versionato è [`code/outputs/SNIP-82-001.txt`](code/outputs/SNIP-82-001.txt).


## Come si collegano i passaggi

- **Da «Dalla versione al deployment» a «Osservabilità».** Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema. Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-82-001; SRC-82-002]

- **Da «Osservabilità» a «Edge».** Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario. Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-82-002; SRC-82-003]

- **Da «Edge» a «Costo».** Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Costo per token, richiesta, utente e risultato utile sono metriche differenti. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-82-003; SRC-82-004]

- **Da «Costo» a «Energia e sostenibilità».** Costo per token, richiesta, utente e risultato utile sono metriche differenti. Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-82-004; SRC-82-001]

La catena completa produce versione attiva, costo per richiesta e alert a partire da modello, richieste, device, energia e monitor. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un costo locale non descrive l'intero ciclo di vita.


## Prove sui confini del sistema

1. Ricostruisci «Dalla versione al deployment» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Osservabilità», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Edge» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Costo» che produca una failure riconoscibile.
5. Per «Energia e sostenibilità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «modello, richieste, device, energia e monitor» e arriva fino a «versione attiva, costo per richiesta e alert». Il limite da conservare è questo: un costo locale non descrive l'intero ciclo di vita. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
