<!--
chapter_id: CH-P05-GENERATIVE-FOUNDATIONS
part_id: P05
order_key: 200
title: Fondamenti della modellazione generativa
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: exception
code_exception: Il capitolo confronta famiglie generative a livello concettuale; le implementazioni verificabili sono distribuite nei capitoli 21-25.
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 20. Fondamenti della modellazione generativa

Questa mappa di fondamenti della modellazione generativa parte da «Imparare una distribuzione» e arriva a «Qualità, copertura e valutazione» conservando le proprietà che non sono state misurate. L'oggetto osservato è una distribuzione sui dati o su una variabile latente. Il contratto locale dichiara input, un dato x, un rumore epsilon o una variabile z; operazione, valutazione di likelihood, trasformazione o campionamento; output, una probabilità, un punteggio o un campione. Il primo esempio osservabile è Un caso minimo con input un dato x, un rumore epsilon o una variabile z e output «una probabilità, un punteggio o un campione». Il limite da non nascondere è: un campione plausibile non dimostra copertura dell'intera distribuzione.

## Imparare una distribuzione

Un modello generativo descrive o campiona dati secondo una distribuzione. Densità, likelihood e sampling sono contratti distinti. [SRC-20-001]

La variabile latente collega un prior a una distribuzione osservabile.

**Caso da seguire.** Un caso minimo con input un dato x, un rumore epsilon o una variabile z e output «una probabilità, un punteggio o un campione».

**Controllo.** Per «Imparare una distribuzione», classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Modelli espliciti e impliciti

Un modello esplicito assegna una densità o probabilità valutabile. Un modello implicito definisce il campionamento senza una likelihood semplice. [SRC-20-002]

**Caso da seguire.** Tre probabilità che sommano a 1 prima della selezione.

**Controllo.** Cambia la proprietà che distingue «Modelli espliciti e impliciti» dalle categorie vicine. Nel caso «Modelli espliciti e impliciti», se la classificazione non cambia, la distinzione va formulata meglio.


## Variabili latenti

Una variabile latente introduce struttura non osservata. L'inferenza deve collegare dati e latenti, esattamente o mediante approssimazione. [SRC-20-003]

**Caso da seguire.** Tre probabilità che sommano a 1 prima del campionamento, distinguendo plausibilità del campione e copertura.

**Controllo.** Per «Variabili latenti», confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


La relazione centrale può essere scritta come:

$$
p(x)=\int p(x|z)p(z)\,dz
$$

La variabile latente collega un prior a una distribuzione osservabile. [SRC-20-001]


![Fondamenti della modellazione generativa: pipeline](../../assets/chapters/20_generative_foundations/FOUNDATI-01/candidate-v49.png)

La prima figura segue il percorso da «Imparare una distribuzione» a «Variabili latenti».


## Energy-based model

Una energia non normalizzata assegna punteggi alle configurazioni. La costante di partizione rende difficile la likelihood in molti casi. [SRC-20-004]

**Caso da seguire.** Per una variabile Bernoulli, la likelihood valuta la probabilità del dato osservato; un campione plausibile non dimostra che la distribuzione sia coperta.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Energy-based model» e quale invece sarebbe irrilevante.


## Qualità, copertura e valutazione

Campioni plausibili non garantiscono copertura. Likelihood e precision-recall generativa rispondono a domande diverse e richiedono protocolli dichiarati. [SRC-20-005]

**Caso da seguire.** Per «Qualità, copertura e valutazione» si mantiene l'input del capitolo e si isola questa condizione: Campioni plausibili non garantiscono copertura.

**Controllo.** Per «Qualità, copertura e valutazione», limita la conclusione alla proprietà dichiarata: Likelihood e precision-recall generativa rispondono a domande diverse e richiedono protocolli dichiarati. Nel caso «Qualità, copertura e valutazione», le dimensioni non osservate restano aperte.


![Fondamenti della modellazione generativa: timeline](../../assets/chapters/20_generative_foundations/FOUNDATI-02/candidate-v49.png)

La seconda figura mette a confronto «Energy-based model» e il limite discusso in «Qualità, copertura e valutazione».


## Perché non forziamo un esempio Python

Il capitolo confronta famiglie generative a livello concettuale; le implementazioni verificabili sono distribuite nei capitoli 21-25. La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi.


## Come si collegano i passaggi

- **Da «Imparare una distribuzione» a «Modelli espliciti e impliciti».** Un modello generativo descrive o campiona dati secondo una distribuzione. Un modello esplicito assegna una densità o probabilità valutabile. «Imparare una distribuzione» stabilisce l'asse e «Modelli espliciti e impliciti» aggiunge una proprietà senza creare una graduatoria. Il passaggio successivo rende misurabile «Modelli espliciti e impliciti». [SRC-20-001; SRC-20-002]

- **Da «Modelli espliciti e impliciti» a «Variabili latenti».** Un modello esplicito assegna una densità o probabilità valutabile. Una variabile latente introduce struttura non osservata. Il confronto tra «Modelli espliciti e impliciti» e «Variabili latenti» mantiene le categorie distinguibili sullo stesso caso. Da «Modelli espliciti e impliciti» a «Variabili latenti» cambia la domanda osservabile. [SRC-20-002; SRC-20-003]

- **Da «Variabili latenti» a «Energy-based model».** Una variabile latente introduce struttura non osservata. Una energia non normalizzata assegna punteggi alle configurazioni. «Energy-based model» mostra il punto in cui l'asse di «Variabili latenti» non è più sufficiente. Il passaggio successivo rende misurabile «Energy-based model». [SRC-20-003; SRC-20-004]

- **Da «Energy-based model» a «Qualità, copertura e valutazione».** Una energia non normalizzata assegna punteggi alle configurazioni. Campioni plausibili non garantiscono copertura. Il passaggio su «Qualità, copertura e valutazione» riunisce più dimensioni senza cancellarne i limiti. Da «Energy-based model» a «Qualità, copertura e valutazione» cambia la domanda osservabile. [SRC-20-004; SRC-20-005]

La catena completa produce una probabilità, un punteggio o un campione a partire da un dato x, un rumore epsilon o una variabile z. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un campione plausibile non dimostra copertura dell'intera distribuzione.


## Domande per distinguere le categorie

1. Ricostruisci «Imparare una distribuzione» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Modelli espliciti e impliciti», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Variabili latenti» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Energy-based model» che produca una failure riconoscibile.
5. Per «Qualità, copertura e valutazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «un dato x, un rumore epsilon o una variabile z» e arriva fino a «una probabilità, un punteggio o un campione». Il limite da conservare è questo: un campione plausibile non dimostra copertura dell'intera distribuzione. Il confronto di «Qualità, copertura e valutazione» resta verificabile nei dossier [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md) e [`CLAIMS.md`](CLAIMS.md), senza trasformare la mappa in una graduatoria.
