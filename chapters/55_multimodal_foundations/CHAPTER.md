<!--
chapter_id: CH-P10-MULTIMODAL-FOUNDATIONS
part_id: P10
order_key: 550
title: Fondamenti della multimodalità
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 55. Fondamenti della multimodalità

Il Capitolo 54, Aggiornamento, merging ed editing del modello, ha lasciato disponibile rappresentazioni di modalità differenti. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «encoder, proiezione, alignment e fusion» e verifichiamo che allineamento misurato non equivale a comprensione generale.

## Modalità e misure

Testo, immagine, audio e azione hanno strutture e scale differenti. Ogni encoder produce una rappresentazione con assi dichiarati. [SRC-55-001]

Il caso minimo di «Modalità e misure» si presenta così: due vettori, testo e immagine, vengono proiettati nella stessa dimensione prima della fusione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Testo, immagine, audio e azione hanno strutture e scale differenti».

Per ricostruire «Modalità e misure» annotiamo l'input «testo, immagine, audio e maschere di modalità», poi l'operazione «encoder, proiezione, alignment e fusion», infine l'output «spazio condiviso o output condizionato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Testo, immagine, audio e azione hanno strutture e scale differenti».

Il passaggio da seguire in «Modalità e misure» è quello descritto dalla frase «Testo, immagine, audio e azione hanno strutture e scale differenti»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Modalità e misure» il controllo cambia una sola premessa della frase «Testo, immagine, audio e azione hanno strutture e scale differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Testo, immagine, audio e azione hanno strutture e scale differenti». [SRC-55-001]

Il punto didattico di «Modalità e misure» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «spazio condiviso o output condizionato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Modalità e misure» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «Modalità e misure» portiamo l'output «spazio condiviso o output condizionato»; non portiamo invece una conclusione oltre il caso locale.

## Allineamento

Coppie sincronizzate o semanticamente collegate forniscono un segnale comune. Corrispondenza temporale e semantica non coincidono sempre. [SRC-55-002]

Prima del nome tecnico fissiamo la situazione: consideriamo due vettori di modalità proiettati nella stessa dimensione. Da qui possiamo leggere la conseguenza dichiarata da «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune».

Nel contratto locale, l'input «testo, immagine, audio e maschere di modalità» entra, l'operazione «encoder, proiezione, alignment e fusion» modifica il percorso e l'output «spazio condiviso o output condizionato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Allineamento»; resta da controllare che allineamento misurato non equivale a comprensione generale. La domanda locale è «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune».

