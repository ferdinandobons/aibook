# Indice editoriale dell'opera

## Stato

- Opera canonica: unica e continua
- Export: volume unico, più tomi, sito o corso
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Numerazione visualizzata: edizione di lavoro
- Architettura e governance: `00_GOVERNANCE_E_ARCHITETTURA.md`
- Catalogo delle tecniche: `02_CATALOGO_E_RICERCA.md`

## Principio organizzativo

Le parti sono stabili e organizzate per funzione. I capitoli seguono problemi, meccanismi e contratti tecnici. Ogni capitolo ha un `chapter_id` stabile; il numero visualizzato può cambiare tra edizioni.

Una tecnica censita nel catalogo può diventare capitolo, sezione, approfondimento, confronto, studio di caso oppure voce dell'osservatorio. Non ogni paper o prodotto riceve un capitolo autonomo.

# P01. Campo, metodo e storia dell'AI

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 1 | `CH-P01-AI-FIELD` | Che cos'è l'intelligenza artificiale | AI, ML, deep learning, AI generativa, sistemi simbolici/statistici/neurali, discriminativo/generativo, foundation model, training e inference. |
| 2 | `CH-P01-HISTORY` | Storia delle idee e dei sistemi di AI | Logica, ricerca, sistemi esperti, probabilità, connessionismo, deep learning, foundation model e multimodalità. |
| 3 | `CH-P01-LEARNING-OVERVIEW` | Come apprende una macchina | Parametri, iperparametri, obiettivi, dati, supervisionato, non supervisionato, auto-supervisionato e RL. |
| 4 | `CH-P01-CRITICAL-EVALUATION` | Come valutare criticamente un risultato di AI | Split, baseline, metriche, ablation, significatività, causalità, riproducibilità e contaminazione. |

# P02. Matematica, informazione e calcolo

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 5 | `CH-P02-LINEAR-ALGEBRA` | Algebra lineare, vettori e tensori | Scalari, vettori, matrici, tensori, prodotti, norme, proiezioni, autovalori, SVD, shape e broadcasting. |
| 6 | `CH-P02-CALCULUS-BACKPROP` | Calcolo differenziale e backpropagation | Derivate, gradienti, Jacobiane, Hessiane, regola della catena, grafi computazionali e autodiff. |
| 7 | `CH-P02-PROBABILITY` | Probabilità, statistica e inferenza | Variabili casuali, distribuzioni, Bayes, valore atteso, varianza, MLE, MAP, sampling e test. |
| 8 | `CH-P02-INFORMATION-THEORY` | Teoria dell'informazione e funzioni obiettivo | Entropia, cross-entropy, perplexity, KL, informazione mutua, likelihood, ELBO e obiettivi contrastivi. |
| 9 | `CH-P02-NUMERICS-HARDWARE` | Calcolo numerico, precisione e hardware | Condizionamento, stabilità, FP32/FP16/BF16/FP8, acceleratori, memoria, banda, FLOP e roofline. |

# P03. Apprendimento, ottimizzazione e decisione

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 10 | `CH-P03-SEARCH-PLANNING` | Ricerca, pianificazione e giochi | Ricerca non informata, A*, CSP, minimax, alpha-beta, MCTS e pianificazione classica. |
| 11 | `CH-P03-KNOWLEDGE-LOGIC` | Conoscenza, logica e modelli probabilistici | Logica proposizionale e del primo ordine, regole, ontologie, knowledge graph, reti bayesiane e Markov. |
| 12 | `CH-P03-SUPERVISED` | Apprendimento supervisionato | Regressione, classificazione, calibrazione, alberi, ensemble, SVM e class imbalance. |
| 13 | `CH-P03-UNSUPERVISED-SELF` | Apprendimento non supervisionato e auto-supervisionato | Clustering, mixture model, PCA, anomaly detection, metric learning e obiettivi auto-supervisionati. |
| 14 | `CH-P03-RL` | Reinforcement learning | MDP, Bellman, value learning, Q-learning, policy gradient, actor-critic, PPO e reward design. |

