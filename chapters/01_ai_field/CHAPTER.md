# Capitolo 1. Che cos'è l'intelligenza artificiale

## Metadati

- `chapter_id`: `CH-P01-AI-FIELD`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Maturità: `CORE`
- Stato: **bozza tecnica, visuali aperte**
- Versione candidata: `0.1.0-draft1`
- Data di apertura: 30 luglio 2026
- Data dell'ultima ricerca web: 30 luglio 2026
- Data dell'ultima verifica delle fonti: 30 luglio 2026
- Data di congelamento editoriale: non assegnata
- Documentazione PyTorch verificata: stable `2.13`
- Ambiente eseguito: Python `3.13.5`, PyTorch `2.10.0+cpu`
- Oggetto continuo: una richiesta di assistenza, `Il pacco non è arrivato`, elaborata da sistemi costruiti in modi diversi
- Concetti differiti: generalizzazione, funzioni obiettivo, gradienti, architetture neurali, famiglie generative, pretraining, scaling, sicurezza e governance

> **Stato della candidatura.** Il testo, le fonti, il registro delle affermazioni e il primo snippet sono disponibili. Le visuali `AI-01` e `AI-02` sono ancora in lavorazione e non sono incluse finché lo strumento immagini non produce candidate coerenti con le specifiche. Il capitolo non può passare alla revisione autoriale prima del loro audit.

## In questo capitolo

La frase `Il pacco non è arrivato` può entrare in sistemi molto diversi. Un programma può cercare parole predefinite e aprire una procedura di rimborso. Un classificatore può assegnare la richiesta alla categoria `problema di consegna`. Un modello generativo può comporre una risposta. Un sistema più ampio può combinare un modello, una ricerca nel database degli ordini e regole che stabiliscono quali azioni siano autorizzate.

Tutti questi sistemi possono essere descritti come sistemi di intelligenza artificiale in un determinato contesto, ma le etichette `AI`, `machine learning`, `deep learning`, `modello generativo`, `generative AI` e `foundation model` non indicano la stessa cosa. Alcune descrivono **come** viene costruito il comportamento. Altre descrivono **quale obiettivo** viene ottimizzato. Altre ancora riguardano **quanto è ampio** il riuso previsto del modello.

L'obiettivo del capitolo è costruire un lessico operativo. Alla fine saremo in grado di osservare un sistema, separare il modello dai componenti circostanti e descriverlo lungo tre assi: meccanismo, obiettivo e ampiezza. Useremo inoltre un piccolo esempio PyTorch per rendere concreta la differenza tra training e inference.

# 1. Dal programma al sistema di AI

Un programma riceve input, esegue operazioni e produce output. Questa descrizione è tanto generale da includere una calcolatrice, un database, un compilatore e un modello neurale. Per delimitare il campo serve una proprietà ulteriore.

La definizione OECD aggiornata descrive un **AI system** come un sistema machine-based che, per obiettivi espliciti o impliciti, inferisce dagli input come produrre output quali predizioni, contenuti, raccomandazioni o decisioni. Gli output possono influire su ambienti fisici o virtuali [OECD, 2024].

In questa definizione, `inferire` non significa necessariamente usare una rete neurale. Significa che il sistema determina, a partire dagli input e dal proprio meccanismo interno, quale output produrre. L'obiettivo può essere scritto direttamente in una funzione, incorporato in regole oppure riflesso nei dati usati durante l'addestramento. L'OECD tratta esplicitamente queste possibilità come casi che possono sovrapporsi [OECD, 2024].

Torniamo alla richiesta:

```text
Il pacco non è arrivato
```

Un sistema di assistenza potrebbe produrre:

```text
categoria = problema_di_consegna
```

oppure:

```text
risposta = "Controllo subito lo stato della spedizione."
```

oppure ancora:

```text
azione = apri_ticket_e_richiedi_numero_ordine
```

La natura dell'output non basta a identificare il meccanismo. La stessa categoria può essere ottenuta con una regola scritta a mano, con una regressione logistica o con una rete neurale. Per questo motivo è utile separare il **sistema** dal **modello**.

Nel lessico di questo libro:

