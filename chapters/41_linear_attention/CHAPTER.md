<!--
chapter_id: CH-P08-LINEAR-ATTENTION
part_id: P08
order_key: 410
title: Linear attention, fast weights e delta rule
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 41. Linear attention, fast weights e delta rule

Finora abbiamo potuto descrivere uno stato causale che sostituisce il prodotto quadratico. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo 41 prendiamo l'input «sequenza x_t, kernel fattorizzabile e stato» e lo seguiamo fino all'output «h_t e predizione con costo dichiarato», dichiarando prima il contratto e poi il limite.

## Kernel fattorizzabile

Una feature map permette di riassociare i prodotti senza una matrice completa di score. [SRC-41-001]

Prima del nome tecnico fissiamo la situazione: consideriamo la stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end. Da qui possiamo leggere la conseguenza dichiarata da «Una feature map permette di riassociare i prodotti senza una matrice completa di score».

La sezione usa l'input «sequenza x_t, kernel fattorizzabile e stato» come punto di partenza e l'output «h_t e predizione con costo dichiarato» come traccia d'uscita. La trasformazione concreta è «recurrence, normalizzazione e fast weights»; il caso non è completo se non dichiariamo anche che la fattorizzazione cambia memoria e capacità di interazione. La condizione da isolare è «Una feature map permette di riassociare i prodotti senza una matrice completa di score».

