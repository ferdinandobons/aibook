<!--
chapter_id: CH-P13-EVAL-DESIGN
part_id: P13
order_key: 830
title: Progettare una valutazione
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 83. Progettare una valutazione

La richiesta «Il pacco non è arrivato» resta il caso guida. In questo capitolo la usiamo per distinguere un claim valutativo e il protocollo che lo rende misurabile, trasformazione e risultato, senza nascondere i dettagli tecnici.

## Decisione e claim

Una valutazione parte dalla decisione che deve sostenere. Il claim deve nominare popolazione, condizioni, metrica e incertezza. [SRC-83-001]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro predizioni producono accuracy pari a 0,75 e una failure esplicita. Da qui possiamo leggere la conseguenza dichiarata da «Una valutazione parte dalla decisione che deve sostenere».

La sezione usa l'input «task, dataset, predizioni, riferimento e metriche» come punto di partenza e l'output «stima, intervallo, errori e decisione» come traccia d'uscita. La trasformazione concreta è «scelta della metrica, giudice, slice e report»; il caso non è completo se non dichiariamo anche che una metrica risponde solo alla domanda per cui è stata progettata. La condizione da isolare è «Una valutazione parte dalla decisione che deve sostenere».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La scheda di prova conserva fonte, data, configurazione e decisione, permettendo di distinguere novità editoriale da evidenza ripetuta. La verifica resta ancorata a «Una valutazione parte dalla decisione che deve sostenere». [SRC-83-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Decisione e claim» conserviamo l'osservazione collegata a «Una valutazione parte dalla decisione che deve sostenere» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Decisione e claim» conserva input, operazione e output; poi esplicita quale parte di «Una valutazione parte dalla decisione che deve sostenere» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Task e dataset», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Task e dataset

Prompt, input, reference e rubric devono rappresentare l'uso previsto. Split e cutoff impediscono contaminazione intenzionale. [SRC-83-002]

Per capire «Task e dataset» partiamo da questo caso: due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Il caso rende osservabile il punto centrale: «Prompt, input, reference e rubric devono rappresentare l'uso previsto».

Per ricostruire «Task e dataset» annotiamo l'input «task, dataset, predizioni, riferimento e metriche», poi l'operazione «scelta della metrica, giudice, slice e report», infine l'output «stima, intervallo, errori e decisione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Prompt, input, reference e rubric devono rappresentare l'uso previsto».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Task e dataset» il controllo cambia una sola premessa della frase «Prompt, input, reference e rubric devono rappresentare l'uso previsto» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Prompt, input, reference e rubric devono rappresentare l'uso previsto». [SRC-83-002]

Il punto didattico di «Task e dataset» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stima, intervallo, errori e decisione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Task e dataset» cambiamo una sola condizione vicina alla frase «Prompt, input, reference e rubric devono rappresentare l'uso previsto», teniamo fermo il resto e registriamo l'output «stima, intervallo, errori e decisione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Metriche», riceve l'output «stima, intervallo, errori e decisione» come base, ma dovrà formulare e verificare la propria distinzione.

## Metriche

Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. Aggregazione e slice devono essere predefinite. [SRC-83-003]

Il caso minimo di «Metriche» si presenta così: quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti».

Nel contratto locale, l'input «task, dataset, predizioni, riferimento e metriche» entra, l'operazione «scelta della metrica, giudice, slice e report» modifica il percorso e l'output «stima, intervallo, errori e decisione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Metriche»; resta da controllare che una metrica risponde solo alla domanda per cui è stata progettata. La domanda locale è «Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza. La verifica resta ancorata a «Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti». [SRC-83-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Aggregazione e slice devono essere predefinite. Il piccolo risultato resta un'illustrazione di «Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti», non una promessa generale.

Il controllo minimo di «Metriche» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Metriche» portiamo l'output «stima, intervallo, errori e decisione»; non portiamo invece una conclusione oltre il caso locale.

## Giudici modello

LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. Serve calibrazione con giudizi indipendenti. [SRC-83-004]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato. Da qui possiamo leggere la conseguenza dichiarata da «LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric».

La sezione usa l'input «task, dataset, predizioni, riferimento e metriche» come punto di partenza e l'output «stima, intervallo, errori e decisione» come traccia d'uscita. La trasformazione concreta è «scelta della metrica, giudice, slice e report»; il caso non è completo se non dichiariamo anche che una metrica risponde solo alla domanda per cui è stata progettata. La condizione da isolare è «LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza. La verifica resta ancorata a «LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric». [SRC-83-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Giudici modello» conserviamo l'osservazione collegata a «LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Giudici modello» conserva input, operazione e output; poi esplicita quale parte di «LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Report», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Progettare una valutazione: checklist](../../assets/chapters/83_eval_design/DESIGN-01/candidate-v48.png)