- un **modello** è un componente matematico parametrizzato che trasforma input in output;
- un **sistema** comprende il modello e tutto ciò che lo circonda: acquisizione e validazione degli input, regole, retrieval, tool, interfacce, autorizzazioni e post-processing.

La distinzione è editoriale ma operativamente importante. NIST organizza il risk management lungo l'intero ciclo di vita di prodotti, servizi e sistemi AI, non soltanto attorno al file che contiene i parametri [NIST AI RMF 1.0, 2023]. Un modello può quindi restare invariato mentre il comportamento del sistema cambia perché vengono modificati il database consultato, la policy di autorizzazione o il modo in cui l'output viene mostrato all'utente.

# 2. Regole esplicite e comportamento appreso

Consideriamo una prima implementazione della classificazione della richiesta:

```text
se il testo contiene "pacco" e "non è arrivato":
    categoria = problema_di_consegna
```

La relazione tra input e output è stata scritta direttamente. Il comportamento dipende dalle regole e dalle rappresentazioni scelte dal progettista. Un sistema di questo tipo può essere descritto come **rule-based** o, quando usa rappresentazioni esplicite di fatti, simboli e relazioni, come parte della tradizione dell'AI simbolica.

Ora immaginiamo di raccogliere molte richieste già etichettate:

```text
"Il corriere non è passato"       -> problema_di_consegna
"Voglio cambiare indirizzo"       -> modifica_ordine
"Il pacco non è arrivato"         -> problema_di_consegna
"La carta è stata rifiutata"      -> problema_di_pagamento
```

Un algoritmo può cercare valori dei propri parametri che riducano gli errori su questi esempi. In questo caso non viene specificata una regola separata per ogni formulazione. Viene definita una famiglia di funzioni, un obiettivo e una procedura che modifica i parametri usando i dati. Questo è il nucleo del **machine learning**.

Il contrasto non è assoluto. Un'applicazione reale può usare contemporaneamente:

- regole esplicite per validare un numero d'ordine;
- un classificatore appreso per assegnare una categoria;
- una rete neurale per produrre una rappresentazione del testo;
- una regola finale che impedisce azioni non autorizzate.

Per questo capitolo useremo `simbolico`, `statistico` e `neurale` come una tassonomia di lavoro, non come tre insiemi esaustivi e sempre disgiunti. `Statistico` indica qui modelli la cui relazione con i dati viene espressa tramite quantità probabilistiche o criteri di stima. `Neurale` indica modelli composti da trasformazioni parametrizzate organizzate in reti. Un modello neurale viene normalmente addestrato con metodi statistici, mentre un sistema simbolico può contenere componenti appresi.

La prima dimensione da annotare è quindi il **meccanismo predominante** con cui il comportamento viene ottenuto:

```text
regole esplicite
modello appreso dai dati
rete neurale profonda
sistema ibrido
```

Queste etichette non dicono ancora se il sistema classifica o genera, né quanto sia ampio il suo campo d'uso.

# 3. AI, machine learning e deep learning

L'intelligenza artificiale è il campo più ampio. Include metodi per rappresentare conoscenza, cercare soluzioni, pianificare, prendere decisioni, apprendere da dati e costruire sistemi capaci di produrre output utili in compiti che richiedono elaborazione non banale.

Il **machine learning** è uno degli approcci all'AI. Invece di descrivere interamente il comportamento tramite regole operative, si usa esperienza sotto forma di dati, interazioni o segnali di valutazione per scegliere i parametri di un modello. Il manuale di Goodfellow, Bengio e Courville colloca esplicitamente il machine learning all'interno dell'AI e ricorda che esistono approcci AI non basati sull'apprendimento automatico, per esempio sistemi costruiti attorno a knowledge base [Goodfellow et al., 2016, cap. 1].

Il **representation learning** è una parte del machine learning in cui anche la rappresentazione usata per il compito viene appresa. Un classificatore di richieste può ricevere feature progettate manualmente, come la presenza di parole specifiche. Un sistema di representation learning può invece imparare vettori intermedi che risultano utili per separare le categorie.

Il **deep learning** usa composizioni di più trasformazioni apprese. Ogni livello riceve una rappresentazione e ne produce un'altra. La profondità permette di costruire funzioni complesse come composizioni di funzioni più semplici. Non esiste tuttavia una soglia universalmente accettata oltre la quale un modello diventa `deep`; il termine descrive una famiglia di metodi, non un numero normativo di layer [Goodfellow et al., 2016, cap. 1].

