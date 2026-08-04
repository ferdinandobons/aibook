<!--
chapter_id: CH-P13-SAE-CIRCUIT-TRACING
part_id: P13
order_key: 870
title: Sparse autoencoder e interpretabilità scalabile
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 87. Sparse autoencoder e interpretabilità scalabile

Il risultato precedente non è ancora una soluzione completa. Partiamo da un'attivazione scomposta in feature sparse e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «feature, errore di ricostruzione e circuito candidato» isoliamo il passaggio «training SAE, splitting, dead features e tracing» e ne misuriamo il limite prima di passare a Robustezza, jailbreak e attacchi adversarial.

## Superposition

Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre un'ipotesi per separarle. [SRC-87-001]

Per capire «Superposition» partiamo da questo caso: due feature sparse ricostruiscono tre coordinate e l'errore viene registrato. Il caso rende osservabile il punto centrale: «Più feature possono condividere le stesse dimensioni di attivazione».

Nel contratto locale, l'input «attivazione, dizionario, sparsità e ricostruzione» entra, l'operazione «training SAE, splitting, dead features e tracing» modifica il percorso e l'output «feature, errore di ricostruzione e circuito candidato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Superposition»; resta da controllare che interpretabilità di una feature richiede valutazione e controlli indipendenti. La domanda locale è «Più feature possono condividere le stesse dimensioni di attivazione».

