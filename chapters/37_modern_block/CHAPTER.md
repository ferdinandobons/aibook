<!--
chapter_id: CH-P08-MODERN-BLOCK
part_id: P08
order_key: 370
title: Anatomia del blocco moderno
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 37. Anatomia del blocco moderno

Il risultato precedente non è ancora una soluzione completa. Partiamo da un residual stream dentro un blocco moderno e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «h' con shape preservata e statistiche confrontabili» isoliamo il passaggio «norm, attention, MLP e gating nell'ordine scelto» e ne misuriamo il limite prima di passare a Posizione e contesto lungo.

## Residual stream

Ogni sottolayer produce un aggiornamento sommato a un percorso identità. [SRC-37-001]

Il caso minimo di «Residual stream» si presenta così: due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Residual stream». Non lo usiamo come decorazione: serve a rendere osservabile la frase «Ogni sottolayer produce un aggiornamento sommato a un percorso identità».

Per ricostruire «Residual stream» annotiamo l'input «h di shape [batch, length, d] e norma misurata», poi l'operazione «norm, attention, MLP e gating nell'ordine scelto», infine l'output «h' con shape preservata e statistiche confrontabili». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Ogni sottolayer produce un aggiornamento sommato a un percorso identità».

Il punto operativo è la scala del segnale: inizializzazione, normalizzazione, residual e regolarizzazione intervengono in momenti diversi e non sono sostituti intercambiabili. Shape compatibili e curve osservate servono a controllare il percorso reale. Per «Residual stream» il controllo cambia una sola premessa della frase «Ogni sottolayer produce un aggiornamento sommato a un percorso identità» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ogni sottolayer produce un aggiornamento sommato a un percorso identità». [SRC-37-001]

Il punto didattico di «Residual stream» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «h' con shape preservata e statistiche confrontabili» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Residual stream» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Residual stream» portiamo l'output «h' con shape preservata e statistiche confrontabili»; non portiamo invece una conclusione oltre il caso locale.

## Pre-norm e post-norm

La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco. [SRC-37-002]

Prima del nome tecnico fissiamo la situazione: consideriamo pre-norm e residuale su un vettore di due coordinate. Da qui possiamo leggere la conseguenza dichiarata da «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco».

Nel contratto locale, l'input «h di shape [batch, length, d] e norma misurata» entra, l'operazione «norm, attention, MLP e gating nell'ordine scelto» modifica il percorso e l'output «h' con shape preservata e statistiche confrontabili» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Pre-norm e post-norm»; resta da controllare che ordine dei sottolayer e shape sono parte del blocco. La domanda locale è «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco».