La relazione concettuale può essere riassunta così:

```text
AI
└── machine learning
    └── representation learning
        └── deep learning
```

La rappresentazione è utile soltanto per questa relazione. Non implica che ogni sistema AI moderno appartenga esclusivamente a un singolo ramo. Un sistema può contenere una rete profonda e regole simboliche, oppure usare un modello appreso all'interno di una procedura di ricerca.

È importante anche ciò che questa gerarchia **non** dice:

- `deep learning` non significa automaticamente `generativo`;
- un modello generativo non deve necessariamente essere una rete profonda;
- un sistema AI può non contenere alcun componente di machine learning;
- una rete neurale non coincide con il prodotto o servizio che la incorpora.

# 4. Dati, parametri e iperparametri

Un modello parametrizzato contiene valori che determinano la trasformazione eseguita. In un modello lineare con due feature di input e due classi, i parametri principali sono una matrice di pesi e un vettore di bias:

$$
\mathbf{z}=W\mathbf{x}+\mathbf{b}.
$$

L'input `x` potrebbe contenere due feature numeriche ricavate dalla richiesta. L'output `z` contiene due logit, uno per classe. La softmax può trasformare i logit in valori normalizzati, ma la scelta dei pesi `W` e del bias `b` determina la separazione appresa.

I **dati di training** forniscono esempi usati per modificare i parametri. Una **funzione obiettivo** misura, secondo una regola dichiarata, quanto l'output corrente differisce dal risultato desiderato. Un **optimizer** applica aggiornamenti ai parametri usando i gradienti o altre quantità calcolate dalla procedura di apprendimento.

Gli **iperparametri** controllano invece la configurazione della procedura o del modello. Nel piccolo esempio che useremo tra poco, il learning rate `0.1` e il numero di iterazioni `100` sono scelti prima dell'esecuzione; non vengono appresi direttamente da `optimizer.step()`.

Questa distinzione è locale alla procedura considerata. Un valore può essere iperparametro in un esperimento e diventare output di un'altra procedura di ottimizzazione. Ciò che conta è dichiarare quale operazione lo modifica.

Quando i parametri vengono salvati, insieme alle informazioni necessarie a riutilizzarli, si ottiene un **checkpoint**. In un progetto reale il checkpoint può includere anche stato dell'optimizer, contatori, configurazione e metadati. Il termine non identifica quindi soltanto una matrice di pesi.

# 5. Training e inference sono due fasi diverse

Durante il **training**, il sistema usa esempi e un segnale obiettivo per modificare i parametri. Nel caso supervisionato più semplice, una iterazione contiene questa sequenza:

```text
input e target
-> output del modello
-> loss
-> gradienti
-> aggiornamento dei parametri
```

La documentazione PyTorch presenta lo stesso ciclo tramite `optimizer.zero_grad()`, forward pass, calcolo della loss, `loss.backward()` e `optimizer.step()` [PyTorch Tutorials 2.13, Optimizing Model Parameters]. `optimizer.step()` è l'operazione che applica l'aggiornamento ai parametri registrati nell'optimizer [PyTorch 2.13, torch.optim].

Durante l'**inference**, un input nuovo viene trasformato usando i parametri disponibili. Nel caso base non viene eseguito un passo dell'optimizer e il checkpoint rimane invariato:

```text
nuovo input
-> modello con parametri fissati
-> output
```

Esistono tecniche che modificano stato o parametri al test time, ma appartengono a capitoli successivi. Per costruire il concetto fondamentale, `inference` indica qui l'uso del modello addestrato senza un update dei suoi parametri.

Anche in PyTorch occorre distinguere due operazioni. `model.eval()` imposta la modalità di evaluation per i moduli che cambiano comportamento tra training ed evaluation, come Dropout e BatchNorm. `torch.inference_mode()` disabilita il tracciamento autograd e altre strutture necessarie al calcolo dei gradienti. Chiamare soltanto `eval()` non equivale a disabilitare autograd, e usare soltanto `inference_mode()` non sostituisce la modalità di evaluation dei moduli interessati [PyTorch 2.13, `Module` e `inference_mode`].

