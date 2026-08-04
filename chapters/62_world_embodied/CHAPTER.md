<!--
chapter_id: CH-P10-WORLD-EMBODIED
part_id: P10
order_key: 620
title: World model, embodied AI e vision-language-action
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 62. World model, embodied AI e vision-language-action

La domanda guida di questa lezione è come collegare «Modello della dinamica» e «Sicurezza e sim-to-real» senza perdere il contratto tecnico di world model, embodied ai e vision-language-action. L'oggetto osservato è lo stato di un agente embodied nel mondo. Il contratto locale è: input, osservazione, stato, azione e dinamica; operazione, world model, planning, VLA e controllo; output, azione, stato previsto e risultato fisico. Il caso guida è questo: Un'azione move porta la posizione da 0 a 1 e consuma una unità di batteria. Il confine da mantenere esplicito è: sim-to-real richiede una misura sul sistema reale.

## Modello della dinamica

Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione. [SRC-62-001]

Un world model o una policy produce un'azione condizionata da osservazione e stato.

**Caso da seguire.** Un'azione move porta la posizione da 0 a 1 e consuma una unità di batteria.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Planning nel modello

Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello possono essere sfruttati dal planner. [SRC-62-002]

**Caso da seguire.** Un'azione prevista in simulazione e il controllo del suo esito.

**Controllo.** Ripeti «Planning nel modello» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![World model, embodied AI e vision-language-action: loop](../../assets/chapters/62_world_embodied/EMBODIED-01/candidate-v48.png)

La prima figura segue il percorso da «Modello della dinamica» a «Embodied perception».


## Embodied perception

Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e calibrazione influenzano ogni azione. [SRC-62-003]

**Caso da seguire.** Un caso in cui sim-to-real richiede una misura sul sistema reale.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Vision-language-action

VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e discretizzazione devono essere dichiarate. [SRC-62-004]

**Caso da seguire.** Una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Sicurezza e sim-to-real

Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale. [SRC-62-001]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale.


![World model, embodied AI e vision-language-action: pipeline](../../assets/chapters/62_world_embodied/EMBODIED-02/candidate-v48.png)

La seconda figura mette a confronto «Vision-language-action» e il limite discusso in «Sicurezza e sim-to-real».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    state = {"position": 0, "battery": 2}
    action = "move"
    next_state = dict(state)
    next_state["position"] += 1
    next_state["battery"] -= 1
    return {"action": action, "next_state": next_state, "invariant": "the world transition exposes state and action consequences"}
```

Esecuzione con `python snip_62_contract.py`:

```text
{"action": "move", "invariant": "the world transition exposes state and action consequences", "next_state": {"battery": 1, "position": 1}}
```

Il test associato è [`code/test_62_contract.py`](code/test_62_contract.py); l'output versionato è [`code/outputs/SNIP-62-001.txt`](code/outputs/SNIP-62-001.txt).


## Come si collegano i passaggi

- **Da «Modello della dinamica» a «Planning nel modello».** Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione. Traiettorie candidate vengono simulate e valutate prima di agire. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-62-001; SRC-62-002]

- **Da «Planning nel modello» a «Embodied perception».** Traiettorie candidate vengono simulate e valutate prima di agire. Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-62-002; SRC-62-003]

- **Da «Embodied perception» a «Vision-language-action».** Un agente fisico collega camera, propriocezione, linguaggio e coordinate. VLA mappa osservazioni e istruzioni a token o controlli di azione. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-62-003; SRC-62-004]

- **Da «Vision-language-action» a «Sicurezza e sim-to-real».** VLA mappa osservazioni e istruzioni a token o controlli di azione. Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-62-004; SRC-62-001]

La catena completa produce azione, stato previsto e risultato fisico a partire da osservazione, stato, azione e dinamica. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: sim-to-real richiede una misura sul sistema reale.


## Prove sui confini del sistema

1. Ricostruisci «Modello della dinamica» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Planning nel modello», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Embodied perception» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Vision-language-action» che produca una failure riconoscibile.
5. Per «Sicurezza e sim-to-real», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «osservazione, stato, azione e dinamica» e arriva fino a «azione, stato previsto e risultato fisico». Il limite da conservare è questo: sim-to-real richiede una misura sul sistema reale. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
