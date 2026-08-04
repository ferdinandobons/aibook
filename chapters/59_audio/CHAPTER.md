<!--
chapter_id: CH-P10-AUDIO
part_id: P10
order_key: 590
title: Audio, parlato e musica
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 59. Audio, parlato e musica

Una frase plausibile non basta a spiegare audio, parlato e musica. L'oggetto è un segnale audio e la sua rappresentazione discreta; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Waveform e spettrogramma

Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti. [SRC-59-001]

Prima del nome tecnico fissiamo la situazione: consideriamo quattro campioni audio vengono divisi in due frame senza cambiare l'ordine temporale. Da qui possiamo leggere la conseguenza dichiarata da «Il segnale audio è campionato nel tempo».

La sezione usa l'input «waveform, sample rate, spettrogramma o codec» come punto di partenza e l'output «testo, waveform o token audio» come traccia d'uscita. La trasformazione concreta è «ASR, TTS, codec e generazione»; il caso non è completo se non dichiariamo anche che sample rate e durata fanno parte del contratto. La condizione da isolare è «Il segnale audio è campionato nel tempo».

Il passaggio da seguire in «Waveform e spettrogramma» è quello descritto dalla frase «Il segnale audio è campionato nel tempo»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Waveform e spettrogramma» il controllo cambia una sola premessa della frase «Il segnale audio è campionato nel tempo» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il segnale audio è campionato nel tempo». [SRC-59-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Waveform e spettrogramma» conserviamo l'osservazione collegata a «Il segnale audio è campionato nel tempo» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Waveform e spettrogramma» conserva input, operazione e output; poi esplicita quale parte di «Il segnale audio è campionato nel tempo» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «ASR», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## ASR

Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi. [SRC-59-002]

Per capire «ASR» partiamo da questo caso: una breve waveform convertita in frame e token. Il caso rende osservabile il punto centrale: «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer».

Per ricostruire «ASR» annotiamo l'input «waveform, sample rate, spettrogramma o codec», poi l'operazione «ASR, TTS, codec e generazione», infine l'output «testo, waveform o token audio». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer».

Il passaggio da seguire in «ASR» è quello descritto dalla frase «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «ASR» il controllo cambia una sola premessa della frase «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer». [SRC-59-002]

Il punto didattico di «ASR» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «testo, waveform o token audio» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «ASR» cambiamo una sola condizione vicina alla frase «Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer», teniamo fermo il resto e registriamo l'output «testo, waveform o token audio». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «TTS», riceve l'output «testo, waveform o token audio» come base, ma dovrà formulare e verificare la propria distinzione.

## TTS

Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti. [SRC-59-003]

Il caso minimo di «TTS» si presenta così: un caso in cui sample rate e durata fanno parte del contratto. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Sintesi vocale trasforma testo in acoustic representation e waveform».

Nel contratto locale, l'input «waveform, sample rate, spettrogramma o codec» entra, l'operazione «ASR, TTS, codec e generazione» modifica il percorso e l'output «testo, waveform o token audio» è ciò che osserviamo. Qui cambia soprattutto il passaggio «TTS»; resta da controllare che sample rate e durata fanno parte del contratto. La domanda locale è «Sintesi vocale trasforma testo in acoustic representation e waveform».

Il passaggio da seguire in «TTS» è quello descritto dalla frase «Sintesi vocale trasforma testo in acoustic representation e waveform»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «TTS» il controllo cambia una sola premessa della frase «Sintesi vocale trasforma testo in acoustic representation e waveform» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Sintesi vocale trasforma testo in acoustic representation e waveform». [SRC-59-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Durata, prosodia e vocoder sono componenti distinti. Il piccolo risultato resta un'illustrazione di «Sintesi vocale trasforma testo in acoustic representation e waveform», non una promessa generale.

Il controllo minimo di «TTS» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «TTS» portiamo l'output «testo, waveform o token audio»; non portiamo invece una conclusione oltre il caso locale.

## Neural codec

Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model. [SRC-59-004]

Prima del nome tecnico fissiamo la situazione: consideriamo due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Da qui possiamo leggere la conseguenza dichiarata da «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model».

La sezione usa l'input «waveform, sample rate, spettrogramma o codec» come punto di partenza e l'output «testo, waveform o token audio» come traccia d'uscita. La trasformazione concreta è «ASR, TTS, codec e generazione»; il caso non è completo se non dichiariamo anche che sample rate e durata fanno parte del contratto. La condizione da isolare è «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Neural codec» il controllo cambia una sola premessa della frase «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model». [SRC-59-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Neural codec» conserviamo l'osservazione collegata a «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Neural codec» conserva input, operazione e output; poi esplicita quale parte di «Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Musica e dialogo», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Audio, parlato e musica: timeline](../../assets/chapters/59_audio/AUDIO-01/candidate-v48.png)

La figura AUDIO-01 usa la famiglia timeline. Il diagramma segue il passaggio: ASR, TTS, codec e generazione. L'input è waveform, sample rate, spettrogramma o codec, l'output è testo, waveform o token audio; il vincolo da controllare è che sample rate e durata fanno parte del contratto.

## Musica e dialogo

Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche. [SRC-59-001]

Per capire «Musica e dialogo» partiamo da questo caso: due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione. Il caso rende osservabile il punto centrale: «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche».

Per ricostruire «Musica e dialogo» annotiamo l'input «waveform, sample rate, spettrogramma o codec», poi l'operazione «ASR, TTS, codec e generazione», infine l'output «testo, waveform o token audio». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche».

Il passaggio da seguire in «Musica e dialogo» è quello descritto dalla frase «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Musica e dialogo» il controllo cambia una sola premessa della frase «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche». [SRC-59-001]

Il punto didattico di «Musica e dialogo» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «testo, waveform o token audio» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Musica e dialogo» cambiamo una sola condizione vicina alla frase «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche», teniamo fermo il resto e registriamo l'output «testo, waveform o token audio». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Un caso dall'input all'output: Waveform e spettrogramma

Il caso intero parte dall'input «waveform, sample rate, spettrogramma o codec», applica l'operazione «ASR, TTS, codec e generazione» e osserva l'output «testo, waveform o token audio». Un esempio controllato: una breve waveform convertita in frame e token. Lo schema compatto è:

$$
wave = decode(tokens, sample_rate)
$$

È una notazione di interfaccia, non un'identità numerica completa. Sample rate, token e durata fanno parte del contratto dell'audio. [SRC-59-001]

![Audio, parlato e musica: pipeline](../../assets/chapters/59_audio/AUDIO-02/candidate-v48.png)

La figura AUDIO-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: ASR, TTS, codec e generazione. L'input è waveform, sample rate, spettrogramma o codec, l'output è testo, waveform o token audio; il vincolo da controllare è che sample rate e durata fanno parte del contratto.

## Dal meccanismo alla prova locale: ASR

Nel run Python rendiamo osservabile la frase «Il segnale audio è campionato nel tempo» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-59-001.txt` documenta il caso senza pretendere una misura generale.

## Dove il risultato si ferma: Musica e dialogo

Il meccanismo di «Audio, parlato e musica» non garantisce da solo che il sistema funzioni fuori dal caso guida. Sample rate e durata fanno parte del contratto. Il limite osservato riguarda la frase «Il segnale audio è campionato nel tempo»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Che cosa portiamo avanti: Audio, parlato e musica

Il percorso ha tenuto insieme un segnale audio e la sua rappresentazione discreta, l'operazione «ASR, TTS, codec e generazione» e l'output «testo, waveform o token audio». Le sezioni «Waveform e spettrogramma», «ASR», «Musica e dialogo» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: sample rate e durata fanno parte del contratto. Il Capitolo 60, Generazione video, può partire da questo output e dichiarare la propria domanda.

### Verifica di comprensione: Waveform e spettrogramma

1. Ricostruisci l'oggetto continuo a partire da «Waveform e spettrogramma» e indica quale parte della frase «Il segnale audio è campionato nel tempo» entra nel caso.
2. Spiega quale trasformazione collega «Waveform e spettrogramma» a «Musica e dialogo» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: sample rate e durata fanno parte del contratto.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi di trasferimento: Musica e dialogo

1. Ricostruisci «Waveform e spettrogramma» senza usare il nome della tecnica, soltanto con input, operazione e output.
2. Sostituisci una condizione di «ASR» e prevedi che cosa non dovrebbe cambiare.
3. Cerca un controesempio per «TTS» e annota quale ipotesi viene rotta.
4. Trasforma il limite di «Neural codec» in un test ripetibile.
5. Spiega come trasferire «Musica e dialogo» senza portare con sé una promessa non misurata.

## Fonti, codice e materiali: Audio, parlato e musica

Per «Audio, parlato e musica», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto allineamento tra modalità. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a allineamento tra modalità.
