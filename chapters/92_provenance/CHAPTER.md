<!--
chapter_id: CH-P13-PROVENANCE
part_id: P13
order_key: 920
title: Watermarking e provenienza dei contenuti
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 92. Watermarking e provenienza dei contenuti

Il risultato precedente non è ancora una soluzione completa. Partiamo da un contenuto e la sua attestazione di provenienza e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «record verificabile e stato di rilevazione» isoliamo il passaggio «digest, firma, C2PA, watermark e detection» e ne misuriamo il limite prima di passare a Diritto, governance e sostenibilità.

## Provenienza crittografica

Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili. [SRC-92-001]

Prima del nome tecnico fissiamo la situazione: consideriamo cambiare il payload cambia il digest e rende rilevabile la manomissione. Da qui possiamo leggere la conseguenza dichiarata da «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili».

La sezione usa l'input «payload, metadata, manifest e chiave o watermark» come punto di partenza e l'output «record verificabile e stato di rilevazione» come traccia d'uscita. La trasformazione concreta è «digest, firma, C2PA, watermark e detection»; il caso non è completo se non dichiariamo anche che provenienza dell'artefatto non certifica la verità del contenuto. La condizione da isolare è «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Il confronto separa integrità del record, identità del firmatario e verità del contenuto, che sono proprietà diverse della stessa pipeline. La verifica resta ancorata a «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili». [SRC-92-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Provenienza crittografica» conserviamo l'osservazione collegata a «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Provenienza crittografica» conserva input, operazione e output; poi esplicita quale parte di «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «C2PA», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## C2PA

Credenziali di contenuto registrano asserzioni e ingredienti. Assenza di credenziali non prova che un contenuto sia sintetico. [SRC-92-002]

Per capire «C2PA» partiamo da questo caso: digest di payload e metadati con verifica di una modifica. Il caso rende osservabile il punto centrale: «Credenziali di contenuto registrano asserzioni e ingredienti».

Per ricostruire «C2PA» annotiamo l'input «payload, metadata, manifest e chiave o watermark», poi l'operazione «digest, firma, C2PA, watermark e detection», infine l'output «record verificabile e stato di rilevazione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Credenziali di contenuto registrano asserzioni e ingredienti».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «C2PA» il controllo cambia una sola premessa della frase «Credenziali di contenuto registrano asserzioni e ingredienti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Credenziali di contenuto registrano asserzioni e ingredienti». [SRC-92-002]

Il punto didattico di «C2PA» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «record verificabile e stato di rilevazione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «C2PA» cambiamo una sola condizione vicina alla frase «Credenziali di contenuto registrano asserzioni e ingredienti», teniamo fermo il resto e registriamo l'output «record verificabile e stato di rilevazione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Watermarking», riceve l'output «record verificabile e stato di rilevazione» come base, ma dovrà formulare e verificare la propria distinzione.

## Watermarking

Un generatore può modulare token o segnali per consentire rilevamento statistico. Robustezza e falsi positivi dipendono dal canale. [SRC-92-003]

Il caso minimo di «Watermarking» si presenta così: un payload modificato dopo la firma, con digest e metadati confrontati separatamente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un generatore può modulare token o segnali per consentire rilevamento statistico».

Nel contratto locale, l'input «payload, metadata, manifest e chiave o watermark» entra, l'operazione «digest, firma, C2PA, watermark e detection» modifica il percorso e l'output «record verificabile e stato di rilevazione» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Watermarking»; resta da controllare che provenienza dell'artefatto non certifica la verità del contenuto. La domanda locale è «Un generatore può modulare token o segnali per consentire rilevamento statistico».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Il confronto separa integrità del record, identità del firmatario e verità del contenuto, che sono proprietà diverse della stessa pipeline. La verifica resta ancorata a «Un generatore può modulare token o segnali per consentire rilevamento statistico». [SRC-92-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Robustezza e falsi positivi dipendono dal canale. Il piccolo risultato resta un'illustrazione di «Un generatore può modulare token o segnali per consentire rilevamento statistico», non una promessa generale.

Il controllo minimo di «Watermarking» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Watermarking» portiamo l'output «record verificabile e stato di rilevazione»; non portiamo invece una conclusione oltre il caso locale.

## Detection

Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift. Un punteggio non è una prova forense isolata. [SRC-92-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un contenuto viene accompagnato da fonte, versione e digest. Il record rende ricostruibile la storia dell'artefatto, ma non sostituisce la verifica del contenuto. Da qui possiamo leggere la conseguenza dichiarata da «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift».

La sezione usa l'input «payload, metadata, manifest e chiave o watermark» come punto di partenza e l'output «record verificabile e stato di rilevazione» come traccia d'uscita. La trasformazione concreta è «digest, firma, C2PA, watermark e detection»; il caso non è completo se non dichiariamo anche che provenienza dell'artefatto non certifica la verità del contenuto. La condizione da isolare è «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Detection» il controllo cambia una sola premessa della frase «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift». [SRC-92-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Detection» conserviamo l'osservazione collegata a «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Detection» conserva input, operazione e output; poi esplicita quale parte di «Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Policy e interfaccia», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Watermarking e provenienza dei contenuti: manifest](../../assets/chapters/92_provenance/PROVENANCE-01/candidate-v48.png)

La figura PROVENANCE-01 usa la famiglia manifest. Il diagramma segue il passaggio: Digest, firma, C2PA, watermark e detection. L'input è payload, metadata, manifest e chiave o watermark, l'output è record verificabile e stato di rilevazione; il vincolo da controllare è che provenienza dell'artefatto non certifica la verità del contenuto.

## Policy e interfaccia

Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione. [SRC-92-004]

Per capire «Policy e interfaccia» partiamo da questo caso: una traiettoria di due passi in cui l'azione scelta modifica lo stato successivo prima del reward. Il caso rende osservabile il punto centrale: «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione».

Per ricostruire «Policy e interfaccia» annotiamo l'input «payload, metadata, manifest e chiave o watermark», poi l'operazione «digest, firma, C2PA, watermark e detection», infine l'output «record verificabile e stato di rilevazione». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Policy e interfaccia» il controllo cambia una sola premessa della frase «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione». [SRC-92-004]

Il punto didattico di «Policy e interfaccia» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «record verificabile e stato di rilevazione» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Policy e interfaccia» cambiamo una sola condizione vicina alla frase «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione», teniamo fermo il resto e registriamo l'output «record verificabile e stato di rilevazione». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il contratto in un caso piccolo: Provenienza crittografica

Il caso intero parte dall'input «payload, metadata, manifest e chiave o watermark», applica l'operazione «digest, firma, C2PA, watermark e detection» e osserva l'output «record verificabile e stato di rilevazione». Un esempio controllato: digest di payload e metadati con verifica di una modifica. Lo schema compatto è:

$$
digest = hash(content + metadata)
$$

È una notazione di interfaccia, non un'identità numerica completa. Il digest collega contenuto e metadati senza certificare la verità semantica. [SRC-92-001]

![Watermarking e provenienza dei contenuti: timeline](../../assets/chapters/92_provenance/PROVENANCE-02/candidate-v48.png)

La figura PROVENANCE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Digest, firma, C2PA, watermark e detection. L'input è payload, metadata, manifest e chiave o watermark, l'output è record verificabile e stato di rilevazione; il vincolo da controllare è che provenienza dell'artefatto non certifica la verità del contenuto.

## Dalla trasformazione al test: C2PA

Lo snippet locale mette in esecuzione questo caso: digest di payload e metadati con verifica di una modifica. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-92-001.txt`, come evidenza locale e non come benchmark di produzione.

## Il perimetro della conclusione: Policy e interfaccia

Il caso di «Watermarking e provenienza dei contenuti» non certifica un servizio completo. Provenienza dell'artefatto non certifica la verità del contenuto. La domanda successiva è se «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Una sintesi operativa: Watermarking e provenienza dei contenuti

Il filo della lezione va dall'input «payload, metadata, manifest e chiave o watermark» all'output «record verificabile e stato di rilevazione». Nei passaggi «Provenienza crittografica», «C2PA», «Policy e interfaccia» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: provenienza dell'artefatto non certifica la verità del contenuto. Il Capitolo 93, Diritto, governance e sostenibilità, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Provenienza crittografica

1. Ricostruisci l'oggetto continuo a partire da «Provenienza crittografica» e indica quale parte della frase «Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili» entra nel caso.
2. Spiega quale trasformazione collega «Provenienza crittografica» a «Policy e interfaccia» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: provenienza dell'artefatto non certifica la verità del contenuto.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Policy e interfaccia

1. Disegna il percorso di «Provenienza crittografica» indicando dati in ingresso e risultato.
2. Ripeti «C2PA» cambiando soltanto un valore dichiarato.
3. Trova in «Watermarking» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Detection» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Policy e interfaccia» richiederebbe un benchmark ulteriore.

## Materiali, fonti e codice verificato: Watermarking e provenienza dei contenuti

Per ricontrollare «Watermarking e provenienza dei contenuti», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il confine tra evidenza e interpretazione oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