# P04. Reti neurali e rappresentazioni

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 15 | `CH-P04-MLP` | Dal percettrone alle reti multilayer | Percettrone, MLP, attivazioni, capacità espressiva, forward pass e implementazione minimale. |
| 16 | `CH-P04-DEEP-TRAINING` | Addestrare reti profonde | Inizializzazione, vanishing/exploding gradient, normalizzazione, residual, regolarizzazione e overfitting. |
| 17 | `CH-P04-CNN-GEOMETRIC` | Convolutional network e apprendimento geometrico | Convoluzione, pooling, receptive field, equivarianza, bias induttivi e GNN. |
| 18 | `CH-P04-RECURRENT` | Reti ricorrenti e modelli sequenziali | RNN, BPTT, LSTM, GRU, encoder-decoder, teacher forcing e limiti della ricorrenza classica. |
| 19 | `CH-P04-REPRESENTATION` | Representation learning | Autoencoder, denoising, sparse autoencoder, contrastive learning, metric learning, transfer e probing. |

# P05. Modellazione generativa

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 20 | `CH-P05-GENERATIVE-FOUNDATIONS` | Fondamenti della modellazione generativa | Distribuzioni dei dati, modelli espliciti/impliciti, variabili latenti, likelihood, sampling, qualità e copertura. |
| 21 | `CH-P05-AUTOREGRESSIVE` | Modelli autoregressivi | Fattorizzazione, teacher forcing, exposure bias e autoregressione per più modalità. |
| 22 | `CH-P05-VAE-VQ` | Variational Autoencoder e latent discreti | ELBO, reparameterization trick, posterior collapse, VAE gerarchici e VQ-VAE. |
| 23 | `CH-P05-GAN` | Generative Adversarial Network | Minimax, non-saturating loss, Wasserstein objective, gradient penalty, mode collapse e condizionamento. |
| 24 | `CH-P05-FLOWS` | Normalizing flow e trasformazioni invertibili | Change of variables, Jacobiano, coupling layer, autoregressive flow, continuous flow ed exact likelihood. |
| 25 | `CH-P05-DIFFUSION-FLOW` | Diffusione, score matching e flow matching | Processi forward/reverse, score-based modeling, SDE, latent diffusion, guidance, flow matching e consistency. |

# P06. Sequenze, linguaggio e contesto

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 26 | `CH-P06-TEXT-DATA` | Il testo come dato | Unicode, normalizzazione, segmentazione, parole, caratteri, byte, token, BPE, WordPiece, Unigram e token-free. |
| 27 | `CH-P06-EMBEDDINGS` | Embedding e spazio semantico | One-hot, word embedding, Word2Vec, rappresentazioni contestuali, sentence embedding e similarità. |
| 28 | `CH-P06-ATTENTION` | Il meccanismo di attention | Query, key, value, score, scaling, mask, softmax, self/cross/causal attention, shape, complessità e PyTorch. |
| 29 | `CH-P06-TRANSFORMER` | Il Transformer da zero | Multi-head attention, feed-forward, residual stream, normalizzazione, posizione, encoder, decoder e implementazione. |
| 30 | `CH-P06-PRETRAIN-FAMILIES` | Famiglie architetturali e obiettivi di pretraining | Encoder-only, decoder-only, encoder-decoder, causal, masked, span corruption e denoising. |
| 31 | `CH-P06-LLM-BEHAVIOR` | Dalla rappresentazione linguistica agli LLM | Few-shot, in-context learning, prompt, istruzioni, decoding di base e generazione vincolata introduttiva. |

# P07. Dati, pretraining e scaling

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 32 | `CH-P07-DATA-LIFECYCLE` | Il ciclo di vita dei dati | Acquisizione, licenze, filtraggio, deduplicazione, qualità, PII, contaminazione e provenance. |
| 33 | `CH-P07-DATA-MIXTURE` | Dataset mixture, curriculum e dati sintetici | Bilanciamento di lingue e domini, curriculum, scheduling, generazione, filtraggio e verifica. |
| 34 | `CH-P07-SCALING` | Scaling law e progettazione del modello | Parametri, token, dati, compute-optimal training, profondità, larghezza, contesto e parameterization. |
| 35 | `CH-P07-PRETRAIN-RECIPE` | La ricetta di pretraining | Batch, optimizer, warm-up, schedule, precisione mista, loss spike, checkpoint e recovery. |
| 36 | `CH-P07-DISTRIBUTED-TRAINING` | Training distribuito e continued pretraining | Parallelismi, ZeRO, FSDP, activation checkpointing, offload, continued pretraining e domain adaptation. |

