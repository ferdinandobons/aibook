# Catalogo dello stato dell'arte

## Stato

- Stato: `vincolante` come registro editoriale
- Data dell'ultima ricerca approfondita globale: **30 luglio 2026**
- Ricerca registrata in: `15_REGISTRO_RICERCHE_APPROFONDITE.md`
- Architettura di collocazione: `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Protocollo di aggiornamento: `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`

## Funzione

Questo catalogo censisce le principali famiglie, i meccanismi e le ottimizzazioni che soddisfano i criteri di inclusione alla data registrata.

Non dichiara di contenere ogni paper o ogni implementazione esistente. La completezza viene valutata rispetto alle famiglie tecniche rilevanti, non rispetto al numero totale di pubblicazioni.

La maturità è una classificazione editoriale del libro, non una dichiarazione universale della comunità scientifica.

## Stati di maturità

- `CORE`: concetto durevole e necessario per numerosi sviluppi successivi.
- `ESTABLISHED`: concetto verificato, rilevante e adottato o riprodotto, ma ancora in evoluzione oppure non universalmente necessario.
- `FRONTIER`: concetto recente, sperimentale, con evidenza o terminologia ancora limitata.

La maturità non determina la parte. Una promozione non sposta automaticamente la voce.

## Campi del registro

| Campo | Significato |
|---|---|
| `topic_id` | Identità stabile della voce. |
| `parte` | Collocazione primaria. |
| `maturità` | `CORE`, `ESTABLISHED` o `FRONTIER`. |
| `destinazione` | Capitolo, sezione, approfondimento, studio di caso oppure osservatorio. |
| `ultima verifica` | Data dell'ultima revisione della voce. |
| `note` | Confini, collegamenti o condizioni di promozione. |

# P01. Campo, metodo e storia dell'AI

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P01-AI-TAXONOMY` | AI, machine learning, deep learning e AI generativa | `CORE` | capitolo | 2026-07-30 |
| `TOP-P01-SYMBOLIC-STATISTICAL` | Sistemi simbolici, probabilistici e neurali | `CORE` | capitolo | 2026-07-30 |
| `TOP-P01-FOUNDATION-MODELS` | Foundation model, generalità e specializzazione | `CORE` | capitolo | 2026-07-30 |
| `TOP-P01-SCIENTIFIC-METHOD` | Baseline, ablation, significatività e riproducibilità | `CORE` | capitolo | 2026-07-30 |
| `TOP-P01-BENCHMARK-CONTAMINATION` | Contaminazione, saturazione e data leakage | `ESTABLISHED` | sezione | 2026-07-30 |

# P02. Matematica, informazione e calcolo

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P02-LINEAR-ALGEBRA` | Algebra lineare, tensor e decomposizioni | `CORE` | capitolo | 2026-07-30 |
| `TOP-P02-AUTODIFF` | Calcolo differenziale, grafi computazionali e autodiff | `CORE` | capitolo | 2026-07-30 |
| `TOP-P02-PROBABILITY` | Probabilità, statistica e inferenza | `CORE` | capitolo | 2026-07-30 |
| `TOP-P02-INFORMATION-THEORY` | Entropia, cross-entropy, KL e informazione mutua | `CORE` | capitolo | 2026-07-30 |
| `TOP-P02-NUMERICAL-STABILITY` | Condizionamento, precisione e stabilità numerica | `CORE` | capitolo | 2026-07-30 |
| `TOP-P02-HARDWARE-MODEL` | FLOP, banda, memoria, cache e modello roofline | `ESTABLISHED` | capitolo | 2026-07-30 |

# P03. Apprendimento, ottimizzazione e decisione

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P03-SUPERVISED` | Apprendimento supervisionato | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-UNSUPERVISED` | Apprendimento non supervisionato | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-SELF-SUPERVISED` | Apprendimento auto-supervisionato | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-OPTIMIZERS` | SGD, momentum, Adam, AdamW e scheduler | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-RL` | MDP, value learning, policy gradient e actor-critic | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-PLANNING-SEARCH` | Ricerca, pianificazione, MCTS e decisione | `CORE` | capitolo | 2026-07-30 |
| `TOP-P03-CAUSAL-INFERENCE` | Inferenza causale per la lettura degli esperimenti | `ESTABLISHED` | approfondimento | 2026-07-30 |

# P04. Reti neurali e rappresentazioni

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P04-MLP` | Percettrone, MLP e universalità espressiva | `CORE` | capitolo | 2026-07-30 |
| `TOP-P04-CNN` | Convoluzioni, equivarianza e receptive field | `CORE` | capitolo | 2026-07-30 |
| `TOP-P04-RNN-LSTM-GRU` | RNN, LSTM e GRU | `CORE` | capitolo | 2026-07-30 |
| `TOP-P04-GNN` | Graph neural network e message passing | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P04-AUTOENCODERS` | Autoencoder, denoising e sparse autoencoder | `CORE` | capitolo | 2026-07-30 |
| `TOP-P04-CONTRASTIVE` | Representation learning contrastivo | `CORE` | capitolo | 2026-07-30 |
| `TOP-P04-METRIC-LEARNING` | Metric learning e spazi di embedding | `ESTABLISHED` | sezione | 2026-07-30 |

# P05. Modellazione generativa

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P05-GENERATIVE-FOUNDATIONS` | Modelli espliciti, impliciti, latenti ed energy-based | `CORE` | capitolo | 2026-07-30 |
| `TOP-P05-AUTOREGRESSIVE` | Fattorizzazione autoregressiva | `CORE` | capitolo | 2026-07-30 |
| `TOP-P05-VAE` | Variational autoencoder e ELBO | `CORE` | capitolo | 2026-07-30 |
| `TOP-P05-VQ` | VQ-VAE e latent discreti | `ESTABLISHED` | sezione | 2026-07-30 |
| `TOP-P05-GAN` | GAN, Wasserstein objective e stabilità | `CORE` | capitolo | 2026-07-30 |
| `TOP-P05-FLOWS` | Normalizing flow e continuous normalizing flow | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P05-DIFFUSION` | Denoising diffusion e score-based modeling | `CORE` | capitolo | 2026-07-30 |
| `TOP-P05-LATENT-DIFFUSION` | Diffusione nello spazio latente | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P05-FLOW-MATCHING` | Flow matching e rectified flow | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P05-CONSISTENCY` | Consistency model e distillazione del sampling | `ESTABLISHED` | approfondimento | 2026-07-30 |
| `TOP-P05-DISCRETE-DIFFUSION` | Diffusione discreta per dati categorici | `ESTABLISHED` | approfondimento | 2026-07-30 |

# P06. Sequenze, linguaggio e contesto

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P06-TOKENIZATION` | BPE, WordPiece, Unigram, byte e caratteri | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-EMBEDDINGS` | Word, contextual e sentence embedding | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-SEQ2SEQ` | Encoder-decoder e sequence-to-sequence | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-ATTENTION` | Query, key, value e scaled dot-product attention | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-MULTIHEAD` | Multi-head, self, cross e causal attention | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-TRANSFORMER` | Transformer encoder, decoder e residual stream | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-PRETRAIN-OBJECTIVES` | Causal, masked, span-corruption e denoising objectives | `CORE` | capitolo | 2026-07-30 |
| `TOP-P06-IN-CONTEXT` | In-context learning e prompting | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P06-DECODING-BASE` | Greedy, beam, temperature, top-k e top-p | `CORE` | capitolo | 2026-07-30 |

# P07. Dati, pretraining e scaling

| topic_id | Tema | Maturità | Destinazione | Ultima verifica |
|---|---|---|---|---|
| `TOP-P07-DATA-LIFECYCLE` | Acquisizione, licenze, filtraggio, deduplicazione e provenance | `CORE` | capitolo | 2026-07-30 |
| `TOP-P07-DATA-MIXTURE` | Dataset mixture, sampling e bilanciamento dei domini | `CORE` | capitolo | 2026-07-30 |
| `TOP-P07-CURRICULUM` | Curriculum e data scheduling | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P07-SYNTHETIC-DATA` | Generazione, filtraggio e verifica dei dati sintetici | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P07-SCALING-LAWS` | Scaling law e compute-optimal training | `CORE` | capitolo | 2026-07-30 |
| `TOP-P07-PRETRAIN-RECIPE` | Batch, optimizer, warm-up, schedule e stabilità | `CORE` | capitolo | 2026-07-30 |
| `TOP-P07-MUP` | Parameterization e trasferimento degli iperparametri | `ESTABLISHED` | approfondimento | 2026-07-30 |
| `TOP-P07-DISTRIBUTED-TRAINING` | Data, tensor, pipeline, sequence, context ed expert parallelism | `CORE` | capitolo | 2026-07-30 |
| `TOP-P07-ZERO-FSDP` | Sharding di parametri, gradienti e optimizer state | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P07-ACTIVATION-CHECKPOINT` | Activation checkpointing, recomputation e offload | `ESTABLISHED` | sezione | 2026-07-30 |
| `TOP-P07-LOW-PRECISION-TRAINING` | FP16, BF16, FP8 e formati ridotti nel training | `ESTABLISHED` | capitolo | 2026-07-30 |
| `TOP-P07-CONTINUED-PRETRAIN` | Continued pretraining e domain adaptation | `ESTABLISHED` | capitolo | 2026-07-30 |

