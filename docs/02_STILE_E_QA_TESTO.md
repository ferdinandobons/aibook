# Stile, didattica e qualità del testo

## Stato

- Stato: `vincolante`
- Ambito: capitoli, appendici, formule, tabelle, snippet e testo destinato al lettore
- Lingua: italiano
- Artefatto di pianificazione: `PLAN.md`
- Artefatto di review: `TEXT_AUDIT.md`
- Fonte metodologica archiviata: `source/`

## 1. Obiettivo

Il libro è un manuale tecnico, non una specifica, una reference API, un registro di audit o una raccolta di schede.

Ogni capitolo deve costruire un modello mentale che il lettore possa ricostruire e applicare. Alla fine di un meccanismo, il lettore deve poter:

- riconoscere l'input;
- descrivere l'ordine reale delle operazioni;
- localizzare componenti e interfacce;
- indicare output, shape e invarianti;
- spiegare che cosa cambia e che cosa resta invariato;
- dichiarare i confini;
- prevedere una variazione controllata;
- collegare il testo a visuali e codice verificato.

La verifica resta rigorosa negli artefatti interni. La superficie destinata al lettore deve risultare continua, leggibile e naturale in italiano.

## 2. Oggetto continuo e progressione

Un oggetto concreto attraversa il capitolo dall'apertura alla ricostruzione finale.

Ogni passaggio principale:

1. parte da ciò che il lettore ha appena stabilizzato;
2. introduce una sola distinzione, operazione o struttura dominante;
3. applica il nuovo elemento allo stesso esempio;
4. rende disponibile lo stato accumulato;
5. consegna il risultato al passaggio successivo.

La progressione interna deve poter essere ricostruita come:

```text
oggetto noto
-> oggetto noto più una distinzione
-> stato precedente più una operazione
-> stato precedente più un risultato
-> modello eseguibile completo
```

Una sezione che può essere spostata altrove senza interrompere il percorso deve essere valutata come ponte, approfondimento, riferimento incrociato o capitolo distinto.

## 3. Catena causale

La spiegazione collega, nel significato:

1. stato iniziale;
2. capacità mancante o problema;
3. motivo della nuova operazione;
4. trasformazione concreta;
5. stato risultante;
6. invariante;
7. elemento ancora mancante.

Questi punti non diventano sette titoli obbligatori. Devono essere ricostruibili nella prosa.

## 4. Scaffold interno e testo pubblico

### 4.1 `PLAN.md`

Prima della stesura si registrano:

```text
Domanda centrale:
Oggetto continuo:
Stato iniziale:
Gap:
Output finale:
Invarianti principali:
Confini:
Concetti differiti:
Consumer successivo:
Visuali previste:
Snippet previsti:
```

