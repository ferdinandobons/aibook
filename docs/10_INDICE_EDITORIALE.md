# Indice editoriale dell'opera

## Titolo di lavoro

**Intelligenza artificiale generativa**  
*Dai fondamenti matematici ai modelli multimodali, al reasoning, agli agenti e ai sistemi di produzione*

## Principio organizzativo

L'opera è divisa in due volumi. I capitoli sono organizzati per idee, problemi e meccanismi, non per singoli prodotti. Le famiglie di modelli e i sistemi contemporanei vengono usati come studi di caso verificati nelle sezioni pertinenti.

Le schede dedicate a modelli recenti devono riportare la data di verifica, la fonte ufficiale e la versione descritta. L'indice resta stabile, mentre gli studi di caso possono essere aggiornati senza cambiare la struttura concettuale.

# Volume I. Fondamenti, apprendimento e modelli generativi

## Parte I. Orientarsi nel campo dell'intelligenza artificiale

### Capitolo 1. Che cos'è l'intelligenza artificiale

- Intelligenza artificiale, machine learning, deep learning e AI generativa.
- Sistemi simbolici e statistici.
- Modelli discriminativi e generativi.
- Foundation model, modelli generalisti e specialistici.
- Training, inference, parametri e dati.

### Capitolo 2. Breve storia dell'AI

- Logica e primi programmi.
- Ricerca simbolica e sistemi esperti.
- Periodi di rallentamento della ricerca.
- Machine learning statistico.
- Connessionismo e deep learning.
- Foundation model, multimodalità e sistemi agentici.

### Capitolo 3. Come apprende una macchina

- Parametri e iperparametri.
- Addestramento e inferenza.
- Apprendimento supervisionato, non supervisionato, auto-supervisionato e per rinforzo.
- Generalizzazione, trasferimento e adattamento.
- Distribuzione dei dati e obiettivo di apprendimento.

### Capitolo 4. Come valutare criticamente un risultato di AI

- Train, validation e test set.
- Baseline, metriche ed esperimenti controllati.
- Ablation study.
- Significatività statistica.
- Correlazione e causalità.
- Riproducibilità.
- Contaminazione e saturazione dei benchmark.

## Parte II. Fondamenti matematici e computazionali

### Capitolo 5. Algebra lineare, vettori e tensori

- Scalari, vettori, matrici e tensori.
- Prodotti scalari e matriciali.
- Norme, proiezioni e cambi di base.
- Autovalori e autovettori.
- Decomposizione SVD.
- Batch, dimensioni, reshape e broadcasting.

### Capitolo 6. Calcolo differenziale e backpropagation

- Derivate e derivate parziali.
- Gradienti, Jacobiane e Hessiane.
- Regola della catena.
- Grafi computazionali.
- Differenziazione automatica.
- Derivazione progressiva della backpropagation.

### Capitolo 7. Probabilità, statistica e inferenza

- Variabili casuali e distribuzioni.
- Probabilità condizionata e teorema di Bayes.
- Valore atteso e varianza.
- Maximum likelihood e MAP.
- Campionamento.
- Intervalli di confidenza e test statistici.
- Introduzione all'inferenza causale.

### Capitolo 8. Teoria dell'informazione e funzioni obiettivo

- Entropia.
- Cross-entropy.
- Perplexity.
- Divergenza KL.
- Informazione mutua.
- Likelihood e log-likelihood.
- Loss supervisionate e auto-supervisionate.
- ELBO e obiettivi contrastivi.

### Capitolo 9. Ottimizzazione numerica e hardware

- Gradient descent, SGD, momentum, Adam e AdamW.
- Learning-rate schedule e warm-up.
- Gradient clipping e weight decay.
- Condizionamento numerico e stabilità.
- FP32, FP16, BF16 e formati a precisione ridotta.
- GPU, TPU, NPU, memoria, cache, banda e FLOP.
- Modello roofline e data movement.

## Parte III. AI classica e machine learning

### Capitolo 10. Ricerca, pianificazione e giochi

- Breadth-first search, depth-first search e uniform-cost search.
- A* ed euristiche.
- Constraint satisfaction.
- Minimax e alpha-beta pruning.
- Monte Carlo Tree Search.
- Pianificazione classica e collegamento con gli agenti moderni.

