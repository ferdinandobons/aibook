<!--
chapter_id: CH-P12-QUANTIZATION
part_id: P12
order_key: 740
title: Quantizzazione
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 74. Quantizzazione

Una frase plausibile non basta a spiegare quantizzazione. L'oggetto è un tensore reale e la sua rappresentazione quantizzata; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Scala e zero point

Una mappa affine converte valori floating point in interi. Granularità per tensor, channel o group cambia errore e metadata. [SRC-74-001]

Prima del nome tecnico fissiamo la situazione: consideriamo tre valori con scala 0,25 vengono quantizzati e ricostruiti con errore massimo misurato. Da qui possiamo leggere la conseguenza dichiarata da «Una mappa affine converte valori floating point in interi».

La sezione usa l'input «valori, scale, zero-point, dtype e calibrazione» come punto di partenza e l'output «codici, tensore ricostruito, errore e memoria» come traccia d'uscita. La trasformazione concreta è «PTQ, QAT, weight-only o activation quantization»; il caso non è completo se non dichiariamo anche che scala e dominio di calibrazione fanno parte del risultato. La condizione da isolare è «Una mappa affine converte valori floating point in interi».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Scala e zero point» il controllo cambia una sola premessa della frase «Una mappa affine converte valori floating point in interi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una mappa affine converte valori floating point in interi». [SRC-74-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Scala e zero point» conserviamo l'osservazione collegata a «Una mappa affine converte valori floating point in interi» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Scala e zero point» conserva input, operazione e output; poi esplicita quale parte di «Una mappa affine converte valori floating point in interi» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «PTQ», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## PTQ

Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale. [SRC-74-002]

Per capire «PTQ» partiamo da questo caso: tre valori quantizzati con scala 0,25 e errore massimo. Il caso rende osservabile il punto centrale: «Post-training quantization usa calibration senza riaddestrare completamente».

Per ricostruire «PTQ» annotiamo l'input «valori, scale, zero-point, dtype e calibrazione», poi l'operazione «PTQ, QAT, weight-only o activation quantization», infine l'output «codici, tensore ricostruito, errore e memoria». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Post-training quantization usa calibration senza riaddestrare completamente».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «PTQ» il controllo cambia una sola premessa della frase «Post-training quantization usa calibration senza riaddestrare completamente» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Post-training quantization usa calibration senza riaddestrare completamente». [SRC-74-002]

Il punto didattico di «PTQ» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «codici, tensore ricostruito, errore e memoria» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «PTQ» cambiamo una sola condizione vicina alla frase «Post-training quantization usa calibration senza riaddestrare completamente», teniamo fermo il resto e registriamo l'output «codici, tensore ricostruito, errore e memoria». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «QAT», riceve l'output «codici, tensore ricostruito, errore e memoria» come base, ma dovrà formulare e verificare la propria distinzione.

## QAT

Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. [SRC-74-003]

Il caso minimo di «QAT» si presenta così: un caso in cui scala e dominio di calibrazione fanno parte del risultato. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi».

Nel contratto locale, l'input «valori, scale, zero-point, dtype e calibrazione» entra, l'operazione «PTQ, QAT, weight-only o activation quantization» modifica il percorso e l'output «codici, tensore ricostruito, errore e memoria» è ciò che osserviamo. Qui cambia soprattutto il passaggio «QAT»; resta da controllare che scala e dominio di calibrazione fanno parte del risultato. La domanda locale è «Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «QAT» il controllo cambia una sola premessa della frase «Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi». [SRC-74-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi», non una promessa generale.

Il controllo minimo di «QAT» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di latency, memoria e throughput. Da «QAT» portiamo l'output «codici, tensore ricostruito, errore e memoria»; non portiamo invece una conclusione oltre il caso locale.

## Weight-only e activation quantization

Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. [SRC-74-004]

Prima del nome tecnico fissiamo la situazione: consideriamo tre valori floating point quantizzati con una scala dichiarata e confrontati con la ricostruzione. Da qui possiamo leggere la conseguenza dichiarata da «Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo».

