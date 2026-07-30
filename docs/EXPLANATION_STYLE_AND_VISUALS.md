# Stile di spiegazione e visuali

## Stato

Metodo vincolante per ogni capitolo del libro.

- Lingua: italiano.
- Ambito: testo, formule, esempi, immagini, tabelle, codice ed esercizi.
- Dipendenze esterne: nessuna.
- Struttura visibile della prosa: `19_STRUTTURA_LOGICA_IN_PROSA.md`.
- Review didattica: `18_PROTOCOLLO_QA_DIDATTICO.md`.
- Standard visuale: `17_STANDARD_VISIVO_CANONICO.md`.

## Scopo

Ogni capitolo deve costruire un modello mentale eseguibile. Al termine della spiegazione il lettore deve poter:

- ricostruire il flusso;
- localizzare ogni componente;
- dire cosa entra e cosa esce;
- descrivere l'ordine reale delle operazioni;
- indicare shape e invarianti;
- prevedere cosa cambia quando una parte viene modificata;
- dire cosa il meccanismo non fa.

Riconoscere i termini non basta. La spiegazione riesce quando il lettore sa ripetere il meccanismo partendo dall'esempio originale, applicarlo a un caso modificato e delimitarne il comportamento.

## Principio centrale

Un oggetto concreto attraversa il capitolo dall'apertura alla ricostruzione finale.

Ogni passaggio principale:

1. parte dall'output del passaggio precedente;
2. aggiunge una sola distinzione, operazione, relazione o struttura;
3. applica l'aggiunta allo stesso esempio;
4. rende disponibile lo stato accumulato;
5. consegna il risultato al passaggio successivo.

La progressione deve poter essere ricostruita come:

```text
oggetto noto
-> oggetto noto più una distinzione
-> stato precedente più una operazione
-> stato precedente più un risultato
-> modello eseguibile completo
```

Una sezione che può essere spostata altrove senza rompere l'esecuzione probabilmente non appartiene alla struttura portante.

## La catena dei sette punti

La spiegazione collega, in ordine causale:

1. stato iniziale;
2. problema non risolvibile in quello stato;
3. motivo della nuova operazione;
4. trasformazione concreta;
5. stato risultante;
6. invariante;
7. elemento ancora mancante.

Questi punti devono essere presenti nel significato. Non devono essere necessariamente pubblicati come sette titoli.

L'invariante non resta implicito. Quando cambiano i valori ma non il numero di token, la shape esterna o l'ordine, la prosa lo dichiara nel punto in cui il lettore osserva la trasformazione.

## Stato del lettore

Ogni paragrafo sposta il lettore tra stati di conoscenza:

| Stato | Significato |
|---|---|
| Stabile | Il lettore può già ricostruire l'oggetto o l'operazione. |
| Corrente | L'oggetto esatto esaminato ora. |
| Nuovo | Un solo concetto introdotto nel passaggio. |
| Stabilizzato | Il concetto è stato eseguito e può essere descritto. |
| Differito | Dipendenza o variante rimandata intenzionalmente. |

Prima della stesura, in `PLAN.md`, si registra:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```

Questa scheda è interna. Non viene ripetuta nel capitolo destinato al lettore.

## Struttura portante universale

Ogni capitolo adatta al proprio soggetto questi movimenti:

1. **Ancora.** Parte dall'ultimo oggetto ricostruibile.
2. **Mostra il gap.** Dimostra una capacità mancante o un vincolo.
3. **Esegue la transizione minima.** Applica una sola operazione reale.
4. **Nomina e contratta.** Introduce il termine tecnico dopo il meccanismo.
5. **Ripete e scala.** Generalizza una dimensione alla volta.
6. **Formalizza e collega.** Aggiunge shape, formule, codice e varianti dopo la stabilizzazione.
7. **Ricostruisce e trasferisce.** Ricompone il percorso e lo applica a un caso modificato.

La sequenza interna è:

```text
ORIENTA -> INTRODUCI -> ESEGUI -> REINTEGRA -> CONTROLLA
```

## Blocco atomico di spiegazione

Per ogni transizione importante, l'autore e il reviewer devono poter rispondere:

```text
Dove siamo?
Quale problema locale resta?
Quali input e shape sono disponibili?
Quale trasformazione viene eseguita?
Quale output e shape risultano?
Che cosa cambia?
Che cosa resta invariato?
Che cosa non fa l'operazione?
Chi usa l'output?
Quale esempio o prova stabilizza il passaggio?
Quale errore è probabile?
Come continua il flusso?
```

Il blocco atomico è uno scaffold di progettazione e review. Per impostazione predefinita le sue etichette non diventano titoli del capitolo.

La prosa incorpora le risposte in modo naturale. Per esempio:

```text
I tre prodotti scalari forniscono uno score per ogni key. Il vettore mantiene shape [S], mentre V non è ancora coinvolta. Gli score non sono coefficienti normalizzati, quindi il passaggio successivo ne controlla la scala prima della softmax.
```

La giunzione deve nominare un oggetto ottenuto e il passaggio successivo, ma non deve usare sempre la stessa formula verbale.

## Struttura logica implicita nella prosa

Il capitolo destinato al lettore usa titoli semantici, come:

```text
Perché una combinazione fissa non basta
Dal confronto ai coefficienti
Escludere le posizioni future
Dalla formula all'implementazione
```

Non usa sistematicamente come intestazioni:

```text
Stato del lettore
Dove siamo
Problema locale
Input e shape
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