Il seguente snippet usa quattro esempi illustrativi con due feature e due classi. Il layer lineare viene addestrato con cross-entropy e SGD. Prima e dopo l'inference vengono copiate le matrici dei parametri, così possiamo controllare direttamente quali fasi le modificano.

```python
import torch
from torch import nn


torch.manual_seed(7)
features = torch.tensor(
    [[2.0, 0.0], [1.5, 0.2], [0.0, 2.0], [0.2, 1.5]],
    dtype=torch.float32,
)
labels = torch.tensor([0, 0, 1, 1])

model = nn.Linear(2, 2)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

model.train()
for _ in range(100):
    optimizer.zero_grad()
    loss = loss_fn(model(features), labels)
    loss.backward()
    optimizer.step()

model.eval()
with torch.inference_mode():
    logits = model(torch.tensor([[1.8, 0.1]]))
    predicted_class = logits.argmax(dim=-1)
```

Il file eseguito è [`code/snip_ai_001_training_inference.py`](code/snip_ai_001_training_inference.py). La versione completa conserva copie dei parametri e restituisce tutti i controlli.

Nell'ambiente registrato, la loss passa da `0.641941` a `0.045580`. Almeno un parametro cambia durante il training. Nessun parametro cambia durante l'inference. Il nuovo input produce un tensor di logit con shape `[1,2]` e la classe prevista è `0`.

Questi valori non dimostrano che il modello generalizzi: il dataset è costruito soltanto per rendere visibile la differenza tra le due fasi. La generalizzazione richiede dati separati e un protocollo di valutazione, che verranno introdotti nei capitoli successivi.

# 6. Predire una proprietà o modellare una distribuzione

Dopo aver distinto il meccanismo di apprendimento, possiamo descrivere un secondo asse: **l'obiettivo modellato**.

Un modello discriminativo può imparare direttamente una relazione utile a distinguere classi o prevedere un target. Per la richiesta di assistenza, può stimare:

$$
p(y\mid x),
$$

dove `x` rappresenta la richiesta e `y` la categoria. La regressione logistica è un esempio classico.

Un modello generativo descrive invece una distribuzione dei dati o un processo capace di produrre campioni. In un problema con input e classi può modellare la distribuzione congiunta:

$$
p(x,y),
$$

oppure la distribuzione degli input:

$$
p(x).
$$

Da una distribuzione modellata è possibile campionare, completare o ricostruire dati, a seconda della famiglia del modello.

Ng e Jordan confrontano logistic regression e naive Bayes proprio come esempi di approccio discriminativo e generativo. Il loro risultato non autorizza a dichiarare che un paradigma sia sempre migliore: il confronto dipende dalla famiglia, dalla quantità di dati e dalle ipotesi considerate [Ng e Jordan, 2001].

La distinzione riguarda l'obiettivo probabilistico o il ruolo nel sistema, non una forma grafica obbligatoria. Nel framework GAN, per esempio, un generatore `G` è addestrato per catturare la distribuzione dei dati e produrre campioni, mentre un discriminatore `D` cerca di distinguere dati reali e campioni prodotti [Goodfellow et al., 2014]. I due componenti convivono nello stesso processo di training.

Un modello discriminativo può essere una rete profonda. Un modello generativo può essere neurale oppure basato su un'altra famiglia probabilistica. L'asse `discriminativo/generativo` non sostituisce quindi l'asse `regole/apprendimento/rete profonda`.

# 7. Che cosa indica generative AI

Il termine **generative AI** viene usato per sistemi orientati alla produzione di contenuto sintetico condizionato da input, istruzioni o contesto. Il profilo NIST per la generative AI descrive modelli che emulano struttura e caratteristiche dei dati di input per produrre contenuto sintetico derivato. Il documento include testo, immagini, video, audio e altri contenuti digitali [NIST AI 600-1, 2024].

Nel nostro esempio, un classificatore produce una categoria tra opzioni già definite:

```text
problema_di_consegna
```

Un sistema generativo può produrre una nuova sequenza testuale:

```text
Mi dispiace per il ritardo. Inserisci il numero dell'ordine e controllerò lo stato della spedizione.
```

