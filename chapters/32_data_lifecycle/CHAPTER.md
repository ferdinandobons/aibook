<!--
chapter_id: CH-P07-DATA-LIFECYCLE
part_id: P07
order_key: 320
title: Il ciclo di vita dei dati
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 32. Il ciclo di vita dei dati

Il risultato precedente non è ancora una soluzione completa. Partiamo da un record di dataset dalla sorgente al manifest e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «record ammesso, conteggi e manifest» isoliamo il passaggio «parsing, filtro, deduplicazione e tokenizzazione» e ne misuriamo il limite prima di passare a Dataset mixture, curriculum e dati sintetici.

## Sorgenti e provenienza

Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard. [SRC-32-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Da qui possiamo leggere la conseguenza dichiarata da «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard».

La sezione usa l'input «testo grezzo, metadati, split e digest» come punto di partenza e l'output «record ammesso, conteggi e manifest» come traccia d'uscita. La trasformazione concreta è «parsing, filtro, deduplicazione e tokenizzazione»; il caso non è completo se non dichiariamo anche che ogni trasformazione deve restare ricostruibile e ordinata. La condizione da isolare è «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard». [SRC-32-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Sorgenti e provenienza» conserviamo l'osservazione collegata a «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Sorgenti e provenienza» conserva input, operazione e output; poi esplicita quale parte di «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Parsing e normalizzazione», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Parsing e normalizzazione

Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate. [SRC-32-002]

Per capire «Parsing e normalizzazione» partiamo da questo caso: due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Il caso rende osservabile il punto centrale: «Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate».

Per ricostruire «Parsing e normalizzazione» annotiamo l'input «testo grezzo, metadati, split e digest», poi l'operazione «parsing, filtro, deduplicazione e tokenizzazione», infine l'output «record ammesso, conteggi e manifest». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate».

Il punto operativo è la scala del segnale: inizializzazione, normalizzazione, residual e regolarizzazione intervengono in momenti diversi e non sono sostituti intercambiabili. Shape compatibili e curve osservate servono a controllare il percorso reale. Per «Parsing e normalizzazione» il controllo cambia una sola premessa della frase «Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate». [SRC-32-002]

Il punto didattico di «Parsing e normalizzazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «record ammesso, conteggi e manifest» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Parsing e normalizzazione» cambiamo una sola condizione vicina alla frase «Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate», teniamo fermo il resto e registriamo l'output «record ammesso, conteggi e manifest». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Filtri», riceve l'output «record ammesso, conteggi e manifest» come base, ma dovrà formulare e verificare la propria distinzione.

## Filtri

Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo. [SRC-32-003]

Il caso minimo di «Filtri» si presenta così: due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo».

Nel contratto locale, l'input «testo grezzo, metadati, split e digest» entra, l'operazione «parsing, filtro, deduplicazione e tokenizzazione» modifica il percorso e l'output «record ammesso, conteggi e manifest» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Filtri»; resta da controllare che ogni trasformazione deve restare ricostruibile e ordinata. La domanda locale è «Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. Per «Filtri» il controllo cambia una sola premessa della frase «Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo». [SRC-32-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo», non una promessa generale.

Il controllo minimo di «Filtri» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. Da «Filtri» portiamo l'output «record ammesso, conteggi e manifest»; non portiamo invece una conclusione oltre il caso locale.

## Deduplicazione e contaminazione

Hash esatti e similarità approssimata rilevano forme differenti di duplicazione. I benchmark richiedono controlli separati. [SRC-32-004]

Prima del nome tecnico fissiamo la situazione: consideriamo due record simili che vengono confrontati con hash esatto e con una regola distinta per la similarità approssimata. Da qui possiamo leggere la conseguenza dichiarata da «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione».

La sezione usa l'input «testo grezzo, metadati, split e digest» come punto di partenza e l'output «record ammesso, conteggi e manifest» come traccia d'uscita. La trasformazione concreta è «parsing, filtro, deduplicazione e tokenizzazione»; il caso non è completo se non dichiariamo anche che ogni trasformazione deve restare ricostruibile e ordinata. La condizione da isolare è «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. Per «Deduplicazione e contaminazione» il controllo cambia una sola premessa della frase «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione». [SRC-32-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Deduplicazione e contaminazione» conserviamo l'osservazione collegata a «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Deduplicazione e contaminazione» conserva input, operazione e output; poi esplicita quale parte di «Hash esatti e similarità approssimata rilevano forme differenti di duplicazione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Split, tokenizzazione e manifest», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Il ciclo di vita dei dati: manifest](../../assets/chapters/32_data_lifecycle/DATA-01/candidate-v47.png)

