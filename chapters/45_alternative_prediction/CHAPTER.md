<!--
chapter_id: CH-P08-ALTERNATIVE-PREDICTION
part_id: P08
order_key: 450
title: Byte, predizione multi-token e language diffusion
maturity: FRONTIER
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 45. Byte, predizione multi-token e language diffusion

Il Capitolo 44, Mixture of Experts e calcolo condizionale, ha lasciato disponibile unità di predizione dal byte al token multiplo. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «raggruppamento, multi-token prediction o diffusione discreta» e verifichiamo che granularità della rappresentazione e parallelismo sono assi distinti.

## Byte e caratteri

Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe. [SRC-45-001]

Per capire «Byte e caratteri» partiamo da questo caso: la stessa stringa convertita prima in code point e poi in byte UTF-8, conservando la reversibilità. Il caso rende osservabile il punto centrale: «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe».

Nel contratto locale, l'input «byte, gerarchia, target e numero di passi» entra, l'operazione «raggruppamento, multi-token prediction o diffusione discreta» modifica il percorso e l'output «unità predette, loss e durata di decoding» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Byte e caratteri»; resta da controllare che granularità della rappresentazione e parallelismo sono assi distinti. La domanda locale è «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe».

Prima del modello, il testo diventa una sequenza di unità con una convenzione precisa. Encoding, tokenizer, token speciali, mask e packing modificano l'input effettivo e quindi fanno parte del contratto del checkpoint. Per «Byte e caratteri» il controllo cambia una sola premessa della frase «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe». [SRC-45-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe», non una promessa generale.

Per verificare «Byte e caratteri» cambiamo una sola condizione vicina alla frase «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe», teniamo fermo il resto e registriamo l'output «unità predette, loss e durata di decoding». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Gerarchie di byte», riceve l'output «unità predette, loss e durata di decoding» come base, ma dovrà formulare e verificare la propria distinzione.

## Gerarchie di byte

Patch fisse o dinamiche riducono la lunghezza vista dal modello globale. [SRC-45-002]

Il caso minimo di «Gerarchie di byte» si presenta così: la stessa stringa convertita prima in code point e poi in byte UTF-8, conservando la reversibilità. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Patch fisse o dinamiche riducono la lunghezza vista dal modello globale».

La sezione usa l'input «byte, gerarchia, target e numero di passi» come punto di partenza e l'output «unità predette, loss e durata di decoding» come traccia d'uscita. La trasformazione concreta è «raggruppamento, multi-token prediction o diffusione discreta»; il caso non è completo se non dichiariamo anche che granularità della rappresentazione e parallelismo sono assi distinti. La condizione da isolare è «Patch fisse o dinamiche riducono la lunghezza vista dal modello globale».

Prima del modello, il testo diventa una sequenza di unità con una convenzione precisa. Encoding, tokenizer, token speciali, mask e packing modificano l'input effettivo e quindi fanno parte del contratto del checkpoint. Per «Gerarchie di byte» il controllo cambia una sola premessa della frase «Patch fisse o dinamiche riducono la lunghezza vista dal modello globale» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Patch fisse o dinamiche riducono la lunghezza vista dal modello globale». [SRC-45-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Gerarchie di byte» conserviamo l'osservazione collegata a «Patch fisse o dinamiche riducono la lunghezza vista dal modello globale» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Gerarchie di byte» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Gerarchie di byte» portiamo l'output «unità predette, loss e durata di decoding»; non portiamo invece una conclusione oltre il caso locale.

![Byte, predizione multi-token e language diffusion: pipeline](../../assets/chapters/45_alternative_prediction/ALT-01/candidate-v47.png)

La figura ALT-01 usa la famiglia pipeline. Il diagramma segue il passaggio: Raggruppamento, multi-token prediction o diffusione discreta. L'input è byte, gerarchia, target e numero di passi, l'output è unità predette, loss e durata di decoding; il vincolo da controllare è che granularità della rappresentazione e parallelismo sono assi distinti.

