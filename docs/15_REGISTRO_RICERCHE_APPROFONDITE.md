# Registro delle ricerche approfondite

## Funzione

Questo documento registra le ricerche globali che modificano la tassonomia, il catalogo, l'indice o la maturità dei contenuti.

Le ricerche specifiche di un capitolo restano anche nel relativo `FONTI_PRIMARIE.md`. Questo registro non sostituisce il controllo puntuale delle fonti quando viene scritta una frase.

# DR-2026-07-30-01

## Stato

- ID: `DR-2026-07-30-01`
- Tipo: ricerca approfondita globale
- Data di chiusura: **30 luglio 2026**
- Ambito temporale dichiarato: fonti e documentazione individuate e ricontrollate fino alla data di chiusura
- Esito: tassonomia editoriale aggiornata e catalogo iniziale creato
- Documenti prodotti o modificati:
  - `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
  - `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
  - `14_CATALOGO_STATO_ARTE.md`;
  - `10_INDICE_EDITORIALE.md`;
  - `08_REGISTRO_DECISIONI.md`;
  - `../GUIDELINE.md`;
  - `../README.md`.

## Domanda della ricerca

Come organizzare un libro completo sull'AI generativa in modo che:

- le parti restino stabili quando compaiono nuove architetture;
- le tecniche recenti possano essere inserite senza rinominare o riordinare l'opera;
- la maturità possa cambiare da `FRONTIER` a `ESTABLISHED` o `CORE` senza spostare la collocazione primaria;
- le principali famiglie di architetture, training, post-training, multimodalità, agenti, inference e sicurezza siano censite alla data della ricerca;
- un sistema AI privo del contesto originario possa aggiornare il progetto seguendo regole esplicite.

## Criteri di inclusione

Una famiglia o tecnica è stata registrata quando soddisfaceva almeno questi criteri:

1. contributo tecnico distinguibile;
2. fonte primaria o documentazione ufficiale accessibile;
3. rilevanza per architettura, training, post-training, generazione, inference, valutazione o governance;
4. possibilità di descrivere input, operazione, output, invariante e confine;
5. collocazione determinabile nella tassonomia funzionale;
6. influenza, adozione o potenziale sufficiente per la maturità assegnata.

Una configurazione, un nome commerciale o una semplice combinazione di tecniche non è stata automaticamente trasformata in voce autonoma.

## Aree coperte

- fondamenti matematici e computazionali;
- famiglie generative;
- tokenizzazione, attention e Transformer;
- dati, scaling e distributed training;
- positional methods e contesto lungo;
- MQA, GQA, MLA e gestione KV;
- exact, sparse, local, ring e linear attention;
- SSM, recurrence, long convolution, fast weights e memory layers;
- MoE, routing, adaptive depth e conditional compute;
- language diffusion e predizione multi-token;
- PEFT, RLHF, preference optimization e RL con reward verificabili;
- reasoning, verifier e test-time compute;
- multimodalità, image, audio, video, 3D, world model ed embodied AI;
- retrieval, RAG, memoria, tool, protocolli e agenti;
- quantizzazione, pruning, distillazione e decoding accelerato;
- serving, cache, batching, disaggregazione, kernel e compiler;
- valutazione, interpretabilità, sicurezza, privacy, provenance e governance.

## Fonti primarie e ufficiali di riferimento

La lista seguente è un insieme di fonti seme usato per costruire la tassonomia. Ogni capitolo deve riaprire le fonti pertinenti e registrare sezioni, versioni e limiti nel proprio dossier.

### Attention, Transformer e contesto

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017, arXiv:1706.03762.
- Bahdanau et al., *Neural Machine Translation by Jointly Learning to Align and Translate*, arXiv:1409.0473.
- Shazeer, *Fast Transformer Decoding: One Write-Head is All You Need*, arXiv:1911.02150.
- Ainslie et al., *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*, arXiv:2305.13245.
- Su et al., *RoFormer: Enhanced Transformer with Rotary Position Embedding*, arXiv:2104.09864.
- Press et al., *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation*, arXiv:2108.12409.
- Peng et al., *YaRN: Efficient Context Window Extension of Large Language Models*, arXiv:2309.00071.
- Ding et al., *LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens*, arXiv:2402.13753.
- Liu et al., *Ring Attention with Blockwise Transformers for Near-Infinite Context*, arXiv:2310.01889.
- Dao et al., *FlashAttention*, arXiv:2205.14135.
- Dao, *FlashAttention-2*, arXiv:2307.08691.
- Shah et al., *FlashAttention-3*, arXiv:2407.08608.
- DeepSeek-AI, *DeepSeek-V2*, arXiv:2405.04434.

### State-space, recurrence e architetture ibride

