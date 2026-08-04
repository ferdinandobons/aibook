<!--
chapter_id: CH-P12-SERVING
part_id: P12
order_key: 790
title: Serving, batching e scheduling
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 79. Serving, batching e scheduling

Una frase plausibile non basta a spiegare serving, batching e scheduling. L'oggetto è richieste eterogenee in una coda di serving; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Richieste eterogenee

Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano. [SRC-79-001]

Il caso minimo di «Richieste eterogenee» si presenta così: due richieste brevi e una lunga entrano nello stesso batch, con token totali registrati. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Prompt e output hanno lunghezze differenti».

Per ricostruire «Richieste eterogenee» annotiamo l'input «prompt, deadline, lunghezza, memoria e priorità», poi l'operazione «batching continuo, admission e scheduling», infine l'output «throughput, latency p50/p99 e richieste ammesse». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Prompt e output hanno lunghezze differenti».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Richieste eterogenee» il controllo cambia una sola premessa della frase «Prompt e output hanno lunghezze differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Prompt e output hanno lunghezze differenti». [SRC-79-001]

Il punto didattico di «Richieste eterogenee» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «throughput, latency p50/p99 e richieste ammesse» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Richieste eterogenee» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «Richieste eterogenee» portiamo l'output «throughput, latency p50/p99 e richieste ammesse»; non portiamo invece una conclusione oltre il caso locale.

