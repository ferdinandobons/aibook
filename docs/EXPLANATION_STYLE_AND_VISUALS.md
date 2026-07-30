# Stile di spiegazione e visuali

## Stato

Metodo vincolante per ogni capitolo del libro.

- Lingua: italiano.
- Ambito: testo, formule, esempi, immagini, tabelle, codice ed esercizi.
- Dipendenze esterne: nessuna.
- `LEARN_GOVERNANCE.md`: non necessario.
- Le decisioni su fonti, audit e codice sono integrate con i protocolli della cartella `docs/`.

## Scopo

Ogni capitolo deve costruire un modello mentale eseguibile. Il lettore deve poter:

- ricostruire il flusso;
- localizzare ogni componente;
- dire cosa entra e cosa esce;
- descrivere l'ordine reale delle operazioni;
- indicare shape e invarianti;
- prevedere cosa cambia quando una parte viene modificata;
- dire cosa il meccanismo non fa.

Riconoscere i termini non basta. La spiegazione riesce soltanto quando il lettore può ripetere il meccanismo partendo dall'esempio originale, applicarlo a un caso modificato e delimitarne il comportamento.

## Principio centrale

Si porta un oggetto concreto dall'apertura alla ricostruzione finale.

Ogni passaggio principale deve:

1. partire dall'output esatto del passaggio precedente;
2. aggiungere una sola distinzione, operazione, relazione o struttura;
3. eseguire l'aggiunta sull'esempio continuo;
4. mostrare lo stato accumulato completo;
5. consegnare quello stato direttamente al passaggio successivo.

La progressione deve essere osservabile:

```text
oggetto noto
-> oggetto noto più una distinzione
-> stato precedente più una operazione
-> stato precedente più un risultato
-> modello eseguibile completo
```

Non si scrivono saggi tematici indipendenti all'interno dello stesso capitolo. Una sezione che può essere spostata altrove senza rompere l'esecuzione probabilmente non appartiene alla struttura portante.

## La catena dei sette punti

La spiegazione centrale collega, nell'ordine:

1. stato iniziale;
2. problema che non può essere risolto nello stato iniziale;
3. motivo per cui la nuova operazione viene introdotta in quel punto;
4. trasformazione concreta, nell'ordine reale di esecuzione;
5. stato risultante;
6. invariante che deve restare vero;
7. ciò che manca ancora intenzionalmente.

I punti 1, 5 e 6 devono essere presenti sia nella prosa sia nella bussola del capitolo:

```text
Stato prima:
Stato dopo:
Invariante:
```

L'invariante non viene lasciato implicito. Quando un'operazione modifica i valori ma non il numero di token, la shape esterna o l'ordine della sequenza, il testo lo dichiara nel punto in cui il lettore osserva la trasformazione.

## Stato del lettore

Ogni paragrafo sposta il lettore tra stati di conoscenza:

| Stato | Significato |
|---|---|
| Stabile | Il lettore può già ricostruire l'oggetto o l'operazione. |
| Corrente | L'oggetto esatto esaminato in quel momento. |
| Nuovo | Un solo concetto introdotto nel passaggio. |
| Stabilizzato | Il lettore ha visto il concetto eseguito e può descrivere la transizione. |
| Differito | Dipendenza o variante reale rimandata intenzionalmente. |

