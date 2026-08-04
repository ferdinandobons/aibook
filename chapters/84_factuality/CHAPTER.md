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

La domanda guida di questa lezione è come collegare «Correttezza e supporto» e «Verifica e retrieval» senza perdere il contratto tecnico di fattualità, incertezza e affidabilità. L'oggetto osservato è una risposta con evidenza, confidenza e possibilità di errore. Il contratto locale è: input, claim, predizione, fonti e score di confidenza; operazione, verifica, calibrazione, astensione e retrieval; output, risposta supportata o astensione motivata. Il caso guida è questo: Una risposta con score 0,95 può essere falsa, perciò la confidence viene confrontata con la correttezza. Il confine da mantenere esplicito è: confidenza alta non certifica la verità fattuale.

## Correttezza e supporto

Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata. [SRC-84-001]

Confidenza, correttezza e factuality sono quantità da separare.

**Caso da seguire.** Una risposta con score 0,95 può essere falsa, perciò la confidence viene confrontata con la correttezza.

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Hallucination

Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La tassonomia deve precedere la metrica. [SRC-84-002]

**Caso da seguire.** Tre risposte corrette e una confidente ma non supportata.

**Controllo.** Cambia la proprietà che distingue «Hallucination» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Calibrazione

Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. [SRC-84-003]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Calibrazione» e all'output risposta supportata o astensione motivata.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Fattualità, incertezza e affidabilità: funnel](../../assets/chapters/84_factuality/FACTUALITY-01/candidate-v48.png)

La prima figura segue il percorso da «Correttezza e supporto» a «Calibrazione».


## Astensione

Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e accuracy conditional vanno riportate insieme. [SRC-84-004]

**Caso da seguire.** Su un piccolo insieme, la metrica viene calcolata insieme a una slice e a un caso fallito. La media non sostituisce la diagnosi.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Astensione» e quale invece sarebbe irrilevante.


## Verifica e retrieval

Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La provenienza deve restare tracciabile. [SRC-84-001]

**Caso da seguire.** Una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale.

**Controllo.** Limita la conclusione alla proprietà dichiarata: La provenienza deve restare tracciabile. Le dimensioni non osservate restano aperte.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
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

- **Da «Correttezza e supporto» a «Hallucination».** Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata. Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-84-001; SRC-84-002]

- **Da «Hallucination» a «Calibrazione».** Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-84-002; SRC-84-003]

- **Da «Calibrazione» a «Astensione».** Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-84-003; SRC-84-004]

- **Da «Astensione» a «Verifica e retrieval».** Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-84-004; SRC-84-001]

La catena completa produce risposta supportata o astensione motivata a partire da claim, predizione, fonti e score di confidenza. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: confidenza alta non certifica la verità fattuale.


## Domande per distinguere le categorie

1. Ricostruisci «Correttezza e supporto» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Hallucination», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Calibrazione» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Astensione» che produca una failure riconoscibile.
5. Per «Verifica e retrieval», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «claim, predizione, fonti e score di confidenza» e arriva fino a «risposta supportata o astensione motivata». Il limite da conservare è questo: confidenza alta non certifica la verità fattuale. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