La sezione usa l'input «valori, scale, zero-point, dtype e calibrazione» come punto di partenza e l'output «codici, tensore ricostruito, errore e memoria» come traccia d'uscita. La trasformazione concreta è «PTQ, QAT, weight-only o activation quantization»; il caso non è completo se non dichiariamo anche che scala e dominio di calibrazione fanno parte del risultato. La condizione da isolare è «Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Il controllo confronta valore originale, rappresentazione compressa e ricostruzione, riportando separatamente errore numerico e comportamento sul compito. La verifica resta ancorata a «Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo». [SRC-74-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Weight-only e activation quantization» conserviamo l'osservazione collegata a «Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Weight-only e activation quantization» conserva input, operazione e output; poi esplicita quale parte di «Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Metodi per LLM», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Quantizzazione: chart](../../assets/chapters/74_quantization/QUANTIZATI-01/candidate-v48.png)

La figura QUANTIZATI-01 usa la famiglia chart. Il diagramma segue il passaggio: PTQ, QAT, weight-only o activation quantization. L'input è valori, scale, zero-point, dtype e calibrazione, l'output è codici, tensore ricostruito, errore e memoria; il vincolo da controllare è che scala e dominio di calibrazione fanno parte del risultato.

## Metodi per LLM

GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti. [SRC-74-001]

Per capire «Metodi per LLM» partiamo da questo caso: ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo. Il caso rende osservabile il punto centrale: «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti».

Per ricostruire «Metodi per LLM» annotiamo l'input «valori, scale, zero-point, dtype e calibrazione», poi l'operazione «PTQ, QAT, weight-only o activation quantization», infine l'output «codici, tensore ricostruito, errore e memoria». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti».

L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end. Per «Metodi per LLM» il controllo cambia una sola premessa della frase «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti». [SRC-74-001]

Il punto didattico di «Metodi per LLM» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «codici, tensore ricostruito, errore e memoria» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Metodi per LLM» cambiamo una sola condizione vicina alla frase «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti», teniamo fermo il resto e registriamo l'output «codici, tensore ricostruito, errore e memoria». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il caso minimo e la sua variante: Scala e zero point

Il caso intero parte dall'input «valori, scale, zero-point, dtype e calibrazione», applica l'operazione «PTQ, QAT, weight-only o activation quantization» e osserva l'output «codici, tensore ricostruito, errore e memoria». Un esempio controllato: tre valori quantizzati con scala 0,25 e errore massimo. La formula locale è:

$$
x_hat = scale * round(x / scale)
$$

Quantizzare espone il trade-off tra memoria, errore e velocità. [SRC-74-001]

![Quantizzazione: compare](../../assets/chapters/74_quantization/QUANTIZATI-02/candidate-v48.png)

La figura QUANTIZATI-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: PTQ, QAT, weight-only o activation quantization. L'input è valori, scale, zero-point, dtype e calibrazione, l'output è codici, tensore ricostruito, errore e memoria; il vincolo da controllare è che scala e dominio di calibrazione fanno parte del risultato.

## Che cosa osserva lo snippet: PTQ

Nel run Python rendiamo osservabile la frase «Una mappa affine converte valori floating point in interi» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-74-001.txt` documenta il caso senza pretendere una misura generale.

## Che cosa non dimostra: Metodi per LLM

Il meccanismo di «Quantizzazione» non garantisce da solo che il sistema funzioni fuori dal caso guida. Scala e dominio di calibrazione fanno parte del risultato. Il limite osservato riguarda la frase «Una mappa affine converte valori floating point in interi»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## La mappa delle condizioni: Quantizzazione

Il percorso ha tenuto insieme un tensore reale e la sua rappresentazione quantizzata, l'operazione «PTQ, QAT, weight-only o activation quantization» e l'output «codici, tensore ricostruito, errore e memoria». Le sezioni «Scala e zero point», «PTQ», «Metodi per LLM» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: scala e dominio di calibrazione fanno parte del risultato. Il Capitolo 75, Modelli low-bit nativi e co-design numerico, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Scala e zero point

1. Ricostruisci l'oggetto continuo a partire da «Scala e zero point» e indica quale parte della frase «Una mappa affine converte valori floating point in interi» entra nel caso.
2. Spiega quale trasformazione collega «Scala e zero point» a «Metodi per LLM» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: scala e dominio di calibrazione fanno parte del risultato.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Metodi per LLM

1. Ricostruisci input e output di «Scala e zero point» usando un esempio di tre righe.
2. Modifica una sola variabile in «PTQ» e anticipa l'invariante che dovrebbe restare.
3. Metti «QAT» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Weight-only e activation quantization».
5. Formula per «Metodi per LLM» una domanda che separi meccanismo e qualità del sistema.

## Fonti e risultati locali: Quantizzazione

Per «Quantizzazione», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto latency, memoria e throughput. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a latency, memoria e throughput.
