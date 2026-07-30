<!--
chapter_id: CH-P01-AI-FIELD
part_id: P01
order_key: 010
title: Che cos'è l'intelligenza artificiale
maturity: CORE
status: revisione editoriale completata, visuali aperte
version: 0.2.0-rc1
opened: 2026-07-30
last_web_research: 2026-07-30
last_source_check: 2026-07-30
environment: Python 3.13.5, PyTorch 2.10.0+cpu
deferred: generalizzazione, gradienti, architetture neurali, pretraining, scaling, sicurezza, governance
-->

# Capitolo 1. Che cos'è l'intelligenza artificiale

La frase «Il pacco non è arrivato» può essere elaborata in molti modi. Un programma può cercare alcune parole e aprire automaticamente un ticket. Un classificatore può assegnare la richiesta alla categoria `problema_di_consegna`. Un modello generativo può comporre una risposta. Un sistema più ampio può inoltre consultare il database degli ordini, verificare lo stato della spedizione e decidere quali azioni sono consentite.

Dall'esterno, tutti questi casi ricevono lo stesso testo e producono un risultato utile. All'interno, però, possono funzionare in modi molto diversi. Chiamarli semplicemente «AI» non basta a descriverli e, nel caso di una semplice automazione, può persino essere discutibile. Per orientarci useremo come riferimento operativo la definizione aggiornata dell'OCSE, senza trattarla come l'unico modo possibile di delimitare il campo. Costruiremo poi un lessico più preciso, capace di distinguere il meccanismo con cui nasce il comportamento, il tipo di risultato modellato e l'ampiezza dei compiti per cui il sistema viene riutilizzato.

## Una stessa richiesta, sistemi diversi

Un programma riceve un input, esegue alcune operazioni e produce un output. Questa descrizione comprende una calcolatrice, un compilatore, un database e una rete neurale, quindi è troppo ampia per definire da sola l'intelligenza artificiale.

L'OCSE descrive un **sistema di AI** come un sistema basato su macchine che, a partire dagli input ricevuti e in relazione a obiettivi espliciti o impliciti, inferisce come produrre predizioni, contenuti, raccomandazioni o decisioni. Questi output possono influire su ambienti fisici o virtuali [OECD, 2024]. In questo contesto, il verbo *inferire* non implica necessariamente una rete neurale. Indica che il sistema determina un output a partire dagli input, dal proprio stato e dal meccanismo che lo governa.

Torniamo alla richiesta iniziale. Un'applicazione di assistenza potrebbe produrre la categoria `problema_di_consegna`, la frase «Controllo subito lo stato della spedizione» oppure la proposta di aprire un ticket e chiedere il numero dell'ordine. Il tipo di output non rivela, da solo, come sia stato ottenuto. La stessa categoria può derivare da una regola scritta a mano, da una regressione logistica o da una rete neurale.

Per descrivere con chiarezza questi casi, nel libro distingueremo **modello** e **sistema**. Un modello è un componente matematico parametrizzato che trasforma input in output. Il sistema comprende il modello, quando presente, e i componenti che ne organizzano l'uso: validazione degli input, regole, retrieval, strumenti esterni, autorizzazioni, interfacce e post-processing. Si tratta di una convenzione editoriale, non di una definizione universale, ma è coerente con l'impostazione del NIST, che tratta rischi e prestazioni lungo l'intero ciclo di vita di prodotti, servizi e sistemi AI [NIST AI RMF 1.0, 2023].

La distinzione ha conseguenze pratiche. Due applicazioni possono usare lo stesso checkpoint e comportarsi diversamente perché consultano dati differenti, applicano regole differenti o possiedono autorizzazioni differenti. Al contrario, due modelli diversi possono essere inseriti nello stesso sistema senza cambiare l'interfaccia visibile all'utente.

## Quando il comportamento è scritto e quando viene appreso

Consideriamo una prima soluzione alla richiesta di consegna:

```text
se il testo contiene "pacco" e "non è arrivato":
    categoria = problema_di_consegna
```

Qui la relazione tra input e output è stata specificata direttamente. Il progettista ha scelto le parole da cercare e l'azione da eseguire. Un sistema di questo tipo può essere descritto come **rule-based**. Quando usa rappresentazioni esplicite di fatti, simboli e relazioni, si colloca nella tradizione dell'AI simbolica.

La stessa regola fallisce facilmente davanti a formulazioni non previste, come «Il corriere non è mai passato» o «La spedizione risulta ferma da una settimana». Per evitare di scrivere una condizione separata per ogni frase, possiamo raccogliere richieste già etichettate:

```text
"Il corriere non è passato"  -> problema_di_consegna
"Voglio cambiare indirizzo"  -> modifica_ordine
"Il pacco non è arrivato"    -> problema_di_consegna
"La carta è stata rifiutata" -> problema_di_pagamento
```

