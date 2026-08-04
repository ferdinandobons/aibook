<!--
chapter_id: CH-P12-LOW-BIT-NATIVE
part_id: P12
order_key: 750
title: Modelli low-bit nativi e co-design numerico
maturity: FRONTIER
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 75. Modelli low-bit nativi e co-design numerico

Il Capitolo 74, Quantizzazione, ha lasciato disponibile un peso low-bit e il suo accumulo numerico. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «training nativo, STE e accumulazione» e verifichiamo che bit nominali e precisione effettiva dell'accumulo sono distinti.

## Training nativo

Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine. [SRC-75-001]

Per capire «Training nativo» partiamo da questo caso: i codici -1, 0 e 1 vengono ricostruiti con una scala e sommati nella precisione dichiarata. Il caso rende osservabile il punto centrale: «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine».

Nel contratto locale, l'input «peso reale, codice ternario, scala e attivazione» entra, l'operazione «training nativo, STE e accumulazione» modifica il percorso e l'output «peso ricostruito, gradiente e costo hardware» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Training nativo»; resta da controllare che bit nominali e precisione effettiva dell'accumulo sono distinti. La domanda locale è «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Training nativo» il controllo cambia una sola premessa della frase «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine». [SRC-75-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine», non una promessa generale.

Per verificare «Training nativo» cambiamo una sola condizione vicina alla frase «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine», teniamo fermo il resto e registriamo l'output «peso ricostruito, gradiente e costo hardware». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Pesi ternari e 1.58-bit», riceve l'output «peso ricostruito, gradiente e costo hardware» come base, ma dovrà formulare e verificare la propria distinzione.

## Pesi ternari e 1.58-bit

BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel. [SRC-75-002]

Il caso minimo di «Pesi ternari e 1.58-bit» si presenta così: tre valori floating point quantizzati con una scala dichiarata e confrontati con la ricostruzione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici».

La sezione usa l'input «peso reale, codice ternario, scala e attivazione» come punto di partenza e l'output «peso ricostruito, gradiente e costo hardware» come traccia d'uscita. La trasformazione concreta è «training nativo, STE e accumulazione»; il caso non è completo se non dichiariamo anche che bit nominali e precisione effettiva dell'accumulo sono distinti. La condizione da isolare è «BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Il controllo confronta valore originale, rappresentazione compressa e ricostruzione, riportando separatamente errore numerico e comportamento sul compito. La verifica resta ancorata a «BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici». [SRC-75-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Pesi ternari e 1.58-bit» conserviamo l'osservazione collegata a «BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Pesi ternari e 1.58-bit» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «Pesi ternari e 1.58-bit» portiamo l'output «peso ricostruito, gradiente e costo hardware»; non portiamo invece una conclusione oltre il caso locale.

![Modelli low-bit nativi e co-design numerico: architecture](../../assets/chapters/75_low_bit_native/NATIVE-01/candidate-v48.png)

La figura NATIVE-01 usa la famiglia architecture. Il diagramma segue il passaggio: Training nativo, STE e accumulazione. L'input è peso reale, codice ternario, scala e attivazione, l'output è peso ricostruito, gradiente e costo hardware; il vincolo da controllare è che bit nominali e precisione effettiva dell'accumulo sono distinti.

## Straight-through estimator

Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione. [SRC-75-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui bit nominali e precisione effettiva dell'accumulo sono distinti. Da qui possiamo leggere la conseguenza dichiarata da «Operazioni discrete usano gradienti surrogati».

Per ricostruire «Straight-through estimator» annotiamo l'input «peso reale, codice ternario, scala e attivazione», poi l'operazione «training nativo, STE e accumulazione», infine l'output «peso ricostruito, gradiente e costo hardware». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Operazioni discrete usano gradienti surrogati».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Straight-through estimator» il controllo cambia una sola premessa della frase «Operazioni discrete usano gradienti surrogati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Operazioni discrete usano gradienti surrogati». [SRC-75-003]

Il punto didattico di «Straight-through estimator» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «peso ricostruito, gradiente e costo hardware» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Straight-through estimator» conserva input, operazione e output; poi esplicita quale parte di «Operazioni discrete usano gradienti surrogati» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Accumulazione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Accumulazione

Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati. [SRC-75-004]

Per capire «Accumulazione» partiamo da questo caso: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Il caso rende osservabile il punto centrale: «Prodotti low-bit possono accumulare in precisione maggiore».

Nel contratto locale, l'input «peso reale, codice ternario, scala e attivazione» entra, l'operazione «training nativo, STE e accumulazione» modifica il percorso e l'output «peso ricostruito, gradiente e costo hardware» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Accumulazione»; resta da controllare che bit nominali e precisione effettiva dell'accumulo sono distinti. La domanda locale è «Prodotti low-bit possono accumulare in precisione maggiore».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Accumulazione» il controllo cambia una sola premessa della frase «Prodotti low-bit possono accumulare in precisione maggiore» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Prodotti low-bit possono accumulare in precisione maggiore». [SRC-75-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Storage, compute e accumulator dtype devono essere separati. Il piccolo risultato resta un'illustrazione di «Prodotti low-bit possono accumulare in precisione maggiore», non una promessa generale.

Per verificare «Accumulazione» cambiamo una sola condizione vicina alla frase «Prodotti low-bit possono accumulare in precisione maggiore», teniamo fermo il resto e registriamo l'output «peso ricostruito, gradiente e costo hardware». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Co-design hardware», riceve l'output «peso ricostruito, gradiente e costo hardware» come base, ma dovrà formulare e verificare la propria distinzione.

## Co-design hardware

Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo. [SRC-75-001]

Il caso minimo di «Co-design hardware» si presenta così: la stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato».

La sezione usa l'input «peso reale, codice ternario, scala e attivazione» come punto di partenza e l'output «peso ricostruito, gradiente e costo hardware» come traccia d'uscita. La trasformazione concreta è «training nativo, STE e accumulazione»; il caso non è completo se non dichiariamo anche che bit nominali e precisione effettiva dell'accumulo sono distinti. La condizione da isolare è «Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato». [SRC-75-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Co-design hardware» conserviamo l'osservazione collegata a «Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Co-design hardware» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## La definizione messa alla prova: Training nativo

Il caso intero parte dall'input «peso reale, codice ternario, scala e attivazione», applica l'operazione «training nativo, STE e accumulazione» e osserva l'output «peso ricostruito, gradiente e costo hardware». Un esempio controllato: peso {-1, 0, 1} con scala e accumulo in precisione maggiore. La formula locale è:

$$
w_hat = dequantize(codebook(index(w)))
$$

Un formato low-bit introduce rappresentazione e operazione di ricostruzione. [SRC-75-001]

![Modelli low-bit nativi e co-design numerico: compare](../../assets/chapters/75_low_bit_native/NATIVE-02/candidate-v48.png)

La figura NATIVE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Training nativo, STE e accumulazione. L'input è peso reale, codice ternario, scala e attivazione, l'output è peso ricostruito, gradiente e costo hardware; il vincolo da controllare è che bit nominali e precisione effettiva dell'accumulo sono distinti.

## Un esperimento piccolo ma leggibile: Pesi ternari e 1.58-bit

Nel run Python rendiamo osservabile la frase «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-75-001.txt` documenta il caso senza pretendere una misura generale.

## Il confine del caso guida: Co-design hardware

Il meccanismo di «Modelli low-bit nativi e co-design numerico» non garantisce da solo che il sistema funzioni fuori dal caso guida. Bit nominali e precisione effettiva dell'accumulo sono distinti. Il limite osservato riguarda la frase «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il contratto che rimane: Modelli low-bit nativi e co-design numerico

Il percorso ha tenuto insieme un peso low-bit e il suo accumulo numerico, l'operazione «training nativo, STE e accumulazione» e l'output «peso ricostruito, gradiente e costo hardware». Le sezioni «Training nativo», «Pesi ternari e 1.58-bit», «Co-design hardware» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: bit nominali e precisione effettiva dell'accumulo sono distinti. Il Capitolo 76, Decoding e generazione vincolata, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Training nativo

1. Ricostruisci l'oggetto continuo a partire da «Training nativo» e indica quale parte della frase «Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine» entra nel caso.
2. Spiega quale trasformazione collega «Training nativo» a «Co-design hardware» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: bit nominali e precisione effettiva dell'accumulo sono distinti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Co-design hardware

1. Racconta «Training nativo» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Pesi ternari e 1.58-bit» mantenendo il resto del setup invariato.
3. Per «Straight-through estimator», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Accumulazione» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Co-design hardware» senza confondere livelli diversi.

## Riferimenti e prove riproducibili: Modelli low-bit nativi e co-design numerico

Per «Modelli low-bit nativi e co-design numerico», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto latency, memoria e throughput. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a latency, memoria e throughput.
