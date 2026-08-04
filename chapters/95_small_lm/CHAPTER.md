<!--
chapter_id: CH-P14-SMALL-LM
part_id: P14
order_key: 950
title: Costruire un piccolo language model
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 95. Costruire un piccolo language model

Il Capitolo 94, Percorso pratico dai fondamenti, ha lasciato disponibile un piccolo language model dalla stringa ai logits. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «embedding, decoder causale, cross-entropy e sampling» e verifichiamo che tokenizer, mask, target shift e sampling devono essere coerenti.

## Corpus e tokenizer

Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili. [SRC-95-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due sequenze di tre token diventano input e target spostati con shape coerenti. Da qui possiamo leggere la conseguenza dichiarata da «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili».

La sezione usa l'input «corpus, tokenizer, batch di sequenze e target» come punto di partenza e l'output «logits, loss, token generati e checkpoint» come traccia d'uscita. La trasformazione concreta è «embedding, decoder causale, cross-entropy e sampling»; il caso non è completo se non dichiariamo anche che tokenizer, mask, target shift e sampling devono essere coerenti. La condizione da isolare è «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Corpus e tokenizer» il controllo cambia una sola premessa della frase «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili». [SRC-95-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Corpus e tokenizer» conserviamo l'osservazione collegata a «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Corpus e tokenizer» conserva input, operazione e output; poi esplicita quale parte di «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Decoder Transformer», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Decoder Transformer

Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape. [SRC-95-002]

Per capire «Decoder Transformer» partiamo da questo caso: un batch [2, 4] attraversa embedding, mask causale, MLP e head dei logits. Il caso rende osservabile il punto centrale: «Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape».

Per ricostruire «Decoder Transformer» annotiamo l'input «corpus, tokenizer, batch di sequenze e target», poi l'operazione «embedding, decoder causale, cross-entropy e sampling», infine l'output «logits, loss, token generati e checkpoint». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Decoder Transformer» il controllo cambia una sola premessa della frase «Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape». [SRC-95-002]

Il punto didattico di «Decoder Transformer» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «logits, loss, token generati e checkpoint» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Decoder Transformer» cambiamo una sola condizione vicina alla frase «Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape», teniamo fermo il resto e registriamo l'output «logits, loss, token generati e checkpoint». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Training», riceve l'output «logits, loss, token generati e checkpoint» come base, ma dovrà formulare e verificare la propria distinzione.

## Training

AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU. [SRC-95-003]

Il caso minimo di «Training» si presenta così: un optimizer step confrontato con loss, seed e stato del checkpoint salvato. Non lo usiamo come decorazione: serve a rendere osservabile la frase «AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU».

Nel contratto locale, l'input «corpus, tokenizer, batch di sequenze e target» entra, l'operazione «embedding, decoder causale, cross-entropy e sampling» modifica il percorso e l'output «logits, loss, token generati e checkpoint» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Training»; resta da controllare che tokenizer, mask, target shift e sampling devono essere coerenti. La domanda locale è «AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Training» il controllo cambia una sola premessa della frase «AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU». [SRC-95-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU», non una promessa generale.

Il controllo minimo di «Training» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Training» portiamo l'output «logits, loss, token generati e checkpoint»; non portiamo invece una conclusione oltre il caso locale.

## Sampling

Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria. [SRC-95-004]

Prima del nome tecnico fissiamo la situazione: consideriamo lo stesso vettore di logits decodificato con greedy e top-k. Da qui possiamo leggere la conseguenza dichiarata da «Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria».

La sezione usa l'input «corpus, tokenizer, batch di sequenze e target» come punto di partenza e l'output «logits, loss, token generati e checkpoint» come traccia d'uscita. La trasformazione concreta è «embedding, decoder causale, cross-entropy e sampling»; il caso non è completo se non dichiariamo anche che tokenizer, mask, target shift e sampling devono essere coerenti. La condizione da isolare è «Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria». [SRC-95-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Sampling» conserviamo l'osservazione collegata a «Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Sampling» conserva input, operazione e output; poi esplicita quale parte di «Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Limiti», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Costruire un piccolo language model: matrix](../../assets/chapters/95_small_lm/LM-01/candidate-v48.png)