### Capitolo 11. Conoscenza, logica e modelli probabilistici

- Logica proposizionale e del primo ordine.
- Regole e ontologie.
- Knowledge graph e sistemi esperti.
- Reti bayesiane.
- Modelli di Markov e Hidden Markov Model.
- Ragionamento simbolico e probabilistico.

### Capitolo 12. Apprendimento supervisionato

- Regressione lineare e logistica.
- Classificazione multiclasse.
- k-nearest neighbours.
- Decision tree e random forest.
- Gradient boosting.
- Support vector machine.
- Class imbalance, feature engineering e calibrazione.

### Capitolo 13. Apprendimento non supervisionato e rappresentazioni

- Clustering e k-means.
- Gaussian mixture.
- PCA e riduzione dimensionale.
- Anomaly detection.
- Metric learning.
- Rappresentazioni latenti.
- Apprendimento auto-supervisionato e contrastivo.

### Capitolo 14. Reinforcement learning

- Processi decisionali di Markov.
- Stato, azione, reward e policy.
- Value function ed equazione di Bellman.
- Q-learning.
- Policy gradient.
- Actor-critic e PPO.
- Esplorazione, credit assignment e reward shaping.
- Collegamento con RLHF e reasoning model.

## Parte IV. Deep learning

### Capitolo 15. Dal percettrone alle reti multilayer

- Percettrone e neurone artificiale.
- MLP.
- Funzioni di attivazione.
- Capacità espressiva.
- Forward pass e classificazione.
- Implementazione di una rete minimale.

### Capitolo 16. Addestrare reti profonde

- Inizializzazione dei pesi.
- Vanishing ed exploding gradient.
- Batch normalization e layer normalization.
- Residual connection.
- Dropout, data augmentation ed early stopping.
- Regolarizzazione.
- Diagnosi di underfitting e overfitting.

### Capitolo 17. Convolutional network e apprendimento geometrico

- Convoluzioni, kernel e pooling.
- Receptive field.
- Architetture CNN.
- Equivarianza e bias induttivi.
- Introduzione alle Graph Neural Network.
- Message passing e rappresentazione dei grafi.

### Capitolo 18. Reti ricorrenti e modelli sequenziali

- RNN.
- Backpropagation through time.
- LSTM e GRU.
- Modelli sequence-to-sequence.
- Encoder-decoder.
- Teacher forcing.
- Limiti della ricorrenza e nascita dell'attention.

### Capitolo 19. Representation learning

- Autoencoder.
- Denoising e sparse autoencoder.
- Apprendimento contrastivo.
- Embedding condivisi.
- Metric learning.
- Transfer learning.
- Probing delle rappresentazioni interne.

## Parte V. Le principali famiglie di modelli generativi

### Capitolo 20. Fondamenti della modellazione generativa

- Stima di una distribuzione dei dati.
- Modelli espliciti e impliciti.
- Variabili latenti.
- Maximum likelihood.
- Sampling e conditional generation.
- Modelli energy-based.
- Qualità, diversità e copertura della distribuzione.

### Capitolo 21. Modelli autoregressivi

- Fattorizzazione della distribuzione.
- Predizione dell'elemento successivo.
- Teacher forcing ed exposure bias.
- Autoregressione per testo, immagini, audio e video.
- Generazione sequenziale e costo dell'inferenza.

### Capitolo 22. Variational Autoencoder

- Encoder probabilistico e decoder generativo.
- Spazio latente.
- ELBO.
- Reparameterization trick.
- Posterior collapse.
- VAE condizionali, gerarchici e discreti.
- VQ-VAE e tokenizzazione di immagini e audio.

### Capitolo 23. Generative Adversarial Network

- Generatore e discriminatore.
- Gioco minimax.
- Non-saturating loss.
- Wasserstein GAN e gradient penalty.
- Mode collapse e instabilità.
- GAN condizionali e architetture orientate allo stile.

### Capitolo 24. Normalizing flow

- Trasformazioni invertibili.
- Formula del cambio di variabili.
- Jacobiano.
- Coupling layer.
- Autoregressive flow.
- Continuous normalizing flow.
- Exact likelihood, espressività e vincoli computazionali.

### Capitolo 25. Diffusione, score matching e flow matching

