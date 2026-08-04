<!--
chapter_id: CH-P14-FOUNDATIONS-LAB
part_id: P14
order_key: 940
title: Percorso pratico dai fondamenti
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 94. Percorso pratico dai fondamenti

Una frase plausibile non basta a spiegare percorso pratico dai fondamenti. L'oggetto è un esperimento didattico con ambiente e artefatti dichiarati; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Ambiente riproducibile

Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti. [SRC-94-001]

Il caso minimo di «Ambiente riproducibile» si presenta così: la stessa configurazione seed=7, split=fixed e dtype=float32 produce un digest ripetibile. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti».

Per ricostruire «Ambiente riproducibile» annotiamo l'input «seed, dataset piccolo, config, codice e versione», poi l'operazione «run, test, valutazione e report», infine l'output «loss, metriche, manifest e limite». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Ambiente riproducibile» il controllo cambia una sola premessa della frase «Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti». [SRC-94-001]

Il punto didattico di «Ambiente riproducibile» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss, metriche, manifest e limite» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Ambiente riproducibile» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Ambiente riproducibile» portiamo l'output «loss, metriche, manifest e limite»; non portiamo invece una conclusione oltre il caso locale.

## Dataset piccolo

Un dataset controllabile permette di vedere preprocessing, split, batch e leakage. [SRC-94-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un dataset di quattro record con split e checksum conservati nel manifest. Da qui possiamo leggere la conseguenza dichiarata da «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage».

Nel contratto locale, l'input «seed, dataset piccolo, config, codice e versione» entra, l'operazione «run, test, valutazione e report» modifica il percorso e l'output «loss, metriche, manifest e limite» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Dataset piccolo»; resta da controllare che un run locale non equivale a una prova generale. La domanda locale è «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Dataset piccolo» il controllo cambia una sola premessa della frase «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage». [SRC-94-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage», non una promessa generale.

La prova di «Dataset piccolo» conserva input, operazione e output; poi esplicita quale parte di «Un dataset controllabile permette di vedere preprocessing, split, batch e leakage» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Modello e loss», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Modello e loss

Una baseline lineare precede la rete. Shape, logits e loss vengono verificati con test. [SRC-94-003]

Per capire «Modello e loss» partiamo da questo caso: un forward che produce loss su target dichiarati e un controllo negativo di shape. Il caso rende osservabile il punto centrale: «Una baseline lineare precede la rete».

La sezione usa l'input «seed, dataset piccolo, config, codice e versione» come punto di partenza e l'output «loss, metriche, manifest e limite» come traccia d'uscita. La trasformazione concreta è «run, test, valutazione e report»; il caso non è completo se non dichiariamo anche che un run locale non equivale a una prova generale. La condizione da isolare è «Una baseline lineare precede la rete».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Modello e loss» il controllo cambia una sola premessa della frase «Una baseline lineare precede la rete» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una baseline lineare precede la rete». [SRC-94-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Modello e loss» conserviamo l'osservazione collegata a «Una baseline lineare precede la rete» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Modello e loss» cambiamo una sola condizione vicina alla frase «Una baseline lineare precede la rete», teniamo fermo il resto e registriamo l'output «loss, metriche, manifest e limite». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Training e valutazione», riceve l'output «loss, metriche, manifest e limite» come base, ma dovrà formulare e verificare la propria distinzione.

![Percorso pratico dai fondamenti: checklist](../../assets/chapters/94_foundations_lab/LAB-01/candidate-v48.png)

La figura LAB-01 usa la famiglia checklist. Il diagramma segue il passaggio: Run, test, valutazione e report. L'input è seed, dataset piccolo, config, codice e versione, l'output è loss, metriche, manifest e limite; il vincolo da controllare è che un run locale non equivale a una prova generale.

## Training e valutazione

Curve, checkpoint, validation e test seguono il protocollo costruito nel libro. [SRC-94-004]

Il caso minimo di «Training e valutazione» si presenta così: due run con la stessa configurazione confrontati con metriche e casi falliti. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Curve, checkpoint, validation e test seguono il protocollo costruito nel libro».

Per ricostruire «Training e valutazione» annotiamo l'input «seed, dataset piccolo, config, codice e versione», poi l'operazione «run, test, valutazione e report», infine l'output «loss, metriche, manifest e limite». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Curve, checkpoint, validation e test seguono il protocollo costruito nel libro».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Curve, checkpoint, validation e test seguono il protocollo costruito nel libro». [SRC-94-004]

Il punto didattico di «Training e valutazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss, metriche, manifest e limite» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Training e valutazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Training e valutazione» portiamo l'output «loss, metriche, manifest e limite»; non portiamo invece una conclusione oltre il caso locale.

## Report

Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit. [SRC-94-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un report che collega comando, artefatti, output e limite del risultato. Da qui possiamo leggere la conseguenza dichiarata da «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit».

Nel contratto locale, l'input «seed, dataset piccolo, config, codice e versione» entra, l'operazione «run, test, valutazione e report» modifica il percorso e l'output «loss, metriche, manifest e limite» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Report»; resta da controllare che un run locale non equivale a una prova generale. La domanda locale è «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza. La verifica resta ancorata a «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit». [SRC-94-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit», non una promessa generale.

La prova di «Report» conserva input, operazione e output; poi esplicita quale parte di «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «loss, metriche, manifest e limite» come evidenza locale e conserva il confine tra evidenza e interpretazione come domanda aperta.

## Un esempio con controllo negativo: Ambiente riproducibile

Il caso intero parte dall'input «seed, dataset piccolo, config, codice e versione», applica l'operazione «run, test, valutazione e report» e osserva l'output «loss, metriche, manifest e limite». Un esempio controllato: seed, split e dtype salvati prima dell'esecuzione. Lo schema compatto è:

$$
result = run(code, data, environment)
$$

È una notazione di interfaccia, non un'identità numerica completa. Un laboratorio è utile quando il risultato può essere ricostruito. [SRC-94-001]

![Percorso pratico dai fondamenti: compare](../../assets/chapters/94_foundations_lab/LAB-02/candidate-v48.png)

La figura LAB-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Run, test, valutazione e report. L'input è seed, dataset piccolo, config, codice e versione, l'output è loss, metriche, manifest e limite; il vincolo da controllare è che un run locale non equivale a una prova generale.

## Dalla formula al run: Dataset piccolo

Il file `code/snip_94_contract.py` collega il contratto del capitolo alla frase «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-94-001.txt` conserva il risultato ripetibile del caso locale.

## Limiti, varianti e nuove misure: Report

Il meccanismo di «Percorso pratico dai fondamenti» resta legato al contratto locale. Un run locale non equivale a una prova generale. Prima di generalizzare la frase «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## L'invariante da conservare: Percorso pratico dai fondamenti

Abbiamo seguito un esperimento didattico con ambiente e artefatti dichiarati, partendo dall'input «seed, dataset piccolo, config, codice e versione» e arrivando all'output «loss, metriche, manifest e limite». Le sezioni «Ambiente riproducibile», «Dataset piccolo», «Report» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: un run locale non equivale a una prova generale. Il Capitolo 95, Costruire un piccolo language model, può partire da questo output e dichiarare la propria domanda.

### Prova di comprensione: Ambiente riproducibile

1. Ricostruisci l'oggetto continuo a partire da «Ambiente riproducibile» e indica quale parte della frase «Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti» entra nel caso.
2. Spiega quale trasformazione collega «Ambiente riproducibile» a «Report» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un run locale non equivale a una prova generale.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi con casi limite: Report

1. Ricostruisci input e output di «Ambiente riproducibile» usando un esempio di tre righe.
2. Modifica una sola variabile in «Dataset piccolo» e anticipa l'invariante che dovrebbe restare.
3. Metti «Modello e loss» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Training e valutazione».
5. Formula per «Report» una domanda che separi meccanismo e qualità del sistema.

## Fonti primarie e artefatti del capitolo: Percorso pratico dai fondamenti

Il dossier di «Percorso pratico dai fondamenti» in `FONTI_PRIMARIE.md` separa definizioni, risultati e la differenza tra media e failure; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
