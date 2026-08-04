<!--
chapter_id: CH-P05-GENERATIVE-FOUNDATIONS
part_id: P05
order_key: 200
title: Fondamenti della modellazione generativa
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 20. Fondamenti della modellazione generativa

Il Capitolo 19, Representation learning, ha lasciato disponibile una distribuzione sui dati o su una variabile latente. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «valutazione di likelihood, trasformazione o campionamento» e verifichiamo che un campione plausibile non dimostra copertura dell'intera distribuzione.

## Imparare una distribuzione

Un modello generativo descrive o campiona dati secondo una distribuzione. Densità, likelihood e sampling sono contratti distinti. [SRC-20-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso minimo con input un dato x, un rumore epsilon o una variabile z e output «una probabilità, un punteggio o un campione». Da qui possiamo leggere la conseguenza dichiarata da «Un modello generativo descrive o campiona dati secondo una distribuzione».

La sezione usa l'input «un dato x, un rumore epsilon o una variabile z» come punto di partenza e l'output «una probabilità, un punteggio o un campione» come traccia d'uscita. La trasformazione concreta è «valutazione di likelihood, trasformazione o campionamento»; il caso non è completo se non dichiariamo anche che un campione plausibile non dimostra copertura dell'intera distribuzione. La condizione da isolare è «Un modello generativo descrive o campiona dati secondo una distribuzione».

Un modello generativo può assegnare un punteggio ai dati, definire una densità oppure descrivere direttamente un percorso di campionamento. Likelihood e qualità del campione sono osservazioni diverse e vanno tenute separate. Per «Imparare una distribuzione» il controllo cambia una sola premessa della frase «Un modello generativo descrive o campiona dati secondo una distribuzione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un modello generativo descrive o campiona dati secondo una distribuzione». [SRC-20-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Imparare una distribuzione» conserviamo l'osservazione collegata a «Un modello generativo descrive o campiona dati secondo una distribuzione» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Imparare una distribuzione» conserva input, operazione e output; poi esplicita quale parte di «Un modello generativo descrive o campiona dati secondo una distribuzione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Modelli espliciti e impliciti», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Modelli espliciti e impliciti

Un modello esplicito assegna una densità o probabilità valutabile. Un modello implicito definisce il campionamento senza una likelihood semplice. [SRC-20-002]

Per capire «Modelli espliciti e impliciti» partiamo da questo caso: tre probabilità che sommano a 1 prima della selezione. Il caso rende osservabile il punto centrale: «Un modello esplicito assegna una densità o probabilità valutabile».

Per ricostruire «Modelli espliciti e impliciti» annotiamo l'input «un dato x, un rumore epsilon o una variabile z», poi l'operazione «valutazione di likelihood, trasformazione o campionamento», infine l'output «una probabilità, un punteggio o un campione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un modello esplicito assegna una densità o probabilità valutabile».

Un modello generativo può assegnare un punteggio ai dati, definire una densità oppure descrivere direttamente un percorso di campionamento. Likelihood e qualità del campione sono osservazioni diverse e vanno tenute separate. Per «Modelli espliciti e impliciti» il controllo cambia una sola premessa della frase «Un modello esplicito assegna una densità o probabilità valutabile» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un modello esplicito assegna una densità o probabilità valutabile». [SRC-20-002]

Il punto didattico di «Modelli espliciti e impliciti» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «una probabilità, un punteggio o un campione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Modelli espliciti e impliciti» cambiamo una sola condizione vicina alla frase «Un modello esplicito assegna una densità o probabilità valutabile», teniamo fermo il resto e registriamo l'output «una probabilità, un punteggio o un campione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Variabili latenti», riceve l'output «una probabilità, un punteggio o un campione» come base, ma dovrà formulare e verificare la propria distinzione.

## Variabili latenti

Una variabile latente introduce struttura non osservata. L'inferenza deve collegare dati e latenti, esattamente o mediante approssimazione. [SRC-20-003]

Il caso minimo di «Variabili latenti» si presenta così: tre probabilità che sommano a 1 prima del campionamento, distinguendo plausibilità del campione e copertura. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Una variabile latente introduce struttura non osservata».

Nel contratto locale, l'input «un dato x, un rumore epsilon o una variabile z» entra, l'operazione «valutazione di likelihood, trasformazione o campionamento» modifica il percorso e l'output «una probabilità, un punteggio o un campione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Variabili latenti»; resta da controllare che un campione plausibile non dimostra copertura dell'intera distribuzione. La domanda locale è «Una variabile latente introduce struttura non osservata».

Il passaggio da seguire in «Variabili latenti» è quello descritto dalla frase «Una variabile latente introduce struttura non osservata»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Variabili latenti» il controllo cambia una sola premessa della frase «Una variabile latente introduce struttura non osservata» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una variabile latente introduce struttura non osservata». [SRC-20-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. L'inferenza deve collegare dati e latenti, esattamente o mediante approssimazione. Il piccolo risultato resta un'illustrazione di «Una variabile latente introduce struttura non osservata», non una promessa generale.

Il controllo minimo di «Variabili latenti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del rapporto tra distribuzione e campione. Da «Variabili latenti» portiamo l'output «una probabilità, un punteggio o un campione»; non portiamo invece una conclusione oltre il caso locale.

## Energy-based model

Una energia non normalizzata assegna punteggi alle configurazioni. La costante di partizione rende difficile la likelihood in molti casi. [SRC-20-004]

Prima del nome tecnico fissiamo la situazione: consideriamo per una variabile Bernoulli, la likelihood valuta la probabilità del dato osservato; un campione plausibile non dimostra che la distribuzione sia coperta. Da qui possiamo leggere la conseguenza dichiarata da «Una energia non normalizzata assegna punteggi alle configurazioni».

La sezione usa l'input «un dato x, un rumore epsilon o una variabile z» come punto di partenza e l'output «una probabilità, un punteggio o un campione» come traccia d'uscita. La trasformazione concreta è «valutazione di likelihood, trasformazione o campionamento»; il caso non è completo se non dichiariamo anche che un campione plausibile non dimostra copertura dell'intera distribuzione. La condizione da isolare è «Una energia non normalizzata assegna punteggi alle configurazioni».

Un modello generativo può assegnare un punteggio ai dati, definire una densità oppure descrivere direttamente un percorso di campionamento. Likelihood e qualità del campione sono osservazioni diverse e vanno tenute separate. Per «Energy-based model» il controllo cambia una sola premessa della frase «Una energia non normalizzata assegna punteggi alle configurazioni» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una energia non normalizzata assegna punteggi alle configurazioni». [SRC-20-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Energy-based model» conserviamo l'osservazione collegata a «Una energia non normalizzata assegna punteggi alle configurazioni» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Energy-based model» conserva input, operazione e output; poi esplicita quale parte di «Una energia non normalizzata assegna punteggi alle configurazioni» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Qualità, copertura e valutazione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Fondamenti della modellazione generativa: pipeline](../../assets/chapters/20_generative_foundations/FOUNDATI-01/candidate-v49.png)

La figura FOUNDATI-01 usa la famiglia pipeline. Il percorso dall'input di fondamenti della modellazione generativa all'output osservabile è leggibile da sinistra a destra.

## Qualità, copertura e valutazione

Campioni plausibili non garantiscono copertura. Likelihood, precision-recall generativa e valutazione umana rispondono a domande diverse. [SRC-20-001]

Per capire «Qualità, copertura e valutazione» partiamo da questo caso: per una variabile Bernoulli, la likelihood valuta la probabilità del dato osservato; un campione plausibile non dimostra che la distribuzione sia coperta. Il caso rende osservabile il punto centrale: «Campioni plausibili non garantiscono copertura».

Per ricostruire «Qualità, copertura e valutazione» annotiamo l'input «un dato x, un rumore epsilon o una variabile z», poi l'operazione «valutazione di likelihood, trasformazione o campionamento», infine l'output «una probabilità, un punteggio o un campione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Campioni plausibili non garantiscono copertura».

Una valutazione deve collegare claim, popolazione, protocollo e decisione. Media, slice, failure, giudice e incertezza misurano aspetti diversi e non diventano intercambiabili perché condividono una tabella. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Campioni plausibili non garantiscono copertura». [SRC-20-001]

Il punto didattico di «Qualità, copertura e valutazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «una probabilità, un punteggio o un campione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Qualità, copertura e valutazione» cambiamo una sola condizione vicina alla frase «Campioni plausibili non garantiscono copertura», teniamo fermo il resto e registriamo l'output «una probabilità, un punteggio o un campione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Un caso dall'input all'output: Imparare una distribuzione

Il caso intero parte dall'input «un dato x, un rumore epsilon o una variabile z», applica l'operazione «valutazione di likelihood, trasformazione o campionamento» e osserva l'output «una probabilità, un punteggio o un campione». Un esempio controllato: tre probabilità che sommano a 1 prima della selezione. La formula locale è:

$$
p(x)=\int p(x|z)p(z)\,dz
$$

La variabile latente collega un prior a una distribuzione osservabile. [SRC-20-001]

![Fondamenti della modellazione generativa: timeline](../../assets/chapters/20_generative_foundations/FOUNDATI-02/candidate-v49.png)

La figura FOUNDATI-02 cambia composizione rispetto alla prima. La stessa informazione viene seguita lungo i passi del processo.

## Dal meccanismo alla prova locale: Modelli espliciti e impliciti

Lo snippet locale mette in esecuzione questo caso: tre probabilità che sommano a 1 prima della selezione. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-20-001.txt`, come evidenza locale e non come benchmark di produzione.

## Dove il risultato si ferma: Qualità, copertura e valutazione

Il caso di «Fondamenti della modellazione generativa» non certifica un servizio completo. Un campione plausibile non dimostra copertura dell'intera distribuzione. La domanda successiva è se «Campioni plausibili non garantiscono copertura» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Che cosa portiamo avanti: Fondamenti della modellazione generativa

Il filo della lezione va dall'input «un dato x, un rumore epsilon o una variabile z» all'output «una probabilità, un punteggio o un campione». Nei passaggi «Imparare una distribuzione», «Modelli espliciti e impliciti», «Qualità, copertura e valutazione» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: un campione plausibile non dimostra copertura dell'intera distribuzione. Il Capitolo 21, Modelli autoregressivi, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Imparare una distribuzione

1. Ricostruisci l'oggetto continuo a partire da «Imparare una distribuzione» e indica quale parte della frase «Un modello generativo descrive o campiona dati secondo una distribuzione» entra nel caso.
2. Spiega quale trasformazione collega «Imparare una distribuzione» a «Qualità, copertura e valutazione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un campione plausibile non dimostra copertura dell'intera distribuzione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Campioni plausibili non garantiscono copertura» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Qualità, copertura e valutazione

1. Racconta «Imparare una distribuzione» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Modelli espliciti e impliciti» mantenendo il resto del setup invariato.
3. Per «Variabili latenti», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Energy-based model» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Qualità, copertura e valutazione» senza confondere livelli diversi.

## Fonti, codice e materiali: Fondamenti della modellazione generativa

Per ricontrollare «Fondamenti della modellazione generativa», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il passaggio dal latente all'osservabile oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione al rapporto tra distribuzione e campione.
