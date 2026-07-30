# Capitolo 1. Che cos'è l'intelligenza artificiale

## Metadati

- `chapter_id`: `CH-P01-AI-FIELD`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Maturità: `CORE`
- Stato: **revisione tecnica, visuali bloccate**
- Versione candidata: `0.1.1-draft2`
- Data di apertura: 30 luglio 2026
- Data dell'ultima ricerca web: 30 luglio 2026
- Data dell'ultima verifica delle fonti: 30 luglio 2026
- Data di congelamento editoriale: non assegnata
- Documentazione PyTorch verificata: stable `2.13`
- Ambiente eseguito: Python `3.13.5`, PyTorch `2.10.0+cpu`
- Oggetto continuo: una richiesta di assistenza, `Il pacco non è arrivato`, elaborata da sistemi costruiti in modi diversi
- Concetti differiti: generalizzazione, funzioni obiettivo, gradienti, architetture neurali, famiglie generative, pretraining, scaling, sicurezza e governance

> **Stato della candidatura.** Testo, fonti, claim, codice e test sono disponibili. Le visuali `AI-01` e `AI-02` restano bloccate: le candidate prodotte finora dallo strumento immagini rappresentavano schermate o riepiloghi del progetto anziché i diagrammi tecnici specificati e sono state respinte. Il capitolo non può passare alla revisione autoriale prima del relativo audit visuale.

## In questo capitolo

La frase `Il pacco non è arrivato` può entrare in programmi molto diversi. Un'automazione può cercare parole predefinite e aprire una procedura. Un classificatore può assegnare la richiesta alla categoria `problema di consegna`. Un modello generativo può comporre una risposta. Un sistema più ampio può combinare un modello, una ricerca nel database degli ordini e regole che stabiliscono quali azioni siano autorizzate.

Non ogni programma che elabora questa frase deve essere chiamato automaticamente `AI`. Il confine dipende dalla definizione adottata e dal tipo di inferenza eseguita. Useremo la definizione OECD aggiornata come ancora operativa, poi distingueremo le proprietà tecniche senza affidare tutto a un'unica etichetta.

`AI`, `machine learning`, `deep learning`, `modello generativo`, `generative AI` e `foundation model` non indicano la stessa cosa. Alcuni termini descrivono **come** viene costruita la relazione tra input e output. Altri descrivono **quale obiettivo** viene modellato. Altri ancora riguardano **quanto è ampio** il riuso previsto del modello.

Alla fine del capitolo sapremo separare il modello dai componenti circostanti e descrivere un sistema lungo tre assi: meccanismo, obiettivo e ampiezza. Un piccolo esempio PyTorch renderà inoltre osservabile la differenza tra training e inference.

# 1. Dal programma al sistema di AI

Un programma riceve input, esegue operazioni e produce output. Questa descrizione include una calcolatrice, un database, un compilatore e un modello neurale, quindi non basta a delimitare l'intelligenza artificiale.

La definizione OECD aggiornata descrive un **AI system** come un sistema machine-based che, per obiettivi espliciti o impliciti, inferisce dagli input come produrre output quali predizioni, contenuti, raccomandazioni o decisioni. Gli output possono influire su ambienti fisici o virtuali [OECD, 2024].

In questa definizione, `inferire` non significa necessariamente usare una rete neurale. Il sistema determina, a partire dagli input e dal proprio meccanismo, quale output produrre. L'obiettivo può essere scritto direttamente in una funzione, incorporato in regole oppure riflesso nei dati usati durante l'addestramento. L'OECD tratta questi casi come possibilità che possono sovrapporsi [OECD, 2024].

Torniamo alla richiesta:

```text
Il pacco non è arrivato
```

Un sistema di assistenza potrebbe produrre una categoria:

```text
categoria = problema_di_consegna
```

oppure una risposta:

```text
risposta = "Controllo subito lo stato della spedizione."
```

oppure una proposta di azione:

```text
azione = apri_ticket_e_richiedi_numero_ordine
```

La natura dell'output non identifica il meccanismo. La stessa categoria può essere ottenuta con una regola scritta a mano, con una regressione logistica o con una rete neurale. Per descrivere il comportamento osservabile occorre inoltre separare il **modello** dal **sistema**.

