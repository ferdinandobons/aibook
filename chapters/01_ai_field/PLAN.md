# Piano interno. Capitolo 1

## Identità

- `chapter_id`: `CH-P01-AI-FIELD`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Profilo: componente e tassonomia introduttiva
- Stato: candidatura completa in revisione autoriale
- Versione del testo: `0.4.0-rc3`
- Domanda centrale: quali proprietà distinguono AI, machine learning, deep learning, AI generativa, modelli generativi e foundation model senza trattarli come sinonimi?
- Oggetto continuo: la richiesta `Il pacco non è arrivato`, trasformata in output da sistemi costruiti in modi diversi
- Output finale: il lettore sa descrivere un sistema attraverso meccanismo, obiettivo e ampiezza, distingue modello e sistema e sa separare training da inference

## Prerequisiti

- familiarità generale con software e dati;
- Python di base soltanto per eseguire lo snippet.

Il testo principale deve restare comprensibile anche a chi non esegue il codice.

## Concetti differiti

- generalizzazione e split dei dati, Capitolo 4;
- funzioni obiettivo e gradienti, Parti P02 e P03;
- architetture neurali, Parte P04;
- famiglie generative, Parte P05;
- pretraining e scaling, Parte P07;
- sicurezza e governance, Parte P13.

## Convenzioni editoriali

- `modello`: componente matematico parametrizzato;
- `sistema`: modello e componenti circostanti, inclusi input, regole, strumenti, interfacce e controlli sull'output;
- `generalista` e `specialistico`: descrizioni relative, non classi universali rigide;
- simbolico, statistico e neurale: famiglie operative non esaustive e non necessariamente disgiunte.

Ogni termine tecnico viene preceduto da una spiegazione in linguaggio comune e ricondotto alla richiesta continua.

## Sequenza didattica interna

### Transizione 1. Tre domande prima della tassonomia

- Stato iniziale: una frase può essere trasformata in risultati diversi.
- Problema: l'etichetta `AI` non spiega come il risultato sia stato ottenuto.
- Nuovo concetto: meccanismo, obiettivo e ampiezza come tre domande indipendenti.
- Output: il lettore possiede una mappa semplice prima delle definizioni.
- Invariante: la richiesta di assistenza resta l'oggetto continuo.

### Transizione 2. Dal programma al sistema di AI

- Stato corrente: input, operazione e output.
- Nuovo concetto: definizione operativa OECD e distinzione tra modello e sistema.
- Output: il lettore separa la parte matematica dai componenti che ne organizzano l'uso.
- Confine: non è ancora stabilito come il comportamento venga costruito.

### Transizione 3. Regole e apprendimento

- Stato corrente: sistema che trasforma una richiesta in un output.
- Nuovo concetto: comportamento scritto tramite regole oppure appreso da esempi.
- Output: machine learning spiegato come scelta e aggiornamento di parametri.
- Invariante: il compito esterno può restare identico.
- Confine: il tipo di risultato non è ancora classificato.

### Transizione 4. AI, machine learning e deep learning

- Stato corrente: sistemi con meccanismi differenti.
- Nuovo concetto: relazione tra AI, machine learning, representation learning e deep learning.
- Output: il lettore sa che non tutta l'AI è machine learning e non tutto il machine learning è deep learning.
- Confine: deep learning non equivale a generazione.

### Transizione 5. Parametri, training e inference

- Stato corrente: modello appreso da esempi.
- Nuovo concetto: i parametri sono numeri interni aggiornati durante il training e usati durante l'inference.
- Output: separazione tra parametri, iperparametri, checkpoint, training e inference.
- Codice: modello lineare PyTorch su valori illustrativi.
- Visuale: `AI-02`, collocata prima dello snippet.
- Invariante: l'inference non esegue `optimizer.step()` e non modifica i parametri.
- Gate di chiarezza: `logit`, `loss`, `optimizer`, `checkpoint` e `shape` ricevono una spiegazione immediata.

### Transizione 6. Predire o generare

- Stato corrente: modello addestrato.
- Nuovo concetto: distinguere una proprietà tra alternative definite oppure modellare dati e produrre nuovi campioni.
- Output: distinzione intuitiva e poi probabilistica tra discriminativo e generativo.
- Confine: generativo non significa necessariamente foundation model.