Questa variante cambia un punto preciso del blocco o del segnale posizionale. Per confrontarla bisogna fissare ordine, shape, mask e condizioni di training, altrimenti si attribuisce alla variante una differenza nata dal setup. Per «Pre-norm e post-norm» il controllo cambia una sola premessa della frase «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco». [SRC-37-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco», non una promessa generale.

La prova di «Pre-norm e post-norm» conserva input, operazione e output; poi esplicita quale parte di «La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «RMSNorm», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## RMSNorm

RMSNorm scala usando la media quadratica e non sottrae la media. [SRC-37-003]

Per capire «RMSNorm» partiamo da questo caso: un caso in cui ordine dei sottolayer e shape sono parte del blocco. Il caso rende osservabile il punto centrale: «RMSNorm scala usando la media quadratica e non sottrae la media».

La sezione usa l'input «h di shape [batch, length, d] e norma misurata» come punto di partenza e l'output «h' con shape preservata e statistiche confrontabili» come traccia d'uscita. La trasformazione concreta è «norm, attention, MLP e gating nell'ordine scelto»; il caso non è completo se non dichiariamo anche che ordine dei sottolayer e shape sono parte del blocco. La condizione da isolare è «RMSNorm scala usando la media quadratica e non sottrae la media».

Questa variante cambia un punto preciso del blocco o del segnale posizionale. Per confrontarla bisogna fissare ordine, shape, mask e condizioni di training, altrimenti si attribuisce alla variante una differenza nata dal setup. Per «RMSNorm» il controllo cambia una sola premessa della frase «RMSNorm scala usando la media quadratica e non sottrae la media» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «RMSNorm scala usando la media quadratica e non sottrae la media». [SRC-37-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «RMSNorm» conserviamo l'osservazione collegata a «RMSNorm scala usando la media quadratica e non sottrae la media» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «RMSNorm» cambiamo una sola condizione vicina alla frase «RMSNorm scala usando la media quadratica e non sottrae la media», teniamo fermo il resto e registriamo l'output «h' con shape preservata e statistiche confrontabili». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «SwiGLU», riceve l'output «h' con shape preservata e statistiche confrontabili» come base, ma dovrà formulare e verificare la propria distinzione.

![Anatomia del blocco moderno: matrix](../../assets/chapters/37_modern_block/BLOCK-01/candidate-v47.png)

La figura BLOCK-01 usa la famiglia matrix. Il diagramma segue il passaggio: Norm, attention, MLP e gating nell'ordine scelto. L'input è h di shape [batch, length, d] e norma misurata, l'output è h' con shape preservata e statistiche confrontabili; il vincolo da controllare è che ordine dei sottolayer e shape sono parte del blocco.

## SwiGLU

Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down. [SRC-37-004]

Il caso minimo di «SwiGLU» si presenta così: un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down».

Per ricostruire «SwiGLU» annotiamo l'input «h di shape [batch, length, d] e norma misurata», poi l'operazione «norm, attention, MLP e gating nell'ordine scelto», infine l'output «h' con shape preservata e statistiche confrontabili». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down».

Questa variante cambia un punto preciso del blocco o del segnale posizionale. Per confrontarla bisogna fissare ordine, shape, mask e condizioni di training, altrimenti si attribuisce alla variante una differenza nata dal setup. Per «SwiGLU» il controllo cambia una sola premessa della frase «Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down». [SRC-37-004]

Il punto didattico di «SwiGLU» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «h' con shape preservata e statistiche confrontabili» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «SwiGLU» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «SwiGLU» portiamo l'output «h' con shape preservata e statistiche confrontabili»; non portiamo invece una conclusione oltre il caso locale.

## Ordine e parallelismo

Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine. [SRC-37-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Da qui possiamo leggere la conseguenza dichiarata da «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine».

Nel contratto locale, l'input «h di shape [batch, length, d] e norma misurata» entra, l'operazione «norm, attention, MLP e gating nell'ordine scelto» modifica il percorso e l'output «h' con shape preservata e statistiche confrontabili» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Ordine e parallelismo»; resta da controllare che ordine dei sottolayer e shape sono parte del blocco. La domanda locale è «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine».

Questa variante cambia un punto preciso del blocco o del segnale posizionale. Per confrontarla bisogna fissare ordine, shape, mask e condizioni di training, altrimenti si attribuisce alla variante una differenza nata dal setup. Per «Ordine e parallelismo» il controllo cambia una sola premessa della frase «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine». [SRC-37-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine», non una promessa generale.

La prova di «Ordine e parallelismo» conserva input, operazione e output; poi esplicita quale parte di «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «h' con shape preservata e statistiche confrontabili» come evidenza locale e conserva il vincolo che impedisce di leggere il futuro come domanda aperta.

## Dal concetto alla situazione concreta: Residual stream

Il caso intero parte dall'input «h di shape [batch, length, d] e norma misurata», applica l'operazione «norm, attention, MLP e gating nell'ordine scelto» e osserva l'output «h' con shape preservata e statistiche confrontabili». Un esempio controllato: pre-norm e residuale su un vettore di due coordinate. La formula locale è:

$$
h' = h + MLP(Norm(h))
$$

La posizione della norm e il percorso residuale sono parte del contratto del blocco. [SRC-37-001]

![Anatomia del blocco moderno: architecture](../../assets/chapters/37_modern_block/BLOCK-02/candidate-v47.png)

La figura BLOCK-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Norm, attention, MLP e gating nell'ordine scelto. L'input è h di shape [batch, length, d] e norma misurata, l'output è h' con shape preservata e statistiche confrontabili; il vincolo da controllare è che ordine dei sottolayer e shape sono parte del blocco.

## Una prova ripetibile: Pre-norm e post-norm

Nel run Python rendiamo osservabile la frase «Ogni sottolayer produce un aggiornamento sommato a un percorso identità» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-37-001.txt` documenta il caso senza pretendere una misura generale.

## Il trasferimento richiede altro: Ordine e parallelismo

Il meccanismo di «Anatomia del blocco moderno» non garantisce da solo che il sistema funzioni fuori dal caso guida. Ordine dei sottolayer e shape sono parte del blocco. Il limite osservato riguarda la frase «Ogni sottolayer produce un aggiornamento sommato a un percorso identità»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il filo che passa oltre: Anatomia del blocco moderno

Il percorso ha tenuto insieme un residual stream dentro un blocco moderno, l'operazione «norm, attention, MLP e gating nell'ordine scelto» e l'output «h' con shape preservata e statistiche confrontabili». Le sezioni «Residual stream», «Pre-norm e post-norm», «Ordine e parallelismo» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: ordine dei sottolayer e shape sono parte del blocco. Il Capitolo 38, Posizione e contesto lungo, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Residual stream

1. Ricostruisci l'oggetto continuo a partire da «Residual stream» e indica quale parte della frase «Ogni sottolayer produce un aggiornamento sommato a un percorso identità» entra nel caso.
2. Spiega quale trasformazione collega «Residual stream» a «Ordine e parallelismo» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: ordine dei sottolayer e shape sono parte del blocco.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Ordine e parallelismo

1. Ricostruisci input e output di «Residual stream» usando un esempio di tre righe.
2. Modifica una sola variabile in «Pre-norm e post-norm» e anticipa l'invariante che dovrebbe restare.
3. Metti «RMSNorm» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «SwiGLU».
5. Formula per «Ordine e parallelismo» una domanda che separi meccanismo e qualità del sistema.

## Dove verificare definizioni e risultati: Anatomia del blocco moderno

Per «Anatomia del blocco moderno», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
