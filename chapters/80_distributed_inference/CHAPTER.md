<!--
chapter_id: CH-P12-DISTRIBUTED-INFERENCE
part_id: P12
order_key: 800
title: Serving disaggregato e inference distribuita
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 80. Serving disaggregato e inference distribuita

Il Capitolo 79, Serving, batching e scheduling, ha lasciato disponibile una richiesta distribuita tra compute e comunicazioni. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «parallelismo, disaggregazione, routing e recovery» e verifichiamo che la comunicazione fa parte della latenza end-to-end.

## Tensor e pipeline parallelism

Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo. [SRC-80-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due worker aggiungono comunicazione e compute alla latenza end-to-end. Da qui possiamo leggere la conseguenza dichiarata da «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo».

La sezione usa l'input «shard, worker, rete, batch e fase prefill/decode» come punto di partenza e l'output «risposta, trasferimenti e fault osservati» come traccia d'uscita. La trasformazione concreta è «parallelismo, disaggregazione, routing e recovery»; il caso non è completo se non dichiariamo anche che la comunicazione fa parte della latenza end-to-end. La condizione da isolare è «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Tensor e pipeline parallelism» il controllo cambia una sola premessa della frase «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo». [SRC-80-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Tensor e pipeline parallelism» conserviamo l'osservazione collegata a «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Tensor e pipeline parallelism» conserva input, operazione e output; poi esplicita quale parte di «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Expert parallelism», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Expert parallelism

MoE distribuisce esperti e usa all-to-all durante l'inference. [SRC-80-002]

Per capire «Expert parallelism» partiamo da questo caso: due worker con una sincronizzazione e un timeout. Il caso rende osservabile il punto centrale: «MoE distribuisce esperti e usa all-to-all durante l'inference».

Per ricostruire «Expert parallelism» annotiamo l'input «shard, worker, rete, batch e fase prefill/decode», poi l'operazione «parallelismo, disaggregazione, routing e recovery», infine l'output «risposta, trasferimenti e fault osservati». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «MoE distribuisce esperti e usa all-to-all durante l'inference».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «MoE distribuisce esperti e usa all-to-all durante l'inference». [SRC-80-002]

Il punto didattico di «Expert parallelism» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risposta, trasferimenti e fault osservati» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Expert parallelism» cambiamo una sola condizione vicina alla frase «MoE distribuisce esperti e usa all-to-all durante l'inference», teniamo fermo il resto e registriamo l'output «risposta, trasferimenti e fault osservati». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Prefill-decode disaggregation», riceve l'output «risposta, trasferimenti e fault osservati» come base, ma dovrà formulare e verificare la propria distinzione.

## Prefill-decode disaggregation

Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete. [SRC-80-003]

Il caso minimo di «Prefill-decode disaggregation» si presenta così: un caso in cui la comunicazione fa parte della latenza end-to-end. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete».

Nel contratto locale, l'input «shard, worker, rete, batch e fase prefill/decode» entra, l'operazione «parallelismo, disaggregazione, routing e recovery» modifica il percorso e l'output «risposta, trasferimenti e fault osservati» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Prefill-decode disaggregation»; resta da controllare che la comunicazione fa parte della latenza end-to-end. La domanda locale è «Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Prefill-decode disaggregation» il controllo cambia una sola premessa della frase «Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete». [SRC-80-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete», non una promessa generale.

Il controllo minimo di «Prefill-decode disaggregation» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «Prefill-decode disaggregation» portiamo l'output «risposta, trasferimenti e fault osservati»; non portiamo invece una conclusione oltre il caso locale.

## Routing

Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi. [SRC-80-004]

Prima del nome tecnico fissiamo la situazione: consideriamo ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Da qui possiamo leggere la conseguenza dichiarata da «Modello, adapter, lunghezza e stato della cache guidano il placement».

La sezione usa l'input «shard, worker, rete, batch e fase prefill/decode» come punto di partenza e l'output «risposta, trasferimenti e fault osservati» come traccia d'uscita. La trasformazione concreta è «parallelismo, disaggregazione, routing e recovery»; il caso non è completo se non dichiariamo anche che la comunicazione fa parte della latenza end-to-end. La condizione da isolare è «Modello, adapter, lunghezza e stato della cache guidano il placement».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «Modello, adapter, lunghezza e stato della cache guidano il placement». [SRC-80-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Routing» conserviamo l'osservazione collegata a «Modello, adapter, lunghezza e stato della cache guidano il placement» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Routing» conserva input, operazione e output; poi esplicita quale parte di «Modello, adapter, lunghezza e stato della cache guidano il placement» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Fault tolerance», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Serving disaggregato e inference distribuita: architecture](../../assets/chapters/80_distributed_inference/INFERENCE-01/candidate-v48.png)

