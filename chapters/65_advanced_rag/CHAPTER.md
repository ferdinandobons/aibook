<!--
chapter_id: CH-P11-ADVANCED-RAG
part_id: P11
order_key: 650
title: RAG adattivo, correttivo e basato su grafi
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 65. RAG adattivo, correttivo e basato su grafi

Il Capitolo 64, Retrieval-Augmented Generation, ha lasciato disponibile una query instradata tra retriever e grafo. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «query transformation, routing e corrective retrieval» e verifichiamo che un router può sbagliare anche quando il generatore è corretto.

## Query transformation

Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni trasformazione può migliorare recall o introdurre drift. [SRC-65-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una domanda segue il percorso q1 -> d1 -> q2 -> d2. Da qui possiamo leggere la conseguenza dichiarata da «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval».

La sezione usa l'input «domanda multi-hop, nodi, archi e documenti» come punto di partenza e l'output «sottoquery, percorso e contesto selezionato» come traccia d'uscita. La trasformazione concreta è «query transformation, routing e corrective retrieval»; il caso non è completo se non dichiariamo anche che un router può sbagliare anche quando il generatore è corretto. La condizione da isolare è «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval». [SRC-65-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Query transformation» conserviamo l'osservazione collegata a «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Query transformation» conserva input, operazione e output; poi esplicita quale parte di «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Retrieval adattivo», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Retrieval adattivo

Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un componente da valutare, non un comportamento gratuito del modello. [SRC-65-002]

Per capire «Retrieval adattivo» partiamo da questo caso: una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Il caso rende osservabile il punto centrale: «Il sistema decide se recuperare, quante volte e con quale sorgente».

Per ricostruire «Retrieval adattivo» annotiamo l'input «domanda multi-hop, nodi, archi e documenti», poi l'operazione «query transformation, routing e corrective retrieval», infine l'output «sottoquery, percorso e contesto selezionato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il sistema decide se recuperare, quante volte e con quale sorgente».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Il sistema decide se recuperare, quante volte e con quale sorgente». [SRC-65-002]

Il punto didattico di «Retrieval adattivo» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «sottoquery, percorso e contesto selezionato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Retrieval adattivo» cambiamo una sola condizione vicina alla frase «Il sistema decide se recuperare, quante volte e con quale sorgente», teniamo fermo il resto e registriamo l'output «sottoquery, percorso e contesto selezionato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Corrective RAG», riceve l'output «sottoquery, percorso e contesto selezionato» come base, ma dovrà formulare e verificare la propria distinzione.

## Corrective RAG

Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e web fallback richiedono soglie e autorizzazioni. [SRC-65-003]

Il caso minimo di «Corrective RAG» si presenta così: una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Documenti vengono valutati, filtrati o sostituiti prima della generazione».

Nel contratto locale, l'input «domanda multi-hop, nodi, archi e documenti» entra, l'operazione «query transformation, routing e corrective retrieval» modifica il percorso e l'output «sottoquery, percorso e contesto selezionato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Corrective RAG»; resta da controllare che un router può sbagliare anche quando il generatore è corretto. La domanda locale è «Documenti vengono valutati, filtrati o sostituiti prima della generazione».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Documenti vengono valutati, filtrati o sostituiti prima della generazione». [SRC-65-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Confidence e web fallback richiedono soglie e autorizzazioni. Il piccolo risultato resta un'illustrazione di «Documenti vengono valutati, filtrati o sostituiti prima della generazione», non una promessa generale.

Il controllo minimo di «Corrective RAG» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Corrective RAG» portiamo l'output «sottoquery, percorso e contesto selezionato»; non portiamo invece una conclusione oltre il caso locale.

## Graph RAG

Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da estrazione, normalizzazione e aggiornamento. [SRC-65-004]

Prima del nome tecnico fissiamo la situazione: consideriamo una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Da qui possiamo leggere la conseguenza dichiarata da «Entità, relazioni e comunità permettono query e sintesi multi-hop».

La sezione usa l'input «domanda multi-hop, nodi, archi e documenti» come punto di partenza e l'output «sottoquery, percorso e contesto selezionato» come traccia d'uscita. La trasformazione concreta è «query transformation, routing e corrective retrieval»; il caso non è completo se non dichiariamo anche che un router può sbagliare anche quando il generatore è corretto. La condizione da isolare è «Entità, relazioni e comunità permettono query e sintesi multi-hop».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Entità, relazioni e comunità permettono query e sintesi multi-hop». [SRC-65-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Graph RAG» conserviamo l'osservazione collegata a «Entità, relazioni e comunità permettono query e sintesi multi-hop» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Graph RAG» conserva input, operazione e output; poi esplicita quale parte di «Entità, relazioni e comunità permettono query e sintesi multi-hop» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «RAG agentico», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![RAG adattivo, correttivo e basato su grafi: branch](../../assets/chapters/65_advanced_rag/RAG-01/candidate-v48.png)

La figura RAG-01 usa la famiglia branch. Il diagramma segue il passaggio: Query transformation, routing e corrective retrieval. L'input è domanda multi-hop, nodi, archi e documenti, l'output è sottoquery, percorso e contesto selezionato; il vincolo da controllare è che un router può sbagliare anche quando il generatore è corretto.

## RAG agentico

Un agente può pianificare retrieval successivi. Più step aumentano copertura e contemporaneamente costo, errori e superficie di attacco. [SRC-65-001]

Per capire «RAG agentico» partiamo da questo caso: una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Il caso rende osservabile il punto centrale: «Un agente può pianificare retrieval successivi».

Per ricostruire «RAG agentico» annotiamo l'input «domanda multi-hop, nodi, archi e documenti», poi l'operazione «query transformation, routing e corrective retrieval», infine l'output «sottoquery, percorso e contesto selezionato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un agente può pianificare retrieval successivi».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Un agente può pianificare retrieval successivi». [SRC-65-001]

Il punto didattico di «RAG agentico» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «sottoquery, percorso e contesto selezionato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «RAG agentico» cambiamo una sola condizione vicina alla frase «Un agente può pianificare retrieval successivi», teniamo fermo il resto e registriamo l'output «sottoquery, percorso e contesto selezionato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Dal concetto alla situazione concreta: Query transformation

Il caso intero parte dall'input «domanda multi-hop, nodi, archi e documenti», applica l'operazione «query transformation, routing e corrective retrieval» e osserva l'output «sottoquery, percorso e contesto selezionato». Un esempio controllato: una domanda divisa in due sottoquery con un arco mancante. Lo schema compatto è:

$$
context = route(query, graph, retriever)
$$

È una notazione di interfaccia, non un'identità numerica completa. Il router sceglie una fonte, ma la scelta resta da valutare. [SRC-65-001]

![RAG adattivo, correttivo e basato su grafi: graph](../../assets/chapters/65_advanced_rag/RAG-02/candidate-v48.png)

La figura RAG-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Query transformation, routing e corrective retrieval. L'input è domanda multi-hop, nodi, archi e documenti, l'output è sottoquery, percorso e contesto selezionato; il vincolo da controllare è che un router può sbagliare anche quando il generatore è corretto.

## Una prova ripetibile: Retrieval adattivo

Il file `code/snip_65_contract.py` collega il contratto del capitolo alla frase «Un agente può pianificare retrieval successivi». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-65-001.txt` conserva il risultato ripetibile del caso locale.

## Il trasferimento richiede altro: RAG agentico

Il meccanismo di «RAG adattivo, correttivo e basato su grafi» resta legato al contratto locale. Un router può sbagliare anche quando il generatore è corretto. Prima di generalizzare la frase «Un agente può pianificare retrieval successivi», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il filo che passa oltre: RAG adattivo, correttivo e basato su grafi

Abbiamo seguito una query instradata tra retriever e grafo, partendo dall'input «domanda multi-hop, nodi, archi e documenti» e arrivando all'output «sottoquery, percorso e contesto selezionato». Le sezioni «Query transformation», «Retrieval adattivo», «RAG agentico» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: un router può sbagliare anche quando il generatore è corretto. Il Capitolo 66, Contesto lungo, retrieval e memoria, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Query transformation

1. Ricostruisci l'oggetto continuo a partire da «Query transformation» e indica quale parte della frase «Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval» entra nel caso.
2. Spiega quale trasformazione collega «Query transformation» a «RAG agentico» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un router può sbagliare anche quando il generatore è corretto.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Un agente può pianificare retrieval successivi» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: RAG agentico

1. Disegna il percorso di «Query transformation» indicando dati in ingresso e risultato.
2. Ripeti «Retrieval adattivo» cambiando soltanto un valore dichiarato.
3. Trova in «Corrective RAG» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Graph RAG» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «RAG agentico» richiederebbe un benchmark ulteriore.

## Dove verificare definizioni e risultati: RAG adattivo, correttivo e basato su grafi

Il dossier di «RAG adattivo, correttivo e basato su grafi» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il confine tra informazione e azione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