Nel lessico di questo libro, un modello è un componente matematico parametrizzato che trasforma input in output. Un sistema comprende il modello e i componenti che ne organizzano l'uso: acquisizione e validazione degli input, regole, retrieval, tool, interfacce, autorizzazioni e post-processing.

Questa è una convenzione editoriale, non una definizione universale. È però coerente con il fatto che NIST organizza il risk management lungo l'intero ciclo di vita di prodotti, servizi e sistemi AI, non soltanto attorno al file dei parametri [NIST AI RMF 1.0, 2023]. Un modello può rimanere invariato mentre il comportamento del sistema cambia perché vengono modificati il database consultato, le autorizzazioni o il modo in cui l'output viene presentato.

# 2. Regole esplicite e comportamento appreso

Consideriamo una prima implementazione:

```text
se il testo contiene "pacco" e "non è arrivato":
    categoria = problema_di_consegna
```

La relazione tra input e output è stata specificata direttamente. Il comportamento dipende dalle regole e dalle rappresentazioni scelte dal progettista. Un sistema di questo tipo può essere descritto come **rule-based**. Quando usa rappresentazioni esplicite di fatti, simboli e relazioni, appartiene alla tradizione dell'AI simbolica.

Ora immaginiamo di raccogliere richieste già etichettate:

```text
"Il corriere non è passato"       -> problema_di_consegna
"Voglio cambiare indirizzo"       -> modifica_ordine
"Il pacco non è arrivato"         -> problema_di_consegna
"La carta è stata rifiutata"      -> problema_di_pagamento
```

Un algoritmo può cercare valori dei parametri che riducano gli errori su questi esempi. Non viene scritta una regola separata per ogni formulazione. Vengono definiti una famiglia di funzioni, un obiettivo e una procedura che modifica i parametri usando i dati. Questo è il nucleo del **machine learning**.

Il contrasto non è assoluto. Un'applicazione reale può usare una regola per validare il numero d'ordine, un classificatore appreso per assegnare la categoria, una rete neurale per rappresentare il testo e un controllo finale che impedisce azioni non autorizzate.

Nel capitolo useremo `simbolico`, `statistico` e `neurale` come tassonomia di lavoro non esaustiva. Non sono tre insiemi sempre disgiunti. `Statistico` indica qui modelli descritti tramite quantità probabilistiche o criteri di stima. `Neurale` indica modelli composti da trasformazioni parametrizzate organizzate in reti. Un modello neurale viene normalmente addestrato con metodi statistici, mentre un sistema simbolico può contenere componenti appresi.

La prima dimensione da annotare è quindi il **meccanismo predominante**:

```text
regole esplicite
modello appreso dai dati
rete neurale profonda
sistema ibrido
```

Queste etichette non dicono ancora se il sistema classifica o genera, né quanto sia ampio il suo campo d'uso.

# 3. AI, machine learning e deep learning

Non esiste una singola tassonomia che esaurisca tutto il campo. Per questo percorso useremo `AI` come categoria più ampia, entro la quale collochiamo metodi di ricerca, pianificazione, rappresentazione della conoscenza, decisione e apprendimento.

Il **machine learning** è uno degli approcci all'AI. Invece di descrivere interamente il comportamento tramite regole operative, si usa esperienza sotto forma di dati, interazioni o segnali di valutazione per scegliere i parametri di un modello. Goodfellow, Bengio e Courville collocano esplicitamente il machine learning all'interno dell'AI e ricordano che esistono approcci AI non basati sull'apprendimento automatico, per esempio sistemi costruiti attorno a knowledge base [Goodfellow et al., 2016, cap. 1].

Il **representation learning** è una parte del machine learning in cui anche la rappresentazione usata per il compito viene appresa. Un classificatore può ricevere feature progettate manualmente, come la presenza di parole specifiche. Un modello di representation learning può invece produrre vettori intermedi utili a separare le categorie.

Il **deep learning** usa composizioni di più trasformazioni apprese. Ogni livello riceve una rappresentazione e ne produce un'altra. La profondità permette di costruire funzioni complesse come composizioni di funzioni più semplici. Non esiste una soglia universalmente accettata oltre la quale un modello diventa `deep`; il termine descrive una famiglia di metodi, non un numero normativo di layer [Goodfellow et al., 2016, cap. 1].