Queste funzioni restano verificabili in `PLAN.md` e `TEXT_AUDIT.md`. La loro ripetizione nella superficie editoriale viene evitata perché rende le lezioni meccaniche e tutte formalmente identiche.

## Gate di comparsa

Ogni elemento nuovo entra dopo che il referente concreto è stabile.

### Termine tecnico

Un termine compare quando:

1. il lettore ha visto l'oggetto o l'operazione;
2. il testo gli assegna un significato stabile;
3. le sezioni successive lo usano nello stesso modo.

Si descrive prima di nominare.

### Astrazione

Parole come `rappresentazione`, `contesto`, `feature`, `memoria` ed `efficienza` richiedono un referente concreto:

```text
quali valori
in quale oggetto
prodotti da quale operazione
usati da quale calcolo successivo
```

### Frecce

Le catene con frecce sono riassunti, non prime spiegazioni. Prima di mostrare `A -> B -> C`, il lettore deve sapere cosa sono i nodi, quale operazione rappresenta ogni freccia e cosa cambia.

### Simboli e formule

La matematica viene introdotta, quando pertinente, nell'ordine:

```text
domanda naturale
-> esempio numerico
-> valori e shape
-> pseudocodice o algoritmo
-> formula
-> derivazione necessaria
```

Ogni simbolo deve avere prima una quantità concreta visibile.

### Codice

Il codice compare dopo che l'operazione indipendente dalla libreria è stabile.

Prima dello snippet, la prosa rende chiari:

- input noto;
- operazione centrale;
- output o invariante da osservare.

Il contratto completo resta negli artefatti del codice; non è obbligatorio pubblicare una sezione chiamata `Contratto dello snippet`.

### Varianti

Varianti, ottimizzazioni ed eccezioni compaiono dopo il caso base. Una variante necessaria per localizzare un confine viene nominata e rinviata, non spiegata a metà.

## Profili di capitolo

La struttura visibile si adatta al profilo:

| Profilo | Percorso dominante |
|---|---|
| Componente | input corrente -> capacità mancante -> esecuzione -> contratto -> prossimo consumer |
| Processo | stato iniziale -> trigger -> transizione -> invariante -> ripetizione o stop |
| Architettura | mappa globale -> confini -> interfacce -> data flow -> parametri e stato |
| Metodo di training | modello prima dell'update -> segnale -> loss -> gradiente -> update |
| Tecnica | baseline -> collo di bottiglia -> modifica -> comportamento invariato -> trade-off |
| Paper | domanda -> baseline -> proposta -> setup -> risultato -> limite -> riproduzione |
| Confronto | livello comune -> differenza controllata -> conseguenza -> condizione d'uso |
| Implementazione | algoritmo -> strutture dati -> pseudocodice -> codice -> test -> failure case |

Capitoli di profilo diverso non vengono forzati nella stessa sagoma di sottotitoli.

## Regole di scrittura

- Italiano calmo, preciso e progressivo.
- Testo scritto direttamente in italiano, non tradotto.
- Termini tecnici standard in inglese quando appropriato.
- Nessun em dash.
- Si spiega perché un componente serve prima di spiegare come funziona.
- Un concetto nuovo per passaggio.
- Una trasformazione dominante per paragrafo.
- Soggetti e referenti espliciti.
- Nomi concreti e verbi operativi.
- Niente hype, keyword stuffing o citazioni finte.
- Gli elenchi non sostituiscono una spiegazione causale.
- Comportamento implementato, valori illustrativi, risultati eseguiti e sviluppi futuri restano distinti.
- Una semplificazione non elimina condizioni necessarie.
- Una frase tecnica senza fonte o prova non entra nella versione approvata.
- La struttura interna non viene esposta come checklist ripetitiva.

## Niente metafore

Non si usano metafore, analogie estranee, personificazioni, etichette infantili o domande retoriche al posto dell'operazione reale.

