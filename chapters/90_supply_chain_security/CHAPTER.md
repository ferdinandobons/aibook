<!--
chapter_id: CH-P13-SUPPLY-CHAIN-SECURITY
part_id: P13
order_key: 900
title: Poisoning, backdoor, extraction e supply chain
maturity: CORE
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: 3 agosto 2026
environment: Python 3.13.12, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo 90. Poisoning, backdoor, extraction e supply chain

Il Capitolo 89, Prompt injection e sicurezza dei tool, ha lasciato disponibile gli artefatti che attraversano la supply chain del modello. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «poisoning, backdoor, extraction e controllo di provenienza» e verifichiamo che integrità del file non certifica assenza di contenuto malevolo.

## Data poisoning

Campioni modificati possono alterare comportamento generale o target specifici. Provenienza e deduplicazione riducono alcune superfici. [SRC-90-001]

Per capire «Data poisoning» partiamo da questo caso: un checkpoint con digest e owner trusted supera l'integrity gate, ma il contenuto resta da analizzare. Il caso rende osservabile il punto centrale: «Campioni modificati possono alterare comportamento generale o target specifici».

Nel contratto locale, l'input «dataset, checkpoint, repository, digest e owner» entra, l'operazione «poisoning, backdoor, extraction e controllo di provenienza» modifica il percorso e l'output «artefatto rilasciato, traccia e decisione di blocco» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Data poisoning»; resta da controllare che integrità del file non certifica assenza di contenuto malevolo. La domanda locale è «Campioni modificati possono alterare comportamento generale o target specifici».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Data poisoning» il controllo cambia una sola premessa della frase «Campioni modificati possono alterare comportamento generale o target specifici» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Campioni modificati possono alterare comportamento generale o target specifici». [SRC-90-001]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Provenienza e deduplicazione riducono alcune superfici. Il piccolo risultato resta un'illustrazione di «Campioni modificati possono alterare comportamento generale o target specifici», non una promessa generale.

Per verificare «Data poisoning» cambiamo una sola condizione vicina alla frase «Campioni modificati possono alterare comportamento generale o target specifici», teniamo fermo il resto e registriamo l'output «artefatto rilasciato, traccia e decisione di blocco». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Backdoor», riceve l'output «artefatto rilasciato, traccia e decisione di blocco» come base, ma dovrà formulare e verificare la propria distinzione.

## Backdoor

Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove. Scanner e fine-tuning non garantiscono rimozione. [SRC-90-002]

Il caso minimo di «Backdoor» si presenta così: un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove».

La sezione usa l'input «dataset, checkpoint, repository, digest e owner» come punto di partenza e l'output «artefatto rilasciato, traccia e decisione di blocco» come traccia d'uscita. La trasformazione concreta è «poisoning, backdoor, extraction e controllo di provenienza»; il caso non è completo se non dichiariamo anche che integrità del file non certifica assenza di contenuto malevolo. La condizione da isolare è «Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Backdoor» il controllo cambia una sola premessa della frase «Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove». [SRC-90-002]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Backdoor» conserviamo l'osservazione collegata a «Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Backdoor» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. Da «Backdoor» portiamo l'output «artefatto rilasciato, traccia e decisione di blocco»; non portiamo invece una conclusione oltre il caso locale.

![Poisoning, backdoor, extraction e supply chain: manifest](../../assets/chapters/90_supply_chain_security/SECURITY-01/candidate-v48.png)

La figura SECURITY-01 usa la famiglia manifest. Il diagramma segue il passaggio: Poisoning, backdoor, extraction e controllo di provenienza. L'input è dataset, checkpoint, repository, digest e owner, l'output è artefatto rilasciato, traccia e decisione di blocco; il vincolo da controllare è che integrità del file non certifica assenza di contenuto malevolo.

## Model extraction

Query e output possono permettere di imitare capacità o recuperare informazioni. Rate limit e watermark comportamentali hanno limiti. [SRC-90-003]

Prima del nome tecnico fissiamo la situazione: consideriamo un caso in cui integrità del file non certifica assenza di contenuto malevolo. Da qui possiamo leggere la conseguenza dichiarata da «Query e output possono permettere di imitare capacità o recuperare informazioni».

Per ricostruire «Model extraction» annotiamo l'input «dataset, checkpoint, repository, digest e owner», poi l'operazione «poisoning, backdoor, extraction e controllo di provenienza», infine l'output «artefatto rilasciato, traccia e decisione di blocco». Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «Query e output possono permettere di imitare capacità o recuperare informazioni».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Model extraction» il controllo cambia una sola premessa della frase «Query e output possono permettere di imitare capacità o recuperare informazioni» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Query e output possono permettere di imitare capacità o recuperare informazioni». [SRC-90-003]

Il punto didattico di «Model extraction» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. L'output «artefatto rilasciato, traccia e decisione di blocco» mostra il contratto locale, ma non sostituisce una misura sul sistema completo.

La prova di «Model extraction» conserva input, operazione e output; poi esplicita quale parte di «Query e output possono permettere di imitare capacità o recuperare informazioni» non è stata misurata. Così il test separa l'evidenza dall'inferenza. Il passaggio successivo, «Artifact security», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.

## Artifact security

Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro. [SRC-90-004]

Per capire «Artifact security» partiamo da questo caso: un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente. Il caso rende osservabile il punto centrale: «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro».