La relazione concettuale può essere riassunta così:

```text
AI
└── machine learning
    └── representation learning
        └── deep learning
```

Questo schema rappresenta una relazione tra concetti, non l'architettura completa di ogni sistema. Un'applicazione può contenere una rete profonda e regole simboliche, oppure usare un modello appreso all'interno di una procedura di ricerca.

La gerarchia non implica che `deep learning` significhi `generativo`. Un modello generativo non deve necessariamente essere una rete profonda. Un sistema AI può non contenere machine learning. Una rete neurale, infine, non coincide con il prodotto o servizio che la incorpora.

# 4. Dati, parametri e iperparametri

Un modello parametrizzato contiene valori che determinano la trasformazione eseguita. In un modello lineare con due feature e due classi, i parametri principali sono una matrice di pesi e un vettore di bias:

$$
\mathbf{z}=W\mathbf{x}+\mathbf{b}.
$$

L'input `x` contiene due feature numeriche. L'output `z` contiene due logit, uno per classe. La softmax può trasformare i logit in valori normalizzati, ma la scelta di `W` e `b` determina la separazione appresa.

I **dati di training** forniscono esempi usati per modificare i parametri. Una **funzione obiettivo** misura, secondo una regola dichiarata, quanto l'output corrente differisce dal risultato desiderato. Un **optimizer** applica aggiornamenti ai parametri usando gradienti o altre quantità calcolate dalla procedura di apprendimento.

Gli **iperparametri** configurano la procedura o la struttura del modello. Nel piccolo esempio del capitolo, il learning rate `0.1` e il numero di iterazioni `100` sono scelti prima dell'esecuzione e non vengono modificati da `optimizer.step()`.

La distinzione è relativa alla procedura considerata. Un valore può essere iperparametro in un esperimento e diventare output di un'altra procedura di ricerca. La domanda operativa è sempre la stessa: quale istruzione può modificarlo?

Quando i parametri e le informazioni necessarie a riutilizzarli vengono salvati, si ottiene un **checkpoint**. In un progetto reale il checkpoint può comprendere anche stato dell'optimizer, contatori, configurazione e metadati. Il termine non indica quindi soltanto una matrice di pesi.

# 5. Training e inference sono due fasi diverse

Durante il **training**, il sistema usa esempi e un segnale obiettivo per modificare i parametri. Nel caso supervisionato più semplice, una iterazione contiene:

```text
input e target
-> output del modello
-> loss
-> gradienti
-> aggiornamento dei parametri
```

La documentazione PyTorch presenta questo ciclo tramite `optimizer.zero_grad()`, forward pass, calcolo della loss, `loss.backward()` e `optimizer.step()` [PyTorch Tutorials 2.13, Optimizing Model Parameters]. `optimizer.step()` applica l'aggiornamento ai parametri registrati nell'optimizer [PyTorch 2.13, torch.optim].

Durante l'**inference**, un input nuovo viene trasformato usando i parametri disponibili. Nel caso base non viene eseguito un passo dell'optimizer:

```text
nuovo input
-> modello con parametri fissati
-> output
```

Esistono metodi che modificano stato o parametri al test time, ma devono essere nominati esplicitamente perché cambiano questo contratto. Nel percorso base, `inference` indica l'uso del modello addestrato senza update dei parametri.

In PyTorch occorre distinguere `model.eval()` e `torch.inference_mode()`. `eval()` imposta la modalità di evaluation dei moduli che cambiano comportamento tra training ed evaluation, come Dropout e BatchNorm. `inference_mode()` disabilita il tracciamento autograd e altre strutture necessarie al calcolo dei gradienti. Chiamare soltanto `eval()` non disabilita autograd, e usare soltanto `inference_mode()` non sostituisce la modalità di evaluation dei moduli interessati [PyTorch 2.13, `Module` e `inference_mode`].

Il seguente snippet usa quattro esempi illustrativi con due feature e due classi. Il layer lineare viene addestrato con cross-entropy e SGD. La versione completa conserva copie dei parametri prima e dopo le due fasi.

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