- Processo forward e reverse.
- Denoising diffusion.
- Score function.
- Equazioni differenziali stocastiche.
- Latent diffusion.
- Classifier guidance e classifier-free guidance.
- Flow matching e rectified flow.
- Consistency model e distillazione del processo generativo.

## Parte VI. Linguaggio, attention e Transformer

### Capitolo 26. Il testo come dato

- Unicode e normalizzazione.
- Segmentazione.
- Parole, caratteri, byte e token.
- Byte Pair Encoding, WordPiece e Unigram Language Model.
- Tokenizzatori multilingue e per il codice.
- Limiti della tokenizzazione e modelli token-free.

### Capitolo 27. Embedding e spazio semantico

- One-hot encoding.
- Word embedding.
- Word2Vec.
- Rappresentazioni contestuali.
- Sentence embedding.
- Similarità coseno.
- Embedding posizionali e multimodali.

### Capitolo 28. Il meccanismo di attention

- Limite del vettore di contesto fisso.
- Query, key e value.
- Punteggi di compatibilità.
- Scaled dot-product attention.
- Softmax e combinazione pesata.
- Attention mask.
- Self-attention, cross-attention e causal self-attention.
- Multi-head attention.
- Shape, complessità e implementazione PyTorch.
- Varianti moderne introdotte dopo il caso base.

### Capitolo 29. Il Transformer da zero

- Multi-head attention.
- Feed-forward network.
- Residual stream.
- Normalizzazione.
- Positional encoding.
- Causal mask.
- Encoder e decoder.
- Implementazione progressiva di un Transformer minimale.

### Capitolo 30. Famiglie architetturali e obiettivi di preaddestramento

- Encoder-only.
- Decoder-only.
- Encoder-decoder.
- Masked language modeling.
- Causal language modeling.
- Span corruption e denoising.
- Sequence-to-sequence e prefix language modeling.

### Capitolo 31. Dalla rappresentazione linguistica agli LLM

- Famiglie storiche come studi di caso.
- Few-shot e in-context learning.
- Prompt, esempi nel contesto e istruzioni.
- Greedy decoding.
- Beam search.
- Temperature, top-k e top-p.
- Generazione vincolata.

## Parte VII. Costruire un foundation model

### Capitolo 32. Il ciclo di vita dei dati

- Acquisizione e licenze.
- Filtraggio e deduplicazione.
- Classificazione della qualità.
- Rimozione di PII e contenuti indesiderati.
- Contaminazione dei benchmark.
- Data provenance e documentazione.

### Capitolo 33. Dataset mixture, curriculum e dati sintetici

- Bilanciamento tra lingue, domini, codice e matematica.
- Sampling delle fonti.
- Curriculum learning.
- Generazione, filtraggio e verifica dei dati sintetici.
- Distillazione da modelli insegnanti.

### Capitolo 34. Scaling law e progettazione del modello

- Relazione tra parametri, token, dati e compute.
- Undertraining.
- Compute-optimal training.
- Scelta di profondità, larghezza e context length.
- Scaling experiment.
- Trasferimento degli iperparametri.
- Confronto dense-versus-sparse.

### Capitolo 35. La ricetta di preaddestramento

- Batch size.
- Learning rate, warm-up e scheduler.
- Optimizer.
- Gradient clipping.
- Precisione mista.
- Stabilità della loss.
- Checkpoint e recovery.
- Diagnosi di loss spike, divergenza e anomalie nei dati.

### Capitolo 36. Addestramento distribuito e continued pretraining

- Data parallelism.
- Tensor parallelism.
- Pipeline parallelism.
- Sequence, context ed expert parallelism.
- ZeRO.
- Activation checkpointing e offloading.
- Comunicazione tra acceleratori.
- Fault tolerance.
- Continued pretraining e adattamento di dominio.

# Volume II. Architetture moderne, multimodalità, agenti e produzione

## Parte VIII. Ottimizzazioni architetturali moderne

### Capitolo 37. Anatomia del blocco Transformer moderno

- Pre-norm e post-norm.
- RMSNorm.
- GELU, GLU e SwiGLU.
- Residual scaling.
- Weight tying.
- Profondità e larghezza.
- Stabilità dei modelli profondi.
- Adaptive computation ed early exit.

### Capitolo 38. Posizione e contesto lungo