Nel contratto locale, l'input «dataset, checkpoint, repository, digest e owner» entra, l'operazione «poisoning, backdoor, extraction e controllo di provenienza» modifica il percorso e l'output «artefatto rilasciato, traccia e decisione di blocco» è ciò che osserviamo. Qui cambia soprattutto il passaggio «Artifact security»; resta da controllare che integrità del file non certifica assenza di contenuto malevolo. La domanda locale è «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Artifact security» il controllo cambia una sola premessa della frase «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro». [SRC-90-004]

La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. Il piccolo risultato resta un'illustrazione di «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro», non una promessa generale.

Per verificare «Artifact security» cambiamo una sola condizione vicina alla frase «Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro», teniamo fermo il resto e registriamo l'output «artefatto rilasciato, traccia e decisione di blocco». Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso. La sezione successiva, «Repository e deployment», riceve l'output «artefatto rilasciato, traccia e decisione di blocco» come base, ma dovrà formulare e verificare la propria distinzione.

## Repository e deployment

File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici. [SRC-90-001]

Il caso minimo di «Repository e deployment» si presenta così: un input non fidato attraversa una policy esterna. Il controllo deve restare attivo anche se il modello produce una richiesta testuale convincente. Non lo usiamo come decorazione: serve a rendere osservabile la frase «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici».

La sezione usa l'input «dataset, checkpoint, repository, digest e owner» come punto di partenza e l'output «artefatto rilasciato, traccia e decisione di blocco» come traccia d'uscita. La trasformazione concreta è «poisoning, backdoor, extraction e controllo di provenienza»; il caso non è completo se non dichiariamo anche che integrità del file non certifica assenza di contenuto malevolo. La condizione da isolare è «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici».

Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo. Per «Repository e deployment» il controllo cambia una sola premessa della frase «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici» e conserva input, output e criterio di successo, così la differenza resta attribuibile. La verifica resta ancorata a «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici». [SRC-90-001]

Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «Repository e deployment» conserviamo l'osservazione collegata a «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici» e lasciamo esplicitamente fuori ciò che non è stato misurato.

Il controllo minimo di «Repository e deployment» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di protocollo, slice e decisione. La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.

## Una traiettoria controllata: Data poisoning

Il caso intero parte dall'input «dataset, checkpoint, repository, digest e owner», applica l'operazione «poisoning, backdoor, extraction e controllo di provenienza» e osserva l'output «artefatto rilasciato, traccia e decisione di blocco». Un esempio controllato: digest uguale ma dataset contaminato da una regola nascosta. Lo schema compatto è:

$$
trace = hash(model, data, artifact, owner)
$$

È una notazione di interfaccia, non un'identità numerica completa. Supply chain e backdoor richiedono una traccia degli artefatti e dei soggetti. [SRC-90-001]

![Poisoning, backdoor, extraction e supply chain: threat](../../assets/chapters/90_supply_chain_security/SECURITY-02/candidate-v50.png)

La figura SECURITY-02 cambia composizione rispetto alla prima. Il diagramma segue il passaggio: Poisoning, backdoor, extraction e controllo di provenienza. L'input è dataset, checkpoint, repository, digest e owner, l'output è artefatto rilasciato, traccia e decisione di blocco; il vincolo da controllare è che integrità del file non certifica assenza di contenuto malevolo.

## Il passaggio eseguito in Python: Backdoor

Nel run Python rendiamo osservabile la frase «Campioni modificati possono alterare comportamento generale o target specifici» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-90-001.txt` documenta il caso senza pretendere una misura generale.

## Prima di generalizzare: Repository e deployment

Il meccanismo di «Poisoning, backdoor, extraction e supply chain» non garantisce da solo che il sistema funzioni fuori dal caso guida. Integrità del file non certifica assenza di contenuto malevolo. Il limite osservato riguarda la frase «Campioni modificati possono alterare comportamento generale o target specifici»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.

## Dalla lezione al capitolo seguente: Poisoning, backdoor, extraction e supply chain

Il percorso ha tenuto insieme gli artefatti che attraversano la supply chain del modello, l'operazione «poisoning, backdoor, extraction e controllo di provenienza» e l'output «artefatto rilasciato, traccia e decisione di blocco». Le sezioni «Data poisoning», «Backdoor», «Repository e deployment» mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere. L'invariante da portare avanti è: integrità del file non certifica assenza di contenuto malevolo. Il Capitolo 91, Privacy, fairness e unlearning, può partire da questo output e dichiarare la propria domanda.

### Domande per ricostruire il percorso: Data poisoning

1. Ricostruisci l'oggetto continuo a partire da «Data poisoning» e indica quale parte della frase «Campioni modificati possono alterare comportamento generale o target specifici» entra nel caso.
2. Spiega quale trasformazione collega «Data poisoning» a «Repository e deployment» e quale output osserviamo nel passaggio.
3. Usa lo snippet per controllare l'invariante del contratto: integrità del file non certifica assenza di contenuto malevolo.
4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.
5. Indica quale parte della frase «File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.

### Esercizi sul failure mode: Repository e deployment

1. Ricostruisci input e output di «Data poisoning» usando un esempio di tre righe.
2. Modifica una sola variabile in «Backdoor» e anticipa l'invariante che dovrebbe restare.
3. Metti «Model extraction» a confronto con il caso base e descrivi il failure mode più vicino.
4. Scrivi un test minimo per rendere osservabile il confine di «Artifact security».
5. Formula per «Repository e deployment» una domanda che separi meccanismo e qualità del sistema.

## Dossier delle fonti e materiali: Poisoning, backdoor, extraction e supply chain

Per «Poisoning, backdoor, extraction e supply chain», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto protocollo, slice e decisione. `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a protocollo, slice e decisione.