Il file eseguito è [`code/snip_ai_001_training_inference.py`](code/snip_ai_001_training_inference.py).

Nell'ambiente registrato, la loss passa da `0.641941` a `0.045580`. Almeno un parametro cambia durante il training. Nessun parametro cambia durante l'inference. Il nuovo input produce logit con shape `[1,2]` e la classe prevista è `0`.

Questi valori non dimostrano generalizzazione. Il dataset è costruito soltanto per rendere visibile la differenza tra le due fasi. La generalizzazione richiede dati separati e un protocollo di valutazione, che verranno introdotti nei capitoli successivi.

# 6. Predire una proprietà o modellare i dati

Dopo aver distinto il meccanismo di apprendimento, possiamo descrivere un secondo asse: **l'obiettivo modellato**.

In un problema di classificazione, un approccio discriminativo può stimare direttamente la distribuzione condizionata

$$
p(y\mid x),
$$

o imparare una frontiera decisionale equivalente per il compito. `x` rappresenta la richiesta e `y` la categoria.

Un classificatore generativo specifica invece un modello per la distribuzione congiunta, spesso tramite

$$
p(x,y)=p(x\mid y)p(y),
$$

e usa tale modello anche per calcolare la classe. Più in generale, i modelli generativi contemporanei possono modellare una distribuzione dei dati non condizionata oppure una distribuzione condizionata, per esempio `p(x|c)`, dalla quale produrre campioni compatibili con una condizione `c`.

Ng e Jordan confrontano logistic regression e naive Bayes come esempi discriminativo e generativo. Il loro risultato riguarda quella coppia di modelli e le ipotesi analizzate; non dimostra che un paradigma sia sempre superiore [Ng e Jordan, 2001].

La distinzione riguarda l'obiettivo probabilistico o il ruolo nel sistema, non una forma grafica obbligatoria. Nel framework GAN, un generatore `G` viene addestrato per catturare la distribuzione dei dati e produrre campioni, mentre un discriminatore `D` cerca di distinguere dati reali e campioni prodotti [Goodfellow et al., 2014]. I due ruoli convivono nello stesso processo di training.

Un modello discriminativo può essere una rete profonda. Un modello generativo può essere neurale oppure appartenere a un'altra famiglia probabilistica. L'asse `discriminativo/generativo` non sostituisce quindi l'asse `regole/apprendimento/rete profonda`.

# 7. Che cosa indica generative AI

Il termine **generative AI** viene usato per sistemi orientati alla produzione di contenuto sintetico condizionato da input, istruzioni o contesto. Il profilo NIST descrive modelli che emulano struttura e caratteristiche dei dati di input per produrre contenuto sintetico derivato. Il documento include testo, immagini, video, audio e altri contenuti digitali [NIST AI 600-1, 2024].

Nel nostro esempio, un classificatore produce una categoria tra opzioni definite:

```text
problema_di_consegna
```

Un sistema generativo può produrre una sequenza testuale:

```text
Mi dispiace per il ritardo. Inserisci il numero dell'ordine e controllerò lo stato della spedizione.
```

`Produrre` non implica intenzione, esperienza soggettiva o comprensione umana. Indica l'esecuzione di una procedura che genera un output sulla base del modello, dell'input e degli altri componenti del sistema.

Un modello linguistico può produrre una distribuzione sui token successivi. Il sistema applicativo può aggiungere un template, retrieval sul database degli ordini, tool, autorizzazioni e controlli sull'output. Il comportamento osservato dall'utente appartiene al sistema completo e non può essere attribuito automaticamente al solo checkpoint.

Il profilo NIST chiarisce anche che **non tutta la generative AI deriva da foundation model** [NIST AI 600-1, 2024]. Un modello generativo piccolo e addestrato per un dominio ristretto può produrre contenuto senza avere il ruolo di foundation model.

# 8. Foundation model e adattamento

Il report dello Stanford Center for Research on Foundation Models introduce il termine **foundation model** per un modello addestrato su dati ampi, generalmente con self-supervision su larga scala, adattabile a numerosi compiti downstream [Bommasani et al., 2021].

La proprietà centrale non è soltanto la generazione. È il ruolo di base riutilizzabile. Il modello può essere adattato tramite fine-tuning, instruction tuning, adapter, prompting, retrieval o configurazioni di sistema. Questi meccanismi verranno trattati più avanti.

