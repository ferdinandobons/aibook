<!--
chapter_id: CH-P07-DATA-MIXTURE
part_id: P07
order_key: 330
title: Dataset mixture, curriculum e dati sintetici
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 33. Dataset mixture, curriculum e dati sintetici

La richiesta «Il pacco non è arrivato» resta il caso guida. In questo capitolo la usiamo per distinguere la miscela effettiva di sorgenti durante il training, trasformazione e risultato, senza nascondere i dettagli tecnici.

## Peso effettivo delle sorgenti

Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni. [SRC-33-001]

Per capire «Peso effettivo delle sorgenti» partiamo da questo caso: due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Il caso rende osservabile il punto centrale: «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni».

Nel contratto locale, l'input «pesi, temperatura, curriculum e conteggio dei token» entra, l'operazione «campionamento, ripesatura e generazione controllata» modifica il percorso e l'output «probabilità effettive e mix osservato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Peso effettivo delle sorgenti»; resta da controllare che peso nominale e esposizione effettiva non sono la stessa misura. La domanda locale è «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni». [SRC-33-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni», non una promessa generale.

Per verificare «Peso effettivo delle sorgenti» cambiamo una sola condizione vicina alla frase «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni», teniamo fermo il resto e registriamo l'output «probabilità effettive e mix osservato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Temperature sampling», riceve l'output «probabilità effettive e mix osservato» come base, ma dovrà formulare e verificare la propria distinzione.

## Temperature sampling

Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli. [SRC-33-002]

Il caso minimo di «Temperature sampling» si presenta così: un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli».

La sezione usa l'input «pesi, temperatura, curriculum e conteggio dei token» come punto di partenza e l'output «probabilità effettive e mix osservato» come traccia d'uscita. La trasformazione concreta è «campionamento, ripesatura e generazione controllata»; il caso non è completo se non dichiariamo anche che peso nominale e esposizione effettiva non sono la stessa misura. La condizione da isolare è «Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli».

