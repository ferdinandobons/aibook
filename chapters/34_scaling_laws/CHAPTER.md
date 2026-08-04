<!--
chapter_id: CH-P07-SCALING
part_id: P07
order_key: 340
title: Scaling law e progettazione del modello
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 34. Scaling law e progettazione del modello

Una frase plausibile non basta a spiegare scaling law e progettazione del modello. L'oggetto è una curva empirica tra scala, compute e loss; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Fit empirico

Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato. [SRC-34-001]

Il caso minimo di «Fit empirico» si presenta così: un caso minimo con input punti con parametri, token, FLOP e loss e output «stima con intervallo osservato e costo». Non lo usiamo come decorazione: serve a rendere osservabile la frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato».

Per ricostruire «Fit empirico» annotiamo l'input «punti con parametri, token, FLOP e loss», poi l'operazione «fit, confronto isoFLOP ed estrapolazione», infine l'output «stima con intervallo osservato e costo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato».

Il passaggio da seguire in «Fit empirico» è quello descritto dalla frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Fit empirico» il controllo cambia una sola premessa della frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato». [SRC-34-001]

Il punto didattico di «Fit empirico» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stima con intervallo osservato e costo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Fit empirico» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. Da «Fit empirico» portiamo l'output «stima con intervallo osservato e costo»; non portiamo invece una conclusione oltre il caso locale.

## Allocazione compute-optimal

A budget fissato, modello e token competono. Il risultato dipende da ricetta e qualità dei dati. [SRC-34-002]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro punti, fit lineare locale e intervallo dichiarato. Da qui possiamo leggere la conseguenza dichiarata da «A budget fissato, modello e token competono».

Nel contratto locale, l'input «punti con parametri, token, FLOP e loss» entra, l'operazione «fit, confronto isoFLOP ed estrapolazione» modifica il percorso e l'output «stima con intervallo osservato e costo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Allocazione compute-optimal»; resta da controllare che un fit fuori dominio non è una legge garantita. La domanda locale è «A budget fissato, modello e token competono».