La figura INFERENCE-01 usa la famiglia architecture. Il diagramma segue il passaggio: Parallelismo, disaggregazione, routing e recovery. L'input è shard, worker, rete, batch e fase prefill/decode, l'output è risposta, trasferimenti e fault osservati; il vincolo da controllare è che la comunicazione fa parte della latenza end-to-end.

## Fault tolerance

Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione. [SRC-80-001]

Per capire «Fault tolerance» partiamo da questo caso: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Il caso rende osservabile il punto centrale: «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione».

Per ricostruire «Fault tolerance» annotiamo l'input «shard, worker, rete, batch e fase prefill/decode», poi l'operazione «parallelismo, disaggregazione, routing e recovery», infine l'output «risposta, trasferimenti e fault osservati». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Fault tolerance» il controllo cambia una sola premessa della frase «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione». [SRC-80-001]

Il punto didattico di «Fault tolerance» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risposta, trasferimenti e fault osservati» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Fault tolerance» cambiamo una sola condizione vicina alla frase «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione», teniamo fermo il resto e registriamo l'output «risposta, trasferimenti e fault osservati». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Una traiettoria controllata: Tensor e pipeline parallelism

Il caso intero parte dall'input «shard, worker, rete, batch e fase prefill/decode», applica l'operazione «parallelismo, disaggregazione, routing e recovery» e osserva l'output «risposta, trasferimenti e fault osservati». Un esempio controllato: due worker con una sincronizzazione e un timeout. Lo schema compatto è:

$$
latency = collective + compute + transfer
$$

È una notazione di interfaccia, non un'identità numerica completa. Il servizio distribuito include comunicazioni oltre al calcolo locale. [SRC-80-001]

![Serving disaggregato e inference distribuita: queue](../../assets/chapters/80_distributed_inference/INFERENCE-02/candidate-v48.png)

La figura INFERENCE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Parallelismo, disaggregazione, routing e recovery. L'input è shard, worker, rete, batch e fase prefill/decode, l'output è risposta, trasferimenti e fault osservati; il vincolo da controllare è che la comunicazione fa parte della latenza end-to-end.

## Il passaggio eseguito in Python: Expert parallelism

Nel run Python rendiamo osservabile la frase «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-80-001.txt` documenta il caso senza pretendere una misura generale.

## Prima di generalizzare: Fault tolerance

Il meccanismo di «Serving disaggregato e inference distribuita» non garantisce da solo che il sistema funzioni fuori dal caso guida. La comunicazione fa parte della latenza end-to-end. Il limite osservato riguarda la frase «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Dalla lezione al capitolo seguente: Serving disaggregato e inference distribuita

Il percorso ha tenuto insieme una richiesta distribuita tra compute e comunicazioni, l'operazione «parallelismo, disaggregazione, routing e recovery» e l'output «risposta, trasferimenti e fault osservati». Le sezioni «Tensor e pipeline parallelism», «Expert parallelism», «Fault tolerance» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: la comunicazione fa parte della latenza end-to-end. Il Capitolo 81, Compiler, kernel e runtime, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Tensor e pipeline parallelism

1. Ricostruisci l'oggetto continuo a partire da «Tensor e pipeline parallelism» e indica quale parte della frase «Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo» entra nel caso.
2. Spiega quale trasformazione collega «Tensor e pipeline parallelism» a «Fault tolerance» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: la comunicazione fa parte della latenza end-to-end.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Fault tolerance

1. Disegna il percorso di «Tensor e pipeline parallelism» indicando dati in ingresso e risultato.
2. Ripeti «Expert parallelism» cambiando soltanto un valore dichiarato.
3. Trova in «Prefill-decode disaggregation» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Routing» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Fault tolerance» richiederebbe un benchmark ulteriore.

## Dossier delle fonti e materiali: Serving disaggregato e inference distribuita

Per «Serving disaggregato e inference distribuita», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto latency, memoria e throughput. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a latency, memoria e throughput.
