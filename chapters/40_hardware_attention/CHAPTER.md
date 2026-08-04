<!--
chapter_id: CH-P08-HARDWARE-AWARE-ATTENTION
part_id: P08
order_key: 400
title: Attention hardware-aware
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 40. Attention hardware-aware

Il Capitolo 39, Varianti dell'attention e gestione KV, ha lasciato disponibile il calcolo dell'attention e il suo movimento di dati. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «tiling, softmax online e ricomputazione» e verifichiamo che una misura hardware dipende da shape, backend e precisione.

## FLOP e movimento dei dati

Lo stesso operatore può avere traffico di memoria molto diverso. [SRC-40-001]

Il caso minimo di «FLOP e movimento dei dati» si presenta così: un caso minimo con input tile di Q, K, V, dtype e device e output «stesso contratto matematico con memoria e latenza misurate». Non lo usiamo come decorazione: serve a rendere osservabile la frase «Lo stesso operatore può avere traffico di memoria molto diverso».

Per ricostruire «FLOP e movimento dei dati» annotiamo l'input «tile di Q, K, V, dtype e device», poi l'operazione «tiling, softmax online e ricomputazione», infine l'output «stesso contratto matematico con memoria e latenza misurate». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Lo stesso operatore può avere traffico di memoria molto diverso».

L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare. Per «FLOP e movimento dei dati» il controllo cambia una sola premessa della frase «Lo stesso operatore può avere traffico di memoria molto diverso» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Lo stesso operatore può avere traffico di memoria molto diverso». [SRC-40-001]

Il punto didattico di «FLOP e movimento dei dati» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stesso contratto matematico con memoria e latenza misurate» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «FLOP e movimento dei dati» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «FLOP e movimento dei dati» portiamo l'output «stesso contratto matematico con memoria e latenza misurate»; non portiamo invece una conclusione oltre il caso locale.

## Tiling

Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score. [SRC-40-002]

Prima del nome tecnico fissiamo la situazione: consideriamo softmax stabile su due tile con massimo per riga. Da qui possiamo leggere la conseguenza dichiarata da «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score».

Nel contratto locale, l'input «tile di Q, K, V, dtype e device» entra, l'operazione «tiling, softmax online e ricomputazione» modifica il percorso e l'output «stesso contratto matematico con memoria e latenza misurate» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Tiling»; resta da controllare che una misura hardware dipende da shape, backend e precisione. La domanda locale è «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score».

