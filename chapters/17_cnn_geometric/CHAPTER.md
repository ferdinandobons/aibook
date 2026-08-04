<!--
chapter_id: CH-P04-CNN-GEOMETRIC
part_id: P04
order_key: 170
title: Convolutional network e apprendimento geometrico
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 17. Convolutional network e apprendimento geometrico

Il risultato precedente non è ancora una soluzione completa. Partiamo da una griglia locale di feature e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «una griglia di attivazioni con dimensioni calcolabili» isoliamo il passaggio «lo stesso kernel scorre posizioni definite da stride e padding» e ne misuriamo il limite prima di passare a Reti ricorrenti e modelli sequenziali.

## Condivisione locale dei pesi

Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora un'ipotesi di regolarità locale. [SRC-17-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Da qui possiamo leggere la conseguenza dichiarata da «Una convoluzione applica lo stesso kernel in posizioni differenti».

La sezione usa l'input «una matrice 3 x 3 e un kernel 2 x 2» come punto di partenza e l'output «una griglia di attivazioni con dimensioni calcolabili» come traccia d'uscita. La trasformazione concreta è «lo stesso kernel scorre posizioni definite da stride e padding»; il caso non è completo se non dichiariamo anche che la condivisione dei pesi non implica invariance a ogni trasformazione. La condizione da isolare è «Una convoluzione applica lo stesso kernel in posizioni differenti».

La convoluzione riusa lo stesso kernel su posizioni diverse. Stride, padding e dilatazione stabiliscono quali vicini entrano nell'output e come cresce il campo ricettivo. Per «Condivisione locale dei pesi» il controllo cambia una sola premessa della frase «Una convoluzione applica lo stesso kernel in posizioni differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una convoluzione applica lo stesso kernel in posizioni differenti». [SRC-17-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Condivisione locale dei pesi» conserviamo l'osservazione collegata a «Una convoluzione applica lo stesso kernel in posizioni differenti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Condivisione locale dei pesi» conserva input, operazione e output; poi esplicita quale parte di «Una convoluzione applica lo stesso kernel in posizioni differenti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Stride, padding e receptive field», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Stride, padding e receptive field

Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione. [SRC-17-002]

Per capire «Stride, padding e receptive field» partiamo da questo caso: una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Il caso rende osservabile il punto centrale: «Stride e padding determinano la griglia dell'output».

Per ricostruire «Stride, padding e receptive field» annotiamo l'input «una matrice 3 x 3 e un kernel 2 x 2», poi l'operazione «lo stesso kernel scorre posizioni definite da stride e padding», infine l'output «una griglia di attivazioni con dimensioni calcolabili». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Stride e padding determinano la griglia dell'output».

La convoluzione riusa lo stesso kernel su posizioni diverse. Stride, padding e dilatazione stabiliscono quali vicini entrano nell'output e come cresce il campo ricettivo. Per «Stride, padding e receptive field» il controllo cambia una sola premessa della frase «Stride e padding determinano la griglia dell'output» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Stride e padding determinano la griglia dell'output». [SRC-17-002]

Il punto didattico di «Stride, padding e receptive field» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «una griglia di attivazioni con dimensioni calcolabili» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Stride, padding e receptive field» cambiamo una sola condizione vicina alla frase «Stride e padding determinano la griglia dell'output», teniamo fermo il resto e registriamo l'output «una griglia di attivazioni con dimensioni calcolabili». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Equivarianza e invariance», riceve l'output «una griglia di attivazioni con dimensioni calcolabili» come base, ma dovrà formulare e verificare la propria distinzione.

## Equivarianza e invariance

La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance. [SRC-17-003]

Il caso minimo di «Equivarianza e invariance» si presenta così: un caso in cui la condivisione dei pesi non implica invariance a ogni trasformazione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «La convoluzione è equivariant a traslazioni entro le condizioni del bordo».

Nel contratto locale, l'input «una matrice 3 x 3 e un kernel 2 x 2» entra, l'operazione «lo stesso kernel scorre posizioni definite da stride e padding» modifica il percorso e l'output «una griglia di attivazioni con dimensioni calcolabili» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Equivarianza e invariance»; resta da controllare che la condivisione dei pesi non implica invariance a ogni trasformazione. La domanda locale è «La convoluzione è equivariant a traslazioni entro le condizioni del bordo».