La figura LM-01 usa la famiglia matrix. Il diagramma segue il passaggio: Embedding, decoder causale, cross-entropy e sampling. L'input è corpus, tokenizer, batch di sequenze e target, l'output è logits, loss, token generati e checkpoint; il vincolo da controllare è che tokenizer, mask, target shift e sampling devono essere coerenti.

## Limiti

Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto. [SRC-95-001]

Per capire «Limiti» partiamo da questo caso: un confronto tra loss del piccolo modello e un claim che non può essere trasferito a modelli grandi. Il caso rende osservabile il punto centrale: «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto».

Per ricostruire «Limiti» annotiamo l'input «corpus, tokenizer, batch di sequenze e target», poi l'operazione «embedding, decoder causale, cross-entropy e sampling», infine l'output «logits, loss, token generati e checkpoint». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Limiti» il controllo cambia una sola premessa della frase «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto». [SRC-95-001]

Il punto didattico di «Limiti» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «logits, loss, token generati e checkpoint» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Limiti» cambiamo una sola condizione vicina alla frase «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto», teniamo fermo il resto e registriamo l'output «logits, loss, token generati e checkpoint». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il contratto in un caso piccolo: Corpus e tokenizer

Il caso intero parte dall'input «corpus, tokenizer, batch di sequenze e target», applica l'operazione «embedding, decoder causale, cross-entropy e sampling» e osserva l'output «logits, loss, token generati e checkpoint». Un esempio controllato: due sequenze, target spostato di un token e loss calcolata. La formula locale è:

$$
loss = cross_entropy(logits, targets)
$$

Un piccolo LM consente di osservare la relazione tra dati, logits e loss. [SRC-95-001]

![Costruire un piccolo language model: pipeline](../../assets/chapters/95_small_lm/LM-02/candidate-v48.png)

La figura LM-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Embedding, decoder causale, cross-entropy e sampling. L'input è corpus, tokenizer, batch di sequenze e target, l'output è logits, loss, token generati e checkpoint; il vincolo da controllare è che tokenizer, mask, target shift e sampling devono essere coerenti.

## Dalla trasformazione al test: Decoder Transformer

Nel run Python rendiamo osservabile la frase «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-95-001.txt` documenta il caso senza pretendere una misura generale.

## Il perimetro della conclusione: Limiti

Il meccanismo di «Costruire un piccolo language model» non garantisce da solo che il sistema funzioni fuori dal caso guida. Tokenizer, mask, target shift e sampling devono essere coerenti. Il limite osservato riguarda la frase «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Una sintesi operativa: Costruire un piccolo language model

Il percorso ha tenuto insieme un piccolo language model dalla stringa ai logits, l'operazione «embedding, decoder causale, cross-entropy e sampling» e l'output «logits, loss, token generati e checkpoint». Le sezioni «Corpus e tokenizer», «Decoder Transformer», «Limiti» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: tokenizer, mask, target shift e sampling devono essere coerenti. Il Capitolo 96, Progetto di produzione completo, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Corpus e tokenizer

1. Ricostruisci l'oggetto continuo a partire da «Corpus e tokenizer» e indica quale parte della frase «Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili» entra nel caso.
2. Spiega quale trasformazione collega «Corpus e tokenizer» a «Limiti» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: tokenizer, mask, target shift e sampling devono essere coerenti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Limiti

1. Disegna il percorso di «Corpus e tokenizer» indicando dati in ingresso e risultato.
2. Ripeti «Decoder Transformer» cambiando soltanto un valore dichiarato.
3. Trova in «Training» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Sampling» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Limiti» richiederebbe un benchmark ulteriore.

## Materiali, fonti e codice verificato: Costruire un piccolo language model

Per «Costruire un piccolo language model», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto protocollo, slice e decisione. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
