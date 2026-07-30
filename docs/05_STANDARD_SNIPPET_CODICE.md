# Standard per gli snippet di codice

## Scopo

Gli snippet devono collegare direttamente il meccanismo spiegato nel capitolo a una implementazione osservabile. Non sostituiscono la spiegazione e non devono introdurre un secondo percorso concettuale.

Il codice principale usa Python e PyTorch. NumPy può essere usato per esempi numerici elementari o per verifiche indipendenti. Pseudocodice e codice eseguibile devono essere etichettati in modo distinto.

## Applicazione per capitolo

Ogni capitolo tecnico deve includere almeno uno snippet eseguibile collegato a una trasformazione centrale del capitolo.

Un capitolo intrinsecamente non computazionale può non includere codice soltanto quando:

- l'eccezione è motivata nei metadati;
- nessuno snippet utile può rappresentare correttamente il contenuto;
- l'assenza viene approvata nella revisione autoriale.

Non si aggiunge codice decorativo soltanto per soddisfare un conteggio.

## Dimensione e ruolo

La forma predefinita è uno snippet breve e autosufficiente, normalmente compreso tra circa 8 e 40 righe significative. Il limite non è rigido. La priorità è mostrare una sola operazione centrale senza nascondere dipendenze necessarie.

Script più lunghi vengono mantenuti nel repository quando servono per:

- riprodurre un esperimento;
- eseguire benchmark;
- addestrare un modello;
- gestire dataset o checkpoint;
- confrontare più implementazioni;
- verificare comportamento su hardware specifico.

Nel corpo del capitolo viene mostrata soltanto la porzione necessaria a comprendere il meccanismo. Il file completo viene referenziato.

## Contratto di ogni snippet

Ogni snippet deve dichiarare:

```text
ID:
Sezione del capitolo:
Domanda a cui risponde:
Input noto:
Shape iniziali:
Operazione centrale:
Output osservabile:
Invariante:
Versione Python:
Versione PyTorch o libreria:
Device:
Dtype:
Seed, quando rilevante:
Fonte API ufficiale:
File completo:
Test associato:
Stato audit:
```

## Regole di scrittura

- Una sola operazione principale per snippet.
- Variabili coerenti con la prosa e con le formule.
- Shape visibili nei commenti o nelle asserzioni.
- Nessuna dipendenza implicita da celle precedenti di un notebook.
- Import completi e minimi.
- Commenti in italiano, termini API mantenuti nella forma ufficiale.
- Nessun output inventato presentato come risultato di esecuzione.
- Nessuna API scritta sulla base della memoria. Firma, argomenti e comportamento vengono controllati sulla documentazione ufficiale della versione dichiarata.
- Nessun blocco definito `PyTorch` quando contiene soltanto pseudocodice.
- Nessun comportamento hardware-specifico presentato come verificato senza esecuzione nell'ambiente dichiarato.

## Ambiente predefinito

Gli snippet didattici devono essere eseguibili su CPU quando il meccanismo non richiede una GPU. Il codice specifico per CUDA, acceleratori, mixed precision, kernel fused o distributed training viene separato e accompagnato dall'ambiente necessario.

Ogni esecuzione registra almeno:

- sistema operativo o immagine ambiente;
- versione Python;
- versione della libreria;
- device;
- dtype;
- seed;
- comando di esecuzione;
- data;
- output atteso o proprietà verificate.

## Struttura consigliata

```text
chapters/<capitolo>/code/
  README.md
  <SNIPPET-ID>.py
  <SNIPPET-ID>_test.py
  CODE_AUDIT.md
  outputs/
  environments/
```

Il capitolo può includere lo snippet direttamente e referenziare il file corrispondente nel repository.

## Tipi di snippet

### 1. Snippet esplicativo minimo

Mostra l'operazione centrale con input piccoli e leggibili.

### 2. Snippet di verifica

Controlla formula, shape, normalizzazione, maschera, gradiente o altro invariante tramite `assert` o test.

### 3. Implementazione da zero

Implementa il meccanismo usando operazioni tensoriali primitive, dopo che il lettore ha stabilizzato l'algoritmo.

### 4. Implementazione con API ufficiale

Mostra l'equivalente tramite un'API verificata della libreria e confronta i risultati con l'implementazione da zero quando il confronto è valido.

### 5. Snippet hardware-specifico

