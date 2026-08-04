<!--
chapter_id: CH-P03-RL
part_id: P03
order_key: 140
title: Reinforcement learning
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 14. Reinforcement learning

Una frase plausibile non basta a spiegare reinforcement learning. L'oggetto è lo stato s_t della spedizione e la scelta a_t; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Dalle predizioni alle azioni

Un agente osserva uno stato, sceglie un'azione e riceve un reward. Il dato centrale non è una label statica, ma una traiettoria prodotta dall'interazione. [SRC-14-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso minimo con input s_t = (in_transito, ritardo=1) e output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Da qui possiamo leggere la conseguenza dichiarata da «Un agente osserva uno stato, sceglie un'azione e riceve un reward».

La sezione usa l'input «s_t = (in_transito, ritardo=1)» come punto di partenza e l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» come traccia d'uscita. La trasformazione concreta è «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}»; il caso non è completo se non dichiariamo anche che un reward osservato non diventa automaticamente una misura del servizio reale. La condizione da isolare è «Un agente osserva uno stato, sceglie un'azione e riceve un reward».

Il passaggio da esperimento a sistema richiede un protocollo esplicito, artefatti identificabili e una decisione delimitata. Una replica, una release o una nuova evidenza aggiunge informazione senza cancellare le condizioni del risultato originale. La scheda di prova conserva fonte, data, configurazione e decisione, permettendo di distinguere novità editoriale da evidenza ripetuta. La verifica resta ancorata a «Un agente osserva uno stato, sceglie un'azione e riceve un reward». [SRC-14-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Dalle predizioni alle azioni» conserviamo l'osservazione collegata a «Un agente osserva uno stato, sceglie un'azione e riceve un reward» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Dalle predizioni alle azioni» conserva input, operazione e output; poi esplicita quale parte di «Un agente osserva uno stato, sceglie un'azione e riceve un reward» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «MDP e ritorno», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## MDP e ritorno

Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto. Il ritorno somma reward futuri pesati e dipende dalla policy seguita. [SRC-14-002]

Per capire «MDP e ritorno» partiamo da questo caso: un ritorno calcolato da reward immediato 1, gamma 0,9 e valore futuro 0,5, mantenendo separati stato e azione. Il caso rende osservabile il punto centrale: «Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto».

Per ricostruire «MDP e ritorno» annotiamo l'input «s_t = (in_transito, ritardo=1)», poi l'operazione «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}», infine l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto».

Un MDP separa stato, azione, transizione e reward; il ritorno non è il reward di un singolo passo, ma una somma scontata lungo la traiettoria. La prova separa reward immediato, stato successivo e fattore di sconto, perché confonderli cambia la quantità stimata. La verifica resta ancorata a «Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto». [SRC-14-002]

Il punto didattico di «MDP e ritorno» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «MDP e ritorno» cambiamo una sola condizione vicina alla frase «Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto», teniamo fermo il resto e registriamo l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Value function e Bellman», riceve l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» come base, ma dovrà formulare e verificare la propria distinzione.

## Value function e Bellman

La value function riassume il ritorno atteso. Le equazioni di Bellman collegano il valore corrente a reward immediato e valore degli stati successivi. [SRC-14-003]

Il caso minimo di «Value function e Bellman» si presenta così: una traiettoria di due passi in cui reward immediato e valore futuro restano separati. Non lo usiamo come decorazione: serve a rendere osservabile la frase «La value function riassume il ritorno atteso».

Nel contratto locale, l'input «s_t = (in_transito, ritardo=1)» entra, l'operazione «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}» modifica il percorso e l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Value function e Bellman»; resta da controllare che un reward osservato non diventa automaticamente una misura del servizio reale. La domanda locale è «La value function riassume il ritorno atteso».

La value function riassume il ritorno atteso a partire da uno stato. La relazione di Bellman lo scompone in reward immediato e valore del prossimo stato, rendendo esplicita la ricorrenza. La verifica confronta il valore ricorsivo con la somma del reward immediato e del valore futuro, mantenendo fissa la policy. La verifica resta ancorata a «La value function riassume il ritorno atteso». [SRC-14-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Le equazioni di Bellman collegano il valore corrente a reward immediato e valore degli stati successivi. Il piccolo risultato resta un'illustrazione di «La value function riassume il ritorno atteso», non una promessa generale.

Il controllo minimo di «Value function e Bellman» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto del collegamento tra blocchi. Da «Value function e Bellman» portiamo l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}»; non portiamo invece una conclusione oltre il caso locale.

## Policy gradient e actor-critic

Il policy gradient aggiorna direttamente una policy stocastica. Actor-critic combina una policy con una stima di valore che riduce la varianza del segnale. [SRC-14-004]

Prima del nome tecnico fissiamo la situazione: consideriamo una traiettoria di due passi in cui reward immediato e valore futuro restano separati. Da qui possiamo leggere la conseguenza dichiarata da «Il policy gradient aggiorna direttamente una policy stocastica».