Un algoritmo può allora cercare i valori dei parametri che riducono gli errori su questi esempi. Non descriviamo più tutte le regole operative. Definiamo una famiglia di funzioni, un obiettivo e una procedura che modifica i parametri usando i dati. Questo è il nucleo del **machine learning**.

La separazione non è assoluta. Un'applicazione reale può usare una regola per validare il numero d'ordine, un classificatore appreso per riconoscere la categoria, una rete neurale per rappresentare il testo e un controllo finale che impedisce azioni non autorizzate. Per questo `simbolico`, `statistico` e `neurale` sono descrizioni utili, ma non formano tre insiemi sempre disgiunti.

L'**intelligenza artificiale** è il campo più ampio. Comprende, tra gli altri, metodi di ricerca, pianificazione, rappresentazione della conoscenza, decisione e apprendimento. Il machine learning è uno degli approcci disponibili: usa dati, interazioni o segnali di valutazione per scegliere i parametri di un modello. Goodfellow, Bengio e Courville collocano esplicitamente il machine learning all'interno dell'AI e ricordano che esistono anche approcci AI non basati sull'apprendimento automatico, per esempio sistemi costruiti attorno a knowledge base [Goodfellow et al., 2016, cap. 1].

Nel **representation learning** viene appresa anche la rappresentazione utile per il compito. Un classificatore tradizionale può ricevere feature progettate a mano, come la presenza di parole specifiche. Un modello di representation learning produce invece vettori intermedi che aiutano a separare le categorie. Il **deep learning** usa più trasformazioni apprese in composizione: ogni livello riceve una rappresentazione e ne produce un'altra. Non esiste una soglia universalmente accettata di layer oltre la quale un modello diventa `deep`; il termine identifica una famiglia di metodi, non un limite normativo [Goodfellow et al., 2016, cap. 1].

Possiamo quindi leggere la relazione tra i termini come una progressione concettuale: il deep learning appartiene al representation learning, che appartiene al machine learning, che a sua volta è uno degli approcci all'AI. La relazione non descrive l'architettura completa di ogni applicazione. Un sistema può combinare una rete profonda con regole simboliche o inserire un modello appreso dentro una procedura di ricerca.

## Parametri, training e inference

Un modello parametrizzato contiene valori che determinano la trasformazione eseguita. Nel caso di un semplice classificatore lineare con due feature e due classi, possiamo scrivere:

$$
\mathbf{z}=W\mathbf{x}+\mathbf{b}.
$$

Il vettore `x` contiene le feature di input. La matrice `W` e il vettore `b` sono i parametri. Il risultato `z` contiene due logit, uno per classe. La softmax può trasformarli in valori normalizzati, ma la separazione appresa dipende dai parametri scelti.

Durante il **training**, gli esempi e una funzione obiettivo forniscono il segnale necessario a modificare quei parametri. Un optimizer applica gli aggiornamenti usando i gradienti o altre quantità calcolate dalla procedura di apprendimento. Il learning rate e il numero di iterazioni sono invece **iperparametri**: configurano l'esperimento, ma non vengono modificati direttamente dal passo dell'optimizer.

La distinzione dipende dalla procedura considerata. Un valore scelto come iperparametro in un esperimento potrebbe essere prodotto da un'altra procedura di ricerca. La domanda utile è sempre la stessa: quale operazione può modificarlo?

Quando i parametri e le informazioni necessarie a riutilizzarli vengono salvati, otteniamo un **checkpoint**. In un progetto reale il checkpoint può comprendere anche lo stato dell'optimizer, la configurazione, i contatori e altri metadati. Non coincide quindi necessariamente con una sola matrice di pesi.

Durante l'**inference**, un nuovo input viene elaborato usando i parametri disponibili. Nel caso base non viene eseguito un passo dell'optimizer e il checkpoint rimane invariato. Questa differenza è visibile nel seguente esempio PyTorch, costruito con quattro osservazioni illustrative e due classi:

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

Nel run registrato, la loss passa da `0.641941` a `0.045580`. Almeno un parametro cambia durante il training; nessun parametro cambia durante l'inference. Il nuovo input produce logit di shape `[1,2]` e la classe prevista è `0`.

Il risultato serve soltanto a distinguere le due fasi. Quattro esempi non costituiscono una valutazione della generalizzazione, che richiede dati separati e un protocollo appropriato.

> **Nota su PyTorch.** `model.eval()` imposta la modalità di evaluation dei moduli che cambiano comportamento tra training ed evaluation, come Dropout e BatchNorm. `torch.inference_mode()` disabilita invece il tracciamento autograd e altre strutture usate per i gradienti. Le due operazioni hanno ruoli diversi e non sono intercambiabili [PyTorch 2.13, `Module` e `inference_mode`].