### Transizione 7. Foundation model e ampiezza

- Stato corrente: modelli discriminativi e generativi.
- Nuovo concetto: modello di base adattabile a più compiti.
- Output: foundation model distinto dal sistema applicativo e dal solo fatto di generare.
- Invariante: il modello di base può restare identico mentre cambiano adattamento, dati, strumenti e autorizzazioni.
- Confine: generalismo e specializzazione sono relativi al contesto.

### Transizione 8. Ricostruzione

Il lettore ricostruisce tre aspetti:

1. meccanismo, regole o apprendimento;
2. obiettivo, classificare, predire, decidere o generare;
3. ampiezza, compito ristretto oppure base adattabile a più contesti.

`AI-01` rende visibili i tre aspetti come pannelli paralleli e non gerarchici. Il lettore localizza inoltre modello e sistema, training e inference, e trasferisce la descrizione a un nuovo caso.

## Superficie editoriale adottata

La versione `0.4.0-rc3` usa sette sezioni principali e apre con le tre domande che guidano l'intero capitolo.

Regole applicate:

- esempio concreto prima della definizione istituzionale;
- spiegazione in linguaggio comune dopo la definizione OECD;
- nessun uso di `checkpoint` prima della sua definizione;
- machine learning descritto come ciclo di esempi, errore e aggiornamento;
- formula lineare introdotta dopo il significato dei parametri;
- termini del codice tradotti subito in azioni osservabili;
- distinzione discriminativo/generativo spiegata prima delle formule probabilistiche;
- liste di metodi di adattamento ridotte a una descrizione generale;
- visuali integrate nella prosa e non usate come pagine autonome;
- riepilogo in prosa, senza una seconda tassonomia ridondante;
- lettura ad alta voce e verifica con un lettore privo di esperienza specifica;
- nuova lettura integrale dopo l'inserimento delle figure.

## Visuali incluse

### `AI-01`. Tre aspetti per descrivere un sistema di AI

- Domanda: perché AI, machine learning, deep learning, generative AI e foundation model non sono sinonimi?
- Famiglia: taxonomy/comparison.
- Orientamento: orizzontale.
- Contenuto: meccanismo, obiettivo, ampiezza.
- File: `assets/chapters/01_ai_field/AI-01/candidate-v1.png`.
- Stato: validata tecnicamente, approvazione autoriale aperta.

### `AI-02`. Training e inference usano il modello in fasi diverse

- Domanda: quando cambiano i parametri e quando vengono soltanto usati?
- Famiglia: process/comparison.
- Orientamento: orizzontale.
- Contenuto: dati, loss, gradienti, optimizer, checkpoint, nuovo input e output.
- File: `assets/chapters/01_ai_field/AI-02/candidate-v1.png`.
- Stato: validata tecnicamente, approvazione autoriale aperta.

## Codice

### `SNIP-AI-001`

- Domanda: quale differenza osservabile separa training e inference?
- Input: quattro esempi illustrativi con due valori e due classi.
- Operazione: training di `nn.Linear(2, 2)` tramite cross-entropy e SGD.
- Controlli:
  - loss finale inferiore alla loss iniziale;
  - almeno un parametro cambia durante il training;
  - nessun parametro cambia durante l'inference;
  - output di shape `[1,2]`;
  - classe prevista deterministica nell'ambiente registrato.

## Gate specifici

- evitare gerarchie false tra meccanismo, obiettivo e ampiezza;
- dichiarare che simbolico, statistico e neurale sono una tassonomia di lavoro;
- spiegare ogni termine necessario a un lettore non esperto prima di usarlo come scorciatoia;
- mantenere le formule come secondo livello di precisione, non come porta di accesso al concetto;
- introdurre foundation model dopo training/inference e generativo/discriminativo;
- non attribuire comprensione o intenzione ai modelli;
- mantenere modello e sistema distinti;
- non esporre metadati o audit nella lezione;
- non frammentare il capitolo in microsezioni;
- superare review linguistica, lettura ad alta voce e parafrasi in linguaggio comune;
- ripetere il controllo incrociato dopo l'inserimento delle visuali;
- non rinominare le immagini in `final.png` prima dell'approvazione autoriale.
