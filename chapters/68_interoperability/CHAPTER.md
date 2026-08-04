<!--
chapter_id: CH-P11-INTEROPERABILITY
part_id: P11
order_key: 680
title: Protocolli e interoperabilità
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 68. Protocolli e interoperabilità

La richiesta «Il pacco non è arrivato» resta il caso guida. In questo capitolo la usiamo per distinguere un messaggio tra componenti con identità e versione, trasformazione e risultato, senza nascondere i dettagli tecnici.

## Contratti tra componenti

Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool. [SRC-68-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un producer versione 1 è compatibile con un consumer che accetta le versioni 1 e 2. Da qui possiamo leggere la conseguenza dichiarata da «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool».

La sezione usa l'input «capability, schema, token e policy» come punto di partenza e l'output «messaggio accettato o errore di protocollo» come traccia d'uscita. La trasformazione concreta è «negoziazione, encoding, autorizzazione e compatibilità»; il caso non è completo se non dichiariamo anche che compatibilità sintattica non garantisce semantica o autorizzazione. La condizione da isolare è «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Contratti tra componenti» il controllo cambia una sola premessa della frase «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool». [SRC-68-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Contratti tra componenti» conserviamo l'osservazione collegata a «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Contratti tra componenti» conserva input, operazione e output; poi esplicita quale parte di «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Model Context Protocol», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Model Context Protocol

MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il trasporto devono essere dichiarati. [SRC-68-001]

Per capire «Model Context Protocol» partiamo da questo caso: un server MCP che espone una capability e un tool con schema degli argomenti. Il caso rende osservabile il punto centrale: «MCP organizza risorse, prompt e tool esposti da server».

Per ricostruire «Model Context Protocol» annotiamo l'input «capability, schema, token e policy», poi l'operazione «negoziazione, encoding, autorizzazione e compatibilità», infine l'output «messaggio accettato o errore di protocollo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «MCP organizza risorse, prompt e tool esposti da server».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Model Context Protocol» il controllo cambia una sola premessa della frase «MCP organizza risorse, prompt e tool esposti da server» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «MCP organizza risorse, prompt e tool esposti da server». [SRC-68-001]

Il punto didattico di «Model Context Protocol» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «messaggio accettato o errore di protocollo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Model Context Protocol» cambiamo una sola condizione vicina alla frase «MCP organizza risorse, prompt e tool esposti da server», teniamo fermo il resto e registriamo l'output «messaggio accettato o errore di protocollo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Agent-to-agent», riceve l'output «messaggio accettato o errore di protocollo» come base, ma dovrà formulare e verificare la propria distinzione.

## Agent-to-agent

Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti. [SRC-68-002]

Il caso minimo di «Agent-to-agent» si presenta così: un task A2A che passa da discovery a working e poi a completed. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti».

Nel contratto locale, l'input «capability, schema, token e policy» entra, l'operazione «negoziazione, encoding, autorizzazione e compatibilità» modifica il percorso e l'output «messaggio accettato o errore di protocollo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Agent-to-agent»; resta da controllare che compatibilità sintattica non garantisce semantica o autorizzazione. La domanda locale è «Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist. La verifica resta ancorata a «Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti». [SRC-68-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti», non una promessa generale.

Il controllo minimo di «Agent-to-agent» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Agent-to-agent» portiamo l'output «messaggio accettato o errore di protocollo»; non portiamo invece una conclusione oltre il caso locale.

## Identità e autorizzazione

Interoperabilità non implica fiducia. Token, scope, provenance e policy devono attraversare ogni hop. [SRC-68-003]

Prima del nome tecnico fissiamo la situazione: consideriamo una credenziale firmata con subject, scope, issuer e scadenza. Da qui possiamo leggere la conseguenza dichiarata da «Interoperabilità non implica fiducia».

La sezione usa l'input «capability, schema, token e policy» come punto di partenza e l'output «messaggio accettato o errore di protocollo» come traccia d'uscita. La trasformazione concreta è «negoziazione, encoding, autorizzazione e compatibilità»; il caso non è completo se non dichiariamo anche che compatibilità sintattica non garantisce semantica o autorizzazione. La condizione da isolare è «Interoperabilità non implica fiducia».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Identità e autorizzazione» il controllo cambia una sola premessa della frase «Interoperabilità non implica fiducia» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Interoperabilità non implica fiducia». [SRC-68-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Identità e autorizzazione» conserviamo l'osservazione collegata a «Interoperabilità non implica fiducia» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Identità e autorizzazione» conserva input, operazione e output; poi esplicita quale parte di «Interoperabilità non implica fiducia» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Compatibilità ed evoluzione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Protocolli e interoperabilità: compare](../../assets/chapters/68_interoperability/INTEROPERA-01/candidate-v50.png)

