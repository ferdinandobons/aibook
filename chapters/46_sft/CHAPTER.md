<!--
chapter_id: CH-P09-SFT
part_id: P09
order_key: 460
title: Supervised fine-tuning e instruction tuning
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 46. Supervised fine-tuning e instruction tuning

Finora abbiamo potuto descrivere una coppia prompt-risposta nel formato di instruction tuning. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 46 prendiamo l'input «messaggi, target, mask delle label e mixture» e lo seguiamo fino all'output «loss per token e comportamento adattato», dichiarando prima il contratto e poi il limite.

## Dal pretraining alle istruzioni

Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate. [SRC-46-001]

Il caso minimo di «Dal pretraining alle istruzioni» si presenta così: una conversazione con quattro token assegna la loss soltanto ai due token della risposta. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate».

Per ricostruire «Dal pretraining alle istruzioni» annotiamo l'input «messaggi, target, mask delle label e mixture», poi l'operazione «teacher forcing e aggiornamento supervisionato», infine l'output «loss per token e comportamento adattato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate».

Il passaggio da seguire in «Dal pretraining alle istruzioni» è quello descritto dalla frase «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Dal pretraining alle istruzioni» il controllo cambia una sola premessa della frase «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate». [SRC-46-001]

Il punto didattico di «Dal pretraining alle istruzioni» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss per token e comportamento adattato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Dal pretraining alle istruzioni» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di target, proxy e comportamento. Da «Dal pretraining alle istruzioni» portiamo l'output «loss per token e comportamento adattato»; non portiamo invece una conclusione oltre il caso locale.

