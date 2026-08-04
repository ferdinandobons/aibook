<!--
chapter_id: CH-P11-RAG
part_id: P11
order_key: 640
title: Retrieval-Augmented Generation
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 64. Retrieval-Augmented Generation

Una frase plausibile non basta a spiegare retrieval-augmented generation. L'oggetto è la pipeline che collega query, contesto e risposta; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Una pipeline in due fasi

Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati. [SRC-64-001]

Il caso minimo di «Una pipeline in due fasi» si presenta così: due chunk vengono recuperati e una risposta mantiene il documento citato come record distinto. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati».

Per ricostruire «Una pipeline in due fasi» annotiamo l'input «query, chunk, fonti e prompt», poi l'operazione «chunking, retrieval, attribution e generazione», infine l'output «risposta con evidenza e score end-to-end». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Una pipeline in due fasi» il controllo cambia una sola premessa della frase «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati». [SRC-64-001]

Il punto didattico di «Una pipeline in due fasi» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risposta con evidenza e score end-to-end» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Una pipeline in due fasi» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Una pipeline in due fasi» portiamo l'output «risposta con evidenza e score end-to-end»; non portiamo invece una conclusione oltre il caso locale.

## Chunking

Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica. [SRC-64-002]

Prima del nome tecnico fissiamo la situazione: consideriamo due chunk citati e una frase che non compare nelle fonti. Da qui possiamo leggere la conseguenza dichiarata da «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto».

Nel contratto locale, l'input «query, chunk, fonti e prompt» entra, l'operazione «chunking, retrieval, attribution e generazione» modifica il percorso e l'output «risposta con evidenza e score end-to-end» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Chunking»; resta da controllare che contesto recuperato e testo generato devono restare distinguibili. La domanda locale è «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Chunking» il controllo cambia una sola premessa della frase «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto». [SRC-64-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Un chunk non coincide sempre con una unità semantica. Il piccolo risultato resta un'illustrazione di «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto», non una promessa generale.

La prova di «Chunking» conserva input, operazione e output; poi esplicita quale parte di «Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Prompt con fonti», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Prompt con fonti

Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto. [SRC-64-003]

Per capire «Prompt con fonti» partiamo da questo caso: un caso in cui contesto recuperato e testo generato devono restare distinguibili. Il caso rende osservabile il punto centrale: «Documenti, istruzioni e domanda devono avere confini espliciti».

La sezione usa l'input «query, chunk, fonti e prompt» come punto di partenza e l'output «risposta con evidenza e score end-to-end» come traccia d'uscita. La trasformazione concreta è «chunking, retrieval, attribution e generazione»; il caso non è completo se non dichiariamo anche che contesto recuperato e testo generato devono restare distinguibili. La condizione da isolare è «Documenti, istruzioni e domanda devono avere confini espliciti».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Prompt con fonti» il controllo cambia una sola premessa della frase «Documenti, istruzioni e domanda devono avere confini espliciti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Documenti, istruzioni e domanda devono avere confini espliciti». [SRC-64-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Prompt con fonti» conserviamo l'osservazione collegata a «Documenti, istruzioni e domanda devono avere confini espliciti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Prompt con fonti» cambiamo una sola condizione vicina alla frase «Documenti, istruzioni e domanda devono avere confini espliciti», teniamo fermo il resto e registriamo l'output «risposta con evidenza e score end-to-end». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Attribution», riceve l'output «risposta con evidenza e score end-to-end» come base, ma dovrà formulare e verificare la propria distinzione.

![Retrieval-Augmented Generation: pipeline](../../assets/chapters/64_rag/RAG-01/candidate-v48.png)

La figura RAG-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Chunking, retrieval, attribution e generazione. L'input è query, chunk, fonti e prompt, l'output è risposta con evidenza e score end-to-end; il vincolo da controllare è che contesto recuperato e testo generato devono restare distinguibili.

## Attribution

Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti. [SRC-64-004]

Il caso minimo di «Attribution» si presenta così: quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Attribution» e all'output risposta con evidenza e score end-to-end. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Una risposta supportata deve essere collegabile a passaggi recuperati».

