<!--
chapter_id: CH-P11-RETRIEVAL
part_id: P11
order_key: 630
title: Information retrieval
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 63. Information retrieval

La richiesta «Il pacco non è arrivato» resta il caso guida. In questo capitolo la usiamo per distinguere query e documenti ordinati per rilevanza, trasformazione e risultato, senza nascondere i dettagli tecnici.

## Documenti, query e rilevanza

Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal bisogno informativo e dalle label disponibili. [SRC-63-001]

Per capire «Documenti, query e rilevanza» partiamo da questo caso: tre documenti vengono ordinati per sovrapposizione con la query. Il caso rende osservabile il punto centrale: «Un sistema di retrieval ordina documenti rispetto a una query».

Nel contratto locale, l'input «query, corpus, termini e indice» entra, l'operazione «BM25, dense retrieval, ANN e reranking» modifica il percorso e l'output «ranking con score e documento recuperato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Documenti, query e rilevanza»; resta da controllare che rilevanza del ranking e correttezza della risposta sono misure separate. La domanda locale è «Un sistema di retrieval ordina documenti rispetto a una query».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Un sistema di retrieval ordina documenti rispetto a una query». [SRC-63-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La rilevanza dipende dal bisogno informativo e dalle label disponibili. Il piccolo risultato resta un'illustrazione di «Un sistema di retrieval ordina documenti rispetto a una query», non una promessa generale.

Per verificare «Documenti, query e rilevanza» cambiamo una sola condizione vicina alla frase «Un sistema di retrieval ordina documenti rispetto a una query», teniamo fermo il resto e registriamo l'output «ranking con score e documento recuperato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «BM25», riceve l'output «ranking con score e documento recuperato» come base, ma dovrà formulare e verificare la propria distinzione.

## BM25

La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza. Tokenizzazione e campi modificano il punteggio. [SRC-63-002]

Il caso minimo di «BM25» si presenta così: tre documenti ordinati per sovrapposizione di termini. Non lo usiamo come decorazione: serve a rendere osservabile la frase «La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza».

La sezione usa l'input «query, corpus, termini e indice» come punto di partenza e l'output «ranking con score e documento recuperato» come traccia d'uscita. La trasformazione concreta è «BM25, dense retrieval, ANN e reranking»; il caso non è completo se non dichiariamo anche che rilevanza del ranking e correttezza della risposta sono misure separate. La condizione da isolare è «La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «BM25» il controllo cambia una sola premessa della frase «La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza». [SRC-63-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «BM25» conserviamo l'osservazione collegata a «La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «BM25» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «BM25» portiamo l'output «ranking con score e documento recuperato»; non portiamo invece una conclusione oltre il caso locale.

![Information retrieval: graph](../../assets/chapters/63_retrieval/RETRIEVAL-01/candidate-v48.png)

La figura RETRIEVAL-01 usa la famiglia graph. Il diagramma segue il passaggio: BM25, dense retrieval, ANN e reranking. L'input è query, corpus, termini e indice, l'output è ranking con score e documento recuperato; il vincolo da controllare è che rilevanza del ranking e correttezza della risposta sono misure separate.

## Dense retrieval

Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento dipende da positivi, negativi e in-batch sampling. [SRC-63-003]

Prima del nome tecnico fissiamo la situazione: consideriamo una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Da qui possiamo leggere la conseguenza dichiarata da «Un bi-encoder mappa query e documenti in vettori e usa una similarità».

Per ricostruire «Dense retrieval» annotiamo l'input «query, corpus, termini e indice», poi l'operazione «BM25, dense retrieval, ANN e reranking», infine l'output «ranking con score e documento recuperato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un bi-encoder mappa query e documenti in vettori e usa una similarità».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Un bi-encoder mappa query e documenti in vettori e usa una similarità». [SRC-63-003]

Il punto didattico di «Dense retrieval» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «ranking con score e documento recuperato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Dense retrieval» conserva input, operazione e output; poi esplicita quale parte di «Un bi-encoder mappa query e documenti in vettori e usa una similarità» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Indici ANN», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Indici ANN

Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall, memoria e latenza dipendono dalla struttura e dai parametri. [SRC-63-004]

