<!--
chapter_id: CH-P09-MODEL-UPDATE
part_id: P09
order_key: 540
title: Aggiornamento, merging ed editing del modello
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 54. Aggiornamento, merging ed editing del modello

Aggiornamento, merging ed editing del modello viene letto come un sistema: «Continued adaptation» e «Versioning e rollback» restano collegati da confini e decisioni osservabili. L'oggetto osservato è versioni di pesi e modifiche localizzate del modello. Il contratto locale dichiara input, base model, delta, task e rollback point; operazione, continued adaptation, merge, editing e regressione; output, versione nuova, diff e test di regressione. Il primo esempio osservabile è Un delta modifica una sola chiave del caso guida e il test confronta prima, dopo e rollback. Il limite da non nascondere è: un merge senza valutazione può introdurre regressioni invisibili.

## Continued adaptation

Nuovi dati e obiettivi aggiornano il checkpoint. Replay, regolarizzazione e valutazioni controllano forgetting e regressioni. [SRC-54-001]

Il merge richiede una regola e una valutazione di regressione.

**Caso da seguire.** Un delta modifica una sola chiave del caso guida e il test confronta prima, dopo e rollback.

**Controllo.** Per «Continued adaptation», registra richiesta, decisione, stato e output finale. Nel caso «Continued adaptation», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Task arithmetic

Differenze tra checkpoint possono essere combinate come vettori. La compatibilità richiede stessa base e corrispondenza dei parametri. [SRC-54-004]

**Caso da seguire.** Due delta combinati e una capability testata prima e dopo.

**Controllo.** Ripeti «Task arithmetic» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La forma compatta aiuta a seguire il flusso senza attribuirgli una garanzia quantitativa.

**Schema concettuale.** `theta' = merge(theta_1, theta_2, rule)`

Il merge richiede una regola e una valutazione di regressione. [SRC-54-001]


![Aggiornamento, merging ed editing del modello: compare](../../assets/chapters/54_model_update/UPDATE-01/candidate-v48.png)

La prima figura segue il percorso da «Continued adaptation» a «TIES e DARE».


## TIES e DARE

Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. I risultati dipendono dai task e dalla scala dei delta. [SRC-54-003]

**Caso da seguire.** Un caso in cui un merge senza valutazione può introdurre regressioni invisibili.

**Controllo.** Per «TIES e DARE», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Model editing

ROME, MEMIT e famiglie affini cercano modifiche localizzate. Località, generalizzazione e side effect devono essere misurati separatamente. [SRC-54-002]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Per «Model editing», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Versioning e rollback

Un update produce un nuovo artefatto con fonti, test e dipendenze. Merging ed editing non sostituiscono la gestione delle versioni. [SRC-54-001]

**Caso da seguire.** Una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione.

**Controllo.** Per «Versioning e rollback», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Versioning e rollback», il risultato resta limitato da: Merging ed editing non sostituiscono la gestione delle versioni.


![Aggiornamento, merging ed editing del modello: timeline](../../assets/chapters/54_model_update/UPDATE-02/candidate-v48.png)

La seconda figura mette a confronto «Model editing» e il limite discusso in «Versioning e rollback».


## Esempio Python eseguito

Questa sezione apre il contratto Python di aggiornamento, merging ed editing del modello: il lettore può eseguire lo stesso file e confrontare il risultato. Per «Aggiornamento, merging ed editing del modello», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «aggiornamento, merging ed editing del modello» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    original = {"pacco": "in_transito", "ritardo": 1}
    edited = dict(original)
    edited["ritardo"] = 0
    changed = [key for key in original if original[key] != edited[key]]
    return {"changed_keys": changed, "rollback": original == {"pacco": "in_transito", "ritardo": 1}, "invariant": "an edit needs a targeted diff and a regression check"}
```

Esecuzione con `python snip_54_contract.py`:

```text
{"changed_keys": ["ritardo"], "invariant": "an edit needs a targeted diff and a regression check", "rollback": true}
```

Il test associato è [`code/test_54_contract.py`](code/test_54_contract.py); l'output versionato è [`code/outputs/SNIP-54-001.txt`](code/outputs/SNIP-54-001.txt).


## Come si collegano i passaggi

- **Da «Continued adaptation» a «Task arithmetic».** Nuovi dati e obiettivi aggiornano il checkpoint. Differenze tra checkpoint possono essere combinate come vettori. «Continued adaptation» nomina il confine e «Task arithmetic» implementa il percorso senza ereditare autorizzazioni implicite. Il passaggio successivo rende misurabile «Task arithmetic». [SRC-54-001; SRC-54-004]

- **Da «Task arithmetic» a «TIES e DARE».** Differenze tra checkpoint possono essere combinate come vettori. Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. Componendo «Task arithmetic» e «TIES e DARE» diventa necessario conservare stato, identità e decisione. Da «Task arithmetic» a «TIES e DARE» cambia la domanda osservabile. [SRC-54-004; SRC-54-003]

- **Da «TIES e DARE» a «Model editing».** Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. ROME, MEMIT e famiglie affini cercano modifiche localizzate. «Model editing» introduce failure e recovery prima di un side effect o di una perdita di stato. Il passaggio successivo rende misurabile «Model editing». [SRC-54-003; SRC-54-002]

- **Da «Model editing» a «Versioning e rollback».** ROME, MEMIT e famiglie affini cercano modifiche localizzate. Un update produce un nuovo artefatto con fonti, test e dipendenze. La chiusura su «Versioning e rollback» valuta il sistema completo, non soltanto il componente iniziale. Da «Model editing» a «Versioning e rollback» cambia la domanda osservabile. [SRC-54-002; SRC-54-001]

La catena completa produce versione nuova, diff e test di regressione a partire da base model, delta, task e rollback point. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un merge senza valutazione può introdurre regressioni invisibili.


## Prove sui confini del sistema

1. Ricostruisci «Continued adaptation» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Task arithmetic», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «TIES e DARE» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Model editing» che produca una failure riconoscibile.
5. Per «Versioning e rollback», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «base model, delta, task e rollback point» e arriva fino a «versione nuova, diff e test di regressione». Il limite da conservare è questo: un merge senza valutazione può introdurre regressioni invisibili. Il confine di «Versioning e rollback» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
