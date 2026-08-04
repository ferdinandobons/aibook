# Fonti primarie e documentazione. Capitolo 1

Data dell'ultima verifica: **30 luglio 2026**.

## SRC-AI-001. OECD, definizione aggiornata di AI system

- Organizzazione: Organisation for Economic Co-operation and Development.
- Titolo: *Explanatory memorandum on the updated OECD definition of an AI system*.
- Data: 5 marzo 2024.
- URL: https://oecd.ai/en/ai-publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system
- Versione della definizione: approvata dagli Stati membri OECD nel novembre 2023.
- Sezioni usate: definizione e chiarimenti relativi a input, inferenza, output, obiettivi ed effetto sugli ambienti fisici o virtuali.
- Sostiene: descrizione di un AI system come sistema machine-based che, a partire dagli input, inferisce come produrre predizioni, contenuti, raccomandazioni o decisioni.
- Limite: è una definizione destinata alla raccomandazione OECD e non impone una tassonomia unica di tutte le tecniche AI.

## SRC-AI-002. NIST AI RMF 1.0

- Organizzazione: National Institute of Standards and Technology.
- Autrice: Elham Tabassi.
- Titolo: *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*.
- Identificatore: NIST AI 100-1.
- Data: 26 gennaio 2023.
- PDF ufficiale: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- Pagina ufficiale: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- Sezioni usate: AI lifecycle, AI actors, distinzione tra prodotti, servizi, sistemi e contesti d'uso.
- Sostiene: il sistema AI viene progettato, sviluppato, distribuito, usato e valutato lungo un ciclo di vita; la valutazione non riguarda soltanto un modello isolato.
- Limite temporale: NIST dichiara che AI RMF 1.0 è in revisione. Il capitolo usa la versione 1.0 pubblicata, non anticipa il contenuto della revisione.

## SRC-AI-003. Goodfellow, Bengio e Courville, Deep Learning

- Autori: Ian Goodfellow, Yoshua Bengio, Aaron Courville.
- Titolo: *Deep Learning*.
- Editore: MIT Press, 2016.
- Versione ufficiale online: https://www.deeplearningbook.org/contents/intro.html
- Sezione usata: Capitolo 1, Introduction.
- Sostiene:
  - machine learning come approccio all'AI basato su esperienza e dati;
  - deep learning come tipo di machine learning fondato sulla composizione di rappresentazioni o funzioni apprese;
  - inclusione di approcci AI non basati su machine learning, esemplificati dalle knowledge base;
  - assenza di una soglia universalmente condivisa che stabilisca quanta profondità renda un modello `deep`.
- Limite: è un manuale autorevole, non uno standard normativo; alcune formulazioni riflettono il quadro del 2016.

## SRC-AI-004. Ng e Jordan, discriminative e generative classifiers

- Autori: Andrew Y. Ng, Michael I. Jordan.
- Titolo: *On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes*.
- Sede: Advances in Neural Information Processing Systems 14, 2001.
- Pagina ufficiale: https://papers.nips.cc/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html
- Sezioni usate: impostazione del confronto tra logistic regression e naive Bayes.
- Sostiene: distinzione tra apprendimento discriminativo, che tratta direttamente la relazione predittiva, e apprendimento generativo, che modella distribuzioni capaci di descrivere il processo dei dati.
- Limite: l'analisi teorica riguarda una coppia specifica di classificatori e non stabilisce che un paradigma sia sempre superiore all'altro.

## SRC-AI-005. Generative Adversarial Nets

- Autori: Ian Goodfellow et al.
- Titolo: *Generative Adversarial Nets*.
- Sede: Advances in Neural Information Processing Systems 27, 2014.
- Pagina ufficiale: https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html
- Sezione usata: abstract e definizione del generative model `G` e del discriminative model `D`.
- Sostiene: un modello generativo può essere addestrato per catturare la distribuzione dei dati e produrre campioni; generativo e discriminativo descrivono ruoli o obiettivi, non necessariamente due famiglie di architetture incompatibili.
- Limite: il paper introduce il framework GAN e non definisce tutta l'AI generativa contemporanea.

