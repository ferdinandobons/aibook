<!--
chapter_id: CH-P09-PREFERENCE-OPT
part_id: P09
order_key: 490
title: Ottimizzazione diretta delle preferenze
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 49. Ottimizzazione diretta delle preferenze

Una frase plausibile non basta a spiegare ottimizzazione diretta delle preferenze. L'oggetto è una coppia chosen-rejected per l'ottimizzazione diretta; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Evitare un reward model esplicito

DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata. [SRC-49-001]

Il caso minimo di «Evitare un reward model esplicito» si presenta così: un margine di policy pari a 0,8, un margine di riferimento pari a 0,2 e beta pari a 0,5 producono un logit di preferenza pari a 0,3. Non lo usiamo come decorazione: serve a rendere osservabile la frase «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata».

Per ricostruire «Evitare un reward model esplicito» annotiamo l'input «prompt, log-probability della policy e riferimento», poi l'operazione «margine DPO, beta e variante offline», infine l'output «loss di preferenza e policy aggiornata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata».

Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta. Per «Evitare un reward model esplicito» il controllo cambia una sola premessa della frase «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata». [SRC-49-001]

Il punto didattico di «Evitare un reward model esplicito» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss di preferenza e policy aggiornata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «Evitare un reward model esplicito» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di target, proxy e comportamento. Da «Evitare un reward model esplicito» portiamo l'output «loss di preferenza e policy aggiornata»; non portiamo invece una conclusione oltre il caso locale.

## Coppie chosen e rejected

Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie. [SRC-49-002]

Prima del nome tecnico fissiamo la situazione: consideriamo margine 0,8 con beta dichiarato e riferimento invariato. Da qui possiamo leggere la conseguenza dichiarata da «Ogni esempio richiede la stessa condizione e due risposte confrontabili».

Nel contratto locale, l'input «prompt, log-probability della policy e riferimento» entra, l'operazione «margine DPO, beta e variante offline» modifica il percorso e l'output «loss di preferenza e policy aggiornata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Coppie chosen e rejected»; resta da controllare che la preferenza osservata non è una verità assoluta. La domanda locale è «Ogni esempio richiede la stessa condizione e due risposte confrontabili».

Il passaggio da seguire in «Coppie chosen e rejected» è quello descritto dalla frase «Ogni esempio richiede la stessa condizione e due risposte confrontabili»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Coppie chosen e rejected» il controllo cambia una sola premessa della frase «Ogni esempio richiede la stessa condizione e due risposte confrontabili» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Ogni esempio richiede la stessa condizione e due risposte confrontabili». [SRC-49-002]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Errori o stili spurii possono diventare scorciatoie. Il piccolo risultato resta un'illustrazione di «Ogni esempio richiede la stessa condizione e due risposte confrontabili», non una promessa generale.

La prova di «Coppie chosen e rejected» conserva input, operazione e output; poi esplicita quale parte di «Ogni esempio richiede la stessa condizione e due risposte confrontabili» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Temperatura beta», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Temperatura beta

Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie. [SRC-49-003]

Per capire «Temperatura beta» partiamo da questo caso: un caso in cui la preferenza osservata non è una verità assoluta. Il caso rende osservabile il punto centrale: «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie».

La sezione usa l'input «prompt, log-probability della policy e riferimento» come punto di partenza e l'output «loss di preferenza e policy aggiornata» come traccia d'uscita. La trasformazione concreta è «margine DPO, beta e variante offline»; il caso non è completo se non dichiariamo anche che la preferenza osservata non è una verità assoluta. La condizione da isolare è «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie».

Il passaggio da seguire in «Temperatura beta» è quello descritto dalla frase «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Temperatura beta» il controllo cambia una sola premessa della frase «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie». [SRC-49-003]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Temperatura beta» conserviamo l'osservazione collegata a «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Per verificare «Temperatura beta» cambiamo una sola condizione vicina alla frase «Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie», teniamo fermo il resto e registriamo l'output «loss di preferenza e policy aggiornata». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «IPO, KTO, ORPO e varianti», riceve l'output «loss di preferenza e policy aggiornata» come base, ma dovrà formulare e verificare la propria distinzione.

![Ottimizzazione diretta delle preferenze: chart](../../assets/chapters/49_preference_opt/OPT-01/candidate-v48.png)

La figura OPT-01 usa la famiglia chart. Il diagramma segue il passaggio: Margine DPO, beta e variante offline. L'input è prompt, log-probability della policy e riferimento, l'output è loss di preferenza e policy aggiornata; il vincolo da controllare è che la preferenza osservata non è una verità assoluta.

## IPO, KTO, ORPO e varianti

Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili. [SRC-49-004]

Il caso minimo di «IPO, KTO, ORPO e varianti» si presenta così: due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Le varianti cambiano assunzioni, forma della loss o tipo di feedback».

Per ricostruire «IPO, KTO, ORPO e varianti» annotiamo l'input «prompt, log-probability della policy e riferimento», poi l'operazione «margine DPO, beta e variante offline», infine l'output «loss di preferenza e policy aggiornata». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Le varianti cambiano assunzioni, forma della loss o tipo di feedback».