- Positional embedding appresi e sinusoidali.
- Relative position.
- RoPE e ALiBi.
- Positional interpolation.
- Context extension.
- Local, sliding-window e global attention.
- Retrieval rispetto a contesto lungo.
- Valutazione della posizione dell'informazione nel contesto.

### Capitolo 39. Varianti dell'attention e KV cache

- Multi-head attention.
- Multi-query attention.
- Grouped-query attention.
- Attention con rappresentazioni latenti o compresse.
- Compressione di key e value.
- KV cache e memory footprint.
- Eviction e cache quantization.
- Cross-attention e attention gerarchica.

### Capitolo 40. Attention hardware-aware

- Data movement e tiling.
- FlashAttention.
- Riduzione delle letture e scritture in memoria.
- Kernel fusion.
- Sparse e block-sparse attention.
- Linear attention.
- Prefill e decode.
- Co-design tra algoritmo, memoria e acceleratore.

### Capitolo 41. Mixture of Experts

- Expert, router e gating.
- Top-k routing.
- Shared e routed expert.
- Load balancing.
- Capacity factor e token dropping.
- Expert parallelism.
- Costo di comunicazione.
- Instabilità, expert collapse e specializzazione.

### Capitolo 42. Oltre il Transformer puro

- Structured State-Space Model.
- S4 e Mamba come famiglie di studio.
- State-space duality.
- Recurrence lineari.
- Architetture ibride attention-SSM.
- Multi-token prediction.
- Modelli linguistici a diffusione.
- Memoria ricorrente ed esterna.
- Apprendimento al test time.

## Parte IX. Post-addestramento, allineamento e reasoning

### Capitolo 43. Supervised Fine-Tuning e instruction tuning

- Costruzione dei dati di istruzione.
- Conversazioni multi-turn.
- Chat template.
- Mascheramento della loss.
- Domain SFT.
- Bilanciamento delle capacità.
- Catastrophic forgetting e regressioni.

### Capitolo 44. Preferenze, reward model e RLHF

- Raccolta di confronti tra risposte.
- Modelli di ricompensa.
- Modello Bradley-Terry.
- PPO e vincolo KL.
- On-policy e off-policy.
- Reward hacking e overoptimization.
- Limiti del feedback umano.

### Capitolo 45. Ottimizzazione diretta delle preferenze

- DPO e metodi correlati.
- Reference policy.
- Preference pair.
- Chosen e rejected response.
- Dati sintetici di preferenza.
- Feedback generato da modelli.
- Critica, revisione e costituzioni comportamentali.

### Capitolo 46. Addestrare il reasoning

- Dati con passaggi intermedi.
- Decomposizione dei problemi.
- Process supervision e outcome supervision.
- Verifier e process reward model.
- Self-consistency.
- Dati sintetici, rejection sampling e distillazione del reasoning.

### Capitolo 47. Reinforcement learning e compute al momento dell'inferenza

- RL con reward verificabili.
- Metodi relativi a gruppi di risposte.
- Best-of-N.
- Ricerca e tree search.
- Adaptive thinking.
- Budget di reasoning.
- Distillazione da reasoning model.
- Controllabilità e conflitti tra capacità e comportamento.

## Parte X. AI multimodale e generazione oltre il testo

### Capitolo 48. Fondamenti della multimodalità

- Modalità e rappresentazioni condivise.
- Allineamento.
- Early, intermediate e late fusion.
- Dual encoder.
- Projector e cross-attention.
- Token multimodali.
- Dati interleaved e multimodal instruction tuning.

### Capitolo 49. Vision encoder e Vision-Language Model

- CNN e Vision Transformer.
- Apprendimento contrastivo testo-immagine.
- Vision encoder, projector e language model.
- Cross-attention dedicata e architetture native.
- OCR, grounding, document understanding e comprensione delle interfacce.

### Capitolo 50. Generazione e modifica delle immagini

- Text-to-image.
- Latent diffusion.
- Diffusion Transformer.
- Flow matching.
- Conditioning e guidance.
- Controlli strutturali.
- Inpainting, outpainting, editing e super-resolution.
- Valutazione della coerenza tra testo e immagine.

### Capitolo 51. Audio, parlato e musica

- Waveform e spettrogramma.
- Neural audio codec.
- Automatic speech recognition.
- Text-to-speech.
- Voice activity detection e diarization.
- Speaker representation.
- Audio language model.
- Generazione musicale e dialogo vocale in streaming.

