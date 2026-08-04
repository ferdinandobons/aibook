<!--
chapter_id: CH-P07-PRETRAIN-RECIPE
part_id: P07
order_key: 350
title: La ricetta di pretraining
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 35. La ricetta di pretraining

Il Capitolo 34, Scaling law e progettazione del modello, ha lasciato disponibile lo stato completo di una ricetta di pretraining. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «forward, backward, update, schedule e recovery» e verifichiamo che un checkpoint deve includere lo stato necessario a continuare il run.

## Batch di token

Packing, padding e mask determinano quanti token validi contribuiscono alla loss. [SRC-35-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Da qui possiamo leggere la conseguenza dichiarata da «Packing, padding e mask determinano quanti token validi contribuiscono alla loss».

La sezione usa l'input «batch, learning rate, seed, optimizer e checkpoint» come punto di partenza e l'output «loss, parametri e checkpoint ripristinabile» come traccia d'uscita. La trasformazione concreta è «forward, backward, update, schedule e recovery»; il caso non è completo se non dichiariamo anche che un checkpoint deve includere lo stato necessario a continuare il run. La condizione da isolare è «Packing, padding e mask determinano quanti token validi contribuiscono alla loss».

La ricetta di training è una sequenza di stato, non soltanto un modello e un learning rate. Optimizer, scheduler, scaler, RNG e posizione nei dati devono ripartire dallo stesso contratto per rendere il resume interpretabile. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Packing, padding e mask determinano quanti token validi contribuiscono alla loss». [SRC-35-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Batch di token» conserviamo l'osservazione collegata a «Packing, padding e mask determinano quanti token validi contribuiscono alla loss» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Batch di token» conserva input, operazione e output; poi esplicita quale parte di «Packing, padding e mask determinano quanti token validi contribuiscono alla loss» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Inizializzazione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Inizializzazione

Scala dei pesi e residual deve restare coerente con profondità, norm e dtype. [SRC-35-002]

Per capire «Inizializzazione» partiamo da questo caso: warmup di quattro step e ripresa dal contatore salvato. Il caso rende osservabile il punto centrale: «Scala dei pesi e residual deve restare coerente con profondità, norm e dtype».

Per ricostruire «Inizializzazione» annotiamo l'input «batch, learning rate, seed, optimizer e checkpoint», poi l'operazione «forward, backward, update, schedule e recovery», infine l'output «loss, parametri e checkpoint ripristinabile». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Scala dei pesi e residual deve restare coerente con profondità, norm e dtype».

Il punto operativo è la scala del segnale: inizializzazione, normalizzazione, residual e regolarizzazione intervengono in momenti diversi e non sono sostituti intercambiabili. Shape compatibili e curve osservate servono a controllare il percorso reale. Per «Inizializzazione» il controllo cambia una sola premessa della frase «Scala dei pesi e residual deve restare coerente con profondità, norm e dtype» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Scala dei pesi e residual deve restare coerente con profondità, norm e dtype». [SRC-35-002]

Il punto didattico di «Inizializzazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss, parametri e checkpoint ripristinabile» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Inizializzazione» cambiamo una sola condizione vicina alla frase «Scala dei pesi e residual deve restare coerente con profondità, norm e dtype», teniamo fermo il resto e registriamo l'output «loss, parametri e checkpoint ripristinabile». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «AdamW», riceve l'output «loss, parametri e checkpoint ripristinabile» come base, ma dovrà formulare e verificare la propria distinzione.

## AdamW

Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer. [SRC-35-003]

Il caso minimo di «AdamW» si presenta così: un caso in cui un checkpoint deve includere lo stato necessario a continuare il run. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer».

Nel contratto locale, l'input «batch, learning rate, seed, optimizer e checkpoint» entra, l'operazione «forward, backward, update, schedule e recovery» modifica il percorso e l'output «loss, parametri e checkpoint ripristinabile» è ciò che osserviamo. Qui cambia soprattutto il passaggio «AdamW»; resta da controllare che un checkpoint deve includere lo stato necessario a continuare il run. La domanda locale è «Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer».

La ricetta di training è una sequenza di stato, non soltanto un modello e un learning rate. Optimizer, scheduler, scaler, RNG e posizione nei dati devono ripartire dallo stesso contratto per rendere il resume interpretabile. Per «AdamW» il controllo cambia una sola premessa della frase «Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer». [SRC-35-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer», non una promessa generale.

Il controllo minimo di «AdamW» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. Da «AdamW» portiamo l'output «loss, parametri e checkpoint ripristinabile»; non portiamo invece una conclusione oltre il caso locale.

## Warmup e schedule

Il learning rate dipende da step o token e deve riprendere dal contatore corretto. [SRC-35-004]

Prima del nome tecnico fissiamo la situazione: consideriamo due ricette con budget di token dichiarato, compute comparabile e loss osservata nello stesso intervallo. Da qui possiamo leggere la conseguenza dichiarata da «Il learning rate dipende da step o token e deve riprendere dal contatore corretto».

La sezione usa l'input «batch, learning rate, seed, optimizer e checkpoint» come punto di partenza e l'output «loss, parametri e checkpoint ripristinabile» come traccia d'uscita. La trasformazione concreta è «forward, backward, update, schedule e recovery»; il caso non è completo se non dichiariamo anche che un checkpoint deve includere lo stato necessario a continuare il run. La condizione da isolare è «Il learning rate dipende da step o token e deve riprendere dal contatore corretto».

La ricetta di training è una sequenza di stato, non soltanto un modello e un learning rate. Optimizer, scheduler, scaler, RNG e posizione nei dati devono ripartire dallo stesso contratto per rendere il resume interpretabile. Per «Warmup e schedule» il controllo cambia una sola premessa della frase «Il learning rate dipende da step o token e deve riprendere dal contatore corretto» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il learning rate dipende da step o token e deve riprendere dal contatore corretto». [SRC-35-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Warmup e schedule» conserviamo l'osservazione collegata a «Il learning rate dipende da step o token e deve riprendere dal contatore corretto» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Warmup e schedule» conserva input, operazione e output; poi esplicita quale parte di «Il learning rate dipende da step o token e deve riprendere dal contatore corretto» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Checkpoint e recovery», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![La ricetta di pretraining: timeline](../../assets/chapters/35_pretraining_recipe/RECIPE-01/candidate-v48.png)

La figura RECIPE-01 usa la famiglia timeline. Il diagramma segue il passaggio: Forward, backward, update, schedule e recovery. L'input è batch, learning rate, seed, optimizer e checkpoint, l'output è loss, parametri e checkpoint ripristinabile; il vincolo da controllare è che un checkpoint deve includere lo stato necessario a continuare il run.

## Checkpoint e recovery

Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele. [SRC-35-001]

Per capire «Checkpoint e recovery» partiamo da questo caso: una metrica del compito nuovo confrontata con la stessa metrica sul comportamento precedente. Il caso rende osservabile il punto centrale: «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele».

Per ricostruire «Checkpoint e recovery» annotiamo l'input «batch, learning rate, seed, optimizer e checkpoint», poi l'operazione «forward, backward, update, schedule e recovery», infine l'output «loss, parametri e checkpoint ripristinabile». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele».

La ricetta di training è una sequenza di stato, non soltanto un modello e un learning rate. Optimizer, scheduler, scaler, RNG e posizione nei dati devono ripartire dallo stesso contratto per rendere il resume interpretabile. Il test deve conservare una misura del comportamento precedente prima e dopo l'aggiornamento, non soltanto il punteggio sul compito nuovo. La verifica resta ancorata a «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele». [SRC-35-001]

Il punto didattico di «Checkpoint e recovery» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss, parametri e checkpoint ripristinabile» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Checkpoint e recovery» cambiamo una sola condizione vicina alla frase «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele», teniamo fermo il resto e registriamo l'output «loss, parametri e checkpoint ripristinabile». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Dal concetto alla situazione concreta: Batch di token

Il caso intero parte dall'input «batch, learning rate, seed, optimizer e checkpoint», applica l'operazione «forward, backward, update, schedule e recovery» e osserva l'output «loss, parametri e checkpoint ripristinabile». Un esempio controllato: warmup di quattro step e ripresa dal contatore salvato. La formula locale è:

$$
theta_t = AdamW(theta_{t-1}, grad_t, lr_t)
$$

Optimizer, schedule e stato del checkpoint formano una sola ricetta. [SRC-35-001]

![La ricetta di pretraining: pipeline](../../assets/chapters/35_pretraining_recipe/RECIPE-02/candidate-v48.png)

La figura RECIPE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Forward, backward, update, schedule e recovery. L'input è batch, learning rate, seed, optimizer e checkpoint, l'output è loss, parametri e checkpoint ripristinabile; il vincolo da controllare è che un checkpoint deve includere lo stato necessario a continuare il run.

## Una prova ripetibile: Inizializzazione

Lo snippet locale mette in esecuzione questo caso: warmup di quattro step e ripresa dal contatore salvato. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-35-001.txt`, come evidenza locale e non come benchmark di produzione.

## Il trasferimento richiede altro: Checkpoint e recovery

Il caso di «La ricetta di pretraining» non certifica un servizio completo. Un checkpoint deve includere lo stato necessario a continuare il run. La domanda successiva è se «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Il filo che passa oltre: La ricetta di pretraining

Il filo della lezione va dall'input «batch, learning rate, seed, optimizer e checkpoint» all'output «loss, parametri e checkpoint ripristinabile». Nei passaggi «Batch di token», «Inizializzazione», «Checkpoint e recovery» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: un checkpoint deve includere lo stato necessario a continuare il run. Il Capitolo 36, Training distribuito e continued pretraining, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Batch di token

1. Ricostruisci l'oggetto continuo a partire da «Batch di token» e indica quale parte della frase «Packing, padding e mask determinano quanti token validi contribuiscono alla loss» entra nel caso.
2. Spiega quale trasformazione collega «Batch di token» a «Checkpoint e recovery» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un checkpoint deve includere lo stato necessario a continuare il run.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Checkpoint e recovery

1. Disegna il percorso di «Batch di token» indicando dati in ingresso e risultato.
2. Ripeti «Inizializzazione» cambiando soltanto un valore dichiarato.
3. Trova in «AdamW» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Warmup e schedule» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Checkpoint e recovery» richiederebbe un benchmark ulteriore.

## Dove verificare definizioni e risultati: La ricetta di pretraining

Per ricontrollare «La ricetta di pretraining», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il legame tra dati esposti e risultato oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a popolazione, manifest e stato del run.
