<!--
chapter_id: CH-P10-WORLD-EMBODIED
part_id: P10
order_key: 620
title: World model, embodied AI e vision-language-action
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 62. World model, embodied AI e vision-language-action

Il risultato precedente non è ancora una soluzione completa. Partiamo da lo stato di un agente embodied nel mondo e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «azione, stato previsto e risultato fisico» isoliamo il passaggio «world model, planning, VLA e controllo» e ne misuriamo il limite prima di passare a Information retrieval.

## Modello della dinamica

Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione. [SRC-62-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un'azione move porta la posizione da 0 a 1 e consuma una unità di batteria. Da qui possiamo leggere la conseguenza dichiarata da «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione».

La sezione usa l'input «osservazione, stato, azione e dinamica» come punto di partenza e l'output «azione, stato previsto e risultato fisico» come traccia d'uscita. La trasformazione concreta è «world model, planning, VLA e controllo»; il caso non è completo se non dichiariamo anche che sim-to-real richiede una misura sul sistema reale. La condizione da isolare è «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Modello della dinamica» il controllo cambia una sola premessa della frase «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione». [SRC-62-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Modello della dinamica» conserviamo l'osservazione collegata a «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Modello della dinamica» conserva input, operazione e output; poi esplicita quale parte di «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Planning nel modello», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Planning nel modello

Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello possono essere sfruttati dal planner. [SRC-62-002]

Per capire «Planning nel modello» partiamo da questo caso: un'azione prevista in simulazione e il controllo del suo esito. Il caso rende osservabile il punto centrale: «Traiettorie candidate vengono simulate e valutate prima di agire».

Per ricostruire «Planning nel modello» annotiamo l'input «osservazione, stato, azione e dinamica», poi l'operazione «world model, planning, VLA e controllo», infine l'output «azione, stato previsto e risultato fisico». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Traiettorie candidate vengono simulate e valutate prima di agire».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Planning nel modello» il controllo cambia una sola premessa della frase «Traiettorie candidate vengono simulate e valutate prima di agire» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Traiettorie candidate vengono simulate e valutate prima di agire». [SRC-62-002]

Il punto didattico di «Planning nel modello» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «azione, stato previsto e risultato fisico» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Planning nel modello» cambiamo una sola condizione vicina alla frase «Traiettorie candidate vengono simulate e valutate prima di agire», teniamo fermo il resto e registriamo l'output «azione, stato previsto e risultato fisico». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Embodied perception», riceve l'output «azione, stato previsto e risultato fisico» come base, ma dovrà formulare e verificare la propria distinzione.

## Embodied perception

Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e calibrazione influenzano ogni azione. [SRC-62-003]

Il caso minimo di «Embodied perception» si presenta così: un caso in cui sim-to-real richiede una misura sul sistema reale. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un agente fisico collega camera, propriocezione, linguaggio e coordinate».

Nel contratto locale, l'input «osservazione, stato, azione e dinamica» entra, l'operazione «world model, planning, VLA e controllo» modifica il percorso e l'output «azione, stato previsto e risultato fisico» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Embodied perception»; resta da controllare che sim-to-real richiede una misura sul sistema reale. La domanda locale è «Un agente fisico collega camera, propriocezione, linguaggio e coordinate».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Embodied perception» il controllo cambia una sola premessa della frase «Un agente fisico collega camera, propriocezione, linguaggio e coordinate» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un agente fisico collega camera, propriocezione, linguaggio e coordinate». [SRC-62-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Latenza e calibrazione influenzano ogni azione. Il piccolo risultato resta un'illustrazione di «Un agente fisico collega camera, propriocezione, linguaggio e coordinate», non una promessa generale.

Il controllo minimo di «Embodied perception» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «Embodied perception» portiamo l'output «azione, stato previsto e risultato fisico»; non portiamo invece una conclusione oltre il caso locale.

## Vision-language-action

VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e discretizzazione devono essere dichiarate. [SRC-62-004]

Prima del nome tecnico fissiamo la situazione: consideriamo una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Da qui possiamo leggere la conseguenza dichiarata da «VLA mappa osservazioni e istruzioni a token o controlli di azione».

La sezione usa l'input «osservazione, stato, azione e dinamica» come punto di partenza e l'output «azione, stato previsto e risultato fisico» come traccia d'uscita. La trasformazione concreta è «world model, planning, VLA e controllo»; il caso non è completo se non dichiariamo anche che sim-to-real richiede una misura sul sistema reale. La condizione da isolare è «VLA mappa osservazioni e istruzioni a token o controlli di azione».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Vision-language-action» il controllo cambia una sola premessa della frase «VLA mappa osservazioni e istruzioni a token o controlli di azione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «VLA mappa osservazioni e istruzioni a token o controlli di azione». [SRC-62-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Vision-language-action» conserviamo l'osservazione collegata a «VLA mappa osservazioni e istruzioni a token o controlli di azione» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Vision-language-action» conserva input, operazione e output; poi esplicita quale parte di «VLA mappa osservazioni e istruzioni a token o controlli di azione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Sicurezza e sim-to-real», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![World model, embodied AI e vision-language-action: loop](../../assets/chapters/62_world_embodied/EMBODIED-01/candidate-v48.png)

La figura EMBODIED-01 usa la famiglia loop. Il diagramma segue il passaggio: World model, planning, VLA e controllo. L'input è osservazione, stato, azione e dinamica, l'output è azione, stato previsto e risultato fisico; il vincolo da controllare è che sim-to-real richiede una misura sul sistema reale.

## Sicurezza e sim-to-real

Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale. [SRC-62-001]

Per capire «Sicurezza e sim-to-real» partiamo da questo caso: due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Il caso rende osservabile il punto centrale: «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale».

Per ricostruire «Sicurezza e sim-to-real» annotiamo l'input «osservazione, stato, azione e dinamica», poi l'operazione «world model, planning, VLA e controllo», infine l'output «azione, stato previsto e risultato fisico». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale».

Il passaggio da seguire in «Sicurezza e sim-to-real» è quello descritto dalla frase «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Sicurezza e sim-to-real» il controllo cambia una sola premessa della frase «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale». [SRC-62-001]

Il punto didattico di «Sicurezza e sim-to-real» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «azione, stato previsto e risultato fisico» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Sicurezza e sim-to-real» cambiamo una sola condizione vicina alla frase «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale», teniamo fermo il resto e registriamo l'output «azione, stato previsto e risultato fisico». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Una traiettoria controllata: Modello della dinamica

Il caso intero parte dall'input «osservazione, stato, azione e dinamica», applica l'operazione «world model, planning, VLA e controllo» e osserva l'output «azione, stato previsto e risultato fisico». Un esempio controllato: un'azione prevista in simulazione e il controllo del suo esito. Lo schema compatto è:

$$
a_t = policy(o_t, state_t)
$$

È una notazione di interfaccia, non un'identità numerica completa. Un world model o una policy produce un'azione condizionata da osservazione e stato. [SRC-62-001]

![World model, embodied AI e vision-language-action: pipeline](../../assets/chapters/62_world_embodied/EMBODIED-02/candidate-v48.png)

La figura EMBODIED-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: World model, planning, VLA e controllo. L'input è osservazione, stato, azione e dinamica, l'output è azione, stato previsto e risultato fisico; il vincolo da controllare è che sim-to-real richiede una misura sul sistema reale.

## Il passaggio eseguito in Python: Planning nel modello

Lo snippet locale mette in esecuzione questo caso: un'azione prevista in simulazione e il controllo del suo esito. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-62-001.txt`, come evidenza locale e non come benchmark di produzione.

## Prima di generalizzare: Sicurezza e sim-to-real

Il caso di «World model, embodied AI e vision-language-action» non certifica un servizio completo. Sim-to-real richiede una misura sul sistema reale. La domanda successiva è se «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Dalla lezione al capitolo seguente: World model, embodied AI e vision-language-action

Il filo della lezione va dall'input «osservazione, stato, azione e dinamica» all'output «azione, stato previsto e risultato fisico». Nei passaggi «Modello della dinamica», «Planning nel modello», «Sicurezza e sim-to-real» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: sim-to-real richiede una misura sul sistema reale. Il Capitolo 63, Information retrieval, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Modello della dinamica

1. Ricostruisci l'oggetto continuo a partire da «Modello della dinamica» e indica quale parte della frase «Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione» entra nel caso.
2. Spiega quale trasformazione collega «Modello della dinamica» a «Sicurezza e sim-to-real» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: sim-to-real richiede una misura sul sistema reale.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Sicurezza e sim-to-real

1. Ricostruisci input e output di «Modello della dinamica» usando un esempio di tre righe.
2. Modifica una sola variabile in «Planning nel modello» e anticipa l'invariante che dovrebbe restare.
3. Metti «Embodied perception» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Vision-language-action».
5. Formula per «Sicurezza e sim-to-real» una domanda che separi meccanismo e qualità del sistema.

## Dossier delle fonti e materiali: World model, embodied AI e vision-language-action

Per ricontrollare «World model, embodied AI e vision-language-action», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il contributo effettivo di ciascun segnale oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a allineamento tra modalità.
