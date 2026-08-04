<!--
chapter_id: CH-P12-COMPILERS-KERNELS
part_id: P12
order_key: 810
title: Compiler, kernel e runtime
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 81. Compiler, kernel e runtime

Finora abbiamo potuto descrivere un grafo di operatori trasformato dal compiler. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 81 prendiamo l'input «grafo, shape, dtype, target e kernel» e lo seguiamo fino all'output «kernel eseguito, latenza e fallback», dichiarando prima il contratto e poi il limite.

## Grafo e operatori

Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. [SRC-81-001]

Per capire «Grafo e operatori» partiamo da questo caso: tre operatori diventano due gruppi dopo una fusione, con correttezza numerica da confrontare. Il caso rende osservabile il punto centrale: «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation».

Nel contratto locale, l'input «grafo, shape, dtype, target e kernel» entra, l'operazione «lowering, fusion, autotuning e gestione dei graph break» modifica il percorso e l'output «kernel eseguito, latenza e fallback» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Grafo e operatori»; resta da controllare che ottimizzazione del grafo e correttezza numerica devono essere confrontate. La domanda locale è «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Grafo e operatori» il controllo cambia una sola premessa della frase «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation». [SRC-81-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation», non una promessa generale.

Per verificare «Grafo e operatori» cambiamo una sola condizione vicina alla frase «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation», teniamo fermo il resto e registriamo l'output «kernel eseguito, latenza e fallback». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Kernel fusion», riceve l'output «kernel eseguito, latenza e fallback» come base, ma dovrà formulare e verificare la propria distinzione.

## Kernel fusion

Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. [SRC-81-002]

Il caso minimo di «Kernel fusion» si presenta così: la stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso».

La sezione usa l'input «grafo, shape, dtype, target e kernel» come punto di partenza e l'output «kernel eseguito, latenza e fallback» come traccia d'uscita. La trasformazione concreta è «lowering, fusion, autotuning e gestione dei graph break»; il caso non è completo se non dichiariamo anche che ottimizzazione del grafo e correttezza numerica devono essere confrontate. La condizione da isolare è «Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso». [SRC-81-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Kernel fusion» conserviamo l'osservazione collegata a «Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Kernel fusion» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «Kernel fusion» portiamo l'output «kernel eseguito, latenza e fallback»; non portiamo invece una conclusione oltre il caso locale.

![Compiler, kernel e runtime: compare](../../assets/chapters/81_compilers_kernels/KERNELS-01/candidate-v48.png)

La figura KERNELS-01 usa la famiglia compare. Il diagramma segue il passaggio: Lowering, fusion, autotuning e gestione dei graph break. L'input è grafo, shape, dtype, target e kernel, l'output è kernel eseguito, latenza e fallback; il vincolo da controllare è che ottimizzazione del grafo e correttezza numerica devono essere confrontate.

## Triton e kernel custom

Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. [SRC-81-003]

Prima del nome tecnico fissiamo la situazione: consideriamo la stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end. Da qui possiamo leggere la conseguenza dichiarata da «Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA».

Per ricostruire «Triton e kernel custom» annotiamo l'input «grafo, shape, dtype, target e kernel», poi l'operazione «lowering, fusion, autotuning e gestione dei graph break», infine l'output «kernel eseguito, latenza e fallback». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA». [SRC-81-003]

Il punto didattico di «Triton e kernel custom» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «kernel eseguito, latenza e fallback» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Triton e kernel custom» conserva input, operazione e output; poi esplicita quale parte di «Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «torch.compile e graph break», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## torch.compile e graph break

Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break. [SRC-81-004]

Per capire «torch.compile e graph break» partiamo da questo caso: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Il caso rende osservabile il punto centrale: «Tracing e guard permettono specializzazione dinamica».

Nel contratto locale, l'input «grafo, shape, dtype, target e kernel» entra, l'operazione «lowering, fusion, autotuning e gestione dei graph break» modifica il percorso e l'output «kernel eseguito, latenza e fallback» è ciò che osserviamo. Qui cambia soprattutto il passaggio «torch.compile e graph break»; resta da controllare che ottimizzazione del grafo e correttezza numerica devono essere confrontate. La domanda locale è «Tracing e guard permettono specializzazione dinamica».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «torch.compile e graph break» il controllo cambia una sola premessa della frase «Tracing e guard permettono specializzazione dinamica» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Tracing e guard permettono specializzazione dinamica». [SRC-81-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Python side effect o shape non supportate producono graph break. Il piccolo risultato resta un'illustrazione di «Tracing e guard permettono specializzazione dinamica», non una promessa generale.

