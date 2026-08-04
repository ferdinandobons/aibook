<!--
chapter_id: CH-P11-AGENT-TRAINING-EVAL
part_id: P11
order_key: 710
title: Training e valutazione degli agenti
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 71. Training e valutazione degli agenti

Finora abbiamo potuto descrivere traiettorie agentiche usate come dati e valutazione. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 71 prendiamo l'input «task, trace, policy, outcome e costo» e lo seguiamo fino all'output «score di task, violazioni e failure per step», dichiarando prima il contratto e poi il limite.

## Traiettorie come dati

Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento. [SRC-71-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due traiettorie hanno lo stesso successo, ma soltanto una ha zero violazioni di policy. Da qui possiamo leggere la conseguenza dichiarata da «Osservazioni, azioni, tool result e reward formano esempi sequenziali».

La sezione usa l'input «task, trace, policy, outcome e costo» come punto di partenza e l'output «score di task, violazioni e failure per step» come traccia d'uscita. La trasformazione concreta è «SFT, RL, benchmark e harness»; il caso non è completo se non dichiariamo anche che task riuscito e traiettoria sicura sono criteri distinti. La condizione da isolare è «Osservazioni, azioni, tool result e reward formano esempi sequenziali».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Traiettorie come dati» il controllo cambia una sola premessa della frase «Osservazioni, azioni, tool result e reward formano esempi sequenziali» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Osservazioni, azioni, tool result e reward formano esempi sequenziali». [SRC-71-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Traiettorie come dati» conserviamo l'osservazione collegata a «Osservazioni, azioni, tool result e reward formano esempi sequenziali» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Traiettorie come dati» conserva input, operazione e output; poi esplicita quale parte di «Osservazioni, azioni, tool result e reward formano esempi sequenziali» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Imitation e SFT», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Imitation e SFT

Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire. [SRC-71-002]

Per capire «Imitation e SFT» partiamo da questo caso: due traiettorie con stesso esito ma una violazione di policy. Il caso rende osservabile il punto centrale: «Traiettorie riuscite possono essere imitate».

Per ricostruire «Imitation e SFT» annotiamo l'input «task, trace, policy, outcome e costo», poi l'operazione «SFT, RL, benchmark e harness», infine l'output «score di task, violazioni e failure per step». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Traiettorie riuscite possono essere imitate».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Imitation e SFT» il controllo cambia una sola premessa della frase «Traiettorie riuscite possono essere imitate» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Traiettorie riuscite possono essere imitate». [SRC-71-002]

Il punto didattico di «Imitation e SFT» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score di task, violazioni e failure per step» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Imitation e SFT» cambiamo una sola condizione vicina alla frase «Traiettorie riuscite possono essere imitate», teniamo fermo il resto e registriamo l'output «score di task, violazioni e failure per step». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «RL in ambienti», riceve l'output «score di task, violazioni e failure per step» come base, ma dovrà formulare e verificare la propria distinzione.

## RL in ambienti

Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker. [SRC-71-003]

Il caso minimo di «RL in ambienti» si presenta così: un caso in cui task riuscito e traiettoria sicura sono criteri distinti. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Reward verificabili o simulati aggiornano policy multi-step».

Nel contratto locale, l'input «task, trace, policy, outcome e costo» entra, l'operazione «SFT, RL, benchmark e harness» modifica il percorso e l'output «score di task, violazioni e failure per step» è ciò che osserviamo. Qui cambia soprattutto il passaggio «RL in ambienti»; resta da controllare che task riuscito e traiettoria sicura sono criteri distinti. La domanda locale è «Reward verificabili o simulati aggiornano policy multi-step».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «RL in ambienti» il controllo cambia una sola premessa della frase «Reward verificabili o simulati aggiornano policy multi-step» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Reward verificabili o simulati aggiornano policy multi-step». [SRC-71-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il modello può sfruttare bug dell'ambiente o del checker. Il piccolo risultato resta un'illustrazione di «Reward verificabili o simulati aggiornano policy multi-step», non una promessa generale.

Il controllo minimo di «RL in ambienti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «RL in ambienti» portiamo l'output «score di task, violazioni e failure per step»; non portiamo invece una conclusione oltre il caso locale.

## Benchmark agentici

Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting. [SRC-71-004]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato. Da qui possiamo leggere la conseguenza dichiarata da «Success rate, step, costo e side effect devono essere misurati».

La sezione usa l'input «task, trace, policy, outcome e costo» come punto di partenza e l'output «score di task, violazioni e failure per step» come traccia d'uscita. La trasformazione concreta è «SFT, RL, benchmark e harness»; il caso non è completo se non dichiariamo anche che task riuscito e traiettoria sicura sono criteri distinti. La condizione da isolare è «Success rate, step, costo e side effect devono essere misurati».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Success rate, step, costo e side effect devono essere misurati». [SRC-71-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Benchmark agentici» conserviamo l'osservazione collegata a «Success rate, step, costo e side effect devono essere misurati» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Benchmark agentici» conserva input, operazione e output; poi esplicita quale parte di «Success rate, step, costo e side effect devono essere misurati» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Evaluation harness», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Training e valutazione degli agenti: chart](../../assets/chapters/71_agent_training_eval/EVAL-01/candidate-v48.png)