La sezione usa l'input «s_t = (in_transito, ritardo=1)» come punto di partenza e l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» come traccia d'uscita. La trasformazione concreta è «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}»; il caso non è completo se non dichiariamo anche che un reward osservato non diventa automaticamente una misura del servizio reale. La condizione da isolare è «Il policy gradient aggiorna direttamente una policy stocastica».

Il policy gradient collega l'aggiornamento alla probabilità delle azioni e all'esito osservato. Nell'actor-critic, il critic fornisce una stima del valore che può ridurre la varianza del segnale senza diventare la policy stessa. La leva da cambiare è il segnale usato per l'aggiornamento: probabilità della policy e stima del critic devono restare distinguibili. La verifica resta ancorata a «Il policy gradient aggiorna direttamente una policy stocastica». [SRC-14-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Policy gradient e actor-critic» conserviamo l'osservazione collegata a «Il policy gradient aggiorna direttamente una policy stocastica» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Policy gradient e actor-critic» conserva input, operazione e output; poi esplicita quale parte di «Il policy gradient aggiorna direttamente una policy stocastica» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Esplorazione e valutazione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Reinforcement learning: branch](../../assets/chapters/14_reinforcement_learning/RL-01/candidate-v51.png)

La figura RL-01 usa la famiglia branch. Il ramo comune resta separato dalle varianti e dai loro esiti.

## Esplorazione e valutazione

Esplorare significa raccogliere informazione su azioni non ancora ben valutate. Una policy deve essere misurata su ritorno, varianza, sicurezza e condizioni dell'ambiente. [SRC-14-001]

Per capire «Esplorazione e valutazione» partiamo da questo caso: due azioni disponibili con ritorni osservati diversi e una misura separata della varianza. Il caso rende osservabile il punto centrale: «Esplorare significa raccogliere informazione su azioni non ancora ben valutate».

Per ricostruire «Esplorazione e valutazione» annotiamo l'input «s_t = (in_transito, ritardo=1)», poi l'operazione «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}», infine l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Esplorare significa raccogliere informazione su azioni non ancora ben valutate».

Esplorare cambia quali traiettorie vengono osservate; valutare mantiene la procedura abbastanza stabile da confrontare le politiche. Ritorno medio, dispersione e vincoli di sicurezza rispondono a domande diverse. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Esplorare significa raccogliere informazione su azioni non ancora ben valutate». [SRC-14-001]

Il punto didattico di «Esplorazione e valutazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Esplorazione e valutazione» cambiamo una sola condizione vicina alla frase «Esplorare significa raccogliere informazione su azioni non ancora ben valutate», teniamo fermo il resto e registriamo l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Una traiettoria controllata: Dalle predizioni alle azioni

Il caso intero parte dall'input «s_t = (in_transito, ritardo=1)», applica l'operazione «la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}» e osserva l'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Un esempio controllato: reward immediato 1, gamma 0,9 e valore futuro 0,5. La formula locale è:

$$
G_t = R_{t+1} + \gamma G_{t+1}
$$

Il ritorno scontato collega reward e decisioni future. [SRC-14-001]

![Reinforcement learning: loop](../../assets/chapters/14_reinforcement_learning/RL-02/candidate-v52.png)

La figura RL-02 cambia composizione rispetto alla prima. Il ciclo rende visibili lo stato restituito e il punto in cui si applica il controllo.

## Il passaggio eseguito in Python: MDP e ritorno

Lo snippet locale mette in esecuzione questo caso: reward immediato 1, gamma 0,9 e valore futuro 0,5. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-14-001.txt`, come evidenza locale e non come benchmark di produzione.

## Prima di generalizzare: Esplorazione e valutazione

Il caso di «Reinforcement learning» non certifica un servizio completo. Un reward osservato non diventa automaticamente una misura del servizio reale. La domanda successiva è se «Esplorare significa raccogliere informazione su azioni non ancora ben valutate» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Dalla lezione al capitolo seguente: Reinforcement learning

Il filo della lezione va dall'input «s_t = (in_transito, ritardo=1)» all'output «la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}». Nei passaggi «Dalle predizioni alle azioni», «MDP e ritorno», «Esplorazione e valutazione» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: un reward osservato non diventa automaticamente una misura del servizio reale. Il Capitolo 15, Dal percettrone alle reti multilayer, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Dalle predizioni alle azioni

1. Ricostruisci l'oggetto continuo a partire da «Dalle predizioni alle azioni» e indica quale parte della frase «Un agente osserva uno stato, sceglie un'azione e riceve un reward» entra nel caso.
2. Spiega quale trasformazione collega «Dalle predizioni alle azioni» a «Esplorazione e valutazione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un reward osservato non diventa automaticamente una misura del servizio reale.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Esplorare significa raccogliere informazione su azioni non ancora ben valutate» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Esplorazione e valutazione

1. Racconta «Dalle predizioni alle azioni» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «MDP e ritorno» mantenendo il resto del setup invariato.
3. Per «Value function e Bellman», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Policy gradient e actor-critic» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Esplorazione e valutazione» senza confondere livelli diversi.

## Dossier delle fonti e materiali: Reinforcement learning

Per ricontrollare «Reinforcement learning», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire la trasformazione che la rete applica al segnale oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione al collegamento tra blocchi.