# P08. Progettazione delle architetture

## Blocchi e stabilità

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-PRENORM-POSTNORM` | Pre-norm, post-norm e ordine del blocco | `CORE` | capitolo | 2026-07-30 | Caso base prima delle varianti. |
| `TOP-P08-RMSNORM` | RMSNorm e normalizzazioni alternative | `ESTABLISHED` | sezione | 2026-07-30 | Confrontare contratto, non solo costo. |
| `TOP-P08-GLU-SWIGLU` | GLU, GEGLU e SwiGLU | `ESTABLISHED` | sezione | 2026-07-30 | Feed-forward gated. |
| `TOP-P08-RESIDUAL-SCALING` | Residual scaling, profondità e stabilità | `ESTABLISHED` | approfondimento | 2026-07-30 | Collegato a inizializzazione e parameterization. |
| `TOP-P08-WEIGHT-TYING` | Condivisione di embedding e output weights | `ESTABLISHED` | sezione | 2026-07-30 | Trade-off architetturale. |

## Posizione e contesto

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-SINUSOIDAL-POS` | Positional encoding sinusoidale | `CORE` | capitolo | 2026-07-30 | Fondamento storico e matematico. |
| `TOP-P08-RELATIVE-POS` | Posizione relativa | `CORE` | capitolo | 2026-07-30 | Famiglia generale. |
| `TOP-P08-ROPE` | Rotary position embedding | `ESTABLISHED` | capitolo | 2026-07-30 | Tecnica ampiamente usata, con limiti da esplicitare. |
| `TOP-P08-ALIBI` | Attention with linear biases | `ESTABLISHED` | confronto | 2026-07-30 | Alternativa alla rappresentazione rotatoria. |
| `TOP-P08-CONTEXT-EXTENSION` | Positional interpolation, NTK-aware scaling, YaRN e LongRoPE | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere training nativo ed estensione. |
| `TOP-P08-LONG-CONTEXT-EVAL` | Lost-in-the-middle, retrieval nel contesto e valutazione posizionale | `ESTABLISHED` | sezione | 2026-07-30 | Collegamento con P13. |