Prima di scrivere una sezione si compila:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```

La sezione successiva può dipendere soltanto da concetti stabili o stabilizzati. I concetti differiti possono essere nominati come confini, non usati come prerequisiti impliciti.

## Struttura portante universale

Ogni capitolo segue questi movimenti:

1. **Ancora.** Parte dall'ultimo oggetto che il lettore target può ricostruire.
2. **Mostra il gap.** Dimostra una capacità mancante, un fallimento o un vincolo.
3. **Esegue la transizione minima.** Applica una sola operazione reale a un oggetto concreto.
4. **Nomina e contratta.** Introduce il termine tecnico dopo che il meccanismo è visibile.
5. **Ripete e scala.** Generalizza una dimensione alla volta.
6. **Formalizza e collega.** Aggiunge shape, formule, codice e varianti dopo la stabilizzazione.
7. **Ricostruisce e trasferisce.** Ricompone il percorso completo e lo applica a un caso modificato.

Ogni sezione di meccanismo segue:

```text
ORIENTA -> INTRODUCI -> ESEGUI -> REINTEGRA -> CONTROLLA
```

## Blocco atomico di spiegazione

Per ogni transizione importante si usa il seguente contratto:

```text
Dove siamo:
Problema:
Input e shape:
Trasformazione:
Output e shape:
Cosa è cambiato:
Cosa è rimasto invariato:
Cosa non fa:
Cosa usa l'output dopo:
Esempio minimo:
Errore comune:
Frase di continuità:
```

La frase di continuità deve essere concreta:

```text
Ora che abbiamo ottenuto X, il componente successivo può usare X per fare Y.
```

Se `X` o `Y` non identificano un oggetto o un'operazione precisa, la sezione non è pronta.

## Gate di comparsa

Ogni elemento nuovo entra soltanto dopo che il suo referente concreto è stabile.

### Gate del termine

Un termine tecnico può comparire quando:

1. il lettore ha visto l'oggetto o l'operazione;
2. il testo assegna al termine un significato stabile;
3. le sezioni successive usano il termine nello stesso modo.

Si descrive prima di nominare.

### Gate dell'astrazione

Parole come `rappresentazione`, `contesto`, `significato`, `feature`, `memoria` ed `efficienza` richiedono un referente concreto:

```text
quali valori
in quale oggetto
prodotti da quale operazione
usati da quale calcolo successivo
```

Un'astrazione non spiega se stessa.

### Gate delle frecce

Le catene con frecce sono riassunti, non prime spiegazioni. Prima di mostrare:

```text
A -> B -> C
```

il lettore deve sapere:

- cosa sono `A`, `B` e `C`;
- cosa rappresenta ogni freccia;
- quale operazione viene eseguita;
- cosa cambia a ogni transizione;
- cosa resta invariato.

### Gate di simboli e formule

La matematica viene introdotta nell'ordine:

```text
domanda in linguaggio naturale
-> esempio numerico
-> tabella o shape
-> pseudocodice
-> formula
-> derivazione, quando necessaria
```

Ogni simbolo deve avere prima una quantità concreta visibile. Una formula entra soltanto se aiuta a calcolare, verificare o prevedere qualcosa.

### Gate del codice

Il codice compare dopo che l'operazione indipendente dalla libreria è stabile.

Ogni blocco deve identificare:

- input noto;
- riga che implementa l'operazione centrale;
- output osservabile;
- invariante;
- versione della libreria;
- file e test associati.

### Gate delle varianti

Varianti, ottimizzazioni, eccezioni e differenze implementative compaiono dopo il caso base. Quando l'accuratezza richiede di nominare prima una variante, la variante viene dichiarata come confine e rinviata.

## Profili di capitolo

La struttura portante viene adattata alla domanda dominante:

| Profilo | Percorso dominante |
|---|---|
| Componente | input corrente -> capacità mancante -> esecuzione -> contratto -> shape -> prossimo consumer |
| Processo | stato iniziale -> trigger -> transizione -> invariante -> ripetizione o stop -> stato finale |
| Architettura | mappa globale -> confini -> interfacce -> data flow -> parametri e stato -> fasi |
| Metodo di training | modello prima dell'update -> segnale obiettivo -> loss -> gradiente -> update -> stato dopo |
| Tecnica | baseline -> collo di bottiglia -> singola modifica -> comportamento invariato -> nuovo costo -> trade-off |
| Paper | domanda -> baseline -> proposta -> setup -> risultato -> limite -> riproduzione |
| Confronto | livello condiviso -> input comune -> differenza controllata -> conseguenza -> condizione d'uso |
| Implementazione | algoritmo invariante -> strutture dati -> pseudocodice -> codice verificato -> test -> failure case |

## Regole di scrittura

- Italiano calmo, preciso e progressivo.
- Il testo deve sembrare scritto direttamente in italiano, non tradotto.
- I termini tecnici standard restano in inglese quando sono l'uso corretto, per esempio `token`, `embedding`, `attention`, `training`, `inference`, `shape`, `input`, `output`, `language model`, `Transformer` e `PyTorch`.
- Non si usano em dash. Si usano punto, virgola, due punti, punto e virgola o parentesi.
- Si spiega perché un componente serve prima di spiegare come funziona.
- Un concetto nuovo per passaggio.
- Una sola trasformazione principale per paragrafo.
- Input, operazione, output, eccezione e sviluppi futuri non vengono compressi in una sola frase.
- I soggetti e i referenti sono espliciti.
- Si evitano pronomi ambigui quando sono presenti più tensor, operazioni o stati.
- Si preferiscono nomi concreti e verbi operativi.
- Il linguaggio antropomorfico viene tradotto nell'operazione numerica realmente eseguita.
- Non si usano hype, keyword stuffing, introduzioni generiche o citazioni finte.
- Un elenco di componenti non sostituisce una spiegazione causale.
- Gli elenchi puntati servono per informazioni senza ordine necessario.
- Gli elenchi numerati servono per procedure o ragionamenti in cui l'ordine conta.
- Comportamento implementato, valori illustrativi, risultati eseguiti e sviluppi futuri restano distinti.
- Una formulazione più semplice non deve eliminare condizioni o far sembrare completo un meccanismo parziale.
- Una frase tecnica senza fonte o prova non entra nella versione approvata.
- Non si colmano lacune con inferenze editoriali.

## Niente metafore

Non si usano:

- metafore;
- analogie con oggetti estranei al meccanismo;
- personificazioni;
- etichette infantili;
- domande retoriche usate al posto di una spiegazione.

Si descrivono direttamente codice, tensor, vocabolario, distribuzioni e comportamento del modello.

Restano ammessi verbi tecnici consolidati che indicano operazioni reali, per esempio:

- il modello predice;
- il layer proietta;
- la maschera azzera o esclude;
- l'optimizer aggiorna.

Questi verbi nominano un calcolo, non attribuiscono intenzione.

## Persona e voce

La prosa è impersonale oppure usa la prima persona plurale per le operazioni eseguite nel testo:

```text
prendiamo la sequenza
chiamiamo n la lunghezza
calcoliamo i punteggi
```

La seconda persona è riservata ai controlli di comprensione e agli esercizi. Fuori da questi punti viene evitata quando aggiunge soltanto riempitivo.

# Grammatica visuale

## Principio

Le visuali fanno parte della spiegazione. Ogni immagine risponde a una sola domanda dichiarata.

La prosa usa ogni visuale in tre fasi:

1. **Inquadra.** Dichiara la domanda a cui la figura risponde.
2. **Ispeziona.** Attraversa gli elementi etichettati nell'ordine di lettura.
3. **Conclude.** Dichiara il risultato e il prossimo consumer.

Una caption non sostituisce la spiegazione.

## Strumento di produzione

I diagrammi tecnici vengono creati con lo strumento immagini.

- Artefatto editoriale principale: PNG ad alta risoluzione.
- Gli SVG non sono il formato principale.
- La prima generazione è sempre una bozza.
- Ogni immagine viene revisionata e, quando necessario, modificata o rigenerata.
- Gli asset finali non contengono watermark, firme, loghi o branding di terzi.
- Le immagini di riferimento definiscono un linguaggio didattico, non un layout da copiare.

## Stile visuale

Le visuali devono privilegiare:

- sfondo chiaro o neutro adatto alla pagina;
- blocchi con ruoli espliciti;
- frecce con origine e destinazione inequivocabili;
- gerarchia visiva stabile;
- testo grande e leggibile;
- spaziatura sufficiente;
- densità coerente con la funzione didattica;
- una sola operazione non ancora insegnata;
- label identiche alla prosa;
- shape visibili quando necessarie.

## Semantica dei colori

Il colore non è mai l'unico portatore di significato.

| Ruolo | Colore consigliato | Requisito testuale |
|---|---|---|
| Input e parametri | neutro o grigio | label `Input` o nome del parametro |
| Operazione corrente | blu | nome dell'operazione |
| Output | verde o blu distinto | label `Output` e nome del tensor |
| Vincolo o mask | ambra | label `Vincolo`, `Mask` o descrizione equivalente |
| Errore o stato invalido | rosso | label testuale esplicita |
| Elemento illustrativo | neutro attenuato | badge `Illustrativo` |
| Risultato misurato | verde con badge | badge `Verificato` o `Eseguito`, con setup |

Il verde non implica automaticamente che un valore sia stato misurato. La provenienza deve essere scritta.

## Badge e provenienza

Badge ammessi:

| Badge | Significato |
|---|---|
| `Input` | oggetto che entra in un'operazione |
| `Operazione` | calcolo in esame |
| `Vincolo` | limite o condizione |
| `Output` | oggetto prodotto |
| `Eseguito` | risultato ottenuto dal codice e dall'ambiente registrati |
| `Verificato` | valore misurato con setup e fonte dichiarati |
| `Confine` | comportamento non implementato |
| `Illustrativo` | valore costruito per l'esempio |

Un valore illustrativo deve essere matematicamente coerente anche quando non deriva da una misura.

## Scelta della rappresentazione

Si usa lo strumento più semplice che rappresenta correttamente la relazione.

| Strumento | Serve per | Non serve per |
|---|---|---|
| Immagine generata | architetture, processi, flussi tensoriali, confronti spaziali e relazioni tra componenti | formule da calcolare o tabelle esatte molto piccole |
| Formula tipografica | notazione, derivazioni, regole simboliche e complessità | layout o processi |
| Tabella Markdown | confronti piccoli ed esatti | processi lunghi o grafi |
| Blocco di codice | codice, output letterale e serializzazioni | relazioni che richiedono nodi e frecce |
| Matrice o griglia nel testo | operazioni numeriche compatte | mappe generali del sistema |

Non si crea un'immagine soltanto perché una sezione ne è priva.

## Tipi di visuale

Tipi ricorrenti:

- architecture diagram;
- process diagram;
- tensor e shape diagram;
- matrix operation;
- comparison diagram;
- algorithm flow;
- benchmark o trade-off chart.

Un nuovo tipo viene introdotto soltanto quando un contenuto reale lo richiede.

## Regole di ammissione visuale

Una visuale è ammessa soltanto quando:

- tutte le label sono note o introdotte subito accanto;
- contiene al massimo una trasformazione non ancora insegnata;
- il colore non è l'unico significato;
- i valori illustrativi sono dichiarati;
- i valori misurati indicano ambiente, modello, checkpoint, comando e data quando pertinenti;
- il capitolo dichiara cosa cambia e cosa resta invariato;
- la stessa informazione è disponibile in testo o markup semantico;
- il testo è leggibile alla dimensione editoriale prevista;
- ogni linea ha una funzione univoca;
- una callout non può essere scambiata per un flusso dati.

Non si mostra l'output di un meccanismo prima che il capitolo abbia stabilito perché quell'output serve.

## Collegamenti e frecce

Ogni freccia deve avere:

- sorgente precisa;
- destinazione precisa;
- direzione leggibile;
- significato dichiarato;
- percorso che non suggerisce giunzioni inesistenti.

Si controllano in particolare:

- ramificazioni;
- ricomposizioni;
- residual path;
- skip connection;
- mask;
- feedback loop;
- percorsi di `Q`, `K` e `V`;
- collegamenti tra score, bias, softmax e output;
- flussi di gradiente quando rappresentati.

Una linea che attraversa un'altra non deve sembrare collegata. Quando l'incrocio è inevitabile, la separazione deve essere visivamente esplicita.

## Accessibilità e adattamento editoriale

Ogni immagine finale include:

- alt text breve;
- equivalente testuale esteso;
- ordine di lettura;
- spiegazione della provenienza dei numeri;
- significato che non dipende dal colore.

Si verifica:

- leggibilità in pagina;
- leggibilità su schermi ridotti quando il libro viene pubblicato digitalmente;
- assenza di testo tagliato;
- pedici e apici leggibili;
- contrasto sufficiente;
- impossibilità di confondere vicinanza e connessione.

## Audit visuale obbligatorio

Prima dell'approvazione si controllano:

1. formule;
2. numeri;
3. shape;
4. origine di ogni freccia;
5. destinazione di ogni freccia;
6. incroci e giunzioni apparenti;
7. semantica di mask e vincoli;
8. distinzione tra flusso dati e annotazione;
9. corrispondenza con la prosa;
10. corrispondenza con il codice;
11. ordine di lettura;
12. densità;
13. allineamento;
14. spaziatura;
15. dimensione del testo;
16. uso non esclusivo del colore;
17. alt text;
18. assenza di watermark e branding.

Dopo ogni modifica si ripete l'intero audit. Non si controllano soltanto i difetti precedenti.

## Stati delle visuali

```text
storyboard
bozza vN
da modificare
da rigenerare
validata tecnicamente
approvata
```

Una visuale validata tecnicamente può essere ancora respinta per ragioni didattiche o compositive.

# Integrazione del codice nella spiegazione

## Principio

Il codice collega il meccanismo a un'implementazione osservabile. Non sostituisce la prosa e non introduce un secondo percorso concettuale.

## Regole

- Il codice entra dopo il meccanismo concreto.
- Python e PyTorch sono predefiniti.
- NumPy può verificare calcoli elementari.
- Pseudocodice e codice eseguibile sono distinti.
- Uno snippet mostra una sola operazione centrale.
- Import, input, shape e output sono espliciti.
- Le variabili coincidono con la prosa.
- Le API vengono controllate nella documentazione ufficiale della versione dichiarata.
- Gli snippet vengono eseguiti e testati.
- Gli output inventati non vengono presentati come eseguiti.

## Presentazione dello snippet

Prima del codice il testo dichiara:

1. input noto;
2. riga centrale;
3. output o invariante da osservare.

Dopo il codice spiega soltanto ciò che collega l'implementazione al meccanismo.

# Check finali di comprensione

Ogni capitolo chiude verificando:

| Check | Azione richiesta |
|---|---|
| Ricostruzione | Ricostruire la transizione dall'input originale. |
| Localizzazione | Dire cosa viene prima e dopo il meccanismo. |
| Confine | Dire cosa il meccanismo non fa. |
| Trasferimento | Applicarlo a un nuovo input o parametro. |
| Variazione | Prevedere l'effetto di rimozione, sostituzione o cambio di parametro. |

Se il lettore non può rispondere, si torna all'ultimo punto stabile e si ripara la giunzione. Non si aggiunge altro materiale sopra una transizione non stabilizzata.

# Istruzione compatta

```text
Costruisci il capitolo come una sequenza di transizioni nello stato del lettore.

Ancora il capitolo all'ultimo oggetto stabile. Dimostra un gap concreto. Esegui la più piccola operazione reale prima di nominarla. Porta un oggetto concreto dal primo paragrafo alla ricostruzione finale. Ogni passaggio parte dall'output esatto del precedente, aggiunge una sola cosa e mostra lo stato accumulato completo. Registra prima, azione, dopo, cambiato, invariato e confine. Generalizza una dimensione alla volta. Introduci termini, simboli, frecce, formule, codice, varianti e visuali soltanto dopo che i referenti concreti sono stabili. Verifica ogni affermazione nelle fonti, ogni calcolo con una derivazione o un'esecuzione, ogni immagine con audit iterativo e ogni snippet con test. Reintegra ogni output nel sistema più grande. Verifica ricostruzione, localizzazione, confine, trasferimento e variazione. Mantieni il capitolo come bozza finché non supera le review tecniche e la revisione autoriale.
```