<!--
chapter_id: CH-P09-SUPERVISION-VERIFIERS
part_id: P09
order_key: 500
title: Process supervision, outcome supervision e verifier
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 50. Process supervision, outcome supervision e verifier

Il Capitolo 49, Ottimizzazione diretta delle preferenze, ha lasciato disponibile una traiettoria e il segnale di un verifier. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «process supervision, outcome supervision e verifica» e verifichiamo che un verifier può ereditare bias o essere ottimizzato.

## Supervisionare il risultato

Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore. [SRC-50-001]

Prima del nome tecnico fissiamo la situazione: consideriamo tre risposte passano davanti a un verifier che accetta soltanto il risultato corretto. Da qui possiamo leggere la conseguenza dichiarata da «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore».

La sezione usa l'input «passaggi, risposta finale, criterio e indipendenza» come punto di partenza e l'output «score verificato e failure localizzata» come traccia d'uscita. La trasformazione concreta è «process supervision, outcome supervision e verifica»; il caso non è completo se non dichiariamo anche che un verifier può ereditare bias o essere ottimizzato. La condizione da isolare è «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Supervisionare il risultato» il controllo cambia una sola premessa della frase «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore». [SRC-50-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Supervisionare il risultato» conserviamo l'osservazione collegata a «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Supervisionare il risultato» conserva input, operazione e output; poi esplicita quale parte di «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Supervisionare il processo», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Supervisionare il processo

Process supervision etichetta passaggi intermedi. La validità dipende da come il processo viene reso osservabile e annotato. [SRC-50-002]

Per capire «Supervisionare il processo» partiamo da questo caso: una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano. Il caso rende osservabile il punto centrale: «Process supervision etichetta passaggi intermedi».

Per ricostruire «Supervisionare il processo» annotiamo l'input «passaggi, risposta finale, criterio e indipendenza», poi l'operazione «process supervision, outcome supervision e verifica», infine l'output «score verificato e failure localizzata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Process supervision etichetta passaggi intermedi».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Supervisionare il processo» il controllo cambia una sola premessa della frase «Process supervision etichetta passaggi intermedi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Process supervision etichetta passaggi intermedi». [SRC-50-002]

Il punto didattico di «Supervisionare il processo» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score verificato e failure localizzata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Supervisionare il processo» cambiamo una sola condizione vicina alla frase «Process supervision etichetta passaggi intermedi», teniamo fermo il resto e registriamo l'output «score verificato e failure localizzata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Verifier», riceve l'output «score verificato e failure localizzata» come base, ma dovrà formulare e verificare la propria distinzione.

## Verifier

Un verifier valuta candidate rispetto a un criterio. Può essere una regola, un esecutore, un modello o una combinazione. [SRC-50-003]

Il caso minimo di «Verifier» si presenta così: un caso in cui un verifier può ereditare bias o essere ottimizzato. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un verifier valuta candidate rispetto a un criterio».

Nel contratto locale, l'input «passaggi, risposta finale, criterio e indipendenza» entra, l'operazione «process supervision, outcome supervision e verifica» modifica il percorso e l'output «score verificato e failure localizzata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Verifier»; resta da controllare che un verifier può ereditare bias o essere ottimizzato. La domanda locale è «Un verifier valuta candidate rispetto a un criterio».

Il post-training trasforma preferenze, verifiche o tracce in un segnale di aggiornamento. Quel segnale è un proxy: bisogna separare ciò che viene premiato dal comportamento applicativo che si vuole valutare. Per «Verifier» il controllo cambia una sola premessa della frase «Un verifier valuta candidate rispetto a un criterio» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un verifier valuta candidate rispetto a un criterio». [SRC-50-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Può essere una regola, un esecutore, un modello o una combinazione. Il piccolo risultato resta un'illustrazione di «Un verifier valuta candidate rispetto a un criterio», non una promessa generale.

Il controllo minimo di «Verifier» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di target, proxy e comportamento. Da «Verifier» portiamo l'output «score verificato e failure localizzata»; non portiamo invece una conclusione oltre il caso locale.

## Reward model di processo

Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento. [SRC-50-004]

Prima del nome tecnico fissiamo la situazione: consideriamo una traiettoria di due passi in cui l'azione scelta modifica lo stato successivo prima del reward. Da qui possiamo leggere la conseguenza dichiarata da «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento».

La sezione usa l'input «passaggi, risposta finale, criterio e indipendenza» come punto di partenza e l'output «score verificato e failure localizzata» come traccia d'uscita. La trasformazione concreta è «process supervision, outcome supervision e verifica»; il caso non è completo se non dichiariamo anche che un verifier può ereditare bias o essere ottimizzato. La condizione da isolare è «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Reward model di processo» il controllo cambia una sola premessa della frase «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento». [SRC-50-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Reward model di processo» conserviamo l'osservazione collegata a «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Reward model di processo» conserva input, operazione e output; poi esplicita quale parte di «Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Goodhart e indipendenza», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Process supervision, outcome supervision e verifier: funnel](../../assets/chapters/50_supervision_verifiers/VERIFIERS-01/candidate-v48.png)