La parola `nuova` va interpretata con precisione. Il contenuto viene prodotto combinando regolarità apprese e condizioni fornite al sistema. Non implica che il sistema possieda intenzione, esperienza soggettiva o comprensione umana.

È utile distinguere ancora una volta modello e sistema. Un modello linguistico produce una distribuzione sui token successivi. Un sistema di generative AI può aggiungere:

- un template che struttura il messaggio;
- un retrieval sul database degli ordini;
- tool per leggere lo stato della spedizione;
- regole che impediscono rimborsi non autorizzati;
- controlli sull'output;
- un'interfaccia conversazionale.

Il comportamento osservato dall'utente appartiene al sistema completo. Non può essere attribuito automaticamente al solo checkpoint.

Il profilo NIST chiarisce anche un confine importante: **non tutta la generative AI deriva da foundation model** [NIST AI 600-1, 2024]. Un piccolo modello generativo addestrato per un dominio ristretto può produrre contenuto senza essere un foundation model.

# 8. Foundation model e adattamento

Il report dello Stanford Center for Research on Foundation Models introduce il termine **foundation model** per un modello addestrato su dati ampi, generalmente con self-supervision su larga scala, che può essere adattato a numerosi compiti downstream [Bommasani et al., 2021].

La proprietà centrale non è soltanto la generazione. È il ruolo di base riutilizzabile. Un modello può essere preaddestrato e poi adattato tramite:

- fine-tuning;
- instruction tuning;
- adapter o LoRA;
- prompting e in-context examples;
- collegamento a retrieval e tool;
- specializzazione tramite dati di dominio.

Queste tecniche verranno trattate più avanti. In questo capitolo interessa la separazione tra tre oggetti:

```text
modello di base
-> adattamento o configurazione
-> sistema applicativo
```

Il modello di base può rimanere lo stesso mentre cambiano il dataset di adattamento, il prompt di sistema, gli strumenti disponibili e le regole operative. Di conseguenza, non è corretto dedurre tutte le proprietà del sistema dalla sola famiglia del foundation model.

`Foundation model` e `generative model` non sono sinonimi. Molti foundation model contemporanei possiedono capacità generative, ma la definizione riguarda ampiezza del pretraining e adattabilità. Analogamente, un modello generativo specialistico può non avere il ruolo di fondazione per un insieme ampio di compiti.

# 9. Generalista e specialistico sono termini relativi

Un sistema **specialistico** è progettato e valutato per un insieme ristretto di compiti o condizioni. Un classificatore delle richieste di consegna è specialistico rispetto a un sistema capace di classificare richieste, generare risposte, tradurre testi, analizzare immagini e chiamare strumenti.

Un sistema viene spesso chiamato **generalista** quando copre molti compiti o modalità. Il termine non possiede però una soglia numerica universale. Un modello può essere generalista rispetto a un'applicazione aziendale e specialistico rispetto all'insieme delle capacità umane.

Per questo libro, `generalista` e `specialistico` descrivono l'ampiezza relativa del riuso e delle valutazioni. Non implicano qualità, affidabilità o autonomia. Un sistema generalista può fallire su un dominio specifico; un sistema specialistico può essere migliore nel proprio perimetro.

La stessa cautela vale per il termine `foundation model`. Il pretraining ampio rende possibile l'adattamento, ma non garantisce che ogni sistema costruito sul modello sia ugualmente competente in ogni compito.

# 10. Tre assi invece di una lista di sinonimi

Possiamo ora descrivere un sistema lungo tre dimensioni indipendenti.

| Asse | Domanda | Esempi di valori |
|---|---|---|
| Meccanismo | Come viene costruita la relazione tra input e output? | regole, modello appreso, rete profonda, sistema ibrido |
| Obiettivo | Quale relazione o distribuzione viene modellata? | discriminativo, generativo, decisionale |
| Ampiezza | Quanto è ampio il riuso previsto e verificato? | specialistico, modello di base adattabile, generalista |

Per la richiesta `Il pacco non è arrivato` possiamo costruire, per esempio:

1. un sistema specialistico rule-based che apre un ticket;
2. un classificatore specialistico di deep learning;
3. un modello generativo specialistico che compone risposte in un solo dominio;
4. un foundation model generativo adattato all'assistenza clienti;
5. un sistema ibrido che combina foundation model, retrieval, tool e regole.

