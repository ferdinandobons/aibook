<!--
chapter_id: CH-P05-AUTOREGRESSIVE
part_id: P05
order_key: 210
title: Modelli autoregressivi
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 21. Modelli autoregressivi

Finora abbiamo potuto descrivere la sequenza di token e la distribuzione del prossimo elemento. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 21 prendiamo l'input «un prefisso di tre token e una mask causale» e lo seguiamo fino all'output «logits, token scelto e traiettoria», dichiarando prima il contratto e poi il limite.

## Fattorizzare una sequenza

La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti. [SRC-21-001]

Per capire «Fattorizzare una sequenza» partiamo da questo caso: tre passi in cui lo stato precedente viene consumato prima di produrre il successivo. Il caso rende osservabile il punto centrale: «La chain rule scompone la probabilità con un ordine».

Nel contratto locale, l'input «un prefisso di tre token e una mask causale» entra, l'operazione «fattorizzazione, teacher forcing e decoding» modifica il percorso e l'output «logits, token scelto e traiettoria» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Fattorizzare una sequenza»; resta da controllare che nessuna posizione futura entra nella predizione causale. La domanda locale è «La chain rule scompone la probabilità con un ordine».

Il passaggio da seguire in «Fattorizzare una sequenza» è quello descritto dalla frase «La chain rule scompone la probabilità con un ordine»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Fattorizzare una sequenza» il controllo cambia una sola premessa della frase «La chain rule scompone la probabilità con un ordine» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «La chain rule scompone la probabilità con un ordine». [SRC-21-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Ogni fattore condiziona sugli elementi precedenti. Il piccolo risultato resta un'illustrazione di «La chain rule scompone la probabilità con un ordine», non una promessa generale.

Per verificare «Fattorizzare una sequenza» cambiamo una sola condizione vicina alla frase «La chain rule scompone la probabilità con un ordine», teniamo fermo il resto e registriamo l'output «logits, token scelto e traiettoria». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Teacher forcing», riceve l'output «logits, token scelto e traiettoria» come base, ma dovrà formulare e verificare la propria distinzione.

## Teacher forcing

Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output. [SRC-21-002]

Il caso minimo di «Teacher forcing» si presenta così: un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Durante il training il modello riceve il prefisso reale e predice il passo successivo».

La sezione usa l'input «un prefisso di tre token e una mask causale» come punto di partenza e l'output «logits, token scelto e traiettoria» come traccia d'uscita. La trasformazione concreta è «fattorizzazione, teacher forcing e decoding»; il caso non è completo se non dichiariamo anche che nessuna posizione futura entra nella predizione causale. La condizione da isolare è «Durante il training il modello riceve il prefisso reale e predice il passo successivo».

L'adattamento cambia il segnale presentato al modello e la porzione di output su cui si calcola la loss. Dati, mask, riferimenti e valutazione separata determinano quale comportamento viene effettivamente rinforzato. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Durante il training il modello riceve il prefisso reale e predice il passo successivo». [SRC-21-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Teacher forcing» conserviamo l'osservazione collegata a «Durante il training il modello riceve il prefisso reale e predice il passo successivo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Teacher forcing» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Teacher forcing» portiamo l'output «logits, token scelto e traiettoria»; non portiamo invece una conclusione oltre il caso locale.

![Modelli autoregressivi: timeline](../../assets/chapters/21_autoregressive/AUTOREGR-01/candidate-v49.png)

La figura AUTOREGR-01 usa la famiglia timeline. Il diagramma segue il passaggio: Fattorizzazione, teacher forcing e decoding. L'input è un prefisso di tre token e una mask causale, l'output è logits, token scelto e traiettoria; il vincolo da controllare è che nessuna posizione futura entra nella predizione causale.

## Maschera causale

La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida. [SRC-21-003]

Prima del nome tecnico fissiamo la situazione: consideriamo una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile. Da qui possiamo leggere la conseguenza dichiarata da «La causal mask impedisce a una posizione di usare target futuri».

Per ricostruire «Maschera causale» annotiamo l'input «un prefisso di tre token e una mask causale», poi l'operazione «fattorizzazione, teacher forcing e decoding», infine l'output «logits, token scelto e traiettoria». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «La causal mask impedisce a una posizione di usare target futuri».

Interpretare significa dichiarare quale oggetto viene analizzato e quale intervento o misura lo collega al comportamento. Informazione decodificabile, attribuzione e causalità non sono lo stesso risultato. Per «Maschera causale» il controllo cambia una sola premessa della frase «La causal mask impedisce a una posizione di usare target futuri» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «La causal mask impedisce a una posizione di usare target futuri». [SRC-21-003]

Il punto didattico di «Maschera causale» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «logits, token scelto e traiettoria» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Maschera causale» conserva input, operazione e output; poi esplicita quale parte di «La causal mask impedisce a una posizione di usare target futuri» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Sampling e accumulo degli errori», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Sampling e accumulo degli errori

Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training. [SRC-21-004]

Per capire «Sampling e accumulo degli errori» partiamo da questo caso: un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Il caso rende osservabile il punto centrale: «Ogni scelta modifica il contesto successivo».

Nel contratto locale, l'input «un prefisso di tre token e una mask causale» entra, l'operazione «fattorizzazione, teacher forcing e decoding» modifica il percorso e l'output «logits, token scelto e traiettoria» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Sampling e accumulo degli errori»; resta da controllare che nessuna posizione futura entra nella predizione causale. La domanda locale è «Ogni scelta modifica il contesto successivo».

L'inference trasforma logits e richieste in una traiettoria sotto vincoli di memoria e tempo. Decoding, cache, batching e scheduling modificano il servizio osservato e richiedono metriche oltre alla qualità dell'output. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Ogni scelta modifica il contesto successivo». [SRC-21-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training. Il piccolo risultato resta un'illustrazione di «Ogni scelta modifica il contesto successivo», non una promessa generale.

Per verificare «Sampling e accumulo degli errori» cambiamo una sola condizione vicina alla frase «Ogni scelta modifica il contesto successivo», teniamo fermo il resto e registriamo l'output «logits, token scelto e traiettoria». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Immagini, audio e token discreti», riceve l'output «logits, token scelto e traiettoria» come base, ma dovrà formulare e verificare la propria distinzione.

## Immagini, audio e token discreti

L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti. [SRC-21-001]

Il caso minimo di «Immagini, audio e token discreti» si presenta così: un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Non lo usiamo come decorazione: serve a rendere osservabile la frase «L'autoregressione non è limitata al testo».

La sezione usa l'input «un prefisso di tre token e una mask causale» come punto di partenza e l'output «logits, token scelto e traiettoria» come traccia d'uscita. La trasformazione concreta è «fattorizzazione, teacher forcing e decoding»; il caso non è completo se non dichiariamo anche che nessuna posizione futura entra nella predizione causale. La condizione da isolare è «L'autoregressione non è limitata al testo».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Immagini, audio e token discreti» il controllo cambia una sola premessa della frase «L'autoregressione non è limitata al testo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «L'autoregressione non è limitata al testo». [SRC-21-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Immagini, audio e token discreti» conserviamo l'osservazione collegata a «L'autoregressione non è limitata al testo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Immagini, audio e token discreti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Un caso dall'input all'output: Fattorizzare una sequenza

Il caso intero parte dall'input «un prefisso di tre token e una mask causale», applica l'operazione «fattorizzazione, teacher forcing e decoding» e osserva l'output «logits, token scelto e traiettoria». Un esempio controllato: due passi di teacher forcing confrontati con un passo campionato. La formula locale è:

$$
p(x_{1:T})=\prod_t p(x_t|x_{<t})
$$

La chain rule rende l'autoregressione una sequenza di predizioni condizionate. [SRC-21-001]

![Modelli autoregressivi: pipeline](../../assets/chapters/21_autoregressive/AUTOREGR-02/candidate-v49.png)

La figura AUTOREGR-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Fattorizzazione, teacher forcing e decoding. L'input è un prefisso di tre token e una mask causale, l'output è logits, token scelto e traiettoria; il vincolo da controllare è che nessuna posizione futura entra nella predizione causale.

## Dal meccanismo alla prova locale: Teacher forcing

Nel run Python rendiamo osservabile la frase «La chain rule scompone la probabilità con un ordine» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-21-001.txt` documenta il caso senza pretendere una misura generale.

## Dove il risultato si ferma: Immagini, audio e token discreti

Il meccanismo di «Modelli autoregressivi» non garantisce da solo che il sistema funzioni fuori dal caso guida. Nessuna posizione futura entra nella predizione causale. Il limite osservato riguarda la frase «La chain rule scompone la probabilità con un ordine»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Che cosa portiamo avanti: Modelli autoregressivi

Il percorso ha tenuto insieme la sequenza di token e la distribuzione del prossimo elemento, l'operazione «fattorizzazione, teacher forcing e decoding» e l'output «logits, token scelto e traiettoria». Le sezioni «Fattorizzare una sequenza», «Teacher forcing», «Immagini, audio e token discreti» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: nessuna posizione futura entra nella predizione causale. Il Capitolo 22, Variational Autoencoder e latent discreti, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Fattorizzare una sequenza

1. Ricostruisci l'oggetto continuo a partire da «Fattorizzare una sequenza» e indica quale parte della frase «La chain rule scompone la probabilità con un ordine» entra nel caso.
2. Spiega quale trasformazione collega «Fattorizzare una sequenza» a «Immagini, audio e token discreti» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: nessuna posizione futura entra nella predizione causale.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «L'autoregressione non è limitata al testo» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Immagini, audio e token discreti

1. Racconta «Fattorizzare una sequenza» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Teacher forcing» mantenendo il resto del setup invariato.
3. Per «Maschera causale», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Sampling e accumulo degli errori» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Immagini, audio e token discreti» senza confondere livelli diversi.

## Fonti, codice e materiali: Modelli autoregressivi

Per «Modelli autoregressivi», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