## Predire una proprietà o modellare i dati

Finora abbiamo distinto il modo in cui il comportamento viene ottenuto. Una seconda domanda riguarda ciò che il modello descrive.

In un problema di classificazione, un approccio **discriminativo** può stimare direttamente la distribuzione condizionata

$$
p(y\mid x),
$$

dove `x` è la richiesta e `y` la categoria, oppure può apprendere una frontiera decisionale equivalente per il compito. Un classificatore **generativo** specifica invece un modello della distribuzione congiunta, spesso attraverso

$$
p(x,y)=p(x\mid y)p(y),
$$

e usa quel modello anche per calcolare la classe. Ng e Jordan confrontano logistic regression e naive Bayes come esempi dei due approcci; il loro risultato riguarda quella coppia e le ipotesi analizzate, non stabilisce la superiorità universale di un paradigma [Ng e Jordan, 2001].

La parola *generativo* copre anche modelli che descrivono una distribuzione dei dati e producono nuovi campioni. La distribuzione può essere non condizionata oppure dipendere da una condizione, come in `p(x|c)`. Nel framework GAN, per esempio, il generatore viene addestrato a produrre campioni compatibili con la distribuzione dei dati, mentre il discriminatore cerca di distinguere dati reali e campioni generati [Goodfellow et al., 2014]. I due ruoli convivono nello stesso processo di training.

Questa distinzione riguarda l'obiettivo probabilistico o il ruolo nel sistema, non una forma architetturale obbligatoria. Un modello discriminativo può essere una rete profonda; un modello generativo può essere neurale oppure appartenere a un'altra famiglia probabilistica.

Il termine **generative AI** viene usato per modelli e sistemi orientati alla produzione di contenuto sintetico a partire da input, istruzioni o contesto. Il profilo NIST include testo, immagini, audio, video e altri contenuti digitali [NIST AI 600-1, 2024]. Nel nostro esempio, il classificatore restituisce una categoria predefinita; un sistema generativo può invece comporre una risposta come «Mi dispiace per il ritardo. Inserisci il numero dell'ordine e controllerò lo stato della spedizione».

Produrre una frase non implica intenzione o comprensione umana. Significa eseguire una procedura che genera un output in funzione del modello, dell'input e degli altri componenti del sistema. Un'applicazione può aggiungere al modello un prompt di sistema, un recupero di dati sugli ordini, strumenti esterni, autorizzazioni e controlli sull'output. Il comportamento osservato appartiene all'insieme di questi componenti, non al solo checkpoint.

## Foundation model, adattamento e varietà dei compiti

Il report dello Stanford Center for Research on Foundation Models introduce il termine **foundation model** per indicare un modello addestrato su dati ampi, in genere con self-supervision su larga scala, e adattabile a numerosi compiti successivi [Bommasani et al., 2021]. La proprietà centrale non è soltanto la capacità di generare contenuti, ma il ruolo di base riutilizzabile.

Un foundation model può essere adattato tramite fine-tuning, instruction tuning, adapter, prompting, retrieval o configurazioni del sistema. Questi metodi verranno studiati nei capitoli successivi. Per ora è sufficiente distinguere tre livelli: il modello di base, l'eventuale adattamento e il sistema applicativo. Il modello può restare invariato mentre cambiano i dati di dominio, gli strumenti disponibili, le autorizzazioni e le regole operative.

`Foundation model` e `modello generativo` non sono sinonimi. Il profilo NIST chiarisce che non tutta la generative AI deriva da foundation model [NIST AI 600-1, 2024]. Un modello piccolo e addestrato per un dominio ristretto può produrre contenuto senza essere usato come base per molti compiti. Allo stesso modo, il fatto che un modello sia ampiamente adattabile non dice che ogni applicazione costruita su di esso sia generalista.

I termini **generalista** e **specialistico** sono relativi al perimetro considerato. Un classificatore delle richieste di consegna è specialistico rispetto a un sistema capace di classificare, tradurre, generare testo, analizzare immagini e usare strumenti. Lo stesso sistema, tuttavia, può essere generalista all'interno di un reparto aziendale e specialistico rispetto alla varietà delle attività umane. Nel libro useremo questi termini in base alla gamma di compiti e contesti per cui un modello o un sistema è stato progettato e valutato, non come giudizi automatici di qualità o affidabilità.

## Tre domande per descrivere un sistema

Le etichette introdotte finora rispondono a domande diverse. Per non confonderle, descriveremo ogni sistema lungo tre dimensioni.

| Aspetto | Domanda | Esempi |
|---|---|---|
| Meccanismo | Come viene costruita la relazione tra input e output? | regole, modello appreso, rete profonda, sistema ibrido |
| Obiettivo | Quale relazione, distribuzione o decisione viene descritta? | discriminativo, generativo, decisionale |
| Ampiezza | Per quali compiti e contesti è previsto e verificato il riuso? | specialistico, base adattabile, generalista |