Nessun asse determina automaticamente gli altri. `Rete profonda` non implica `generativo`. `Generativo` non implica `foundation model`. `Foundation model` non implica che il sistema applicativo sia privo di specializzazione.

> **Visuale prevista `AI-01`.** La figura mostrerà i tre assi attorno alla stessa richiesta di assistenza. Non è ancora inclusa perché le candidate prodotte dallo strumento immagini non hanno rappresentato il contenuto richiesto e sono state respinte durante l'audit.

# 11. Una mappa minima del ciclo di vita

Le etichette appena costruite descrivono il modello e il sistema, ma non sostituiscono il ciclo di vita. Un progetto reale attraversa almeno:

```text
definizione del compito
-> raccolta e preparazione dei dati
-> scelta del modello e dell'obiettivo
-> training o configurazione
-> valutazione
-> deployment
-> uso e monitoraggio
-> aggiornamento o ritiro
```

NIST usa il concetto di AI lifecycle proprio per ricordare che rischi, responsabilità e prestazioni dipendono dalle fasi e dagli attori coinvolti [NIST AI RMF 1.0, 2023]. Una misura ottenuta durante lo sviluppo non descrive automaticamente il comportamento dopo il deployment. Un checkpoint non documenta da solo i dati, il contesto d'uso o le procedure di controllo.

Nel caso della richiesta di consegna, il modello può essere tecnicamente identico in due applicazioni, ma i sistemi differiscono se uno può soltanto suggerire una categoria mentre l'altro può modificare un ordine reale. Le autorizzazioni e le conseguenze operative appartengono al sistema.

> **Visuale prevista `AI-02`.** La figura separerà training e inference: a sinistra dati, loss, gradienti, optimizer e checkpoint aggiornato; a destra nuovo input, checkpoint fissato e output. Anche questa visuale resta aperta finché una candidata non supera l'audit.

# 12. Errori di classificazione frequenti

## `AI` e `machine learning` usati come sinonimi

Il machine learning è un approccio all'AI, non la definizione completa del campo. Un sistema basato su ricerca, pianificazione o regole può rientrare nell'AI senza apprendere i parametri dai dati.

## `Machine learning` e `deep learning` usati come sinonimi

Il deep learning è una parte del machine learning. Regressione lineare, alberi decisionali e molti modelli probabilistici sono machine learning ma non vengono normalmente descritti come deep learning.

## `Deep` interpretato come misura assoluta

La profondità riguarda la composizione di trasformazioni; non esiste un numero universalmente valido di layer che separi ogni modello shallow da ogni modello deep.

## `Generativo` interpretato come sinonimo di foundation model

Un modello generativo può essere piccolo e specialistico. Il profilo NIST dichiara esplicitamente che non tutta la generative AI deriva da foundation model.

## `Foundation model` interpretato come prodotto completo

Un foundation model è una base adattabile. Retrieval, tool, dati di dominio, autorizzazioni e interfaccia appartengono al sistema costruito attorno al modello.

## `Inference` interpretata come aggiornamento automatico

Nel caso base, l'inference usa i parametri disponibili senza un passo dell'optimizer. Tecniche di test-time adaptation esistono, ma devono essere nominate esplicitamente perché cambiano il contratto.

## `eval()` interpretato come disabilitazione dei gradienti

In PyTorch, `eval()` modifica la modalità dei moduli interessati. `inference_mode()` o `no_grad()` gestiscono il tracciamento autograd. Le due operazioni non sono equivalenti.

# 13. Ricostruzione completa

Partiamo dalla richiesta:

```text
Il pacco non è arrivato
```

Per descrivere il sistema che la elabora procediamo in questo ordine.

1. Identifichiamo input e output osservabili.
2. Separiamo il modello dal sistema completo.
3. Chiediamo se il comportamento deriva da regole, apprendimento dai dati, reti neurali o una combinazione.
4. Se esiste training, distinguiamo dati, parametri, iperparametri, obiettivo e optimizer.
5. Separiamo la fase che modifica i parametri dalla fase che li usa per produrre output.
6. Classifichiamo l'obiettivo come discriminativo, generativo o appartenente a un'altra formulazione decisionale dichiarata.
7. Verifichiamo se il modello svolge un ruolo specialistico oppure funge da base adattabile per compiti diversi.
8. Ricostruiamo infine il sistema applicativo, includendo retrieval, tool, regole, interfacce e autorizzazioni.