## Formati conversazionali

Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. [SRC-46-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un messaggio utente e una risposta con loss solo sulla risposta. Da qui possiamo leggere la conseguenza dichiarata da «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente».

Nel contratto locale, l'input «messaggi, target, mask delle label e mixture» entra, l'operazione «teacher forcing e aggiornamento supervisionato» modifica il percorso e l'output «loss per token e comportamento adattato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Formati conversazionali»; resta da controllare che il formato dei dati e le label decidono che cosa viene ottimizzato. La domanda locale è «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente».

L'adattamento cambia il segnale presentato al modello e la porzione di output su cui si calcola la loss. Dati, mask, riferimenti e valutazione separata determinano quale comportamento viene effettivamente rinforzato. Per «Formati conversazionali» il controllo cambia una sola premessa della frase «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente». [SRC-46-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente», non una promessa generale.

La prova di «Formati conversazionali» conserva input, operazione e output; poi esplicita quale parte di «Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Instruction mixture», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Instruction mixture

Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile. [SRC-46-003]

Per capire «Instruction mixture» partiamo da questo caso: due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Il caso rende osservabile il punto centrale: «Compiti e domini vengono mescolati con pesi espliciti».

La sezione usa l'input «messaggi, target, mask delle label e mixture» come punto di partenza e l'output «loss per token e comportamento adattato» come traccia d'uscita. La trasformazione concreta è «teacher forcing e aggiornamento supervisionato»; il caso non è completo se non dichiariamo anche che il formato dei dati e le label decidono che cosa viene ottimizzato. La condizione da isolare è «Compiti e domini vengono mescolati con pesi espliciti».

La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Compiti e domini vengono mescolati con pesi espliciti». [SRC-46-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Instruction mixture» conserviamo l'osservazione collegata a «Compiti e domini vengono mescolati con pesi espliciti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Instruction mixture» cambiamo una sola condizione vicina alla frase «Compiti e domini vengono mescolati con pesi espliciti», teniamo fermo il resto e registriamo l'output «loss per token e comportamento adattato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Teacher forcing e generalizzazione», riceve l'output «loss per token e comportamento adattato» come base, ma dovrà formulare e verificare la propria distinzione.

![Supervised fine-tuning e instruction tuning: pipeline](../../assets/chapters/46_sft/SFT-01/candidate-v48.png)

La figura SFT-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Teacher forcing e aggiornamento supervisionato. L'input è messaggi, target, mask delle label e mixture, l'output è loss per token e comportamento adattato; il vincolo da controllare è che il formato dei dati e le label decidono che cosa viene ottimizzato.

## Teacher forcing e generalizzazione

Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati. [SRC-46-004]

Il caso minimo di «Teacher forcing e generalizzazione» si presenta così: un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Durante il training il modello vede il prefisso corretto».

Per ricostruire «Teacher forcing e generalizzazione» annotiamo l'input «messaggi, target, mask delle label e mixture», poi l'operazione «teacher forcing e aggiornamento supervisionato», infine l'output «loss per token e comportamento adattato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Durante il training il modello vede il prefisso corretto».

L'adattamento cambia il segnale presentato al modello e la porzione di output su cui si calcola la loss. Dati, mask, riferimenti e valutazione separata determinano quale comportamento viene effettivamente rinforzato. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Durante il training il modello vede il prefisso corretto». [SRC-46-004]

Il punto didattico di «Teacher forcing e generalizzazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss per token e comportamento adattato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Teacher forcing e generalizzazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di target, proxy e comportamento. Da «Teacher forcing e generalizzazione» portiamo l'output «loss per token e comportamento adattato»; non portiamo invece una conclusione oltre il caso locale.

## Catastrophic forgetting e controllo

Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili. [SRC-46-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una metrica del compito nuovo confrontata con la stessa metrica sul comportamento precedente. Da qui possiamo leggere la conseguenza dichiarata da «Learning rate, durata e replay influenzano la perdita di capacità precedenti».

Nel contratto locale, l'input «messaggi, target, mask delle label e mixture» entra, l'operazione «teacher forcing e aggiornamento supervisionato» modifica il percorso e l'output «loss per token e comportamento adattato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Catastrophic forgetting e controllo»; resta da controllare che il formato dei dati e le label decidono che cosa viene ottimizzato. La domanda locale è «Learning rate, durata e replay influenzano la perdita di capacità precedenti».

L'adattamento cambia il segnale presentato al modello e la porzione di output su cui si calcola la loss. Dati, mask, riferimenti e valutazione separata determinano quale comportamento viene effettivamente rinforzato. Il test deve conservare una misura del comportamento precedente prima e dopo l'aggiornamento, non soltanto il punteggio sul compito nuovo. La verifica resta ancorata a «Learning rate, durata e replay influenzano la perdita di capacità precedenti». [SRC-46-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Base model, modello SFT e sistema devono restare identificabili. Il piccolo risultato resta un'illustrazione di «Learning rate, durata e replay influenzano la perdita di capacità precedenti», non una promessa generale.

La prova di «Catastrophic forgetting e controllo» conserva input, operazione e output; poi esplicita quale parte di «Learning rate, durata e replay influenzano la perdita di capacità precedenti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «loss per token e comportamento adattato» come evidenza locale e conserva la distanza tra obiettivo locale e compito come domanda aperta.

## La definizione messa alla prova: Dal pretraining alle istruzioni

Il caso intero parte dall'input «messaggi, target, mask delle label e mixture», applica l'operazione «teacher forcing e aggiornamento supervisionato» e osserva l'output «loss per token e comportamento adattato». Un esempio controllato: un messaggio utente e una risposta con loss solo sulla risposta. La formula locale è:

$$
L = -sum_t log p_theta(y_t | x, y_<t)
$$

SFT assegna target espliciti, ma la qualità dipende da dati, formato e copertura. [SRC-46-001]

![Supervised fine-tuning e instruction tuning: branch](../../assets/chapters/46_sft/SFT-02/candidate-v48.png)

La figura SFT-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Teacher forcing e aggiornamento supervisionato. L'input è messaggi, target, mask delle label e mixture, l'output è loss per token e comportamento adattato; il vincolo da controllare è che il formato dei dati e le label decidono che cosa viene ottimizzato.

## Un esperimento piccolo ma leggibile: Formati conversazionali

Il file `code/snip_46_contract.py` collega il contratto del capitolo alla frase «Learning rate, durata e replay influenzano la perdita di capacità precedenti». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-46-001.txt` conserva il risultato ripetibile del caso locale.

## Il confine del caso guida: Catastrophic forgetting e controllo

Il meccanismo di «Supervised fine-tuning e instruction tuning» resta legato al contratto locale. Il formato dei dati e le label decidono che cosa viene ottimizzato. Prima di generalizzare la frase «Learning rate, durata e replay influenzano la perdita di capacità precedenti», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il contratto che rimane: Supervised fine-tuning e instruction tuning

Abbiamo seguito una coppia prompt-risposta nel formato di instruction tuning, partendo dall'input «messaggi, target, mask delle label e mixture» e arrivando all'output «loss per token e comportamento adattato». Le sezioni «Dal pretraining alle istruzioni», «Formati conversazionali», «Catastrophic forgetting e controllo» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: il formato dei dati e le label decidono che cosa viene ottimizzato. Il Capitolo 47, Fine-tuning efficiente, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Dal pretraining alle istruzioni

1. Ricostruisci l'oggetto continuo a partire da «Dal pretraining alle istruzioni» e indica quale parte della frase «Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate» entra nel caso.
2. Spiega quale trasformazione collega «Dal pretraining alle istruzioni» a «Catastrophic forgetting e controllo» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: il formato dei dati e le label decidono che cosa viene ottimizzato.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Learning rate, durata e replay influenzano la perdita di capacità precedenti» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Catastrophic forgetting e controllo

1. Disegna il percorso di «Dal pretraining alle istruzioni» indicando dati in ingresso e risultato.
2. Ripeti «Formati conversazionali» cambiando soltanto un valore dichiarato.
3. Trova in «Instruction mixture» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Teacher forcing e generalizzazione» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Catastrophic forgetting e controllo» richiederebbe un benchmark ulteriore.

## Riferimenti e prove riproducibili: Supervised fine-tuning e instruction tuning

Il dossier di «Supervised fine-tuning e instruction tuning» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il segnale che premia una risposta; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a target, proxy e comportamento.
