<!--
chapter_id: CH-P13-EVAL-DESIGN
part_id: P13
order_key: 830
title: Progettare una valutazione
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 83. Progettare una valutazione

La domanda guida di questa lezione è come collegare «Decisione e claim» e «Report» senza perdere il contratto tecnico di progettare una valutazione. L'oggetto osservato è un claim valutativo e il protocollo che lo rende misurabile. Il contratto locale è: input, task, dataset, predizioni, riferimento e metriche; operazione, scelta della metrica, giudice, slice e report; output, stima, intervallo, errori e decisione. Il caso guida è questo: Quattro predizioni producono accuracy pari a 0,75 e una failure esplicita. Il confine da mantenere esplicito è: una metrica risponde solo alla domanda per cui è stata progettata.

## Decisione e claim

Una valutazione parte dalla decisione che deve sostenere. Il claim deve nominare popolazione, condizioni, metrica e incertezza. [SRC-83-001]

La metrica ha significato soltanto rispetto alla domanda di valutazione.

**Caso da seguire.** Quattro predizioni producono accuracy pari a 0,75 e una failure esplicita.

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Task e dataset

Prompt, input, reference e rubric devono rappresentare l'uso previsto. Split e cutoff impediscono contaminazione intenzionale. [SRC-83-002]

**Caso da seguire.** Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata.

**Controllo.** Cambia la proprietà che distingue «Task e dataset» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Metriche

Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. Aggregazione e slice devono essere predefinite. [SRC-83-003]

**Caso da seguire.** Quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Progettare una valutazione: checklist](../../assets/chapters/83_eval_design/DESIGN-01/candidate-v48.png)

La prima figura segue il percorso da «Decisione e claim» a «Metriche».


## Giudici modello

LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. Serve calibrazione con giudizi indipendenti. [SRC-83-004]

**Caso da seguire.** Per «Giudici modello» si mantiene l'input del capitolo e si isola questa condizione: LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Giudici modello» e quale invece sarebbe irrilevante.


## Report

Intervalli, fallimenti, costi e limiti accompagnano il punteggio. Una leaderboard non sostituisce il protocollo. [SRC-83-001]

**Caso da seguire.** Per «Report» si mantiene l'input del capitolo e si isola questa condizione: Intervalli, fallimenti, costi e limiti accompagnano il punteggio.

**Controllo.** Limita la conclusione alla proprietà dichiarata: Una leaderboard non sostituisce il protocollo. Le dimensioni non osservate restano aperte.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    predictions = [1, 1, 0, 1]
    labels = [1, 0, 0, 1]
    correct = sum(prediction == label for prediction, label in zip(predictions, labels))
    failures = [index for index, pair in enumerate(zip(predictions, labels)) if pair[0] != pair[1]]
    return {"accuracy": correct / len(labels), "failures": failures, "invariant": "a metric is reported with its decision target and failure cases"}
```

Esecuzione con `python snip_83_contract.py`:

```text
{"accuracy": 0.75, "failures": [1], "invariant": "a metric is reported with its decision target and failure cases"}
```

Il test associato è [`code/test_83_contract.py`](code/test_83_contract.py); l'output versionato è [`code/outputs/SNIP-83-001.txt`](code/outputs/SNIP-83-001.txt).


![Progettare una valutazione: funnel](../../assets/chapters/83_eval_design/DESIGN-02/candidate-v48.png)

La seconda figura mette a confronto «Giudici modello» e il limite discusso in «Report».


## Come si collegano i passaggi

- **Da «Decisione e claim» a «Task e dataset».** Una valutazione parte dalla decisione che deve sostenere. Prompt, input, reference e rubric devono rappresentare l'uso previsto. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-83-001; SRC-83-002]

- **Da «Task e dataset» a «Metriche».** Prompt, input, reference e rubric devono rappresentare l'uso previsto. Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-83-002; SRC-83-003]

- **Da «Metriche» a «Giudici modello».** Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-83-003; SRC-83-004]

- **Da «Giudici modello» a «Report».** LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. Intervalli, fallimenti, costi e limiti accompagnano il punteggio. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-83-004; SRC-83-001]

La catena completa produce stima, intervallo, errori e decisione a partire da task, dataset, predizioni, riferimento e metriche. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una metrica risponde solo alla domanda per cui è stata progettata.


## Domande per distinguere le categorie

1. Ricostruisci «Decisione e claim» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Task e dataset», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Metriche» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Giudici modello» che produca una failure riconoscibile.
5. Per «Report», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «task, dataset, predizioni, riferimento e metriche» e arriva fino a «stima, intervallo, errori e decisione». Il limite da conservare è questo: una metrica risponde solo alla domanda per cui è stata progettata. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