La figura EVAL-01 usa la famiglia chart. Il diagramma segue il passaggio: SFT, RL, benchmark e harness. L'input è task, trace, policy, outcome e costo, l'output è score di task, violazioni e failure per step; il vincolo da controllare è che task riuscito e traiettoria sicura sono criteri distinti.

## Evaluation harness

Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale. [SRC-71-001]

Per capire «Evaluation harness» partiamo da questo caso: quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Evaluation harness» e all'output score di task, violazioni e failure per step. Il caso rende osservabile il punto centrale: «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale».

Per ricostruire «Evaluation harness» annotiamo l'input «task, trace, policy, outcome e costo», poi l'operazione «SFT, RL, benchmark e harness», infine l'output «score di task, violazioni e failure per step». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale».

La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro. Per «Evaluation harness» il controllo cambia una sola premessa della frase «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale». [SRC-71-001]

Il punto didattico di «Evaluation harness» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score di task, violazioni e failure per step» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Evaluation harness» cambiamo una sola condizione vicina alla frase «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale», teniamo fermo il resto e registriamo l'output «score di task, violazioni e failure per step». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il contratto in un caso piccolo: Traiettorie come dati

Il caso intero parte dall'input «task, trace, policy, outcome e costo», applica l'operazione «SFT, RL, benchmark e harness» e osserva l'output «score di task, violazioni e failure per step». Un esempio controllato: due traiettorie con stesso esito ma una violazione di policy. Lo schema compatto è:

$$
score = evaluate(trajectory, task, policy)
$$

È una notazione di interfaccia, non un'identità numerica completa. L'eval deve distinguere compito riuscito, traiettoria e violazione di policy. [SRC-71-001]

![Training e valutazione degli agenti: funnel](../../assets/chapters/71_agent_training_eval/EVAL-02/candidate-v50.png)

La figura EVAL-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: SFT, RL, benchmark e harness. L'input è task, trace, policy, outcome e costo, l'output è score di task, violazioni e failure per step; il vincolo da controllare è che task riuscito e traiettoria sicura sono criteri distinti.

## Dalla trasformazione al test: Imitation e SFT

Nel run Python rendiamo osservabile la frase «Osservazioni, azioni, tool result e reward formano esempi sequenziali» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-71-001.txt` documenta il caso senza pretendere una misura generale.

## Il perimetro della conclusione: Evaluation harness

Il meccanismo di «Training e valutazione degli agenti» non garantisce da solo che il sistema funzioni fuori dal caso guida. Task riuscito e traiettoria sicura sono criteri distinti. Il limite osservato riguarda la frase «Osservazioni, azioni, tool result e reward formano esempi sequenziali»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Una sintesi operativa: Training e valutazione degli agenti

Il percorso ha tenuto insieme traiettorie agentiche usate come dati e valutazione, l'operazione «SFT, RL, benchmark e harness» e l'output «score di task, violazioni e failure per step». Le sezioni «Traiettorie come dati», «Imitation e SFT», «Evaluation harness» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: task riuscito e traiettoria sicura sono criteri distinti. Il Capitolo 72, Sicurezza operativa degli agenti, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Traiettorie come dati

1. Ricostruisci l'oggetto continuo a partire da «Traiettorie come dati» e indica quale parte della frase «Osservazioni, azioni, tool result e reward formano esempi sequenziali» entra nel caso.
2. Spiega quale trasformazione collega «Traiettorie come dati» a «Evaluation harness» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: task riuscito e traiettoria sicura sono criteri distinti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Evaluation harness

1. Ricostruisci input e output di «Traiettorie come dati» usando un esempio di tre righe.
2. Modifica una sola variabile in «Imitation e SFT» e anticipa l'invariante che dovrebbe restare.
3. Metti «RL in ambienti» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Benchmark agentici».
5. Formula per «Evaluation harness» una domanda che separi meccanismo e qualità del sistema.

## Materiali, fonti e codice verificato: Training e valutazione degli agenti

Per «Training e valutazione degli agenti», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto decisione, tool e side effect. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