Il passaggio da seguire in «Allineamento» è quello descritto dalla frase «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Allineamento» il controllo cambia una sola premessa della frase «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune». [SRC-55-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Corrispondenza temporale e semantica non coincidono sempre. Il piccolo risultato resta un'illustrazione di «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune», non una promessa generale.

La prova di «Allineamento» conserva input, operazione e output; poi esplicita quale parte di «Coppie sincronizzate o semanticamente collegate forniscono un segnale comune» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Fusion», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Fusion

Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati. [SRC-55-003]

Per capire «Fusion» partiamo da questo caso: un caso in cui allineamento misurato non equivale a comprensione generale. Il caso rende osservabile il punto centrale: «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati».

La sezione usa l'input «testo, immagine, audio e maschere di modalità» come punto di partenza e l'output «spazio condiviso o output condizionato» come traccia d'uscita. La trasformazione concreta è «encoder, proiezione, alignment e fusion»; il caso non è completo se non dichiariamo anche che allineamento misurato non equivale a comprensione generale. La condizione da isolare è «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati».

Il passaggio da seguire in «Fusion» è quello descritto dalla frase «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Fusion» il controllo cambia una sola premessa della frase «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati». [SRC-55-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Fusion» conserviamo l'osservazione collegata a «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Fusion» cambiamo una sola condizione vicina alla frase «Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati», teniamo fermo il resto e registriamo l'output «spazio condiviso o output condizionato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Missing modality», riceve l'output «spazio condiviso o output condizionato» come base, ma dovrà formulare e verificare la propria distinzione.

![Fondamenti della multimodalità: scatter](../../assets/chapters/55_multimodal_foundations/FOUNDATION-01/candidate-v48.png)

La figura FOUNDATION-01 usa la famiglia scatter. Il diagramma segue il passaggio: Encoder, proiezione, alignment e fusion. L'input è testo, immagine, audio e maschere di modalità, l'output è spazio condiviso o output condizionato; il vincolo da controllare è che allineamento misurato non equivale a comprensione generale.

## Missing modality

Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata. [SRC-55-004]

Il caso minimo di «Missing modality» si presenta così: due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata».

Per ricostruire «Missing modality» annotiamo l'input «testo, immagine, audio e maschere di modalità», poi l'operazione «encoder, proiezione, alignment e fusion», infine l'output «spazio condiviso o output condizionato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata».

Il passaggio da seguire in «Missing modality» è quello descritto dalla frase «Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Missing modality» il controllo cambia una sola premessa della frase «Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata». [SRC-55-004]

Il punto didattico di «Missing modality» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «spazio condiviso o output condizionato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Missing modality» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «Missing modality» portiamo l'output «spazio condiviso o output condizionato»; non portiamo invece una conclusione oltre il caso locale.

## Valutazione

Comprensione, retrieval, grounding e generazione richiedono benchmark distinti. Una media multimodale può nascondere una modalità debole. [SRC-55-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Da qui possiamo leggere la conseguenza dichiarata da «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti».

Nel contratto locale, l'input «testo, immagine, audio e maschere di modalità» entra, l'operazione «encoder, proiezione, alignment e fusion» modifica il percorso e l'output «spazio condiviso o output condizionato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Valutazione»; resta da controllare che allineamento misurato non equivale a comprensione generale. La domanda locale è «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti».

Una valutazione deve collegare claim, popolazione, protocollo e decisione. Media, slice, failure, giudice e incertezza misurano aspetti diversi e non diventano intercambiabili perché condividono una tabella. Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse. La verifica resta ancorata a «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti». [SRC-55-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Una media multimodale può nascondere una modalità debole. Il piccolo risultato resta un'illustrazione di «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti», non una promessa generale.

La prova di «Valutazione» conserva input, operazione e output; poi esplicita quale parte di «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «spazio condiviso o output condizionato» come evidenza locale e conserva il contributo effettivo di ciascun segnale come domanda aperta.

## Un caso dall'input all'output: Modalità e misure

Il caso intero parte dall'input «testo, immagine, audio e maschere di modalità», applica l'operazione «encoder, proiezione, alignment e fusion» e osserva l'output «spazio condiviso o output condizionato». Un esempio controllato: due vettori di modalità proiettati nella stessa dimensione. La formula locale è:

$$
z_m = f_m(x_m)
$$

Ogni modalità ha un encoder e un contratto prima dell'allineamento. [SRC-55-001]

![Fondamenti della multimodalità: compare](../../assets/chapters/55_multimodal_foundations/FOUNDATION-02/candidate-v48.png)

La figura FOUNDATION-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Encoder, proiezione, alignment e fusion. L'input è testo, immagine, audio e maschere di modalità, l'output è spazio condiviso o output condizionato; il vincolo da controllare è che allineamento misurato non equivale a comprensione generale.

## Dal meccanismo alla prova locale: Allineamento

Nel run Python rendiamo osservabile la frase «Testo, immagine, audio e azione hanno strutture e scale differenti» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-55-001.txt` documenta il caso senza pretendere una misura generale.

## Dove il risultato si ferma: Valutazione

Il meccanismo di «Fondamenti della multimodalità» non garantisce da solo che il sistema funzioni fuori dal caso guida. Allineamento misurato non equivale a comprensione generale. Il limite osservato riguarda la frase «Testo, immagine, audio e azione hanno strutture e scale differenti»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Che cosa portiamo avanti: Fondamenti della multimodalità

Il percorso ha tenuto insieme rappresentazioni di modalità differenti, l'operazione «encoder, proiezione, alignment e fusion» e l'output «spazio condiviso o output condizionato». Le sezioni «Modalità e misure», «Allineamento», «Valutazione» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: allineamento misurato non equivale a comprensione generale. Il Capitolo 56, Vision encoder e Vision-Language Model, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Modalità e misure

1. Ricostruisci l'oggetto continuo a partire da «Modalità e misure» e indica quale parte della frase «Testo, immagine, audio e azione hanno strutture e scale differenti» entra nel caso.
2. Spiega quale trasformazione collega «Modalità e misure» a «Valutazione» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: allineamento misurato non equivale a comprensione generale.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Comprensione, retrieval, grounding e generazione richiedono benchmark distinti» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Valutazione

1. Ricostruisci input e output di «Modalità e misure» usando un esempio di tre righe.
2. Modifica una sola variabile in «Allineamento» e anticipa l'invariante che dovrebbe restare.
3. Metti «Fusion» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Missing modality».
5. Formula per «Valutazione» una domanda che separi meccanismo e qualità del sistema.

## Fonti, codice e materiali: Fondamenti della multimodalità

Per «Fondamenti della multimodalità», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto allineamento tra modalità. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a allineamento tra modalità.