Il passaggio da seguire in «Superposition» è quello descritto dalla frase «Più feature possono condividere le stesse dimensioni di attivazione»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Superposition» il controllo cambia una sola premessa della frase «Più feature possono condividere le stesse dimensioni di attivazione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Più feature possono condividere le stesse dimensioni di attivazione». [SRC-87-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La sparsità offre un'ipotesi per separarle. Il piccolo risultato resta un'illustrazione di «Più feature possono condividere le stesse dimensioni di attivazione», non una promessa generale.

Per verificare «Superposition» cambiamo una sola condizione vicina alla frase «Più feature possono condividere le stesse dimensioni di attivazione», teniamo fermo il resto e registriamo l'output «feature, errore di ricostruzione e circuito candidato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Sparse autoencoder», riceve l'output «feature, errore di ricostruzione e circuito candidato» come base, ma dovrà formulare e verificare la propria distinzione.

## Sparse autoencoder

Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Loss e sparsity coefficient determinano il dizionario. [SRC-87-002]

Il caso minimo di «Sparse autoencoder» si presenta così: due feature attive, una ricostruzione e un intervento. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream».

La sezione usa l'input «attivazione, dizionario, sparsità e ricostruzione» come punto di partenza e l'output «feature, errore di ricostruzione e circuito candidato» come traccia d'uscita. La trasformazione concreta è «training SAE, splitting, dead features e tracing»; il caso non è completo se non dichiariamo anche che interpretabilità di una feature richiede valutazione e controlli indipendenti. La condizione da isolare è «Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream».

Una rappresentazione non ha significato isolato: è una quantità prodotta per un uso successivo. Obiettivo, dati, augmentazioni e metrica determinano quali relazioni vengono rese facili da leggere. Per «Sparse autoencoder» il controllo cambia una sola premessa della frase «Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream». [SRC-87-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Sparse autoencoder» conserviamo l'osservazione collegata a «Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Sparse autoencoder» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Sparse autoencoder» portiamo l'output «feature, errore di ricostruzione e circuito candidato»; non portiamo invece una conclusione oltre il caso locale.

![Sparse autoencoder e interpretabilità scalabile: scatter](../../assets/chapters/87_sae_circuit_tracing/TRACING-01/candidate-v48.png)

La figura TRACING-01 usa la famiglia scatter. Il diagramma segue il passaggio: Training SAE, splitting, dead features e tracing. L'input è attivazione, dizionario, sparsità e ricostruzione, l'output è feature, errore di ricostruzione e circuito candidato; il vincolo da controllare è che interpretabilità di una feature richiede valutazione e controlli indipendenti.

## Dead e splitting features

Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità. [SRC-87-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un manifest che conserva conteggi, checksum, tokenizer e confini dello split prima del training. Da qui possiamo leggere la conseguenza dichiarata da «Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità».

Per ricostruire «Dead e splitting features» annotiamo l'input «attivazione, dizionario, sparsità e ricostruzione», poi l'operazione «training SAE, splitting, dead features e tracing», infine l'output «feature, errore di ricostruzione e circuito candidato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. Per «Dead e splitting features» il controllo cambia una sola premessa della frase «Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità». [SRC-87-003]

Il punto didattico di «Dead e splitting features» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «feature, errore di ricostruzione e circuito candidato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Dead e splitting features» conserva input, operazione e output; poi esplicita quale parte di «Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Circuit tracing», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Circuit tracing

Feature e attribution graph possono collegare input, computazione e output. Il grafo resta un'approssimazione del calcolo completo. [SRC-87-004]

Per capire «Circuit tracing» partiamo da questo caso: quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Circuit tracing» e all'output feature, errore di ricostruzione e circuito candidato. Il caso rende osservabile il punto centrale: «Feature e attribution graph possono collegare input, computazione e output».

Nel contratto locale, l'input «attivazione, dizionario, sparsità e ricostruzione» entra, l'operazione «training SAE, splitting, dead features e tracing» modifica il percorso e l'output «feature, errore di ricostruzione e circuito candidato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Circuit tracing»; resta da controllare che interpretabilità di una feature richiede valutazione e controlli indipendenti. La domanda locale è «Feature e attribution graph possono collegare input, computazione e output».

Interpretare significa dichiarare quale oggetto viene analizzato e quale intervento o misura lo collega al comportamento. Informazione decodificabile, attribuzione e causalità non sono lo stesso risultato. Per «Circuit tracing» il controllo cambia una sola premessa della frase «Feature e attribution graph possono collegare input, computazione e output» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Feature e attribution graph possono collegare input, computazione e output». [SRC-87-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il grafo resta un'approssimazione del calcolo completo. Il piccolo risultato resta un'illustrazione di «Feature e attribution graph possono collegare input, computazione e output», non una promessa generale.

Per verificare «Circuit tracing» cambiamo una sola condizione vicina alla frase «Feature e attribution graph possono collegare input, computazione e output», teniamo fermo il resto e registriamo l'output «feature, errore di ricostruzione e circuito candidato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Valutazione», riceve l'output «feature, errore di ricostruzione e circuito candidato» come base, ma dovrà formulare e verificare la propria distinzione.

## Valutazione

Interpretabilità automatica, causal intervention e coverage devono essere misurate. Una etichetta leggibile non prova monosemanticità universale. [SRC-87-001]

Il caso minimo di «Valutazione» si presenta così: su un piccolo insieme, la metrica viene calcolata insieme a una slice e a un caso fallito. La media non sostituisce la diagnosi. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Interpretabilità automatica, causal intervention e coverage devono essere misurate».

La sezione usa l'input «attivazione, dizionario, sparsità e ricostruzione» come punto di partenza e l'output «feature, errore di ricostruzione e circuito candidato» come traccia d'uscita. La trasformazione concreta è «training SAE, splitting, dead features e tracing»; il caso non è completo se non dichiariamo anche che interpretabilità di una feature richiede valutazione e controlli indipendenti. La condizione da isolare è «Interpretabilità automatica, causal intervention e coverage devono essere misurate».

Una valutazione deve collegare claim, popolazione, protocollo e decisione. Media, slice, failure, giudice e incertezza misurano aspetti diversi e non diventano intercambiabili perché condividono una tabella. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Interpretabilità automatica, causal intervention e coverage devono essere misurate». [SRC-87-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Valutazione» conserviamo l'osservazione collegata a «Interpretabilità automatica, causal intervention e coverage devono essere misurate» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Valutazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Un esempio con controllo negativo: Superposition

Il caso intero parte dall'input «attivazione, dizionario, sparsità e ricostruzione», applica l'operazione «training SAE, splitting, dead features e tracing» e osserva l'output «feature, errore di ricostruzione e circuito candidato». Un esempio controllato: due feature attive, una ricostruzione e un intervento. Lo schema compatto è:

$$
feature = encode(activation)
$$

È una notazione di interfaccia, non un'identità numerica completa. Un circuito descritto da feature richiede controlli indipendenti sull'attivazione. [SRC-87-001]

![Sparse autoencoder e interpretabilità scalabile: architecture](../../assets/chapters/87_sae_circuit_tracing/TRACING-02/candidate-v48.png)

La figura TRACING-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Training SAE, splitting, dead features e tracing. L'input è attivazione, dizionario, sparsità e ricostruzione, l'output è feature, errore di ricostruzione e circuito candidato; il vincolo da controllare è che interpretabilità di una feature richiede valutazione e controlli indipendenti.

## Dalla formula al run: Sparse autoencoder

Il file `code/snip_87_contract.py` collega il contratto del capitolo alla frase «Interpretabilità automatica, causal intervention e coverage devono essere misurate». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-87-001.txt` conserva il risultato ripetibile del caso locale.

## Limiti, varianti e nuove misure: Valutazione

Il meccanismo di «Sparse autoencoder e interpretabilità scalabile» resta legato al contratto locale. Interpretabilità di una feature richiede valutazione e controlli indipendenti. Prima di generalizzare la frase «Interpretabilità automatica, causal intervention e coverage devono essere misurate», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## L'invariante da conservare: Sparse autoencoder e interpretabilità scalabile

Abbiamo seguito un'attivazione scomposta in feature sparse, partendo dall'input «attivazione, dizionario, sparsità e ricostruzione» e arrivando all'output «feature, errore di ricostruzione e circuito candidato». Le sezioni «Superposition», «Sparse autoencoder», «Valutazione» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: interpretabilità di una feature richiede valutazione e controlli indipendenti. Il Capitolo 88, Robustezza, jailbreak e attacchi adversarial, può partire da questo output e dichiarare la propria domanda.

### Prova di comprensione: Superposition

1. Ricostruisci l'oggetto continuo a partire da «Superposition» e indica quale parte della frase «Più feature possono condividere le stesse dimensioni di attivazione» entra nel caso.
2. Spiega quale trasformazione collega «Superposition» a «Valutazione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: interpretabilità di una feature richiede valutazione e controlli indipendenti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Interpretabilità automatica, causal intervention e coverage devono essere misurate» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi con casi limite: Valutazione

1. Ricostruisci input e output di «Superposition» usando un esempio di tre righe.
2. Modifica una sola variabile in «Sparse autoencoder» e anticipa l'invariante che dovrebbe restare.
3. Metti «Dead e splitting features» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Circuit tracing».
5. Formula per «Valutazione» una domanda che separi meccanismo e qualità del sistema.

## Fonti primarie e artefatti del capitolo: Sparse autoencoder e interpretabilità scalabile

Il dossier di «Sparse autoencoder e interpretabilità scalabile» in `FONTI_PRIMARIE.md` separa definizioni, risultati e la differenza tra media e failure; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
