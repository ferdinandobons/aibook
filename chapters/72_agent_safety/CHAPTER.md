<!--
chapter_id: CH-P11-AGENT-SAFETY
part_id: P11
order_key: 720
title: Sicurezza operativa degli agenti
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 72. Sicurezza operativa degli agenti

Sicurezza operativa degli agenti viene letto come un sistema: «Least privilege» e «Prompt injection» restano collegati da confini e decisioni osservabili. L'oggetto osservato è una decisione agentica su una risorsa reale. Il contratto locale dichiara input, input non fidato, tool, scope e approvazione; operazione, least privilege, sandbox, human approval e rollback; output, allow/deny, side effect o rollback auditabile. La situazione minima da seguire è Lookup_order è consentito, mentre refund richiede approvazione o viene negato dalla policy esterna. Il limite da non nascondere è: l'enforcement deve stare fuori dal testo generato.

## Least privilege

Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant. [SRC-72-001]

Sicurezza agentica richiede una decisione esterna alla sola generazione.

**Caso da seguire.** Lookup_order è consentito, mentre refund richiede approvazione o viene negato dalla policy esterna.

**Controllo.** Per «Least privilege», registra richiesta, decisione, stato e output finale. Nel caso «Least privilege», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Sandbox

Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. [SRC-72-002]

**Caso da seguire.** Una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione.

**Controllo.** Ripeti «Sandbox» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


Per questo capitolo la notazione compatta chiarisce input, trasformazione e risultato.

**Schema concettuale.** `allow = policy(input, tool, scope)`

Sicurezza agentica richiede una decisione esterna alla sola generazione. [SRC-72-001]


![Sicurezza operativa degli agenti: threat](../../assets/chapters/72_agent_safety/SAFETY-01/candidate-v50.png)

La prima figura segue il percorso da «Least privilege» a «Human approval».


## Human approval

Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. [SRC-72-003]

**Caso da seguire.** Per «Human approval» si mantiene l'input del capitolo e si isola questa condizione: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti.

**Controllo.** Per «Human approval», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Rollback e audit

Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. [SRC-72-004]

**Caso da seguire.** Per «Rollback e audit» si mantiene l'input del capitolo e si isola questa condizione: Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria.

**Controllo.** Per «Rollback e audit», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Prompt injection

Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati. [SRC-72-001]

**Caso da seguire.** Un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente.

**Controllo.** Per «Prompt injection», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Prompt injection», il risultato resta limitato da: Dati non fidati e istruzioni di sistema devono restare separati.


![Sicurezza operativa degli agenti: loop](../../assets/chapters/72_agent_safety/SAFETY-02/candidate-v48.png)

La seconda figura mette a confronto «Rollback e audit» e il limite discusso in «Prompt injection».


## Esempio Python eseguito

Per rendere osservabile sicurezza operativa degli agenti, il capitolo conserva qui l'artefatto Python eseguito. Per «Sicurezza operativa degli agenti», il caso di default usa valori piccoli per isolare il meccanismo. Il test rifiuta anche un caso non documentato di «sicurezza operativa degli agenti».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    request = {"tool": "refund", "scope": "order:A1"}
    policy = {"allowed_tools": {"lookup_order"}, "requires_approval": {"refund"}}
    allowed = request["tool"] in policy["allowed_tools"]
    return {"allowed": allowed, "approval_required": request["tool"] in policy["requires_approval"], "invariant": "authorization and rollback live outside the model text"}
```

Esecuzione con `python snip_72_contract.py`:

```text
{"allowed": false, "approval_required": true, "invariant": "authorization and rollback live outside the model text"}
```

Il test associato è [`code/test_72_contract.py`](code/test_72_contract.py); l'output versionato è [`code/outputs/SNIP-72-001.txt`](code/outputs/SNIP-72-001.txt).


## Come si collegano i passaggi

- **Da «Least privilege» a «Sandbox».** Ogni tool riceve soltanto gli scope necessari. Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. «Least privilege» nomina il confine e «Sandbox» implementa il percorso senza ereditare autorizzazioni implicite. Il passaggio successivo rende misurabile «Sandbox». [SRC-72-001; SRC-72-002]

- **Da «Sandbox» a «Human approval».** Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. Componendo «Sandbox» e «Human approval» diventa necessario conservare stato, identità e decisione. Da «Sandbox» a «Human approval» cambia la domanda osservabile. [SRC-72-002; SRC-72-003]

- **Da «Human approval» a «Rollback e audit».** Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. «Rollback e audit» introduce failure e recovery prima di un side effect o di una perdita di stato. Il passaggio successivo rende misurabile «Rollback e audit». [SRC-72-003; SRC-72-004]

- **Da «Rollback e audit» a «Prompt injection».** Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. Contenuti esterni possono tentare di cambiare il piano. La chiusura su «Prompt injection» valuta il sistema completo, non soltanto il componente iniziale. Da «Rollback e audit» a «Prompt injection» cambia la domanda osservabile. [SRC-72-004; SRC-72-001]

La catena completa produce allow/deny, side effect o rollback auditabile a partire da input non fidato, tool, scope e approvazione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: l'enforcement deve stare fuori dal testo generato.


## Prove sui confini del sistema

1. Ricostruisci «Least privilege» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Sandbox», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Human approval» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Rollback e audit» che produca una failure riconoscibile.
5. Per «Prompt injection», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «input non fidato, tool, scope e approvazione» e arriva fino a «allow/deny, side effect o rollback auditabile». Il limite da conservare è questo: l'enforcement deve stare fuori dal testo generato. Il confine di «Prompt injection» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
