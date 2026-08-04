<!--
chapter_id: CH-P14-REPLICATION
part_id: P14
order_key: 970
title: Riprodurre e leggere un paper
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 97. Riprodurre e leggere un paper

Il risultato precedente non è ancora una soluzione completa. Partiamo da un claim di paper e il protocollo necessario per riprodurlo e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «risultato replicato o differenza spiegata» isoliamo il passaggio «setup indipendente, run, confronto e analisi delle divergenze» e ne misuriamo il limite prima di passare a Osservatorio della frontiera.

## Domanda e claim

Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti. [SRC-97-001]

Il caso minimo di «Domanda e claim» si presenta così: due run con split uguale ma seed diversi producono una differenza che va registrata. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti».

Per ricostruire «Domanda e claim» annotiamo l'input «paper, codice, dati, seed, hardware e metriche», poi l'operazione «setup indipendente, run, confronto e analisi delle divergenze», infine l'output «risultato replicato o differenza spiegata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. La scheda di prova conserva fonte, data, configurazione e decisione, permettendo di distinguere novità editoriale da evidenza ripetuta. La verifica resta ancorata a «Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti». [SRC-97-001]

Il punto didattico di «Domanda e claim» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato replicato o differenza spiegata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Domanda e claim» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Domanda e claim» portiamo l'output «risultato replicato o differenza spiegata»; non portiamo invece una conclusione oltre il caso locale.