## Attention e gestione delle key/value

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-MQA` | Multi-query attention | `ESTABLISHED` | capitolo | 2026-07-30 | Condivisione di key e value. |
| `TOP-P08-GQA` | Grouped-query attention | `ESTABLISHED` | capitolo | 2026-07-30 | Posizione intermedia tra MHA e MQA. |
| `TOP-P08-MLA` | Multi-head latent attention e compressione latente KV | `ESTABLISHED` | approfondimento | 2026-07-30 | Verificare la specifica implementazione descritta. |
| `TOP-P08-KV-COMPRESSION` | Compressione, quantizzazione ed eviction della KV cache | `ESTABLISHED` | capitolo condiviso con P12 | 2026-07-30 | P08 per contratto, P12 per runtime. |
| `TOP-P08-FLASH-ATTENTION` | Attention esatta IO-aware e tiling | `ESTABLISHED` | capitolo | 2026-07-30 | Separare matematica e kernel. |
| `TOP-P08-LOCAL-SLIDING` | Local e sliding-window attention | `ESTABLISHED` | capitolo | 2026-07-30 | Pattern di connettività. |
| `TOP-P08-BLOCK-SPARSE` | Block-sparse e sparse attention | `ESTABLISHED` | capitolo | 2026-07-30 | Sparsità strutturata. |
| `TOP-P08-RING-ATTENTION` | Ring attention e distribuzione del contesto | `ESTABLISHED` | approfondimento | 2026-07-30 | Collegamento con context parallelism. |
| `TOP-P08-DIFFERENTIAL-ATTENTION` | Differential attention | `FRONTIER` | osservatorio e approfondimento | 2026-07-30 | Richiede più evidenza indipendente. |

## Linear attention, recurrence e memoria interna

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-LINEAR-ATTENTION` | Linear attention e kernel feature map | `ESTABLISHED` | capitolo | 2026-07-30 | Famiglia, non singola implementazione. |
| `TOP-P08-FAST-WEIGHTS` | Fast-weight memory e delta rule | `ESTABLISHED` | capitolo | 2026-07-30 | Collegamento tra recurrence e memoria. |
| `TOP-P08-GATED-DELTANET` | Gated DeltaNet | `FRONTIER` | approfondimento | 2026-07-30 | Monitorare repliche e varianti. |
| `TOP-P08-GATED-DELTANET-2` | Evoluzioni della delta rule con stato più espressivo | `FRONTIER` | osservatorio | 2026-07-30 | Voce separata finché il contratto non converge. |
| `TOP-P08-S4` | Structured State Space Models e S4 | `ESTABLISHED` | capitolo | 2026-07-30 | Fondamento degli SSM moderni. |
| `TOP-P08-MAMBA` | Selective state-space model | `ESTABLISHED` | capitolo | 2026-07-30 | Caso principale della famiglia selettiva. |
| `TOP-P08-MAMBA2-SSD` | State Space Duality e Mamba-2 | `ESTABLISHED` | capitolo | 2026-07-30 | Formalizzazione del rapporto con attention. |
| `TOP-P08-MAMBA3` | Evoluzioni hardware-aware dei selective SSM | `FRONTIER` | osservatorio e studio di caso | 2026-07-30 | Verificare implementazioni e risultati indipendenti. |
| `TOP-P08-RETNET` | Retentive network | `ESTABLISHED` | confronto | 2026-07-30 | Parallel, recurrent e chunkwise forms. |
| `TOP-P08-RWKV` | Recurrence time-mixing in stile RWKV | `ESTABLISHED` | confronto | 2026-07-30 | Trattare per meccanismo, non per release. |
| `TOP-P08-HYENA` | Long convolution e implicit filter | `ESTABLISHED` | confronto | 2026-07-30 | Alternativa subquadratica. |
| `TOP-P08-XLSTM` | xLSTM e matricializzazione della memoria LSTM | `ESTABLISHED` | approfondimento | 2026-07-30 | Collegare alla ricorrenza classica. |
| `TOP-P08-GRIFFIN-HAWK` | Recurrence gated con local attention | `ESTABLISHED` | confronto | 2026-07-30 | Famiglie ibride. |
| `TOP-P08-KIMI-LINEAR` | Hybrid linear/full attention con delta-rule memory | `FRONTIER` | osservatorio e studio di caso | 2026-07-30 | Valutare stabilità della tassonomia. |
| `TOP-P08-HYBRID-SEQUENCE` | Architetture ibride attention, SSM, convolution e recurrence | `ESTABLISHED` | capitolo | 2026-07-30 | Categoria durevole. |
| `TOP-P08-NEURAL-MEMORY` | Neural long-term memory e memory layers | `FRONTIER` | capitolo candidato | 2026-07-30 | Distinguere memoria parametrica, ricorrente ed esterna. |
| `TOP-P08-TEST-TIME-LEARNING` | Update o apprendimento interno al test time | `FRONTIER` | capitolo candidato | 2026-07-30 | Richiede confini precisi con P09. |

## Sparsità e calcolo condizionale

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-MOE` | Sparsely gated Mixture of Experts | `CORE` | capitolo | 2026-07-30 | Meccanismo generale di conditional compute. |
| `TOP-P08-SWITCH-MOE` | Routing top-1 e Switch-style MoE | `ESTABLISHED` | sezione | 2026-07-30 | Caso architetturale. |
| `TOP-P08-FINE-GRAINED-MOE` | Expert più piccoli, shared expert e specializzazione fine | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere design del router e layout degli expert. |
| `TOP-P08-EXPERT-CHOICE` | Expert-choice routing e varianti del bilanciamento | `ESTABLISHED` | approfondimento | 2026-07-30 | Trade-off tra capacità e dispatch. |
| `TOP-P08-MOE-UPCYCLING` | Conversione o upcycling di modelli dense in MoE | `ESTABLISHED` | approfondimento | 2026-07-30 | Collegamento con training e distillazione. |
| `TOP-P08-MIXTURE-OF-DEPTHS` | Allocazione dinamica della profondità | `FRONTIER` | approfondimento | 2026-07-30 | Conditional compute lungo la profondità. |
| `TOP-P08-EARLY-EXIT` | Early exit e adaptive computation | `ESTABLISHED` | sezione | 2026-07-30 | Separare training e inference. |

## Token, predizione e paradigmi alternativi

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P08-BYTE-MODELS` | Modelli byte-level e token-free | `ESTABLISHED` | capitolo condiviso con P06 | 2026-07-30 | Contratto di rappresentazione. |
| `TOP-P08-MULTISCALE-BYTE` | Patch dinamiche e modelli multiscala sui byte | `FRONTIER` | approfondimento | 2026-07-30 | Valutare stabilità e costi. |
| `TOP-P08-MULTI-TOKEN-PREDICTION` | Predizione di più token futuri | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere training objective e decoding. |
| `TOP-P08-AUXILIARY-DRAFT-HEADS` | Draft head e predizione ausiliaria | `ESTABLISHED` | sezione condivisa con P12 | 2026-07-30 | Collegamento con speculative decoding. |
| `TOP-P08-DIFFUSION-LM` | Language model a diffusione discreta o masked diffusion | `FRONTIER` | capitolo candidato | 2026-07-30 | Terminologia e benchmark ancora in evoluzione. |
| `TOP-P08-HYBRID-AR-DIFFUSION` | Ibridi autoregressivi e diffusion per il linguaggio | `FRONTIER` | osservatorio | 2026-07-30 | Verificare il contratto di decoding. |