L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare. Per «Tiling» il controllo cambia una sola premessa della frase «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score». [SRC-40-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score», non una promessa generale.

La prova di «Tiling» conserva input, operazione e output; poi esplicita quale parte di «Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Softmax online», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Softmax online

Massimo, denominatore e numeratore vengono aggiornati blocco per blocco. [SRC-40-003]

Per capire «Softmax online» partiamo da questo caso: un caso in cui una misura hardware dipende da shape, backend e precisione. Il caso rende osservabile il punto centrale: «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco».

La sezione usa l'input «tile di Q, K, V, dtype e device» come punto di partenza e l'output «stesso contratto matematico con memoria e latenza misurate» come traccia d'uscita. La trasformazione concreta è «tiling, softmax online e ricomputazione»; il caso non è completo se non dichiariamo anche che una misura hardware dipende da shape, backend e precisione. La condizione da isolare è «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco».

L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare. Per «Softmax online» il controllo cambia una sola premessa della frase «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco». [SRC-40-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Softmax online» conserviamo l'osservazione collegata a «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Softmax online» cambiamo una sola condizione vicina alla frase «Massimo, denominatore e numeratore vengono aggiornati blocco per blocco», teniamo fermo il resto e registriamo l'output «stesso contratto matematico con memoria e latenza misurate». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Backward e ricomputazione», riceve l'output «stesso contratto matematico con memoria e latenza misurate» come base, ma dovrà formulare e verificare la propria distinzione.

![Attention hardware-aware: pipeline](../../assets/chapters/40_hardware_attention/FLASH-01/candidate-v47.png)

La figura FLASH-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Tiling, softmax online e ricomputazione. L'input è tile di Q, K, V, dtype e device, l'output è stesso contratto matematico con memoria e latenza misurate; il vincolo da controllare è che una misura hardware dipende da shape, backend e precisione.

## Backward e ricomputazione

Salvare meno intermedi scambia memoria con compute aggiuntivo. [SRC-40-004]

Il caso minimo di «Backward e ricomputazione» si presenta così: un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Salvare meno intermedi scambia memoria con compute aggiuntivo».

Per ricostruire «Backward e ricomputazione» annotiamo l'input «tile di Q, K, V, dtype e device», poi l'operazione «tiling, softmax online e ricomputazione», infine l'output «stesso contratto matematico con memoria e latenza misurate». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Salvare meno intermedi scambia memoria con compute aggiuntivo».

L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare. Per «Backward e ricomputazione» il controllo cambia una sola premessa della frase «Salvare meno intermedi scambia memoria con compute aggiuntivo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Salvare meno intermedi scambia memoria con compute aggiuntivo». [SRC-40-004]

Il punto didattico di «Backward e ricomputazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «stesso contratto matematico con memoria e latenza misurate» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Backward e ricomputazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Backward e ricomputazione» portiamo l'output «stesso contratto matematico con memoria e latenza misurate»; non portiamo invece una conclusione oltre il caso locale.

## Backend

FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse. [SRC-40-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Da qui possiamo leggere la conseguenza dichiarata da «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse».

Nel contratto locale, l'input «tile di Q, K, V, dtype e device» entra, l'operazione «tiling, softmax online e ricomputazione» modifica il percorso e l'output «stesso contratto matematico con memoria e latenza misurate» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Backend»; resta da controllare che una misura hardware dipende da shape, backend e precisione. La domanda locale è «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse».

L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare. Per «Backend» il controllo cambia una sola premessa della frase «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse». [SRC-40-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse», non una promessa generale.

La prova di «Backend» conserva input, operazione e output; poi esplicita quale parte di «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «stesso contratto matematico con memoria e latenza misurate» come evidenza locale e conserva il vincolo che impedisce di leggere il futuro come domanda aperta.

## Il contratto in un caso piccolo: FLOP e movimento dei dati

Il caso intero parte dall'input «tile di Q, K, V, dtype e device», applica l'operazione «tiling, softmax online e ricomputazione» e osserva l'output «stesso contratto matematico con memoria e latenza misurate». Un esempio controllato: softmax stabile su due tile con massimo per riga. Lo schema compatto è:

$$
Attention = tiles(Q,K,V)
$$

È una notazione di interfaccia, non un'identità numerica completa. Il tiling cambia il movimento dei dati senza cambiare automaticamente il contratto matematico. [SRC-40-001]

![Attention hardware-aware: chart](../../assets/chapters/40_hardware_attention/FLASH-02/candidate-v47.png)

La figura FLASH-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Tiling, softmax online e ricomputazione. L'input è tile di Q, K, V, dtype e device, l'output è stesso contratto matematico con memoria e latenza misurate; il vincolo da controllare è che una misura hardware dipende da shape, backend e precisione.

## Dalla trasformazione al test: Tiling

Nel run Python rendiamo osservabile la frase «Lo stesso operatore può avere traffico di memoria molto diverso» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-40-001.txt` documenta il caso senza pretendere una misura generale.

## Il perimetro della conclusione: Backend

Il meccanismo di «Attention hardware-aware» non garantisce da solo che il sistema funzioni fuori dal caso guida. Una misura hardware dipende da shape, backend e precisione. Il limite osservato riguarda la frase «Lo stesso operatore può avere traffico di memoria molto diverso»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Una sintesi operativa: Attention hardware-aware

Il percorso ha tenuto insieme il calcolo dell'attention e il suo movimento di dati, l'operazione «tiling, softmax online e ricomputazione» e l'output «stesso contratto matematico con memoria e latenza misurate». Le sezioni «FLOP e movimento dei dati», «Tiling», «Backend» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: una misura hardware dipende da shape, backend e precisione. Il Capitolo 41, Linear attention, fast weights e delta rule, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: FLOP e movimento dei dati

1. Ricostruisci l'oggetto continuo a partire da «FLOP e movimento dei dati» e indica quale parte della frase «Lo stesso operatore può avere traffico di memoria molto diverso» entra nel caso.
2. Spiega quale trasformazione collega «FLOP e movimento dei dati» a «Backend» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: una misura hardware dipende da shape, backend e precisione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Backend

1. Disegna il percorso di «FLOP e movimento dei dati» indicando dati in ingresso e risultato.
2. Ripeti «Tiling» cambiando soltanto un valore dichiarato.
3. Trova in «Softmax online» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Backward e ricomputazione» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Backend» richiederebbe un benchmark ulteriore.

## Materiali, fonti e codice verificato: Attention hardware-aware

Per «Attention hardware-aware», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
