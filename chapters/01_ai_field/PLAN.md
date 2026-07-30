# Piano interno. Capitolo 1

## Identità

- `chapter_id`: `CH-P01-AI-FIELD`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Profilo: componente e tassonomia introduttiva
- Stato: `research`
- Domanda centrale: quali proprietà distinguono AI, machine learning, deep learning, AI generativa, modelli generativi e foundation model senza trattarli come sinonimi?
- Oggetto continuo: una richiesta di assistenza, `Il pacco non è arrivato`, trasformata in output da sistemi costruiti in modi diversi
- Output finale: il lettore sa classificare un sistema lungo tre assi, meccanismo, obiettivo e ampiezza, e sa distinguere training da inference

## Prerequisiti

- nessun prerequisito tecnico oltre alla familiarità con software, dati e funzioni elementari;
- il codice richiede soltanto Python di base.

## Concetti differiti

- generalizzazione e split dei dati, Capitolo 4;
- funzioni obiettivo e gradienti, Parti P02 e P03;
- architetture neurali, Parte P04;
- famiglie generative, Parte P05;
- pretraining e scaling, Parte P07;
- sicurezza e governance, Parte P13.

## Convenzioni editoriali dichiarate

- `modello`: componente matematico parametrizzato;
- `sistema`: modello e componenti circostanti, inclusi input, pre-processing, regole, tool, interfacce e post-processing;
- `generalista` e `specialistico`: descrizioni relative dell'ampiezza dei compiti, non classi universali rigide;
- simbolico, statistico e neurale: famiglie operative non esaustive e non necessariamente disgiunte.

## Sequenza didattica interna

### Transizione 1. Dal software all'AI system

- Stato iniziale: un programma riceve un input e produce un output.
- Problema: il termine AI viene usato per sistemi molto diversi.
- Nuovo concetto: definire il sistema tramite input, inferenza e output.
- Output: distinzione tra sistema e singolo modello.
- Invariante: lo stesso input di assistenza resta l'oggetto continuo.
- Confine: non è ancora stabilito come il comportamento venga costruito.

### Transizione 2. Meccanismo

- Stato corrente: sistema che mappa una richiesta a un output.
- Nuovo concetto: comportamento esplicito tramite regole oppure appreso da dati.
- Output: tassonomia di lavoro simbolico, statistico e neurale.
- Invariante: il compito esterno può restare identico.
- Confine: il tipo di output non è ancora stato classificato.

### Transizione 3. AI, ML e deep learning

- Stato corrente: sistemi con meccanismi diversi.
- Nuovo concetto: relazione gerarchica tra AI, ML, representation learning e deep learning.
- Output: il lettore sa che non tutta l'AI è ML e non tutto il ML è deep learning.
- Confine: deep learning non equivale a generazione.

### Transizione 4. Parametri, dati, training e inference

- Stato corrente: un modello appreso da dati.
- Nuovo concetto: i parametri vengono aggiornati durante il training e riusati durante l'inference.
- Output: separazione tra dati, obiettivo, parametri, iperparametri e checkpoint.
- Codice: modello lineare PyTorch su feature illustrative.
- Invariante: l'inference non esegue `optimizer.step()` e non modifica i parametri.

### Transizione 5. Obiettivo discriminativo o generativo

- Stato corrente: modello addestrato.
- Nuovo concetto: prevedere una proprietà dell'input oppure modellare una distribuzione capace di produrre campioni o contenuti.
- Output: distinzione tra modello discriminativo e generativo.
- Confine: generativo non significa necessariamente foundation model.

### Transizione 6. Generative AI

- Stato corrente: modello generativo come categoria tecnica.
- Nuovo concetto: sistema orientato alla produzione di contenuto sintetico condizionato da input.
- Output: distinzione tra modello generativo e sistema di AI generativa.
- Confine: non tutta l'AI generativa deriva da foundation model; non ogni foundation model è usato soltanto per generare.

### Transizione 7. Foundation model, generalista e specialistico

- Stato corrente: sistemi generativi e discriminativi.
- Nuovo concetto: pretraining su dati ampi e adattabilità a molti compiti.
- Output: foundation model distinto dal sistema downstream.
- Invariante: il modello di base può restare identico mentre cambiano adattamento, dati, tool e interfaccia.
- Confine: ampiezza e specializzazione sono relative al contesto d'uso.

### Transizione 8. Ricostruzione

- Ricostruire tre assi:
  1. meccanismo, regole o apprendimento;
  2. obiettivo, discriminativo o generativo;
  3. ampiezza, specialistico o adattabile a molti compiti.
- Localizzare training e inference.
- Trasferire la tassonomia a un nuovo sistema.

## Visuali previste

### `AI-01`. Tre assi per descrivere un sistema di AI

- Domanda: perché AI, ML, deep learning, generative AI e foundation model non sono sinonimi?
- Famiglia: taxonomy/comparison.
- Orientamento: orizzontale.
- Contenuto: meccanismo, obiettivo, ampiezza.

### `AI-02`. Training e inference usano lo stesso modello in fasi diverse

- Domanda: quando cambiano i parametri e quando vengono soltanto usati?
- Famiglia: process/comparison.
- Orientamento: orizzontale.
- Contenuto: dati, loss, gradienti, optimizer, checkpoint, nuovo input e output.

## Codice previsto

### `SNIP-AI-001`

- Domanda: quale differenza osservabile separa training e inference?
- Input: quattro esempi numerici illustrativi con due feature e due classi.
- Operazione: training di `nn.Linear(2, 2)` tramite cross-entropy e SGD.
- Controlli:
  - la loss finale è inferiore alla loss iniziale;
  - almeno un parametro cambia durante il training;
  - nessun parametro cambia durante l'inference;
  - output di inference con shape `[1, 2]`;
  - classe prevista deterministica nell'ambiente registrato.

## Gate didattico specifico

- evitare un diagramma di insiemi che faccia sembrare generative AI un sottoinsieme esatto di deep learning;
- dichiarare esplicitamente che la tassonomia simbolico/statistico/neurale è una convenzione di lavoro;
- introdurre foundation model dopo la distinzione training/inference e generativo/discriminativo;
- non attribuire comprensione, intenzione o autonomia ai modelli;
- mantenere modello e sistema distinti in tutto il capitolo.