# P09. Adattamento, allineamento e ragionamento

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P09-SFT` | Supervised fine-tuning e instruction tuning | `CORE` | capitolo | 2026-07-30 | Caso base del post-training. |
| `TOP-P09-PEFT` | Adapter, prompt tuning, prefix tuning e IA3 | `ESTABLISHED` | capitolo | 2026-07-30 | Famiglia di adattamento efficiente. |
| `TOP-P09-LORA` | LoRA e low-rank adaptation | `CORE` | capitolo | 2026-07-30 | Prerequisito per molte pipeline. |
| `TOP-P09-QLORA` | Fine-tuning low-rank su modello quantizzato | `ESTABLISHED` | sezione | 2026-07-30 | Distinguere quantizzazione di training e serving. |
| `TOP-P09-DORA` | Decomposizione direzione-magnitudine per PEFT | `ESTABLISHED` | approfondimento | 2026-07-30 | Confronto controllato con LoRA. |
| `TOP-P09-REWARD-MODELING` | Preference data e reward model | `CORE` | capitolo | 2026-07-30 | Include modello Bradley-Terry e limiti. |
| `TOP-P09-RLHF` | RLHF con policy optimization e vincolo KL | `CORE` | capitolo | 2026-07-30 | Distinguere pipeline e algoritmo. |
| `TOP-P09-RLAIF` | Feedback generato da modelli e costituzioni | `ESTABLISHED` | capitolo | 2026-07-30 | Provenienza e bias del feedback. |
| `TOP-P09-DPO` | Direct Preference Optimization | `ESTABLISHED` | capitolo | 2026-07-30 | Metodo di riferimento della famiglia diretta. |
| `TOP-P09-IPO` | Implicit Preference Optimization | `ESTABLISHED` | confronto | 2026-07-30 | Variante dell'obiettivo. |
| `TOP-P09-KTO` | Kahneman-Tversky Optimization | `ESTABLISHED` | confronto | 2026-07-30 | Dati non necessariamente appaiati. |
| `TOP-P09-ORPO` | Odds Ratio Preference Optimization | `ESTABLISHED` | confronto | 2026-07-30 | Obiettivo combinato. |
| `TOP-P09-SIMPO` | Simple Preference Optimization | `ESTABLISHED` | confronto | 2026-07-30 | Verificare condizioni di confronto. |
| `TOP-P09-ONLINE-PREFERENCE` | Preference optimization online e on-policy | `FRONTIER` | approfondimento | 2026-07-30 | Distinguere dati freschi e reward drift. |
| `TOP-P09-PROCESS-SUPERVISION` | Process supervision e process reward model | `ESTABLISHED` | capitolo | 2026-07-30 | Verifica dei passaggi intermedi. |
| `TOP-P09-OUTCOME-SUPERVISION` | Outcome supervision e verifier finali | `CORE` | capitolo | 2026-07-30 | Caso base verificabile. |
| `TOP-P09-GRPO` | Group-relative policy optimization | `ESTABLISHED` | capitolo | 2026-07-30 | Documentare varianti e implementazioni. |
| `TOP-P09-RLVR` | Reinforcement learning con reward verificabili | `ESTABLISHED` | capitolo | 2026-07-30 | Matematica, codice e ambienti verificabili. |
| `TOP-P09-REASONING-DISTILLATION` | Distillazione di traiettorie di reasoning | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere capacità e stile di output. |
| `TOP-P09-SELF-CONSISTENCY` | Campionamento multiplo e self-consistency | `ESTABLISHED` | sezione | 2026-07-30 | Test-time compute. |
| `TOP-P09-BEST-OF-N` | Best-of-N e reranking delle risposte | `ESTABLISHED` | capitolo | 2026-07-30 | Richiede scorer o verifier. |
| `TOP-P09-TREE-SEARCH` | Tree search e ricerca guidata nel reasoning | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere ricerca esplicita e generazione lineare. |
| `TOP-P09-BUDGET-CONTROL` | Adaptive thinking e controllo del budget di compute | `FRONTIER` | capitolo candidato | 2026-07-30 | Valutazione costo-qualità ancora dinamica. |
| `TOP-P09-LATENT-REASONING` | Reasoning in stati latenti o ricorrenti | `FRONTIER` | osservatorio | 2026-07-30 | Richiede verifiche causali e benchmark. |
| `TOP-P09-SELF-IMPROVEMENT` | Self-training, self-rewarding e iterative refinement | `FRONTIER` | capitolo candidato | 2026-07-30 | Evitare generalizzazioni non sostenute. |
| `TOP-P09-MODEL-MERGING` | Task arithmetic, TIES, DARE e model merging | `ESTABLISHED` | capitolo | 2026-07-30 | Verificare compatibilità delle basi. |
| `TOP-P09-MODEL-EDITING` | Model editing localizzato | `ESTABLISHED` | approfondimento | 2026-07-30 | Collegamento con factuality e safety. |
| `TOP-P09-CONTINUAL-ADAPTATION` | Continual learning e aggiornamento senza forgetting | `FRONTIER` | capitolo candidato | 2026-07-30 | Problema aperto per foundation model. |
| `TOP-P09-AGENTIC-RL` | Post-training in ambienti con tool e azioni multi-step | `FRONTIER` | capitolo candidato | 2026-07-30 | Confine con P11. |

# P10. Multimodalità e modelli del mondo

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P10-MULTIMODAL-FUSION` | Early, intermediate e late fusion | `CORE` | capitolo | 2026-07-30 | Tassonomia stabile. |
| `TOP-P10-DUAL-ENCODER` | Dual encoder e contrastive alignment | `CORE` | capitolo | 2026-07-30 | Fondamento di retrieval multimodale. |
| `TOP-P10-VIT` | Vision Transformer | `CORE` | capitolo | 2026-07-30 | Tokenizzazione visiva. |
| `TOP-P10-VLM-PROJECTOR` | Vision encoder, projector e language model | `ESTABLISHED` | capitolo | 2026-07-30 | Architettura modulare. |
| `TOP-P10-QFORMER-CROSSATTN` | Query transformer e cross-attention dedicata | `ESTABLISHED` | confronto | 2026-07-30 | Interfaccia tra modalità. |
| `TOP-P10-NATIVE-MULTIMODAL` | Modelli nativamente multimodali e token interleaved | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere training e interfaccia. |
| `TOP-P10-ANY-TO-ANY` | Modelli any-to-any e output multimodali | `FRONTIER` | capitolo candidato | 2026-07-30 | Richiede contratti uniformi tra modalità. |
| `TOP-P10-DIT` | Diffusion Transformer | `ESTABLISHED` | capitolo | 2026-07-30 | Backbone generativo. |
| `TOP-P10-IMAGE-CONTROL` | Conditioning, guidance, inpainting e controlli strutturali | `ESTABLISHED` | capitolo | 2026-07-30 | Separare condizione e sampler. |
| `TOP-P10-MULTIMODAL-DIFFUSION-LM` | Unified understanding e generation con diffusion/autoregression | `FRONTIER` | osservatorio | 2026-07-30 | Tassonomia ancora mobile. |
| `TOP-P10-AUDIO-CODECS` | Neural audio codec e token audio | `ESTABLISHED` | capitolo | 2026-07-30 | Base per audio language model. |
| `TOP-P10-ASR-TTS` | Speech recognition e speech synthesis | `CORE` | capitolo | 2026-07-30 | Pipeline e modelli end-to-end. |
| `TOP-P10-AUDIO-LM` | Audio language model e dialogo vocale streaming | `ESTABLISHED` | capitolo | 2026-07-30 | Latenza e turn-taking. |
| `TOP-P10-MUSIC-GENERATION` | Generazione musicale condizionata | `ESTABLISHED` | approfondimento | 2026-07-30 | Valutazione specifica del dominio. |
| `TOP-P10-VIDEO-GENERATION` | Video diffusion, autoregression e flow | `ESTABLISHED` | capitolo | 2026-07-30 | Coerenza temporale e costo. |
| `TOP-P10-3D-REPRESENTATION` | NeRF, Gaussian splatting e scene representation | `ESTABLISHED` | capitolo | 2026-07-30 | Collegamento tra rendering e generazione. |
| `TOP-P10-SPATIAL-INTELLIGENCE` | Grounding spaziale e scene dinamiche | `FRONTIER` | capitolo candidato | 2026-07-30 | Definizione e benchmark da stabilizzare. |
| `TOP-P10-WORLD-MODELS` | Modelli di dinamica, simulazione e previsione del mondo | `ESTABLISHED` | capitolo | 2026-07-30 | Famiglia storica con nuova scala. |
| `TOP-P10-VLA` | Vision-language-action model | `FRONTIER` | capitolo candidato | 2026-07-30 | Confine con controllo robotico. |
| `TOP-P10-EMBODIED` | Embodied AI e pianificazione robotica | `ESTABLISHED` | capitolo | 2026-07-30 | Integra percezione, memoria e azione. |

