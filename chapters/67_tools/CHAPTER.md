<!--
chapter_id: CH-P11-TOOLS
part_id: P11
order_key: 670
title: Output strutturato e uso degli strumenti
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 67. Output strutturato e uso degli strumenti

Il risultato precedente non è ancora una soluzione completa. Partiamo da una chiamata a tool con schema e autorizzazione e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «risultato del tool o rifiuto tracciato» isoliamo il passaggio «parsing, selezione, esecuzione e osservazione» e ne misuriamo il limite prima di passare a Protocolli e interoperabilità.

## Schema dell'output

JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non garantisce correttezza semantica. [SRC-67-001]

Il caso minimo di «Schema dell'output» si presenta così: lookup_order passa l'allowlist, mentre refund viene rifiutato prima del side effect. Non lo usiamo come decorazione: serve a rendere osservabile la frase «JSON Schema, grammar o tipi stabiliscono campi e vincoli».

Per ricostruire «Schema dell'output» annotiamo l'input «nome, argomenti, scope e stato», poi l'operazione «parsing, selezione, esecuzione e osservazione», infine l'output «risultato del tool o rifiuto tracciato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «JSON Schema, grammar o tipi stabiliscono campi e vincoli».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Schema dell'output» il controllo cambia una sola premessa della frase «JSON Schema, grammar o tipi stabiliscono campi e vincoli» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «JSON Schema, grammar o tipi stabiliscono campi e vincoli». [SRC-67-001]

Il punto didattico di «Schema dell'output» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato del tool o rifiuto tracciato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Schema dell'output» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Schema dell'output» portiamo l'output «risultato del tool o rifiuto tracciato»; non portiamo invece una conclusione oltre il caso locale.

## Selezione del tool

Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e autorizzazioni influenzano la decisione. [SRC-67-002]

Prima del nome tecnico fissiamo la situazione: consideriamo una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Da qui possiamo leggere la conseguenza dichiarata da «Il modello sceglie una funzione tra opzioni descritte».

Nel contratto locale, l'input «nome, argomenti, scope e stato» entra, l'operazione «parsing, selezione, esecuzione e osservazione» modifica il percorso e l'output «risultato del tool o rifiuto tracciato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Selezione del tool»; resta da controllare che schema valido non significa permesso di eseguire il side effect. La domanda locale è «Il modello sceglie una funzione tra opzioni descritte».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Il modello sceglie una funzione tra opzioni descritte». [SRC-67-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Nomi, descrizioni e autorizzazioni influenzano la decisione. Il piccolo risultato resta un'illustrazione di «Il modello sceglie una funzione tra opzioni descritte», non una promessa generale.

La prova di «Selezione del tool» conserva input, operazione e output; poi esplicita quale parte di «Il modello sceglie una funzione tra opzioni descritte» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Argomenti», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Argomenti

Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi mancanti richiedono chiarimento o fallback. [SRC-67-003]

Per capire «Argomenti» partiamo da questo caso: un caso in cui schema valido non significa permesso di eseguire il side effect. Il caso rende osservabile il punto centrale: «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione».

La sezione usa l'input «nome, argomenti, scope e stato» come punto di partenza e l'output «risultato del tool o rifiuto tracciato» come traccia d'uscita. La trasformazione concreta è «parsing, selezione, esecuzione e osservazione»; il caso non è completo se non dichiariamo anche che schema valido non significa permesso di eseguire il side effect. La condizione da isolare è «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Argomenti» il controllo cambia una sola premessa della frase «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione». [SRC-67-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Argomenti» conserviamo l'osservazione collegata a «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Argomenti» cambiamo una sola condizione vicina alla frase «Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione», teniamo fermo il resto e registriamo l'output «risultato del tool o rifiuto tracciato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Esecuzione e osservazione», riceve l'output «risultato del tool o rifiuto tracciato» come base, ma dovrà formulare e verificare la propria distinzione.

![Output strutturato e uso degli strumenti: branch](../../assets/chapters/67_tools/TOOLS-01/candidate-v48.png)

La figura TOOLS-01 usa la famiglia branch. Il diagramma segue il passaggio: Parsing, selezione, esecuzione e osservazione. L'input è nome, argomenti, scope e stato, l'output è risultato del tool o rifiuto tracciato; il vincolo da controllare è che schema valido non significa permesso di eseguire il side effect.

## Esecuzione e osservazione

Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Timeout ed errori devono essere rappresentati. [SRC-67-004]

Il caso minimo di «Esecuzione e osservazione» si presenta così: una traiettoria minima alterna osservazione, decisione, tool e verifica. Il test può controllare che un'azione non autorizzata venga bloccata. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato».