Per ora separiamo tre oggetti:

```text
modello di base
-> adattamento o configurazione
-> sistema applicativo
```

Il modello di base può restare lo stesso mentre cambiano il dataset di adattamento, il prompt di sistema, gli strumenti disponibili e le regole operative. Non è quindi corretto dedurre tutte le proprietà del sistema dalla sola famiglia del foundation model.

`Foundation model` e `generative model` non sono sinonimi. Molti foundation model contemporanei hanno capacità generative, ma la definizione riguarda ampiezza del pretraining e adattabilità. Un modello generativo specialistico può non fungere da fondazione per un insieme ampio di compiti.

# 9. Generalista e specialistico sono termini relativi

Un sistema **specialistico** è progettato e valutato per un insieme ristretto di compiti o condizioni. Un classificatore delle richieste di consegna è specialistico rispetto a un sistema capace di classificare richieste, generare risposte, tradurre testi, analizzare immagini e chiamare strumenti.

Un sistema viene spesso chiamato **generalista** quando copre molti compiti o modalità. Il termine non possiede però una soglia numerica universale. Un modello può essere generalista rispetto a un'applicazione aziendale e specialistico rispetto all'insieme delle capacità umane.

Nel libro, `generalista` e `specialistico` descrivono l'ampiezza relativa del riuso e delle valutazioni. Non implicano qualità, affidabilità o autonomia. Un sistema generalista può fallire su un dominio specifico; un sistema specialistico può essere migliore nel proprio perimetro.

La stessa cautela vale per `foundation model`. Il pretraining ampio rende possibile l'adattamento, ma non garantisce che ogni sistema costruito sul modello sia competente in ogni compito.

# 10. Tre assi invece di una lista di sinonimi

Possiamo ora descrivere un sistema lungo tre dimensioni indipendenti.

| Asse | Domanda | Esempi di valori |
|---|---|---|
| Meccanismo | Come viene costruita la relazione tra input e output? | regole, modello appreso, rete profonda, sistema ibrido |
| Obiettivo | Quale relazione, distribuzione o decisione viene modellata? | discriminativo, generativo, decisionale |
| Ampiezza | Quanto è ampio il riuso previsto e verificato? | specialistico, modello di base adattabile, generalista |

Per la richiesta `Il pacco non è arrivato` possiamo costruire:

1. un'automazione specialistica rule-based che apre un ticket;
2. un classificatore specialistico basato su deep learning;
3. un modello generativo specialistico che compone risposte in un dominio;
4. un foundation model generativo adattato all'assistenza clienti;
5. un sistema ibrido che combina foundation model, retrieval, tool e regole.

Nel primo caso, la parola `AI` dipende dalla definizione e dal grado di inferenza attribuito alla semplice automazione. L'esempio serve a mostrare il meccanismo, non a risolvere universalmente il confine tra software ordinario e AI.

Nessun asse determina automaticamente gli altri. `Rete profonda` non implica `generativo`. `Generativo` non implica `foundation model`. `Foundation model` non implica che il sistema applicativo sia privo di specializzazione.

> **Visuale prevista `AI-01`.** La figura dovrà mostrare i tre assi attorno alla stessa richiesta. Le candidate prodotte finora non rappresentavano questa tassonomia e sono state respinte.

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

NIST usa il concetto di AI lifecycle per ricordare che rischi, responsabilità e prestazioni dipendono dalle fasi e dagli attori coinvolti [NIST AI RMF 1.0, 2023]. Una misura ottenuta durante lo sviluppo non descrive automaticamente il comportamento dopo il deployment. Un checkpoint non documenta da solo i dati, il contesto d'uso o le procedure di controllo.

Nel caso della richiesta di consegna, il modello può essere identico in due applicazioni, ma i sistemi differiscono se uno può soltanto suggerire una categoria mentre l'altro può modificare un ordine reale. Le autorizzazioni e le conseguenze operative appartengono al sistema.

> **Visuale prevista `AI-02`.** La figura dovrà separare training e inference: dati, loss, gradienti, optimizer e checkpoint aggiornato a sinistra; nuovo input, checkpoint fissato e output a destra. Anche questa visuale resta aperta.