# P08. Progettazione delle architetture

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 37 | `CH-P08-MODERN-BLOCK` | Anatomia del blocco moderno | Pre/post-norm, RMSNorm, GLU/GEGLU/SwiGLU, residual scaling, weight tying e stabilità. |
| 38 | `CH-P08-POSITION-CONTEXT` | Posizione e contesto lungo | Posizione assoluta/relativa, RoPE, ALiBi, interpolation, YaRN, LongRoPE e valutazione del contesto. |
| 39 | `CH-P08-ATTENTION-KV` | Varianti dell'attention e gestione KV | MHA, MQA, GQA, latent attention, compressione/quantizzazione/eviction KV, local e sparse attention. |
| 40 | `CH-P08-HARDWARE-AWARE-ATTENTION` | Attention hardware-aware | Tiling, data movement, FlashAttention, IO-aware exact attention, kernel fusion e co-design. |
| 41 | `CH-P08-LINEAR-ATTENTION` | Linear attention, fast weights e delta rule | Kernel feature map, forma ricorrente, fast-weight memory, delta rule e gating. |
| 42 | `CH-P08-SEQUENCE-ALTERNATIVES` | State-space model, recurrence e long convolution | S4, selective SSM, state-space duality, Mamba, RetNet, RWKV, Hyena, xLSTM e Griffin. |
| 43 | `CH-P08-HYBRID-MEMORY` | Architetture ibride e memoria interna | Ibridi attention/SSM/convolution/recurrence, neural memory, memory layers e test-time learning interno. |
| 44 | `CH-P08-MOE-CONDITIONAL` | Mixture of Experts e calcolo condizionale | Expert, router, gating, load balancing, shared expert, expert parallelism, upcycling e Mixture-of-Depths. |
| 45 | `CH-P08-ALTERNATIVE-PREDICTION` | Byte, predizione multi-token e language diffusion | Byte-level, patch multiscala, multi-token prediction, draft head, diffusion language model e ibridi. |

# P09. Adattamento, allineamento e ragionamento

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 46 | `CH-P09-SFT` | Supervised fine-tuning e instruction tuning | Dati di istruzione, chat template, multi-turn, loss masking, domain SFT e regressioni. |
| 47 | `CH-P09-PEFT` | Fine-tuning efficiente | Adapter, prompt/prefix tuning, IA3, LoRA, QLoRA, DoRA e scelta del rank. |
| 48 | `CH-P09-RLHF` | Preferenze, reward model e RLHF | Raccolta preferenze, reward modeling, PPO, KL, reward hacking, RLAIF e feedback costituzionale. |
| 49 | `CH-P09-PREFERENCE-OPT` | Ottimizzazione diretta delle preferenze | DPO, IPO, KTO, ORPO, SimPO, metodi online, condizioni di confronto e limiti. |
| 50 | `CH-P09-SUPERVISION-VERIFIERS` | Process supervision, outcome supervision e verifier | Supervisione di passaggi/esito, process reward model, verifier, dati sintetici e rejection sampling. |
| 51 | `CH-P09-RLVR` | Reinforcement learning con reward verificabili | Reward verificabili, group-relative optimization e ambienti matematici, di codice e interattivi. |
| 52 | `CH-P09-REASONING-TRAINING` | Addestrare e distillare il reasoning | Traiettorie intermedie, decomposizione, distillazione, self-consistency, critica e controllabilità. |
| 53 | `CH-P09-TEST-TIME-COMPUTE` | Test-time compute, ricerca e controllo del budget | Best-of-N, reranking, verifier, tree search, adaptive thinking e trade-off costo-qualità. |
| 54 | `CH-P09-MODEL-UPDATE` | Aggiornamento, merging ed editing del modello | Model merging, task arithmetic, editing localizzato, continual adaptation e catastrophic forgetting. |

# P10. Multimodalità e modelli del mondo

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 55 | `CH-P10-MULTIMODAL-FOUNDATIONS` | Fondamenti della multimodalità | Allineamento, rappresentazioni condivise, early/intermediate/late fusion, token e dati interleaved. |
| 56 | `CH-P10-VLM` | Vision encoder e Vision-Language Model | CNN, ViT, contrastive alignment, projector, Q-Former, cross-attention, OCR, grounding e documenti. |
| 57 | `CH-P10-IMAGE-GENERATION` | Generazione e modifica delle immagini | Latent diffusion, DiT, flow matching, conditioning, guidance, inpainting, editing e super-resolution. |
| 58 | `CH-P10-NATIVE-MULTIMODAL` | Modelli multimodali nativi e any-to-any | Early fusion, vocabolari unificati, understanding/generation, output multipli e streaming. |
| 59 | `CH-P10-AUDIO` | Audio, parlato e musica | Waveform, spettrogramma, neural codec, ASR, TTS, audio LM, dialogo streaming e musica. |
| 60 | `CH-P10-VIDEO` | Generazione video | Temporal attention, autoregression, diffusion, flow, coerenza temporale, identità e controllo. |
| 61 | `CH-P10-SPATIAL-3D` | 3D, spazio e rappresentazione delle scene | NeRF, Gaussian splatting, scene representation, grounding spaziale e generazione 3D. |
| 62 | `CH-P10-WORLD-EMBODIED` | World model, embodied AI e vision-language-action | Dinamica, simulazione, pianificazione fisica, VLA e controllo robotico. |