Il passaggio da seguire in «IPO, KTO, ORPO e varianti» è quello descritto dalla frase «Le varianti cambiano assunzioni, forma della loss o tipo di feedback»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «IPO, KTO, ORPO e varianti» il controllo cambia una sola premessa della frase «Le varianti cambiano assunzioni, forma della loss o tipo di feedback» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Le varianti cambiano assunzioni, forma della loss o tipo di feedback». [SRC-49-004]

Il punto didattico di «IPO, KTO, ORPO e varianti» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «loss di preferenza e policy aggiornata» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Il controllo minimo di «IPO, KTO, ORPO e varianti» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di target, proxy e comportamento. Da «IPO, KTO, ORPO e varianti» portiamo l'output «loss di preferenza e policy aggiornata»; non portiamo invece una conclusione oltre il caso locale.

## Offline preference data

L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie. [SRC-49-001]

Prima del nome tecnico fissiamo la situazione: consideriamo due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata. Da qui possiamo leggere la conseguenza dichiarata da «L'ottimizzazione resta limitata alla copertura del dataset».

Nel contratto locale, l'input «prompt, log-probability della policy e riferimento» entra, l'operazione «margine DPO, beta e variante offline» modifica il percorso e l'output «loss di preferenza e policy aggiornata» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Offline preference data»; resta da controllare che la preferenza osservata non è una verità assoluta. La domanda locale è «L'ottimizzazione resta limitata alla copertura del dataset».

Il post-training trasforma preferenze, verifiche o tracce in un segnale di aggiornamento. Quel segnale è un proxy: bisogna separare ciò che viene premiato dal comportamento applicativo che si vuole valutare. Per «Offline preference data» il controllo cambia una sola premessa della frase «L'ottimizzazione resta limitata alla copertura del dataset» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «L'ottimizzazione resta limitata alla copertura del dataset». [SRC-49-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Nuove policy possono visitare risposte non rappresentate nelle coppie. Il piccolo risultato resta un'illustrazione di «L'ottimizzazione resta limitata alla copertura del dataset», non una promessa generale.

La prova di «Offline preference data» conserva input, operazione e output; poi esplicita quale parte di «L'ottimizzazione resta limitata alla copertura del dataset» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il caso finale consegna l'output «loss di preferenza e policy aggiornata» come evidenza locale e conserva la distanza tra obiettivo locale e compito come domanda aperta.

## Il caso minimo e la sua variante: Evitare un reward model esplicito

Il caso intero parte dall'input «prompt, log-probability della policy e riferimento», applica l'operazione «margine DPO, beta e variante offline» e osserva l'output «loss di preferenza e policy aggiornata». Un esempio controllato: margine 0,8 con beta dichiarato e riferimento invariato. La formula locale è:

$$
L_DPO = -log sigma(beta (r_c - r_r))
$$

DPO usa il margine di preferenza senza presentarlo come verità assoluta. [SRC-49-001]

![Ottimizzazione diretta delle preferenze: compare](../../assets/chapters/49_preference_opt/OPT-02/candidate-v48.png)

La figura OPT-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Margine DPO, beta e variante offline. L'input è prompt, log-probability della policy e riferimento, l'output è loss di preferenza e policy aggiornata; il vincolo da controllare è che la preferenza osservata non è una verità assoluta.

## Che cosa osserva lo snippet: Coppie chosen e rejected

Nel run Python rendiamo osservabile la frase «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-49-001.txt` documenta il caso senza pretendere una misura generale.

## Che cosa non dimostra: Offline preference data

Il meccanismo di «Ottimizzazione diretta delle preferenze» non garantisce da solo che il sistema funzioni fuori dal caso guida. La preferenza osservata non è una verità assoluta. Il limite osservato riguarda la frase «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## La mappa delle condizioni: Ottimizzazione diretta delle preferenze

Il percorso ha tenuto insieme una coppia chosen-rejected per l'ottimizzazione diretta, l'operazione «margine DPO, beta e variante offline» e l'output «loss di preferenza e policy aggiornata». Le sezioni «Evitare un reward model esplicito», «Coppie chosen e rejected», «Offline preference data» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: la preferenza osservata non è una verità assoluta. Il Capitolo 50, Process supervision, outcome supervision e verifier, può partire da questo output e dichiarare la propria domanda.

### Cinque domande di controllo: Evitare un reward model esplicito

1. Ricostruisci l'oggetto continuo a partire da «Evitare un reward model esplicito» e indica quale parte della frase «DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata» entra nel caso.
2. Spiega quale trasformazione collega «Evitare un reward model esplicito» a «Offline preference data» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: la preferenza osservata non è una verità assoluta.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «L'ottimizzazione resta limitata alla copertura del dataset» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi per cambiare una condizione: Offline preference data

1. Racconta «Evitare un reward model esplicito» come una trasformazione: che cosa entra e che cosa esce?
2. Confronta due esecuzioni di «Coppie chosen e rejected» mantenendo il resto del setup invariato.
3. Per «Temperatura beta», separa l'esempio locale dal limite che impedisce di generalizzarlo.
4. Progetta una prova per «IPO, KTO, ORPO e varianti» che renda visibile il suo confine.
5. Scrivi una metrica o una domanda per valutare «Offline preference data» senza confondere livelli diversi.

## Fonti e risultati locali: Ottimizzazione diretta delle preferenze

Per «Ottimizzazione diretta delle preferenze», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto target, proxy e comportamento. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a target, proxy e comportamento.