Per verificare «torch.compile e graph break» cambiamo una sola condizione vicina alla frase «Tracing e guard permettono specializzazione dinamica», teniamo fermo il resto e registriamo l'output «kernel eseguito, latenza e fallback». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Autotuning e portabilità», riceve l'output «kernel eseguito, latenza e fallback» come base, ma dovrà formulare e verificare la propria distinzione.

## Autotuning e portabilità

Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati. [SRC-81-001]

Il caso minimo di «Autotuning e portabilità» si presenta così: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Tile, num warps e schedule ottimali dipendono dall'hardware».

La sezione usa l'input «grafo, shape, dtype, target e kernel» come punto di partenza e l'output «kernel eseguito, latenza e fallback» come traccia d'uscita. La trasformazione concreta è «lowering, fusion, autotuning e gestione dei graph break»; il caso non è completo se non dichiariamo anche che ottimizzazione del grafo e correttezza numerica devono essere confrontate. La condizione da isolare è «Tile, num warps e schedule ottimali dipendono dall'hardware».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Autotuning e portabilità» il controllo cambia una sola premessa della frase «Tile, num warps e schedule ottimali dipendono dall'hardware» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Tile, num warps e schedule ottimali dipendono dall'hardware». [SRC-81-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Autotuning e portabilità» conserviamo l'osservazione collegata a «Tile, num warps e schedule ottimali dipendono dall'hardware» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Autotuning e portabilità» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Il contratto in un caso piccolo: Grafo e operatori

Il caso intero parte dall'input «grafo, shape, dtype, target e kernel», applica l'operazione «lowering, fusion, autotuning e gestione dei graph break» e osserva l'output «kernel eseguito, latenza e fallback». Un esempio controllato: due operatori fusi con output numericamente equivalente. Lo schema compatto è:

$$
kernel = lower(graph, target)
$$

È una notazione di interfaccia, non un'identità numerica completa. Compiler e runtime trasformano il grafo in operazioni del backend. [SRC-81-001]

![Compiler, kernel e runtime: pipeline](../../assets/chapters/81_compilers_kernels/KERNELS-02/candidate-v48.png)

La figura KERNELS-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Lowering, fusion, autotuning e gestione dei graph break. L'input è grafo, shape, dtype, target e kernel, l'output è kernel eseguito, latenza e fallback; il vincolo da controllare è che ottimizzazione del grafo e correttezza numerica devono essere confrontate.

## Dalla trasformazione al test: Kernel fusion

Il file `code/snip_81_contract.py` collega il contratto del capitolo alla frase «Tile, num warps e schedule ottimali dipendono dall'hardware». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-81-001.txt` conserva il risultato ripetibile del caso locale.

## Il perimetro della conclusione: Autotuning e portabilità

Il meccanismo di «Compiler, kernel e runtime» resta legato al contratto locale. Ottimizzazione del grafo e correttezza numerica devono essere confrontate. Prima di generalizzare la frase «Tile, num warps e schedule ottimali dipendono dall'hardware», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Una sintesi operativa: Compiler, kernel e runtime

Abbiamo seguito un grafo di operatori trasformato dal compiler, partendo dall'input «grafo, shape, dtype, target e kernel» e arrivando all'output «kernel eseguito, latenza e fallback». Le sezioni «Grafo e operatori», «Kernel fusion», «Autotuning e portabilità» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: ottimizzazione del grafo e correttezza numerica devono essere confrontate. Il Capitolo 82, LLMOps, edge, costo ed energia, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Grafo e operatori

1. Ricostruisci l'oggetto continuo a partire da «Grafo e operatori» e indica quale parte della frase «Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation» entra nel caso.
2. Spiega quale trasformazione collega «Grafo e operatori» a «Autotuning e portabilità» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: ottimizzazione del grafo e correttezza numerica devono essere confrontate.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Tile, num warps e schedule ottimali dipendono dall'hardware» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Autotuning e portabilità

1. Racconta «Grafo e operatori» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Kernel fusion» mantenendo il resto del setup invariato.
3. Per «Triton e kernel custom», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «torch.compile e graph break» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Autotuning e portabilità» senza confondere livelli diversi.

## Materiali, fonti e codice verificato: Compiler, kernel e runtime

Il dossier di «Compiler, kernel e runtime» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il costo che si sposta tra kernel e servizio; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a latency, memoria e throughput.