La richiesta «Il pacco non è arrivato» può quindi essere gestita da un'automazione specialistica basata su regole, da un classificatore neurale specialistico, da un modello generativo addestrato nel dominio dell'assistenza oppure da un sistema ibrido costruito attorno a un foundation model, un database e un insieme di strumenti.

Nessuna dimensione determina automaticamente le altre. Una rete profonda non è necessariamente generativa. Un modello generativo non è necessariamente un foundation model. Un foundation model non rende generalista ogni applicazione che lo utilizza.

Questa descrizione non esaurisce il ciclo di vita di un sistema. Dati, valutazione, deployment, monitoraggio e ritiro influenzano ciò che il sistema può fare e i rischi che introduce. Per esempio, lo stesso modello di assistenza assume conseguenze operative diverse se può soltanto suggerire una categoria oppure modificare direttamente un ordine. Le autorizzazioni appartengono al sistema, non alla formula del modello.

<!-- Inserire AI-01 dopo la validazione visuale. -->
<!-- Inserire AI-02 dopo la validazione visuale. -->

## Le distinzioni che contano

A questo punto possiamo chiarire alcuni equivoci frequenti senza trasformare i termini in sinonimi.

- **AI e machine learning.** Il machine learning è un approccio all'AI, non l'intero campo. Ricerca, pianificazione e rappresentazione simbolica della conoscenza possono rientrare nell'AI senza apprendere parametri dai dati.
- **Machine learning e deep learning.** Il deep learning è una parte del machine learning. Regressione lineare, alberi decisionali e molti modelli probabilistici non vengono normalmente descritti come deep learning.
- **Generativo e foundation model.** Un modello generativo può essere piccolo e specialistico. Un foundation model è definito soprattutto dal ruolo di base adattabile, non dalla sola capacità di generare.
- **Modello e prodotto.** Retrieval, strumenti, dati aggiornati, autorizzazioni e interfacce appartengono al sistema costruito attorno al modello.
- **Training e inference.** Nel caso base, il training modifica i parametri; l'inference li usa. Tecniche di adattamento al test time cambiano questo contratto e verranno dichiarate esplicitamente quando compariranno.

## Riepilogo

Siamo partiti da una sola richiesta e abbiamo visto che lo stesso output può essere ottenuto con meccanismi differenti. Una regola esplicita, un modello appreso e una rete profonda non sono tre nomi per la stessa cosa; descrivono modi diversi di costruire il comportamento. Allo stesso modo, `discriminativo`, `generativo` e `foundation model` rispondono a domande diverse.

Per descrivere un sistema in modo utile conviene quindi chiedere: come viene prodotto il comportamento, che cosa viene modellato e quanto è ampio il perimetro di riuso? A queste domande va aggiunta la distinzione tra modello e sistema, perché dati esterni, strumenti, regole e autorizzazioni possono cambiare profondamente il comportamento osservato senza modificare il checkpoint.

### Verifica della comprensione

1. Spiega la relazione tra AI, machine learning, representation learning e deep learning senza usare i termini come sinonimi.
2. Individua nello snippet l'istruzione che modifica i parametri e il blocco che esegue soltanto l'inference.
3. Spiega perché un modello generativo non è necessariamente un foundation model.
4. Descrivi un filtro antispam lungo le tre dimensioni: meccanismo, obiettivo e ampiezza.
5. Supponi di aggiungere al sistema di assistenza uno strumento che legge lo stato reale della spedizione. Quale parte del modello può restare invariata e quale parte del sistema è cambiata?

### Esercizi

1. Descrivi un sistema di raccomandazione separando input, modello, output e componenti circostanti.
2. Scrivi una regola esplicita per riconoscere un problema di consegna e trova due formulazioni che la regola non intercetta.
3. Rimuovi il ciclo di training da `SNIP-AI-001` e verifica che i parametri rimangano invariati.
4. Aggiungi una seconda inference con un input diverso e controlla la shape dell'output.
5. Trova un esempio di modello generativo specialistico che non richieda la nozione di foundation model.
6. Elenca tre componenti di un sistema di generative AI che non appartengono al checkpoint.

## Fonti e materiali verificabili

Le fonti portanti sono la definizione aggiornata di sistema di AI dell'OCSE, il NIST AI RMF 1.0, il profilo NIST sulla generative AI, *Deep Learning* di Goodfellow, Bengio e Courville, il confronto di Ng e Jordan tra classificatori discriminativi e generativi, il paper originale sui GAN e il report sui foundation model.

Le schede complete e i limiti d'uso sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md). Il codice eseguito, i test, gli output e l'ambiente sono raccolti nella cartella [`code/`](code/).