# P11. Conoscenza esterna, memoria e azione

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 63 | `CH-P11-RETRIEVAL` | Information retrieval | Ricerca lessicale, densa e ibrida, ANN, bi-encoder, late interaction e reranking. |
| 64 | `CH-P11-RAG` | Retrieval-Augmented Generation | Ingestion, parsing, indicizzazione, retrieval, costruzione del contesto, grounding e citazioni. |
| 65 | `CH-P11-ADVANCED-RAG` | RAG adattivo, correttivo e basato su grafi | Query transformation, multi-hop, Self-RAG, corrective RAG, RAPTOR, Graph RAG e compression. |
| 66 | `CH-P11-CONTEXT-RETRIEVAL-MEMORY` | Contesto lungo, retrieval e memoria | Scelta tra contesto e retrieval, memoria parametrica/episodica/semantica/esterna, persistenza e privacy. |
| 67 | `CH-P11-TOOLS` | Output strutturato e uso degli strumenti | Function calling, schema, tool selection, argomenti, errori, calcolatrici, database, browser e runtime. |
| 68 | `CH-P11-INTEROPERABILITY` | Protocolli e interoperabilità | Contratti modello-tool-risorse, MCP, protocolli agent-to-agent, versionamento, autorizzazioni e discovery. |
| 69 | `CH-P11-AGENT-LOOP` | Ciclo agentico, pianificazione e verifica | Osservazione, decisione, azione, verifica, ReAct, planning, reflection, critique e workflow. |
| 70 | `CH-P11-AGENT-SYSTEMS` | Multi-agent, browser, computer e code agents | Coordinamento multi-agent, browser/computer use e agenti per software engineering. |
| 71 | `CH-P11-AGENT-TRAINING-EVAL` | Training e valutazione degli agenti | Ambienti interattivi, traiettorie, reward, curriculum, simulazione, success rate, costo e recovery. |
| 72 | `CH-P11-AGENT-SAFETY` | Sicurezza operativa degli agenti | Human approval, permission model, sandbox, secrets, esfiltrazione, rollback e incident response. |

# P12. Efficienza, inference e sistemi

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 73 | `CH-P12-DISTILLATION-PRUNING` | Distillazione e pruning | Knowledge/sequence/reasoning distillation e pruning strutturato, non strutturato e post-training. |
| 74 | `CH-P12-QUANTIZATION` | Quantizzazione | PTQ, QAT, weight-only, weight-activation, GPTQ, AWQ, SmoothQuant e sub-4-bit. |
| 75 | `CH-P12-LOW-BIT-NATIVE` | Modelli low-bit nativi e co-design numerico | Training a precisione estrema, scale, accumulatori, kernel, hardware e differenza dal post hoc. |
| 76 | `CH-P12-DECODING` | Decoding e generazione vincolata | Sampling, repetition control, stopping, grammar, schema, constrained decoding e non autoregressivo. |
| 77 | `CH-P12-SPECULATIVE-DECODING` | Speculative e parallel decoding | Draft model, acceptance, verifica esatta, Medusa, EAGLE, recurrent drafter, tree attention e lookahead. |
| 78 | `CH-P12-KV-CACHE` | KV cache e riuso del contesto | Layout, quantizzazione, eviction, offload, prefix caching e condivisione dei prefissi. |
| 79 | `CH-P12-SERVING` | Serving, batching e scheduling | Prefill, decode, TTFT, inter-token latency, paged memory, continuous batching, scheduling e preemption. |
| 80 | `CH-P12-DISTRIBUTED-INFERENCE` | Serving disaggregato e inference distribuita | Separazione prefill/decode, parallelismi, routing, rete e fault tolerance. |
| 81 | `CH-P12-COMPILERS-KERNELS` | Compiler, kernel e runtime | Graph compiler, MLIR, XLA, TorchInductor, Triton, kernel specializzati e co-design. |
| 82 | `CH-P12-LLMOPS` | LLMOps, edge, costo ed energia | Versionamento, tracing, observability, rollback, edge, on-device, throughput, latenza, costo ed energia. |