La figura DATA-01 usa la famiglia manifest. Il diagramma segue il passaggio: Parsing, filtro, deduplicazione e tokenizzazione. L'input è testo grezzo, metadati, split e digest, l'output è record ammesso, conteggi e manifest; il vincolo da controllare è che ogni trasformazione deve restare ricostruibile e ordinata.

## Split, tokenizzazione e manifest

Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training. [SRC-32-001]

Per capire «Split, tokenizzazione e manifest» partiamo da questo caso: un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Il caso rende osservabile il punto centrale: «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training».

Per ricostruire «Split, tokenizzazione e manifest» annotiamo l'input «testo grezzo, metadati, split e digest», poi l'operazione «parsing, filtro, deduplicazione e tokenizzazione», infine l'output «record ammesso, conteggi e manifest». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training».

Prima del modello, il testo diventa una sequenza di unità con una convenzione precisa. Encoding, tokenizer, token speciali, mask e packing modificano l'input effettivo e quindi fanno parte del contratto del checkpoint. Per «Split, tokenizzazione e manifest» il controllo cambia una sola premessa della frase «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training». [SRC-32-001]

Il punto didattico di «Split, tokenizzazione e manifest» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «record ammesso, conteggi e manifest» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Split, tokenizzazione e manifest» cambiamo una sola condizione vicina alla frase «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training», teniamo fermo il resto e registriamo l'output «record ammesso, conteggi e manifest». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Un esempio con controllo negativo: Sorgenti e provenienza

Il caso intero parte dall'input «testo grezzo, metadati, split e digest», applica l'operazione «parsing, filtro, deduplicazione e tokenizzazione» e osserva l'output «record ammesso, conteggi e manifest». Un esempio controllato: due record, uno duplicato, con digest prima e dopo il filtro. La formula locale è:

$$
manifest = hash(raw, transform, tokenizer, split)
$$

Il digest diventa utile soltanto se le trasformazioni incluse sono dichiarate. [SRC-32-001]

![Il ciclo di vita dei dati: funnel](../../assets/chapters/32_data_lifecycle/DATA-02/candidate-v47.png)

La figura DATA-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Parsing, filtro, deduplicazione e tokenizzazione. L'input è testo grezzo, metadati, split e digest, l'output è record ammesso, conteggi e manifest; il vincolo da controllare è che ogni trasformazione deve restare ricostruibile e ordinata.

## Dalla formula al run: Parsing e normalizzazione

Lo snippet locale mette in esecuzione questo caso: due record, uno duplicato, con digest prima e dopo il filtro. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-32-001.txt`, come evidenza locale e non come benchmark di produzione.

## Limiti, varianti e nuove misure: Split, tokenizzazione e manifest

Il caso di «Il ciclo di vita dei dati» non certifica un servizio completo. Ogni trasformazione deve restare ricostruibile e ordinata. La domanda successiva è se «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training» regga quando cambiano dati, scala, hardware o criteri di decisione.

## L'invariante da conservare: Il ciclo di vita dei dati

Il filo della lezione va dall'input «testo grezzo, metadati, split e digest» all'output «record ammesso, conteggi e manifest». Nei passaggi «Sorgenti e provenienza», «Parsing e normalizzazione», «Split, tokenizzazione e manifest» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: ogni trasformazione deve restare ricostruibile e ordinata. Il Capitolo 33, Dataset mixture, curriculum e dati sintetici, può partire da questo output e dichiarare la propria domanda.

### Prova di comprensione: Sorgenti e provenienza

1. Ricostruisci l'oggetto continuo a partire da «Sorgenti e provenienza» e indica quale parte della frase «Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard» entra nel caso.
2. Spiega quale trasformazione collega «Sorgenti e provenienza» a «Split, tokenizzazione e manifest» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: ogni trasformazione deve restare ricostruibile e ordinata.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi con casi limite: Split, tokenizzazione e manifest

1. Racconta «Sorgenti e provenienza» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Parsing e normalizzazione» mantenendo il resto del setup invariato.
3. Per «Filtri», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Deduplicazione e contaminazione» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Split, tokenizzazione e manifest» senza confondere livelli diversi.

## Fonti primarie e artefatti del capitolo: Il ciclo di vita dei dati

Per ricontrollare «Il ciclo di vita dei dati», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il legame tra dati esposti e risultato oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a popolazione, manifest e stato del run.