La figura DESIGN-01 usa la famiglia checklist. Il diagramma segue il passaggio: Scelta della metrica, giudice, slice e report. L'input è task, dataset, predizioni, riferimento e metriche, l'output è stima, intervallo, errori e decisione; il vincolo da controllare è che una metrica risponde solo alla domanda per cui è stata progettata.

## Report

Intervalli, fallimenti, costi e limiti accompagnano il punteggio. Una leaderboard non sostituisce il protocollo. [SRC-83-001]

Per capire «Report» partiamo da questo caso: quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato. Il caso rende osservabile il punto centrale: «Intervalli, fallimenti, costi e limiti accompagnano il punteggio».

Per ricostruire «Report» annotiamo l'input «task, dataset, predizioni, riferimento e metriche», poi l'operazione «scelta della metrica, giudice, slice e report», infine l'output «stima, intervallo, errori e decisione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Intervalli, fallimenti, costi e limiti accompagnano il punteggio».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza. La verifica resta ancorata a «Intervalli, fallimenti, costi e limiti accompagnano il punteggio». [SRC-83-001]

Il punto didattico di «Report» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stima, intervallo, errori e decisione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Report» cambiamo una sola condizione vicina alla frase «Intervalli, fallimenti, costi e limiti accompagnano il punteggio», teniamo fermo il resto e registriamo l'output «stima, intervallo, errori e decisione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## La definizione messa alla prova: Decisione e claim

Il caso intero parte dall'input «task, dataset, predizioni, riferimento e metriche», applica l'operazione «scelta della metrica, giudice, slice e report» e osserva l'output «stima, intervallo, errori e decisione». Un esempio controllato: accuracy media accompagnata da una slice fallita. Lo schema compatto è:

$$
estimate = metric(outputs, references, protocol)
$$

È una notazione di interfaccia, non un'identità numerica completa. La metrica ha significato soltanto rispetto alla domanda di valutazione. [SRC-83-001]

![Progettare una valutazione: funnel](../../assets/chapters/83_eval_design/DESIGN-02/candidate-v48.png)

La figura DESIGN-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Scelta della metrica, giudice, slice e report. L'input è task, dataset, predizioni, riferimento e metriche, l'output è stima, intervallo, errori e decisione; il vincolo da controllare è che una metrica risponde solo alla domanda per cui è stata progettata.

## Un esperimento piccolo ma leggibile: Task e dataset

Nel run Python rendiamo osservabile la frase «Una valutazione parte dalla decisione che deve sostenere» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-83-001.txt` documenta il caso senza pretendere una misura generale.

## Il confine del caso guida: Report

Il meccanismo di «Progettare una valutazione» non garantisce da solo che il sistema funzioni fuori dal caso guida. Una metrica risponde solo alla domanda per cui è stata progettata. Il limite osservato riguarda la frase «Una valutazione parte dalla decisione che deve sostenere»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il contratto che rimane: Progettare una valutazione

Il percorso ha tenuto insieme un claim valutativo e il protocollo che lo rende misurabile, l'operazione «scelta della metrica, giudice, slice e report» e l'output «stima, intervallo, errori e decisione». Le sezioni «Decisione e claim», «Task e dataset», «Report» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: una metrica risponde solo alla domanda per cui è stata progettata. Il Capitolo 84, Fattualità, incertezza e affidabilità, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Decisione e claim

1. Ricostruisci l'oggetto continuo a partire da «Decisione e claim» e indica quale parte della frase «Una valutazione parte dalla decisione che deve sostenere» entra nel caso.
2. Spiega quale trasformazione collega «Decisione e claim» a «Report» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: una metrica risponde solo alla domanda per cui è stata progettata.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Intervalli, fallimenti, costi e limiti accompagnano il punteggio» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Report

1. Ricostruisci input e output di «Decisione e claim» usando un esempio di tre righe.
2. Modifica una sola variabile in «Task e dataset» e anticipa l'invariante che dovrebbe restare.
3. Metti «Metriche» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Giudici modello».
5. Formula per «Report» una domanda che separi meccanismo e qualità del sistema.

## Riferimenti e prove riproducibili: Progettare una valutazione

Per «Progettare una valutazione», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto protocollo, slice e decisione. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