La figura INTEROPERA-01 usa la famiglia compare. Il diagramma segue il passaggio: Negoziazione, encoding, autorizzazione e compatibilità. L'input è capability, schema, token e policy, l'output è messaggio accettato o errore di protocollo; il vincolo da controllare è che compatibilità sintattica non garantisce semantica o autorizzazione.

## Compatibilità ed evoluzione

Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow. [SRC-68-004]

Per capire «Compatibilità ed evoluzione» partiamo da questo caso: una negoziazione che rifiuta un campo nuovo quando la versione non lo supporta. Il caso rende osservabile il punto centrale: «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow».

Per ricostruire «Compatibilità ed evoluzione» annotiamo l'input «capability, schema, token e policy», poi l'operazione «negoziazione, encoding, autorizzazione e compatibilità», infine l'output «messaggio accettato o errore di protocollo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow».

Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto. Per «Compatibilità ed evoluzione» il controllo cambia una sola premessa della frase «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow». [SRC-68-004]

Il punto didattico di «Compatibilità ed evoluzione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «messaggio accettato o errore di protocollo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Compatibilità ed evoluzione» cambiamo una sola condizione vicina alla frase «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow», teniamo fermo il resto e registriamo l'output «messaggio accettato o errore di protocollo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il caso minimo e la sua variante: Contratti tra componenti

Il caso intero parte dall'input «capability, schema, token e policy», applica l'operazione «negoziazione, encoding, autorizzazione e compatibilità» e osserva l'output «messaggio accettato o errore di protocollo». Un esempio controllato: due versioni dello schema con campo obbligatorio mancante. Lo schema compatto è:

$$
message = protocol.encode(state)
$$

È una notazione di interfaccia, non un'identità numerica completa. Un protocollo definisce formato e semantica condivisa tra componenti. [SRC-68-001]

![Protocolli e interoperabilità: graph](../../assets/chapters/68_interoperability/INTEROPERA-02/candidate-v48.png)

La figura INTEROPERA-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Negoziazione, encoding, autorizzazione e compatibilità. L'input è capability, schema, token e policy, l'output è messaggio accettato o errore di protocollo; il vincolo da controllare è che compatibilità sintattica non garantisce semantica o autorizzazione.

## Che cosa osserva lo snippet: Model Context Protocol

Nel run Python rendiamo osservabile la frase «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-68-001.txt` documenta il caso senza pretendere una misura generale.

## Che cosa non dimostra: Compatibilità ed evoluzione

Il meccanismo di «Protocolli e interoperabilità» non garantisce da solo che il sistema funzioni fuori dal caso guida. Compatibilità sintattica non garantisce semantica o autorizzazione. Il limite osservato riguarda la frase «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## La mappa delle condizioni: Protocolli e interoperabilità

Il percorso ha tenuto insieme un messaggio tra componenti con identità e versione, l'operazione «negoziazione, encoding, autorizzazione e compatibilità» e l'output «messaggio accettato o errore di protocollo». Le sezioni «Contratti tra componenti», «Model Context Protocol», «Compatibilità ed evoluzione» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: compatibilità sintattica non garantisce semantica o autorizzazione. Il Capitolo 69, Ciclo agentico, pianificazione e verifica, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Contratti tra componenti

1. Ricostruisci l'oggetto continuo a partire da «Contratti tra componenti» e indica quale parte della frase «Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool» entra nel caso.
2. Spiega quale trasformazione collega «Contratti tra componenti» a «Compatibilità ed evoluzione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: compatibilità sintattica non garantisce semantica o autorizzazione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Compatibilità ed evoluzione

1. Ricostruisci input e output di «Contratti tra componenti» usando un esempio di tre righe.
2. Modifica una sola variabile in «Model Context Protocol» e anticipa l'invariante che dovrebbe restare.
3. Metti «Agent-to-agent» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Identità e autorizzazione».
5. Formula per «Compatibilità ed evoluzione» una domanda che separi meccanismo e qualità del sistema.

## Fonti e risultati locali: Protocolli e interoperabilità

Per «Protocolli e interoperabilità», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto decisione, tool e side effect. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