## Continuous batching

Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse. [SRC-79-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un batch di richieste eterogenee in cui throughput, coda e time-to-first-token vengono misurati separatamente. Da qui possiamo leggere la conseguenza dichiarata da «Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse».

Nel contratto locale, l'input «prompt, deadline, lunghezza, memoria e priorità» entra, l'operazione «batching continuo, admission e scheduling» modifica il percorso e l'output «throughput, latency p50/p99 e richieste ammesse» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Continuous batching»; resta da controllare che throughput e latenza devono essere misurati insieme. La domanda locale è «Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse». [SRC-79-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse», non una promessa generale.

La prova di «Continuous batching» conserva input, operazione e output; poi esplicita quale parte di «Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Throughput e latency», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Throughput e latency

Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency. [SRC-79-003]

Per capire «Throughput e latency» partiamo da questo caso: un batch di richieste eterogenee in cui throughput, coda e time-to-first-token vengono misurati separatamente. Il caso rende osservabile il punto centrale: «Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency».

La sezione usa l'input «prompt, deadline, lunghezza, memoria e priorità» come punto di partenza e l'output «throughput, latency p50/p99 e richieste ammesse» come traccia d'uscita. La trasformazione concreta è «batching continuo, admission e scheduling»; il caso non è completo se non dichiariamo anche che throughput e latenza devono essere misurati insieme. La condizione da isolare è «Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency». [SRC-79-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Throughput e latency» conserviamo l'osservazione collegata a «Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Throughput e latency» cambiamo una sola condizione vicina alla frase «Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency», teniamo fermo il resto e registriamo l'output «throughput, latency p50/p99 e richieste ammesse». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Admission control», riceve l'output «throughput, latency p50/p99 e richieste ammesse» come base, ma dovrà formulare e verificare la propria distinzione.

![Serving, batching e scheduling: chart](../../assets/chapters/79_serving/SERVING-01/candidate-v48.png)

La figura SERVING-01 usa la famiglia chart. Il diagramma segue il passaggio: Batching continuo, admission e scheduling. L'input è prompt, deadline, lunghezza, memoria e priorità, l'output è throughput, latency p50/p99 e richieste ammesse; il vincolo da controllare è che throughput e latenza devono essere misurati insieme.

## Admission control

Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema. [SRC-79-004]

Il caso minimo di «Admission control» si presenta così: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema».

Per ricostruire «Admission control» annotiamo l'input «prompt, deadline, lunghezza, memoria e priorità», poi l'operazione «batching continuo, admission e scheduling», infine l'output «throughput, latency p50/p99 e richieste ammesse». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Admission control» il controllo cambia una sola premessa della frase «Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema». [SRC-79-004]

Il punto didattico di «Admission control» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «throughput, latency p50/p99 e richieste ammesse» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Admission control» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «Admission control» portiamo l'output «throughput, latency p50/p99 e richieste ammesse»; non portiamo invece una conclusione oltre il caso locale.

## Metriche di servizio

TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta. [SRC-79-001]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato. Da qui possiamo leggere la conseguenza dichiarata da «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta».

Nel contratto locale, l'input «prompt, deadline, lunghezza, memoria e priorità» entra, l'operazione «batching continuo, admission e scheduling» modifica il percorso e l'output «throughput, latency p50/p99 e richieste ammesse» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Metriche di servizio»; resta da controllare che throughput e latenza devono essere misurati insieme. La domanda locale è «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza. La verifica resta ancorata a «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta». [SRC-79-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta», non una promessa generale.

La prova di «Metriche di servizio» conserva input, operazione e output; poi esplicita quale parte di «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «throughput, latency p50/p99 e richieste ammesse» come evidenza locale e conserva la misura end-to-end sotto carico dichiarato come domanda aperta.

## Il contratto in un caso piccolo: Richieste eterogenee

Il caso intero parte dall'input «prompt, deadline, lunghezza, memoria e priorità», applica l'operazione «batching continuo, admission e scheduling» e osserva l'output «throughput, latency p50/p99 e richieste ammesse». Un esempio controllato: una richiesta lunga e due brevi in un batch continuo. Lo schema compatto è:

$$
schedule = batch(requests, deadline, memory)
$$

È una notazione di interfaccia, non un'identità numerica completa. Batching e scheduling sono una decisione con vincoli, non solo una coda. [SRC-79-001]

![Serving, batching e scheduling: queue](../../assets/chapters/79_serving/SERVING-02/candidate-v48.png)

La figura SERVING-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Batching continuo, admission e scheduling. L'input è prompt, deadline, lunghezza, memoria e priorità, l'output è throughput, latency p50/p99 e richieste ammesse; il vincolo da controllare è che throughput e latenza devono essere misurati insieme.

## Dalla trasformazione al test: Continuous batching

Nel run Python rendiamo osservabile la frase «Prompt e output hanno lunghezze differenti» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-79-001.txt` documenta il caso senza pretendere una misura generale.

## Il perimetro della conclusione: Metriche di servizio

Il meccanismo di «Serving, batching e scheduling» non garantisce da solo che il sistema funzioni fuori dal caso guida. Throughput e latenza devono essere misurati insieme. Il limite osservato riguarda la frase «Prompt e output hanno lunghezze differenti»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Una sintesi operativa: Serving, batching e scheduling

Il percorso ha tenuto insieme richieste eterogenee in una coda di serving, l'operazione «batching continuo, admission e scheduling» e l'output «throughput, latency p50/p99 e richieste ammesse». Le sezioni «Richieste eterogenee», «Continuous batching», «Metriche di servizio» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: throughput e latenza devono essere misurati insieme. Il Capitolo 80, Serving disaggregato e inference distribuita, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Richieste eterogenee

1. Ricostruisci l'oggetto continuo a partire da «Richieste eterogenee» e indica quale parte della frase «Prompt e output hanno lunghezze differenti» entra nel caso.
2. Spiega quale trasformazione collega «Richieste eterogenee» a «Metriche di servizio» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: throughput e latenza devono essere misurati insieme.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Metriche di servizio

1. Ricostruisci «Richieste eterogenee» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «Continuous batching» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Throughput e latency» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Admission control» in un test ripetibile.
5. Spiega come trasferire «Metriche di servizio» senza portare con sé una promessa non misurata.

## Materiali, fonti e codice verificato: Serving, batching e scheduling

Per «Serving, batching e scheduling», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto latency, memoria e throughput. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a latency, memoria e throughput.
