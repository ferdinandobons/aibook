<!--
chapter_id: CH-P11-CONTEXT-RETRIEVAL-MEMORY
part_id: P11
order_key: 660
title: Contesto lungo, retrieval e memoria
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 66. Contesto lungo, retrieval e memoria

Finora abbiamo potuto descrivere la decisione tra contesto, retrieval e memoria. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 66 prendiamo l'input «segmento, query, budget e durata» e lo seguiamo fino all'output «contesto scelto, memoria aggiornata e costo», dichiarando prima il contratto e poi il limite.

## Tre risorse differenti

Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti. [SRC-66-001]

Per capire «Tre risorse differenti» partiamo da questo caso: un fatto stabile entra nella memoria persistente, mentre un dettaglio recente resta nel contesto breve. Il caso rende osservabile il punto centrale: «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti».

Nel contratto locale, l'input «segmento, query, budget e durata» entra, l'operazione «routing, scrittura episodica e recupero» modifica il percorso e l'output «contesto scelto, memoria aggiornata e costo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Tre risorse differenti»; resta da controllare che memoria persistente e contesto temporaneo hanno politiche diverse. La domanda locale è «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Tre risorse differenti» il controllo cambia una sola premessa della frase «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti». [SRC-66-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti», non una promessa generale.

Per verificare «Tre risorse differenti» cambiamo una sola condizione vicina alla frase «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti», teniamo fermo il resto e registriamo l'output «contesto scelto, memoria aggiornata e costo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Quando usare il contesto», riceve l'output «contesto scelto, memoria aggiornata e costo» come base, ma dovrà formulare e verificare la propria distinzione.

## Quando usare il contesto

Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta. [SRC-66-002]

Il caso minimo di «Quando usare il contesto» si presenta così: un fatto stabile salvato e un dettaglio recente escluso. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta».

La sezione usa l'input «segmento, query, budget e durata» come punto di partenza e l'output «contesto scelto, memoria aggiornata e costo» come traccia d'uscita. La trasformazione concreta è «routing, scrittura episodica e recupero»; il caso non è completo se non dichiariamo anche che memoria persistente e contesto temporaneo hanno politiche diverse. La condizione da isolare è «Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La variabile da isolare è il pattern di visibilità o di riuso: la stessa shape può corrispondere a dipendenze e costi diversi. La verifica resta ancorata a «Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta». [SRC-66-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Quando usare il contesto» conserviamo l'osservazione collegata a «Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Quando usare il contesto» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. Da «Quando usare il contesto» portiamo l'output «contesto scelto, memoria aggiornata e costo»; non portiamo invece una conclusione oltre il caso locale.

![Contesto lungo, retrieval e memoria: queue](../../assets/chapters/66_context_retrieval_memory/MEMORY-01/candidate-v48.png)

La figura MEMORY-01 usa la famiglia queue. Il diagramma segue il passaggio: Routing, scrittura episodica e recupero. L'input è segmento, query, budget e durata, l'output è contesto scelto, memoria aggiornata e costo; il vincolo da controllare è che memoria persistente e contesto temporaneo hanno politiche diverse.

## Quando recuperare

