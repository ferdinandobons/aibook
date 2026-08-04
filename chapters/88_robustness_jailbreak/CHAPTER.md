<!--
chapter_id: CH-P13-ROBUSTNESS-JAILBREAK
part_id: P13
order_key: 880
title: Robustezza, jailbreak e attacchi adversarial
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 88. Robustezza, jailbreak e attacchi adversarial

La domanda guida di questa lezione è come collegare «Threat model» e «Valutazione adattiva» senza perdere il contratto tecnico di robustezza, jailbreak e attacchi adversarial. L'oggetto osservato è una superficie di attacco e il comportamento sotto perturbazione. Il contratto locale è: input, threat model, prompt, budget e risposta; operazione, jailbreak, perturbazione, difesa e adaptive evaluation; output, success rate, failure mode e costo della difesa. Il caso guida è questo: Una perturbazione sullo stesso prompt produce un failure di attacco che la baseline non produce. Il confine da mantenere esplicito è: un test superato non copre minacce non incluse nel protocollo.

## Threat model

Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Un jailbreak testuale e un attacco ai pesi hanno contratti diversi. [SRC-88-001]

Robustezza e jailbreak vanno definiti con minaccia e protocollo.

**Caso da seguire.** Una perturbazione sullo stesso prompt produce un failure di attacco che la baseline non produce.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Perturbazioni

Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali. [SRC-88-002]

**Caso da seguire.** Stesso prompt con perturbazione e controllo di policy.

**Controllo.** Ripeti «Perturbazioni» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Robustezza, jailbreak e attacchi adversarial: threat](../../assets/chapters/88_robustness_jailbreak/JAILBREAK-01/candidate-v48.png)

La prima figura segue il percorso da «Threat model» a «Ottimizzazione adversarial».


## Ottimizzazione adversarial

Suffix e prompt vengono cercati per aumentare una loss di attacco. Trasferibilità e query budget devono essere riportati. [SRC-88-003]

**Caso da seguire.** Un caso in cui un test superato non copre minacce non incluse nel protocollo.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Difese

Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass. [SRC-88-004]

**Caso da seguire.** Un input non fidato attraversa una policy esterna. Il controllo deve restare attivo anche se il modello produce una richiesta testuale convincente.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Valutazione adattiva

Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato. [SRC-88-001]

**Caso da seguire.** Per «Valutazione adattiva» si mantiene l'input del capitolo e si isola questa condizione: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato.


![Robustezza, jailbreak e attacchi adversarial: chart](../../assets/chapters/88_robustness_jailbreak/JAILBREAK-02/candidate-v50.png)

La seconda figura mette a confronto «Difese» e il limite discusso in «Valutazione adattiva».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    prompts = [("base", False), ("perturbed", True)]
    failures = [name for name, attack_succeeded in prompts if attack_succeeded]
    return {"attack_success_rate": len(failures) / len(prompts), "failures": failures, "invariant": "robustness is defined relative to an explicit threat model"}
```

Esecuzione con `python snip_88_contract.py`:

```text
{"attack_success_rate": 0.5, "failures": ["perturbed"], "invariant": "robustness is defined relative to an explicit threat model"}
```

Il test associato è [`code/test_88_contract.py`](code/test_88_contract.py); l'output versionato è [`code/outputs/SNIP-88-001.txt`](code/outputs/SNIP-88-001.txt).


## Come si collegano i passaggi

- **Da «Threat model» a «Perturbazioni».** Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-88-001; SRC-88-002]

- **Da «Perturbazioni» a «Ottimizzazione adversarial».** Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali. Suffix e prompt vengono cercati per aumentare una loss di attacco. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-88-002; SRC-88-003]

- **Da «Ottimizzazione adversarial» a «Difese».** Suffix e prompt vengono cercati per aumentare una loss di attacco. Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-88-003; SRC-88-004]

- **Da «Difese» a «Valutazione adattiva».** Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass. Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-88-004; SRC-88-001]

La catena completa produce success rate, failure mode e costo della difesa a partire da threat model, prompt, budget e risposta. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un test superato non copre minacce non incluse nel protocollo.


## Prove sui confini del sistema

1. Ricostruisci «Threat model» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Perturbazioni», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Ottimizzazione adversarial» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Difese» che produca una failure riconoscibile.
5. Per «Valutazione adattiva», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «threat model, prompt, budget e risposta» e arriva fino a «success rate, failure mode e costo della difesa». Il limite da conservare è questo: un test superato non copre minacce non incluse nel protocollo. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