Per ogni transizione portante:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Input e shape:
Operazione:
Output e shape:
Cosa cambia:
Cosa resta invariato:
Cosa non fa:
Chi usa l'output:
Esempio o prova:
Errore comune:
Giunzione con il passaggio successivo:
```

Lo scaffold è obbligatorio per progettazione e review. Non determina i titoli visibili.

### 4.2 `CHAPTER.md`

Il capitolo destinato al lettore contiene:

- titolo e apertura;
- spiegazione in prosa;
- formule e tabelle necessarie;
- visuali tecniche;
- snippet essenziali;
- riepilogo, verifiche ed esercizi;
- fonti principali e rinvio ai materiali riproducibili.

Non interrompono il flusso:

- stato editoriale;
- versione candidata;
- date di lavorazione;
- esiti degli audit;
- branch e commit;
- nomi delle bozze respinte;
- elenco completo dei file interni;
- dettagli di riproducibilità non necessari alla comprensione.

Questi dati restano in commenti HTML non renderizzati, `PLAN.md`, `TEXT_AUDIT.md`, `CHANGELOG.md`, `REVIEW.md` o nei file del codice.

Formato consigliato per i metadati nascosti:

```text
<!--
chapter_id:
part_id:
order_key:
title:
maturity:
status:
version:
last_source_check:
environment:
deferred:
-->
```

Il capitolo non apre con `Stato della candidatura` e non chiude con `Registro di approvazione`.

## 5. Architettura delle sezioni

Le sezioni seguono domande, problemi, oggetti e meccanismi reali. Non si crea una sezione per ogni micro-operazione.

Una sezione principale è giustificata quando cambia almeno uno tra:

- domanda;
- oggetto osservato;
- livello di astrazione;
- fase del processo;
- tipo di evidenza;
- destinazione del risultato.

Una singola sezione può contenere più passaggi brevi che appartengono allo stesso movimento concettuale.

Da cinque a dieci sezioni principali sono un riferimento editoriale per un capitolo tecnico ordinario, non un limite rigido.

Segnali di frammentazione:

- molte sezioni di uno o due paragrafi;
- un titolo per ogni operazione aritmetica;
- sequenze ripetute `definizione -> cautela -> nuovo titolo`;
- titoli che descrivono il metodo di scrittura invece del contenuto;
- fonti, artefatti e registri separati in numerosi blocchi finali.

Titoli adatti:

```text
Perché una combinazione fissa non basta
Dal confronto ai coefficienti
Escludere le posizioni future
Dalla formula all'implementazione
```

Titoli da non usare come telaio ricorrente:

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

Una singola etichetta può comparire quando è davvero la forma più chiara. La ripetizione sistematica viene respinta.

## 6. Costruzione del paragrafo

Un paragrafo può collegare naturalmente:

1. stato raggiunto;
2. problema rimasto;
3. nuovo passaggio;
4. conseguenza;
5. limite necessario;
6. continuità con ciò che segue.

Esempio:

```text
I tre prodotti scalari forniscono uno score per ogni key, ma questi valori non sono ancora coefficienti: possono essere negativi e non sommano a uno. Li dividiamo quindi per la radice della dimensione delle key e applichiamo la softmax. Otteniamo tre coefficienti associati alle stesse coppie key-value; soltanto a questo punto possiamo usarli per costruire l'output.
```

Il paragrafo conserva la sequenza tecnica senza esporre un modulo compilato.

## 7. Stato del lettore

Per la review interna si distinguono:

| Stato | Significato |
|---|---|
| Stabile | Il lettore può ricostruire l'oggetto o l'operazione. |
| Corrente | L'oggetto esaminato nel passaggio. |
| Nuovo | L'unico concetto introdotto ora. |
| Stabilizzato | Il concetto è stato eseguito e può essere descritto. |
| Differito | Variante o dipendenza rimandata intenzionalmente. |

La scheda appartiene al piano e all'audit, non alla pagina del manuale.

## 8. Gate di comparsa

### 8.1 Termine tecnico

Un termine compare quando:

1. il lettore ha visto l'oggetto o l'operazione;
2. il testo gli assegna un significato stabile;
3. le sezioni successive lo usano nello stesso modo.

Si descrive prima di nominare.

### 8.2 Astrazione

Parole come `rappresentazione`, `contesto`, `feature`, `memoria` ed `efficienza` richiedono un referente concreto:

- quali valori;
- in quale oggetto;
- prodotti da quale operazione;
- usati da quale calcolo successivo.

### 8.3 Frecce

Le catene con frecce sono riassunti. Prima di mostrare `A -> B -> C`, il lettore deve conoscere nodi, operazioni e cambiamenti.

### 8.4 Matematica

Quando pertinente, l'ordine è:

```text
domanda naturale
-> esempio osservabile o numerico
-> valori e shape
-> algoritmo o pseudocodice
-> formula generale
-> derivazione necessaria
```

Ogni simbolo deve avere prima una quantità concreta visibile.

### 8.5 Codice

Il codice compare dopo il meccanismo indipendente dalla libreria. La prosa chiarisce input, operazione centrale e risultato da osservare. Il contratto completo resta negli artefatti del codice.

### 8.6 Varianti

Varianti, ottimizzazioni ed eccezioni compaiono dopo il caso base. Una variante necessaria soltanto per localizzare un confine viene nominata e rinviata.

## 9. Profili di capitolo

La struttura visibile si adatta al soggetto.

| Profilo | Percorso dominante |
|---|---|
| Componente | input -> capacità mancante -> esecuzione -> contratto -> componente successivo |
| Processo | stato iniziale -> trigger -> transizione -> invariante -> ripetizione o stop |
| Architettura | mappa globale -> moduli -> interfacce -> flusso -> parametri e stato |
| Training | modello prima dell'update -> segnale -> loss -> gradiente -> update |
| Tecnica | baseline -> collo di bottiglia -> modifica -> comportamento invariato -> trade-off |
| Paper | domanda -> baseline -> proposta -> setup -> risultato -> limite -> riproduzione |
| Confronto | livello comune -> differenza controllata -> conseguenza -> condizione d'uso |
| Implementazione | algoritmo -> strutture dati -> pseudocodice -> codice -> test -> failure case |

Capitoli diversi non vengono forzati nella stessa sagoma.

## 10. Voce editoriale

### 10.1 Principi

- Italiano calmo, preciso e progressivo.
- Testo scritto direttamente in italiano, non tradotto.
- Termini tecnici standard in inglese quando appropriato.
- Nessun em dash.
- Soggetti e referenti espliciti.
- Nomi concreti e verbi operativi.
- Una trasformazione dominante per paragrafo.
- Nessun hype o keyword stuffing.
- Gli elenchi non sostituiscono una spiegazione causale.
- Esempio illustrativo, risultato eseguito e comportamento generale restano distinti.
- Una semplificazione non elimina condizioni necessarie.

### 10.2 Ritmo

La prosa alterna periodi brevi, medi e articolati. Una successione di frasi tutte della stessa lunghezza produce un ritmo meccanico. Periodi troppo lunghi rendono difficile localizzare l'operazione principale.

Regole:

- una frase esprime una relazione principale;
- condizioni ed eccezioni vengono separate quando competono con il meccanismo;
- soggetto e verbo restano vicini nei periodi tecnici densi;
- le liste vengono usate per ordine e confronto, non per evitare la prosa;
- le transizioni variano nella forma e nominano l'oggetto ottenuto.

Non è obbligatorio iniziare ogni passaggio con `Ora che`, `A questo punto` o `Quindi`.

### 10.3 Italiano idiomatico

Evitare, quando non necessari:

```text
consumer
ancora operativa
dimensione da annotare
meccanismo stabilizzato
contratto algoritmico
ambiente registrato
obiettivo modellato
ampiezza del riuso
```

Preferire:

```text
posizione o componente che usa il risultato
riferimento operativo
aspetto da osservare
meccanismo appena costruito
ordine delle operazioni
ambiente in cui il codice è stato eseguito
risultato o relazione descritta dal modello
varietà dei compiti e dei contesti d'uso
```

`Token`, `embedding`, `attention`, `training`, `inference`, `checkpoint`, `loss`, `optimizer`, `batch` e `shape` possono restare in inglese. La sintassi della frase resta italiana.

### 10.4 Precisione senza rigidità

Le condizioni indispensabili entrano nel punto in cui servono. Le cautele secondarie vengono spostate in una nota, in un box `Da non confondere`, in un approfondimento o negli audit.

La stessa cautela non viene ripetuta nel corpo, nel riepilogo e negli errori comuni, salvo che svolga una funzione didattica distinta.

### 10.5 Esempio continuo

L'esempio non compare soltanto all'inizio e alla fine. Ogni nuova distinzione importante viene applicata all'oggetto già noto.

Se oggetti concettualmente diversi usano valori numerici identici, la prosa dichiara che l'uguaglianza serve soltanto a semplificare i conti.

### 10.6 Metafore e persona

Non si usano metafore, analogie estranee, personificazioni o domande retoriche al posto dell'operazione reale.

Sono ammessi verbi tecnici consolidati, come `il modello predice`, `il layer proietta` e `la maschera esclude`.

La prosa è impersonale oppure usa la prima persona plurale per operazioni svolte nel testo. La seconda persona è riservata a verifiche ed esercizi.

## 11. Citazioni nel flusso

Le citazioni restano vicino alle affermazioni che sostengono. I dettagli che interrompono il ragionamento vengono spostati nel dossier o nei file di riproduzione.

Nel corpo bastano, quando pertinenti:

- fonte e anno;
- sezione o pagina;
- versione dell'API necessaria;
- risultato indispensabile a comprendere il passaggio.

Sistema operativo, commit, comando completo, log, tolleranze e limitazioni hardware restano negli artefatti, salvo che cambino l'interpretazione del risultato.

## 12. Template del capitolo

Struttura file:

```text
chapters/<slug>/
  PLAN.md
  CHAPTER.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
  assets/
