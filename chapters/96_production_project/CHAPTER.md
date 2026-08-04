<!--
chapter_id: CH-P14-PRODUCTION-PROJECT
part_id: P14
order_key: 960
title: Progetto di produzione completo
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 96. Progetto di produzione completo

Finora abbiamo potuto descrivere un sistema ML che attraversa sviluppo, rilascio e monitoraggio. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 96 prendiamo l'input «problema, dati, modello, eval, deployment e rollback» e lo seguiamo fino all'output «servizio versionato con metriche e piano di ritorno», dichiarando prima il contratto e poi il limite.

## Definizione del problema

Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello. [SRC-96-001]

Per capire «Definizione del problema» partiamo da questo caso: una release passa offline gate, canary e rollback prima di essere candidata. Il caso rende osservabile il punto centrale: «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello».

Nel contratto locale, l'input «problema, dati, modello, eval, deployment e rollback» entra, l'operazione «design, test, release, osservabilità e change management» modifica il percorso e l'output «servizio versionato con metriche e piano di ritorno» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Definizione del problema»; resta da controllare che un modello che passa un test offline non è automaticamente pronto in produzione. La domanda locale è «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Definizione del problema» il controllo cambia una sola premessa della frase «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello». [SRC-96-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello», non una promessa generale.

Per verificare «Definizione del problema» cambiamo una sola condizione vicina alla frase «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello», teniamo fermo il resto e registriamo l'output «servizio versionato con metriche e piano di ritorno». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Architettura», riceve l'output «servizio versionato con metriche e piano di ritorno» come base, ma dovrà formulare e verificare la propria distinzione.

## Architettura

Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi. [SRC-96-004]

Il caso minimo di «Architettura» si presenta così: un diagramma che separa dati, modello, policy, API, monitor e rollback. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi».

La sezione usa l'input «problema, dati, modello, eval, deployment e rollback» come punto di partenza e l'output «servizio versionato con metriche e piano di ritorno» come traccia d'uscita. La trasformazione concreta è «design, test, release, osservabilità e change management»; il caso non è completo se non dichiariamo anche che un modello che passa un test offline non è automaticamente pronto in produzione. La condizione da isolare è «Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Architettura» il controllo cambia una sola premessa della frase «Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi». [SRC-96-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Architettura» conserviamo l'osservazione collegata a «Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Architettura» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Architettura» portiamo l'output «servizio versionato con metriche e piano di ritorno»; non portiamo invece una conclusione oltre il caso locale.

![Progetto di produzione completo: pipeline](../../assets/chapters/96_production_project/PROJECT-01/candidate-v48.png)

La figura PROJECT-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Design, test, release, osservabilità e change management. L'input è problema, dati, modello, eval, deployment e rollback, l'output è servizio versionato con metriche e piano di ritorno; il vincolo da controllare è che un modello che passa un test offline non è automaticamente pronto in produzione.

## Valutazione

Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti. [SRC-96-002]

Prima del nome tecnico fissiamo la situazione: consideriamo un gate offline con slice, soglia, errore e decisione di promozione. Da qui possiamo leggere la conseguenza dichiarata da «Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti».

Per ricostruire «Valutazione» annotiamo l'input «problema, dati, modello, eval, deployment e rollback», poi l'operazione «design, test, release, osservabilità e change management», infine l'output «servizio versionato con metriche e piano di ritorno». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti». [SRC-96-002]

Il punto didattico di «Valutazione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «servizio versionato con metriche e piano di ritorno» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Valutazione» conserva input, operazione e output; poi esplicita quale parte di «Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Deployment», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Deployment

Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale. [SRC-96-003]

Per capire «Deployment» partiamo da questo caso: un canary versionato con alert, owner e ritorno alla versione precedente. Il caso rende osservabile il punto centrale: «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale».