Il compiler abbassa un grafo in operazioni del backend e può fondere, riordinare o specializzare i kernel. Correttezza numerica e velocità sono controlli distinti e dipendono dal target hardware. La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel. La verifica resta ancorata a «Una feature map permette di riassociare i prodotti senza una matrice completa di score». [SRC-41-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Kernel fattorizzabile» conserviamo l'osservazione collegata a «Una feature map permette di riassociare i prodotti senza una matrice completa di score» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Kernel fattorizzabile» conserva input, operazione e output; poi esplicita quale parte di «Una feature map permette di riassociare i prodotti senza una matrice completa di score» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Recurrence causale», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Recurrence causale

Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza. [SRC-41-002]

Per capire «Recurrence causale» partiamo da questo caso: una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile. Il caso rende osservabile il punto centrale: «Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza».

Per ricostruire «Recurrence causale» annotiamo l'input «sequenza x_t, kernel fattorizzabile e stato», poi l'operazione «recurrence, normalizzazione e fast weights», infine l'output «h_t e predizione con costo dichiarato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza».

La forma fattorizzata sostituisce parte della matrice di interazioni con uno stato aggiornato. Il vantaggio dipende da ciò che lo stato conserva, dalla stabilità della normalizzazione e dalla dipendenza dalla lunghezza della sequenza. Per «Recurrence causale» il controllo cambia una sola premessa della frase «Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza». [SRC-41-002]

Il punto didattico di «Recurrence causale» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «h_t e predizione con costo dichiarato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Recurrence causale» cambiamo una sola condizione vicina alla frase «Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza», teniamo fermo il resto e registriamo l'output «h_t e predizione con costo dichiarato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Normalizzazione», riceve l'output «h_t e predizione con costo dichiarato» come base, ma dovrà formulare e verificare la propria distinzione.

## Normalizzazione

Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti. [SRC-41-003]

Il caso minimo di «Normalizzazione» si presenta così: due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Normalizzazione». Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti».

Nel contratto locale, l'input «sequenza x_t, kernel fattorizzabile e stato» entra, l'operazione «recurrence, normalizzazione e fast weights» modifica il percorso e l'output «h_t e predizione con costo dichiarato» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Normalizzazione»; resta da controllare che la fattorizzazione cambia memoria e capacità di interazione. La domanda locale è «Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti».

Il punto operativo è la scala del segnale: inizializzazione, normalizzazione, residual e regolarizzazione intervengono in momenti diversi e non sono sostituti intercambiabili. Shape compatibili e curve osservate servono a controllare il percorso reale. Per «Normalizzazione» il controllo cambia una sola premessa della frase «Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti». [SRC-41-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti», non una promessa generale.

Il controllo minimo di «Normalizzazione» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Normalizzazione» portiamo l'output «h_t e predizione con costo dichiarato»; non portiamo invece una conclusione oltre il caso locale.

## Fast weights

Lo stato può essere letto come memoria associativa che accumula coppie key-value. [SRC-41-004]

Prima del nome tecnico fissiamo la situazione: consideriamo un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Da qui possiamo leggere la conseguenza dichiarata da «Lo stato può essere letto come memoria associativa che accumula coppie key-value».

La sezione usa l'input «sequenza x_t, kernel fattorizzabile e stato» come punto di partenza e l'output «h_t e predizione con costo dichiarato» come traccia d'uscita. La trasformazione concreta è «recurrence, normalizzazione e fast weights»; il caso non è completo se non dichiariamo anche che la fattorizzazione cambia memoria e capacità di interazione. La condizione da isolare è «Lo stato può essere letto come memoria associativa che accumula coppie key-value».

La forma fattorizzata sostituisce parte della matrice di interazioni con uno stato aggiornato. Il vantaggio dipende da ciò che lo stato conserva, dalla stabilità della normalizzazione e dalla dipendenza dalla lunghezza della sequenza. Per «Fast weights» il controllo cambia una sola premessa della frase «Lo stato può essere letto come memoria associativa che accumula coppie key-value» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Lo stato può essere letto come memoria associativa che accumula coppie key-value». [SRC-41-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Fast weights» conserviamo l'osservazione collegata a «Lo stato può essere letto come memoria associativa che accumula coppie key-value» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Fast weights» conserva input, operazione e output; poi esplicita quale parte di «Lo stato può essere letto come memoria associativa che accumula coppie key-value» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Delta rule», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Linear attention, fast weights e delta rule: compare](../../assets/chapters/41_linear_attention/LINATT-01/candidate-v47.png)

La figura LINATT-01 usa la famiglia compare. Il diagramma segue il passaggio: Recurrence, normalizzazione e fast weights. L'input è sequenza x_t, kernel fattorizzabile e stato, l'output è h_t e predizione con costo dichiarato; il vincolo da controllare è che la fattorizzazione cambia memoria e capacità di interazione.

## Delta rule

L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca. [SRC-41-001]

Per capire «Delta rule» partiamo da questo caso: un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Il caso rende osservabile il punto centrale: «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca».

Per ricostruire «Delta rule» annotiamo l'input «sequenza x_t, kernel fattorizzabile e stato», poi l'operazione «recurrence, normalizzazione e fast weights», infine l'output «h_t e predizione con costo dichiarato». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca».

La forma fattorizzata sostituisce parte della matrice di interazioni con uno stato aggiornato. Il vantaggio dipende da ciò che lo stato conserva, dalla stabilità della normalizzazione e dalla dipendenza dalla lunghezza della sequenza. Per «Delta rule» il controllo cambia una sola premessa della frase «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca». [SRC-41-001]

Il punto didattico di «Delta rule» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «h_t e predizione con costo dichiarato» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Delta rule» cambiamo una sola condizione vicina alla frase «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca», teniamo fermo il resto e registriamo l'output «h_t e predizione con costo dichiarato». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Il contratto in un caso piccolo: Kernel fattorizzabile

Il caso intero parte dall'input «sequenza x_t, kernel fattorizzabile e stato», applica l'operazione «recurrence, normalizzazione e fast weights» e osserva l'output «h_t e predizione con costo dichiarato». Un esempio controllato: tre aggiornamenti causali con stato scalare. La formula locale è:

$$
h_t = h_{t-1} + phi(x_t)
$$

Una forma fattorizzata sostituisce una matrice completa con uno stato aggiornato. [SRC-41-001]

![Linear attention, fast weights e delta rule: timeline](../../assets/chapters/41_linear_attention/LINATT-02/candidate-v47.png)

La figura LINATT-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Recurrence, normalizzazione e fast weights. L'input è sequenza x_t, kernel fattorizzabile e stato, l'output è h_t e predizione con costo dichiarato; il vincolo da controllare è che la fattorizzazione cambia memoria e capacità di interazione.

## Dalla trasformazione al test: Recurrence causale

Lo snippet locale mette in esecuzione questo caso: tre aggiornamenti causali con stato scalare. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-41-001.txt`, come evidenza locale e non come benchmark di produzione.

## Il perimetro della conclusione: Delta rule

Il caso di «Linear attention, fast weights e delta rule» non certifica un servizio completo. La fattorizzazione cambia memoria e capacità di interazione. La domanda successiva è se «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca» regga quando cambiano dati, scala, hardware o criteri di decisione.

## Una sintesi operativa: Linear attention, fast weights e delta rule

Il filo della lezione va dall'input «sequenza x_t, kernel fattorizzabile e stato» all'output «h_t e predizione con costo dichiarato». Nei passaggi «Kernel fattorizzabile», «Recurrence causale», «Delta rule» abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione. L'invariante da portare avanti è: la fattorizzazione cambia memoria e capacità di interazione. Il Capitolo 42, State-space model, recurrence e long convolution, può partire da questo output e dichiarare la propria domanda.

### Domande per il lettore: Kernel fattorizzabile

1. Ricostruisci l'oggetto continuo a partire da «Kernel fattorizzabile» e indica quale parte della frase «Una feature map permette di riassociare i prodotti senza una matrice completa di score» entra nel caso.
2. Spiega quale trasformazione collega «Kernel fattorizzabile» a «Delta rule» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: la fattorizzazione cambia memoria e capacità di interazione.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di ricostruzione: Delta rule

1. Racconta «Kernel fattorizzabile» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Recurrence causale» mantenendo il resto del setup invariato.
3. Per «Normalizzazione», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Fast weights» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Delta rule» senza confondere livelli diversi.

## Materiali, fonti e codice verificato: Linear attention, fast weights e delta rule

Per ricontrollare «Linear attention, fast weights e delta rule», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire il vincolo che impedisce di leggere il futuro oltre il caso locale, con la data di consultazione dichiarata. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