Una relazione di scaling è una misura nell'intervallo del setup osservato. Cambiare qualità dei dati, ricetta, obiettivo o costo di inference può spostare la conclusione, quindi l'extrapolation richiede ipotesi esplicite. Per «Allocazione compute-optimal» il controllo cambia una sola premessa della frase «A budget fissato, modello e token competono» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «A budget fissato, modello e token competono». [SRC-34-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il risultato dipende da ricetta e qualità dei dati. Il piccolo risultato resta un'illustrazione di «A budget fissato, modello e token competono», non una promessa generale.

La prova di «Allocazione compute-optimal» conserva input, operazione e output; poi esplicita quale parte di «A budget fissato, modello e token competono» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Esperimenti isoFLOP», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Esperimenti isoFLOP

Configurazioni con compute simile rendono osservabile la loss minima per budget. [SRC-34-003]

Per capire «Esperimenti isoFLOP» partiamo da questo caso: un caso in cui un fit fuori dominio non è una legge garantita. Il caso rende osservabile il punto centrale: «Configurazioni con compute simile rendono osservabile la loss minima per budget».

La sezione usa l'input «punti con parametri, token, FLOP e loss» come punto di partenza e l'output «stima con intervallo osservato e costo» come traccia d'uscita. La trasformazione concreta è «fit, confronto isoFLOP ed estrapolazione»; il caso non è completo se non dichiariamo anche che un fit fuori dominio non è una legge garantita. La condizione da isolare è «Configurazioni con compute simile rendono osservabile la loss minima per budget».

Una relazione di scaling è una misura nell'intervallo del setup osservato. Cambiare qualità dei dati, ricetta, obiettivo o costo di inference può spostare la conclusione, quindi l'extrapolation richiede ipotesi esplicite. Per «Esperimenti isoFLOP» il controllo cambia una sola premessa della frase «Configurazioni con compute simile rendono osservabile la loss minima per budget» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Configurazioni con compute simile rendono osservabile la loss minima per budget». [SRC-34-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Esperimenti isoFLOP» conserviamo l'osservazione collegata a «Configurazioni con compute simile rendono osservabile la loss minima per budget» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Esperimenti isoFLOP» cambiamo una sola condizione vicina alla frase «Configurazioni con compute simile rendono osservabile la loss minima per budget», teniamo fermo il resto e registriamo l'output «stima con intervallo osservato e costo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Extrapolation», riceve l'output «stima con intervallo osservato e costo» come base, ma dovrà formulare e verificare la propria distinzione.

![Scaling law e progettazione del modello: chart](../../assets/chapters/34_scaling_laws/SCALE-01/candidate-v48.png)

La figura SCALE-01 usa la famiglia chart. Il diagramma segue il passaggio: Fit, confronto isoFLOP ed estrapolazione. L'input è punti con parametri, token, FLOP e loss, l'output è stima con intervallo osservato e costo; il vincolo da controllare è che un fit fuori dominio non è una legge garantita.

## Extrapolation

Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala. [SRC-34-004]

Il caso minimo di «Extrapolation» si presenta così: due ricette con budget di token dichiarato, compute comparabile e loss osservata nello stesso intervallo. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala».

Per ricostruire «Extrapolation» annotiamo l'input «punti con parametri, token, FLOP e loss», poi l'operazione «fit, confronto isoFLOP ed estrapolazione», infine l'output «stima con intervallo osservato e costo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala».

Una relazione di scaling è una misura nell'intervallo del setup osservato. Cambiare qualità dei dati, ricetta, obiettivo o costo di inference può spostare la conclusione, quindi l'extrapolation richiede ipotesi esplicite. Per «Extrapolation» il controllo cambia una sola premessa della frase «Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala». [SRC-34-004]

Il punto didattico di «Extrapolation» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stima con intervallo osservato e costo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Extrapolation» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. Da «Extrapolation» portiamo l'output «stima con intervallo osservato e costo»; non portiamo invece una conclusione oltre il caso locale.

## Training e inference cost

Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio. [SRC-34-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Training e inference cost». Da qui possiamo leggere la conseguenza dichiarata da «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio».

Nel contratto locale, l'input «punti con parametri, token, FLOP e loss» entra, l'operazione «fit, confronto isoFLOP ed estrapolazione» modifica il percorso e l'output «stima con intervallo osservato e costo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Training e inference cost»; resta da controllare che un fit fuori dominio non è una legge garantita. La domanda locale è «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio».

Una relazione di scaling è una misura nell'intervallo del setup osservato. Cambiare qualità dei dati, ricetta, obiettivo o costo di inference può spostare la conclusione, quindi l'extrapolation richiede ipotesi esplicite. Per «Training e inference cost» il controllo cambia una sola premessa della frase «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio». [SRC-34-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio», non una promessa generale.

La prova di «Training e inference cost» conserva input, operazione e output; poi esplicita quale parte di «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «stima con intervallo osservato e costo» come evidenza locale e conserva il legame tra dati esposti e risultato come domanda aperta.

## Dal concetto alla situazione concreta: Fit empirico

Il caso intero parte dall'input «punti con parametri, token, FLOP e loss», applica l'operazione «fit, confronto isoFLOP ed estrapolazione» e osserva l'output «stima con intervallo osservato e costo». Un esempio controllato: quattro punti, fit lineare locale e intervallo dichiarato. La formula locale è:

$$
L(N) = L_inf + A N^(-alpha)
$$

Un fit empirico vale nell'intervallo e nel setup che lo hanno prodotto. [SRC-34-001]

![Scaling law e progettazione del modello: architecture](../../assets/chapters/34_scaling_laws/SCALE-02/candidate-v48.png)

La figura SCALE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Fit, confronto isoFLOP ed estrapolazione. L'input è punti con parametri, token, FLOP e loss, l'output è stima con intervallo osservato e costo; il vincolo da controllare è che un fit fuori dominio non è una legge garantita.

## Una prova ripetibile: Allocazione compute-optimal

Nel run Python rendiamo osservabile la frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-34-001.txt` documenta il caso senza pretendere una misura generale.

## Il trasferimento richiede altro: Training e inference cost

Il meccanismo di «Scaling law e progettazione del modello» non garantisce da solo che il sistema funzioni fuori dal caso guida. Un fit fuori dominio non è una legge garantita. Il limite osservato riguarda la frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il filo che passa oltre: Scaling law e progettazione del modello

Il percorso ha tenuto insieme una curva empirica tra scala, compute e loss, l'operazione «fit, confronto isoFLOP ed estrapolazione» e l'output «stima con intervallo osservato e costo». Le sezioni «Fit empirico», «Allocazione compute-optimal», «Training e inference cost» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: un fit fuori dominio non è una legge garantita. Il Capitolo 35, La ricetta di pretraining, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Fit empirico

1. Ricostruisci l'oggetto continuo a partire da «Fit empirico» e indica quale parte della frase «Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato» entra nel caso.
2. Spiega quale trasformazione collega «Fit empirico» a «Training e inference cost» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un fit fuori dominio non è una legge garantita.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Training e inference cost

1. Racconta «Fit empirico» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Allocazione compute-optimal» mantenendo il resto del setup invariato.
3. Per «Esperimenti isoFLOP», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Extrapolation» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Training e inference cost» senza confondere livelli diversi.

## Dove verificare definizioni e risultati: Scaling law e progettazione del modello

Per «Scaling law e progettazione del modello», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto popolazione, manifest e stato del run. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a popolazione, manifest e stato del run.
