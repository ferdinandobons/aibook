<!--
chapter_id: CH-P11-AGENT-LOOP
part_id: P11
order_key: 690
title: Ciclo agentico, pianificazione e verifica
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 69. Ciclo agentico, pianificazione e verifica

Una frase plausibile non basta a spiegare ciclo agentico, pianificazione e verifica. L'oggetto è lo stato di una traiettoria agentica; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Osservare e aggiornare lo stato

Un agente riceve input, risultato dei tool e memoria. Lo stato operativo deve essere separato dal testo libero del modello. [SRC-69-001]

Per capire «Osservare e aggiornare lo stato» partiamo da questo caso: una traiettoria minima registra observe, plan, tool e verify. Il caso rende osservabile il punto centrale: «Un agente riceve input, risultato dei tool e memoria».

Nel contratto locale, l'input «osservazione, piano, azione e risultato del tool» entra, l'operazione «observe, plan, act, verify e terminate» modifica il percorso e l'output «stato successivo o arresto motivato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Osservare e aggiornare lo stato»; resta da controllare che ogni side effect deve avere precondizioni e verifica. La domanda locale è «Un agente riceve input, risultato dei tool e memoria».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Osservare e aggiornare lo stato» il controllo cambia una sola premessa della frase «Un agente riceve input, risultato dei tool e memoria» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un agente riceve input, risultato dei tool e memoria». [SRC-69-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Lo stato operativo deve essere separato dal testo libero del modello. Il piccolo risultato resta un'illustrazione di «Un agente riceve input, risultato dei tool e memoria», non una promessa generale.

Per verificare «Osservare e aggiornare lo stato» cambiamo una sola condizione vicina alla frase «Un agente riceve input, risultato dei tool e memoria», teniamo fermo il resto e registriamo l'output «stato successivo o arresto motivato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Pianificare», riceve l'output «stato successivo o arresto motivato» come base, ma dovrà formulare e verificare la propria distinzione.

## Pianificare

Un piano scompone il compito in passi e dipendenze. Il piano iniziale può essere rivisto dopo nuove osservazioni. [SRC-69-002]

Il caso minimo di «Pianificare» si presenta così: lookup, conferma utente e aggiornamento dell'ordine. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un piano scompone il compito in passi e dipendenze».

La sezione usa l'input «osservazione, piano, azione e risultato del tool» come punto di partenza e l'output «stato successivo o arresto motivato» come traccia d'uscita. La trasformazione concreta è «observe, plan, act, verify e terminate»; il caso non è completo se non dichiariamo anche che ogni side effect deve avere precondizioni e verifica. La condizione da isolare è «Un piano scompone il compito in passi e dipendenze».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Pianificare» il controllo cambia una sola premessa della frase «Un piano scompone il compito in passi e dipendenze» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un piano scompone il compito in passi e dipendenze». [SRC-69-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Pianificare» conserviamo l'osservazione collegata a «Un piano scompone il compito in passi e dipendenze» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Pianificare» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Pianificare» portiamo l'output «stato successivo o arresto motivato»; non portiamo invece una conclusione oltre il caso locale.

![Ciclo agentico, pianificazione e verifica: timeline](../../assets/chapters/69_agent_loop/LOOP-01/candidate-v48.png)

La figura LOOP-01 usa la famiglia timeline. Il diagramma segue il passaggio: Observe, plan, act, verify e terminate. L'input è osservazione, piano, azione e risultato del tool, l'output è stato successivo o arresto motivato; il vincolo da controllare è che ogni side effect deve avere precondizioni e verifica.

## Agire

