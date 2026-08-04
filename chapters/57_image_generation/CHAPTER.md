<!--
chapter_id: CH-P10-IMAGE-GENERATION
part_id: P10
order_key: 570
title: Generazione e modifica delle immagini
maturity: ESTABLISHED
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 57. Generazione e modifica delle immagini

Il risultato precedente non è ancora una soluzione completa. Partiamo da un contenuto immagine e la condizione che lo modifica e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare all'output «immagine, score e metadati di provenienza» isoliamo il passaggio «denoising, guidance, editing o inpainting» e ne misuriamo il limite prima di passare a Modelli multimodali nativi e any-to-any.

## Latent diffusion

Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine. [SRC-57-001]

Per capire «Latent diffusion» partiamo da questo caso: un singolo passo riduce una coppia di valori rumorosi secondo uno schedule dichiarato. Il caso rende osservabile il punto centrale: «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente».

Nel contratto locale, l'input «latent, prompt, mask e rumore» entra, l'operazione «denoising, guidance, editing o inpainting» modifica il percorso e l'output «immagine, score e metadati di provenienza» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Latent diffusion»; resta da controllare che controllo dell'immagine e verità del contenuto sono proprietà diverse. La domanda locale è «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente».

Il passaggio da seguire in «Latent diffusion» è quello descritto dalla frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Latent diffusion» il controllo cambia una sola premessa della frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente». [SRC-57-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il decoder ricostruisce pixel al termine. Il piccolo risultato resta un'illustrazione di «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente», non una promessa generale.

Per verificare «Latent diffusion» cambiamo una sola condizione vicina alla frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente», teniamo fermo il resto e registriamo l'output «immagine, score e metadati di provenienza». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Conditioning», riceve l'output «immagine, score e metadati di provenienza» come base, ma dovrà formulare e verificare la propria distinzione.

## Conditioning

Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati. [SRC-57-002]

Il caso minimo di «Conditioning» si presenta così: una regione mascherata modificata lasciando il resto fissato. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati».

La sezione usa l'input «latent, prompt, mask e rumore» come punto di partenza e l'output «immagine, score e metadati di provenienza» come traccia d'uscita. La trasformazione concreta è «denoising, guidance, editing o inpainting»; il caso non è completo se non dichiariamo anche che controllo dell'immagine e verità del contenuto sono proprietà diverse. La condizione da isolare è «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati».

Il passaggio da seguire in «Conditioning» è quello descritto dalla frase «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Conditioning» il controllo cambia una sola premessa della frase «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati». [SRC-57-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Conditioning» conserviamo l'osservazione collegata a «Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Conditioning» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. Da «Conditioning» portiamo l'output «immagine, score e metadati di provenienza»; non portiamo invece una conclusione oltre il caso locale.

![Generazione e modifica delle immagini: timeline](../../assets/chapters/57_image_generation/GENERATION-01/candidate-v48.png)

La figura GENERATION-01 usa la famiglia timeline. Il diagramma segue il passaggio: Denoising, guidance, editing o inpainting. L'input è latent, prompt, mask e rumore, l'output è immagine, score e metadati di provenienza; il vincolo da controllare è che controllo dell'immagine e verità del contenuto sono proprietà diverse.

## Classifier-free guidance

Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione. [SRC-57-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui controllo dell'immagine e verità del contenuto sono proprietà diverse. Da qui possiamo leggere la conseguenza dichiarata da «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione».

Per ricostruire «Classifier-free guidance» annotiamo l'input «latent, prompt, mask e rumore», poi l'operazione «denoising, guidance, editing o inpainting», infine l'output «immagine, score e metadati di provenienza». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione».

Il passaggio da seguire in «Classifier-free guidance» è quello descritto dalla frase «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Classifier-free guidance» il controllo cambia una sola premessa della frase «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione». [SRC-57-003]

Il punto didattico di «Classifier-free guidance» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «immagine, score e metadati di provenienza» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Classifier-free guidance» conserva input, operazione e output; poi esplicita quale parte di «Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Editing e inpainting», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Editing e inpainting

Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition. [SRC-57-004]

Per capire «Editing e inpainting» partiamo da questo caso: due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito. Il caso rende osservabile il punto centrale: «Una mask stabilisce regioni modificabili».

Nel contratto locale, l'input «latent, prompt, mask e rumore» entra, l'operazione «denoising, guidance, editing o inpainting» modifica il percorso e l'output «immagine, score e metadati di provenienza» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Editing e inpainting»; resta da controllare che controllo dell'immagine e verità del contenuto sono proprietà diverse. La domanda locale è «Una mask stabilisce regioni modificabili».

Il passaggio da seguire in «Editing e inpainting» è quello descritto dalla frase «Una mask stabilisce regioni modificabili»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione. Per «Editing e inpainting» il controllo cambia una sola premessa della frase «Una mask stabilisce regioni modificabili» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Una mask stabilisce regioni modificabili». [SRC-57-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. La coerenza con le aree conservate dipende da noise schedule e condition. Il piccolo risultato resta un'illustrazione di «Una mask stabilisce regioni modificabili», non una promessa generale.

Per verificare «Editing e inpainting» cambiamo una sola condizione vicina alla frase «Una mask stabilisce regioni modificabili», teniamo fermo il resto e registriamo l'output «immagine, score e metadati di provenienza». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Controllo e provenienza», riceve l'output «immagine, score e metadati di provenienza» come base, ma dovrà formulare e verificare la propria distinzione.

## Controllo e provenienza

ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema. [SRC-57-001]

Il caso minimo di «Controllo e provenienza» si presenta così: un payload modificato dopo la firma, con digest e metadati confrontati separatamente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «ControlNet, adapter e reference image aggiungono vincoli».

La sezione usa l'input «latent, prompt, mask e rumore» come punto di partenza e l'output «immagine, score e metadati di provenienza» come traccia d'uscita. La trasformazione concreta è «denoising, guidance, editing o inpainting»; il caso non è completo se non dichiariamo anche che controllo dell'immagine e verità del contenuto sono proprietà diverse. La condizione da isolare è «ControlNet, adapter e reference image aggiungono vincoli».

Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello. Il confronto separa integrità del record, identità del firmatario e verità del contenuto, che sono proprietà diverse della stessa pipeline. La verifica resta ancorata a «ControlNet, adapter e reference image aggiungono vincoli». [SRC-57-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Controllo e provenienza» conserviamo l'osservazione collegata a «ControlNet, adapter e reference image aggiungono vincoli» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Controllo e provenienza» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di allineamento tra modalità. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Dal concetto alla situazione concreta: Latent diffusion

Il caso intero parte dall'input «latent, prompt, mask e rumore», applica l'operazione «denoising, guidance, editing o inpainting» e osserva l'output «immagine, score e metadati di provenienza». Un esempio controllato: una regione mascherata modificata lasciando il resto fissato. La formula locale è:

$$
x_hat = g(z, condition)
$$

Editing e generazione modificano un contenuto sotto una condizione dichiarata. [SRC-57-001]

![Generazione e modifica delle immagini: pipeline](../../assets/chapters/57_image_generation/GENERATION-02/candidate-v48.png)

La figura GENERATION-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Denoising, guidance, editing o inpainting. L'input è latent, prompt, mask e rumore, l'output è immagine, score e metadati di provenienza; il vincolo da controllare è che controllo dell'immagine e verità del contenuto sono proprietà diverse.

## Una prova ripetibile: Conditioning

Nel run Python rendiamo osservabile la frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-57-001.txt` documenta il caso senza pretendere una misura generale.

## Il trasferimento richiede altro: Controllo e provenienza

Il meccanismo di «Generazione e modifica delle immagini» non garantisce da solo che il sistema funzioni fuori dal caso guida. Controllo dell'immagine e verità del contenuto sono proprietà diverse. Il limite osservato riguarda la frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Il filo che passa oltre: Generazione e modifica delle immagini

Il percorso ha tenuto insieme un contenuto immagine e la condizione che lo modifica, l'operazione «denoising, guidance, editing o inpainting» e l'output «immagine, score e metadati di provenienza». Le sezioni «Latent diffusion», «Conditioning», «Controllo e provenienza» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: controllo dell'immagine e verità del contenuto sono proprietà diverse. Il Capitolo 58, Modelli multimodali nativi e any-to-any, può partire da questo output e dichiarare la propria domanda.

### Rilettura guidata: Latent diffusion

1. Ricostruisci l'oggetto continuo a partire da «Latent diffusion» e indica quale parte della frase «Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente» entra nel caso.
2. Spiega quale trasformazione collega «Latent diffusion» a «Controllo e provenienza» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: controllo dell'immagine e verità del contenuto sono proprietà diverse.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «ControlNet, adapter e reference image aggiungono vincoli» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Allenamento e trasferimento: Controllo e provenienza

1. Disegna il percorso di «Latent diffusion» indicando dati in ingresso e risultato.
2. Ripeti «Conditioning» cambiando soltanto un valore dichiarato.
3. Trova in «Classifier-free guidance» una condizione che, se rimossa, produrrebbe una failure leggibile.
4. Aggiungi a «Editing e inpainting» un controllo negativo e spiega che cosa protegge.
5. Indica quale claim su «Controllo e provenienza» richiederebbe un benchmark ulteriore.

## Dove verificare definizioni e risultati: Generazione e modifica delle immagini

Per «Generazione e modifica delle immagini», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto allineamento tra modalità. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a allineamento tra modalità.
