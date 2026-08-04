<!--
chapter_id: CH-P10-VIDEO
part_id: P10
order_key: 600
title: Generazione video
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 60. Generazione video

Il Capitolo 59, Audio, parlato e musica, ha lasciato disponibile una sequenza di frame condizionata nel tempo. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «denoising, autoregressione e controllo temporale» e verifichiamo che qualità del singolo frame non dimostra coerenza tra frame.

## Spazio e tempo

Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono conservare movimento e identità. [SRC-60-001]

Per capire «Spazio e tempo» partiamo da questo caso: tre frame condividono una condizione e conservano l'ordine temporale. Il caso rende osservabile il punto centrale: «Un video aggiunge una dimensione temporale alle immagini».

Nel contratto locale, l'input «frame, latent video, testo e timestamp» entra, l'operazione «denoising, autoregressione e controllo temporale» modifica il percorso e l'output «frame coerenti e misura di flicker» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Spazio e tempo»; resta da controllare che qualità del singolo frame non dimostra coerenza tra frame. La domanda locale è «Un video aggiunge una dimensione temporale alle immagini».

Il passaggio da seguire in «Spazio e tempo» è quello descritto dalla frase «Un video aggiunge una dimensione temporale alle immagini»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Spazio e tempo» il controllo cambia una sola premessa della frase «Un video aggiunge una dimensione temporale alle immagini» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un video aggiunge una dimensione temporale alle immagini». [SRC-60-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Token, patch o latent devono conservare movimento e identità. Il piccolo risultato resta un'illustrazione di «Un video aggiunge una dimensione temporale alle immagini», non una promessa generale.

Per verificare «Spazio e tempo» cambiamo una sola condizione vicina alla frase «Un video aggiunge una dimensione temporale alle immagini», teniamo fermo il resto e registriamo l'output «frame coerenti e misura di flicker». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Video diffusion», riceve l'output «frame coerenti e misura di flicker» come base, ma dovrà formulare e verificare la propria distinzione.

## Video diffusion

Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata e convoluzioni riducono il costo. [SRC-60-002]

Il caso minimo di «Video diffusion» si presenta così: due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Il denoiser opera su tensori spazio-temporali o latent compressi».

La sezione usa l'input «frame, latent video, testo e timestamp» come punto di partenza e l'output «frame coerenti e misura di flicker» come traccia d'uscita. La trasformazione concreta è «denoising, autoregressione e controllo temporale»; il caso non è completo se non dichiariamo anche che qualità del singolo frame non dimostra coerenza tra frame. La condizione da isolare è «Il denoiser opera su tensori spazio-temporali o latent compressi».

Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale. Per «Video diffusion» il controllo cambia una sola premessa della frase «Il denoiser opera su tensori spazio-temporali o latent compressi» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il denoiser opera su tensori spazio-temporali o latent compressi». [SRC-60-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Video diffusion» conserviamo l'osservazione collegata a «Il denoiser opera su tensori spazio-temporali o latent compressi» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Video diffusion» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «Video diffusion» portiamo l'output «frame coerenti e misura di flicker»; non portiamo invece una conclusione oltre il caso locale.

![Generazione video: timeline](../../assets/chapters/60_video/VIDEO-01/candidate-v48.png)

La figura VIDEO-01 usa la famiglia timeline. Il diagramma segue il passaggio: Denoising, autoregressione e controllo temporale. L'input è frame, latent video, testo e timestamp, l'output è frame coerenti e misura di flicker; il vincolo da controllare è che qualità del singolo frame non dimostra coerenza tra frame.

## Autoregressione

Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica dipendenze e cache. [SRC-60-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente. Da qui possiamo leggere la conseguenza dichiarata da «Frame, patch o token video possono essere generati in ordine».

Per ricostruire «Autoregressione» annotiamo l'input «frame, latent video, testo e timestamp», poi l'operazione «denoising, autoregressione e controllo temporale», infine l'output «frame coerenti e misura di flicker». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Frame, patch o token video possono essere generati in ordine».

Il passaggio da seguire in «Autoregressione» è quello descritto dalla frase «Frame, patch o token video possono essere generati in ordine»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference. La verifica resta ancorata a «Frame, patch o token video possono essere generati in ordine». [SRC-60-003]

Il punto didattico di «Autoregressione» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «frame coerenti e misura di flicker» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Autoregressione» conserva input, operazione e output; poi esplicita quale parte di «Frame, patch o token video possono essere generati in ordine» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Coerenza», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Coerenza

Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame. [SRC-60-004]

Per capire «Coerenza» partiamo da questo caso: due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Il caso rende osservabile il punto centrale: «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame».

Nel contratto locale, l'input «frame, latent video, testo e timestamp» entra, l'operazione «denoising, autoregressione e controllo temporale» modifica il percorso e l'output «frame coerenti e misura di flicker» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Coerenza»; resta da controllare che qualità del singolo frame non dimostra coerenza tra frame. La domanda locale è «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame».

Il passaggio da seguire in «Coerenza» è quello descritto dalla frase «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Coerenza» il controllo cambia una sola premessa della frase «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame». [SRC-60-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame», non una promessa generale.

Per verificare «Coerenza» cambiamo una sola condizione vicina alla frase «Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame», teniamo fermo il resto e registriamo l'output «frame coerenti e misura di flicker». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Condizionamento e editing», riceve l'output «frame coerenti e misura di flicker» come base, ma dovrà formulare e verificare la propria distinzione.

## Condizionamento e editing

Testo, immagine iniziale, traiettoria o maschere guidano il video. Il controllo deve essere valutato nel tempo. [SRC-60-001]

Il caso minimo di «Condizionamento e editing» si presenta così: due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Testo, immagine iniziale, traiettoria o maschere guidano il video».

La sezione usa l'input «frame, latent video, testo e timestamp» come punto di partenza e l'output «frame coerenti e misura di flicker» come traccia d'uscita. La trasformazione concreta è «denoising, autoregressione e controllo temporale»; il caso non è completo se non dichiariamo anche che qualità del singolo frame non dimostra coerenza tra frame. La condizione da isolare è «Testo, immagine iniziale, traiettoria o maschere guidano il video».

Il passaggio da seguire in «Condizionamento e editing» è quello descritto dalla frase «Testo, immagine iniziale, traiettoria o maschere guidano il video»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Condizionamento e editing» il controllo cambia una sola premessa della frase «Testo, immagine iniziale, traiettoria o maschere guidano il video» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Testo, immagine iniziale, traiettoria o maschere guidano il video». [SRC-60-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Condizionamento e editing» conserviamo l'osservazione collegata a «Testo, immagine iniziale, traiettoria o maschere guidano il video» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Condizionamento e editing» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Il caso minimo e la sua variante: Spazio e tempo

Il caso intero parte dall'input «frame, latent video, testo e timestamp», applica l'operazione «denoising, autoregressione e controllo temporale» e osserva l'output «frame coerenti e misura di flicker». Un esempio controllato: tre frame con un oggetto che deve mantenere posizione. Lo schema compatto è:

$$
frames = decode(z_video, t)
$$

È una notazione di interfaccia, non un'identità numerica completa. Una sequenza video aggiunge asse temporale e coerenza tra frame. [SRC-60-001]

![Generazione video: pipeline](../../assets/chapters/60_video/VIDEO-02/candidate-v48.png)

La figura VIDEO-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Denoising, autoregressione e controllo temporale. L'input è frame, latent video, testo e timestamp, l'output è frame coerenti e misura di flicker; il vincolo da controllare è che qualità del singolo frame non dimostra coerenza tra frame.

## Che cosa osserva lo snippet: Video diffusion

Il file `code/snip_60_contract.py` collega il contratto del capitolo alla frase «Testo, immagine iniziale, traiettoria o maschere guidano il video». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-60-001.txt` conserva il risultato ripetibile del caso locale.

## Che cosa non dimostra: Condizionamento e editing

Il meccanismo di «Generazione video» resta legato al contratto locale. Qualità del singolo frame non dimostra coerenza tra frame. Prima di generalizzare la frase «Testo, immagine iniziale, traiettoria o maschere guidano il video», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.

## La mappa delle condizioni: Generazione video

Abbiamo seguito una sequenza di frame condizionata nel tempo, partendo dall'input «frame, latent video, testo e timestamp» e arrivando all'output «frame coerenti e misura di flicker». Le sezioni «Spazio e tempo», «Video diffusion», «Condizionamento e editing» hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo. L'invariante da portare avanti è: qualità del singolo frame non dimostra coerenza tra frame. Il Capitolo 61, 3D, spazio e rappresentazione delle scene, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Spazio e tempo

1. Ricostruisci l'oggetto continuo a partire da «Spazio e tempo» e indica quale parte della frase «Un video aggiunge una dimensione temporale alle immagini» entra nel caso.
2. Spiega quale trasformazione collega «Spazio e tempo» a «Condizionamento e editing» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: qualità del singolo frame non dimostra coerenza tra frame.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Testo, immagine iniziale, traiettoria o maschere guidano il video» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Condizionamento e editing

1. Racconta «Spazio e tempo» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Video diffusion» mantenendo il resto del setup invariato.
3. Per «Autoregressione», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «Coerenza» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Condizionamento e editing» senza confondere livelli diversi.

## Fonti e risultati locali: Generazione video

Il dossier di «Generazione video» in `FONTI_PRIMARIE.md` separa definizioni, risultati e sincronizzazione, rappresentazione e fusione; la data di consultazione è registrata accanto ai riferimenti. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a allineamento tra modalità.
