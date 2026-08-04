<!--
chapter_id: CH-P13-SYSTEM-EVAL
part_id: P13
order_key: 850
title: Valutare contesto lungo, RAG, multimodalità e agenti
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 85. Valutare contesto lungo, RAG, multimodalità e agenti

Il Capitolo 84, Fattualità, incertezza e affidabilità, ha lasciato disponibile un sistema composto da modello, contesto, tool e interfaccia. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «eval end-to-end, stress, slice e monitoraggio» e verifichiamo che misurare il modello isolato non misura il comportamento del sistema.

## Contesto lungo

Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale. [SRC-85-001]

Il caso minimo di «Contesto lungo» si presenta così: il RAG risponde correttamente ma la citation fallisce, quindi il sistema non passa il gate end-to-end. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale».

Per ricostruire «Contesto lungo» annotiamo l'input «task, componenti, trace e policy», poi l'operazione «eval end-to-end, stress, slice e monitoraggio», infine l'output «score di sistema, failure e regressione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La variabile da isolare è il pattern di visibilità o di riuso: la stessa shape può corrispondere a dipendenze e costi diversi. La verifica resta ancorata a «Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale». [SRC-85-001]

Il punto didattico di «Contesto lungo» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score di sistema, failure e regressione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Contesto lungo» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Contesto lungo» portiamo l'output «score di sistema, failure e regressione»; non portiamo invece una conclusione oltre il caso locale.

## RAG

Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili. [SRC-85-002]

Prima del nome tecnico fissiamo la situazione: consideriamo una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Da qui possiamo leggere la conseguenza dichiarata da «Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili».

Nel contratto locale, l'input «task, componenti, trace e policy» entra, l'operazione «eval end-to-end, stress, slice e monitoraggio» modifica il percorso e l'output «score di sistema, failure e regressione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «RAG»; resta da controllare che misurare il modello isolato non misura il comportamento del sistema. La domanda locale è «Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili». [SRC-85-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili», non una promessa generale.

La prova di «RAG» conserva input, operazione e output; poi esplicita quale parte di «Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Multimodalità», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Multimodalità

Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche. [SRC-85-003]

Per capire «Multimodalità» partiamo da questo caso: due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione. Il caso rende osservabile il punto centrale: «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche».

La sezione usa l'input «task, componenti, trace e policy» come punto di partenza e l'output «score di sistema, failure e regressione» come traccia d'uscita. La trasformazione concreta è «eval end-to-end, stress, slice e monitoraggio»; il caso non è completo se non dichiariamo anche che misurare il modello isolato non misura il comportamento del sistema. La condizione da isolare è «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Multimodalità» il controllo cambia una sola premessa della frase «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche». [SRC-85-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Multimodalità» conserviamo l'osservazione collegata a «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Multimodalità» cambiamo una sola condizione vicina alla frase «Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche», teniamo fermo il resto e registriamo l'output «score di sistema, failure e regressione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Agenti», riceve l'output «score di sistema, failure e regressione» come base, ma dovrà formulare e verificare la propria distinzione.

![Valutare contesto lungo, RAG, multimodalità e agenti: funnel](../../assets/chapters/85_system_eval/EVAL-01/candidate-v48.png)

La figura EVAL-01 usa la famiglia funnel. Il diagramma segue il passaggio: Eval end-to-end, stress, slice e monitoraggio. L'input è task, componenti, trace e policy, l'output è score di sistema, failure e regressione; il vincolo da controllare è che misurare il modello isolato non misura il comportamento del sistema.

## Agenti

Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili. [SRC-85-004]

Il caso minimo di «Agenti» si presenta così: una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili».

Per ricostruire «Agenti» annotiamo l'input «task, componenti, trace e policy», poi l'operazione «eval end-to-end, stress, slice e monitoraggio», infine l'output «score di sistema, failure e regressione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili». [SRC-85-004]

Il punto didattico di «Agenti» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score di sistema, failure e regressione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Agenti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Agenti» portiamo l'output «score di sistema, failure e regressione»; non portiamo invece una conclusione oltre il caso locale.

## Evaluation in production

Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli. [SRC-85-001]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Evaluation in production» e all'output score di sistema, failure e regressione. Da qui possiamo leggere la conseguenza dichiarata da «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli».

Nel contratto locale, l'input «task, componenti, trace e policy» entra, l'operazione «eval end-to-end, stress, slice e monitoraggio» modifica il percorso e l'output «score di sistema, failure e regressione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Evaluation in production»; resta da controllare che misurare il modello isolato non misura il comportamento del sistema. La domanda locale è «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Evaluation in production» il controllo cambia una sola premessa della frase «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli». [SRC-85-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli», non una promessa generale.

La prova di «Evaluation in production» conserva input, operazione e output; poi esplicita quale parte di «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «score di sistema, failure e regressione» come evidenza locale e conserva il confine tra evidenza e interpretazione come domanda aperta.

## Un caso dall'input all'output: Contesto lungo

Il caso intero parte dall'input «task, componenti, trace e policy», applica l'operazione «eval end-to-end, stress, slice e monitoraggio» e osserva l'output «score di sistema, failure e regressione». Un esempio controllato: un RAG che risponde bene ma cita una fonte irrilevante. Lo schema compatto è:

$$
system = model + tools + policy + ui
$$

È una notazione di interfaccia, non un'identità numerica completa. La valutazione di sistema deve includere componenti che il modello non controlla. [SRC-85-001]

![Valutare contesto lungo, RAG, multimodalità e agenti: architecture](../../assets/chapters/85_system_eval/EVAL-02/candidate-v48.png)

La figura EVAL-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Eval end-to-end, stress, slice e monitoraggio. L'input è task, componenti, trace e policy, l'output è score di sistema, failure e regressione; il vincolo da controllare è che misurare il modello isolato non misura il comportamento del sistema.

## Dal meccanismo alla prova locale: RAG

Il file `code/snip_85_contract.py` collega il contratto del capitolo alla frase «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-85-001.txt` conserva il risultato ripetibile del caso locale.

## Dove il risultato si ferma: Evaluation in production

Il meccanismo di «Valutare contesto lungo, RAG, multimodalità e agenti» resta legato al contratto locale. Misurare il modello isolato non misura il comportamento del sistema. Prima di generalizzare la frase «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Che cosa portiamo avanti: Valutare contesto lungo, RAG, multimodalità e agenti

Abbiamo seguito un sistema composto da modello, contesto, tool e interfaccia, partendo dall'input «task, componenti, trace e policy» e arrivando all'output «score di sistema, failure e regressione». Le sezioni «Contesto lungo», «RAG», «Evaluation in production» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: misurare il modello isolato non misura il comportamento del sistema. Il Capitolo 86, Interpretabilità delle rappresentazioni e dei circuiti, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Contesto lungo

1. Ricostruisci l'oggetto continuo a partire da «Contesto lungo» e indica quale parte della frase «Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale» entra nel caso.
2. Spiega quale trasformazione collega «Contesto lungo» a «Evaluation in production» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: misurare il modello isolato non misura il comportamento del sistema.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Evaluation in production

1. Ricostruisci «Contesto lungo» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «RAG» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Multimodalità» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Agenti» in un test ripetibile.
5. Spiega come trasferire «Evaluation in production» senza portare con sé una promessa non misurata.

## Fonti, codice e materiali: Valutare contesto lungo, RAG, multimodalità e agenti

Il dossier di «Valutare contesto lungo, RAG, multimodalità e agenti» in `FONTI_PRIMARIE.md` separa definizioni, risultati e la differenza tra media e failure; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