# P11. Conoscenza esterna, memoria e azione

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P11-LEXICAL-RETRIEVAL` | BM25 e ricerca lessicale | `CORE` | capitolo | 2026-07-30 | Baseline indispensabile. |
| `TOP-P11-DENSE-RETRIEVAL` | Dense retrieval e bi-encoder | `CORE` | capitolo | 2026-07-30 | Rappresentazioni e ANN. |
| `TOP-P11-LATE-INTERACTION` | Late interaction e ColBERT-style retrieval | `ESTABLISHED` | approfondimento | 2026-07-30 | Trade-off tra qualità e costo. |
| `TOP-P11-HYBRID-RETRIEVAL` | Retrieval ibrido e fusion | `ESTABLISHED` | capitolo | 2026-07-30 | Unisce segnali lessicali e densi. |
| `TOP-P11-RERANKING` | Cross-encoder e learned reranker | `CORE` | capitolo | 2026-07-30 | Separare recall e precision. |
| `TOP-P11-RAG` | Retrieval-Augmented Generation | `CORE` | capitolo | 2026-07-30 | Pipeline portante. |
| `TOP-P11-QUERY-TRANSFORM` | Query rewriting, expansion, decomposition e HyDE | `ESTABLISHED` | capitolo | 2026-07-30 | Trasformazione prima del retrieval. |
| `TOP-P11-SELF-RAG` | Retrieval adattivo e Self-RAG | `ESTABLISHED` | approfondimento | 2026-07-30 | Decisione se e quando recuperare. |
| `TOP-P11-CORRECTIVE-RAG` | Corrective e confidence-aware RAG | `ESTABLISHED` | approfondimento | 2026-07-30 | Verifica del retrieval. |
| `TOP-P11-GRAPH-RAG` | Graph RAG e knowledge graph augmentation | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere indice, grafo e generazione. |
| `TOP-P11-HIERARCHICAL-RAG` | Retrieval gerarchico e summarization tree | `ESTABLISHED` | approfondimento | 2026-07-30 | Relazioni multi-livello. |
| `TOP-P11-AGENTIC-RAG` | Agentic RAG e retrieval multi-step | `FRONTIER` | capitolo candidato | 2026-07-30 | Confine con sistemi agentici. |
| `TOP-P11-LONG-CONTEXT-VS-RAG` | Scelta tra contesto lungo, retrieval e memoria | `ESTABLISHED` | capitolo | 2026-07-30 | Decisione di sistema. |
| `TOP-P11-PARAMETRIC-EXTERNAL-MEMORY` | Memoria parametrica, esterna ed episodica | `CORE` | capitolo | 2026-07-30 | Tassonomia necessaria. |
| `TOP-P11-LONG-TERM-AGENT-MEMORY` | Memoria persistente degli agenti | `FRONTIER` | capitolo candidato | 2026-07-30 | Consistenza, privacy e forgetting. |
| `TOP-P11-STRUCTURED-OUTPUT` | Output strutturato e constrained generation | `CORE` | capitolo | 2026-07-30 | Contratto tra modello e sistema. |
| `TOP-P11-FUNCTION-CALLING` | Tool calling, selezione e generazione degli argomenti | `CORE` | capitolo | 2026-07-30 | Include gestione degli errori. |
| `TOP-P11-TOOL-LEARNING` | Apprendimento dell'uso di tool e API | `ESTABLISHED` | capitolo | 2026-07-30 | Dati, supervision e feedback. |
| `TOP-P11-MCP` | Model Context Protocol | `ESTABLISHED` | sezione di interoperabilità | 2026-07-30 | Versionare la specifica. |
| `TOP-P11-A2A` | Protocolli agent-to-agent | `FRONTIER` | osservatorio e sezione | 2026-07-30 | Standard e adozione ancora dinamici. |
| `TOP-P11-REACT` | Reasoning and Acting loop | `CORE` | capitolo | 2026-07-30 | Ciclo osservazione-azione. |
| `TOP-P11-PLANNING` | Pianificazione esplicita e decomposizione dei task | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere piano e traiettoria. |
| `TOP-P11-REFLECTION` | Reflection, critique e verifier loop | `ESTABLISHED` | capitolo | 2026-07-30 | Necessita valutazione controllata. |
| `TOP-P11-MULTIAGENT` | Sistemi multi-agent | `FRONTIER` | capitolo candidato | 2026-07-30 | Misurare beneficio rispetto a workflow singolo. |
| `TOP-P11-COMPUTER-USE` | Browser e computer use | `ESTABLISHED` | capitolo | 2026-07-30 | Include percezione dell'interfaccia e azioni. |
| `TOP-P11-CODE-AGENTS` | Agenti per software engineering | `ESTABLISHED` | capitolo | 2026-07-30 | Ambiente, test e repository state. |
| `TOP-P11-AGENT-ENVIRONMENTS` | Training degli agenti in ambienti interattivi | `FRONTIER` | capitolo candidato | 2026-07-30 | Collegamento con P09. |
| `TOP-P11-HUMAN-APPROVAL` | Human approval, autorizzazioni, sandbox e rollback | `CORE` | capitolo | 2026-07-30 | Contratto di sicurezza. |

# P12. Efficienza, inference e sistemi

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P12-DISTILLATION` | Knowledge, sequence e reasoning distillation | `CORE` | capitolo | 2026-07-30 | Distinguere target e objective. |
| `TOP-P12-PRUNING` | Pruning strutturato e non strutturato | `ESTABLISHED` | capitolo | 2026-07-30 | Misurare sparsità realmente sfruttabile. |
| `TOP-P12-SPARSEGPT-WANDA` | Pruning post-training di LLM | `ESTABLISHED` | confronto | 2026-07-30 | Casi di studio della famiglia. |
| `TOP-P12-PTQ` | Post-training quantization | `CORE` | capitolo | 2026-07-30 | Fondamento della compressione runtime. |
| `TOP-P12-QAT` | Quantization-aware training | `ESTABLISHED` | capitolo | 2026-07-30 | Training con simulazione della quantizzazione. |
| `TOP-P12-LLM-INT8` | Quantizzazione mixed-precision int8 | `ESTABLISHED` | confronto | 2026-07-30 | Outlier handling. |
| `TOP-P12-GPTQ` | GPTQ-style weight-only quantization | `ESTABLISHED` | confronto | 2026-07-30 | Metodo PTQ. |
| `TOP-P12-AWQ` | Activation-aware weight quantization | `ESTABLISHED` | confronto | 2026-07-30 | Salienza delle weight channel. |
| `TOP-P12-SMOOTHQUANT` | Smoothing per weight-activation quantization | `ESTABLISHED` | confronto | 2026-07-30 | Trasferimento degli outlier. |
| `TOP-P12-AQLM-QUIP` | Quantizzazione avanzata sub-4-bit | `ESTABLISHED` | approfondimento | 2026-07-30 | Verificare kernel e formato. |
| `TOP-P12-BITNET` | Reti a pesi estremamente ridotti e 1.58-bit | `FRONTIER` | capitolo candidato | 2026-07-30 | Separare training nativo e quantizzazione. |
| `TOP-P12-KV-QUANT` | Quantizzazione della KV cache | `ESTABLISHED` | capitolo | 2026-07-30 | Impatto su memoria e qualità. |
| `TOP-P12-SAMPLING` | Sampling, temperature e truncation | `CORE` | capitolo | 2026-07-30 | Decoding probabilistico. |
| `TOP-P12-CONSTRAINED-DECODING` | Grammar, schema e constrained decoding | `ESTABLISHED` | capitolo | 2026-07-30 | Collegamento con P11. |
| `TOP-P12-SPECULATIVE-DECODING` | Draft model e speculative decoding | `ESTABLISHED` | capitolo | 2026-07-30 | Verifica esatta e acceptance. |
| `TOP-P12-MEDUSA` | Head multiple per speculative decoding | `ESTABLISHED` | confronto | 2026-07-30 | Draft senza modello separato. |
| `TOP-P12-EAGLE` | Predizione speculativa nello spazio delle feature | `ESTABLISHED` | confronto | 2026-07-30 | Varianti versionate. |
| `TOP-P12-REDRAFTER` | Recurrent drafter e tree attention | `ESTABLISHED` | confronto | 2026-07-30 | Famiglia di drafting. |
| `TOP-P12-PARALLEL-DECODING` | Lookahead e parallel decoding | `FRONTIER` | approfondimento | 2026-07-30 | Contratto di esattezza da esplicitare. |
| `TOP-P12-DIFFUSION-DECODING` | Decoding iterativo non autoregressivo per language diffusion | `FRONTIER` | osservatorio | 2026-07-30 | Collegamento con P08. |
| `TOP-P12-PREFILL-DECODE` | Separazione delle fasi prefill e decode | `CORE` | capitolo | 2026-07-30 | Metriche e colli di bottiglia diversi. |
| `TOP-P12-KV-CACHE` | Allocazione e gestione della KV cache | `CORE` | capitolo | 2026-07-30 | Base del serving autoregressivo. |
| `TOP-P12-PAGED-ATTENTION` | Paged memory management e PagedAttention | `ESTABLISHED` | capitolo | 2026-07-30 | Riduzione della frammentazione. |
| `TOP-P12-CONTINUOUS-BATCHING` | Continuous batching e scheduling iterativo | `CORE` | capitolo | 2026-07-30 | Serving ad alto throughput. |
| `TOP-P12-PREFIX-CACHE` | Prefix caching e riuso dei prefissi | `ESTABLISHED` | capitolo | 2026-07-30 | Validità e invalidazione. |
| `TOP-P12-DISAGGREGATED-SERVING` | Disaggregazione prefill/decode | `ESTABLISHED` | capitolo | 2026-07-30 | Routing e rete diventano parte del costo. |
| `TOP-P12-DISTRIBUTED-INFERENCE` | Tensor, pipeline ed expert parallelism nel serving | `ESTABLISHED` | capitolo | 2026-07-30 | Distinguere training e inference. |
| `TOP-P12-SERVING-SCHEDULERS` | Scheduling, preemption e fairness | `ESTABLISHED` | capitolo | 2026-07-30 | Policy di sistema. |
| `TOP-P12-SGLANG-RADIX` | Runtime con prefix/radix caching e structured generation | `ESTABLISHED` | studio di caso | 2026-07-30 | Non trasformare il runtime in tassonomia. |
| `TOP-P12-COMPILERS` | XLA, MLIR, TVM, TorchInductor e compilazione dei grafi | `ESTABLISHED` | capitolo | 2026-07-30 | Famiglia di sistema. |
| `TOP-P12-TRITON` | Kernel programmabili e Triton | `ESTABLISHED` | capitolo | 2026-07-30 | Collegare algoritmo e layout. |
| `TOP-P12-FLASHINFER` | Kernel e primitive specializzate per LLM inference | `ESTABLISHED` | studio di caso | 2026-07-30 | Versionare API e hardware. |
| `TOP-P12-LOW-PRECISION-KERNELS` | FP8, FP4 e kernel hardware-specifici | `FRONTIER` | approfondimento | 2026-07-30 | Risultati dipendenti dall'hardware. |
| `TOP-P12-EDGE-ONDEVICE` | Edge e on-device inference | `ESTABLISHED` | capitolo | 2026-07-30 | Vincoli di memoria, energia e privacy. |
| `TOP-P12-LLMOPS` | Versionamento, tracing, observability e rollback | `CORE` | capitolo | 2026-07-30 | Sistema di produzione. |
| `TOP-P12-COST-ENERGY` | Costo, throughput, latenza ed energia | `CORE` | capitolo | 2026-07-30 | Metriche con setup dichiarato. |

