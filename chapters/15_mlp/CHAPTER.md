<!--
chapter_id: CH-P04-MLP
part_id: P04
order_key: 150
title: Dal percettrone alle reti multilayer
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 15. Dal percettrone alle reti multilayer

Il Capitolo 14, Reinforcement learning, ha lasciato disponibile il vettore di feature x della richiesta. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «una trasformazione affine seguita da una funzione di attivazione» e verifichiamo che una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.

## Una decisione lineare

Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature. [SRC-15-001]

Per capire «Una decisione lineare» partiamo da questo caso: un caso minimo con input x = [1, 2] con shape [2] e output «un nuovo vettore h con shape dichiarata». Il caso rende osservabile il punto centrale: «Il percettrone combina feature con pesi e bias».

Nel contratto locale, l'input «x = [1, 2] con shape [2]» entra, l'operazione «una trasformazione affine seguita da una funzione di attivazione» modifica il percorso e l'output «un nuovo vettore h con shape dichiarata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Una decisione lineare»; resta da controllare che una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. La domanda locale è «Il percettrone combina feature con pesi e bias».

Una trasformazione affine combina le feature con pesi e bias. La non linearità è ciò che impedisce a più trasformazioni affini consecutive di collassare in una sola mappa. Per «Una decisione lineare» il controllo cambia una sola premessa della frase «Il percettrone combina feature con pesi e bias» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il percettrone combina feature con pesi e bias». [SRC-15-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il confine risultante è lineare nello spazio delle feature. Il piccolo risultato resta un'illustrazione di «Il percettrone combina feature con pesi e bias», non una promessa generale.

Per verificare «Una decisione lineare» cambiamo una sola condizione vicina alla frase «Il percettrone combina feature con pesi e bias», teniamo fermo il resto e registriamo l'output «un nuovo vettore h con shape dichiarata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Strati nascosti», riceve l'output «un nuovo vettore h con shape dichiarata» come base, ma dovrà formulare e verificare la propria distinzione.

## Strati nascosti

Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine. [SRC-15-002]

Il caso minimo di «Strati nascosti» si presenta così: W x + b prima di ReLU, con due coordinate osservabili. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Una MLP alterna trasformazioni affini e funzioni non lineari».

La sezione usa l'input «x = [1, 2] con shape [2]» come punto di partenza e l'output «un nuovo vettore h con shape dichiarata» come traccia d'uscita. La trasformazione concreta è «una trasformazione affine seguita da una funzione di attivazione»; il caso non è completo se non dichiariamo anche che una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. La condizione da isolare è «Una MLP alterna trasformazioni affini e funzioni non lineari».

Una trasformazione affine combina le feature con pesi e bias. La non linearità è ciò che impedisce a più trasformazioni affini consecutive di collassare in una sola mappa. Per «Strati nascosti» il controllo cambia una sola premessa della frase «Una MLP alterna trasformazioni affini e funzioni non lineari» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una MLP alterna trasformazioni affini e funzioni non lineari». [SRC-15-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Strati nascosti» conserviamo l'osservazione collegata a «Una MLP alterna trasformazioni affini e funzioni non lineari» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Strati nascosti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del collegamento tra blocchi. Da «Strati nascosti» portiamo l'output «un nuovo vettore h con shape dichiarata»; non portiamo invece una conclusione oltre il caso locale.

![Dal percettrone alle reti multilayer: chart](../../assets/chapters/15_mlp/MLP-01/candidate-v49.png)

La figura MLP-01 usa la famiglia chart. Il grafico confronta la quantità che cambia con quella che non viene misurata.

## Attivazioni

ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione. [SRC-15-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. Da qui possiamo leggere la conseguenza dichiarata da «ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità».

Per ricostruire «Attivazioni» annotiamo l'input «x = [1, 2] con shape [2]», poi l'operazione «una trasformazione affine seguita da una funzione di attivazione», infine l'output «un nuovo vettore h con shape dichiarata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità».

Una trasformazione affine combina le feature con pesi e bias. La non linearità è ciò che impedisce a più trasformazioni affini consecutive di collassare in una sola mappa. Per «Attivazioni» il controllo cambia una sola premessa della frase «ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità». [SRC-15-003]

Il punto didattico di «Attivazioni» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «un nuovo vettore h con shape dichiarata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Attivazioni» conserva input, operazione e output; poi esplicita quale parte di «ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Capacità ed espressività», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Capacità ed espressività

Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile. [SRC-15-004]

Per capire «Capacità ed espressività» partiamo da questo caso: x=[1,2] passato in una trasformazione affine e poi in una non linearità, con shape e confine espliciti. Il caso rende osservabile il punto centrale: «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile».

Nel contratto locale, l'input «x = [1, 2] con shape [2]» entra, l'operazione «una trasformazione affine seguita da una funzione di attivazione» modifica il percorso e l'output «un nuovo vettore h con shape dichiarata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Capacità ed espressività»; resta da controllare che una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. La domanda locale è «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile».

Il passaggio da seguire in «Capacità ed espressività» è quello descritto dalla frase «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile». [SRC-15-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile», non una promessa generale.

Per verificare «Capacità ed espressività» cambiamo una sola condizione vicina alla frase «Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile», teniamo fermo il resto e registriamo l'output «un nuovo vettore h con shape dichiarata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Dal forward al training», riceve l'output «un nuovo vettore h con shape dichiarata» come base, ma dovrà formulare e verificare la propria distinzione.

## Dal forward al training

Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici. [SRC-15-001]

Il caso minimo di «Dal forward al training» si presenta così: due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Dal forward al training». Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il forward produce logits e loss».

La sezione usa l'input «x = [1, 2] con shape [2]» come punto di partenza e l'output «un nuovo vettore h con shape dichiarata» come traccia d'uscita. La trasformazione concreta è «una trasformazione affine seguita da una funzione di attivazione»; il caso non è completo se non dichiariamo anche che una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. La condizione da isolare è «Il forward produce logits e loss».

Il passaggio da seguire in «Dal forward al training» è quello descritto dalla frase «Il forward produce logits e loss»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Dal forward al training» il controllo cambia una sola premessa della frase «Il forward produce logits e loss» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il forward produce logits e loss». [SRC-15-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Dal forward al training» conserviamo l'osservazione collegata a «Il forward produce logits e loss» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Dal forward al training» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del collegamento tra blocchi. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Il contratto in un caso piccolo: Una decisione lineare

Il caso intero parte dall'input «x = [1, 2] con shape [2]», applica l'operazione «una trasformazione affine seguita da una funzione di attivazione» e osserva l'output «un nuovo vettore h con shape dichiarata». Un esempio controllato: W x + b prima di ReLU, con due coordinate osservabili. La formula locale è:

$$
h = \phi(Wx+b)
$$

La non linearità impedisce di collassare tutti i layer affini in uno solo. [SRC-15-001]

![Dal percettrone alle reti multilayer: architecture](../../assets/chapters/15_mlp/MLP-02/candidate-v49.png)

La figura MLP-02 cambia composizione rispetto alla prima. I componenti cambiano lo stato mentre il contratto conserva le invarianti dichiarate.

## Dalla trasformazione al test: Strati nascosti

Lo snippet locale mette in esecuzione questo caso: W x + b prima di ReLU, con due coordinate osservabili. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-15-001.txt`, come evidenza locale e non come benchmark di produzione.

## Il perimetro della conclusione: Dal forward al training

Il caso di «Dal percettrone alle reti multilayer» non certifica un servizio completo. Una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. La domanda successiva è se «Il forward produce logits e loss» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Una sintesi operativa: Dal percettrone alle reti multilayer

Il filo della lezione va dall'input «x = [1, 2] con shape [2]» all'output «un nuovo vettore h con shape dichiarata». Nei passaggi «Una decisione lineare», «Strati nascosti», «Dal forward al training» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. Il Capitolo 16, Addestrare reti profonde, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Una decisione lineare

1. Ricostruisci l'oggetto continuo a partire da «Una decisione lineare» e indica quale parte della frase «Il percettrone combina feature con pesi e bias» entra nel caso.
2. Spiega quale trasformazione collega «Una decisione lineare» a «Dal forward al training» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Il forward produce logits e loss» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Dal forward al training

1. Ricostruisci input e output di «Una decisione lineare» usando un esempio di tre righe.
2. Modifica una sola variabile in «Strati nascosti» e anticipa l'invariante che dovrebbe restare.
3. Metti «Attivazioni» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Capacità ed espressività».
5. Formula per «Dal forward al training» una domanda che separi meccanismo e qualità del sistema.

## Materiali, fonti e codice verificato: Dal percettrone alle reti multilayer

Per ricontrollare «Dal percettrone alle reti multilayer», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire la trasformazione che la rete applica al segnale oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione al collegamento tra blocchi.