La tassonomia ottenuta non assegna un'etichetta unica. Produce una descrizione composta. Un sistema può essere contemporaneamente:

```text
ibrido nel meccanismo
+ generativo nell'output
+ costruito su un foundation model
+ specializzato nell'assistenza clienti
```

Questa descrizione è più informativa della sola parola `AI`.

# 14. Controlli di comprensione

## Ricostruzione

Spiegare la relazione tra AI, machine learning, representation learning e deep learning senza usare i termini come sinonimi.

## Localizzazione

Indicare quale operazione modifica i parametri nello snippet PyTorch e quale blocco esegue soltanto l'inference.

## Confine

Spiegare perché un modello generativo non è necessariamente un foundation model e perché un foundation model non coincide con il sistema applicativo.

## Trasferimento

Classificare un filtro antispam che usa una rete neurale addestrata su email etichettate. Descriverlo lungo gli assi meccanismo, obiettivo e ampiezza.

## Variazione

Supporre di aggiungere al sistema di assistenza un tool che legge lo stato reale della spedizione. Dire quale parte del modello può restare invariata e quale parte del sistema è cambiata.

# 15. Esercizi

1. Descrivere un sistema di raccomandazione usando separatamente input, modello, output e componenti di sistema.
2. Scrivere una regola esplicita per classificare una richiesta di consegna, poi indicare due formulazioni che la regola non riconoscerebbe.
3. Modificare `SNIP-AI-001` rimuovendo il ciclo di training. Verificare che i parametri rimangano invariati e confrontare la loss.
4. Aggiungere una seconda chiamata di inference con un input differente e verificare la shape dell'output.
5. Trovare un esempio di modello generativo specialistico che non richieda la nozione di foundation model.
6. Spiegare perché un sistema costruito su un modello generalista può essere comunque specialistico nel deployment.
7. Elencare tre componenti di un sistema di generative AI che non fanno parte del checkpoint.
8. Confrontare `model.eval()` e `torch.inference_mode()` usando la documentazione PyTorch citata nel dossier delle fonti.

# 16. Fonti e artefatti

Le schede complete, le sezioni consultate e i limiti sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md).

Fonti portanti:

- OECD, *Explanatory memorandum on the updated OECD definition of an AI system*, 2024.
- NIST, *Artificial Intelligence Risk Management Framework 1.0*, 2023.
- Goodfellow, Bengio e Courville, *Deep Learning*, 2016.
- Ng e Jordan, *On Discriminative vs. Generative Classifiers*, 2001.
- Goodfellow et al., *Generative Adversarial Nets*, 2014.
- NIST, *Generative Artificial Intelligence Profile*, 2024.
- Bommasani et al., *On the Opportunities and Risks of Foundation Models*, 2021.
- PyTorch stable 2.13, documentazione su optimization, `torch.optim`, `Module` e `inference_mode`.

Artefatti di riproduzione:

- registro delle affermazioni: [`CLAIMS.md`](CLAIMS.md);
- piano interno: [`PLAN.md`](PLAN.md);
- codice: [`code/snip_ai_001_training_inference.py`](code/snip_ai_001_training_inference.py);
- test: [`code/test_ai_snippets.py`](code/test_ai_snippets.py);
- output: [`code/outputs/`](code/outputs/);
- ambiente: [`code/environments/python-pytorch.txt`](code/environments/python-pytorch.txt).

## Registro di approvazione

- Review fattuale: aperta sulla bozza `0.1.0-draft1`
- Review matematica: aperta
- Review architetturale e terminologica: aperta
- Review temporale: fonti ricontrollate il 30 luglio 2026
- Review codice: esecuzione locale completata, artefatti da pubblicare
- Review visuale: **bloccata**, candidate errate respinte
- Review incrociata: aperta
- Review didattica: aperta
- Review autoriale: non aperta
- Data di congelamento: non assegnata
- Commit congelato: non assegnato
