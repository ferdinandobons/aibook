<!--
chapter_id: CH-P05-FLOWS
part_id: P05
order_key: 240
title: Normalizing flow e trasformazioni invertibili
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 24. Normalizing flow e trasformazioni invertibili

Una frase plausibile non basta a spiegare normalizing flow e trasformazioni invertibili. L'oggetto è un dato trasformato da una mappa invertibile; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Cambio di variabile

Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano. [SRC-24-001]

Per capire «Cambio di variabile» partiamo da questo caso: un caso minimo con input x, log-determinante e variabile latente z e output «log-likelihood, z e campione ricostruito». Il caso rende osservabile il punto centrale: «Una trasformazione invertibile collega una distribuzione semplice ai dati».

Nel contratto locale, l'input «x, log-determinante e variabile latente z» entra, l'operazione «coupling, cambio di variabile e inversione» modifica il percorso e l'output «log-likelihood, z e campione ricostruito» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Cambio di variabile»; resta da controllare che l'inversione richiede una trasformazione e un log-determinante coerenti. La domanda locale è «Una trasformazione invertibile collega una distribuzione semplice ai dati».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Cambio di variabile» il controllo cambia una sola premessa della frase «Una trasformazione invertibile collega una distribuzione semplice ai dati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una trasformazione invertibile collega una distribuzione semplice ai dati». [SRC-24-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La densità usa il determinante Jacobiano. Il piccolo risultato resta un'illustrazione di «Una trasformazione invertibile collega una distribuzione semplice ai dati», non una promessa generale.

Per verificare «Cambio di variabile» cambiamo una sola condizione vicina alla frase «Una trasformazione invertibile collega una distribuzione semplice ai dati», teniamo fermo il resto e registriamo l'output «log-likelihood, z e campione ricostruito». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Coupling layer», riceve l'output «log-likelihood, z e campione ricostruito» come base, ma dovrà formulare e verificare la propria distinzione.

## Coupling layer

RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti. [SRC-24-002]

Il caso minimo di «Coupling layer» si presenta così: due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Coupling layer». Non lo usiamo come decorazione: serve a rendere osservabile la frase «RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti».

La sezione usa l'input «x, log-determinante e variabile latente z» come punto di partenza e l'output «log-likelihood, z e campione ricostruito» come traccia d'uscita. La trasformazione concreta è «coupling, cambio di variabile e inversione»; il caso non è completo se non dichiariamo anche che l'inversione richiede una trasformazione e un log-determinante coerenti. La condizione da isolare è «RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Coupling layer» il controllo cambia una sola premessa della frase «RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti». [SRC-24-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Coupling layer» conserviamo l'osservazione collegata a «RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Coupling layer» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del rapporto tra distribuzione e campione. Da «Coupling layer» portiamo l'output «log-likelihood, z e campione ricostruito»; non portiamo invece una conclusione oltre il caso locale.

![Normalizing flow e trasformazioni invertibili: pipeline](../../assets/chapters/24_normalizing_flows/FLOWS-01/candidate-v48.png)

La figura FLOWS-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Coupling, cambio di variabile e inversione. L'input è x, log-determinante e variabile latente z, l'output è log-likelihood, z e campione ricostruito; il vincolo da controllare è che l'inversione richiede una trasformazione e un log-determinante coerenti.

## Invertibilità e architettura

L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla. [SRC-24-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui l'inversione richiede una trasformazione e un log-determinante coerenti. Da qui possiamo leggere la conseguenza dichiarata da «L'invertibilità limita operazioni e dimensioni».

Per ricostruire «Invertibilità e architettura» annotiamo l'input «x, log-determinante e variabile latente z», poi l'operazione «coupling, cambio di variabile e inversione», infine l'output «log-likelihood, z e campione ricostruito». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «L'invertibilità limita operazioni e dimensioni».

Il passaggio da seguire in «Invertibilità e architettura» è quello descritto dalla frase «L'invertibilità limita operazioni e dimensioni»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Invertibilità e architettura» il controllo cambia una sola premessa della frase «L'invertibilità limita operazioni e dimensioni» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «L'invertibilità limita operazioni e dimensioni». [SRC-24-003]

Il punto didattico di «Invertibilità e architettura» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «log-likelihood, z e campione ricostruito» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Invertibilità e architettura» conserva input, operazione e output; poi esplicita quale parte di «L'invertibilità limita operazioni e dimensioni» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Continuous normalizing flow», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Continuous normalizing flow

Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso. [SRC-24-004]

Per capire «Continuous normalizing flow» partiamo da questo caso: un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata. Il caso rende osservabile il punto centrale: «Una ODE definisce una trasformazione continua».

Nel contratto locale, l'input «x, log-determinante e variabile latente z» entra, l'operazione «coupling, cambio di variabile e inversione» modifica il percorso e l'output «log-likelihood, z e campione ricostruito» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Continuous normalizing flow»; resta da controllare che l'inversione richiede una trasformazione e un log-determinante coerenti. La domanda locale è «Una ODE definisce una trasformazione continua».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Continuous normalizing flow» il controllo cambia una sola premessa della frase «Una ODE definisce una trasformazione continua» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una ODE definisce una trasformazione continua». [SRC-24-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La likelihood usa la variazione del log-density lungo il flusso. Il piccolo risultato resta un'illustrazione di «Una ODE definisce una trasformazione continua», non una promessa generale.

Per verificare «Continuous normalizing flow» cambiamo una sola condizione vicina alla frase «Una ODE definisce una trasformazione continua», teniamo fermo il resto e registriamo l'output «log-likelihood, z e campione ricostruito». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Sampling e costo», riceve l'output «log-likelihood, z e campione ricostruito» come base, ma dovrà formulare e verificare la propria distinzione.

## Sampling e costo

I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici. [SRC-24-001]

Il caso minimo di «Sampling e costo» si presenta così: un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici».

La sezione usa l'input «x, log-determinante e variabile latente z» come punto di partenza e l'output «log-likelihood, z e campione ricostruito» come traccia d'uscita. La trasformazione concreta è «coupling, cambio di variabile e inversione»; il caso non è completo se non dichiariamo anche che l'inversione richiede una trasformazione e un log-determinante coerenti. La condizione da isolare è «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici».

L'inference trasforma logits e richieste in una traiettoria sotto vincoli di memoria e tempo. Decoding, cache, batching e scheduling modificano il servizio osservato e richiedono metriche oltre alla qualità dell'output. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici». [SRC-24-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Sampling e costo» conserviamo l'osservazione collegata a «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Sampling e costo» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del rapporto tra distribuzione e campione. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Un caso dall'input all'output: Cambio di variabile

Il caso intero parte dall'input «x, log-determinante e variabile latente z», applica l'operazione «coupling, cambio di variabile e inversione» e osserva l'output «log-likelihood, z e campione ricostruito». Un esempio controllato: una trasformazione affine a due coordinate invertita senza perdita. La formula locale è:

$$
log p_x(x)=log p_z(f(x))+log|det J_f(x)|
$$

Il cambio di variabile richiede trasformazione invertibile e Jacobiano. [SRC-24-001]

![Normalizing flow e trasformazioni invertibili: timeline](../../assets/chapters/24_normalizing_flows/FLOWS-02/candidate-v48.png)

La figura FLOWS-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Coupling, cambio di variabile e inversione. L'input è x, log-determinante e variabile latente z, l'output è log-likelihood, z e campione ricostruito; il vincolo da controllare è che l'inversione richiede una trasformazione e un log-determinante coerenti.

## Dal meccanismo alla prova locale: Coupling layer

Lo snippet locale mette in esecuzione questo caso: una trasformazione affine a due coordinate invertita senza perdita. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-24-001.txt`, come evidenza locale e non come benchmark di produzione.

## Dove il risultato si ferma: Sampling e costo

Il caso di «Normalizing flow e trasformazioni invertibili» non certifica un servizio completo. L'inversione richiede una trasformazione e un log-determinante coerenti. La domanda successiva è se «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Che cosa portiamo avanti: Normalizing flow e trasformazioni invertibili

Il filo della lezione va dall'input «x, log-determinante e variabile latente z» all'output «log-likelihood, z e campione ricostruito». Nei passaggi «Cambio di variabile», «Coupling layer», «Sampling e costo» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: l'inversione richiede una trasformazione e un log-determinante coerenti. Il Capitolo 25, Diffusione, score matching e flow matching, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Cambio di variabile

1. Ricostruisci l'oggetto continuo a partire da «Cambio di variabile» e indica quale parte della frase «Una trasformazione invertibile collega una distribuzione semplice ai dati» entra nel caso.
2. Spiega quale trasformazione collega «Cambio di variabile» a «Sampling e costo» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: l'inversione richiede una trasformazione e un log-determinante coerenti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Sampling e costo

1. Ricostruisci «Cambio di variabile» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «Coupling layer» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Invertibilità e architettura» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Continuous normalizing flow» in un test ripetibile.
5. Spiega come trasferire «Sampling e costo» senza portare con sé una promessa non misurata.

## Fonti, codice e materiali: Normalizing flow e trasformazioni invertibili

Per ricontrollare «Normalizing flow e trasformazioni invertibili», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il passaggio dal latente all'osservabile oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione al rapporto tra distribuzione e campione.
