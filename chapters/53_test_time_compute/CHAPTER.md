<!--
chapter_id: CH-P09-TEST-TIME-COMPUTE
part_id: P09
order_key: 530
title: Test-time compute, ricerca e controllo del budget
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 53. Test-time compute, ricerca e controllo del budget

La lezione prende un caso piccolo e lo accompagna da «Più compute dopo il training» fino a «Metriche costo-qualità», senza saltare i passaggi. L'oggetto osservato è un budget di compute aggiunto durante l'inferenza. Il contratto locale dichiara input, prompt, numero di campioni, token e deadline; operazione, best-of-n, tree search e adaptive compute; output, risposta, costo, latenza e qualità. Per fissare il riferimento usiamo Tre candidati vengono valutati entro un budget comune e si conserva il punteggio migliore. Il limite da non nascondere è: qualità e costo devono essere riportati insieme.

## Più compute dopo il training

Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta. [SRC-53-001]

Il test-time compute è una risorsa da misurare insieme a qualità e latenza.

**Caso da seguire.** Tre candidati vengono valutati entro un budget comune e si conserva il punteggio migliore.

**Controllo.** Per «Più compute dopo il training», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Più compute dopo il training», il vincolo da conservare è: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta.


## Best-of-n

Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla diversità e dalla qualità del ranking. [SRC-53-002]

**Caso da seguire.** Quattro campioni con un budget massimo di token.

**Controllo.** Per «Best-of-n», ricalcola il caso a mano e con lo snippet. Nel caso «Best-of-n», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


Lo schema seguente rende esplicito il confine tra il meccanismo e la sua valutazione.

**Schema concettuale.** `budget = samples * tokens`

Il test-time compute è una risorsa da misurare insieme a qualità e latenza. [SRC-53-001]


![Test-time compute, ricerca e controllo del budget: branch](../../assets/chapters/53_test_time_compute/COMPUTE-01/candidate-v48.png)

La prima figura segue il percorso da «Più compute dopo il training» a «Tree search».


## Tree search

Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget definiscono il costo. [SRC-53-003]

**Caso da seguire.** Un caso in cui qualità e costo devono essere riportati insieme.

**Controllo.** Per «Tree search», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Tree search».


## Adaptive compute

Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. La stima di difficoltà può essere errata. [SRC-53-004]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Per «Adaptive compute», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Adaptive compute», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il caso computazionale di test-time compute, ricerca e controllo del budget è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Test-time compute, ricerca e controllo del budget», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «test-time compute, ricerca e controllo del budget».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    candidates = [0.4, 0.6, 0.5]
    best = max(candidates)
    return {"samples": len(candidates), "best_score": best, "invariant": "test-time compute changes the selection budget, not the base model weights"}
```

Esecuzione con `python snip_53_contract.py`:

```text
{"best_score": 0.6, "invariant": "test-time compute changes the selection budget, not the base model weights", "samples": 3}
```

Il test associato è [`code/test_53_contract.py`](code/test_53_contract.py); l'output versionato è [`code/outputs/SNIP-53-001.txt`](code/outputs/SNIP-53-001.txt).


## Metriche costo-qualità

Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier. [SRC-53-001]

**Caso da seguire.** Quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato.

**Controllo.** Per «Metriche costo-qualità», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Metriche costo-qualità» non si applica.


![Test-time compute, ricerca e controllo del budget: chart](../../assets/chapters/53_test_time_compute/COMPUTE-02/candidate-v48.png)

La seconda figura mette a confronto «Adaptive compute» e il limite discusso in «Metriche costo-qualità».


## Come si collegano i passaggi

- **Da «Più compute dopo il training» a «Best-of-n».** Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta. Un proposer genera n candidate e un verifier seleziona. Tra «Più compute dopo il training» e «Best-of-n» l'ingresso viene fissato prima della regola che produce il valore. Da «Più compute dopo il training» a «Best-of-n» cambia la domanda osservabile. [SRC-53-001; SRC-53-002]

- **Da «Best-of-n» a «Tree search».** Un proposer genera n candidate e un verifier seleziona. Stati parziali vengono espansi, valutati e potati. Nel caso «Tree search» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Tree search». [SRC-53-002; SRC-53-003]

- **Da «Tree search» a «Adaptive compute».** Stati parziali vengono espansi, valutati e potati. Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. Dopo «Tree search», la variante di «Adaptive compute» cambia una proprietà alla volta. Da «Tree search» a «Adaptive compute» cambia la domanda osservabile. [SRC-53-003; SRC-53-004]

- **Da «Adaptive compute» a «Metriche costo-qualità».** Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier. Da «Metriche costo-qualità» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Metriche costo-qualità». [SRC-53-004; SRC-53-001]

La catena completa produce risposta, costo, latenza e qualità a partire da prompt, numero di campioni, token e deadline. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: qualità e costo devono essere riportati insieme.


## Esercizi sul meccanismo

1. Ricostruisci «Più compute dopo il training» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Best-of-n», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Tree search» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Adaptive compute» che produca una failure riconoscibile.
5. Per «Metriche costo-qualità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «prompt, numero di campioni, token e deadline» e arriva fino a «risposta, costo, latenza e qualità». Il limite da conservare è questo: qualità e costo devono essere riportati insieme. La formula e il codice collegati a «Metriche costo-qualità» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