### Capitolo 52. Video, 3D, spazio e mondo fisico

- Temporal attention.
- Video diffusion e video autoregressivo.
- Coerenza temporale e identità persistente.
- Rappresentazioni 3D e scene.
- Spatial intelligence.
- World model.
- Simulazione, pianificazione robotica ed embodied AI.

## Parte XI. Conoscenza esterna, RAG, strumenti e agenti

### Capitolo 53. Embedding e information retrieval

- Ricerca lessicale e semantica.
- BM25.
- Dense e hybrid retrieval.
- Approximate nearest neighbour.
- Bi-encoder e cross-encoder.
- Reranker.
- Chunking, metadati e vector database.

### Capitolo 54. Retrieval-Augmented Generation

- Ingestion e parsing.
- Indicizzazione.
- Retrieval.
- Costruzione del contesto.
- Generazione.
- Grounding e citazioni.
- Aggiornamento della conoscenza.
- Memoria parametrica e memoria esterna.

### Capitolo 55. RAG avanzato

- Query rewriting ed expansion.
- Decomposition.
- Multi-hop retrieval.
- Adaptive retrieval.
- Graph RAG e knowledge graph.
- Reranking.
- Context compression e deduplicazione.
- Agentic RAG.
- Valutazione separata di retrieval e generation.

### Capitolo 56. Uso degli strumenti e output strutturato

- Function calling.
- Generazione JSON basata su schema.
- Constrained decoding.
- Calcolatrici, motori di ricerca, database, API e ambienti di esecuzione.
- Tool selection e argument generation.
- Gestione degli errori.
- Protocolli di interoperabilità.

### Capitolo 57. Sistemi agentici

- Ciclo osservazione, decisione, azione e verifica.
- ReAct come studio di metodo.
- Pianificazione.
- Memoria episodica e semantica.
- Reflection e critique.
- Workflow deterministici e agenti autonomi.
- Sistemi multi-agent.
- Browser e computer use.
- Approvazione umana, sandboxing, autorizzazioni e rollback.
- Valutazione delle traiettorie.

## Parte XII. Adattamento, compressione, inference e produzione

### Capitolo 58. Fine-tuning efficiente

- Full fine-tuning.
- Adapter.
- Prompt tuning e prefix tuning.
- LoRA.
- Scelta del rank.
- QLoRA.
- Adapter multipli.
- Model merging.
- Continued learning e aggiornamento senza dimenticanza.

### Capitolo 59. Compressione dei modelli

- Knowledge distillation.
- Sequence-level distillation.
- Pruning strutturato e non strutturato.
- Quantizzazione post-training.
- Quantization-aware training.
- Weight-only e weight-activation quantization.
- Trade-off tra memoria, velocità e accuratezza.

### Capitolo 60. Decoding e accelerazione della generazione

- Greedy e beam search.
- Temperature, top-k e nucleus sampling.
- Repetition penalty.
- Structured e constrained decoding.
- Speculative decoding.
- Draft model e strategie ad albero.
- Multi-token prediction.
- Generazione non autoregressiva.

### Capitolo 61. Serving degli LLM

- Prefill e decode.
- Time to first token e inter-token latency.
- KV cache.
- Prefix caching.
- Continuous batching.
- Paged memory management.
- Scheduling e preemption.
- Separazione di prefill e decode.

### Capitolo 62. Sistemi di produzione e LLMOps

- Inference distribuita.
- Tensor e pipeline parallelism nel serving.
- Edge e on-device AI.
- API gateway, caching e rate limiting.
- Versionamento di modello, prompt e dati.
- Tracing e observability.
- Valutazioni online e A/B test.
- Fallback e rollback.
- Throughput, latenza, costo ed energia.

## Parte XIII. Valutazione, interpretabilità, sicurezza e governance

### Capitolo 63. Progettare una valutazione

- Capacità da misurare.
- Benchmark statici e dinamici.
- Valutazione automatica, umana e con modelli giudici.
- Rubriche.
- Pairwise comparison.
- Significatività statistica.
- Contaminazione e cherry-picking.

### Capitolo 64. Fattualità, incertezza e affidabilità