Ogni azione usa un tool o modifica un ambiente. Parametri, autorizzazioni e costo devono essere validati. [SRC-69-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui ogni side effect deve avere precondizioni e verifica. Da qui possiamo leggere la conseguenza dichiarata da «Ogni azione usa un tool o modifica un ambiente».

Per ricostruire «Agire» annotiamo l'input «osservazione, piano, azione e risultato del tool», poi l'operazione «observe, plan, act, verify e terminate», infine l'output «stato successivo o arresto motivato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Ogni azione usa un tool o modifica un ambiente».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Agire» il controllo cambia una sola premessa della frase «Ogni azione usa un tool o modifica un ambiente» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ogni azione usa un tool o modifica un ambiente». [SRC-69-003]

Il punto didattico di «Agire» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stato successivo o arresto motivato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Agire» conserva input, operazione e output; poi esplicita quale parte di «Ogni azione usa un tool o modifica un ambiente» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Verificare», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Verificare

Test, controlli di stato o giudici indipendenti valutano il risultato. Una autocritica del modello non equivale a verifica esterna. [SRC-69-004]

Per capire «Verificare» partiamo da questo caso: una traiettoria minima alterna osservazione, decisione, tool e verifica. Il test può controllare che un'azione non autorizzata venga bloccata. Il caso rende osservabile il punto centrale: «Test, controlli di stato o giudici indipendenti valutano il risultato».

Nel contratto locale, l'input «osservazione, piano, azione e risultato del tool» entra, l'operazione «observe, plan, act, verify e terminate» modifica il percorso e l'output «stato successivo o arresto motivato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Verificare»; resta da controllare che ogni side effect deve avere precondizioni e verifica. La domanda locale è «Test, controlli di stato o giudici indipendenti valutano il risultato».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Verificare» il controllo cambia una sola premessa della frase «Test, controlli di stato o giudici indipendenti valutano il risultato» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Test, controlli di stato o giudici indipendenti valutano il risultato». [SRC-69-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Una autocritica del modello non equivale a verifica esterna. Il piccolo risultato resta un'illustrazione di «Test, controlli di stato o giudici indipendenti valutano il risultato», non una promessa generale.

Per verificare «Verificare» cambiamo una sola condizione vicina alla frase «Test, controlli di stato o giudici indipendenti valutano il risultato», teniamo fermo il resto e registriamo l'output «stato successivo o arresto motivato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Terminare», riceve l'output «stato successivo o arresto motivato» come base, ma dovrà formulare e verificare la propria distinzione.

## Terminare

Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop. [SRC-69-001]

Il caso minimo di «Terminare» si presenta così: una traiettoria minima alterna osservazione, decisione, tool e verifica. Il test può controllare che un'azione non autorizzata venga bloccata. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop».

La sezione usa l'input «osservazione, piano, azione e risultato del tool» come punto di partenza e l'output «stato successivo o arresto motivato» come traccia d'uscita. La trasformazione concreta è «observe, plan, act, verify e terminate»; il caso non è completo se non dichiariamo anche che ogni side effect deve avere precondizioni e verifica. La condizione da isolare è «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Terminare» il controllo cambia una sola premessa della frase «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop». [SRC-69-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Terminare» conserviamo l'osservazione collegata a «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Terminare» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Un caso dall'input all'output: Osservare e aggiornare lo stato

Il caso intero parte dall'input «osservazione, piano, azione e risultato del tool», applica l'operazione «observe, plan, act, verify e terminate» e osserva l'output «stato successivo o arresto motivato». Un esempio controllato: lookup, conferma utente e aggiornamento dell'ordine. Lo schema compatto è:

$$
state_{t+1} = step(state_t, action_t, observation_t)
$$

È una notazione di interfaccia, non un'identità numerica completa. Il ciclo deve rendere visibili azione, osservazione e arresto. [SRC-69-001]

![Ciclo agentico, pianificazione e verifica: loop](../../assets/chapters/69_agent_loop/LOOP-02/candidate-v50.png)

La figura LOOP-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Observe, plan, act, verify e terminate. L'input è osservazione, piano, azione e risultato del tool, l'output è stato successivo o arresto motivato; il vincolo da controllare è che ogni side effect deve avere precondizioni e verifica.

## Dal meccanismo alla prova locale: Pianificare

Il file `code/snip_69_contract.py` collega il contratto del capitolo alla frase «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-69-001.txt` conserva il risultato ripetibile del caso locale.

## Dove il risultato si ferma: Terminare

Il meccanismo di «Ciclo agentico, pianificazione e verifica» resta legato al contratto locale. Ogni side effect deve avere precondizioni e verifica. Prima di generalizzare la frase «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Che cosa portiamo avanti: Ciclo agentico, pianificazione e verifica

Abbiamo seguito lo stato di una traiettoria agentica, partendo dall'input «osservazione, piano, azione e risultato del tool» e arrivando all'output «stato successivo o arresto motivato». Le sezioni «Osservare e aggiornare lo stato», «Pianificare», «Terminare» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: ogni side effect deve avere precondizioni e verifica. Il Capitolo 70, Multi-agent, browser, computer e code agents, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Osservare e aggiornare lo stato

1. Ricostruisci l'oggetto continuo a partire da «Osservare e aggiornare lo stato» e indica quale parte della frase «Un agente riceve input, risultato dei tool e memoria» entra nel caso.
2. Spiega quale trasformazione collega «Osservare e aggiornare lo stato» a «Terminare» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: ogni side effect deve avere precondizioni e verifica.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Terminare

1. Ricostruisci input e output di «Osservare e aggiornare lo stato» usando un esempio di tre righe.
2. Modifica una sola variabile in «Pianificare» e anticipa l'invariante che dovrebbe restare.
3. Metti «Agire» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Verificare».
5. Formula per «Terminare» una domanda che separi meccanismo e qualità del sistema.

## Fonti, codice e materiali: Ciclo agentico, pianificazione e verifica

Il dossier di «Ciclo agentico, pianificazione e verifica» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il confine tra informazione e azione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