# P13. Valutazione, interpretabilità, sicurezza e governance

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 83 | `CH-P13-EVAL-DESIGN` | Progettare una valutazione | Capacità, rubriche, baseline, significatività, benchmark, contaminazione, valutazione umana e judge. |
| 84 | `CH-P13-FACTUALITY` | Fattualità, incertezza e affidabilità | Factuality, faithfulness, citation correctness, calibrazione, abstention e selective prediction. |
| 85 | `CH-P13-SYSTEM-EVAL` | Valutare contesto lungo, RAG, multimodalità e agenti | Retrieval/generation, posizione dell'informazione, traiettorie, tool, recovery, costo e metriche modali. |
| 86 | `CH-P13-INTERPRETABILITY` | Interpretabilità delle rappresentazioni e dei circuiti | Probing, attribution, feature visualization, activation patching, causal tracing e circuiti. |
| 87 | `CH-P13-SAE-CIRCUIT-TRACING` | Sparse autoencoder e interpretabilità scalabile | Decomposizione delle feature, auto-interpretation, circuit tracing, router ed expert MoE. |
| 88 | `CH-P13-ROBUSTNESS-JAILBREAK` | Robustezza, jailbreak e attacchi adversarial | Adversarial example, universal suffix, jailbreak, red teaming e valutazione delle difese. |
| 89 | `CH-P13-PROMPT-INJECTION` | Prompt injection e sicurezza dei tool | Injection diretta/indiretta, confused deputy, esfiltrazione, autorizzazioni e sicurezza degli agenti. |
| 90 | `CH-P13-SUPPLY-CHAIN-SECURITY` | Poisoning, backdoor, extraction e supply chain | Data/model poisoning, backdoor, extraction, checkpoint risk e integrità di dataset e dipendenze. |
| 91 | `CH-P13-PRIVACY-FAIRNESS` | Privacy, fairness e unlearning | Memorizzazione, PII leakage, membership inference, DP, federated learning, bias, fairness e unlearning. |
| 92 | `CH-P13-PROVENANCE` | Watermarking e provenienza dei contenuti | Watermarking, detection, content credentials, C2PA e catena di provenienza. |
| 93 | `CH-P13-GOVERNANCE` | Diritto, governance e sostenibilità | Copyright, licenze, responsabilità, regolazione, card, risk management, lavoro, accesso ed energia. |

# P14. Laboratori, integrazione e osservatorio

| N. | chapter_id | Titolo | Contenuti principali |
|---:|---|---|---|
| 94 | `CH-P14-FOUNDATIONS-LAB` | Percorso pratico dai fondamenti | Regressione, backpropagation, MLP, CNN, RNN, VAE, GAN, diffusion e attention. |
| 95 | `CH-P14-SMALL-LM` | Costruire un piccolo language model | Dataset, tokenizer, pretraining, valutazione, instruction tuning, adattamento, quantizzazione e serving. |
| 96 | `CH-P14-PRODUCTION-PROJECT` | Progetto di produzione completo | RAG con citazioni, tool calling, agente, input multimodale, valutazione, sicurezza, costo e rollback. |
| 97 | `CH-P14-REPLICATION` | Riprodurre e leggere un paper | Domanda, baseline, modifica, setup, ablation, replica ridotta e divergenze tra paper e codice. |
| 98 | `CH-P14-FRONTIER-OBSERVATORY` | Osservatorio della frontiera | Mappa delle voci frontier, cronologia delle maturità, domande aperte, piani di verifica e candidati. |

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

1. Le parti `P01`-`P14` non cambiano per l'arrivo di una nuova tecnica.
2. Una nuova voce entra prima nel catalogo.
3. La collocazione usa il routing funzionale.
4. La maturità non determina la parte.
5. Un nuovo capitolo richiede domanda autonoma, fonti e contratto didattico.
6. `chapter_id` resta stabile; il numero visualizzato cambia tra edizioni.
7. Una voce `FRONTIER` resta nella parte funzionale pertinente.
8. `P14` osserva la frontiera, ma non la usa come contenitore generico.
9. Split e merge richiedono alias, redirect e mappa di migrazione.
10. Ogni modifica strutturale aggiorna governance, catalogo, indice e audit.