- Hallucination e confabulation.
- Faithfulness rispetto alle fonti.
- Precisione fattuale e correttezza delle citazioni.
- Calibrazione.
- Abstention e selective prediction.
- Valutazione del contesto lungo, RAG, tool e agenti.

### Capitolo 65. Interpretabilità

- Feature visualization.
- Probing e attribution.
- Activation patching e causal tracing.
- Circuiti e residual stream.
- Sparse autoencoder e decomposizione delle feature.
- Interpretabilità dei router MoE.
- Limiti delle spiegazioni post hoc.

### Capitolo 66. Robustezza e sicurezza offensiva

- Adversarial example.
- Jailbreak e prompt injection.
- Indirect prompt injection.
- Esfiltrazione attraverso tool.
- Data poisoning, backdoor e model poisoning.
- Model extraction.
- Supply-chain risk.
- Sandboxing, permission model, red teaming e incident response.

### Capitolo 67. Privacy, equità e provenienza

- Memorizzazione dei dati.
- PII leakage.
- Membership inference.
- Differential privacy e federated learning.
- Bias, fairness e accessibilità.
- Watermarking, content credentials e provenienza dei contenuti.

### Capitolo 68. Diritto, governance e impatto sociale

- Copyright e licenze.
- Proprietà degli output e responsabilità.
- Model card, data card e system card.
- Audit e risk management.
- Regolazione nei diversi settori.
- Impatto sul lavoro, concentrazione tecnologica e accesso.
- Consumo energetico e sostenibilità.

## Parte XIV. Laboratori, progetti e frontiera della ricerca

### Capitolo 69. Percorso pratico dai fondamenti

- Regressione e backpropagation da zero.
- MLP, CNN e RNN.
- Attention.
- VAE, GAN e piccolo modello di diffusione.
- Transformer minimale.

### Capitolo 70. Costruire un piccolo language model

- Dataset.
- Tokenizer.
- Pretraining.
- Valutazione.
- Instruction tuning.
- LoRA.
- Quantizzazione.
- Esportazione e serving locale.
- Analisi sistematica degli errori.

### Capitolo 71. Progetto di produzione completo

- RAG con citazioni.
- Tool calling.
- Agente con autorizzazioni.
- Input multimodale.
- Suite di valutazione.
- Osservabilità.
- Sicurezza contro prompt injection.
- Ottimizzazione di costo e latenza.
- Deployment e rollback.

### Capitolo 72. Frontiere e domande aperte

- Architetture ibride e sparse.
- Modelli linguistici a diffusione.
- Memoria persistente e apprendimento continuo.
- Native multimodality.
- World model ed embodied AI.
- Neuro-symbolic AI.
- Dimostrazione formale e verifier.
- Data efficiency.
- Self-improving system.
- Limiti dello scaling.
- Lettura e verifica di technical report recenti.

# Appendici

## Appendice A. Python, NumPy e PyTorch essenziali

## Appendice B. JAX, compilazione e trasformazioni funzionali

## Appendice C. Formulario matematico

## Appendice D. Complessità computazionale delle principali architetture

## Appendice E. Glossario italiano-inglese

## Appendice F. Schede comparative di dataset e benchmark

## Appendice G. Schede architetturali dei principali modelli

## Appendice H. Checklist per riproducibilità, sicurezza e deployment

## Appendice I. Soluzioni degli esercizi

## Appendice J. Cronologia dei paper fondamentali

## Appendice K. Guida alla lettura critica di paper e technical report

# Struttura interna ricorrente dei capitoli

Ogni capitolo adatta il template canonico e include, quando pertinenti:

1. problema;
2. intuizione operativa senza formule;
3. esempio continuo;
4. formalismo matematico;
5. pseudocodice;
6. snippet eseguibile;
7. shape e strutture dati;
8. complessità, memoria e stabilità;
9. trade-off e ablation;
10. failure mode e confini;
11. visuali sottoposte ad audit;
12. esercizi e controlli di comprensione;
13. fonti, claim e registri di review.

# Regola di aggiornamento

L'indice può essere modificato soltanto tramite una decisione registrata in `08_REGISTRO_DECISIONI.md`. Nuovi modelli o tecniche vengono inizialmente inseriti come studi di caso nella sezione concettuale appropriata. Si crea un nuovo capitolo soltanto quando il nuovo argomento introduce un problema o un meccanismo che non può essere spiegato correttamente nella struttura esistente.