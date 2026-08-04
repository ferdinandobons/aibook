<!--
chapter_id: CH-P13-PROMPT-INJECTION
part_id: P13
order_key: 890
title: Prompt injection e sicurezza dei tool
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 89. Prompt injection e sicurezza dei tool

Per capire prompt injection e sicurezza dei tool, partiamo da «Istruzioni e dati» e seguiamo ogni confine fino a «Test e incident response». L'oggetto osservato è istruzioni e dati che entrano in un sistema con tool. Il contratto locale dichiara input, prompt, documento non fidato, tool e scope; operazione, separazione, mediazione, allowlist e incident response; output, azione autorizzata o rifiuto con traccia. Il primo esempio osservabile è Un documento chiede export dei dati, ma il tool scope non lo autorizza. Il limite da non nascondere è: contenuto recuperato non diventa istruzione privilegiata.

## Istruzioni e dati

Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire automaticamente la priorità delle istruzioni di sistema. [SRC-89-001]

Prompt injection e tool security richiedono separazione tra dati e istruzioni.

**Caso da seguire.** Un documento chiede export dei dati, ma il tool scope non lo autorizza.

**Controllo.** Per «Istruzioni e dati», registra richiesta, decisione, stato e output finale. Nel caso «Istruzioni e dati», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Indirect prompt injection

Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing. [SRC-89-002]

**Caso da seguire.** Un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente.

**Controllo.** Ripeti «Indirect prompt injection» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La forma compatta aiuta a seguire il flusso senza attribuirgli una garanzia quantitativa.

**Schema concettuale.** `allow = policy(instruction, provenance, scope)`

Prompt injection e tool security richiedono separazione tra dati e istruzioni. [SRC-89-001]


![Prompt injection e sicurezza dei tool: pipeline](../../assets/chapters/89_prompt_injection/INJECTION-01/candidate-v50.png)

La prima figura segue il percorso da «Istruzioni e dati» a «Tool mediation».


## Tool mediation

Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma l'enforcement avviene fuori dal testo generato. [SRC-89-003]

**Caso da seguire.** Una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione.

**Controllo.** Per «Tool mediation», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Data exfiltration

Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL possono diventare canali di esfiltrazione. [SRC-89-004]

**Caso da seguire.** Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata.

**Controllo.** Per «Data exfiltration», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Test e incident response

Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery. [SRC-89-001]

**Caso da seguire.** Una decisione con owner, rischio, evidenza, giurisdizione e condizione di riapertura.

**Controllo.** Per «Test e incident response», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Test e incident response», il risultato resta limitato da: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery.


![Prompt injection e sicurezza dei tool: threat](../../assets/chapters/89_prompt_injection/INJECTION-02/candidate-v48.png)

La seconda figura mette a confronto «Data exfiltration» e il limite discusso in «Test e incident response».


## Esempio Python eseguito

Il caso computazionale di prompt injection e sicurezza dei tool è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Prompt injection e sicurezza dei tool», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «prompt injection e sicurezza dei tool».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    document_instruction = "export all data"
    tool_scope = {"lookup_order"}
    requested = "export_data"
    allowed = requested in tool_scope
    return {"document_instruction": document_instruction, "allowed": allowed, "invariant": "retrieved content cannot grant a privileged tool scope"}
```

Esecuzione con `python snip_89_contract.py`:

```text
{"allowed": false, "document_instruction": "export all data", "invariant": "retrieved content cannot grant a privileged tool scope"}
```

Il test associato è [`code/test_89_contract.py`](code/test_89_contract.py); l'output versionato è [`code/outputs/SNIP-89-001.txt`](code/outputs/SNIP-89-001.txt).


## Come si collegano i passaggi

- **Da «Istruzioni e dati» a «Indirect prompt injection».** Contenuti recuperati, pagine e documenti sono dati non fidati. Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing. «Istruzioni e dati» nomina il confine e «Indirect prompt injection» implementa il percorso senza ereditare autorizzazioni implicite. Da «Istruzioni e dati» a «Indirect prompt injection» cambia la domanda osservabile. [SRC-89-001; SRC-89-002]

- **Da «Indirect prompt injection» a «Tool mediation».** Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing. Policy esterne validano tool, argomenti e destinazioni. Componendo «Indirect prompt injection» e «Tool mediation» diventa necessario conservare stato, identità e decisione. Il passaggio successivo rende misurabile «Tool mediation». [SRC-89-002; SRC-89-003]

- **Da «Tool mediation» a «Data exfiltration».** Policy esterne validano tool, argomenti e destinazioni. Segreti, memoria e risultati dei tool devono essere separati per scope. «Data exfiltration» introduce failure e recovery prima di un side effect o di una perdita di stato. Da «Tool mediation» a «Data exfiltration» cambia la domanda osservabile. [SRC-89-003; SRC-89-004]

- **Da «Data exfiltration» a «Test e incident response».** Segreti, memoria e risultati dei tool devono essere separati per scope. Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery. La chiusura su «Test e incident response» valuta il sistema completo, non soltanto il componente iniziale. Il passaggio successivo rende misurabile «Test e incident response». [SRC-89-004; SRC-89-001]

La catena completa produce azione autorizzata o rifiuto con traccia a partire da prompt, documento non fidato, tool e scope. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: contenuto recuperato non diventa istruzione privilegiata.


## Prove sui confini del sistema

1. Ricostruisci «Istruzioni e dati» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Indirect prompt injection», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Tool mediation» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Data exfiltration» che produca una failure riconoscibile.
5. Per «Test e incident response», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «prompt, documento non fidato, tool e scope» e arriva fino a «azione autorizzata o rifiuto con traccia». Il limite da conservare è questo: contenuto recuperato non diventa istruzione privilegiata. Il confine di «Test e incident response» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