## Artefatti

Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione. [SRC-97-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un manifest con commit, dataset, seed, hardware, dipendenze e checksum. Da qui possiamo leggere la conseguenza dichiarata da «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione».

Nel contratto locale, l'input «paper, codice, dati, seed, hardware e metriche» entra, l'operazione «setup indipendente, run, confronto e analisi delle divergenze» modifica il percorso e l'output «risultato replicato o differenza spiegata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Artefatti»; resta da controllare che una replica richiede stesso claim e confini dichiarati, non solo stesso codice. La domanda locale è «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Artefatti» il controllo cambia una sola premessa della frase «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione». [SRC-97-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione», non una promessa generale.

La prova di «Artefatti» conserva input, operazione e output; poi esplicita quale parte di «Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Replica», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Replica

Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie. [SRC-97-003]

Per capire «Replica» partiamo da questo caso: un setup indipendente che ripete il protocollo senza riusare l'output originale. Il caso rende osservabile il punto centrale: «Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie».

La sezione usa l'input «paper, codice, dati, seed, hardware e metriche» come punto di partenza e l'output «risultato replicato o differenza spiegata» come traccia d'uscita. La trasformazione concreta è «setup indipendente, run, confronto e analisi delle divergenze»; il caso non è completo se non dichiariamo anche che una replica richiede stesso claim e confini dichiarati, non solo stesso codice. La condizione da isolare è «Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. La scheda di prova conserva fonte, data, configurazione e decisione, permettendo di distinguere novità editoriale da evidenza ripetuta. La verifica resta ancorata a «Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie». [SRC-97-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Replica» conserviamo l'osservazione collegata a «Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Replica» cambiamo una sola condizione vicina alla frase «Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie», teniamo fermo il resto e registriamo l'output «risultato replicato o differenza spiegata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Divergenze», riceve l'output «risultato replicato o differenza spiegata» come base, ma dovrà formulare e verificare la propria distinzione.

![Riprodurre e leggere un paper: checklist](../../assets/chapters/97_replication/REPLICATIO-01/candidate-v48.png)

La figura REPLICATIO-01 usa la famiglia checklist. Il diagramma segue il passaggio: Setup indipendente, run, confronto e analisi delle divergenze. L'input è paper, codice, dati, seed, hardware e metriche, l'output è risultato replicato o differenza spiegata; il vincolo da controllare è che una replica richiede stesso claim e confini dichiarati, non solo stesso codice.

## Divergenze

Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste. [SRC-97-004]

Il caso minimo di «Divergenze» si presenta così: una tabella che separa divergenze di seed, preprocessing, hardware e implementazione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste».

Per ricostruire «Divergenze» annotiamo l'input «paper, codice, dati, seed, hardware e metriche», poi l'operazione «setup indipendente, run, confronto e analisi delle divergenze», infine l'output «risultato replicato o differenza spiegata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Divergenze» il controllo cambia una sola premessa della frase «Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste». [SRC-97-004]

Il punto didattico di «Divergenze» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «risultato replicato o differenza spiegata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Divergenze» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Divergenze» portiamo l'output «risultato replicato o differenza spiegata»; non portiamo invece una conclusione oltre il caso locale.

## Conclusione sostenibile

Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale. [SRC-97-001]

Prima del nome tecnico fissiamo la situazione: consideriamo una conclusione limitata al claim e all'intervallo realmente eseguiti. Da qui possiamo leggere la conseguenza dichiarata da «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale».

Nel contratto locale, l'input «paper, codice, dati, seed, hardware e metriche» entra, l'operazione «setup indipendente, run, confronto e analisi delle divergenze» modifica il percorso e l'output «risultato replicato o differenza spiegata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Conclusione sostenibile»; resta da controllare che una replica richiede stesso claim e confini dichiarati, non solo stesso codice. La domanda locale è «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Conclusione sostenibile» il controllo cambia una sola premessa della frase «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale». [SRC-97-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale», non una promessa generale.

La prova di «Conclusione sostenibile» conserva input, operazione e output; poi esplicita quale parte di «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «risultato replicato o differenza spiegata» come evidenza locale e conserva il confine tra evidenza e interpretazione come domanda aperta.

## La definizione messa alla prova: Domanda e claim

Il caso intero parte dall'input «paper, codice, dati, seed, hardware e metriche», applica l'operazione «setup indipendente, run, confronto e analisi delle divergenze» e osserva l'output «risultato replicato o differenza spiegata». Un esempio controllato: due run con seed diversi e divergenza registrata. La formula locale è:

$$
replica = run(protocol, independent_setup)
$$

La replica verifica quanto il risultato dipenda dal setup originale. [SRC-97-001]

![Riprodurre e leggere un paper: compare](../../assets/chapters/97_replication/REPLICATIO-02/candidate-v48.png)

La figura REPLICATIO-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Setup indipendente, run, confronto e analisi delle divergenze. L'input è paper, codice, dati, seed, hardware e metriche, l'output è risultato replicato o differenza spiegata; il vincolo da controllare è che una replica richiede stesso claim e confini dichiarati, non solo stesso codice.

## Un esperimento piccolo ma leggibile: Artefatti

Lo snippet locale mette in esecuzione questo caso: due run con seed diversi e divergenza registrata. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-97-001.txt`, come evidenza locale e non come benchmark di produzione.

## Il confine del caso guida: Conclusione sostenibile

Il caso di «Riprodurre e leggere un paper» non certifica un servizio completo. Una replica richiede stesso claim e confini dichiarati, non solo stesso codice. La domanda successiva è se «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Il contratto che rimane: Riprodurre e leggere un paper

Il filo della lezione va dall'input «paper, codice, dati, seed, hardware e metriche» all'output «risultato replicato o differenza spiegata». Nei passaggi «Domanda e claim», «Artefatti», «Conclusione sostenibile» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: una replica richiede stesso claim e confini dichiarati, non solo stesso codice. Il Capitolo 98, Osservatorio della frontiera, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Domanda e claim

1. Ricostruisci l'oggetto continuo a partire da «Domanda e claim» e indica quale parte della frase «Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti» entra nel caso.
2. Spiega quale trasformazione collega «Domanda e claim» a «Conclusione sostenibile» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: una replica richiede stesso claim e confini dichiarati, non solo stesso codice.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Conclusione sostenibile

1. Ricostruisci input e output di «Domanda e claim» usando un esempio di tre righe.
2. Modifica una sola variabile in «Artefatti» e anticipa l'invariante che dovrebbe restare.
3. Metti «Replica» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Divergenze».
5. Formula per «Conclusione sostenibile» una domanda che separi meccanismo e qualità del sistema.

## Riferimenti e prove riproducibili: Riprodurre e leggere un paper

Per ricontrollare «Riprodurre e leggere un paper», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il confine tra evidenza e interpretazione oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