# 12. Errori di classificazione frequenti

## `AI` e `machine learning` usati come sinonimi

Il machine learning è un approccio all'AI, non la definizione completa del campo. Un sistema basato su ricerca, pianificazione o rappresentazione esplicita della conoscenza può rientrare nell'AI senza apprendere parametri dai dati.

## `Machine learning` e `deep learning` usati come sinonimi

Il deep learning è una parte del machine learning. Regressione lineare, alberi decisionali e molti modelli probabilistici sono machine learning ma non vengono normalmente descritti come deep learning.

## `Deep` interpretato come soglia assoluta

La profondità riguarda la composizione di trasformazioni. Non esiste un numero universalmente valido di layer che separi ogni modello shallow da ogni modello deep.

## `Generativo` interpretato come sinonimo di foundation model

Un modello generativo può essere piccolo e specialistico. Il profilo NIST dichiara esplicitamente che non tutta la generative AI deriva da foundation model.

## `Foundation model` interpretato come prodotto completo

Un foundation model è una base adattabile. Retrieval, tool, dati di dominio, autorizzazioni e interfaccia appartengono al sistema costruito attorno al modello.

## `Inference` interpretata come aggiornamento automatico

Nel caso base, l'inference usa i parametri disponibili senza un passo dell'optimizer. Tecniche di test-time adaptation esistono, ma cambiano il contratto e devono essere dichiarate.

## `eval()` interpretato come disabilitazione dei gradienti

In PyTorch, `eval()` modifica la modalità dei moduli interessati. `inference_mode()` o `no_grad()` gestiscono il tracciamento autograd. Le operazioni non sono equivalenti.

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
6. Classifichiamo l'obiettivo come discriminativo, generativo o decisionale, dichiarando la formulazione.
7. Verifichiamo se il modello è specialistico oppure funge da base adattabile per compiti diversi.
8. Ricostruiamo il sistema applicativo, includendo retrieval, tool, regole, interfacce e autorizzazioni.

La tassonomia non assegna un'etichetta unica. Produce una descrizione composta. Un sistema può essere contemporaneamente:

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

Indicare quale istruzione modifica i parametri nello snippet PyTorch e quale blocco esegue soltanto l'inference.

## Confine

Spiegare perché un modello generativo non è necessariamente un foundation model e perché un foundation model non coincide con il sistema applicativo.

## Trasferimento

Classificare un filtro antispam che usa una rete neurale addestrata su email etichettate. Descriverlo lungo gli assi meccanismo, obiettivo e ampiezza.

## Variazione

Supporre di aggiungere al sistema di assistenza un tool che legge lo stato reale della spedizione. Dire quale parte del modello può restare invariata e quale parte del sistema è cambiata.

# 15. Esercizi

1. Descrivere un sistema di raccomandazione separando input, modello, output e componenti di sistema.
2. Scrivere una regola esplicita per classificare una richiesta di consegna, poi indicare due formulazioni che non riconoscerebbe.
3. Modificare `SNIP-AI-001` rimuovendo il ciclo di training. Verificare che i parametri rimangano invariati e confrontare la loss.
4. Aggiungere una seconda inference con un input differente e verificare la shape dell'output.
5. Trovare un esempio di modello generativo specialistico che non richieda la nozione di foundation model.
6. Spiegare perché un sistema costruito su un modello generalista può essere specialistico nel deployment.
7. Elencare tre componenti di un sistema di generative AI che non fanno parte del checkpoint.
8. Confrontare `model.eval()` e `torch.inference_mode()` usando la documentazione PyTorch citata.

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

- Review fattuale: completata sulla bozza `0.1.1-draft2`, visuali escluse
- Review matematica: completata per formula lineare e distribuzioni introduttive
- Review architetturale e terminologica: completata, modello e sistema distinti
- Review temporale: fonti ricontrollate il 30 luglio 2026
- Review codice: superata tecnicamente
- Review visuale: **bloccata**, candidate errate respinte
- Review incrociata: superata per testo e codice; visuali aperte
- Review didattica: seconda lettura completata sul testo
- Review autoriale: non aperta
- Data di congelamento: non assegnata
- Commit congelato: non assegnato
