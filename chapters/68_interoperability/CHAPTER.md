<!--
chapter_id: CH-P11-INTEROPERABILITY
part_id: P11
order_key: 680
title: Protocolli e interoperabilità
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 68. Protocolli e interoperabilità

Per capire protocolli e interoperabilità, partiamo da «Contratti tra componenti» e seguiamo ogni confine fino a «Compatibilità ed evoluzione». L'oggetto osservato è un messaggio tra componenti con identità e versione. Il contratto locale dichiara input, capability, schema, token e policy; operazione, negoziazione, encoding, autorizzazione e compatibilità; output, messaggio accettato o errore di protocollo. Il caso di partenza è Un producer versione 1 è compatibile con un consumer che accetta le versioni 1 e 2. Il limite da non nascondere è: compatibilità sintattica non garantisce semantica o autorizzazione.

## Contratti tra componenti

Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool. [SRC-68-001]

Un protocollo definisce formato e semantica condivisa tra componenti.

**Caso da seguire.** Un producer versione 1 è compatibile con un consumer che accetta le versioni 1 e 2.

**Controllo.** Per «Contratti tra componenti», registra richiesta, decisione, stato e output finale. Nel caso «Contratti tra componenti», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Model Context Protocol

MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il trasporto devono essere dichiarati. [SRC-68-001]

**Caso da seguire.** Un server MCP che espone una capability e un tool con schema degli argomenti.

**Controllo.** Ripeti «Model Context Protocol» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


Lo schema seguente rende esplicito il confine tra il meccanismo e la sua valutazione.

**Schema concettuale.** `message = protocol.encode(state)`

Un protocollo definisce formato e semantica condivisa tra componenti. [SRC-68-001]


![Protocolli e interoperabilità: compare](../../assets/chapters/68_interoperability/INTEROPERA-01/candidate-v50.png)

La prima figura segue il percorso da «Contratti tra componenti» a «Agent-to-agent».


## Agent-to-agent

Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti. [SRC-68-002]

**Caso da seguire.** Un task A2A che passa da discovery a working e poi a completed.

**Controllo.** Per «Agent-to-agent», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Identità e autorizzazione

Interoperabilità non implica fiducia. Token, scope, provenance e policy devono attraversare ogni hop. [SRC-68-003]

**Caso da seguire.** Una credenziale firmata con subject, scope, issuer e scadenza.

**Controllo.** Per «Identità e autorizzazione», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Compatibilità ed evoluzione

Version e capability negotiation rendono esplicita l'incompatibilità. Una versione non supportata non deve proseguire silenziosamente. [SRC-68-001]

**Caso da seguire.** Una negoziazione che rifiuta un campo nuovo quando la versione non lo supporta.

**Controllo.** Per «Compatibilità ed evoluzione», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Compatibilità ed evoluzione», il risultato resta limitato da: Una versione non supportata non deve proseguire silenziosamente.


![Protocolli e interoperabilità: graph](../../assets/chapters/68_interoperability/INTEROPERA-02/candidate-v48.png)

La seconda figura mette a confronto «Identità e autorizzazione» e il limite discusso in «Compatibilità ed evoluzione».


## Esempio Python eseguito

Per rendere osservabile protocolli e interoperabilità, il capitolo conserva qui l'artefatto Python eseguito. Per «Protocolli e interoperabilità», il caso di default usa valori piccoli per isolare il meccanismo. Il test rifiuta anche un caso non documentato di «protocolli e interoperabilità».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    producer = {"version": 1, "capability": "lookup_order"}
    consumer = {"accepted_versions": {1, 2}, "required": "lookup_order"}
    compatible = producer["version"] in consumer["accepted_versions"] and producer["capability"] == consumer["required"]
    return {"compatible": compatible, "invariant": "interoperability is a versioned contract, not a shared label"}
```

Esecuzione con `python snip_68_contract.py`:

```text
{"compatible": true, "invariant": "interoperability is a versioned contract, not a shared label"}
```

Il test associato è [`code/test_68_contract.py`](code/test_68_contract.py); l'output versionato è [`code/outputs/SNIP-68-001.txt`](code/outputs/SNIP-68-001.txt).


## Come si collegano i passaggi

- **Da «Contratti tra componenti» a «Model Context Protocol».** Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool. MCP organizza risorse, prompt e tool esposti da server. «Contratti tra componenti» nomina il confine e «Model Context Protocol» implementa il percorso senza ereditare autorizzazioni implicite. Il passaggio successivo rende misurabile «Model Context Protocol». [SRC-68-001; SRC-68-001]

- **Da «Model Context Protocol» a «Agent-to-agent».** MCP organizza risorse, prompt e tool esposti da server. Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti. Componendo «Model Context Protocol» e «Agent-to-agent» diventa necessario conservare stato, identità e decisione. Da «Model Context Protocol» a «Agent-to-agent» cambia la domanda osservabile. [SRC-68-001; SRC-68-002]

- **Da «Agent-to-agent» a «Identità e autorizzazione».** Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti. Interoperabilità non implica fiducia. «Identità e autorizzazione» introduce failure e recovery prima di un side effect o di una perdita di stato. Il passaggio successivo rende misurabile «Identità e autorizzazione». [SRC-68-002; SRC-68-003]

- **Da «Identità e autorizzazione» a «Compatibilità ed evoluzione».** Interoperabilità non implica fiducia. Version e capability negotiation rendono esplicita l'incompatibilità. La chiusura su «Compatibilità ed evoluzione» valuta il sistema completo, non soltanto il componente iniziale. Da «Identità e autorizzazione» a «Compatibilità ed evoluzione» cambia la domanda osservabile. [SRC-68-003; SRC-68-001]

La catena completa produce messaggio accettato o errore di protocollo a partire da capability, schema, token e policy. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: compatibilità sintattica non garantisce semantica o autorizzazione.


## Prove sui confini del sistema

1. Ricostruisci «Contratti tra componenti» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Model Context Protocol», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Agent-to-agent» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Identità e autorizzazione» che produca una failure riconoscibile.
5. Per «Compatibilità ed evoluzione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «capability, schema, token e policy» e arriva fino a «messaggio accettato o errore di protocollo». Il limite da conservare è questo: compatibilità sintattica non garantisce semantica o autorizzazione. Il confine di «Compatibilità ed evoluzione» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