```

Possibile percorso del testo:

```text
Titolo
Apertura in prosa
Problema concreto
Meccanismo costruito per passaggi
Esempio continuo
Pseudocodice, quando utile
Formalizzazione
Implementazione
Varianti o confini pertinenti
Riepilogo
Verifiche ed esercizi
Fonti e materiali
```

Non esiste una sequenza obbligatoria identica per tutti i capitoli.

## 13. Classi di contenuto

Ogni elemento tecnico appartiene a una classe:

1. fatto sostenuto da fonte;
2. derivazione da definizioni verificate;
3. risultato riprodotto con ambiente e test;
4. esempio illustrativo dichiarato;
5. confine del meccanismo.

Una inferenza fattuale editoriale non entra nella versione approvata.

## 14. Review del testo

### 14.1 Artefatti

Ogni capitolo usa:

- `FONTI_PRIMARIE.md` per fonti e limiti;
- `CLAIMS.md` per la mappa frase-prova;
- `TEXT_AUDIT.md` per review e difetti;
- `CHANGELOG.md` per le modifiche sostanziali.

### 14.2 Audit fattuale

Per ogni periodo tecnico si controlla:

- quale parte è un fatto;
- quale fonte la sostiene;
- se la fonte dice realmente ciò che il testo afferma;
- se la formulazione è più forte della prova;
- se mancano condizioni o limiti;
- se paper, implementazione, checkpoint e prodotto sono distinti;
- se esiste una inferenza editoriale non ammessa.

### 14.3 Audit matematico

Si ricontrollano:

- definizioni;
- simboli;
- domini e shape;
- derivazioni;
- segni e fattori di scala;
- normalizzazioni;
- arrotondamenti;
- esempi numerici;
- condizioni di validità.

Quando possibile, i calcoli vengono verificati con codice indipendente.

### 14.4 Audit architetturale e algoritmico

Si controllano ordine e posizione di normalizzazioni, residual, mask, routing, caching, loss, gradienti, update, sampling e comunicazione.

Si distingue tra:

- metodo del paper;
- setup sperimentale;
- implementazione del repository;
- contratto della documentazione;
- comportamento di un checkpoint o prodotto.

### 14.5 Audit incrociato e temporale

Prosa, formule, visuali e codice coincidono per nomi, shape, numeri, ordine e confini.

Documentazione, API, release, report, errata e norme vengono ricontrollati prima dell'approvazione.

## 15. Review didattica

Ogni capitolo riceve almeno una review completa. La modalità predefinita usa più passaggi indipendenti.

### Passaggio 1. Struttura e gate

Controlla:

- oggetto continuo;
- catena causale;
- stato del lettore;
- gate di termini, formule, codice e varianti;
- una trasformazione dominante per passaggio;
- confini e concetti differiti;
- integrazione delle visuali;
- gate anti-template.

### Passaggio 2. Prosa e ricostruibilità

Dopo le correzioni, rilegge integralmente:

- ordine reale;
- referenti;
- densità;
- ritmo;
- continuità;
- stato accumulato;
- titoli;
- esercizi;
- coerenza tra artefatti;
- ricostruibilità senza consultare il piano.

La seconda review non si limita ai difetti già trovati.

## 16. Gate anti-template

Il capitolo viene respinto quando:

- ripete intestazioni metacognitive;
- espone il foglio di progettazione;
- spezza un meccanismo semplice in microsezioni;
- usa elenchi e box al posto della prosa;
- rende capitoli diversi formalmente identici;
- nasconde shape, invarianti o confini dopo la rimozione delle etichette.

La correzione trasferisce la logica nella prosa. Non la elimina.

## 17. Review editoriale e linguistica

Dopo la review tecnica e didattica viene eseguita una lettura completa come manuale.

Si controllano:

- fluidità tra paragrafi e sezioni;
- naturalezza dell'italiano;
- calchi dall'inglese;
- ripetizioni sintattiche;
- densità di sostantivi astratti;
- frequenza di negazioni e cautele;
- ritmo dei periodi;
- eccesso di titoli, tabelle, liste e blocchi;
- separazione tra testo pubblico e materiali operativi;
- continuità dell'esempio;
- leggibilità delle citazioni;
- comprensibilità ad alta voce.

### 17.1 Tre profili di lettore

La review simula almeno:

1. lettore che incontra il concetto per la prima volta;
2. lettore tecnico che verifica precisione e condizioni;
3. lettore che riprende il capitolo dopo tempo.

### 17.2 Lettura ad alta voce

Una frase difficile da pronunciare, che costringe a tornare indietro o che suona come una specifica viene riscritta anche quando è grammaticalmente corretta.

## 18. Visuali e codice nel testo

Una figura viene:

1. introdotta con la domanda a cui risponde;
2. attraversata nell'ordine di lettura;
3. conclusa con il risultato e il passo successivo.

Prima di uno snippet, la prosa rende chiari input, operazione centrale e controllo atteso. Le etichette editoriali non sono obbligatorie.

## 19. Verifiche finali

Il capitolo deve permettere:

- **ricostruzione**, ripetere il flusso dall'input;
- **localizzazione**, indicare dove opera un componente;
- **confine**, dire che cosa il meccanismo non fa;
- **trasferimento**, applicare il concetto a un nuovo caso;
- **variazione**, prevedere una modifica controllata.

## 20. Registro in `TEXT_AUDIT.md`

Ogni review registra:

```text
Review ID:
Versione esaminata:
Data:
Ambito:
Profili di lettore:
Difetti bloccanti:
Difetti non bloccanti:
Correzioni applicate:
Artefatti riaperti:
Lettura ad alta voce:
Esito:
Reviewer:
```

Stati ammessi:

```text
non eseguita
in corso
respinta
corretta, nuova review richiesta
superata
```

## 21. Difetti bloccanti

Un capitolo non può essere approvato se presenta:

- affermazione senza prova;
- citazione non pertinente;
- formula, shape o derivazione errata;
- esempio incoerente;
- API non verificata;
- termine o formula anticipati;
- codice prima del meccanismo;
- variante prima del caso base;
- più concetti non separati nella stessa transizione;
- invariante necessario implicito;
- visuale non attraversata dalla prosa;
- contraddizione tra artefatti;
- semplificazione falsa;
- struttura simile a una checklist;
- microsezioni eccessive;
- prosa burocratica, tradotta o meccanica;
- metadati operativi nel flusso del manuale;
- frase che non supera la lettura ad alta voce.

## 22. Gate di approvazione

Un capitolo passa alla revisione autoriale soltanto quando:

- claim portanti verificati;
- audit tecnico positivo;
- review didattica completa;
- difetti bloccanti corretti;
- nuova review integrale eseguita;
- gate anti-template superato;
- review editoriale e linguistica superata;
- lettura ad alta voce superata;
- testo, visuali e codice seguono lo stesso percorso.

Una modifica strutturale o linguistica successiva riapre il gate.