## Predizione multi-token

Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato. [SRC-45-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Da qui possiamo leggere la conseguenza dichiarata da «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato».

Per ricostruire «Predizione multi-token» annotiamo l'input «byte, gerarchia, target e numero di passi», poi l'operazione «raggruppamento, multi-token prediction o diffusione discreta», infine l'output «unità predette, loss e durata di decoding». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato».

Il passaggio da seguire in «Predizione multi-token» è quello descritto dalla frase «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Predizione multi-token» il controllo cambia una sola premessa della frase «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato». [SRC-45-003]

Il punto didattico di «Predizione multi-token» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «unità predette, loss e durata di decoding» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Predizione multi-token» conserva input, operazione e output; poi esplicita quale parte di «Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Diffusione linguistica», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Diffusione linguistica

Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi. [SRC-45-004]

Per capire «Diffusione linguistica» partiamo da questo caso: tre probabilità che sommano a 1 prima del campionamento, distinguendo plausibilità del campione e copertura. Il caso rende osservabile il punto centrale: «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi».

Nel contratto locale, l'input «byte, gerarchia, target e numero di passi» entra, l'operazione «raggruppamento, multi-token prediction o diffusione discreta» modifica il percorso e l'output «unità predette, loss e durata di decoding» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Diffusione linguistica»; resta da controllare che granularità della rappresentazione e parallelismo sono assi distinti. La domanda locale è «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi».

La diffusione separa corruzione e ricostruzione attraverso uno schedule. Target, parametrizzazione e sampler descrivono punti diversi dello stesso percorso e una riduzione degli step non conserva automaticamente ogni proprietà. Per «Diffusione linguistica» il controllo cambia una sola premessa della frase «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi». [SRC-45-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi», non una promessa generale.

Per verificare «Diffusione linguistica» cambiamo una sola condizione vicina alla frase «Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi», teniamo fermo il resto e registriamo l'output «unità predette, loss e durata di decoding». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Assi separati», riceve l'output «unità predette, loss e durata di decoding» come base, ma dovrà formulare e verificare la propria distinzione.

## Assi separati

Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono. [SRC-45-001]

Il caso minimo di «Assi separati» si presenta così: un messaggio con ruolo, contenuto e maschera che assegna il gradiente soltanto alla risposta. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono».

La sezione usa l'input «byte, gerarchia, target e numero di passi» come punto di partenza e l'output «unità predette, loss e durata di decoding» come traccia d'uscita. La trasformazione concreta è «raggruppamento, multi-token prediction o diffusione discreta»; il caso non è completo se non dichiariamo anche che granularità della rappresentazione e parallelismo sono assi distinti. La condizione da isolare è «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono».

Il passaggio da seguire in «Assi separati» è quello descritto dalla frase «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. In questa sezione si isola la maschera: a parità di messaggio, si controlla quali posizioni contribuiscono davvero alla loss. La verifica resta ancorata a «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono». [SRC-45-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Assi separati» conserviamo l'osservazione collegata a «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Assi separati» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Il caso minimo e la sua variante: Byte e caratteri

Il caso intero parte dall'input «byte, gerarchia, target e numero di passi», applica l'operazione «raggruppamento, multi-token prediction o diffusione discreta» e osserva l'output «unità predette, loss e durata di decoding». Un esempio controllato: due byte raggruppati e due target predetti nello stesso passo. Lo schema compatto è:

$$
x = decode(bytes, hierarchy, steps)
$$

È una notazione di interfaccia, non un'identità numerica completa. Byte, unità gerarchiche e numero di passi sono assi separati del design. [SRC-45-001]

![Byte, predizione multi-token e language diffusion: compare](../../assets/chapters/45_alternative_prediction/ALT-02/candidate-v47.png)

La figura ALT-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Raggruppamento, multi-token prediction o diffusione discreta. L'input è byte, gerarchia, target e numero di passi, l'output è unità predette, loss e durata di decoding; il vincolo da controllare è che granularità della rappresentazione e parallelismo sono assi distinti.

## Che cosa osserva lo snippet: Gerarchie di byte

Nel run Python rendiamo osservabile la frase «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-45-001.txt` documenta il caso senza pretendere una misura generale.

## Che cosa non dimostra: Assi separati

Il meccanismo di «Byte, predizione multi-token e language diffusion» non garantisce da solo che il sistema funzioni fuori dal caso guida. Granularità della rappresentazione e parallelismo sono assi distinti. Il limite osservato riguarda la frase «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## La mappa delle condizioni: Byte, predizione multi-token e language diffusion

Il percorso ha tenuto insieme unità di predizione dal byte al token multiplo, l'operazione «raggruppamento, multi-token prediction o diffusione discreta» e l'output «unità predette, loss e durata di decoding». Le sezioni «Byte e caratteri», «Gerarchie di byte», «Assi separati» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: granularità della rappresentazione e parallelismo sono assi distinti. Il Capitolo 46, Supervised fine-tuning e instruction tuning, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Byte e caratteri

1. Ricostruisci l'oggetto continuo a partire da «Byte e caratteri» e indica quale parte della frase «Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe» entra nel caso.
2. Spiega quale trasformazione collega «Byte e caratteri» a «Assi separati» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: granularità della rappresentazione e parallelismo sono assi distinti.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Assi separati

1. Disegna il percorso di «Byte e caratteri» indicando dati in ingresso e risultato.
2. Ripeti «Gerarchie di byte» cambiando soltanto un valore dichiarato.
3. Trova in «Predizione multi-token» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Diffusione linguistica» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Assi separati» richiederebbe un benchmark ulteriore.

## Fonti e risultati locali: Byte, predizione multi-token e language diffusion

Per «Byte, predizione multi-token e language diffusion», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
