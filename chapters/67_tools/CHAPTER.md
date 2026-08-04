<!--
chapter_id: CH-P11-TOOLS
part_id: P11
order_key: 670
title: Output strutturato e uso degli strumenti
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 67. Output strutturato e uso degli strumenti

Il percorso di output strutturato e uso degli strumenti attraversa «Schema dell'output» e «Idempotenza e side effect» senza attribuire al solo modello ciò che dipende dal sistema. L'oggetto osservato è una chiamata a tool con schema e autorizzazione. Il contratto locale dichiara input, nome, argomenti, scope e stato; operazione, parsing, selezione, esecuzione e osservazione; output, risultato del tool o rifiuto tracciato. Per fissare il riferimento usiamo Lookup_order passa l'allowlist, mentre refund viene rifiutato prima del side effect. Il limite da non nascondere è: schema valido non significa permesso di eseguire il side effect.

## Schema dell'output

JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non garantisce correttezza semantica. [SRC-67-001]

Lo schema rende l'azione parsabile, non automaticamente autorizzata.

**Caso da seguire.** Lookup_order passa l'allowlist, mentre refund viene rifiutato prima del side effect.

**Controllo.** Per «Schema dell'output», registra richiesta, decisione, stato e output finale. Nel caso «Schema dell'output», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Selezione del tool

Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e autorizzazioni influenzano la decisione. [SRC-67-002]

**Caso da seguire.** Una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione.

**Controllo.** Ripeti «Selezione del tool» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


Per questo capitolo la notazione compatta chiarisce input, trasformazione e risultato.

**Schema concettuale.** `tool_call = schema(name, args, scope)`

Lo schema rende l'azione parsabile, non automaticamente autorizzata. [SRC-67-001]


![Output strutturato e uso degli strumenti: branch](../../assets/chapters/67_tools/TOOLS-01/candidate-v48.png)

La prima figura segue il percorso da «Schema dell'output» a «Argomenti».


## Argomenti

Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi mancanti richiedono chiarimento o fallback. [SRC-67-003]

**Caso da seguire.** Un caso in cui schema valido non significa permesso di eseguire il side effect.

**Controllo.** Per «Argomenti», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Esecuzione e osservazione

Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Timeout ed errori devono essere rappresentati. [SRC-67-004]

**Caso da seguire.** Una traiettoria minima alterna osservazione, decisione, tool e verifica. Il test può controllare che un'azione non autorizzata venga bloccata.

**Controllo.** Per «Esecuzione e osservazione», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Idempotenza e side effect

Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate. [SRC-67-001]

**Caso da seguire.** Per «Idempotenza e side effect» si mantiene l'input del capitolo e si isola questa condizione: Operazioni di lettura e scrittura hanno rischi differenti.

**Controllo.** Per «Idempotenza e side effect», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Idempotenza e side effect», il risultato resta limitato da: Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate.


![Output strutturato e uso degli strumenti: pipeline](../../assets/chapters/67_tools/TOOLS-02/candidate-v50.png)

La seconda figura mette a confronto «Esecuzione e osservazione» e il limite discusso in «Idempotenza e side effect».


## Esempio Python eseguito

La prova locale di output strutturato e uso degli strumenti parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Output strutturato e uso degli strumenti», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «output strutturato e uso degli strumenti» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    request = {"tool": "lookup_order", "order_id": "A1"}
    allowlist = {"lookup_order"}
    allowed = request["tool"] in allowlist and bool(request["order_id"])
    return {"allowed": allowed, "request": request, "invariant": "tool execution requires validation outside generated text"}
```

Esecuzione con `python snip_67_contract.py`:

```text
{"allowed": true, "invariant": "tool execution requires validation outside generated text", "request": {"order_id": "A1", "tool": "lookup_order"}}
```

Il test associato è [`code/test_67_contract.py`](code/test_67_contract.py); l'output versionato è [`code/outputs/SNIP-67-001.txt`](code/outputs/SNIP-67-001.txt).


## Come si collegano i passaggi

- **Da «Schema dell'output» a «Selezione del tool».** JSON Schema, grammar o tipi stabiliscono campi e vincoli. Il modello sceglie una funzione tra opzioni descritte. «Schema dell'output» nomina il confine e «Selezione del tool» implementa il percorso senza ereditare autorizzazioni implicite. Da «Schema dell'output» a «Selezione del tool» cambia la domanda osservabile. [SRC-67-001; SRC-67-002]

- **Da «Selezione del tool» a «Argomenti».** Il modello sceglie una funzione tra opzioni descritte. Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Componendo «Selezione del tool» e «Argomenti» diventa necessario conservare stato, identità e decisione. Il passaggio successivo rende misurabile «Argomenti». [SRC-67-002; SRC-67-003]

- **Da «Argomenti» a «Esecuzione e osservazione».** Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. «Esecuzione e osservazione» introduce failure e recovery prima di un side effect o di una perdita di stato. Da «Argomenti» a «Esecuzione e osservazione» cambia la domanda osservabile. [SRC-67-003; SRC-67-004]

- **Da «Esecuzione e osservazione» a «Idempotenza e side effect».** Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Operazioni di lettura e scrittura hanno rischi differenti. La chiusura su «Idempotenza e side effect» valuta il sistema completo, non soltanto il componente iniziale. Il passaggio successivo rende misurabile «Idempotenza e side effect». [SRC-67-004; SRC-67-001]

La catena completa produce risultato del tool o rifiuto tracciato a partire da nome, argomenti, scope e stato. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: schema valido non significa permesso di eseguire il side effect.


## Prove sui confini del sistema

1. Ricostruisci «Schema dell'output» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Selezione del tool», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Argomenti» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Esecuzione e osservazione» che produca una failure riconoscibile.
5. Per «Idempotenza e side effect», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «nome, argomenti, scope e stato» e arriva fino a «risultato del tool o rifiuto tracciato». Il limite da conservare è questo: schema valido non significa permesso di eseguire il side effect. Il confine di «Idempotenza e side effect» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