Il passaggio da seguire in «Equivarianza e invariance» è quello descritto dalla frase «La convoluzione è equivariant a traslazioni entro le condizioni del bordo»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Equivarianza e invariance» il controllo cambia una sola premessa della frase «La convoluzione è equivariant a traslazioni entro le condizioni del bordo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «La convoluzione è equivariant a traslazioni entro le condizioni del bordo». [SRC-17-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Pooling e aggregazione possono costruire una maggiore invariance. Il piccolo risultato resta un'illustrazione di «La convoluzione è equivariant a traslazioni entro le condizioni del bordo», non una promessa generale.

Il controllo minimo di «Equivarianza e invariance» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del collegamento tra blocchi. Da «Equivarianza e invariance» portiamo l'output «una griglia di attivazioni con dimensioni calcolabili»; non portiamo invece una conclusione oltre il caso locale.

## Vision Transformer e ibridi

Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati. [SRC-17-004]

Prima del nome tecnico fissiamo la situazione: consideriamo una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Da qui possiamo leggere la conseguenza dichiarata da «Patch embedding e attention offrono una geometria diversa».

La sezione usa l'input «una matrice 3 x 3 e un kernel 2 x 2» come punto di partenza e l'output «una griglia di attivazioni con dimensioni calcolabili» come traccia d'uscita. La trasformazione concreta è «lo stesso kernel scorre posizioni definite da stride e padding»; il caso non è completo se non dichiariamo anche che la condivisione dei pesi non implica invariance a ogni trasformazione. La condizione da isolare è «Patch embedding e attention offrono una geometria diversa».

Il Transformer compone embedding, posizione, attention, MLP, residual e normalizzazione. Il contratto cambia quando cambiano mask, direzione della sequenza o interfaccia tra encoder e decoder, anche se la shape finale resta uguale. Per «Vision Transformer e ibridi» il controllo cambia una sola premessa della frase «Patch embedding e attention offrono una geometria diversa» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Patch embedding e attention offrono una geometria diversa». [SRC-17-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Vision Transformer e ibridi» conserviamo l'osservazione collegata a «Patch embedding e attention offrono una geometria diversa» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Vision Transformer e ibridi» conserva input, operazione e output; poi esplicita quale parte di «Patch embedding e attention offrono una geometria diversa» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Grafi e message passing», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Convolutional network e apprendimento geometrico: architecture](../../assets/chapters/17_cnn_geometric/GEOMETRI-01/candidate-v49.png)

La figura GEOMETRI-01 usa la famiglia architecture. I componenti cambiano lo stato mentre il contratto conserva le invarianti dichiarate.

## Grafi e message passing

Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate. [SRC-17-001]

Per capire «Grafi e message passing» partiamo da questo caso: una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Il caso rende osservabile il punto centrale: «Su un grafo, i vicini non sono disposti in una griglia regolare».

Per ricostruire «Grafi e message passing» annotiamo l'input «una matrice 3 x 3 e un kernel 2 x 2», poi l'operazione «lo stesso kernel scorre posizioni definite da stride e padding», infine l'output «una griglia di attivazioni con dimensioni calcolabili». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Su un grafo, i vicini non sono disposti in una griglia regolare».

Il passaggio da seguire in «Grafi e message passing» è quello descritto dalla frase «Su un grafo, i vicini non sono disposti in una griglia regolare»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Grafi e message passing» il controllo cambia una sola premessa della frase «Su un grafo, i vicini non sono disposti in una griglia regolare» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Su un grafo, i vicini non sono disposti in una griglia regolare». [SRC-17-001]

Il punto didattico di «Grafi e message passing» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «una griglia di attivazioni con dimensioni calcolabili» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Grafi e message passing» cambiamo una sola condizione vicina alla frase «Su un grafo, i vicini non sono disposti in una griglia regolare», teniamo fermo il resto e registriamo l'output «una griglia di attivazioni con dimensioni calcolabili». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il contratto in un caso piccolo: Condivisione locale dei pesi

Il caso intero parte dall'input «una matrice 3 x 3 e un kernel 2 x 2», applica l'operazione «lo stesso kernel scorre posizioni definite da stride e padding» e osserva l'output «una griglia di attivazioni con dimensioni calcolabili». Un esempio controllato: una singola finestra 2 x 2 calcolata a mano. La formula locale è:

$$
y[i,j]=\sum_{u,v}K[u,v]x[i+u,j+v]
$$

Lo stesso kernel viene riutilizzato nelle posizioni della griglia. [SRC-17-001]

![Convolutional network e apprendimento geometrico: matrix](../../assets/chapters/17_cnn_geometric/GEOMETRI-02/candidate-v49.png)

La figura GEOMETRI-02 cambia composizione rispetto alla prima. La matrice rende visibili posizioni, dimensioni e vincoli dell'operazione.

## Dalla trasformazione al test: Stride, padding e receptive field

Il file `code/snip_17_contract.py` collega il contratto del capitolo alla frase «Su un grafo, i vicini non sono disposti in una griglia regolare». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-17-001.txt` conserva il risultato ripetibile del caso locale.

## Il perimetro della conclusione: Grafi e message passing

Il meccanismo di «Convolutional network e apprendimento geometrico» resta legato al contratto locale. La condivisione dei pesi non implica invariance a ogni trasformazione. Prima di generalizzare la frase «Su un grafo, i vicini non sono disposti in una griglia regolare», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Una sintesi operativa: Convolutional network e apprendimento geometrico

Abbiamo seguito una griglia locale di feature, partendo dall'input «una matrice 3 x 3 e un kernel 2 x 2» e arrivando all'output «una griglia di attivazioni con dimensioni calcolabili». Le sezioni «Condivisione locale dei pesi», «Stride, padding e receptive field», «Grafi e message passing» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: la condivisione dei pesi non implica invariance a ogni trasformazione. Il Capitolo 18, Reti ricorrenti e modelli sequenziali, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Condivisione locale dei pesi

1. Ricostruisci l'oggetto continuo a partire da «Condivisione locale dei pesi» e indica quale parte della frase «Una convoluzione applica lo stesso kernel in posizioni differenti» entra nel caso.
2. Spiega quale trasformazione collega «Condivisione locale dei pesi» a «Grafi e message passing» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: la condivisione dei pesi non implica invariance a ogni trasformazione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Su un grafo, i vicini non sono disposti in una griglia regolare» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Grafi e message passing

1. Disegna il percorso di «Condivisione locale dei pesi» indicando dati in ingresso e risultato.
2. Ripeti «Stride, padding e receptive field» cambiando soltanto un valore dichiarato.
3. Trova in «Equivarianza e invariance» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Vision Transformer e ibridi» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Grafi e message passing» richiederebbe un benchmark ulteriore.

## Materiali, fonti e codice verificato: Convolutional network e apprendimento geometrico

Il dossier di «Convolutional network e apprendimento geometrico» in `FONTI_PRIMARIE.md` separa definizioni, risultati e la shape e il percorso del segnale; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione al collegamento tra blocchi.