- Gu et al., *Efficiently Modeling Long Sequences with Structured State Spaces*, arXiv:2111.00396.
- Gu e Dao, *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*, arXiv:2312.00752.
- Dao e Gu, *Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality*, arXiv:2405.21060.
- Mamba-3 research report, arXiv:2603.15569.
- Sun et al., *Retentive Network*, arXiv:2307.08621.
- Peng et al., *RWKV: Reinventing RNNs for the Transformer Era*, arXiv:2305.13048.
- Poli et al., *Hyena Hierarchy*, arXiv:2302.10866.
- Beck et al., *xLSTM: Extended Long Short-Term Memory*, arXiv:2405.04517.
- De et al., *Griffin: Mixing Gated Linear Recurrences with Local Attention*, arXiv:2402.19427.
- Yang et al., *Gated Delta Networks*, arXiv:2412.06464.
- *Gated DeltaNet-2*, arXiv:2602.21487.
- *Hybrid Linear Attention Done Right*, arXiv:2603.12201.
- Moonshot AI, *Kimi Linear*, arXiv:2510.26692.
- Behrouz et al., *Titans: Learning to Memorize at Test Time*, arXiv:2501.00663.

### MoE e conditional computation

- Shazeer et al., *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*, arXiv:1701.06538.
- Fedus et al., *Switch Transformers*, arXiv:2101.03961.
- Dai et al., *DeepSeekMoE*, arXiv:2401.06066.
- Raposo et al., *Mixture-of-Depths*, arXiv:2404.02258.
- DeepSeek-AI, *DeepSeek-V3 Technical Report*, arXiv:2412.19437.

### Tokenizzazione, byte e predizione

- Xue et al., *ByT5*, arXiv:2105.13626.
- Yu et al., *MEGABYTE*, arXiv:2305.07185.
- Meta AI, *Byte Latent Transformer*, arXiv:2412.09871.
- Gloeckle et al., *Better & Faster Large Language Models via Multi-token Prediction*, arXiv:2404.19737.

### Generazione, diffusion e flow

- Ho et al., *Denoising Diffusion Probabilistic Models*, arXiv:2006.11239.
- Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*, arXiv:2112.10752.
- Lipman et al., *Flow Matching for Generative Modeling*, arXiv:2210.02747.
- Peebles e Xie, *Scalable Diffusion Models with Transformers*, arXiv:2212.09748.
- Austin et al., *Structured Denoising Diffusion Models in Discrete State-Spaces*, arXiv:2107.03006.
- Li et al., *Diffusion-LM*, arXiv:2205.14217.
- Sahoo et al., *Simple and Effective Masked Diffusion Language Models*, arXiv:2406.07524.
- Nie et al., *Large Language Diffusion Models*, arXiv:2502.09992.

### Scaling, dati e training

- Kaplan et al., *Scaling Laws for Neural Language Models*, arXiv:2001.08361.
- Hoffmann et al., *Training Compute-Optimal Large Language Models*, arXiv:2203.15556.
- Yang et al., *Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer*, arXiv:2203.03466.
- Shoeybi et al., *Megatron-LM*, arXiv:1909.08053.
- Rajbhandari et al., *ZeRO*, arXiv:1910.02054.
- PyTorch official documentation for distributed training, FSDP, mixed precision and current APIs.

### Post-training, preferenze e reasoning

- Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, arXiv:2203.02155.
- Bai et al., *Constitutional AI*, arXiv:2212.08073.
- Rafailov et al., *Direct Preference Optimization*, arXiv:2305.18290.
- Azar et al., *A General Theoretical Paradigm to Understand Learning from Human Preferences*, arXiv:2310.12036.
- Ethayarajh et al., *KTO: Model Alignment as Prospect Theoretic Optimization*, arXiv:2402.01306.
- Hong et al., *ORPO*, arXiv:2403.07691.
- Meng et al., *SimPO*, arXiv:2405.14734.
- Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050.
- Shao et al., *DeepSeekMath*, arXiv:2402.03300.
- DeepSeek-AI, *DeepSeek-R1*, arXiv:2501.12948.
- Wang et al., *Self-Consistency Improves Chain of Thought Reasoning*, arXiv:2203.11171.
- Snell et al., *Scaling LLM Test-Time Compute Optimally*, arXiv:2408.03314.

### Multimodalità e world model

- Dosovitskiy et al., *An Image is Worth 16x16 Words*, arXiv:2010.11929.
- Radford et al., *Learning Transferable Visual Models From Natural Language Supervision*, arXiv:2103.00020.
- Alayrac et al., *Flamingo*, arXiv:2204.14198.
- Li et al., *BLIP-2*, arXiv:2301.12597.
- Liu et al., *Visual Instruction Tuning*, arXiv:2304.08485.
- Team Chameleon, *Chameleon*, arXiv:2405.09818.
- Girdhar et al., *ImageBind*, arXiv:2305.05665.
- Meta, *Movie Gen*, arXiv:2410.13720.
- Ha e Schmidhuber, *World Models*, arXiv:1803.10122.
- Hafner et al., *Mastering Diverse Domains through World Models*, arXiv:2301.04104.