## SRC-AI-006. NIST AI 600-1, Generative AI Profile

- Organizzazione: National Institute of Standards and Technology.
- Autori: Chloe Autio et al.
- Titolo: *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*.
- Identificatore: NIST AI 600-1.
- Data: luglio 2024; pagina ufficiale aggiornata l'8 aprile 2026.
- PDF ufficiale: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Sezione usata: Introduzione, nota 1, pagina 1 del corpo.
- Sostiene:
  - generative AI come classe di modelli che emula struttura e caratteristiche dei dati di input per produrre contenuto sintetico derivato;
  - contenuti possibili: testo, immagini, video, audio e altri contenuti digitali;
  - non tutta la generative AI deriva da foundation model;
  - nel profilo NIST, il focus operativo è principalmente sui generative foundation model.
- Limite: il documento è un profilo di risk management e adotta definizioni funzionali al proprio ambito.

## SRC-AI-007. Stanford CRFM, foundation models

- Autori: Rishi Bommasani et al.
- Titolo: *On the Opportunities and Risks of Foundation Models*.
- Organizzazione: Stanford Center for Research on Foundation Models.
- Data: 2021.
- Pagina ufficiale: https://crfm.stanford.edu/report.html
- Sezione usata: Abstract e Introduction.
- Sostiene: foundation model come modello addestrato su dati ampi, generalmente con self-supervision su larga scala, adattabile a un'ampia gamma di compiti downstream.
- Limite: il termine è stato proposto dal report; le soglie di scala e le modalità di adattamento non costituiscono una definizione universale e immutabile.

## SRC-AI-008. PyTorch, ottimizzazione dei parametri

- Organizzazione: PyTorch Foundation.
- Titolo: *Optimizing Model Parameters*.
- Documentazione: PyTorch Tutorials 2.13.
- URL: https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html
- Ultimo aggiornamento indicato dalla pagina alla verifica: 7 maggio 2026.
- Sostiene: il training iterativo calcola output, loss, gradienti e aggiorna i parametri tramite un optimizer.
- Limite: è un tutorial introduttivo riferito a PyTorch; il concetto generale di training non dipende dalla libreria.

## SRC-AI-009. PyTorch, torch.optim

- Organizzazione: PyTorch Foundation.
- Titolo: `torch.optim`.
- Documentazione: PyTorch stable 2.13.
- URL: https://docs.pytorch.org/docs/stable/optim.html
- Sostiene: un optimizer riceve i parametri da ottimizzare e `optimizer.step()` li aggiorna dopo il calcolo dei gradienti.

## SRC-AI-010. PyTorch, modalità train, eval e inference

- Organizzazione: PyTorch Foundation.
- Documentazione:
  - `torch.nn.Module`: https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html
  - `torch.inference_mode`: https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html
- Versione verificata: stable 2.13.
- Sostiene:
  - `Module.train()` e `Module.eval()` modificano il comportamento dei moduli che distinguono training ed evaluation, per esempio Dropout e BatchNorm;
  - `torch.inference_mode()` disabilita il tracciamento necessario ad autograd durante inference;
  - `eval()` e disabilitazione dei gradienti sono operazioni distinte.
- Limite: il capitolo usa un layer lineare che non cambia comportamento tra `train()` ed `eval()`, ma adotta entrambe le chiamate per mostrare il contratto corretto.

## Divergenze e decisioni editoriali

1. Il termine `AI` non possiede una singola definizione tecnica universale. Il capitolo usa la definizione di AI system dell'OECD come ancora operativa e dichiara il proprio lessico locale per `modello` e `sistema`.
2. Simbolico, statistico e neurale sono una tassonomia di lavoro non esaustiva. Non vengono presentati come insiemi disgiunti.
3. `Generalista` e `specialistico` sono descrizioni relative dell'ampiezza dei compiti e del contesto di impiego.
4. `Generative AI`, `generative model` e `foundation model` restano termini distinti.
5. La versione PyTorch eseguita localmente è `2.10.0+cpu`; la documentazione API ricontrollata è stable `2.13`. Il capitolo non dichiara un'esecuzione locale sotto `2.13`.
