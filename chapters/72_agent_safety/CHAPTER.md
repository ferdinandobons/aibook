<!--
chapter_id: CH-P11-AGENT-SAFETY
part_id: P11
order_key: 720
title: Sicurezza operativa degli agenti
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 72. Sicurezza operativa degli agenti

Il risultato precedente non è ancora una soluzione completa. Partiamo da una decisione agentica su una risorsa reale e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «allow/deny, side effect o rollback auditabile» isoliamo il passaggio «least privilege, sandbox, human approval e rollback» e ne misuriamo il limite prima di passare a Distillazione e pruning.

## Least privilege

Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant. [SRC-72-001]

Per capire «Least privilege» partiamo da questo caso: lookup_order è consentito, mentre refund richiede approvazione o viene negato dalla policy esterna. Il caso rende osservabile il punto centrale: «Ogni tool riceve soltanto gli scope necessari».

Nel contratto locale, l'input «input non fidato, tool, scope e approvazione» entra, l'operazione «least privilege, sandbox, human approval e rollback» modifica il percorso e l'output «allow/deny, side effect o rollback auditabile» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Least privilege»; resta da controllare che l'enforcement deve stare fuori dal testo generato. La domanda locale è «Ogni tool riceve soltanto gli scope necessari».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Least privilege» il controllo cambia una sola premessa della frase «Ogni tool riceve soltanto gli scope necessari» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ogni tool riceve soltanto gli scope necessari». [SRC-72-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Credenziali e filesystem devono essere separati per task e tenant. Il piccolo risultato resta un'illustrazione di «Ogni tool riceve soltanto gli scope necessari», non una promessa generale.

Per verificare «Least privilege» cambiamo una sola condizione vicina alla frase «Ogni tool riceve soltanto gli scope necessari», teniamo fermo il resto e registriamo l'output «allow/deny, side effect o rollback auditabile». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Sandbox», riceve l'output «allow/deny, side effect o rollback auditabile» come base, ma dovrà formulare e verificare la propria distinzione.

## Sandbox

Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. [SRC-72-002]

Il caso minimo di «Sandbox» si presenta così: una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate».

La sezione usa l'input «input non fidato, tool, scope e approvazione» come punto di partenza e l'output «allow/deny, side effect o rollback auditabile» come traccia d'uscita. La trasformazione concreta è «least privilege, sandbox, human approval e rollback»; il caso non è completo se non dichiariamo anche che l'enforcement deve stare fuori dal testo generato. La condizione da isolare è «Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate». [SRC-72-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Sandbox» conserviamo l'osservazione collegata a «Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Sandbox» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Sandbox» portiamo l'output «allow/deny, side effect o rollback auditabile»; non portiamo invece una conclusione oltre il caso locale.

![Sicurezza operativa degli agenti: threat](../../assets/chapters/72_agent_safety/SAFETY-01/candidate-v50.png)

La figura SAFETY-01 usa la famiglia threat. Il diagramma segue il passaggio: Least privilege, sandbox, human approval e rollback. L'input è input non fidato, tool, scope e approvazione, l'output è allow/deny, side effect o rollback auditabile; il vincolo da controllare è che l'enforcement deve stare fuori dal testo generato.

## Human approval

Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. [SRC-72-003]

Prima del nome tecnico fissiamo la situazione: consideriamo una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Da qui possiamo leggere la conseguenza dichiarata da «Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti».

Per ricostruire «Human approval» annotiamo l'input «input non fidato, tool, scope e approvazione», poi l'operazione «least privilege, sandbox, human approval e rollback», infine l'output «allow/deny, side effect o rollback auditabile». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti». [SRC-72-003]

Il punto didattico di «Human approval» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «allow/deny, side effect o rollback auditabile» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Human approval» conserva input, operazione e output; poi esplicita quale parte di «Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Rollback e audit», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Rollback e audit

Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. [SRC-72-004]

Per capire «Rollback e audit» partiamo da questo caso: una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Il caso rende osservabile il punto centrale: «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria».

Nel contratto locale, l'input «input non fidato, tool, scope e approvazione» entra, l'operazione «least privilege, sandbox, human approval e rollback» modifica il percorso e l'output «allow/deny, side effect o rollback auditabile» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Rollback e audit»; resta da controllare che l'enforcement deve stare fuori dal testo generato. La domanda locale è «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Rollback e audit» il controllo cambia una sola premessa della frase «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria». [SRC-72-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria», non una promessa generale.

Per verificare «Rollback e audit» cambiamo una sola condizione vicina alla frase «Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria», teniamo fermo il resto e registriamo l'output «allow/deny, side effect o rollback auditabile». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Prompt injection», riceve l'output «allow/deny, side effect o rollback auditabile» come base, ma dovrà formulare e verificare la propria distinzione.

## Prompt injection

Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati. [SRC-72-001]

Il caso minimo di «Prompt injection» si presenta così: un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Contenuti esterni possono tentare di cambiare il piano».

La sezione usa l'input «input non fidato, tool, scope e approvazione» come punto di partenza e l'output «allow/deny, side effect o rollback auditabile» come traccia d'uscita. La trasformazione concreta è «least privilege, sandbox, human approval e rollback»; il caso non è completo se non dichiariamo anche che l'enforcement deve stare fuori dal testo generato. La condizione da isolare è «Contenuti esterni possono tentare di cambiare il piano».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Prompt injection» il controllo cambia una sola premessa della frase «Contenuti esterni possono tentare di cambiare il piano» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Contenuti esterni possono tentare di cambiare il piano». [SRC-72-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Prompt injection» conserviamo l'osservazione collegata a «Contenuti esterni possono tentare di cambiare il piano» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Prompt injection» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Dal concetto alla situazione concreta: Least privilege

Il caso intero parte dall'input «input non fidato, tool, scope e approvazione», applica l'operazione «least privilege, sandbox, human approval e rollback» e osserva l'output «allow/deny, side effect o rollback auditabile». Un esempio controllato: refund bloccato e lookup consentito con log firmato. Lo schema compatto è:

$$
allow = policy(input, tool, scope)
$$

È una notazione di interfaccia, non un'identità numerica completa. Sicurezza agentica richiede una decisione esterna alla sola generazione. [SRC-72-001]

![Sicurezza operativa degli agenti: loop](../../assets/chapters/72_agent_safety/SAFETY-02/candidate-v48.png)

La figura SAFETY-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Least privilege, sandbox, human approval e rollback. L'input è input non fidato, tool, scope e approvazione, l'output è allow/deny, side effect o rollback auditabile; il vincolo da controllare è che l'enforcement deve stare fuori dal testo generato.

## Una prova ripetibile: Sandbox

Il file `code/snip_72_contract.py` collega il contratto del capitolo alla frase «Contenuti esterni possono tentare di cambiare il piano». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-72-001.txt` conserva il risultato ripetibile del caso locale.

## Il trasferimento richiede altro: Prompt injection

Il meccanismo di «Sicurezza operativa degli agenti» resta legato al contratto locale. L'enforcement deve stare fuori dal testo generato. Prima di generalizzare la frase «Contenuti esterni possono tentare di cambiare il piano», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il filo che passa oltre: Sicurezza operativa degli agenti

Abbiamo seguito una decisione agentica su una risorsa reale, partendo dall'input «input non fidato, tool, scope e approvazione» e arrivando all'output «allow/deny, side effect o rollback auditabile». Le sezioni «Least privilege», «Sandbox», «Prompt injection» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: l'enforcement deve stare fuori dal testo generato. Il Capitolo 73, Distillazione e pruning, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Least privilege

1. Ricostruisci l'oggetto continuo a partire da «Least privilege» e indica quale parte della frase «Ogni tool riceve soltanto gli scope necessari» entra nel caso.
2. Spiega quale trasformazione collega «Least privilege» a «Prompt injection» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: l'enforcement deve stare fuori dal testo generato.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Contenuti esterni possono tentare di cambiare il piano» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Prompt injection

1. Ricostruisci «Least privilege» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «Sandbox» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Human approval» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Rollback e audit» in un test ripetibile.
5. Spiega come trasferire «Prompt injection» senza portare con sé una promessa non misurata.

## Dove verificare definizioni e risultati: Sicurezza operativa degli agenti

Il dossier di «Sicurezza operativa degli agenti» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il confine tra informazione e azione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
