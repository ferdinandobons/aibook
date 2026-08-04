<!--
chapter_id: CH-P08-MOE-CONDITIONAL
part_id: P08
order_key: 440
title: Mixture of Experts e calcolo condizionale
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 44. Mixture of Experts e calcolo condizionale

Una frase plausibile non basta a spiegare mixture of experts e calcolo condizionale. L'oggetto è token e assegnazioni del router agli esperti; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.

## Router top-k

Un router assegna probabilità agli esperti e attiva un sottoinsieme per token. [SRC-44-001]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso minimo con input logits del router, top-k e capacità per esperto e output «carico, token restituiti e costo attivo». Da qui possiamo leggere la conseguenza dichiarata da «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token».

La sezione usa l'input «logits del router, top-k e capacità per esperto» come punto di partenza e l'output «carico, token restituiti e costo attivo» come traccia d'uscita. La trasformazione concreta è «routing, dispatch, expert compute e combine»; il caso non è completo se non dichiariamo anche che parametri totali e parametri attivi non sono la stessa quantità. La condizione da isolare è «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token».

Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema. Per «Router top-k» il controllo cambia una sola premessa della frase «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token». [SRC-44-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Router top-k» conserviamo l'osservazione collegata a «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Router top-k» conserva input, operazione e output; poi esplicita quale parte di «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Capacità», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Capacità

Ogni esperto riceve un limite di token. Overflow, rerouting o dropping devono essere dichiarati. [SRC-44-002]

Per capire «Capacità» partiamo da questo caso: x=[1,2] passato in una trasformazione affine e poi in una non linearità, con shape e confine espliciti. Il caso rende osservabile il punto centrale: «Ogni esperto riceve un limite di token».

Per ricostruire «Capacità» annotiamo l'input «logits del router, top-k e capacità per esperto», poi l'operazione «routing, dispatch, expert compute e combine», infine l'output «carico, token restituiti e costo attivo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Ogni esperto riceve un limite di token».

Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «Ogni esperto riceve un limite di token». [SRC-44-002]

Il punto didattico di «Capacità» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «carico, token restituiti e costo attivo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Capacità» cambiamo una sola condizione vicina alla frase «Ogni esperto riceve un limite di token», teniamo fermo il resto e registriamo l'output «carico, token restituiti e costo attivo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Load balancing», riceve l'output «carico, token restituiti e costo attivo» come base, ma dovrà formulare e verificare la propria distinzione.

## Load balancing

Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione. [SRC-44-003]

Il caso minimo di «Load balancing» si presenta così: un caso in cui parametri totali e parametri attivi non sono la stessa quantità. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione».

Nel contratto locale, l'input «logits del router, top-k e capacità per esperto» entra, l'operazione «routing, dispatch, expert compute e combine» modifica il percorso e l'output «carico, token restituiti e costo attivo» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Load balancing»; resta da controllare che parametri totali e parametri attivi non sono la stessa quantità. La domanda locale è «Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione».

Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema. Per «Load balancing» il controllo cambia una sola premessa della frase «Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione». [SRC-44-003]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione», non una promessa generale.

Il controllo minimo di «Load balancing» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di ordine, posizione e memoria contestuale. Da «Load balancing» portiamo l'output «carico, token restituiti e costo attivo»; non portiamo invece una conclusione oltre il caso locale.

## Expert parallelism

Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti. [SRC-44-004]

Prima del nome tecnico fissiamo la situazione: consideriamo un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Da qui possiamo leggere la conseguenza dichiarata da «Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti».

La sezione usa l'input «logits del router, top-k e capacità per esperto» come punto di partenza e l'output «carico, token restituiti e costo attivo» come traccia d'uscita. La trasformazione concreta è «routing, dispatch, expert compute e combine»; il caso non è completo se non dichiariamo anche che parametri totali e parametri attivi non sono la stessa quantità. La condizione da isolare è «Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti».

Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema. La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti. La verifica resta ancorata a «Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti». [SRC-44-004]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Expert parallelism» conserviamo l'osservazione collegata a «Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti» e lasciamo esplicitamente fuori ciò che non è stato misurato.

La prova di «Expert parallelism» conserva input, operazione e output; poi esplicita quale parte di «Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Parametri totali e attivi», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

![Mixture of Experts e calcolo condizionale: branch](../../assets/chapters/44_moe_conditional/MOE-01/candidate-v45.png)

La figura MOE-01 usa la famiglia branch. Il diagramma segue il passaggio: Routing, dispatch, expert compute e combine. L'input è logits del router, top-k e capacità per esperto, l'output è carico, token restituiti e costo attivo; il vincolo da controllare è che parametri totali e parametri attivi non sono la stessa quantità.

## Parametri totali e attivi

Un MoE può avere molti parametri totali e pochi parametri attivi per token. FLOP, memoria e comunicazione vanno riportati separatamente. [SRC-44-001]

Per capire «Parametri totali e attivi» partiamo da questo caso: un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup. Il caso rende osservabile il punto centrale: «Un MoE può avere molti parametri totali e pochi parametri attivi per token».

Per ricostruire «Parametri totali e attivi» annotiamo l'input «logits del router, top-k e capacità per esperto», poi l'operazione «routing, dispatch, expert compute e combine», infine l'output «carico, token restituiti e costo attivo». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Un MoE può avere molti parametri totali e pochi parametri attivi per token».

Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema. Per «Parametri totali e attivi» il controllo cambia una sola premessa della frase «Un MoE può avere molti parametri totali e pochi parametri attivi per token» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un MoE può avere molti parametri totali e pochi parametri attivi per token». [SRC-44-001]

Il punto didattico di «Parametri totali e attivi» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «carico, token restituiti e costo attivo» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

Per verificare «Parametri totali e attivi» cambiamo una sola condizione vicina alla frase «Un MoE può avere molti parametri totali e pochi parametri attivi per token», teniamo fermo il resto e registriamo l'output «carico, token restituiti e costo attivo». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.

## Una traiettoria controllata: Router top-k

Il caso intero parte dall'input «logits del router, top-k e capacità per esperto», applica l'operazione «routing, dispatch, expert compute e combine» e osserva l'output «carico, token restituiti e costo attivo». Un esempio controllato: quattro token assegnati a due esperti con capacità limitata. La formula locale è:

$$
load_e = sum_i 1[router(i)=e]
$$

Il router deve bilanciare carico e capacità senza perdere il contratto dei token. [SRC-44-001]

![Mixture of Experts e calcolo condizionale: chart](../../assets/chapters/44_moe_conditional/MOE-02/candidate-v45.png)

La figura MOE-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Routing, dispatch, expert compute e combine. L'input è logits del router, top-k e capacità per esperto, l'output è carico, token restituiti e costo attivo; il vincolo da controllare è che parametri totali e parametri attivi non sono la stessa quantità.

## Il passaggio eseguito in Python: Capacità

Nel run Python rendiamo osservabile la frase «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-44-001.txt` documenta il caso senza pretendere una misura generale.

## Prima di generalizzare: Parametri totali e attivi

Il meccanismo di «Mixture of Experts e calcolo condizionale» non garantisce da solo che il sistema funzioni fuori dal caso guida. Parametri totali e parametri attivi non sono la stessa quantità. Il limite osservato riguarda la frase «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Dalla lezione al capitolo seguente: Mixture of Experts e calcolo condizionale

Il percorso ha tenuto insieme token e assegnazioni del router agli esperti, l'operazione «routing, dispatch, expert compute e combine» e l'output «carico, token restituiti e costo attivo». Le sezioni «Router top-k», «Capacità», «Parametri totali e attivi» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: parametri totali e parametri attivi non sono la stessa quantità. Il Capitolo 45, Byte, predizione multi-token e language diffusion, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Router top-k

1. Ricostruisci l'oggetto continuo a partire da «Router top-k» e indica quale parte della frase «Un router assegna probabilità agli esperti e attiva un sottoinsieme per token» entra nel caso.
2. Spiega quale trasformazione collega «Router top-k» a «Parametri totali e attivi» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: parametri totali e parametri attivi non sono la stessa quantità.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «Un MoE può avere molti parametri totali e pochi parametri attivi per token» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Parametri totali e attivi

1. Ricostruisci input e output di «Router top-k» usando un esempio di tre righe.
2. Modifica una sola variabile in «Capacità» e anticipa l'invariante che dovrebbe restare.
3. Metti «Load balancing» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Expert parallelism».
5. Formula per «Parametri totali e attivi» una domanda che separi meccanismo e qualità del sistema.

## Dossier delle fonti e materiali: Mixture of Experts e calcolo condizionale

Per «Mixture of Experts e calcolo condizionale», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto ordine, posizione e memoria contestuale. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a ordine, posizione e memoria contestuale.
