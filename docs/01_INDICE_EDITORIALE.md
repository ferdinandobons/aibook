# Indice editoriale dell'opera

## Stato

- Opera canonica: unica e continua
- Export: volume unico, più tomi, sito o corso
- Capitoli pianificati: 98
- Appendici pianificate: 12
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Numerazione: edizione di lavoro
- Governance: `00_GOVERNANCE_E_ARCHITETTURA.md`
- Catalogo dettagliato: `14_CATALOGO_STATO_ARTE.md`

## Principio

Le parti sono stabili e organizzate per funzione. Ogni capitolo possiede un `chapter_id` stabile; il numero visualizzato può cambiare tra edizioni.

Il catalogo contiene tecniche, maturità e destinazioni editoriali. L'indice contiene soltanto la struttura del libro, per evitare duplicazioni.

# P01. Campo, metodo e storia dell'AI

| N. | chapter_id | Titolo |
|---:|---|---|
| 1 | `CH-P01-AI-FIELD` | Che cos'è l'intelligenza artificiale |
| 2 | `CH-P01-HISTORY` | Dai simboli ai foundation model |
| 3 | `CH-P01-LIFECYCLE` | Il ciclo di vita di un sistema di AI |
| 4 | `CH-P01-CRITICAL-EVALUATION` | Come valutare criticamente un risultato di AI |

`CH-P01-LEARNING-OVERVIEW` era un ID di pianificazione non congelato. È stato ritirato prima della produzione canonica perché l'overview dell'apprendimento è distribuita nei capitoli P03 e P04, mentre P01 richiedeva un capitolo metodologico sul ciclo di vita. Non esiste una versione approvata da migrare.

# P02. Matematica, informazione e calcolo

| N. | chapter_id | Titolo |
|---:|---|---|
| 5 | `CH-P02-LINEAR-ALGEBRA` | Algebra lineare, vettori e tensori |
| 6 | `CH-P02-CALCULUS-BACKPROP` | Calcolo differenziale e backpropagation |
| 7 | `CH-P02-PROBABILITY` | Probabilità, statistica e inferenza |
| 8 | `CH-P02-INFORMATION-THEORY` | Teoria dell'informazione e funzioni obiettivo |
| 9 | `CH-P02-NUMERICS-HARDWARE` | Calcolo numerico, precisione e hardware |

# P03. Apprendimento, ottimizzazione e decisione

| N. | chapter_id | Titolo |
|---:|---|---|
| 10 | `CH-P03-SEARCH-PLANNING` | Ricerca, pianificazione e giochi |
| 11 | `CH-P03-KNOWLEDGE-LOGIC` | Conoscenza, logica e modelli probabilistici |
| 12 | `CH-P03-SUPERVISED` | Apprendimento supervisionato |
| 13 | `CH-P03-UNSUPERVISED-SELF` | Apprendimento non supervisionato e auto-supervisionato |
| 14 | `CH-P03-RL` | Reinforcement learning |

# P04. Reti neurali e rappresentazioni

| N. | chapter_id | Titolo |
|---:|---|---|
| 15 | `CH-P04-MLP` | Dal percettrone alle reti multilayer |
| 16 | `CH-P04-DEEP-TRAINING` | Addestrare reti profonde |
| 17 | `CH-P04-CNN-GEOMETRIC` | Convolutional network e apprendimento geometrico |
| 18 | `CH-P04-RECURRENT` | Reti ricorrenti e modelli sequenziali |
| 19 | `CH-P04-REPRESENTATION` | Representation learning |

# P05. Modellazione generativa

| N. | chapter_id | Titolo |
|---:|---|---|
| 20 | `CH-P05-GENERATIVE-FOUNDATIONS` | Fondamenti della modellazione generativa |
| 21 | `CH-P05-AUTOREGRESSIVE` | Modelli autoregressivi |
| 22 | `CH-P05-VAE-VQ` | Variational Autoencoder e latent discreti |
| 23 | `CH-P05-GAN` | Generative Adversarial Network |
| 24 | `CH-P05-FLOWS` | Normalizing flow e trasformazioni invertibili |
| 25 | `CH-P05-DIFFUSION-FLOW` | Diffusione, score matching e flow matching |

# P06. Sequenze, linguaggio e contesto

| N. | chapter_id | Titolo |
|---:|---|---|
| 26 | `CH-P06-TEXT-DATA` | Il testo come dato |
| 27 | `CH-P06-EMBEDDINGS` | Embedding e spazio semantico |
| 28 | `CH-P06-ATTENTION` | Il meccanismo di attention |
| 29 | `CH-P06-TRANSFORMER` | Il Transformer da zero |
| 30 | `CH-P06-PRETRAIN-FAMILIES` | Famiglie architetturali e obiettivi di pretraining |
| 31 | `CH-P06-LLM-BEHAVIOR` | Dalla rappresentazione linguistica agli LLM |

