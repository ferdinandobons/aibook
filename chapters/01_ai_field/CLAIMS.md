# Registro delle affermazioni. Capitolo 1

Data di verifica: **30 luglio 2026**.

| ID | Affermazione portante | Tipo | Fonte o prova | Esito |
|---|---|---|---|---|
| `CLM-AI-001` | Nella definizione OECD aggiornata, un AI system è un sistema machine-based che, per obiettivi espliciti o impliciti, inferisce dagli input come produrre output quali predizioni, contenuti, raccomandazioni o decisioni. | fonte istituzionale | `SRC-AI-001` | verificata |
| `CLM-AI-002` | Per questo libro, `modello` indica il componente matematico parametrizzato, mentre `sistema` include anche input, pre-processing, regole, tool, interfacce e post-processing. | convenzione editoriale + confine | `SRC-AI-002`; decisione dichiarata nel capitolo | verificata |
| `CLM-AI-003` | L'AI comprende anche approcci che non apprendono i propri parametri dai dati; quindi AI e machine learning non sono sinonimi. | fonte autorevole | `SRC-AI-003`; esempi di knowledge base e approcci AI non-ML | verificata |
| `CLM-AI-004` | Il machine learning è un approccio all'AI in cui il comportamento viene migliorato attraverso esperienza o dati, anziché essere descritto interamente tramite regole operative esplicite. | fonte autorevole | `SRC-AI-003` | verificata |
| `CLM-AI-005` | Il deep learning è un tipo di machine learning che costruisce una rappresentazione o funzione tramite composizioni di più livelli; non esiste una soglia di profondità universalmente accettata. | fonte autorevole | `SRC-AI-003` | verificata |
| `CLM-AI-006` | Le etichette `simbolico`, `statistico` e `neurale` sono usate nel capitolo come tassonomia di lavoro non esaustiva e non come insiemi sempre disgiunti. | convenzione editoriale | dichiarazione esplicita nel capitolo | verificata |
| `CLM-AI-007` | Nel ciclo di training PyTorch mostrato, la loss viene calcolata dagli output e dai target, `backward()` produce gradienti e `optimizer.step()` aggiorna i parametri. | documentazione ufficiale + esecuzione | `SRC-AI-008`, `SRC-AI-009`, `SNIP-AI-001` | verificata |
| `CLM-AI-008` | `Module.eval()` e `torch.inference_mode()` hanno ruoli distinti: il primo imposta la modalità di evaluation dei moduli interessati, il secondo disabilita il tracciamento autograd previsto per l'inference. | documentazione ufficiale | `SRC-AI-010` | verificata |
| `CLM-AI-009` | Nel risultato eseguito del capitolo, almeno un parametro cambia durante il training e nessun parametro cambia durante l'inference. | risultato eseguito | `SNIP-AI-001`; test `test_ai_snippets.py` | verificata |
| `CLM-AI-010` | Nel risultato eseguito, la loss scende da `0.641941` a `0.045580`; l'output di inference ha shape `[1,2]` e la classe prevista è `0`. | risultato eseguito | `SNIP-AI-001`; output registrato | verificata |
| `CLM-AI-011` | Un classificatore discriminativo e un modello generativo differiscono per la relazione probabilistica o l'obiettivo modellato; la distinzione non implica che uno dei due paradigmi sia sempre migliore. | fonte primaria + confine | `SRC-AI-004` | verificata |
| `CLM-AI-012` | Nel framework GAN, il generatore è addestrato per catturare la distribuzione dei dati e produrre campioni, mentre il discriminatore stima la provenienza dei campioni. | fonte primaria | `SRC-AI-005` | verificata |
| `CLM-AI-013` | Nel profilo NIST, generative AI indica modelli che emulano struttura e caratteristiche dei dati di input per produrre contenuto sintetico derivato, inclusi testo, immagini, video e audio. | fonte istituzionale | `SRC-AI-006`, introduzione | verificata |
| `CLM-AI-014` | Non tutta la generative AI deriva da foundation model. | fonte istituzionale | `SRC-AI-006`, nota introduttiva | verificata |
| `CLM-AI-015` | Il report Stanford CRFM introduce `foundation model` per modelli addestrati su dati ampi, generalmente con self-supervision su larga scala, adattabili a numerosi compiti downstream. | fonte primaria istituzionale | `SRC-AI-007`, abstract e introduzione | verificata |
| `CLM-AI-016` | Un foundation model non coincide con il sistema applicativo completo: adattamento, retrieval, tool, interfaccia e vincoli possono cambiare lasciando invariato il modello di base. | derivazione architetturale + confine | `SRC-AI-002`, `SRC-AI-007`; convenzione modello/sistema | verificata |
| `CLM-AI-017` | `Generalista` e `specialistico` sono usati come descrizioni relative dell'ampiezza dei compiti e del contesto d'uso, non come categorie universali con una soglia numerica fissa. | convenzione editoriale | dichiarazione esplicita nel capitolo | verificata |
| `CLM-AI-018` | La stessa applicazione può combinare regole, modelli statistici e reti neurali; il meccanismo, l'obiettivo e l'ampiezza sono assi distinti. | derivazione tassonomica | esempi e convenzioni dichiarate; visuale `AI-01` da validare | verificata per il testo; visuale aperta |

## Regole d'uso

- Le convenzioni editoriali sono presentate come convenzioni, non come definizioni universali.
- Le affermazioni temporali sulle versioni PyTorch vengono ricontrollate prima del congelamento.
- `AI-01` e `AI-02` non possono essere marcate finali finché non superano audit tecnico e approvazione autoriale.