Restano ammessi verbi tecnici consolidati, come `il modello predice`, `il layer proietta` o `la maschera esclude`, perché nominano un calcolo.

## Persona e voce

La prosa è impersonale oppure usa la prima persona plurale per le operazioni eseguite nel testo.

La seconda persona è riservata ai controlli di comprensione e agli esercizi.

# Grammatica visuale

## Principio

Le visuali fanno parte della spiegazione. Ogni immagine risponde a una domanda.

La prosa:

1. inquadra la domanda;
2. attraversa gli elementi nell'ordine di lettura;
3. conclude con risultato e passo successivo.

Queste funzioni non richiedono le etichette letterali `Domanda della figura` e `Conclusione della figura`.

## Produzione e stile

I diagrammi tecnici vengono creati con lo strumento immagini.

- Artefatto principale: PNG ad alta risoluzione.
- Prima generazione sempre bozza.
- Sfondo bianco puro e stile secondo `17_STANDARD_VISIVO_CANONICO.md`.
- Contenimento del testo secondo `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`.
- Nessun watermark, firma o branding di terzi.
- Le immagini di riferimento orientano il linguaggio, non vengono copiate.

## Scelta della rappresentazione

Si usa lo strumento più semplice che rappresenta correttamente la relazione.

| Strumento | Serve per |
|---|---|
| Immagine generata | architetture, processi, flussi tensoriali e confronti spaziali |
| Formula | notazione, derivazioni e complessità |
| Tabella Markdown | confronti piccoli ed esatti |
| Blocco di codice | codice e output letterale |
| Matrice o griglia | operazioni numeriche compatte |

Non si crea un'immagine soltanto perché una sezione ne è priva.

## Ammissione visuale

Una visuale è ammessa quando:

- le label sono note o introdotte accanto;
- contiene al massimo una trasformazione non insegnata;
- il colore non è l'unico significato;
- i valori illustrativi sono dichiarati;
- i dati misurati indicano setup e provenienza;
- cambiamento e invariante risultano comprensibili;
- la stessa informazione è disponibile in testo;
- testo e simboli sono leggibili;
- ogni linea ha una funzione univoca.

## Collegamenti e frecce

Ogni freccia ha sorgente, destinazione, direzione e significato precisi. Incroci, ramificazioni, residual path, mask e percorsi di `Q`, `K` e `V` devono risultare inequivocabili.

## Accessibilità e audit

Ogni immagine finale include alt text, equivalente testuale, ordine di lettura e provenienza dei numeri.

Prima dell'approvazione si controllano formule, numeri, shape, frecce, incroci, mask, corrispondenza con prosa e codice, densità, spaziatura, dimensione del testo, contenimento e assenza di branding.

Dopo ogni modifica si ripete l'intero audit.

# Integrazione del codice

Il codice collega il meccanismo a un'implementazione osservabile. Non sostituisce la prosa e non introduce un secondo percorso concettuale.

- Python e PyTorch sono predefiniti.
- NumPy può verificare calcoli elementari.
- Pseudocodice e codice eseguibile restano distinti.
- Uno snippet mostra una sola operazione centrale.
- Import, input, shape e output sono espliciti.
- Le variabili coincidono con la prosa.
- Le API vengono controllate nella documentazione ufficiale.
- Gli snippet vengono eseguiti e testati.
- Gli output inventati non vengono presentati come eseguiti.

# Check finali di comprensione

Ogni capitolo chiude verificando:

| Check | Azione richiesta |
|---|---|
| Ricostruzione | Ricostruire la transizione dall'input originale. |
| Localizzazione | Dire cosa viene prima e dopo il meccanismo. |
| Confine | Dire cosa il meccanismo non fa. |
| Trasferimento | Applicarlo a un nuovo input o parametro. |
| Variazione | Prevedere l'effetto di una modifica. |

Se il lettore non può rispondere, si torna all'ultimo punto stabile e si ripara la giunzione.

# Istruzione compatta

```text
Costruisci il capitolo come una sequenza di transizioni nello stato del lettore. Usa uno scaffold rigoroso in pianificazione e review, ma trasformalo in prosa naturale nella versione destinata al lettore. Porta un oggetto concreto dall'apertura alla ricostruzione finale. Ogni passaggio parte dall'output del precedente, aggiunge una sola cosa e rende comprensibili cambiamento, invariante, confine e passo successivo senza ripetere meccanicamente queste etichette come titoli. Introduci termini, formule, codice, varianti e visuali soltanto dopo che i referenti concreti sono stabili. Verifica fonti, calcoli, immagini e snippet. Chiudi con ricostruzione, localizzazione, confine, trasferimento e variazione. Mantieni il capitolo come bozza finché non supera review tecnica, review didattica, gate anti-template e revisione autoriale.
```