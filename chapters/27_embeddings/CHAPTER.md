<!--
chapter_id: CH-P06-EMBEDDINGS
part_id: P06
order_key: 270
title: Embedding e spazio semantico
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 27. Embedding e spazio semantico

Il risultato precedente non è ancora una soluzione completa. Partiamo da un ID e il vettore che lo rappresenta e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «embedding, ranking o predizione» isoliamo il passaggio «lookup, pooling, similarità e normalizzazione» e ne misuriamo il limite prima di passare a Embedding e spazio semantico.

## Da ID a vettore

Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale. [SRC-27-001]

Per capire «Da ID a vettore» partiamo da questo caso: un caso minimo con input due ID, due vettori e una query e output «embedding, ranking o predizione». Il caso rende osservabile il punto centrale: «Una embedding table seleziona una riga per token».

Nel contratto locale, l'input «due ID, due vettori e una query» entra, l'operazione «lookup, pooling, similarità e normalizzazione» modifica il percorso e l'output «embedding, ranking o predizione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Da ID a vettore»; resta da controllare che la similarità dipende da training, metrica e normalizzazione. La domanda locale è «Una embedding table seleziona una riga per token».

Il passaggio da seguire in «Da ID a vettore» è quello descritto dalla frase «Una embedding table seleziona una riga per token»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Da ID a vettore» il controllo cambia una sola premessa della frase «Una embedding table seleziona una riga per token» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una embedding table seleziona una riga per token». [SRC-27-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La dimensione del vettore è una scelta architetturale. Il piccolo risultato resta un'illustrazione di «Una embedding table seleziona una riga per token», non una promessa generale.

Per verificare «Da ID a vettore» cambiamo una sola condizione vicina alla frase «Una embedding table seleziona una riga per token», teniamo fermo il resto e registriamo l'output «embedding, ranking o predizione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Word embedding», riceve l'output «embedding, ranking o predizione» come base, ma dovrà formulare e verificare la propria distinzione.

## Word embedding

Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo. [SRC-27-002]

Il caso minimo di «Word embedding» si presenta così: due ID che selezionano righe diverse dalla stessa embedding table, prima di aggiungere il contesto. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Word2vec e GloVe usano statistiche distributive con obiettivi differenti».

La sezione usa l'input «due ID, due vettori e una query» come punto di partenza e l'output «embedding, ranking o predizione» come traccia d'uscita. La trasformazione concreta è «lookup, pooling, similarità e normalizzazione»; il caso non è completo se non dichiariamo anche che la similarità dipende da training, metrica e normalizzazione. La condizione da isolare è «Word2vec e GloVe usano statistiche distributive con obiettivi differenti».

Una embedding table seleziona vettori per ID; il contesto e l'obiettivo possono poi trasformare quella rappresentazione. La similarità è una misura scelta per un uso, non una definizione universale di significato. Per «Word embedding» il controllo cambia una sola premessa della frase «Word2vec e GloVe usano statistiche distributive con obiettivi differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Word2vec e GloVe usano statistiche distributive con obiettivi differenti». [SRC-27-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Word embedding» conserviamo l'osservazione collegata a «Word2vec e GloVe usano statistiche distributive con obiettivi differenti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Word embedding» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Word embedding» portiamo l'output «embedding, ranking o predizione»; non portiamo invece una conclusione oltre il caso locale.

![Embedding e spazio semantico: branch](../../assets/chapters/27_embeddings/EMBEDDIN-01/candidate-v48.png)

La figura EMBEDDIN-01 usa la famiglia branch. Il diagramma segue il passaggio: Lookup, pooling, similarità e normalizzazione. L'input è due ID, due vettori e una query, l'output è embedding, ranking o predizione; il vincolo da controllare è che la similarità dipende da training, metrica e normalizzazione.

## Embedding contestuale

In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi. [SRC-27-003]

Prima del nome tecnico fissiamo la situazione: consideriamo due ID che selezionano righe diverse dalla stessa embedding table, prima di aggiungere il contesto. Da qui possiamo leggere la conseguenza dichiarata da «In un Transformer, la rappresentazione di un token cambia con il contesto».

Per ricostruire «Embedding contestuale» annotiamo l'input «due ID, due vettori e una query», poi l'operazione «lookup, pooling, similarità e normalizzazione», infine l'output «embedding, ranking o predizione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «In un Transformer, la rappresentazione di un token cambia con il contesto».

Una embedding table seleziona vettori per ID; il contesto e l'obiettivo possono poi trasformare quella rappresentazione. La similarità è una misura scelta per un uso, non una definizione universale di significato. Per «Embedding contestuale» il controllo cambia una sola premessa della frase «In un Transformer, la rappresentazione di un token cambia con il contesto» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «In un Transformer, la rappresentazione di un token cambia con il contesto». [SRC-27-003]

Il punto didattico di «Embedding contestuale» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «embedding, ranking o predizione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Embedding contestuale» conserva input, operazione e output; poi esplicita quale parte di «In un Transformer, la rappresentazione di un token cambia con il contesto» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Sentence embedding», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Sentence embedding

Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto. [SRC-27-004]

Per capire «Sentence embedding» partiamo da questo caso: due ID che selezionano righe diverse dalla stessa embedding table, prima di aggiungere il contesto. Il caso rende osservabile il punto centrale: «Pooling o training contrastivo producono vettori per frasi e documenti».

Nel contratto locale, l'input «due ID, due vettori e una query» entra, l'operazione «lookup, pooling, similarità e normalizzazione» modifica il percorso e l'output «embedding, ranking o predizione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Sentence embedding»; resta da controllare che la similarità dipende da training, metrica e normalizzazione. La domanda locale è «Pooling o training contrastivo producono vettori per frasi e documenti».

Una embedding table seleziona vettori per ID; il contesto e l'obiettivo possono poi trasformare quella rappresentazione. La similarità è una misura scelta per un uso, non una definizione universale di significato. Per «Sentence embedding» il controllo cambia una sola premessa della frase «Pooling o training contrastivo producono vettori per frasi e documenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Pooling o training contrastivo producono vettori per frasi e documenti». [SRC-27-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La metrica deve corrispondere all'uso previsto. Il piccolo risultato resta un'illustrazione di «Pooling o training contrastivo producono vettori per frasi e documenti», non una promessa generale.

Per verificare «Sentence embedding» cambiamo una sola condizione vicina alla frase «Pooling o training contrastivo producono vettori per frasi e documenti», teniamo fermo il resto e registriamo l'output «embedding, ranking o predizione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Ricerca e anisotropia», riceve l'output «embedding, ranking o predizione» come base, ma dovrà formulare e verificare la propria distinzione.

## Ricerca e anisotropia

Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking. [SRC-27-001]

Il caso minimo di «Ricerca e anisotropia» si presenta così: un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Cosine similarity è una convenzione, non una misura universale di significato».

La sezione usa l'input «due ID, due vettori e una query» come punto di partenza e l'output «embedding, ranking o predizione» come traccia d'uscita. La trasformazione concreta è «lookup, pooling, similarità e normalizzazione»; il caso non è completo se non dichiariamo anche che la similarità dipende da training, metrica e normalizzazione. La condizione da isolare è «Cosine similarity è una convenzione, non una misura universale di significato».

Una embedding table seleziona vettori per ID; il contesto e l'obiettivo possono poi trasformare quella rappresentazione. La similarità è una misura scelta per un uso, non una definizione universale di significato. Per «Ricerca e anisotropia» il controllo cambia una sola premessa della frase «Cosine similarity è una convenzione, non una misura universale di significato» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Cosine similarity è una convenzione, non una misura universale di significato». [SRC-27-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Ricerca e anisotropia» conserviamo l'osservazione collegata a «Cosine similarity è una convenzione, non una misura universale di significato» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Ricerca e anisotropia» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Un caso dall'input all'output: Da ID a vettore

Il caso intero parte dall'input «due ID, due vettori e una query», applica l'operazione «lookup, pooling, similarità e normalizzazione» e osserva l'output «embedding, ranking o predizione». Un esempio controllato: similarità coseno tra due vettori dopo la normalizzazione. La formula locale è:

$$
E[i]=W[i]
$$

Un ID seleziona una riga della tabella di embedding. [SRC-27-001]

![Embedding e spazio semantico: matrix](../../assets/chapters/27_embeddings/EMBEDDIN-02/candidate-v48.png)

La figura EMBEDDIN-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Lookup, pooling, similarità e normalizzazione. L'input è due ID, due vettori e una query, l'output è embedding, ranking o predizione; il vincolo da controllare è che la similarità dipende da training, metrica e normalizzazione.

## Dal meccanismo alla prova locale: Word embedding

Nel run Python rendiamo osservabile la frase «Una embedding table seleziona una riga per token» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-27-001.txt` documenta il caso senza pretendere una misura generale.

## Dove il risultato si ferma: Ricerca e anisotropia

Il meccanismo di «Embedding e spazio semantico» non garantisce da solo che il sistema funzioni fuori dal caso guida. La similarità dipende da training, metrica e normalizzazione. Il limite osservato riguarda la frase «Una embedding table seleziona una riga per token»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Che cosa portiamo avanti: Embedding e spazio semantico

Il percorso ha tenuto insieme un ID e il vettore che lo rappresenta, l'operazione «lookup, pooling, similarità e normalizzazione» e l'output «embedding, ranking o predizione». Le sezioni «Da ID a vettore», «Word embedding», «Ricerca e anisotropia» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: la similarità dipende da training, metrica e normalizzazione. Il Capitolo 28, Embedding e spazio semantico, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Da ID a vettore

1. Ricostruisci l'oggetto continuo a partire da «Da ID a vettore» e indica quale parte della frase «Una embedding table seleziona una riga per token» entra nel caso.
2. Spiega quale trasformazione collega «Da ID a vettore» a «Ricerca e anisotropia» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: la similarità dipende da training, metrica e normalizzazione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Cosine similarity è una convenzione, non una misura universale di significato» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Ricerca e anisotropia

1. Racconta «Da ID a vettore» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Word embedding» mantenendo il resto del setup invariato.
3. Per «Embedding contestuale», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Sentence embedding» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Ricerca e anisotropia» senza confondere livelli diversi.

## Fonti, codice e materiali: Embedding e spazio semantico

Per «Embedding e spazio semantico», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