# P13. Valutazione, interpretabilità, sicurezza e governance

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P13-EVAL-DESIGN` | Disegno della valutazione, rubriche e significatività | `CORE` | capitolo | 2026-07-30 | Prima dei benchmark specifici. |
| `TOP-P13-STATIC-DYNAMIC-BENCH` | Benchmark statici, dinamici e live | `ESTABLISHED` | capitolo | 2026-07-30 | Aggiornamento continuo. |
| `TOP-P13-CONTAMINATION` | Contaminazione, memorization e benchmark leakage | `CORE` | capitolo | 2026-07-30 | Provenienza dei dati. |
| `TOP-P13-LLM-JUDGE` | LLM-as-a-judge e pairwise evaluation | `ESTABLISHED` | capitolo | 2026-07-30 | Bias, posizione e self-preference. |
| `TOP-P13-FACTUALITY` | Fattualità, faithfulness e citation correctness | `CORE` | capitolo | 2026-07-30 | Distinguere proprietà. |
| `TOP-P13-CALIBRATION` | Calibrazione, abstention e selective prediction | `ESTABLISHED` | capitolo | 2026-07-30 | Decisioni sotto incertezza. |
| `TOP-P13-LONG-CONTEXT-EVAL` | Valutazione del contesto lungo | `ESTABLISHED` | capitolo | 2026-07-30 | Retrieval, posizione e distrattori. |
| `TOP-P13-RAG-EVAL` | Valutazione separata di retrieval e generation | `ESTABLISHED` | capitolo | 2026-07-30 | Grounding e coverage. |
| `TOP-P13-AGENT-EVAL` | Valutazione di traiettorie, tool use e ambienti | `FRONTIER` | capitolo candidato | 2026-07-30 | Costi, sicurezza e non determinismo. |
| `TOP-P13-MULTIMODAL-EVAL` | Valutazione multimodale e generativa | `ESTABLISHED` | capitolo | 2026-07-30 | Metriche specifiche per modalità. |
| `TOP-P13-PROBING-ATTRIBUTION` | Probing, attribution e feature visualization | `CORE` | capitolo | 2026-07-30 | Limiti delle correlazioni. |
| `TOP-P13-CAUSAL-TRACING` | Activation patching e causal tracing | `ESTABLISHED` | capitolo | 2026-07-30 | Interventi causali sul modello. |
| `TOP-P13-CIRCUITS` | Circuiti e analisi del residual stream | `ESTABLISHED` | capitolo | 2026-07-30 | Dalla componente al comportamento. |
| `TOP-P13-SAE` | Sparse autoencoder per decomposizione delle feature | `ESTABLISHED` | capitolo | 2026-07-30 | Interpretazione e validazione delle feature. |
| `TOP-P13-AUTO-INTERP` | Interpretabilità automatizzata e circuit tracing scalabile | `FRONTIER` | osservatorio | 2026-07-30 | Necessita benchmark di validità. |
| `TOP-P13-MOE-INTERP` | Interpretabilità di router ed expert | `FRONTIER` | approfondimento | 2026-07-30 | Specializzazione e routing. |
| `TOP-P13-ADVERSARIAL` | Adversarial example e robustezza | `CORE` | capitolo | 2026-07-30 | Famiglia generale. |
| `TOP-P13-JAILBREAK` | Jailbreak e universal adversarial suffix | `ESTABLISHED` | capitolo | 2026-07-30 | Attacco al comportamento. |
| `TOP-P13-PROMPT-INJECTION` | Prompt injection diretta e indiretta | `CORE` | capitolo | 2026-07-30 | Centrale nei sistemi con tool. |
| `TOP-P13-TOOL-SECURITY` | Esfiltrazione, confused deputy e autorizzazioni agentiche | `FRONTIER` | capitolo candidato | 2026-07-30 | Sistema, non solo modello. |
| `TOP-P13-POISONING-BACKDOOR` | Data poisoning, backdoor e model poisoning | `ESTABLISHED` | capitolo | 2026-07-30 | Supply chain del training. |
| `TOP-P13-MODEL-EXTRACTION` | Model extraction e stealing | `ESTABLISHED` | capitolo | 2026-07-30 | API e weight security. |
| `TOP-P13-SUPPLY-CHAIN` | Dipendenze, checkpoint, dataset e artifact security | `CORE` | capitolo | 2026-07-30 | Provenienza e integrità. |
| `TOP-P13-PRIVACY` | Memorizzazione, PII leakage e membership inference | `CORE` | capitolo | 2026-07-30 | Rischi dei dati. |
| `TOP-P13-DP` | Differential privacy e federated learning | `ESTABLISHED` | capitolo | 2026-07-30 | Utility-privacy trade-off. |
| `TOP-P13-UNLEARNING` | Machine unlearning per foundation model | `FRONTIER` | capitolo candidato | 2026-07-30 | Verifica dell'effettiva rimozione. |
| `TOP-P13-FAIRNESS` | Bias, fairness e accessibilità | `CORE` | capitolo | 2026-07-30 | Metriche e contesto d'uso. |
| `TOP-P13-WATERMARKING` | Watermarking dei contenuti generati | `ESTABLISHED` | capitolo | 2026-07-30 | Robustezza e falsi positivi. |
| `TOP-P13-PROVENANCE` | Content credentials e provenienza | `ESTABLISHED` | capitolo | 2026-07-30 | Standard e catena di custodia. |
| `TOP-P13-MODEL-DOCUMENTATION` | Model card, data card e system card | `CORE` | capitolo | 2026-07-30 | Documentazione del rischio. |
| `TOP-P13-GOVERNANCE` | Risk management, audit e governance | `CORE` | capitolo | 2026-07-30 | Processi organizzativi. |
| `TOP-P13-LAW` | Copyright, licenze, responsabilità e regolazione | `ESTABLISHED` | capitolo | 2026-07-30 | Verifica normativa per data e giurisdizione. |
| `TOP-P13-SUSTAINABILITY` | Energia, acqua, hardware e sostenibilità | `ESTABLISHED` | capitolo | 2026-07-30 | Dati quantitativi con setup. |

# P14. Laboratori, integrazione e osservatorio

| topic_id | Tema | Maturità | Destinazione | Ultima verifica | Note |
|---|---|---|---|---|---|
| `TOP-P14-FROM-SCRATCH` | Implementazioni minime dai fondamenti | `CORE` | laboratorio | 2026-07-30 | Verifica dei meccanismi. |
| `TOP-P14-SMALL-LM` | Costruzione di un piccolo language model | `CORE` | progetto | 2026-07-30 | Pipeline completa. |
| `TOP-P14-PRODUCTION-PROJECT` | RAG, tool, agenti, valutazione e deployment | `ESTABLISHED` | progetto | 2026-07-30 | Integrazione end-to-end. |
| `TOP-P14-REPLICATION` | Repliche controllate di paper e ablation | `CORE` | laboratorio | 2026-07-30 | Setup e risultati registrati. |
| `TOP-P14-MODEL-CASE-STUDIES` | Schede di modelli e technical report | `ESTABLISHED` | studi di caso | 2026-07-30 | Non sostituiscono i capitoli concettuali. |
| `TOP-P14-FRONTIER-OBSERVATORY` | Registro delle aree frontier | `FRONTIER` | osservatorio | 2026-07-30 | Mirror delle voci nelle parti funzionali. |
| `TOP-P14-OPEN-PROBLEMS` | Domande aperte e piani di verifica | `FRONTIER` | osservatorio | 2026-07-30 | Nessuna affermazione non verificata come fatto. |

# Regole di manutenzione

## Inserimento

Una nuova voce riceve:

- `topic_id` stabile;
- collocazione primaria;
- maturità iniziale;
- destinazione editoriale;
- data di verifica;
- fonti nel registro della ricerca o nel dossier del capitolo;
- condizioni di promozione quando `FRONTIER`.

## Promozione

La promozione aggiorna il badge e la profondità del trattamento. Non cambia automaticamente parte, ID o ordine.

## Modelli e prodotti

I nomi dei modelli non sono voci obbligatorie del catalogo. Vengono aggiunti soltanto come studi di caso o come fonte di un meccanismo distinto.

## Verifica periodica

Durante la produzione attiva:

- le voci `FRONTIER` vengono ricontrollate almeno ogni 90 giorni;
- le API e le specifiche vengono verificate quando entra in lavorazione il capitolo relativo;
- il catalogo viene riesaminato integralmente prima di ogni nuova edizione;
- ogni modifica sostanziale viene registrata in `15_REGISTRO_RICERCHE_APPROFONDITE.md`.

## Confine di completezza

La presenza nel catalogo non dimostra superiorità. L'assenza non dimostra irrilevanza. Una voce entra quando soddisfa i criteri di inclusione del protocollo e può essere collocata con sufficiente precisione.