La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli». [SRC-33-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Temperature sampling» conserviamo l'osservazione collegata a «Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Temperature sampling» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. Da «Temperature sampling» portiamo l'output «probabilità effettive e mix osservato»; non portiamo invece una conclusione oltre il caso locale.

![Dataset mixture, curriculum e dati sintetici: compare](../../assets/chapters/33_data_mixture/MIX-01/candidate-v47.png)

La figura MIX-01 usa la famiglia compare. Il diagramma segue il passaggio: Campionamento, ripesatura e generazione controllata. L'input è pesi, temperatura, curriculum e conteggio dei token, l'output è probabilità effettive e mix osservato; il vincolo da controllare è che peso nominale e esposizione effettiva non sono la stessa misura.

## Mixture ottimizzata

Pesi appresi con proxy model dipendono da domini, validation e budget. [SRC-33-003]

Prima del nome tecnico fissiamo la situazione: consideriamo due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Da qui possiamo leggere la conseguenza dichiarata da «Pesi appresi con proxy model dipendono da domini, validation e budget».

Per ricostruire «Mixture ottimizzata» annotiamo l'input «pesi, temperatura, curriculum e conteggio dei token», poi l'operazione «campionamento, ripesatura e generazione controllata», infine l'output «probabilità effettive e mix osservato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Pesi appresi con proxy model dipendono da domini, validation e budget».

La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Pesi appresi con proxy model dipendono da domini, validation e budget». [SRC-33-003]

Il punto didattico di «Mixture ottimizzata» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «probabilità effettive e mix osservato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Mixture ottimizzata» conserva input, operazione e output; poi esplicita quale parte di «Pesi appresi con proxy model dipendono da domini, validation e budget» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Curriculum», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Curriculum

Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione. [SRC-33-004]

Per capire «Curriculum» partiamo da questo caso: due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Il caso rende osservabile il punto centrale: «Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione».

Nel contratto locale, l'input «pesi, temperatura, curriculum e conteggio dei token» entra, l'operazione «campionamento, ripesatura e generazione controllata» modifica il percorso e l'output «probabilità effettive e mix osservato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Curriculum»; resta da controllare che peso nominale e esposizione effettiva non sono la stessa misura. La domanda locale è «Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione».

La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione». [SRC-33-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione», non una promessa generale.

Per verificare «Curriculum» cambiamo una sola condizione vicina alla frase «Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione», teniamo fermo il resto e registriamo l'output «probabilità effettive e mix osservato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Dati sintetici», riceve l'output «probabilità effettive e mix osservato» come base, ma dovrà formulare e verificare la propria distinzione.

## Dati sintetici

Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato. [SRC-33-001]

Il caso minimo di «Dati sintetici» si presenta così: due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato».

La sezione usa l'input «pesi, temperatura, curriculum e conteggio dei token» come punto di partenza e l'output «probabilità effettive e mix osservato» come traccia d'uscita. La trasformazione concreta è «campionamento, ripesatura e generazione controllata»; il caso non è completo se non dichiariamo anche che peso nominale e esposizione effettiva non sono la stessa misura. La condizione da isolare è «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato».

La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata. La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record. La verifica resta ancorata a «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato». [SRC-33-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Dati sintetici» conserviamo l'osservazione collegata a «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Dati sintetici» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di popolazione, manifest e stato del run. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## La definizione messa alla prova: Peso effettivo delle sorgenti

Il caso intero parte dall'input «pesi, temperatura, curriculum e conteggio dei token», applica l'operazione «campionamento, ripesatura e generazione controllata» e osserva l'output «probabilità effettive e mix osservato». Un esempio controllato: tre sorgenti ripesate con temperatura e conteggio finale. La formula locale è:

$$
p_i = w_i^tau / sum_j w_j^tau
$$

Il campionamento modifica le esposizioni effettive, non la dimensione grezza delle sorgenti. [SRC-33-001]

![Dataset mixture, curriculum e dati sintetici: chart](../../assets/chapters/33_data_mixture/MIX-02/candidate-v47.png)

La figura MIX-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Campionamento, ripesatura e generazione controllata. L'input è pesi, temperatura, curriculum e conteggio dei token, l'output è probabilità effettive e mix osservato; il vincolo da controllare è che peso nominale e esposizione effettiva non sono la stessa misura.

## Un esperimento piccolo ma leggibile: Temperature sampling

Il file `code/snip_33_contract.py` collega il contratto del capitolo alla frase «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-33-001.txt` conserva il risultato ripetibile del caso locale.

## Il confine del caso guida: Dati sintetici

Il meccanismo di «Dataset mixture, curriculum e dati sintetici» resta legato al contratto locale. Peso nominale e esposizione effettiva non sono la stessa misura. Prima di generalizzare la frase «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il contratto che rimane: Dataset mixture, curriculum e dati sintetici

Abbiamo seguito la miscela effettiva di sorgenti durante il training, partendo dall'input «pesi, temperatura, curriculum e conteggio dei token» e arrivando all'output «probabilità effettive e mix osservato». Le sezioni «Peso effettivo delle sorgenti», «Temperature sampling», «Dati sintetici» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: peso nominale e esposizione effettiva non sono la stessa misura. Il Capitolo 34, Scaling law e progettazione del modello, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Peso effettivo delle sorgenti

1. Ricostruisci l'oggetto continuo a partire da «Peso effettivo delle sorgenti» e indica quale parte della frase «Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni» entra nel caso.
2. Spiega quale trasformazione collega «Peso effettivo delle sorgenti» a «Dati sintetici» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: peso nominale e esposizione effettiva non sono la stessa misura.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Dati sintetici

1. Racconta «Peso effettivo delle sorgenti» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Temperature sampling» mantenendo il resto del setup invariato.
3. Per «Mixture ottimizzata», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Curriculum» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Dati sintetici» senza confondere livelli diversi.

## Riferimenti e prove riproducibili: Dataset mixture, curriculum e dati sintetici

Il dossier di «Dataset mixture, curriculum e dati sintetici» in `FONTI_PRIMARIE.md` separa definizioni, risultati e conteggi, split e trasformazioni registrate; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a popolazione, manifest e stato del run.
