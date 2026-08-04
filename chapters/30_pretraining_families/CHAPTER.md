<!--
chapter_id: CH-P06-PRETRAIN-FAMILIES
part_id: P06
order_key: 300
title: Famiglie architetturali e obiettivi di pretraining
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: exception
code_exception: Il capitolo è una mappa tra architetture e obiettivi; il Transformer eseguibile è nel capitolo 29 e le ricette di training iniziano dal 32.
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 30. Famiglie architetturali e obiettivi di pretraining

Il punto di vista di famiglie architetturali e obiettivi di pretraining nasce dal confronto tra «Encoder-only» e «Architettura e obiettivo», non da una graduatoria. L'oggetto osservato è una famiglia architetturale legata al proprio obiettivo. Il contratto locale dichiara input, sequenza, mask e target di pretraining; operazione, encoder, decoder, span corruption o causal prediction; output, rappresentazione o distribuzione predittiva. Il primo esempio osservabile è Un caso minimo con input sequenza, mask e target di pretraining e output «rappresentazione o distribuzione predittiva». Il limite da non nascondere è: architettura e objective non possono essere scambiati senza cambiare il compito.

## Encoder-only

Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione. [SRC-30-001]

L'obiettivo stabilisce quali posizioni contribuiscono alla loss.

**Caso da seguire.** Un caso minimo con input sequenza, mask e target di pretraining e output «rappresentazione o distribuzione predittiva».

**Controllo.** Per «Encoder-only», classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Decoder-only

Un decoder causale predice token successivi e supporta generazione incrementale. [SRC-30-002]

**Caso da seguire.** Lo stesso testo con target masked e causal separati.

**Controllo.** Cambia la proprietà che distingue «Decoder-only» dalle categorie vicine. Nel caso «Decoder-only», se la classificazione non cambia, la distinzione va formulata meglio.


## Encoder-decoder

T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. [SRC-30-003]

**Caso da seguire.** Un caso in cui architettura e objective non possono essere scambiati senza cambiare il compito.

**Controllo.** Per «Encoder-decoder», confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


La relazione centrale può essere scritta come:

$$
L= -\sum_t log p(x_t|x_{<t})
$$

L'obiettivo stabilisce quali posizioni contribuiscono alla loss. [SRC-30-001]


![Famiglie architetturali e obiettivi di pretraining: matrix](../../assets/chapters/30_pretraining_families/FAMILIES-01/candidate-v48.png)

La prima figura segue il percorso da «Encoder-only» a «Encoder-decoder».


## Masked, causal e span corruption

Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. [SRC-30-004]

**Caso da seguire.** Una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Masked, causal e span corruption» e quale invece sarebbe irrilevante.


## Architettura e obiettivo

La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti. [SRC-30-001]

**Caso da seguire.** Un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita.

**Controllo.** Per «Architettura e obiettivo», limita la conclusione alla proprietà dichiarata: Confrontarli richiede dati, compute e task coerenti. Nel caso «Architettura e obiettivo», le dimensioni non osservate restano aperte.


![Famiglie architetturali e obiettivi di pretraining: branch](../../assets/chapters/30_pretraining_families/FAMILIES-02/candidate-v48.png)

La seconda figura mette a confronto «Masked, causal e span corruption» e il limite discusso in «Architettura e obiettivo».


## Perché non forziamo un esempio Python

Il capitolo è una mappa tra architetture e obiettivi; il Transformer eseguibile è nel capitolo 29 e le ricette di training iniziano dal 32. La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi.


## Come si collegano i passaggi

- **Da «Encoder-only» a «Decoder-only».** Modelli come BERT usano contesto bidirezionale e obiettivi masked. Un decoder causale predice token successivi e supporta generazione incrementale. «Encoder-only» stabilisce l'asse e «Decoder-only» aggiunge una proprietà senza creare una graduatoria. Il passaggio successivo rende misurabile «Decoder-only». [SRC-30-001; SRC-30-002]

- **Da «Decoder-only» a «Encoder-decoder».** Un decoder causale predice token successivi e supporta generazione incrementale. T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. Il confronto tra «Decoder-only» e «Encoder-decoder» mantiene le categorie distinguibili sullo stesso caso. Da «Decoder-only» a «Encoder-decoder» cambia la domanda osservabile. [SRC-30-002; SRC-30-003]

- **Da «Encoder-decoder» a «Masked, causal e span corruption».** T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. «Masked, causal e span corruption» mostra il punto in cui l'asse di «Encoder-decoder» non è più sufficiente. Il passaggio successivo rende misurabile «Masked, causal e span corruption». [SRC-30-003; SRC-30-004]

- **Da «Masked, causal e span corruption» a «Architettura e obiettivo».** Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. La forma del modello e l'obiettivo sono assi separati. Il passaggio su «Architettura e obiettivo» riunisce più dimensioni senza cancellarne i limiti. Da «Masked, causal e span corruption» a «Architettura e obiettivo» cambia la domanda osservabile. [SRC-30-004; SRC-30-001]

La catena completa produce rappresentazione o distribuzione predittiva a partire da sequenza, mask e target di pretraining. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: architettura e objective non possono essere scambiati senza cambiare il compito.


## Domande per distinguere le categorie

1. Ricostruisci «Encoder-only» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Decoder-only», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Encoder-decoder» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Masked, causal e span corruption» che produca una failure riconoscibile.
5. Per «Architettura e obiettivo», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «sequenza, mask e target di pretraining» e arriva fino a «rappresentazione o distribuzione predittiva». Il limite da conservare è questo: architettura e objective non possono essere scambiati senza cambiare il compito. Il confronto di «Architettura e obiettivo» resta verificabile nei dossier [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md) e [`CLAIMS.md`](CLAIMS.md), senza trasformare la mappa in una graduatoria.