Per capire «Indici ANN» partiamo da questo caso: una query e tre documenti ricevono punteggi distinti. Prima di generare, controlliamo quale documento è entrato nel contesto e con quale ranking. Il caso rende osservabile il punto centrale: «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo».

Nel contratto locale, l'input «query, corpus, termini e indice» entra, l'operazione «BM25, dense retrieval, ANN e reranking» modifica il percorso e l'output «ranking con score e documento recuperato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Indici ANN»; resta da controllare che rilevanza del ranking e correttezza della risposta sono misure separate. La domanda locale è «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Indici ANN» il controllo cambia una sola premessa della frase «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo». [SRC-63-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Recall, memoria e latenza dipendono dalla struttura e dai parametri. Il piccolo risultato resta un'illustrazione di «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo», non una promessa generale.

Per verificare «Indici ANN» cambiamo una sola condizione vicina alla frase «Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo», teniamo fermo il resto e registriamo l'output «ranking con score e documento recuperato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Reranking», riceve l'output «ranking con score e documento recuperato» come base, ma dovrà formulare e verificare la propria distinzione.

## Reranking

Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo. [SRC-63-001]

Il caso minimo di «Reranking» si presenta così: una query e tre documenti ricevono punteggi distinti. Prima di generare, controlliamo quale documento è entrato nel contesto e con quale ranking. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo».

La sezione usa l'input «query, corpus, termini e indice» come punto di partenza e l'output «ranking con score e documento recuperato» come traccia d'uscita. La trasformazione concreta è «BM25, dense retrieval, ANN e reranking»; il caso non è completo se non dichiariamo anche che rilevanza del ranking e correttezza della risposta sono misure separate. La condizione da isolare è «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Reranking» il controllo cambia una sola premessa della frase «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo». [SRC-63-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Reranking» conserviamo l'osservazione collegata a «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Reranking» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Una traiettoria controllata: Documenti, query e rilevanza

Il caso intero parte dall'input «query, corpus, termini e indice», applica l'operazione «BM25, dense retrieval, ANN e reranking» e osserva l'output «ranking con score e documento recuperato». Un esempio controllato: tre documenti ordinati per sovrapposizione di termini. La formula locale è:

$$
score(q,d) = bm25(q,d)
$$

Il ranking è una funzione osservabile prima di qualsiasi generazione. [SRC-63-001]

![Information retrieval: pipeline](../../assets/chapters/63_retrieval/RETRIEVAL-02/candidate-v48.png)

La figura RETRIEVAL-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: BM25, dense retrieval, ANN e reranking. L'input è query, corpus, termini e indice, l'output è ranking con score e documento recuperato; il vincolo da controllare è che rilevanza del ranking e correttezza della risposta sono misure separate.

## Il passaggio eseguito in Python: BM25

Lo snippet locale mette in esecuzione questo caso: tre documenti ordinati per sovrapposizione di termini. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-63-001.txt`, come evidenza locale e non come benchmark di produzione.

## Prima di generalizzare: Reranking

Il caso di «Information retrieval» non certifica un servizio completo. Rilevanza del ranking e correttezza della risposta sono misure separate. La domanda successiva è se «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Dalla lezione al capitolo seguente: Information retrieval

Il filo della lezione va dall'input «query, corpus, termini e indice» all'output «ranking con score e documento recuperato». Nei passaggi «Documenti, query e rilevanza», «BM25», «Reranking» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: rilevanza del ranking e correttezza della risposta sono misure separate. Il Capitolo 64, Retrieval-Augmented Generation, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Documenti, query e rilevanza

1. Ricostruisci l'oggetto continuo a partire da «Documenti, query e rilevanza» e indica quale parte della frase «Un sistema di retrieval ordina documenti rispetto a una query» entra nel caso.
2. Spiega quale trasformazione collega «Documenti, query e rilevanza» a «Reranking» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: rilevanza del ranking e correttezza della risposta sono misure separate.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Reranking

1. Ricostruisci «Documenti, query e rilevanza» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «BM25» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «Dense retrieval» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Indici ANN» in un test ripetibile.
5. Spiega come trasferire «Reranking» senza portare con sé una promessa non misurata.

## Dossier delle fonti e materiali: Information retrieval

Per ricontrollare «Information retrieval», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire la traccia della traiettoria prima dell'effetto oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