Nel contratto locale, l'input «problema, dati, modello, eval, deployment e rollback» entra, l'operazione «design, test, release, osservabilità e change management» modifica il percorso e l'output «servizio versionato con metriche e piano di ritorno» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Deployment»; resta da controllare che un modello che passa un test offline non è automaticamente pronto in produzione. La domanda locale è «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. Per «Deployment» il controllo cambia una sola premessa della frase «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale». [SRC-96-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale», non una promessa generale.

Per verificare «Deployment» cambiamo una sola condizione vicina alla frase «Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale», teniamo fermo il resto e registriamo l'output «servizio versionato con metriche e piano di ritorno». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Documentazione», riceve l'output «servizio versionato con metriche e piano di ritorno» come base, ma dovrà formulare e verificare la propria distinzione.

## Documentazione

Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile. [SRC-96-001]

Il caso minimo di «Documentazione» si presenta così: una model card collegata a changelog, dataset, limiti e contatto operativo. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile».

La sezione usa l'input «problema, dati, modello, eval, deployment e rollback» come punto di partenza e l'output «servizio versionato con metriche e piano di ritorno» come traccia d'uscita. La trasformazione concreta è «design, test, release, osservabilità e change management»; il caso non è completo se non dichiariamo anche che un modello che passa un test offline non è automaticamente pronto in produzione. La condizione da isolare è «Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile».

Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile». [SRC-96-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Documentazione» conserviamo l'osservazione collegata a «Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Documentazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Dal concetto alla situazione concreta: Definizione del problema

Il caso intero parte dall'input «problema, dati, modello, eval, deployment e rollback», applica l'operazione «design, test, release, osservabilità e change management» e osserva l'output «servizio versionato con metriche e piano di ritorno». Un esempio controllato: release candidata con gate offline, canary e rollback. Lo schema compatto è:

$$
release = model + eval + monitoring + rollback
$$

È una notazione di interfaccia, non un'identità numerica completa. Un progetto di produzione richiede anche gestione del ciclo di vita. [SRC-96-001]

![Progetto di produzione completo: checklist](../../assets/chapters/96_production_project/PROJECT-02/candidate-v48.png)

La figura PROJECT-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Design, test, release, osservabilità e change management. L'input è problema, dati, modello, eval, deployment e rollback, l'output è servizio versionato con metriche e piano di ritorno; il vincolo da controllare è che un modello che passa un test offline non è automaticamente pronto in produzione.

## Una prova ripetibile: Architettura

Nel run Python rendiamo osservabile la frase «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-96-001.txt` documenta il caso senza pretendere una misura generale.

## Il trasferimento richiede altro: Documentazione

Il meccanismo di «Progetto di produzione completo» non garantisce da solo che il sistema funzioni fuori dal caso guida. Un modello che passa un test offline non è automaticamente pronto in produzione. Il limite osservato riguarda la frase «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il filo che passa oltre: Progetto di produzione completo

Il percorso ha tenuto insieme un sistema ML che attraversa sviluppo, rilascio e monitoraggio, l'operazione «design, test, release, osservabilità e change management» e l'output «servizio versionato con metriche e piano di ritorno». Le sezioni «Definizione del problema», «Architettura», «Documentazione» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: un modello che passa un test offline non è automaticamente pronto in produzione. Il Capitolo 97, Riprodurre e leggere un paper, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Definizione del problema

1. Ricostruisci l'oggetto continuo a partire da «Definizione del problema» e indica quale parte della frase «Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello» entra nel caso.
2. Spiega quale trasformazione collega «Definizione del problema» a «Documentazione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un modello che passa un test offline non è automaticamente pronto in produzione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Documentazione

1. Ricostruisci input e output di «Definizione del problema» usando un esempio di tre righe.
2. Modifica una sola variabile in «Architettura» e anticipa l'invariante che dovrebbe restare.
3. Metti «Valutazione» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Deployment».
5. Formula per «Documentazione» una domanda che separi meccanismo e qualità del sistema.

## Dove verificare definizioni e risultati: Progetto di produzione completo

Per «Progetto di produzione completo», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto protocollo, slice e decisione. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
