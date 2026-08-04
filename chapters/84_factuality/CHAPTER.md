<!--
chapter_id: CH-P13-FACTUALITY
part_id: P13
order_key: 840
title: Fattualità, incertezza e affidabilità
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 84. Fattualità, incertezza e affidabilità

Il punto di vista di fattualità, incertezza e affidabilità nasce dal confronto tra «Correttezza e supporto» e «Verifica e retrieval», non da una graduatoria. L'oggetto osservato è una risposta con evidenza, confidenza e possibilità di errore. Il contratto locale dichiara input, claim, predizione, fonti e score di confidenza; operazione, verifica, calibrazione, astensione e retrieval; output, risposta supportata o astensione motivata. Il primo esempio osservabile è Una risposta con score 0,95 può essere falsa, perciò la confidence viene confrontata con la correttezza. Il limite da non nascondere è: confidenza alta non certifica la verità fattuale.

## Correttezza e supporto

Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata. [SRC-84-001]

Confidenza, correttezza e factuality sono quantità da separare.

**Caso da seguire.** Una risposta con score 0,95 può essere falsa, perciò la confidence viene confrontata con la correttezza.

**Controllo.** Per «Correttezza e supporto», classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Hallucination

Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La tassonomia deve precedere la metrica. [SRC-84-002]

**Caso da seguire.** Tre risposte corrette e una confidente ma non supportata.

**Controllo.** Cambia la proprietà che distingue «Hallucination» dalle categorie vicine. Nel caso «Hallucination», se la classificazione non cambia, la distinzione va formulata meglio.


## Calibrazione

Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. [SRC-84-003]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Calibrazione» e all'output risposta supportata o astensione motivata.

**Controllo.** Per «Calibrazione», confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


La relazione centrale può essere scritta come:

$$
calibration = P(correct | confidence)
$$

Confidenza, correttezza e factuality sono quantità da separare. [SRC-84-001]


![Fattualità, incertezza e affidabilità: funnel](../../assets/chapters/84_factuality/FACTUALITY-01/candidate-v48.png)

La prima figura segue il percorso da «Correttezza e supporto» a «Calibrazione».


## Astensione

Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e accuracy conditional vanno riportate insieme. [SRC-84-004]

**Caso da seguire.** Su un piccolo insieme, la metrica viene calcolata insieme a una slice e a un caso fallito. La media non sostituisce la diagnosi.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Astensione» e quale invece sarebbe irrilevante.


## Verifica e retrieval

Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La provenienza deve restare tracciabile. [SRC-84-001]

**Caso da seguire.** Una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale.

**Controllo.** Per «Verifica e retrieval», limita la conclusione alla proprietà dichiarata: La provenienza deve restare tracciabile. Nel caso «Verifica e retrieval», le dimensioni non osservate restano aperte.


## Esempio Python eseguito

Per rendere osservabile fattualità, incertezza e affidabilità, il capitolo conserva qui l'artefatto Python eseguito. Per «Fattualità, incertezza e affidabilità», il caso di default usa valori piccoli per isolare il meccanismo. Il test rifiuta anche un caso non documentato di «fattualità, incertezza e affidabilità».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    claims = [(True, 0.9), (True, 0.8), (False, 0.95), (True, 0.7)]
    confident_errors = sum((not correct) and score >= 0.9 for correct, score in claims)
    return {"accuracy": sum(correct for correct, _score in claims) / len(claims), "confident_errors": confident_errors, "invariant": "confidence is evaluated against factual correctness, not substituted for it"}
```

Esecuzione con `python snip_84_contract.py`:

```text
{"accuracy": 0.75, "confident_errors": 1, "invariant": "confidence is evaluated against factual correctness, not substituted for it"}
```

Il test associato è [`code/test_84_contract.py`](code/test_84_contract.py); l'output versionato è [`code/outputs/SNIP-84-001.txt`](code/outputs/SNIP-84-001.txt).


![Fattualità, incertezza e affidabilità: scatter](../../assets/chapters/84_factuality/FACTUALITY-02/candidate-v48.png)

La seconda figura mette a confronto «Astensione» e il limite discusso in «Verifica e retrieval».


## Come si collegano i passaggi

- **Da «Correttezza e supporto» a «Hallucination».** Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata. Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. «Correttezza e supporto» stabilisce l'asse e «Hallucination» aggiunge una proprietà senza creare una graduatoria. Il passaggio successivo rende misurabile «Hallucination». [SRC-84-001; SRC-84-002]

- **Da «Hallucination» a «Calibrazione».** Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. Il confronto tra «Hallucination» e «Calibrazione» mantiene le categorie distinguibili sullo stesso caso. Da «Hallucination» a «Calibrazione» cambia la domanda osservabile. [SRC-84-002; SRC-84-003]

- **Da «Calibrazione» a «Astensione».** Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. «Astensione» mostra il punto in cui l'asse di «Calibrazione» non è più sufficiente. Il passaggio successivo rende misurabile «Astensione». [SRC-84-003; SRC-84-004]

- **Da «Astensione» a «Verifica e retrieval».** Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. Il passaggio su «Verifica e retrieval» riunisce più dimensioni senza cancellarne i limiti. Da «Astensione» a «Verifica e retrieval» cambia la domanda osservabile. [SRC-84-004; SRC-84-001]

La catena completa produce risposta supportata o astensione motivata a partire da claim, predizione, fonti e score di confidenza. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: confidenza alta non certifica la verità fattuale.


## Domande per distinguere le categorie

1. Ricostruisci «Correttezza e supporto» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Hallucination», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Calibrazione» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Astensione» che produca una failure riconoscibile.
5. Per «Verifica e retrieval», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «claim, predizione, fonti e score di confidenza» e arriva fino a «risposta supportata o astensione motivata». Il limite da conservare è questo: confidenza alta non certifica la verità fattuale. Il confronto di «Verifica e retrieval» resta verificabile nei dossier [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md) e [`CLAIMS.md`](CLAIMS.md), senza trasformare la mappa in una graduatoria.
