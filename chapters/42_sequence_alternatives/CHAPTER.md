<!--
chapter_id: CH-P08-SEQUENCE-ALTERNATIVES
part_id: P08
order_key: 420
title: State-space model, recurrence e long convolution
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 42. State-space model, recurrence e long convolution

Il risultato precedente non è ancora una soluzione completa. Partiamo da lo stato dinamico di un modello state-space e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «stato e uscita per ogni posizione» isoliamo il passaggio «recurrence, convolutione lunga o selezione» e ne misuriamo il limite prima di passare a Architetture ibride e memoria interna.

## State-space model

Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale. [SRC-42-001]

Per capire «State-space model» partiamo da questo caso: un caso minimo con input x_t, stato s_t e matrici A, B, C e output «stato e uscita per ogni posizione». Il caso rende osservabile il punto centrale: «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale».

Nel contratto locale, l'input «x_t, stato s_t e matrici A, B, C» entra, l'operazione «recurrence, convolutione lunga o selezione» modifica il percorso e l'output «stato e uscita per ogni posizione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «State-space model»; resta da controllare che stabilità e discretizzazione fanno parte dell'implementazione. La domanda locale è «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «State-space model» il controllo cambia una sola premessa della frase «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale». [SRC-42-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale», non una promessa generale.

Per verificare «State-space model» cambiamo una sola condizione vicina alla frase «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale», teniamo fermo il resto e registriamo l'output «stato e uscita per ogni posizione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «S4», riceve l'output «stato e uscita per ogni posizione» come base, ma dovrà formulare e verificare la propria distinzione.

## S4

Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili. [SRC-42-002]

Il caso minimo di «S4» si presenta così: tre passi di una dinamica lineare con stato osservabile. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili».

La sezione usa l'input «x_t, stato s_t e matrici A, B, C» come punto di partenza e l'output «stato e uscita per ogni posizione» come traccia d'uscita. La trasformazione concreta è «recurrence, convolutione lunga o selezione»; il caso non è completo se non dichiariamo anche che stabilità e discretizzazione fanno parte dell'implementazione. La condizione da isolare è «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili».

Il passaggio da seguire in «S4» è quello descritto dalla frase «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «S4» il controllo cambia una sola premessa della frase «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili». [SRC-42-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «S4» conserviamo l'osservazione collegata a «Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «S4» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «S4» portiamo l'output «stato e uscita per ogni posizione»; non portiamo invece una conclusione oltre il caso locale.

![State-space model, recurrence e long convolution: timeline](../../assets/chapters/42_sequence_alternatives/SSM-01/candidate-v47.png)

La figura SSM-01 usa la famiglia timeline. Il diagramma segue il passaggio: Recurrence, convolutione lunga o selezione. L'input è x_t, stato s_t e matrici A, B, C, l'output è stato e uscita per ogni posizione; il vincolo da controllare è che stabilità e discretizzazione fanno parte dell'implementazione.

## Mamba

Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware. [SRC-42-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui stabilità e discretizzazione fanno parte dell'implementazione. Da qui possiamo leggere la conseguenza dichiarata da «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware».

Per ricostruire «Mamba» annotiamo l'input «x_t, stato s_t e matrici A, B, C», poi l'operazione «recurrence, convolutione lunga o selezione», infine l'output «stato e uscita per ogni posizione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware».

Il passaggio da seguire in «Mamba» è quello descritto dalla frase «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Mamba» il controllo cambia una sola premessa della frase «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware». [SRC-42-003]

Il punto didattico di «Mamba» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stato e uscita per ogni posizione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Mamba» conserva input, operazione e output; poi esplicita quale parte di «Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Hyena e long convolution», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Hyena e long convolution

Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise. [SRC-42-004]

Per capire «Hyena e long convolution» partiamo da questo caso: una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Il caso rende osservabile il punto centrale: «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise».

Nel contratto locale, l'input «x_t, stato s_t e matrici A, B, C» entra, l'operazione «recurrence, convolutione lunga o selezione» modifica il percorso e l'output «stato e uscita per ogni posizione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Hyena e long convolution»; resta da controllare che stabilità e discretizzazione fanno parte dell'implementazione. La domanda locale è «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise».

La convoluzione riusa lo stesso kernel su posizioni diverse. Stride, padding e dilatazione stabiliscono quali vicini entrano nell'output e come cresce il campo ricettivo. Per «Hyena e long convolution» il controllo cambia una sola premessa della frase «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise». [SRC-42-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise», non una promessa generale.

Per verificare «Hyena e long convolution» cambiamo una sola condizione vicina alla frase «Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise», teniamo fermo il resto e registriamo l'output «stato e uscita per ogni posizione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «RWKV, RetNet, xLSTM e Griffin», riceve l'output «stato e uscita per ogni posizione» come base, ma dovrà formulare e verificare la propria distinzione.

## RWKV, RetNet, xLSTM e Griffin

Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti. [SRC-42-001]

Il caso minimo di «RWKV, RetNet, xLSTM e Griffin» si presenta così: tre passi in cui lo stato precedente viene consumato prima di produrre il successivo. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti».

La sezione usa l'input «x_t, stato s_t e matrici A, B, C» come punto di partenza e l'output «stato e uscita per ogni posizione» come traccia d'uscita. La trasformazione concreta è «recurrence, convolutione lunga o selezione»; il caso non è completo se non dichiariamo anche che stabilità e discretizzazione fanno parte dell'implementazione. La condizione da isolare è «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti».

Una rete ricorrente riusa lo stato e gli stessi parametri a ogni passo. Srotolare il calcolo rende visibile il percorso dei gradienti; gate e direzione della sequenza cambiano quali informazioni possono sopravvivere. La variabile da isolare è il pattern di visibilità o di riuso: la stessa shape può corrispondere a dipendenze e costi diversi. La verifica resta ancorata a «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti». [SRC-42-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «RWKV, RetNet, xLSTM e Griffin» conserviamo l'osservazione collegata a «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «RWKV, RetNet, xLSTM e Griffin» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Il caso minimo e la sua variante: State-space model

Il caso intero parte dall'input «x_t, stato s_t e matrici A, B, C», applica l'operazione «recurrence, convolutione lunga o selezione» e osserva l'output «stato e uscita per ogni posizione». Un esempio controllato: tre passi di una dinamica lineare con stato osservabile. La formula locale è:

$$
x_{t+1} = A x_t + B u_t
$$

La ricorrenza espone stato, input e dinamica prima della scelta implementativa. [SRC-42-001]

![State-space model, recurrence e long convolution: architecture](../../assets/chapters/42_sequence_alternatives/SSM-02/candidate-v47.png)

La figura SSM-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Recurrence, convolutione lunga o selezione. L'input è x_t, stato s_t e matrici A, B, C, l'output è stato e uscita per ogni posizione; il vincolo da controllare è che stabilità e discretizzazione fanno parte dell'implementazione.

## Che cosa osserva lo snippet: S4

Lo snippet locale mette in esecuzione questo caso: tre passi di una dinamica lineare con stato osservabile. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-42-001.txt`, come evidenza locale e non come benchmark di produzione.

## Che cosa non dimostra: RWKV, RetNet, xLSTM e Griffin

Il caso di «State-space model, recurrence e long convolution» non certifica un servizio completo. Stabilità e discretizzazione fanno parte dell'implementazione. La domanda successiva è se «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti» regga quando cambiano dati, scala, hardware o criteri di decisione.

## La mappa delle condizioni: State-space model, recurrence e long convolution

Il filo della lezione va dall'input «x_t, stato s_t e matrici A, B, C» all'output «stato e uscita per ogni posizione». Nei passaggi «State-space model», «S4», «RWKV, RetNet, xLSTM e Griffin» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: stabilità e discretizzazione fanno parte dell'implementazione. Il Capitolo 43, Architetture ibride e memoria interna, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: State-space model

1. Ricostruisci l'oggetto continuo a partire da «State-space model» e indica quale parte della frase «Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale» entra nel caso.
2. Spiega quale trasformazione collega «State-space model» a «RWKV, RetNet, xLSTM e Griffin» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: stabilità e discretizzazione fanno parte dell'implementazione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: RWKV, RetNet, xLSTM e Griffin

1. Ricostruisci «State-space model» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «S4» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Mamba» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Hyena e long convolution» in un test ripetibile.
5. Spiega come trasferire «RWKV, RetNet, xLSTM e Griffin» senza portare con sé una promessa non misurata.

## Fonti e risultati locali: State-space model, recurrence e long convolution

Per ricontrollare «State-space model, recurrence e long convolution», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il vincolo che impedisce di leggere il futuro oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