La figura VERIFIERS-01 usa la famiglia funnel. Il diagramma segue il passaggio: Process supervision, outcome supervision e verifica. L'input è passaggi, risposta finale, criterio e indipendenza, l'output è score verificato e failure localizzata; il vincolo da controllare è che un verifier può ereditare bias o essere ottimizzato.

## Goodhart e indipendenza

Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting. Servono test e verificatori indipendenti. [SRC-50-001]

Per capire «Goodhart e indipendenza» partiamo da questo caso: due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza. Il caso rende osservabile il punto centrale: «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting».

Per ricostruire «Goodhart e indipendenza» annotiamo l'input «passaggi, risposta finale, criterio e indipendenza», poi l'operazione «process supervision, outcome supervision e verifica», infine l'output «score verificato e failure localizzata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting».

Il passaggio da seguire in «Goodhart e indipendenza» è quello descritto dalla frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Goodhart e indipendenza» il controllo cambia una sola premessa della frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting». [SRC-50-001]

Il punto didattico di «Goodhart e indipendenza» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «score verificato e failure localizzata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Goodhart e indipendenza» cambiamo una sola condizione vicina alla frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting», teniamo fermo il resto e registriamo l'output «score verificato e failure localizzata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Dal concetto alla situazione concreta: Supervisionare il risultato

Il caso intero parte dall'input «passaggi, risposta finale, criterio e indipendenza», applica l'operazione «process supervision, outcome supervision e verifica» e osserva l'output «score verificato e failure localizzata». Un esempio controllato: stesso risultato finale con un passaggio corretto e uno scorretto. La formula locale è:

$$
score = verify(trace, outcome)
$$

Un verificatore di processo può osservare passaggi, esito o entrambi. [SRC-50-001]

![Process supervision, outcome supervision e verifier: loop](../../assets/chapters/50_supervision_verifiers/VERIFIERS-02/candidate-v48.png)

La figura VERIFIERS-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Process supervision, outcome supervision e verifica. L'input è passaggi, risposta finale, criterio e indipendenza, l'output è score verificato e failure localizzata; il vincolo da controllare è che un verifier può ereditare bias o essere ottimizzato.

## Una prova ripetibile: Supervisionare il processo

Il file `code/snip_50_contract.py` collega il contratto del capitolo alla frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-50-001.txt` conserva il risultato ripetibile del caso locale.

## Il trasferimento richiede altro: Goodhart e indipendenza

Il meccanismo di «Process supervision, outcome supervision e verifier» resta legato al contratto locale. Un verifier può ereditare bias o essere ottimizzato. Prima di generalizzare la frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il filo che passa oltre: Process supervision, outcome supervision e verifier

Abbiamo seguito una traiettoria e il segnale di un verifier, partendo dall'input «passaggi, risposta finale, criterio e indipendenza» e arrivando all'output «score verificato e failure localizzata». Le sezioni «Supervisionare il risultato», «Supervisionare il processo», «Goodhart e indipendenza» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: un verifier può ereditare bias o essere ottimizzato. Il Capitolo 51, Reinforcement learning con reward verificabili, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Supervisionare il risultato

1. Ricostruisci l'oggetto continuo a partire da «Supervisionare il risultato» e indica quale parte della frase «Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore» entra nel caso.
2. Spiega quale trasformazione collega «Supervisionare il risultato» a «Goodhart e indipendenza» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: un verifier può ereditare bias o essere ottimizzato.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Goodhart e indipendenza

1. Disegna il percorso di «Supervisionare il risultato» indicando dati in ingresso e risultato.
2. Ripeti «Supervisionare il processo» cambiando soltanto un valore dichiarato.
3. Trova in «Verifier» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Reward model di processo» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Goodhart e indipendenza» richiederebbe un benchmark ulteriore.

## Dove verificare definizioni e risultati: Process supervision, outcome supervision e verifier

Il dossier di «Process supervision, outcome supervision e verifier» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il segnale che premia una risposta; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a target, proxy e comportamento.