Mostra comportamento che dipende da GPU, dtype, kernel o backend. Deve dichiarare ambiente e limiti. Non viene incluso come eseguibile verificato se l'ambiente necessario non è stato realmente usato.

### 6. Script di riproduzione

Riproduce un esperimento o un benchmark più ampio. Rimane nel repository e il capitolo mostra soltanto l'estratto necessario.

## Ciclo di review del codice

### 1. Verifica della fonte

Si controllano documentazione ufficiale, firma dell'API, note di versione ed eventuali differenze tra documentazione e implementazione.

### 2. Ispezione statica

Si controllano:

- import;
- nomi;
- shape;
- broadcasting;
- dtype;
- device;
- gestione della casualità;
- gradienti;
- mask;
- condizioni limite;
- eventuali side effect.

### 3. Esecuzione pulita

Lo snippet viene eseguito da un processo nuovo, senza stato precedente. Un codice che funziona soltanto dopo l'esecuzione implicita di altre celle viene respinto.

### 4. Test degli invarianti

Vengono aggiunte asserzioni per le proprietà spiegate nel testo, per esempio:

- shape attesa;
- somme di probabilità;
- equivalenza entro tolleranza;
- assenza di accesso a posizioni mascherate;
- determinismo quando previsto;
- presenza dei gradienti;
- comportamento su input non valido.

### 5. Confronto indipendente

Quando possibile, il risultato viene confrontato con:

- una implementazione diretta della formula;
- un'API ufficiale;
- un calcolo NumPy;
- un valore manuale su input minimo.

### 6. Audit di coerenza editoriale

Si verifica che lo snippet implementi esattamente l'operazione descritta, senza introdurre ottimizzazioni, parametri o varianti non ancora spiegate.

Nomi, shape, numeri, ordine delle operazioni, invarianti e confini devono coincidere con prosa, formule e immagini.

### 7. Nuova esecuzione dopo le correzioni

Ogni modifica richiede una nuova esecuzione completa e il riesame dei test. Non si assume che una correzione locale lasci invariato il resto.

### 8. Controllo temporale

Prima dell'approvazione si ricontrollano:

- versione corrente della documentazione;
- firma dell'API;
- deprecazioni;
- note di rilascio;
- differenze tra backend.

## Stati di audit

- `bozza`;
- `da correggere`;
- `eseguito`;
- `test superati`;
- `allineato al capitolo`;
- `approvato`.

## Difetti bloccanti

Uno snippet non può essere approvato se presenta almeno uno dei seguenti problemi:

- non è stato eseguito nell'ambiente dichiarato;
- usa una firma API non verificata;
- output, formula o shape non coincidono con il testo;
- dipende da stato nascosto;
- manca un import necessario;
- produce un risultato casuale senza seed quando il confronto richiede ripetibilità;
- usa broadcasting non dichiarato;
- confonde mask booleane e additive;
- confronta tensor con dtype o device incompatibili senza spiegarlo;
- mostra un output atteso non ottenuto dall'esecuzione;
- presenta pseudocodice come eseguibile;
- presenta codice hardware-specifico non verificato sull'hardware dichiarato;
- è tanto lungo da nascondere il meccanismo quando una versione più piccola è possibile;
- usa una versione diversa da quella dichiarata;
- contraddice testo, formula o immagine.

## Presentazione nel capitolo

Ogni snippet nel libro viene introdotto con tre frasi operative:

1. quale input già noto utilizza;
2. quale riga implementa il calcolo centrale;
3. quale output o invariante deve essere osservato.

Dopo il blocco vengono spiegati soltanto gli elementi necessari a collegare codice e meccanismo. Il capitolo non commenta riga per riga istruzioni già evidenti.

## Output e provenienza

Un output mostrato nel capitolo porta una delle due etichette:

- `Eseguito`: prodotto dal file e dall'ambiente registrati;
- `Illustrativo`: costruito per spiegare il formato, non ottenuto da una esecuzione.

L'etichetta `Eseguito` non viene usata senza log o test associati nel repository.

## Gate di approvazione

Uno snippet è approvato soltanto quando:

- la fonte API è verificata;
- l'ambiente è registrato;
- l'esecuzione pulita riesce;
- i test passano;
- il confronto indipendente, quando applicabile, è coerente;
- il codice coincide con il capitolo;
- output e provenienza sono registrati;
- `CODE_AUDIT.md` riporta esito positivo.