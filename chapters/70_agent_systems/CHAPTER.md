<!--
chapter_id: CH-P11-AGENT-SYSTEMS
part_id: P11
order_key: 700
title: Multi-agent, browser, computer e code agents
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 70. Multi-agent, browser, computer e code agents

Il Capitolo 69, Ciclo agentico, pianificazione e verifica, ha lasciato disponibile una traiettoria composta da agenti e strumenti. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «delega, comunicazione, esecuzione e aggregazione» e verifichiamo che più agenti ampliano anche superficie e costo dell'errore.

## Browser agent

L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate. [SRC-70-001]

Il caso minimo di «Browser agent» si presenta così: planner, executor e critic scambiano tre messaggi con ruoli espliciti. Non lo usiamo come decorazione: serve a rendere osservabile la frase «L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate».

Per ricostruire «Browser agent» annotiamo l'input «task, ruoli, browser, codice e handoff», poi l'operazione «delega, comunicazione, esecuzione e aggregazione», infine l'output «risultato con responsabilità e log per componente». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate». [SRC-70-001]

Il punto didattico di «Browser agent» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato con responsabilità e log per componente» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Browser agent» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Browser agent» portiamo l'output «risultato con responsabilità e log per componente»; non portiamo invece una conclusione oltre il caso locale.

## Computer use

Screenshot, coordinate e azioni di input formano un loop percettivo. Risoluzione, focus e stato dell'interfaccia possono cambiare. [SRC-70-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un planner delega ricerca e verifica a due ruoli separati. Da qui possiamo leggere la conseguenza dichiarata da «Screenshot, coordinate e azioni di input formano un loop percettivo».