# P07. Dati, pretraining e scaling

| N. | chapter_id | Titolo |
|---:|---|---|
| 32 | `CH-P07-DATA-LIFECYCLE` | Il ciclo di vita dei dati |
| 33 | `CH-P07-DATA-MIXTURE` | Dataset mixture, curriculum e dati sintetici |
| 34 | `CH-P07-SCALING` | Scaling law e progettazione del modello |
| 35 | `CH-P07-PRETRAIN-RECIPE` | La ricetta di pretraining |
| 36 | `CH-P07-DISTRIBUTED-TRAINING` | Training distribuito e continued pretraining |

# P08. Progettazione delle architetture

| N. | chapter_id | Titolo |
|---:|---|---|
| 37 | `CH-P08-MODERN-BLOCK` | Anatomia del blocco moderno |
| 38 | `CH-P08-POSITION-CONTEXT` | Posizione e contesto lungo |
| 39 | `CH-P08-ATTENTION-KV` | Varianti dell'attention e gestione KV |
| 40 | `CH-P08-HARDWARE-AWARE-ATTENTION` | Attention hardware-aware |
| 41 | `CH-P08-LINEAR-ATTENTION` | Linear attention, fast weights e delta rule |
| 42 | `CH-P08-SEQUENCE-ALTERNATIVES` | State-space model, recurrence e long convolution |
| 43 | `CH-P08-HYBRID-MEMORY` | Architetture ibride e memoria interna |
| 44 | `CH-P08-MOE-CONDITIONAL` | Mixture of Experts e calcolo condizionale |
| 45 | `CH-P08-ALTERNATIVE-PREDICTION` | Byte, predizione multi-token e language diffusion |

# P09. Adattamento, allineamento e ragionamento

| N. | chapter_id | Titolo |
|---:|---|---|
| 46 | `CH-P09-SFT` | Supervised fine-tuning e instruction tuning |
| 47 | `CH-P09-PEFT` | Fine-tuning efficiente |
| 48 | `CH-P09-RLHF` | Preferenze, reward model e RLHF |
| 49 | `CH-P09-PREFERENCE-OPT` | Ottimizzazione diretta delle preferenze |
| 50 | `CH-P09-SUPERVISION-VERIFIERS` | Process supervision, outcome supervision e verifier |
| 51 | `CH-P09-RLVR` | Reinforcement learning con reward verificabili |
| 52 | `CH-P09-REASONING-TRAINING` | Addestrare e distillare il reasoning |
| 53 | `CH-P09-TEST-TIME-COMPUTE` | Test-time compute, ricerca e controllo del budget |
| 54 | `CH-P09-MODEL-UPDATE` | Aggiornamento, merging ed editing del modello |

# P10. Multimodalità e modelli del mondo

| N. | chapter_id | Titolo |
|---:|---|---|
| 55 | `CH-P10-MULTIMODAL-FOUNDATIONS` | Fondamenti della multimodalità |
| 56 | `CH-P10-VLM` | Vision encoder e Vision-Language Model |
| 57 | `CH-P10-IMAGE-GENERATION` | Generazione e modifica delle immagini |
| 58 | `CH-P10-NATIVE-MULTIMODAL` | Modelli multimodali nativi e any-to-any |
| 59 | `CH-P10-AUDIO` | Audio, parlato e musica |
| 60 | `CH-P10-VIDEO` | Generazione video |
| 61 | `CH-P10-SPATIAL-3D` | 3D, spazio e rappresentazione delle scene |
| 62 | `CH-P10-WORLD-EMBODIED` | World model, embodied AI e vision-language-action |

# P11. Conoscenza esterna, memoria e azione

| N. | chapter_id | Titolo |
|---:|---|---|
| 63 | `CH-P11-RETRIEVAL` | Information retrieval |
| 64 | `CH-P11-RAG` | Retrieval-Augmented Generation |
| 65 | `CH-P11-ADVANCED-RAG` | RAG adattivo, correttivo e basato su grafi |
| 66 | `CH-P11-CONTEXT-RETRIEVAL-MEMORY` | Contesto lungo, retrieval e memoria |
| 67 | `CH-P11-TOOLS` | Output strutturato e uso degli strumenti |
| 68 | `CH-P11-INTEROPERABILITY` | Protocolli e interoperabilità |
| 69 | `CH-P11-AGENT-LOOP` | Ciclo agentico, pianificazione e verifica |
| 70 | `CH-P11-AGENT-SYSTEMS` | Multi-agent, browser, computer e code agents |
| 71 | `CH-P11-AGENT-TRAINING-EVAL` | Training e valutazione degli agenti |
| 72 | `CH-P11-AGENT-SAFETY` | Sicurezza operativa degli agenti |