Per ricostruire «Attribution» annotiamo l'input «query, chunk, fonti e prompt», poi l'operazione «chunking, retrieval, attribution e generazione», infine l'output «risposta con evidenza e score end-to-end». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Una risposta supportata deve essere collegabile a passaggi recuperati».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Attribution» il controllo cambia una sola premessa della frase «Una risposta supportata deve essere collegabile a passaggi recuperati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una risposta supportata deve essere collegabile a passaggi recuperati». [SRC-64-004]

Il punto didattico di «Attribution» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risposta con evidenza e score end-to-end» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Attribution» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Attribution» portiamo l'output «risposta con evidenza e score end-to-end»; non portiamo invece una conclusione oltre il caso locale.

## Valutazione end-to-end

Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme. [SRC-64-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una query e tre documenti ricevono punteggi distinti. Prima di generare, controlliamo quale documento è entrato nel contesto e con quale ranking. Da qui possiamo leggere la conseguenza dichiarata da «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme».

Nel contratto locale, l'input «query, chunk, fonti e prompt» entra, l'operazione «chunking, retrieval, attribution e generazione» modifica il percorso e l'output «risposta con evidenza e score end-to-end» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Valutazione end-to-end»; resta da controllare che contesto recuperato e testo generato devono restare distinguibili. La domanda locale è «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme». [SRC-64-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme», non una promessa generale.

La prova di «Valutazione end-to-end» conserva input, operazione e output; poi esplicita quale parte di «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «risposta con evidenza e score end-to-end» come evidenza locale e conserva la traccia della traiettoria prima dell'effetto come domanda aperta.

## Il contratto in un caso piccolo: Una pipeline in due fasi

Il caso intero parte dall'input «query, chunk, fonti e prompt», applica l'operazione «chunking, retrieval, attribution e generazione» e osserva l'output «risposta con evidenza e score end-to-end». Un esempio controllato: due chunk citati e una frase che non compare nelle fonti. La formula locale è:

$$
answer = generate(query, retrieve(query))
$$

Il contesto recuperato deve essere ispezionabile e separato dalla risposta. [SRC-64-001]

![Retrieval-Augmented Generation: graph](../../assets/chapters/64_rag/RAG-02/candidate-v48.png)

La figura RAG-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Chunking, retrieval, attribution e generazione. L'input è query, chunk, fonti e prompt, l'output è risposta con evidenza e score end-to-end; il vincolo da controllare è che contesto recuperato e testo generato devono restare distinguibili.

## Dalla trasformazione al test: Chunking

Nel run Python rendiamo osservabile la frase «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-64-001.txt` documenta il caso senza pretendere una misura generale.

## Il perimetro della conclusione: Valutazione end-to-end

Il meccanismo di «Retrieval-Augmented Generation» non garantisce da solo che il sistema funzioni fuori dal caso guida. Contesto recuperato e testo generato devono restare distinguibili. Il limite osservato riguarda la frase «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Una sintesi operativa: Retrieval-Augmented Generation

Il percorso ha tenuto insieme la pipeline che collega query, contesto e risposta, l'operazione «chunking, retrieval, attribution e generazione» e l'output «risposta con evidenza e score end-to-end». Le sezioni «Una pipeline in due fasi», «Chunking», «Valutazione end-to-end» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: contesto recuperato e testo generato devono restare distinguibili. Il Capitolo 65, RAG adattivo, correttivo e basato su grafi, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Una pipeline in due fasi

1. Ricostruisci l'oggetto continuo a partire da «Una pipeline in due fasi» e indica quale parte della frase «Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati» entra nel caso.
2. Spiega quale trasformazione collega «Una pipeline in due fasi» a «Valutazione end-to-end» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: contesto recuperato e testo generato devono restare distinguibili.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Valutazione end-to-end

1. Ricostruisci input e output di «Una pipeline in due fasi» usando un esempio di tre righe.
2. Modifica una sola variabile in «Chunking» e anticipa l'invariante che dovrebbe restare.
3. Metti «Prompt con fonti» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Attribution».
5. Formula per «Valutazione end-to-end» una domanda che separi meccanismo e qualità del sistema.

## Materiali, fonti e codice verificato: Retrieval-Augmented Generation

Per «Retrieval-Augmented Generation», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto decisione, tool e side effect. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