Nel contratto locale, l'input «task, ruoli, browser, codice e handoff» entra, l'operazione «delega, comunicazione, esecuzione e aggregazione» modifica il percorso e l'output «risultato con responsabilità e log per componente» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Computer use»; resta da controllare che più agenti ampliano anche superficie e costo dell'errore. La domanda locale è «Screenshot, coordinate e azioni di input formano un loop percettivo».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Computer use» il controllo cambia una sola premessa della frase «Screenshot, coordinate e azioni di input formano un loop percettivo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Screenshot, coordinate e azioni di input formano un loop percettivo». [SRC-70-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Risoluzione, focus e stato dell'interfaccia possono cambiare. Il piccolo risultato resta un'illustrazione di «Screenshot, coordinate e azioni di input formano un loop percettivo», non una promessa generale.

La prova di «Computer use» conserva input, operazione e output; poi esplicita quale parte di «Screenshot, coordinate e azioni di input formano un loop percettivo» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Code agent», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Code agent

Repository, test, shell e diff definiscono l'ambiente. Modifiche devono essere limitate, testate e revisionabili. [SRC-70-003]

Per capire «Code agent» partiamo da questo caso: una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Il caso rende osservabile il punto centrale: «Repository, test, shell e diff definiscono l'ambiente».

La sezione usa l'input «task, ruoli, browser, codice e handoff» come punto di partenza e l'output «risultato con responsabilità e log per componente» come traccia d'uscita. La trasformazione concreta è «delega, comunicazione, esecuzione e aggregazione»; il caso non è completo se non dichiariamo anche che più agenti ampliano anche superficie e costo dell'errore. La condizione da isolare è «Repository, test, shell e diff definiscono l'ambiente».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Repository, test, shell e diff definiscono l'ambiente». [SRC-70-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Code agent» conserviamo l'osservazione collegata a «Repository, test, shell e diff definiscono l'ambiente» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Code agent» cambiamo una sola condizione vicina alla frase «Repository, test, shell e diff definiscono l'ambiente», teniamo fermo il resto e registriamo l'output «risultato con responsabilità e log per componente». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Multi-agent», riceve l'output «risultato con responsabilità e log per componente» come base, ma dovrà formulare e verificare la propria distinzione.

![Multi-agent, browser, computer e code agents: graph](../../assets/chapters/70_agent_systems/SYSTEMS-01/candidate-v50.png)

La figura SYSTEMS-01 usa la famiglia graph. Il diagramma segue il passaggio: Delega, comunicazione, esecuzione e aggregazione. L'input è task, ruoli, browser, codice e handoff, l'output è risultato con responsabilità e log per componente; il vincolo da controllare è che più agenti ampliano anche superficie e costo dell'errore.

## Multi-agent

Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori. [SRC-70-004]

Il caso minimo di «Multi-agent» si presenta così: una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori».

Per ricostruire «Multi-agent» annotiamo l'input «task, ruoli, browser, codice e handoff», poi l'operazione «delega, comunicazione, esecuzione e aggregazione», infine l'output «risultato con responsabilità e log per componente». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori». [SRC-70-004]

Il punto didattico di «Multi-agent» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato con responsabilità e log per componente» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Multi-agent» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Multi-agent» portiamo l'output «risultato con responsabilità e log per componente»; non portiamo invece una conclusione oltre il caso locale.

## Confronto con un singolo workflow

Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget. [SRC-70-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata. Da qui possiamo leggere la conseguenza dichiarata da «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget».

Nel contratto locale, l'input «task, ruoli, browser, codice e handoff» entra, l'operazione «delega, comunicazione, esecuzione e aggregazione» modifica il percorso e l'output «risultato con responsabilità e log per componente» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Confronto con un singolo workflow»; resta da controllare che più agenti ampliano anche superficie e costo dell'errore. La domanda locale è «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Confronto con un singolo workflow» il controllo cambia una sola premessa della frase «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget». [SRC-70-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget», non una promessa generale.

La prova di «Confronto con un singolo workflow» conserva input, operazione e output; poi esplicita quale parte di «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «risultato con responsabilità e log per componente» come evidenza locale e conserva la traccia della traiettoria prima dell'effetto come domanda aperta.

## Il caso minimo e la sua variante: Browser agent

Il caso intero parte dall'input «task, ruoli, browser, codice e handoff», applica l'operazione «delega, comunicazione, esecuzione e aggregazione» e osserva l'output «risultato con responsabilità e log per componente». Un esempio controllato: un planner delega ricerca e verifica a due ruoli separati. Lo schema compatto è:

$$
trajectory = compose(agents, tools, browser)
$$

È una notazione di interfaccia, non un'identità numerica completa. Più componenti ampliano la traiettoria e anche la superficie di errore. [SRC-70-001]

![Multi-agent, browser, computer e code agents: compare](../../assets/chapters/70_agent_systems/SYSTEMS-02/candidate-v48.png)

La figura SYSTEMS-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Delega, comunicazione, esecuzione e aggregazione. L'input è task, ruoli, browser, codice e handoff, l'output è risultato con responsabilità e log per componente; il vincolo da controllare è che più agenti ampliano anche superficie e costo dell'errore.

## Che cosa osserva lo snippet: Computer use

Lo snippet locale mette in esecuzione questo caso: un planner delega ricerca e verifica a due ruoli separati. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-70-001.txt`, come evidenza locale e non come benchmark di produzione.

## Che cosa non dimostra: Confronto con un singolo workflow

Il caso di «Multi-agent, browser, computer e code agents» non certifica un servizio completo. Più agenti ampliano anche superficie e costo dell'errore. La domanda successiva è se «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget» regga quando cambiano dati, scala, hardware o criteri di decisione.

## La mappa delle condizioni: Multi-agent, browser, computer e code agents

Il filo della lezione va dall'input «task, ruoli, browser, codice e handoff» all'output «risultato con responsabilità e log per componente». Nei passaggi «Browser agent», «Computer use», «Confronto con un singolo workflow» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: più agenti ampliano anche superficie e costo dell'errore. Il Capitolo 71, Training e valutazione degli agenti, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Browser agent

1. Ricostruisci l'oggetto continuo a partire da «Browser agent» e indica quale parte della frase «L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate» entra nel caso.
2. Spiega quale trasformazione collega «Browser agent» a «Confronto con un singolo workflow» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: più agenti ampliano anche superficie e costo dell'errore.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Confronto con un singolo workflow

1. Ricostruisci «Browser agent» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «Computer use» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Code agent» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Multi-agent» in un test ripetibile.
5. Spiega come trasferire «Confronto con un singolo workflow» senza portare con sé una promessa non misurata.

## Fonti e risultati locali: Multi-agent, browser, computer e code agents

Per ricontrollare «Multi-agent, browser, computer e code agents», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire la traccia della traiettoria prima dell'effetto oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