Retrieval seleziona un sottoinsieme aggiornabile e attribuibile. Può fallire per query, indice o ranking. [SRC-66-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui memoria persistente e contesto temporaneo hanno politiche diverse. Da qui possiamo leggere la conseguenza dichiarata da «Retrieval seleziona un sottoinsieme aggiornabile e attribuibile».

Per ricostruire «Quando recuperare» annotiamo l'input «segmento, query, budget e durata», poi l'operazione «routing, scrittura episodica e recupero», infine l'output «contesto scelto, memoria aggiornata e costo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Retrieval seleziona un sottoinsieme aggiornabile e attribuibile».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. Per «Quando recuperare» il controllo cambia una sola premessa della frase «Retrieval seleziona un sottoinsieme aggiornabile e attribuibile» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Retrieval seleziona un sottoinsieme aggiornabile e attribuibile». [SRC-66-003]

Il punto didattico di «Quando recuperare» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «contesto scelto, memoria aggiornata e costo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Quando recuperare» conserva input, operazione e output; poi esplicita quale parte di «Retrieval seleziona un sottoinsieme aggiornabile e attribuibile» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Memoria episodica», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Memoria episodica

Un sistema può salvare fatti o riassunti tra sessioni. Provenienza, consenso, scadenza e correzione diventano parte del contratto. [SRC-66-004]

Per capire «Memoria episodica» partiamo da questo caso: una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale. Il caso rende osservabile il punto centrale: «Un sistema può salvare fatti o riassunti tra sessioni».

Nel contratto locale, l'input «segmento, query, budget e durata» entra, l'operazione «routing, scrittura episodica e recupero» modifica il percorso e l'output «contesto scelto, memoria aggiornata e costo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Memoria episodica»; resta da controllare che memoria persistente e contesto temporaneo hanno politiche diverse. La domanda locale è «Un sistema può salvare fatti o riassunti tra sessioni».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione. La verifica resta ancorata a «Un sistema può salvare fatti o riassunti tra sessioni». [SRC-66-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Provenienza, consenso, scadenza e correzione diventano parte del contratto. Il piccolo risultato resta un'illustrazione di «Un sistema può salvare fatti o riassunti tra sessioni», non una promessa generale.

Per verificare «Memoria episodica» cambiamo una sola condizione vicina alla frase «Un sistema può salvare fatti o riassunti tra sessioni», teniamo fermo il resto e registriamo l'output «contesto scelto, memoria aggiornata e costo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Routing ibrido», riceve l'output «contesto scelto, memoria aggiornata e costo» come base, ma dovrà formulare e verificare la propria distinzione.

## Routing ibrido

Una policy può scegliere cache, contesto, retrieval o memoria. La decisione deve essere misurata rispetto a qualità, latenza e privacy. [SRC-66-001]

Il caso minimo di «Routing ibrido» si presenta così: una query e tre documenti ricevono punteggi distinti. Prima di generare, controlliamo quale documento è entrato nel contesto e con quale ranking. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Una policy può scegliere cache, contesto, retrieval o memoria».

La sezione usa l'input «segmento, query, budget e durata» come punto di partenza e l'output «contesto scelto, memoria aggiornata e costo» come traccia d'uscita. La trasformazione concreta è «routing, scrittura episodica e recupero»; il caso non è completo se non dichiariamo anche che memoria persistente e contesto temporaneo hanno politiche diverse. La condizione da isolare è «Una policy può scegliere cache, contesto, retrieval o memoria».

La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «Una policy può scegliere cache, contesto, retrieval o memoria». [SRC-66-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Routing ibrido» conserviamo l'osservazione collegata a «Una policy può scegliere cache, contesto, retrieval o memoria» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Routing ibrido» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di decisione, tool e side effect. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## La definizione messa alla prova: Tre risorse differenti

Il caso intero parte dall'input «segmento, query, budget e durata», applica l'operazione «routing, scrittura episodica e recupero» e osserva l'output «contesto scelto, memoria aggiornata e costo». Un esempio controllato: un fatto stabile salvato e un dettaglio recente escluso. La formula locale è:

$$
memory_t = update(memory_{t-1}, segment_t)
$$

Memoria e contesto hanno politiche diverse di conservazione e recupero. [SRC-66-001]

![Contesto lungo, retrieval e memoria: loop](../../assets/chapters/66_context_retrieval_memory/MEMORY-02/candidate-v48.png)

La figura MEMORY-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Routing, scrittura episodica e recupero. L'input è segmento, query, budget e durata, l'output è contesto scelto, memoria aggiornata e costo; il vincolo da controllare è che memoria persistente e contesto temporaneo hanno politiche diverse.

## Un esperimento piccolo ma leggibile: Quando usare il contesto

Il file `code/snip_66_contract.py` collega il contratto del capitolo alla frase «Una policy può scegliere cache, contesto, retrieval o memoria». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-66-001.txt` conserva il risultato ripetibile del caso locale.

## Il confine del caso guida: Routing ibrido

Il meccanismo di «Contesto lungo, retrieval e memoria» resta legato al contratto locale. Memoria persistente e contesto temporaneo hanno politiche diverse. Prima di generalizzare la frase «Una policy può scegliere cache, contesto, retrieval o memoria», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## Il contratto che rimane: Contesto lungo, retrieval e memoria

Abbiamo seguito la decisione tra contesto, retrieval e memoria, partendo dall'input «segmento, query, budget e durata» e arrivando all'output «contesto scelto, memoria aggiornata e costo». Le sezioni «Tre risorse differenti», «Quando usare il contesto», «Routing ibrido» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: memoria persistente e contesto temporaneo hanno politiche diverse. Il Capitolo 67, Output strutturato e uso degli strumenti, può partire da questo output e dichiarare la propria domanda.

### Controllo finale della lezione: Tre risorse differenti

1. Ricostruisci l'oggetto continuo a partire da «Tre risorse differenti» e indica quale parte della frase «Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti» entra nel caso.
2. Spiega quale trasformazione collega «Tre risorse differenti» a «Routing ibrido» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: memoria persistente e contesto temporaneo hanno politiche diverse.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Una policy può scegliere cache, contesto, retrieval o memoria» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Prove da rifare e modificare: Routing ibrido

1. Ricostruisci input e output di «Tre risorse differenti» usando un esempio di tre righe.
2. Modifica una sola variabile in «Quando usare il contesto» e anticipa l'invariante che dovrebbe restare.
3. Metti «Quando recuperare» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Memoria episodica».
5. Formula per «Routing ibrido» una domanda che separi meccanismo e qualità del sistema.

## Riferimenti e prove riproducibili: Contesto lungo, retrieval e memoria

Il dossier di «Contesto lungo, retrieval e memoria» in `FONTI_PRIMARIE.md` separa definizioni, risultati e il confine tra informazione e azione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a decisione, tool e side effect.