# P12. Efficienza, inference e sistemi

| N. | chapter_id | Titolo |
|---:|---|---|
| 73 | `CH-P12-DISTILLATION-PRUNING` | Distillazione e pruning |
| 74 | `CH-P12-QUANTIZATION` | Quantizzazione |
| 75 | `CH-P12-LOW-BIT-NATIVE` | Modelli low-bit nativi e co-design numerico |
| 76 | `CH-P12-DECODING` | Decoding e generazione vincolata |
| 77 | `CH-P12-SPECULATIVE-DECODING` | Speculative e parallel decoding |
| 78 | `CH-P12-KV-CACHE` | KV cache e riuso del contesto |
| 79 | `CH-P12-SERVING` | Serving, batching e scheduling |
| 80 | `CH-P12-DISTRIBUTED-INFERENCE` | Serving disaggregato e inference distribuita |
| 81 | `CH-P12-COMPILERS-KERNELS` | Compiler, kernel e runtime |
| 82 | `CH-P12-LLMOPS` | LLMOps, edge, costo ed energia |

# P13. Valutazione, interpretabilità, sicurezza e governance

| N. | chapter_id | Titolo |
|---:|---|---|
| 83 | `CH-P13-EVAL-DESIGN` | Progettare una valutazione |
| 84 | `CH-P13-FACTUALITY` | Fattualità, incertezza e affidabilità |
| 85 | `CH-P13-SYSTEM-EVAL` | Valutare contesto lungo, RAG, multimodalità e agenti |
| 86 | `CH-P13-INTERPRETABILITY` | Interpretabilità delle rappresentazioni e dei circuiti |
| 87 | `CH-P13-SAE-CIRCUIT-TRACING` | Sparse autoencoder e interpretabilità scalabile |
| 88 | `CH-P13-ROBUSTNESS-JAILBREAK` | Robustezza, jailbreak e attacchi adversarial |
| 89 | `CH-P13-PROMPT-INJECTION` | Prompt injection e sicurezza dei tool |
| 90 | `CH-P13-SUPPLY-CHAIN-SECURITY` | Poisoning, backdoor, extraction e supply chain |
| 91 | `CH-P13-PRIVACY-FAIRNESS` | Privacy, fairness e unlearning |
| 92 | `CH-P13-PROVENANCE` | Watermarking e provenienza dei contenuti |
| 93 | `CH-P13-GOVERNANCE` | Diritto, governance e sostenibilità |

# P14. Laboratori, integrazione e osservatorio

| N. | chapter_id | Titolo |
|---:|---|---|
| 94 | `CH-P14-FOUNDATIONS-LAB` | Percorso pratico dai fondamenti |
| 95 | `CH-P14-SMALL-LM` | Costruire un piccolo language model |
| 96 | `CH-P14-PRODUCTION-PROJECT` | Progetto di produzione completo |
| 97 | `CH-P14-REPLICATION` | Riprodurre e leggere un paper |
| 98 | `CH-P14-FRONTIER-OBSERVATORY` | Osservatorio della frontiera |

# Appendici

- **A.** Python, NumPy e PyTorch essenziali.
- **B.** JAX, compilazione e trasformazioni funzionali.
- **C.** Formulario matematico.
- **D.** Complessità delle architetture.
- **E.** Glossario italiano-inglese.
- **F.** Dataset, benchmark e metriche.
- **G.** Schede di modelli e technical report.
- **H.** Checklist per riproducibilità, sicurezza e deployment.
- **I.** Soluzioni degli esercizi.
- **J.** Cronologia dei paper fondamentali.
- **K.** Guida alla lettura critica delle fonti.
- **L.** Registro delle edizioni, degli alias e delle migrazioni.

# Regole di aggiornamento

1. Le parti `P01`-`P14` non cambiano per una nuova tecnica.
2. Una nuova voce entra prima nel catalogo.
3. La collocazione usa il routing funzionale.
4. La maturità non determina la parte.
5. Un nuovo capitolo richiede domanda autonoma, fonti e contratto didattico.
6. `chapter_id` resta stabile; il numero cambia tra edizioni.
7. Una voce `FRONTIER` resta nella parte funzionale.
8. `P14` osserva la frontiera, non la usa come contenitore generico.
9. Split e merge richiedono alias, redirect e mappa di migrazione.
10. Ogni modifica strutturale aggiorna governance, catalogo, indice e audit.