### Retrieval, memoria, tool e agenti

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, arXiv:2005.11401.
- Karpukhin et al., *Dense Passage Retrieval*, arXiv:2004.04906.
- Khattab e Zaharia, *ColBERT*, arXiv:2004.12832.
- Gao et al., *Precise Zero-Shot Dense Retrieval without Relevance Labels*, arXiv:2212.10496.
- Asai et al., *Self-RAG*, arXiv:2310.11511.
- Sarthi et al., *RAPTOR*, arXiv:2401.18059.
- Yao et al., *ReAct*, arXiv:2210.03629.
- Schick et al., *Toolformer*, arXiv:2302.04761.
- Packer et al., *MemGPT*, arXiv:2310.08560.
- Yang et al., *SWE-agent*, arXiv:2405.15793.
- Specifiche ufficiali versionate per Model Context Protocol e protocolli agent-to-agent.

### Adattamento, compressione, decoding e serving

- Hu et al., *LoRA*, arXiv:2106.09685.
- Dettmers et al., *QLoRA*, arXiv:2305.14314.
- Frantar et al., *GPTQ*, arXiv:2210.17323.
- Xiao et al., *SmoothQuant*, arXiv:2211.10438.
- Lin et al., *AWQ*, arXiv:2306.00978.
- Frantar e Alistarh, *SparseGPT*, arXiv:2301.00774.
- Sun et al., *A Simple and Effective Pruning Approach for Large Language Models*, arXiv:2306.11695.
- Leviathan et al., *Fast Inference from Transformers via Speculative Decoding*, arXiv:2211.17192.
- Chen et al., *Accelerating Large Language Model Decoding with Speculative Sampling*, arXiv:2302.01318.
- Cai et al., *Medusa*, arXiv:2401.10774.
- Li et al., *EAGLE*, arXiv:2401.15077.
- Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv:2309.06180.
- Zheng et al., *SGLang*, arXiv:2312.07104.
- Zhong et al., *DistServe*, arXiv:2401.09670.
- Documentazione ufficiale versionata di PyTorch, Triton e runtime di serving usati nei capitoli.

### Valutazione, interpretabilità e sicurezza

- Liang et al., *Holistic Evaluation of Language Models*, arXiv:2211.09110.
- Hendrycks et al., *Measuring Massive Multitask Language Understanding*, arXiv:2009.03300.
- Jimenez et al., *SWE-bench*, arXiv:2310.06770.
- Zou et al., *Universal and Transferable Adversarial Attacks on Aligned Language Models*, arXiv:2307.15043.
- Greshake et al., *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, arXiv:2302.12173.
- Abadi et al., *Deep Learning with Differential Privacy*, arXiv:1607.00133.
- Kirchenbauer et al., *A Watermark for Large Language Models*, arXiv:2301.10226.
- Documenti e repository ufficiali per circuit analysis, sparse autoencoder, model cards, C2PA e standard di provenance.

## Risultati strutturali della ricerca

### Opera unica

È stata sostituita la divisione canonica in due volumi con una sola opera continua. La divisione in tomi è diventata una scelta di export.

### Parti stabili

Sono state definite quattordici parti funzionali con ID da `P01` a `P14`. I nomi non contengono riferimenti a una generazione di modelli o a un periodo temporale specifico.

### Routing

Le novità vengono collocate in base all'oggetto modificato e al problema risolto. Le relazioni secondarie vengono mantenute tramite tag e cross-reference.

### Maturità

Sono stati definiti gli stati `CORE`, `ESTABLISHED` e `FRONTIER`. La maturità è separata dalla collocazione e può cambiare senza spostare la voce.

### Identità dei capitoli

È stato separato l'ID semantico stabile dal numero stampato specifico dell'edizione.

### Frontiera distribuita

Le voci frontier restano nella propria parte funzionale. `P14` conserva soltanto l'osservatorio, le repliche, la cronologia e le domande aperte.

## Limiti della ricerca

- La ricerca non dimostra l'assenza di altri lavori rilevanti.
- La classificazione di maturità è editoriale e deve essere riesaminata.
- Una fonte seme non autorizza a riportare ogni dettaglio senza riaprire il documento originale.
- I risultati quantitativi non vengono trasferiti nel libro senza setup, versione e verifica puntuale.
- API, standard, repository e normative devono essere ricontrollati alla data del capitolo.
- Le aree frontier possono cambiare rapidamente dopo la data di chiusura.

## Prossima revisione

Durante la produzione attiva:

- controllo locale prima di ogni capitolo;
- revisione delle voci `FRONTIER` entro 90 giorni dall'ultima verifica;
- ricerca globale prima della prima edizione congelata;
- ricerca straordinaria quando una nuova famiglia non è collocabile con il routing corrente.

Ogni ricerca successiva riceve un nuovo ID e non sovrascrive retroattivamente questa scheda.