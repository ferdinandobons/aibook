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

La domanda guida di questa lezione è come collegare «Encoder-only» e «Architettura e obiettivo» senza perdere il contratto tecnico di famiglie architetturali e obiettivi di pretraining. L'oggetto osservato è una famiglia architetturale legata al proprio obiettivo. Il contratto locale è: input, sequenza, mask e target di pretraining; operazione, encoder, decoder, span corruption o causal prediction; output, rappresentazione o distribuzione predittiva. Il caso guida è questo: Un caso minimo con input sequenza, mask e target di pretraining e output «rappresentazione o distribuzione predittiva». Il confine da mantenere esplicito è: architettura e objective non possono essere scambiati senza cambiare il compito.

## Encoder-only

Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione. [SRC-30-001]

L'obiettivo stabilisce quali posizioni contribuiscono alla loss.

**Caso da seguire.** Un caso minimo con input sequenza, mask e target di pretraining e output «rappresentazione o distribuzione predittiva».

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Decoder-only

Un decoder causale predice token successivi e supporta generazione incrementale. [SRC-30-002]

**Caso da seguire.** Lo stesso testo con target masked e causal separati.

**Controllo.** Cambia la proprietà che distingue «Decoder-only» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Encoder-decoder

T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. [SRC-30-003]

**Caso da seguire.** Un caso in cui architettura e objective non possono essere scambiati senza cambiare il compito.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Famiglie architetturali e obiettivi di pretraining: matrix](../../assets/chapters/30_pretraining_families/FAMILIES-01/candidate-v48.png)

La prima figura segue il percorso da «Encoder-only» a «Encoder-decoder».


## Masked, causal e span corruption

Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. [SRC-30-004]

**Caso da seguire.** Una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Masked, causal e span corruption» e quale invece sarebbe irrilevante.


## Architettura e obiettivo

La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti. [SRC-30-001]

**Caso da seguire.** Un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita.

**Controllo.** Limita la conclusione alla proprietà dichiarata: Confrontarli richiede dati, compute e task coerenti. Le dimensioni non osservate restano aperte.


![Famiglie architetturali e obiettivi di pretraining: branch](../../assets/chapters/30_pretraining_families/FAMILIES-02/candidate-v48.png)

La seconda figura mette a confronto «Masked, causal e span corruption» e il limite discusso in «Architettura e obiettivo».


## Perché non forziamo un esempio Python

Il capitolo è una mappa tra architetture e obiettivi; il Transformer eseguibile è nel capitolo 29 e le ricette di training iniziano dal 32. La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi.


## Come si collegano i passaggi

- **Da «Encoder-only» a «Decoder-only».** Modelli come BERT usano contesto bidirezionale e obiettivi masked. Un decoder causale predice token successivi e supporta generazione incrementale. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-30-001; SRC-30-002]

- **Da «Decoder-only» a «Encoder-decoder».** Un decoder causale predice token successivi e supporta generazione incrementale. T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-30-002; SRC-30-003]

- **Da «Encoder-decoder» a «Masked, causal e span corruption».** T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-30-003; SRC-30-004]

- **Da «Masked, causal e span corruption» a «Architettura e obiettivo».** Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. La forma del modello e l'obiettivo sono assi separati. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-30-004; SRC-30-001]

La catena completa produce rappresentazione o distribuzione predittiva a partire da sequenza, mask e target di pretraining. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: architettura e objective non possono essere scambiati senza cambiare il compito.


## Domande per distinguere le categorie

1. Ricostruisci «Encoder-only» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Decoder-only», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Encoder-decoder» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Masked, causal e span corruption» che produca una failure riconoscibile.
5. Per «Architettura e obiettivo», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «sequenza, mask e target di pretraining» e arriva fino a «rappresentazione o distribuzione predittiva». Il limite da conservare è questo: architettura e objective non possono essere scambiati senza cambiare il compito. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
