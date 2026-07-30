# Protocollo di qualità per le visuali

## Scopo

Ogni immagine tecnica deve ridurre l’ambiguità, non soltanto risultare gradevole. Una singola linea collegata al punto sbagliato può modificare il modello mentale del lettore. Per questo motivo nessuna prima generazione viene considerata finale.

## Ciclo obbligatorio

### 1. Specifica prima della generazione

Per ogni visuale vengono fissati:

- domanda unica;
- oggetto già noto al lettore;
- trasformazione nuova;
- nodi e ruoli;
- frecce e direzioni;
- shape;
- eventuali valori illustrativi;
- invariante;
- confine;
- prossimo consumer.

### 2. Generazione della bozza

La bozza viene prodotta con lo strumento immagini. Il prompt deve descrivere esplicitamente origine e destinazione delle frecce, linee che non devono toccarsi, elementi che non devono apparire e gerarchia di lettura.

### 3. Audit tecnico indipendente

La bozza viene riletta come se non fosse disponibile il prompt. Si controlla ciò che la figura comunica realmente.

Domande obbligatorie:

1. Ogni formula è corretta?
2. Ogni numero deriva davvero dall’operazione dichiarata?
3. Ogni shape è compatibile con l’operazione?
4. Ogni freccia parte dal nodo corretto?
5. Ogni freccia termina sul consumer corretto?
6. Una linea attraversata da un’altra può sembrare una giunzione?
7. Una callout line può essere scambiata per un flusso dati?
8. I rami e le ricomposizioni sono espliciti?
9. Una mask è applicata agli score, ai pesi o alle value? La figura lo rende inequivocabile?
10. Le label coincidono con quelle usate nella prosa?

### 4. Audit visivo e compositivo

Si controllano:

- ordine di lettura;
- equilibrio degli spazi;
- dimensione del testo;
- contrasto;
- allineamento;
- densità;
- sovrapposizioni;
- frecce troppo lunghe o tortuose;
- elementi che sembrano collegati per sola vicinanza;
- uso del colore non accompagnato da label;
- leggibilità alla dimensione prevista nel libro.

### 5. Verdetto

La bozza riceve uno dei seguenti stati:

- `da rigenerare`: struttura o collegamenti non recuperabili con una correzione locale;
- `da modificare`: problema circoscritto e chiaramente correggibile;
- `validata tecnicamente`: contenuto e collegamenti corretti;
- `approvata`: validata tecnicamente e adeguata alla composizione del capitolo.

### 6. Nuova iterazione

Dopo ogni modifica viene ripetuto l’intero audit. Non si controllano soltanto i difetti precedenti, perché la correzione può introdurre nuovi problemi.

## Difetti bloccanti

Una visuale non può essere approvata quando presenta almeno uno di questi difetti:

- collegamento errato o ambiguo;
- formula o valore numerico errato;
- shape incompatibile;
- testo illeggibile o alterato;
- maschera rappresentata sul tensor sbagliato;
- incrocio che sembra una giunzione;
- nodo senza origine o consumer;
- colore usato come unico significato;
- densità tale da impedire un ordine di lettura unico;
- contenuto non coerente con le fonti o con il capitolo;
- watermark, firma o branding di terzi.

## Gestione dei file

Struttura consigliata:

```text
assets/chapters/<capitolo>/<figura>/
  final.png
  AUDIT.md
```

Le bozze respinte possono restare fuori dal repository per evitare peso inutile. `AUDIT.md` registra il numero di iterazioni, i problemi individuati e le correzioni applicate. La versione `final.png` entra nel repository solo dopo l’approvazione.

## Regola di continuità

Prima di procedere alla visuale successiva, la visuale corrente deve essere approvata oppure esplicitamente rimandata con un problema documentato. Non si accumulano figure non revisionate.
