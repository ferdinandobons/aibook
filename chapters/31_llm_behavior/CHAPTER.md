<!--
chapter_id: CH-P06-LLM-BEHAVIOR
part_id: P06
order_key: 310
title: Dalla rappresentazione linguistica agli LLM
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 31. Dalla rappresentazione linguistica agli LLM

Per distinguere dalla rappresentazione linguistica agli llm, mettiamo in relazione «Distribuzione del token successivo» e «Modello e sistema» mantenendo separati gli assi osservati. L'oggetto osservato è un prompt e la distribuzione del token successivo. Il contratto locale dichiara input, prefisso tokenizzato, esempi e temperatura dichiarati; operazione, in-context learning, decoding e calibrazione; output, logits, risposta e confidenza misurabile. Per fissare il riferimento usiamo Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Il limite da non nascondere è: probabilità, comportamento osservato e correttezza non sono sinonimi.

## Distribuzione del token successivo

Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce una distribuzione, non una risposta già scelta. [SRC-31-001]

La softmax trasforma logits condizionati in una distribuzione; la scelta del token viene dopo.

**Caso da seguire.** Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati.

**Controllo.** Per «Distribuzione del token successivo», classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Prompt e dimostrazioni

Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta invariato durante in-context learning. [SRC-31-002]

**Caso da seguire.** Lo stesso prompt con greedy e top-p confrontati.

**Controllo.** Cambia la proprietà che distingue «Prompt e dimostrazioni» dalle categorie vicine. Nel caso «Prompt e dimostrazioni», se la classificazione non cambia, la distinzione va formulata meglio.


## Decoding

Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria. [SRC-31-003]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Per «Decoding», confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


La relazione centrale può essere scritta come:

$$
p(x_t | x_{<t}) = softmax(z_t)
$$

La softmax trasforma logits condizionati in una distribuzione; la scelta del token viene dopo. [SRC-31-001]


![Dalla rappresentazione linguistica agli LLM: matrix](../../assets/chapters/31_llm_behavior/LLM-01/candidate-v48.png)

La prima figura segue il percorso da «Distribuzione del token successivo» a «Decoding».


## Calibrazione

Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti. [SRC-31-004]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Calibrazione» e all'output logits, risposta e confidenza misurabile.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Calibrazione» e quale invece sarebbe irrilevante.


## Modello e sistema

Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato. [SRC-31-001]

**Caso da seguire.** Un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita.

**Controllo.** Per «Modello e sistema», limita la conclusione alla proprietà dichiarata: Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato. Nel caso «Modello e sistema», le dimensioni non osservate restano aperte.


## Esempio Python eseguito

La prova locale di dalla rappresentazione linguistica agli llm parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Dalla rappresentazione linguistica agli LLM», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «dalla rappresentazione linguistica agli llm» e interrompe l'interpretazione prima dell'output.

```python
def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    logits = [2.0, 1.0, 0.0]
    probabilities = normalize(logits)
    demonstrations = 2
    chosen = max(range(len(probabilities)), key=probabilities.__getitem__)
    return {"demonstrations": demonstrations, "probabilities": [round(value, 6) for value in probabilities], "chosen": chosen, "invariant": "decoding selects from a distribution and does not certify truth"}
```

Esecuzione con `python snip_31_contract.py`:

```text
{"chosen": 0, "demonstrations": 2, "invariant": "decoding selects from a distribution and does not certify truth", "probabilities": [0.665241, 0.244728, 0.090031]}
```

Il test associato è [`code/test_31_contract.py`](code/test_31_contract.py); l'output versionato è [`code/outputs/SNIP-31-001.txt`](code/outputs/SNIP-31-001.txt).


![Dalla rappresentazione linguistica agli LLM: branch](../../assets/chapters/31_llm_behavior/LLM-02/candidate-v48.png)

La seconda figura mette a confronto «Calibrazione» e il limite discusso in «Modello e sistema».


## Come si collegano i passaggi

- **Da «Distribuzione del token successivo» a «Prompt e dimostrazioni».** Un LLM autoregressivo produce logits condizionati sul prefisso. Istruzioni ed esempi entrano nel contesto senza un optimizer step. «Distribuzione del token successivo» stabilisce l'asse e «Prompt e dimostrazioni» aggiunge una proprietà senza creare una graduatoria. Da «Distribuzione del token successivo» a «Prompt e dimostrazioni» cambia la domanda osservabile. [SRC-31-001; SRC-31-002]

- **Da «Prompt e dimostrazioni» a «Decoding».** Istruzioni ed esempi entrano nel contesto senza un optimizer step. Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria. Il confronto tra «Prompt e dimostrazioni» e «Decoding» mantiene le categorie distinguibili sullo stesso caso. Il passaggio successivo rende misurabile «Decoding». [SRC-31-002; SRC-31-003]

- **Da «Decoding» a «Calibrazione».** Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria. Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti. «Calibrazione» mostra il punto in cui l'asse di «Decoding» non è più sufficiente. Da «Decoding» a «Calibrazione» cambia la domanda osservabile. [SRC-31-003; SRC-31-004]

- **Da «Calibrazione» a «Modello e sistema».** Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti. Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato. Il passaggio su «Modello e sistema» riunisce più dimensioni senza cancellarne i limiti. Il passaggio successivo rende misurabile «Modello e sistema». [SRC-31-004; SRC-31-001]

La catena completa produce logits, risposta e confidenza misurabile a partire da prefisso tokenizzato, esempi e temperatura dichiarati. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: probabilità, comportamento osservato e correttezza non sono sinonimi.


## Domande per distinguere le categorie

1. Ricostruisci «Distribuzione del token successivo» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Prompt e dimostrazioni», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Decoding» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Calibrazione» che produca una failure riconoscibile.
5. Per «Modello e sistema», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «prefisso tokenizzato, esempi e temperatura dichiarati» e arriva fino a «logits, risposta e confidenza misurabile». Il limite da conservare è questo: probabilità, comportamento osservato e correttezza non sono sinonimi. Il confronto di «Modello e sistema» resta verificabile nei dossier [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md) e [`CLAIMS.md`](CLAIMS.md), senza trasformare la mappa in una graduatoria.
