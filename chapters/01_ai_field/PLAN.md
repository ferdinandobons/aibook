# Piano interno. Capitolo 1

## Identità

- `chapter_id`: `CH-P01-AI-FIELD`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Profilo: componente e tassonomia introduttiva
- Stato: review editoriale superata, visuali aperte
- Versione del testo: `0.2.0-rc1`
- Domanda centrale: quali proprietà distinguono AI, machine learning, deep learning, AI generativa, modelli generativi e foundation model senza trattarli come sinonimi?
- Oggetto continuo: la richiesta `Il pacco non è arrivato`, trasformata in output da sistemi costruiti in modi diversi
- Output finale: il lettore sa descrivere un sistema attraverso meccanismo, obiettivo e perimetro d'uso, e sa distinguere training da inference

## Prerequisiti

- familiarità generale con software, dati e funzioni elementari;
- Python di base per lo snippet.

## Concetti differiti

- generalizzazione e split dei dati, Capitolo 4;
- funzioni obiettivo e gradienti, Parti P02 e P03;
- architetture neurali, Parte P04;
- famiglie generative, Parte P05;
- pretraining e scaling, Parte P07;
- sicurezza e governance, Parte P13.

## Convenzioni editoriali

- `modello`: componente matematico parametrizzato;
- `sistema`: modello e componenti circostanti, inclusi input, regole, tool, interfacce e post-processing;
- `generalista` e `specialistico`: descrizioni relative, non classi universali rigide;
- simbolico, statistico e neurale: famiglie operative non esaustive e non necessariamente disgiunte.

## Sequenza didattica interna

### Transizione 1. Dal software al sistema di AI

- Stato iniziale: un programma riceve un input e produce un output.
- Problema: il termine AI viene usato per sistemi molto diversi.
- Nuovo concetto: definizione operativa attraverso input, inferenza e output.
- Output: distinzione tra modello e sistema.
- Invariante: la richiesta di assistenza resta l'oggetto continuo.
- Confine: non è ancora stabilito come il comportamento venga costruito.

### Transizione 2. Regole e apprendimento

- Stato corrente: sistema che trasforma una richiesta in un output.
- Nuovo concetto: comportamento scritto tramite regole oppure appreso da dati.
- Output: tassonomia di lavoro simbolico, statistico e neurale.
- Invariante: il compito esterno può restare identico.
- Confine: il tipo di output non è ancora classificato.

### Transizione 3. AI, machine learning e deep learning

- Stato corrente: sistemi con meccanismi differenti.
- Nuovo concetto: relazione tra AI, machine learning, representation learning e deep learning.
- Output: il lettore sa che non tutta l'AI è machine learning e non tutto il machine learning è deep learning.
- Confine: deep learning non equivale a generazione.

### Transizione 4. Parametri, training e inference

- Stato corrente: modello appreso da dati.
- Nuovo concetto: i parametri vengono aggiornati durante il training e riusati durante l'inference.
- Output: separazione tra dati, obiettivo, parametri, iperparametri e checkpoint.
- Codice: modello lineare PyTorch su feature illustrative.
- Invariante: l'inference non esegue `optimizer.step()` e non modifica i parametri.

### Transizione 5. Obiettivo discriminativo o generativo

- Stato corrente: modello addestrato.
- Nuovo concetto: predire una proprietà oppure modellare una distribuzione capace di produrre campioni o contenuti.
- Output: distinzione tra discriminativo e generativo.
- Confine: generativo non significa necessariamente foundation model.

### Transizione 6. Generative AI

- Stato corrente: modello generativo come categoria tecnica.
- Nuovo concetto: sistema orientato alla produzione di contenuto sintetico condizionato da input.
- Output: distinzione tra modello generativo e sistema di AI generativa.
- Confine: non tutta l'AI generativa deriva da foundation model.

### Transizione 7. Foundation model e perimetro d'uso

- Stato corrente: sistemi generativi e discriminativi.
- Nuovo concetto: pretraining ampio e adattabilità a più compiti.
- Output: foundation model distinto dal sistema applicativo.
- Invariante: il modello di base può restare identico mentre cambiano adattamento, dati, tool e interfaccia.
- Confine: generalismo e specializzazione sono relativi al contesto.

### Transizione 8. Ricostruzione

Il lettore ricostruisce tre dimensioni:

1. meccanismo, regole o apprendimento;
2. obiettivo, discriminativo o generativo;
3. perimetro, specialistico o adattabile a molti compiti.

Localizza inoltre training e inference e trasferisce la descrizione a un nuovo sistema.

## Superficie editoriale adottata

La versione `0.2.0-rc1` usa otto sezioni principali e non espone lo scaffold.

Regole applicate:

- metadati in commento non renderizzato;
- richiesta continua lungo il capitolo;
- definizioni ricondotte subito all'esempio;
- dettagli API confinati in una nota;
- cautele duplicate rimosse;
- riepilogo costruito sul problema iniziale;
- review linguistica e lettura ad alta voce.

## Visuali previste

### `AI-01`. Tre aspetti per descrivere un sistema di AI

- Domanda: perché AI, machine learning, deep learning, generative AI e foundation model non sono sinonimi?
- Famiglia: taxonomy/comparison.
- Orientamento: orizzontale.
- Contenuto: meccanismo, obiettivo, perimetro d'uso.
- Stato: da rigenerare.

### `AI-02`. Training e inference usano il modello in fasi diverse

- Domanda: quando cambiano i parametri e quando vengono soltanto usati?
- Famiglia: process/comparison.
- Orientamento: orizzontale.
- Contenuto: dati, loss, gradienti, optimizer, checkpoint, nuovo input e output.
- Stato: da generare.

## Codice

### `SNIP-AI-001`

- Domanda: quale differenza osservabile separa training e inference?
- Input: quattro esempi illustrativi con due feature e due classi.
- Operazione: training di `nn.Linear(2, 2)` tramite cross-entropy e SGD.
- Controlli:
  - loss finale inferiore alla loss iniziale;
  - almeno un parametro cambia durante il training;
  - nessun parametro cambia durante l'inference;
  - output di shape `[1,2]`;
  - classe prevista deterministica nell'ambiente registrato.

## Gate specifici

- evitare gerarchie false tra meccanismo, obiettivo e perimetro;
- dichiarare che simbolico, statistico e neurale sono una tassonomia di lavoro;
- introdurre foundation model dopo training/inference e generativo/discriminativo;
- non attribuire comprensione o intenzione ai modelli;
- mantenere modello e sistema distinti;
- non esporre metadati o audit nella lezione;
- non frammentare il capitolo in microsezioni;
- superare review linguistica e lettura ad alta voce;
- ripetere il controllo incrociato dopo l'inserimento delle visuali.