Per ricostruire «Esecuzione e osservazione» annotiamo l'input «nome, argomenti, scope e stato», poi l'operazione «parsing, selezione, esecuzione e osservazione», infine l'output «risultato del tool o rifiuto tracciato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Esecuzione e osservazione» il controllo cambia una sola premessa della frase «Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato». [SRC-67-004]

Il punto didattico di «Esecuzione e osservazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato del tool o rifiuto tracciato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Esecuzione e osservazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Esecuzione e osservazione» portiamo l'output «risultato del tool o rifiuto tracciato»; non portiamo invece una conclusione oltre il caso locale.

## Idempotenza e side effect

Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate. [SRC-67-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una traiettoria minima alterna osservazione, decisione, tool e verifica. Il test può controllare che un'azione non autorizzata venga bloccata. Da qui possiamo leggere la conseguenza dichiarata da «Operazioni di lettura e scrittura hanno rischi differenti».

Nel contratto locale, l'input «nome, argomenti, scope e stato» entra, l'operazione «parsing, selezione, esecuzione e osservazione» modifica il percorso e l'output «risultato del tool o rifiuto tracciato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Idempotenza e side effect»; resta da controllare che schema valido non significa permesso di eseguire il side effect. La domanda locale è «Operazioni di lettura e scrittura hanno rischi differenti».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Idempotenza e side effect» il controllo cambia una sola premessa della frase «Operazioni di lettura e scrittura hanno rischi differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Operazioni di lettura e scrittura hanno rischi differenti». [SRC-67-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate. Il piccolo risultato resta un'illustrazione di «Operazioni di lettura e scrittura hanno rischi differenti», non una promessa generale.

La prova di «Idempotenza e side effect» conserva input, operazione e output; poi esplicita quale parte di «Operazioni di lettura e scrittura hanno rischi differenti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «risultato del tool o rifiuto tracciato» come evidenza locale e conserva la traccia della traiettoria prima dell'effetto come domanda aperta.

## Il caso minimo e la sua variante: Schema dell'output

Il caso intero parte dall'input «nome, argomenti, scope e stato», applica l'operazione «parsing, selezione, esecuzione e osservazione» e osserva l'output «risultato del tool o rifiuto tracciato». Un esempio controllato: lookup consentito e refund rifiutato da allowlist. Lo schema compatto è:

$$
tool_call = schema(name, args, scope)
$$

È una notazione di interfaccia, non un'identità numerica completa. Lo schema rende l'azione parsabile, non automaticamente autorizzata. [SRC-67-001]

![Output strutturato e uso degli strumenti: pipeline](../../assets/chapters/67_tools/TOOLS-02/candidate-v50.png)

La figura TOOLS-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Parsing, selezione, esecuzione e osservazione. L'input è nome, argomenti, scope e stato, l'output è risultato del tool o rifiuto tracciato; il vincolo da controllare è che schema valido non significa permesso di eseguire il side effect.

## Che cosa osserva lo snippet: Selezione del tool

Il file `code/snip_67_contract.py` collega il contratto del capitolo alla frase «Operazioni di lettura e scrittura hanno rischi differenti». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-67-001.txt` conserva il risultato ripetibile del caso locale.

## Che cosa non dimostra: Idempotenza e side effect

Il meccanismo di «Output strutturato e uso degli strumenti» resta legato al contratto locale. Schema valido non significa permesso di eseguire il side effect. Prima di generalizzare la frase «Operazioni di lettura e scrittura hanno rischi differenti», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## La mappa delle condizioni: Output strutturato e uso degli strumenti

Abbiamo seguito una chiamata a tool con schema e autorizzazione, partendo dall'input «nome, argomenti, scope e stato» e arrivando all'output «risultato del tool o rifiuto tracciato». Le sezioni «Schema dell'output», «Selezione del tool», «Idempotenza e side effect» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: schema valido non significa permesso di eseguire il side effect. Il Capitolo 68, Protocolli e interoperabilità, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Schema dell'output

1. Ricostruisci l'oggetto continuo a partire da «Schema dell'output» e indica quale parte della frase «JSON Schema, grammar o tipi stabiliscono campi e vincoli» entra nel caso.
2. Spiega quale trasformazione collega «Schema dell'output» a «Idempotenza e side effect» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: schema valido non significa permesso di eseguire il side effect.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Operazioni di lettura e scrittura hanno rischi differenti» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Idempotenza e side effect

1. Disegna il percorso di «Schema dell'output» indicando dati in ingresso e risultato.
2. Ripeti «Selezione del tool» cambiando soltanto un valore dichiarato.
3. Trova in «Argomenti» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Esecuzione e osservazione» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Idempotenza e side effect» richiederebbe un benchmark ulteriore.

## Fonti e risultati locali: Output strutturato e uso degli strumenti

Il dossier di «Output strutturato e uso degli strumenti» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il confine tra informazione e azione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
