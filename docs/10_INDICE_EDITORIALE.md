# Indice editoriale dell'opera

## Titolo di lavoro

**Intelligenza artificiale generativa**  
*Dai fondamenti matematici ai modelli multimodali, al reasoning, agli agenti e ai sistemi di produzione*

## Stato dell'indice

- Opera canonica: unica e continua
- Export possibili: volume unico, più tomi, sito o corso
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Architettura delle parti: `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Catalogo delle tecniche: `14_CATALOGO_STATO_ARTE.md`
- Numerazione visualizzata: edizione di lavoro, non ancora congelata

## Principio organizzativo

Le parti sono stabili e organizzate per funzione. I capitoli sono organizzati per problemi, meccanismi e contratti tecnici. I singoli modelli vengono usati come studi di caso e non determinano da soli la struttura.

Ogni capitolo ha un `chapter_id` semantico stabile. Il numero visualizzato può cambiare durante la preparazione di una nuova edizione. Le aggiunte future usano `order_key`, prerequisiti e collegamenti, senza rinominare o riordinare automaticamente le parti.

Le tecniche censite nel catalogo non devono diventare tutte capitoli autonomi. Una voce può essere trattata come sezione, approfondimento, confronto, studio di caso o osservatorio.

# P01. Campo, metodo e storia dell'AI

## Capitolo 1. Che cos'è l'intelligenza artificiale

- `chapter_id`: `CH-P01-AI-FIELD`
- AI, machine learning, deep learning e AI generativa.
- Sistemi simbolici, statistici e neurali.
- Modelli discriminativi e generativi.
- Foundation model, modelli generalisti e specialistici.
- Training, inference, parametri e dati.

## Capitolo 2. Storia delle idee e dei sistemi di AI

- `chapter_id`: `CH-P01-HISTORY`
- Logica, ricerca e primi programmi.
- Sistemi esperti e modelli probabilistici.
- Machine learning statistico e connessionismo.
- Deep learning, foundation model e sistemi multimodali.
- Distinzione tra storia documentata e ricostruzioni retrospettive.

## Capitolo 3. Come apprende una macchina

- `chapter_id`: `CH-P01-LEARNING-OVERVIEW`
- Parametri e iperparametri.
- Obiettivi e distribuzioni dei dati.
- Apprendimento supervisionato, non supervisionato, auto-supervisionato e per rinforzo.
- Generalizzazione, trasferimento e adattamento.

## Capitolo 4. Come valutare criticamente un risultato di AI

- `chapter_id`: `CH-P01-CRITICAL-EVALUATION`
- Train, validation e test set.
- Baseline, metriche, ablation e significatività.
- Correlazione e causalità.
- Riproducibilità, contaminazione e saturazione dei benchmark.

# P02. Matematica, informazione e calcolo

## Capitolo 5. Algebra lineare, vettori e tensori

- `chapter_id`: `CH-P02-LINEAR-ALGEBRA`
- Scalari, vettori, matrici e tensori.
- Prodotti, norme, proiezioni e cambi di base.
- Autovalori, autovettori e SVD.
- Shape, batch, reshape e broadcasting.

## Capitolo 6. Calcolo differenziale e backpropagation

- `chapter_id`: `CH-P02-CALCULUS-BACKPROP`
- Derivate, gradienti, Jacobiane e Hessiane.
- Regola della catena.
- Grafi computazionali e autodiff.
- Backpropagation derivata passo per passo.

## Capitolo 7. Probabilità, statistica e inferenza

- `chapter_id`: `CH-P02-PROBABILITY`
- Variabili casuali e distribuzioni.
- Probabilità condizionata e Bayes.
- Valore atteso e varianza.
- Maximum likelihood, MAP, sampling e test statistici.

## Capitolo 8. Teoria dell'informazione e funzioni obiettivo

- `chapter_id`: `CH-P02-INFORMATION-THEORY`
- Entropia, cross-entropy, perplexity e KL.
- Informazione mutua.
- Likelihood, ELBO e obiettivi contrastivi.

## Capitolo 9. Calcolo numerico, precisione e hardware

- `chapter_id`: `CH-P02-NUMERICS-HARDWARE`
- Condizionamento e stabilità numerica.
- FP32, FP16, BF16, FP8 e formati ridotti.
- GPU, TPU, NPU, memoria, cache, banda e FLOP.
- Roofline model e data movement.

# P03. Apprendimento, ottimizzazione e decisione

## Capitolo 10. Ricerca, pianificazione e giochi

- `chapter_id`: `CH-P03-SEARCH-PLANNING`
- Ricerca non informata e A*.
- Constraint satisfaction.
- Minimax, alpha-beta e MCTS.
- Pianificazione classica e collegamenti con i sistemi agentici.

## Capitolo 11. Conoscenza, logica e modelli probabilistici

- `chapter_id`: `CH-P03-KNOWLEDGE-LOGIC`
- Logica proposizionale e del primo ordine.
- Regole, ontologie e knowledge graph.
- Reti bayesiane e modelli di Markov.

## Capitolo 12. Apprendimento supervisionato

- `chapter_id`: `CH-P03-SUPERVISED`
- Regressione, classificazione e calibrazione.
- Decision tree, random forest e gradient boosting.
- Support vector machine e class imbalance.

## Capitolo 13. Apprendimento non supervisionato e auto-supervisionato

- `chapter_id`: `CH-P03-UNSUPERVISED-SELF`
- Clustering, mixture model e PCA.
- Anomaly detection.
- Metric learning e obiettivi auto-supervisionati.

## Capitolo 14. Reinforcement learning

- `chapter_id`: `CH-P03-RL`
- MDP, value function ed equazione di Bellman.
- Q-learning, policy gradient e actor-critic.
- PPO, esplorazione, credit assignment e reward design.

# P04. Reti neurali e rappresentazioni

## Capitolo 15. Dal percettrone alle reti multilayer

- `chapter_id`: `CH-P04-MLP`
- Percettrone, MLP e funzioni di attivazione.
- Capacità espressiva e forward pass.
- Implementazione minimale.

## Capitolo 16. Addestrare reti profonde

- `chapter_id`: `CH-P04-DEEP-TRAINING`
- Inizializzazione.
- Vanishing ed exploding gradient.
- Normalizzazione, residual connection e regolarizzazione.
- Underfitting e overfitting.

## Capitolo 17. Convolutional network e apprendimento geometrico

- `chapter_id`: `CH-P04-CNN-GEOMETRIC`
- Convoluzione, pooling e receptive field.
- Equivarianza e bias induttivi.
- Graph neural network e message passing.

## Capitolo 18. Reti ricorrenti e modelli sequenziali

- `chapter_id`: `CH-P04-RECURRENT`
- RNN, BPTT, LSTM e GRU.
- Encoder-decoder e teacher forcing.
- Limiti della ricorrenza classica.

## Capitolo 19. Representation learning

- `chapter_id`: `CH-P04-REPRESENTATION`
- Autoencoder, denoising e sparse autoencoder.
- Apprendimento contrastivo e metric learning.
- Transfer learning e probing.

# P05. Modellazione generativa

## Capitolo 20. Fondamenti della modellazione generativa

- `chapter_id`: `CH-P05-GENERATIVE-FOUNDATIONS`
- Distribuzioni dei dati, modelli espliciti e impliciti.
- Variabili latenti, likelihood e sampling.
- Qualità, diversità e copertura.

## Capitolo 21. Modelli autoregressivi

- `chapter_id`: `CH-P05-AUTOREGRESSIVE`
- Fattorizzazione della distribuzione.
- Teacher forcing ed exposure bias.
- Autoregressione per testo, immagini, audio e video.

## Capitolo 22. Variational Autoencoder e latent discreti

- `chapter_id`: `CH-P05-VAE-VQ`
- ELBO e reparameterization trick.
- Posterior collapse.
- VAE gerarchici e VQ-VAE.

## Capitolo 23. Generative Adversarial Network

- `chapter_id`: `CH-P05-GAN`
- Gioco minimax e non-saturating loss.
- Wasserstein objective e gradient penalty.
- Mode collapse, stabilità e condizionamento.

## Capitolo 24. Normalizing flow e trasformazioni invertibili

- `chapter_id`: `CH-P05-FLOWS`
- Change of variables e Jacobiano.
- Coupling layer, autoregressive flow e continuous flow.
- Exact likelihood e vincoli computazionali.

## Capitolo 25. Diffusione, score matching e flow matching

- `chapter_id`: `CH-P05-DIFFUSION-FLOW`
- Processo forward e reverse.
- Score-based modeling e SDE.
- Latent diffusion, guidance, flow matching e rectified flow.
- Consistency model e distillazione del sampler.

# P06. Sequenze, linguaggio e contesto

## Capitolo 26. Il testo come dato

- `chapter_id`: `CH-P06-TEXT-DATA`
- Unicode, normalizzazione e segmentazione.
- Parole, caratteri, byte e token.
- BPE, WordPiece, Unigram e modelli token-free.

## Capitolo 27. Embedding e spazio semantico

- `chapter_id`: `CH-P06-EMBEDDINGS`
- One-hot, word embedding e Word2Vec.
- Rappresentazioni contestuali e sentence embedding.
- Similarità e spazi condivisi.

## Capitolo 28. Il meccanismo di attention

- `chapter_id`: `CH-P06-ATTENTION`
- Query, key e value.
- Score, scaling, mask, softmax e combinazione delle value.
- Self, cross e causal attention.
- Multi-head attention, shape, complessità e PyTorch.

## Capitolo 29. Il Transformer da zero

- `chapter_id`: `CH-P06-TRANSFORMER`
- Blocco attention e feed-forward.
- Residual stream, normalizzazione e positional information.
- Encoder, decoder e implementazione progressiva.

## Capitolo 30. Famiglie architetturali e obiettivi di pretraining

- `chapter_id`: `CH-P06-PRETRAIN-FAMILIES`
- Encoder-only, decoder-only ed encoder-decoder.
- Causal, masked, span-corruption e denoising objectives.

## Capitolo 31. Dalla rappresentazione linguistica agli LLM

- `chapter_id`: `CH-P06-LLM-BEHAVIOR`
- Few-shot e in-context learning.
- Prompt e istruzioni.
- Decoding di base e generazione vincolata introduttiva.

# P07. Dati, pretraining e scaling

## Capitolo 32. Il ciclo di vita dei dati

- `chapter_id`: `CH-P07-DATA-LIFECYCLE`
- Acquisizione, licenze, filtraggio e deduplicazione.
- Qualità, PII, contaminazione e provenance.

## Capitolo 33. Dataset mixture, curriculum e dati sintetici

- `chapter_id`: `CH-P07-DATA-MIXTURE`
- Bilanciamento di lingue e domini.
- Curriculum e data scheduling.
- Generazione, filtraggio e verifica dei dati sintetici.

## Capitolo 34. Scaling law e progettazione del modello

- `chapter_id`: `CH-P07-SCALING`
- Parametri, token, dati e compute.
- Compute-optimal training.
- Profondità, larghezza, context length e parameterization.

## Capitolo 35. La ricetta di pretraining

- `chapter_id`: `CH-P07-PRETRAIN-RECIPE`
- Batch, optimizer, warm-up e schedule.
- Precisione mista, loss spike, checkpoint e recovery.

## Capitolo 36. Training distribuito e continued pretraining

- `chapter_id`: `CH-P07-DISTRIBUTED-TRAINING`
- Data, tensor, pipeline, sequence, context ed expert parallelism.
- ZeRO, FSDP, activation checkpointing e offload.
- Continued pretraining e domain adaptation.

# P08. Progettazione delle architetture

## Capitolo 37. Anatomia del blocco moderno

- `chapter_id`: `CH-P08-MODERN-BLOCK`
- Pre-norm e post-norm.
- RMSNorm, GLU, GEGLU e SwiGLU.
- Residual scaling, weight tying, profondità e stabilità.

## Capitolo 38. Posizione e contesto lungo

- `chapter_id`: `CH-P08-POSITION-CONTEXT`
- Posizione assoluta e relativa.
- RoPE, ALiBi, positional interpolation, YaRN e LongRoPE.
- Training nativo, estensione e valutazione del contesto.

## Capitolo 39. Varianti dell'attention e gestione KV

- `chapter_id`: `CH-P08-ATTENTION-KV`
- MHA, MQA, GQA e latent attention.
- Compressione, quantizzazione ed eviction della KV cache.
- Local, sliding-window, block-sparse e ring attention.

## Capitolo 40. Attention hardware-aware

- `chapter_id`: `CH-P08-HARDWARE-AWARE-ATTENTION`
- Tiling e data movement.
- FlashAttention e implementazioni esatte IO-aware.
- Kernel fusion e co-design con l'acceleratore.

## Capitolo 41. Linear attention, fast weights e delta rule

- `chapter_id`: `CH-P08-LINEAR-ATTENTION`
- Kernel feature map e forma ricorrente.
- Fast-weight memory.
- Delta rule, gating e varianti moderne.

## Capitolo 42. State-space model, recurrence e long convolution

- `chapter_id`: `CH-P08-SEQUENCE-ALTERNATIVES`
- S4, selective SSM e state-space duality.
- Mamba e successive evoluzioni.
- RetNet, RWKV, Hyena, xLSTM e recurrence gated.

## Capitolo 43. Architetture ibride e memoria interna

- `chapter_id`: `CH-P08-HYBRID-MEMORY`
- Ibridi attention, SSM, convolution e recurrence.
- Neural memory e memory layers.
- Test-time learning interno al modello.

## Capitolo 44. Mixture of Experts e calcolo condizionale

- `chapter_id`: `CH-P08-MOE-CONDITIONAL`
- Expert, router, gating e load balancing.
- Shared expert, routing fine-grained ed expert parallelism.
- Upcycling, early exit e Mixture-of-Depths.

## Capitolo 45. Byte, predizione multi-token e language diffusion

- `chapter_id`: `CH-P08-ALTERNATIVE-PREDICTION`
- Byte-level e patch multiscala.
- Multi-token prediction e draft head.
- Diffusion language model e paradigmi ibridi.

# P09. Adattamento, allineamento e ragionamento

## Capitolo 46. Supervised fine-tuning e instruction tuning

- `chapter_id`: `CH-P09-SFT`
- Dati di istruzione, chat template e multi-turn.
- Loss masking, domain SFT e regressioni.

## Capitolo 47. Fine-tuning efficiente

- `chapter_id`: `CH-P09-PEFT`
- Adapter, prompt tuning, prefix tuning e IA3.
- LoRA, QLoRA, DoRA e scelta del rank.

## Capitolo 48. Preferenze, reward model e RLHF

- `chapter_id`: `CH-P09-RLHF`
- Raccolta delle preferenze e reward modeling.
- PPO, vincolo KL, reward hacking e overoptimization.
- RLAIF e feedback costituzionale.

## Capitolo 49. Ottimizzazione diretta delle preferenze

- `chapter_id`: `CH-P09-PREFERENCE-OPT`
- DPO e famiglia di obiettivi diretti.
- IPO, KTO, ORPO, SimPO e metodi online.
- Condizioni di confronto e limiti.

## Capitolo 50. Process supervision, outcome supervision e verifier

- `chapter_id`: `CH-P09-SUPERVISION-VERIFIERS`
- Supervisione dei passaggi e dell'esito.
- Process reward model e verifier.
- Dati sintetici e rejection sampling.

## Capitolo 51. Reinforcement learning con reward verificabili

- `chapter_id`: `CH-P09-RLVR`
- Reward verificabili.
- Group-relative optimization e varianti.
- Ambienti matematici, di codice e interattivi.

## Capitolo 52. Addestrare e distillare il reasoning

- `chapter_id`: `CH-P09-REASONING-TRAINING`
- Traiettorie intermedie e decomposizione.
- Distillazione, self-consistency e critica.
- Capacità, stile di output e controllabilità.

## Capitolo 53. Test-time compute, ricerca e controllo del budget

- `chapter_id`: `CH-P09-TEST-TIME-COMPUTE`
- Best-of-N, reranking e verifier.
- Tree search e adaptive thinking.
- Budget di compute e trade-off costo-qualità.

## Capitolo 54. Aggiornamento, merging ed editing del modello

- `chapter_id`: `CH-P09-MODEL-UPDATE`
- Model merging e task arithmetic.
- Model editing localizzato.
- Continual adaptation e catastrophic forgetting.

# P10. Multimodalità e modelli del mondo

## Capitolo 55. Fondamenti della multimodalità

- `chapter_id`: `CH-P10-MULTIMODAL-FOUNDATIONS`
- Allineamento e rappresentazioni condivise.
- Early, intermediate e late fusion.
- Token multimodali e dati interleaved.

## Capitolo 56. Vision encoder e Vision-Language Model

- `chapter_id`: `CH-P10-VLM`
- CNN, ViT e contrastive alignment.
- Projector, Q-Former e cross-attention.
- OCR, grounding e document understanding.

## Capitolo 57. Generazione e modifica delle immagini

- `chapter_id`: `CH-P10-IMAGE-GENERATION`
- Latent diffusion, DiT e flow matching.
- Conditioning, guidance e controlli strutturali.
- Inpainting, outpainting, editing e super-resolution.

## Capitolo 58. Modelli multimodali nativi e any-to-any

- `chapter_id`: `CH-P10-NATIVE-MULTIMODAL`
- Early fusion e vocabolari unificati.
- Understanding e generation nello stesso modello.
- Output multipli e streaming multimodale.

## Capitolo 59. Audio, parlato e musica

- `chapter_id`: `CH-P10-AUDIO`
- Waveform, spettrogramma e neural codec.
- ASR, TTS, audio language model e dialogo streaming.
- Generazione musicale.

## Capitolo 60. Generazione video

- `chapter_id`: `CH-P10-VIDEO`
- Temporal attention, autoregression, diffusion e flow.
- Coerenza temporale, identità persistente e controllo.

## Capitolo 61. 3D, spazio e rappresentazione delle scene

- `chapter_id`: `CH-P10-SPATIAL-3D`
- NeRF, Gaussian splatting e scene representation.
- Grounding spaziale e generazione 3D.

## Capitolo 62. World model, embodied AI e vision-language-action

- `chapter_id`: `CH-P10-WORLD-EMBODIED`
- Modelli di dinamica e simulazione.
- Pianificazione nel mondo fisico.
- Vision-language-action e controllo robotico.

# P11. Conoscenza esterna, memoria e azione

## Capitolo 63. Information retrieval

- `chapter_id`: `CH-P11-RETRIEVAL`
- Ricerca lessicale, densa e ibrida.
- ANN, bi-encoder, late interaction e reranking.

## Capitolo 64. Retrieval-Augmented Generation

- `chapter_id`: `CH-P11-RAG`
- Ingestion, parsing, indicizzazione e retrieval.
- Costruzione del contesto, grounding e citazioni.

## Capitolo 65. RAG adattivo, correttivo e basato su grafi

- `chapter_id`: `CH-P11-ADVANCED-RAG`
- Query transformation e multi-hop retrieval.
- Self-RAG, corrective RAG, RAPTOR e Graph RAG.
- Context compression e deduplicazione.

## Capitolo 66. Contesto lungo, retrieval e memoria

- `chapter_id`: `CH-P11-CONTEXT-RETRIEVAL-MEMORY`
- Decisione tra contesto lungo e retrieval.
- Memoria parametrica, episodica, semantica ed esterna.
- Persistenza, forgetting e privacy.

## Capitolo 67. Output strutturato e uso degli strumenti

- `chapter_id`: `CH-P11-TOOLS`
- Function calling e schema.
- Tool selection, argument generation e gestione degli errori.
- Calcolatrici, database, browser e ambienti di esecuzione.

## Capitolo 68. Protocolli e interoperabilità

- `chapter_id`: `CH-P11-INTEROPERABILITY`
- Contratti tra modello, tool e risorse.
- Model Context Protocol e protocolli agent-to-agent.
- Versionamento, autorizzazioni e discovery.

## Capitolo 69. Ciclo agentico, pianificazione e verifica

- `chapter_id`: `CH-P11-AGENT-LOOP`
- Osservazione, decisione, azione e verifica.
- ReAct, planning, reflection e critique.
- Workflow deterministici e autonomia.

## Capitolo 70. Multi-agent, browser, computer e code agents

- `chapter_id`: `CH-P11-AGENT-SYSTEMS`
- Coordinamento multi-agent.
- Browser e computer use.
- Agenti per software engineering.

## Capitolo 71. Training e valutazione degli agenti

- `chapter_id`: `CH-P11-AGENT-TRAINING-EVAL`
- Ambienti interattivi e traiettorie.
- Reward, curriculum e simulazione.
- Success rate, costo, recovery e non determinismo.

## Capitolo 72. Sicurezza operativa degli agenti

- `chapter_id`: `CH-P11-AGENT-SAFETY`
- Human approval, permission model e sandbox.
- Secrets, esfiltrazione, rollback e incident response.

# P12. Efficienza, inference e sistemi

## Capitolo 73. Distillazione e pruning

- `chapter_id`: `CH-P12-DISTILLATION-PRUNING`
- Knowledge, sequence e reasoning distillation.
- Pruning strutturato, non strutturato e post-training.

## Capitolo 74. Quantizzazione

- `chapter_id`: `CH-P12-QUANTIZATION`
- PTQ e QAT.
- Weight-only e weight-activation quantization.
- GPTQ, AWQ, SmoothQuant e metodi sub-4-bit.

## Capitolo 75. Modelli low-bit nativi e co-design numerico

- `chapter_id`: `CH-P12-LOW-BIT-NATIVE`
- Training con pesi estremamente ridotti.
- Scale, accumulatori, kernel e hardware.
- Differenza tra training nativo e quantizzazione post hoc.

## Capitolo 76. Decoding e generazione vincolata

- `chapter_id`: `CH-P12-DECODING`
- Sampling, repetition control e stopping.
- Grammar, schema e constrained decoding.
- Generazione non autoregressiva introduttiva.

## Capitolo 77. Speculative e parallel decoding

- `chapter_id`: `CH-P12-SPECULATIVE-DECODING`
- Draft model, acceptance e verifica esatta.
- Medusa, EAGLE, recurrent drafter e tree attention.
- Lookahead e parallel decoding.

## Capitolo 78. KV cache e riuso del contesto

- `chapter_id`: `CH-P12-KV-CACHE`
- Layout, quantizzazione, eviction e offload.
- Prefix caching e condivisione dei prefissi.

## Capitolo 79. Serving, batching e scheduling

- `chapter_id`: `CH-P12-SERVING`
- Prefill, decode, TTFT e inter-token latency.
- Paged memory, continuous batching, scheduling e preemption.

## Capitolo 80. Serving disaggregato e inference distribuita

- `chapter_id`: `CH-P12-DISTRIBUTED-INFERENCE`
- Separazione prefill/decode.
- Tensor, pipeline ed expert parallelism.
- Routing, rete e fault tolerance.

## Capitolo 81. Compiler, kernel e runtime

- `chapter_id`: `CH-P12-COMPILERS-KERNELS`
- Graph compiler, MLIR, XLA e TorchInductor.
- Triton e kernel specializzati.
- Co-design tra algoritmo, layout e acceleratore.

## Capitolo 82. LLMOps, edge, costo ed energia

- `chapter_id`: `CH-P12-LLMOPS`
- Versionamento, tracing, observability e rollback.
- Edge e on-device AI.
- Throughput, latenza, costo ed energia.

# P13. Valutazione, interpretabilità, sicurezza e governance

## Capitolo 83. Progettare una valutazione

- `chapter_id`: `CH-P13-EVAL-DESIGN`
- Capacità, rubriche, baseline e significatività.
- Benchmark statici, dinamici e contaminazione.
- Valutazione umana e LLM-as-a-judge.

## Capitolo 84. Fattualità, incertezza e affidabilità

- `chapter_id`: `CH-P13-FACTUALITY`
- Factuality, faithfulness e citation correctness.
- Calibrazione, abstention e selective prediction.

## Capitolo 85. Valutare contesto lungo, RAG, multimodalità e agenti

- `chapter_id`: `CH-P13-SYSTEM-EVAL`
- Retrieval e generation separati.
- Posizione dell'informazione nel contesto.
- Traiettorie, tool, recovery e costo degli agenti.
- Metriche specifiche per modalità.

## Capitolo 86. Interpretabilità delle rappresentazioni e dei circuiti

- `chapter_id`: `CH-P13-INTERPRETABILITY`
- Probing, attribution e feature visualization.
- Activation patching, causal tracing e circuiti.

## Capitolo 87. Sparse autoencoder e interpretabilità scalabile

- `chapter_id`: `CH-P13-SAE-CIRCUIT-TRACING`
- Decomposizione delle feature.
- Auto-interpretation e circuit tracing.
- Router ed expert nei MoE.

## Capitolo 88. Robustezza, jailbreak e attacchi adversarial

- `chapter_id`: `CH-P13-ROBUSTNESS-JAILBREAK`
- Adversarial example e universal suffix.
- Jailbreak, red teaming e valutazione delle difese.

## Capitolo 89. Prompt injection e sicurezza dei tool

- `chapter_id`: `CH-P13-PROMPT-INJECTION`
- Prompt injection diretta e indiretta.
- Confused deputy, esfiltrazione e autorizzazioni.
- Sicurezza di browser, computer use e agenti.

## Capitolo 90. Poisoning, backdoor, extraction e supply chain

- `chapter_id`: `CH-P13-SUPPLY-CHAIN-SECURITY`
- Data e model poisoning.
- Backdoor, model extraction e checkpoint risk.
- Integrità di dataset, dipendenze e artefatti.

## Capitolo 91. Privacy, fairness e unlearning

- `chapter_id`: `CH-P13-PRIVACY-FAIRNESS`
- Memorizzazione, PII leakage e membership inference.
- Differential privacy e federated learning.
- Bias, fairness, accessibilità e machine unlearning.

## Capitolo 92. Watermarking e provenienza dei contenuti

- `chapter_id`: `CH-P13-PROVENANCE`
- Watermarking e detection.
- Content credentials, C2PA e catena di provenienza.

## Capitolo 93. Diritto, governance e sostenibilità

- `chapter_id`: `CH-P13-GOVERNANCE`
- Copyright, licenze, responsabilità e regolazione.
- Model card, data card, system card e risk management.
- Lavoro, accesso, concentrazione, energia e sostenibilità.

# P14. Laboratori, integrazione e osservatorio

## Capitolo 94. Percorso pratico dai fondamenti

- `chapter_id`: `CH-P14-FOUNDATIONS-LAB`
- Regressione, backpropagation, MLP, CNN e RNN.
- VAE, GAN, diffusion e attention.

## Capitolo 95. Costruire un piccolo language model

- `chapter_id`: `CH-P14-SMALL-LM`
- Dataset, tokenizer, pretraining e valutazione.
- Instruction tuning, adattamento, quantizzazione e serving.

## Capitolo 96. Progetto di produzione completo

- `chapter_id`: `CH-P14-PRODUCTION-PROJECT`
- RAG con citazioni.
- Tool calling, agente, input multimodale e valutazione.
- Sicurezza, observability, costo e rollback.

## Capitolo 97. Riprodurre e leggere un paper

- `chapter_id`: `CH-P14-REPLICATION`
- Domanda, baseline, modifica, setup e ablation.
- Riproduzione su scala ridotta.
- Divergenze tra paper, repository e risultati eseguiti.

## Capitolo 98. Osservatorio della frontiera

- `chapter_id`: `CH-P14-FRONTIER-OBSERVATORY`
- Mappa delle voci `FRONTIER` nelle parti funzionali.
- Cronologia delle promozioni e demozioni.
- Domande aperte, piani di verifica e candidati a nuovi capitoli.

# Appendici

- Appendice A. Python, NumPy e PyTorch essenziali.
- Appendice B. JAX, compilazione e trasformazioni funzionali.
- Appendice C. Formulario matematico.
- Appendice D. Complessità delle architetture.
- Appendice E. Glossario italiano-inglese.
- Appendice F. Dataset, benchmark e metriche.
- Appendice G. Schede di modelli e technical report.
- Appendice H. Checklist per riproducibilità, sicurezza e deployment.
- Appendice I. Soluzioni degli esercizi.
- Appendice J. Cronologia dei paper fondamentali.
- Appendice K. Guida alla lettura critica delle fonti.
- Appendice L. Registro delle edizioni, degli alias e delle migrazioni.

# Regole per gli aggiornamenti futuri

1. Le parti `P01`-`P14` non cambiano per l'arrivo di una nuova tecnica.
2. Una nuova voce viene prima registrata nel catalogo.
3. La collocazione usa il routing funzionale.
4. La maturità non determina la collocazione.
5. Un nuovo capitolo richiede una domanda didattica autonoma e fonti sufficienti.
6. `chapter_id` resta stabile; il numero visualizzato cambia solo tra edizioni.
7. Una voce `FRONTIER` rimane nella parte funzionale pertinente.
8. `P14` osserva la frontiera, ma non la usa come contenitore generico.
9. Split e merge richiedono alias, redirect e mappa di migrazione.
10. Ogni modifica strutturale aggiorna decisioni, catalogo, indice e audit documentale.