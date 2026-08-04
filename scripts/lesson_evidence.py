"""Topic-specific evidence and teaching contracts for the lesson generator.

The book is a single continuous course, but a generic profile is not enough to
justify a claim.  This module keeps the semantic routing explicit: each lesson
gets a topic, a small primary-source dossier, and an object/input/operation/
output/invariant contract used by both prose and visuals.
"""

from __future__ import annotations


CHAPTER_TOPIC = {
    14: "rl",
    15: "mlp",
    16: "deep",
    17: "conv",
    18: "rnn",
    19: "representation",
    20: "generative",
    21: "autoregressive",
    22: "vae",
    23: "gan",
    24: "flows",
    25: "diffusion",
    26: "text_data",
    27: "embeddings",
    29: "transformer",
    30: "pretraining_families",
    31: "llm_behavior",
    32: "data_lifecycle",
    33: "mixture",
    34: "scaling",
    35: "pretraining_recipe",
    36: "distributed_training",
    37: "modern_block",
    38: "position",
    39: "attention_variants",
    40: "flash",
    41: "linear_attention",
    42: "ssm",
    43: "hybrid_memory",
    44: "moe",
    45: "alternative_prediction",
    46: "sft",
    47: "peft",
    48: "rlhf",
    49: "preference",
    50: "verifier",
    51: "rlvr",
    52: "reasoning",
    53: "test_time",
    54: "editing",
    55: "multimodal",
    56: "vlm",
    57: "imagegen",
    58: "native_multimodal",
    59: "audio",
    60: "video",
    61: "3d",
    62: "world",
    63: "retrieval",
    64: "rag",
    65: "advanced_rag",
    66: "memory",
    67: "tools",
    68: "interoperability",
    69: "agent_loop",
    70: "multiagent",
    71: "agent_eval",
    72: "agent_safety",
    73: "distillation",
    74: "quantization",
    75: "low_bit",
    76: "decoding",
    77: "speculative",
    78: "kv_cache",
    79: "serving",
    80: "distributed_inference",
    81: "compiler",
    82: "llmops",
    83: "eval_design",
    84: "factuality",
    85: "system_eval",
    86: "interpretability",
    87: "sae",
    88: "robustness",
    89: "injection",
    90: "supply_chain",
    91: "privacy_fairness",
    92: "provenance",
    93: "governance",
    94: "lab",
    95: "small_lm",
    96: "production",
    97: "replication",
    98: "frontier",
}


# Each dossier is deliberately small.  The first item is the primary anchor
# for the first and fifth section; the remaining items cover the middle
# mechanisms.  URLs are stable paper, standard, or official documentation
# locations rather than secondary summaries.
SOURCE_BANKS = {
    "autoregressive": [
        ("Graves, Generating Sequences With Recurrent Neural Networks", "https://arxiv.org/abs/1308.0850"),
        ("Bengio et al., A Neural Probabilistic Language Model", "https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf"),
        ("Holtzman et al., The Curious Case of Neural Text Degeneration", "https://arxiv.org/abs/1904.09751"),
        ("Vaswani et al., Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
    ],
    "vae": [
        ("Kingma and Welling, Auto-Encoding Variational Bayes", "https://arxiv.org/abs/1312.6114"),
        ("Rezende, Mohamed and Wierstra, Stochastic Backpropagation", "https://arxiv.org/abs/1401.4082"),
        ("van den Oord, Vinyals and Kavukcuoglu, Neural Discrete Representation Learning", "https://arxiv.org/abs/1711.00937"),
        ("Lucas et al., Understanding Posterior Collapse in Generative Latent Variable Models", "https://arxiv.org/abs/1901.05534"),
    ],
    "gan": [
        ("Goodfellow et al., Generative Adversarial Nets", "https://arxiv.org/abs/1406.2661"),
        ("Arjovsky, Chintala and Bottou, Wasserstein GAN", "https://arxiv.org/abs/1701.07875"),
        ("Gulrajani et al., Improved Training of Wasserstein GANs", "https://arxiv.org/abs/1704.00028"),
        ("Thanh-Tung and Tran, Catastrophic Forgetting and Mode Collapse in GANs", "https://arxiv.org/abs/1802.10336"),
    ],
    "flows": [
        ("Dinh, Sohl-Dickstein and Bengio, Density Estimation Using Real NVP", "https://arxiv.org/abs/1605.08803"),
        ("Dinh, Krueger and Bengio, NICE", "https://arxiv.org/abs/1410.8516"),
        ("Grathwohl et al., FFJORD", "https://arxiv.org/abs/1810.01367"),
        ("Papamakarios et al., Normalizing Flows for Probabilistic Modeling", "https://arxiv.org/abs/1912.02762"),
    ],
    "diffusion": [
        ("Ho, Jain and Abbeel, Denoising Diffusion Probabilistic Models", "https://arxiv.org/abs/2006.11239"),
        ("Song et al., Score-Based Generative Modeling through Stochastic Differential Equations", "https://arxiv.org/abs/2011.13456"),
        ("Lipman et al., Flow Matching for Generative Modeling", "https://arxiv.org/abs/2210.02747"),
        ("Rombach et al., High-Resolution Image Synthesis with Latent Diffusion Models", "https://arxiv.org/abs/2112.10752"),
    ],
    "text_data": [
        ("Unicode Consortium, The Unicode Standard", "https://www.unicode.org/versions/latest/"),
        ("Sennrich, Haddow and Birch, Neural Machine Translation of Rare Words with Subword Units", "https://arxiv.org/abs/1508.07909"),
        ("Xue et al., ByT5", "https://arxiv.org/abs/2105.13626"),
        ("Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "https://arxiv.org/abs/1910.10683"),
    ],
    "embeddings": [
        ("Mikolov et al., Efficient Estimation of Word Representations in Vector Space", "https://arxiv.org/abs/1301.3781"),
        ("Devlin et al., BERT", "https://arxiv.org/abs/1810.04805"),
        ("Reimers and Gurevych, Sentence-BERT", "https://arxiv.org/abs/1908.10084"),
        ("Gao, Yao and Chen, SimCSE", "https://arxiv.org/abs/2104.08821"),
    ],
    "transformer": [
        ("Vaswani et al., Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
        ("Devlin et al., BERT", "https://arxiv.org/abs/1810.04805"),
        ("Radford et al., Improving Language Understanding by Generative Pre-Training", "https://openai.com/research/language-unsupervised"),
        ("Xiong et al., On Layer Normalization in the Transformer Architecture", "https://arxiv.org/abs/2002.04745"),
    ],
    "pretraining_families": [
        ("Devlin et al., BERT", "https://arxiv.org/abs/1810.04805"),
        ("Radford et al., Language Models are Unsupervised Multitask Learners", "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf"),
        ("Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "https://arxiv.org/abs/1910.10683"),
        ("Lewis et al., BART", "https://arxiv.org/abs/1910.13461"),
    ],
    "llm_behavior": [
        ("Brown et al., Language Models are Few-Shot Learners", "https://arxiv.org/abs/2005.14165"),
        ("Min et al., Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?", "https://arxiv.org/abs/2202.12837"),
        ("Holtzman et al., The Curious Case of Neural Text Degeneration", "https://arxiv.org/abs/1904.09751"),
        ("Guo et al., On Calibration of Modern Neural Networks", "https://arxiv.org/abs/1706.04599"),
    ],
    "data_lifecycle": [
        ("Gebru et al., Datasheets for Datasets", "https://doi.org/10.1145/3458723"),
        ("Bender and Friedman, Data Statements for Natural Language Processing", "https://arxiv.org/abs/1804.07741"),
        ("Lee et al., Deduplicating Training Data Makes Language Models Better", "https://arxiv.org/abs/2107.06499"),
        ("Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "https://arxiv.org/abs/1910.10683"),
    ],
    "mixture": [
        ("Xie et al., DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining", "https://arxiv.org/abs/2305.10429"),
        ("Hoffmann et al., Training Compute-Optimal Large Language Models", "https://arxiv.org/abs/2203.15556"),
        ("Wenzek et al., CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data", "https://arxiv.org/abs/1911.00359"),
        ("Wang et al., Self-Instruct: Aligning Language Models with Self-Generated Instructions", "https://arxiv.org/abs/2212.10560"),
    ],
    "scaling": [
        ("Kaplan et al., Scaling Laws for Neural Language Models", "https://arxiv.org/abs/2001.08361"),
        ("Hoffmann et al., Training Compute-Optimal Large Language Models", "https://arxiv.org/abs/2203.15556"),
        ("Shoeybi et al., Megatron-LM", "https://arxiv.org/abs/1909.08053"),
        ("Rajbhandari et al., ZeRO", "https://arxiv.org/abs/1910.02054"),
    ],
    "pretraining_recipe": [
        ("Brown et al., Language Models are Few-Shot Learners", "https://arxiv.org/abs/2005.14165"),
        ("Loshchilov and Hutter, Decoupled Weight Decay Regularization", "https://arxiv.org/abs/1711.05101"),
        ("Goyal et al., Accurate, Large Minibatch SGD", "https://arxiv.org/abs/1706.02677"),
        ("PyTorch, Saving and Loading Checkpoints", "https://pytorch.org/tutorials/beginner/saving_loading_models.html"),
    ],
    "distributed_training": [
        ("Shoeybi et al., Megatron-LM", "https://arxiv.org/abs/1909.08053"),
        ("Rajbhandari et al., ZeRO", "https://arxiv.org/abs/1910.02054"),
        ("PyTorch, Fully Sharded Data Parallel", "https://pytorch.org/docs/stable/fsdp.html"),
        ("Narayanan et al., Efficient Large-Scale Language Model Training on GPU Clusters", "https://arxiv.org/abs/2104.04473"),
    ],
    "modern_block": [
        ("Vaswani et al., Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
        ("Xiong et al., On Layer Normalization in the Transformer Architecture", "https://arxiv.org/abs/2002.04745"),
        ("Zhang and Sennrich, Root Mean Square Layer Normalization", "https://arxiv.org/abs/1910.07467"),
        ("Shazeer, GLU Variants Improve Transformer", "https://arxiv.org/abs/2002.05202"),
    ],
    "position": [
        ("Su et al., RoFormer: Enhanced Transformer with Rotary Position Embedding", "https://arxiv.org/abs/2104.09864"),
        ("Press, Smith and Lewis, Train Short, Test Long", "https://arxiv.org/abs/2108.12409"),
        ("Peng et al., YaRN: Efficient Context Window Extension of Large Language Models", "https://arxiv.org/abs/2309.00071"),
        ("Ding et al., LongRoPE", "https://arxiv.org/abs/2402.13753"),
    ],
    "attention_variants": [
        ("Shazeer, Fast Transformer Decoding: One Write-Head is All You Need", "https://arxiv.org/abs/1911.02150"),
        ("Ainslie et al., GQA: Training Generalized Multi-Query Transformer Models", "https://arxiv.org/abs/2305.13245"),
        ("DeepSeek-AI, DeepSeek-V2", "https://arxiv.org/abs/2405.04434"),
        ("Beltagy, Peters and Cohan, Longformer", "https://arxiv.org/abs/2004.05150"),
    ],
    "flash": [
        ("Dao et al., FlashAttention", "https://arxiv.org/abs/2205.14135"),
        ("Dao, FlashAttention-2", "https://arxiv.org/abs/2307.08691"),
        ("Shah et al., FlashAttention-3", "https://arxiv.org/abs/2407.08608"),
        ("PyTorch, Scaled Dot Product Attention", "https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html"),
    ],
    "linear_attention": [
        ("Katharopoulos et al., Transformers are RNNs", "https://arxiv.org/abs/2006.16236"),
        ("Schlag et al., Linear Transformers as Programmable Fast Weight Programmers", "https://arxiv.org/abs/2106.13820"),
        ("Sun et al., Retentive Network", "https://arxiv.org/abs/2307.08621"),
        ("Yang et al., Gated Delta Networks", "https://arxiv.org/abs/2412.06464"),
    ],
    "ssm": [
        ("Gu et al., Efficiently Modeling Long Sequences with Structured State Spaces", "https://arxiv.org/abs/2111.00396"),
        ("Gu and Dao, Mamba: Linear-Time Sequence Modeling with Selective State Spaces", "https://arxiv.org/abs/2312.00752"),
        ("Poli et al., Hyena Hierarchy", "https://arxiv.org/abs/2302.10866"),
        ("Peng et al., RWKV: Reinventing RNNs for the Transformer Era", "https://arxiv.org/abs/2305.13048"),
    ],
    "hybrid_memory": [
        ("De et al., Griffin: Mixing Gated Linear Recurrences with Local Attention", "https://arxiv.org/abs/2402.19427"),
        ("Behrouz et al., Titans: Learning to Memorize at Test Time", "https://arxiv.org/abs/2501.00663"),
        ("Sun et al., Retentive Network", "https://arxiv.org/abs/2307.08621"),
        ("Dao and Gu, Transformers are SSMs", "https://arxiv.org/abs/2405.21060"),
    ],
    "moe": [
        ("Shazeer et al., Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", "https://arxiv.org/abs/1701.06538"),
        ("Fedus, Zoph and Shazeer, Switch Transformers", "https://arxiv.org/abs/2101.03961"),
        ("Dai et al., DeepSeekMoE", "https://arxiv.org/abs/2401.06066"),
        ("DeepSeek-AI, DeepSeek-V3 Technical Report", "https://arxiv.org/abs/2412.19437"),
    ],
    "alternative_prediction": [
        ("Xue et al., ByT5", "https://arxiv.org/abs/2105.13626"),
        ("Yu et al., MEGABYTE", "https://arxiv.org/abs/2305.07185"),
        ("Gloeckle et al., Better and Faster Large Language Models via Multi-token Prediction", "https://arxiv.org/abs/2404.19737"),
        ("Li et al., Diffusion-LM", "https://arxiv.org/abs/2205.14217"),
    ],
    "sft": [
        ("Ouyang et al., Training Language Models to Follow Instructions with Human Feedback", "https://arxiv.org/abs/2203.02155"),
        ("Wei et al., Finetuned Language Models are Zero-Shot Learners", "https://arxiv.org/abs/2109.01652"),
        ("Zhou et al., LIMA: Less Is More for Alignment", "https://arxiv.org/abs/2305.11206"),
        ("Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "https://arxiv.org/abs/1910.10683"),
    ],
    "peft": [
        ("Houlsby et al., Parameter-Efficient Transfer Learning for NLP", "https://arxiv.org/abs/1902.00751"),
        ("Hu et al., LoRA: Low-Rank Adaptation of Large Language Models", "https://arxiv.org/abs/2106.09685"),
        ("Liu et al., Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning", "https://arxiv.org/abs/2205.05638"),
        ("Dettmers et al., QLoRA", "https://arxiv.org/abs/2305.14314"),
    ],
    "rlhf": [
        ("Christiano et al., Deep Reinforcement Learning from Human Preferences", "https://arxiv.org/abs/1706.03741"),
        ("Ouyang et al., Training Language Models to Follow Instructions with Human Feedback", "https://arxiv.org/abs/2203.02155"),
        ("Bai et al., Constitutional AI", "https://arxiv.org/abs/2212.08073"),
        ("Gao et al., Scaling Laws for Reward Model Overoptimization", "https://arxiv.org/abs/2210.10760"),
    ],
    "preference": [
        ("Rafailov et al., Direct Preference Optimization", "https://arxiv.org/abs/2305.18290"),
        ("Azar et al., A General Theoretical Paradigm to Understand Learning from Human Preferences", "https://arxiv.org/abs/2310.12036"),
        ("Ethayarajh et al., KTO: Model Alignment as Prospect Theoretic Optimization", "https://arxiv.org/abs/2402.01306"),
        ("Hong et al., ORPO: Monolithic Preference Optimization without Reference Model", "https://arxiv.org/abs/2403.07691"),
    ],
    "verifier": [
        ("Cobbe et al., Training Verifiers to Solve Math Word Problems", "https://arxiv.org/abs/2110.14168"),
        ("Uesato et al., Solving Math Word Problems with Process- and Outcome-Based Feedback", "https://arxiv.org/abs/2211.14275"),
        ("Lightman et al., Let’s Verify Step by Step", "https://arxiv.org/abs/2305.20050"),
        ("Gao et al., Scaling Laws for Reward Model Overoptimization", "https://arxiv.org/abs/2210.10760"),
    ],
    "rlvr": [
        ("Shao et al., DeepSeekMath", "https://arxiv.org/abs/2402.03300"),
        ("DeepSeek-AI, DeepSeek-R1", "https://arxiv.org/abs/2501.12948"),
        ("Lightman et al., Let’s Verify Step by Step", "https://arxiv.org/abs/2305.20050"),
        ("Uesato et al., Solving Math Word Problems with Process- and Outcome-Based Feedback", "https://arxiv.org/abs/2211.14275"),
    ],
    "reasoning": [
        ("Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "https://arxiv.org/abs/2201.11903"),
        ("Wang et al., Self-Consistency Improves Chain of Thought Reasoning", "https://arxiv.org/abs/2203.11171"),
        ("DeepSeek-AI, DeepSeek-R1", "https://arxiv.org/abs/2501.12948"),
        ("Hinton, Vinyals and Dean, Distilling the Knowledge in a Neural Network", "https://arxiv.org/abs/1503.02531"),
    ],
    "test_time": [
        ("Snell et al., Scaling LLM Test-Time Compute Optimally", "https://arxiv.org/abs/2408.03314"),
        ("Wang et al., Self-Consistency Improves Chain of Thought Reasoning", "https://arxiv.org/abs/2203.11171"),
        ("Yao et al., Tree of Thoughts", "https://arxiv.org/abs/2305.10601"),
        ("Lightman et al., Let’s Verify Step by Step", "https://arxiv.org/abs/2305.20050"),
    ],
    "editing": [
        ("Meng et al., Locating and Editing Factual Associations in GPT", "https://arxiv.org/abs/2202.05262"),
        ("Meng et al., Mass-Editing Memory in a Transformer", "https://arxiv.org/abs/2210.07229"),
        ("Yadav et al., TIES-Merging", "https://arxiv.org/abs/2306.01708"),
        ("Ilharco et al., Editing Models with Task Arithmetic", "https://arxiv.org/abs/2212.04089"),
    ],
    "multimodal": [
        ("Radford et al., Learning Transferable Visual Models From Natural Language Supervision", "https://arxiv.org/abs/2103.00020"),
        ("Alayrac et al., Flamingo", "https://arxiv.org/abs/2204.14198"),
        ("Girdhar et al., ImageBind", "https://arxiv.org/abs/2305.05665"),
        ("Team Chameleon, Chameleon", "https://arxiv.org/abs/2405.09818"),
    ],
    "vlm": [
        ("Dosovitskiy et al., An Image is Worth 16x16 Words", "https://arxiv.org/abs/2010.11929"),
        ("Li et al., BLIP-2", "https://arxiv.org/abs/2301.12597"),
        ("Liu et al., Visual Instruction Tuning", "https://arxiv.org/abs/2304.08485"),
        ("Alayrac et al., Flamingo", "https://arxiv.org/abs/2204.14198"),
    ],
    "imagegen": [
        ("Ho, Jain and Abbeel, Denoising Diffusion Probabilistic Models", "https://arxiv.org/abs/2006.11239"),
        ("Rombach et al., High-Resolution Image Synthesis with Latent Diffusion Models", "https://arxiv.org/abs/2112.10752"),
        ("Zhang et al., Adding Conditional Control to Text-to-Image Diffusion Models", "https://arxiv.org/abs/2302.05543"),
        ("Brooks, Holynski and Efros, InstructPix2Pix", "https://arxiv.org/abs/2211.09800"),
    ],
    "native_multimodal": [
        ("Team Chameleon, Chameleon", "https://arxiv.org/abs/2405.09818"),
        ("Girdhar et al., ImageBind", "https://arxiv.org/abs/2305.05665"),
        ("Piergiovanni et al., Mirasol3B: A Multimodal Autoregressive Model", "https://arxiv.org/abs/2311.05698"),
        ("Wu et al., NExT-GPT", "https://arxiv.org/abs/2309.05519"),
    ],
    "audio": [
        ("Baevski et al., wav2vec 2.0", "https://arxiv.org/abs/2006.11477"),
        ("Radford et al., Robust Speech Recognition via Large-Scale Weak Supervision", "https://arxiv.org/abs/2212.04356"),
        ("Borsos et al., AudioLM", "https://arxiv.org/abs/2209.03143"),
        ("Zeghidour et al., SoundStream", "https://arxiv.org/abs/2107.03312"),
    ],
    "video": [
        ("Ho et al., Video Diffusion Models", "https://arxiv.org/abs/2204.03458"),
        ("Singer et al., Make-A-Video", "https://arxiv.org/abs/2206.01718"),
        ("Hong et al., CogVideo", "https://arxiv.org/abs/2205.15868"),
        ("Polyak et al., Movie Gen", "https://arxiv.org/abs/2410.13720"),
    ],
    "3d": [
        ("Mildenhall et al., NeRF", "https://arxiv.org/abs/2003.08934"),
        ("Kerbl et al., 3D Gaussian Splatting", "https://arxiv.org/abs/2308.04079"),
        ("Qi et al., PointNet", "https://arxiv.org/abs/1612.00593"),
        ("Poole et al., DreamFusion", "https://arxiv.org/abs/2209.14988"),
    ],
    "world": [
        ("Ha and Schmidhuber, World Models", "https://arxiv.org/abs/1803.10122"),
        ("Hafner et al., Mastering Diverse Domains through World Models", "https://arxiv.org/abs/2301.04104"),
        ("Driess et al., PaLM-E", "https://arxiv.org/abs/2303.03378"),
        ("Brohan et al., RT-2", "https://arxiv.org/abs/2307.15818"),
    ],
    "retrieval": [
        ("Robertson and Zaragoza, The Probabilistic Relevance Framework: BM25 and Beyond", "https://doi.org/10.1561/1500000019"),
        ("Karpukhin et al., Dense Passage Retrieval", "https://arxiv.org/abs/2004.04906"),
        ("Khattab and Zaharia, ColBERT", "https://arxiv.org/abs/2004.12832"),
        ("Johnson, Douze and Jégou, Billion-scale Similarity Search with GPUs", "https://arxiv.org/abs/1702.08734"),
    ],
    "rag": [
        ("Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", "https://arxiv.org/abs/2005.11401"),
        ("Karpukhin et al., Dense Passage Retrieval", "https://arxiv.org/abs/2004.04906"),
        ("Asai et al., Self-RAG", "https://arxiv.org/abs/2310.11511"),
        ("Rashkin et al., Measuring Attribution in Natural Language Generation Models", "https://arxiv.org/abs/2112.12870"),
    ],
    "advanced_rag": [
        ("Asai et al., Self-RAG", "https://arxiv.org/abs/2310.11511"),
        ("Sarthi et al., RAPTOR", "https://arxiv.org/abs/2401.18059"),
        ("Edge et al., From Local to Global: A Graph RAG Approach", "https://arxiv.org/abs/2404.16130"),
        ("Gao et al., Precise Zero-Shot Dense Retrieval without Relevance Labels", "https://arxiv.org/abs/2212.10496"),
    ],
    "memory": [
        ("Packer et al., MemGPT", "https://arxiv.org/abs/2310.08560"),
        ("Wu et al., Memorizing Transformers", "https://arxiv.org/abs/2203.08913"),
        ("Wang et al., Augmenting Language Models with Long-Term Memory", "https://arxiv.org/abs/2306.07174"),
        ("Lewis et al., Retrieval-Augmented Generation", "https://arxiv.org/abs/2005.11401"),
    ],
    "tools": [
        ("Schick et al., Toolformer", "https://arxiv.org/abs/2302.04761"),
        ("Yao et al., ReAct", "https://arxiv.org/abs/2210.03629"),
        ("Patil et al., Gorilla", "https://arxiv.org/abs/2305.15334"),
        ("Qin et al., ToolLLM", "https://arxiv.org/abs/2307.16789"),
    ],
    "interoperability": [
        ("Model Context Protocol, Basic Specification 2025-06-18", "https://modelcontextprotocol.io/specification/2025-06-18/basic/index"),
        ("Agent2Agent Protocol, Specification", "https://a2a-protocol.org/latest/specification/"),
        ("NIST, Digital Identity Guidelines", "https://pages.nist.gov/800-63-4/"),
        ("W3C, Verifiable Credentials Data Model 2.0", "https://www.w3.org/TR/vc-data-model-2.0/"),
    ],
    "agent_loop": [
        ("Yao et al., ReAct", "https://arxiv.org/abs/2210.03629"),
        ("Schick et al., Toolformer", "https://arxiv.org/abs/2302.04761"),
        ("Zhou et al., WebArena", "https://arxiv.org/abs/2307.13854"),
        ("Yang et al., SWE-agent", "https://arxiv.org/abs/2405.15793"),
    ],
    "multiagent": [
        ("Li et al., CAMEL", "https://arxiv.org/abs/2303.17760"),
        ("Wu et al., AutoGen", "https://arxiv.org/abs/2308.08155"),
        ("Zhou et al., WebArena", "https://arxiv.org/abs/2307.13854"),
        ("Yang et al., SWE-agent", "https://arxiv.org/abs/2405.15793"),
    ],
    "agent_eval": [
        ("Liu et al., AgentBench", "https://arxiv.org/abs/2308.03688"),
        ("Zhou et al., WebArena", "https://arxiv.org/abs/2307.13854"),
        ("Jimenez et al., SWE-bench", "https://arxiv.org/abs/2310.06770"),
        ("Yao et al., τ-bench", "https://arxiv.org/abs/2406.12045"),
    ],
    "agent_safety": [
        ("Debenedetti et al., AgentDojo", "https://arxiv.org/abs/2406.13352"),
        ("OWASP, Top 10 for Large Language Model Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
        ("Greshake et al., Not What You’ve Signed Up For", "https://arxiv.org/abs/2302.12173"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
    "distillation": [
        ("Hinton, Vinyals and Dean, Distilling the Knowledge in a Neural Network", "https://arxiv.org/abs/1503.02531"),
        ("Sanh et al., DistilBERT", "https://arxiv.org/abs/1910.01108"),
        ("Frantar and Alistarh, SparseGPT", "https://arxiv.org/abs/2301.00774"),
        ("Sun et al., A Simple and Effective Pruning Approach for Large Language Models", "https://arxiv.org/abs/2306.11695"),
    ],
    "quantization": [
        ("Frantar et al., GPTQ", "https://arxiv.org/abs/2210.17323"),
        ("Xiao et al., SmoothQuant", "https://arxiv.org/abs/2211.10438"),
        ("Lin et al., AWQ", "https://arxiv.org/abs/2306.00978"),
        ("Dettmers et al., QLoRA", "https://arxiv.org/abs/2305.14314"),
    ],
    "low_bit": [
        ("Ma et al., The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits", "https://arxiv.org/abs/2402.17764"),
        ("Wang et al., BitNet: Scaling 1-bit Transformers for Large Language Models", "https://arxiv.org/abs/2310.11453"),
        ("Hubara et al., Binarized Neural Networks", "https://arxiv.org/abs/1602.02830"),
        ("Liu et al., Bi-Real Net", "https://arxiv.org/abs/1608.06037"),
    ],
    "decoding": [
        ("Holtzman et al., The Curious Case of Neural Text Degeneration", "https://arxiv.org/abs/1904.09751"),
        ("Vijayakumar et al., Diverse Beam Search", "https://arxiv.org/abs/1610.02424"),
        ("Meister et al., Locally Typical Sampling", "https://arxiv.org/abs/2202.00666"),
        ("Poesia et al., Constrained Language Models Yield Few-Shot ...", "https://arxiv.org/abs/2305.13971"),
    ],
    "speculative": [
        ("Leviathan, Kalman and Matias, Fast Inference from Transformers via Speculative Decoding", "https://arxiv.org/abs/2211.17192"),
        ("Chen et al., Accelerating Large Language Model Decoding with Speculative Sampling", "https://arxiv.org/abs/2302.01318"),
        ("Cai et al., Medusa", "https://arxiv.org/abs/2401.10774"),
        ("Li et al., EAGLE", "https://arxiv.org/abs/2401.15077"),
    ],
    "kv_cache": [
        ("Kwon et al., Efficient Memory Management for Large Language Model Serving with PagedAttention", "https://arxiv.org/abs/2309.06180"),
        ("Xiao et al., Efficient Streaming Language Models with Attention Sinks", "https://arxiv.org/abs/2309.17453"),
        ("Zheng et al., SGLang", "https://arxiv.org/abs/2312.07104"),
        ("Dao et al., FlashAttention", "https://arxiv.org/abs/2205.14135"),
    ],
    "serving": [
        ("Kwon et al., Efficient Memory Management for Large Language Model Serving with PagedAttention", "https://arxiv.org/abs/2309.06180"),
        ("Yu et al., Orca: A Distributed Serving System for Transformer-Based Generative Models", "https://arxiv.org/abs/2309.11687"),
        ("Zheng et al., SGLang", "https://arxiv.org/abs/2312.07104"),
        ("Kang et al., DistServe", "https://arxiv.org/abs/2401.09670"),
    ],
    "distributed_inference": [
        ("Shoeybi et al., Megatron-LM", "https://arxiv.org/abs/1909.08053"),
        ("Rajbhandari et al., ZeRO", "https://arxiv.org/abs/1910.02054"),
        ("Kang et al., DistServe", "https://arxiv.org/abs/2401.09670"),
        ("DeepSpeed, Inference Documentation", "https://www.deepspeed.ai/inference/"),
    ],
    "compiler": [
        ("Tillet et al., Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations", "https://arxiv.org/abs/2107.03374"),
        ("PyTorch, torch.compile", "https://pytorch.org/docs/stable/torch.compiler.html"),
        ("Tian et al., XLA: Compiling Graphs of Operations", "https://openxla.org/xla"),
        ("PyTorch, Performance Tuning Guide", "https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html"),
    ],
    "llmops": [
        ("Sculley et al., Hidden Technical Debt in Machine Learning Systems", "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("Mitchell et al., Model Cards for Model Reporting", "https://doi.org/10.1145/3287560.3287596"),
        ("Schwartz et al., Green AI", "https://arxiv.org/abs/1907.10597"),
    ],
    "eval_design": [
        ("Liang et al., Holistic Evaluation of Language Models", "https://arxiv.org/abs/2211.09110"),
        ("Hendrycks et al., Measuring Massive Multitask Language Understanding", "https://arxiv.org/abs/2009.03300"),
        ("Mitchell et al., Model Cards for Model Reporting", "https://doi.org/10.1145/3287560.3287596"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
    "factuality": [
        ("Lin, Hilton and Evans, TruthfulQA", "https://arxiv.org/abs/2109.07958"),
        ("Manakul, Liusie and Gales, SelfCheckGPT", "https://arxiv.org/abs/2303.08896"),
        ("Guo et al., On Calibration of Modern Neural Networks", "https://arxiv.org/abs/1706.04599"),
        ("Lewis et al., Retrieval-Augmented Generation", "https://arxiv.org/abs/2005.11401"),
    ],
    "system_eval": [
        ("Liang et al., Holistic Evaluation of Language Models", "https://arxiv.org/abs/2211.09110"),
        ("Liu et al., AgentBench", "https://arxiv.org/abs/2308.03688"),
        ("Jimenez et al., SWE-bench", "https://arxiv.org/abs/2310.06770"),
        ("Zhou et al., WebArena", "https://arxiv.org/abs/2307.13854"),
    ],
    "interpretability": [
        ("Elhage et al., A Mathematical Framework for Transformer Circuits", "https://transformer-circuits.pub/2021/framework/index.html"),
        ("Meng et al., Locating and Editing Factual Associations in GPT", "https://arxiv.org/abs/2202.05262"),
        ("Geiger et al., Causal Abstractions of Neural Networks", "https://arxiv.org/abs/2106.02997"),
        ("Nanda et al., Progress Measures for Grokking via Mechanistic Interpretability", "https://arxiv.org/abs/2301.05217"),
    ],
    "sae": [
        ("Bricken et al., Towards Monosemanticity: Decomposing Language Models with Dictionary Learning", "https://arxiv.org/abs/2305.12195"),
        ("Cunningham et al., Sparse Autoencoders Find Highly Interpretable Features in Language Models", "https://arxiv.org/abs/2309.08600"),
        ("Templeton et al., Scaling Monosemanticity", "https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html"),
        ("Marks et al., Sparse Feature Circuits", "https://arxiv.org/abs/2403.19647"),
    ],
    "robustness": [
        ("Zou et al., Universal and Transferable Adversarial Attacks on Aligned Language Models", "https://arxiv.org/abs/2307.15043"),
        ("Wei et al., Jailbroken: How Does LLM Safety Training Fail?", "https://arxiv.org/abs/2307.02483"),
        ("Perez et al., Red Teaming Language Models with Language Models", "https://arxiv.org/abs/2202.03286"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
    "injection": [
        ("Greshake et al., Not What You’ve Signed Up For", "https://arxiv.org/abs/2302.12173"),
        ("Debenedetti et al., AgentDojo", "https://arxiv.org/abs/2406.13352"),
        ("OWASP, Top 10 for Large Language Model Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
    "supply_chain": [
        ("Biggio, Nelson and Laskov, Poisoning Attacks against Machine Learning", "https://arxiv.org/abs/1804.00792"),
        ("Carlini et al., Extracting Training Data from Large Language Models", "https://arxiv.org/abs/2012.07805"),
        ("Tramer et al., Stealing Machine Learning Models via Prediction APIs", "https://arxiv.org/abs/1609.02943"),
        ("NIST, Secure Software Development Framework SP 800-218", "https://csrc.nist.gov/pubs/sp/800/218/final"),
    ],
    "privacy_fairness": [
        ("Abadi et al., Deep Learning with Differential Privacy", "https://arxiv.org/abs/1607.00133"),
        ("Shokri et al., Membership Inference Attacks Against Machine Learning Models", "https://arxiv.org/abs/1610.05820"),
        ("Selbst et al., Fairness and Abstraction in Sociotechnical Systems", "https://arxiv.org/abs/1811.03577"),
        ("Bourtouf et al., Machine Unlearning", "https://arxiv.org/abs/1912.03817"),
    ],
    "provenance": [
        ("C2PA, Technical Specification 2.3", "https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html"),
        ("W3C, Verifiable Credentials Data Model 2.0", "https://www.w3.org/TR/vc-data-model-2.0/"),
        ("Kirchenbauer et al., A Watermark for Large Language Models", "https://arxiv.org/abs/2301.10226"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
    "governance": [
        ("NIST, Artificial Intelligence Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("NIST, Artificial Intelligence Risk Management Framework: Generative AI Profile", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"),
        ("European Union, Regulation (EU) 2024/1689", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32024R1689"),
        ("Schwartz et al., Green AI", "https://arxiv.org/abs/1907.10597"),
    ],
    "lab": [
        ("Pineau et al., Improving Reproducibility in Machine Learning Research", "https://jmlr.org/papers/v22/20-303.html"),
        ("ACM, Artifact Review and Badging", "https://www.acm.org/publications/policies/artifact-review-and-badging-current"),
        ("PyTorch, Reproducibility", "https://pytorch.org/docs/stable/notes/randomness.html"),
        ("Python Documentation, venv", "https://docs.python.org/3/library/venv.html"),
    ],
    "small_lm": [
        ("Bengio et al., A Neural Probabilistic Language Model", "https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf"),
        ("Vaswani et al., Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
        ("PyTorch, Language Modeling with nn.Transformer", "https://pytorch.org/tutorials/beginner/transformer_tutorial.html"),
        ("Holtzman et al., The Curious Case of Neural Text Degeneration", "https://arxiv.org/abs/1904.09751"),
    ],
    "production": [
        ("Sculley et al., Hidden Technical Debt in Machine Learning Systems", "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems"),
        ("Mitchell et al., Model Cards for Model Reporting", "https://doi.org/10.1145/3287560.3287596"),
        ("NIST, AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("Google, Rules of Machine Learning", "https://developers.google.com/machine-learning/guides/rules-of-ml"),
    ],
    "replication": [
        ("Pineau et al., Improving Reproducibility in Machine Learning Research", "https://jmlr.org/papers/v22/20-303.html"),
        ("ACM, Artifact Review and Badging", "https://www.acm.org/publications/policies/artifact-review-and-badging-current"),
        ("NeurIPS, Paper Checklist", "https://neurips.cc/public/guides/PaperChecklist"),
        ("Pineau et al., Improving Reproducibility in Machine Learning Research", "https://reproducibility-challenge.github.io/neurips2019/"),
    ],
    "frontier": [
        ("Stanford HAI, AI Index Report 2025", "https://hai.stanford.edu/ai-index/2025-ai-index-report"),
        ("DeepSeek-AI, DeepSeek-R1", "https://arxiv.org/abs/2501.12948"),
        ("DeepSeek-AI, DeepSeek-V3 Technical Report", "https://arxiv.org/abs/2412.19437"),
        ("MLCommons, MLPerf Inference", "https://mlcommons.org/benchmarks/inference/"),
    ],
}

# The first seven technical chapters predate the topic-specific registry
# above.  They still need their own primary anchors; falling back to the lab
# dossier would make the text look sourced while leaving the mechanism
# unsupported.
SOURCE_BANKS.update({
    "rl": [
        ("Sutton e Barto, Reinforcement Learning: An Introduction", "http://incompleteideas.net/book/the-book-2nd.html"),
        ("Mnih et al., Human-level control through deep reinforcement learning", "https://doi.org/10.1038/nature14236"),
        ("Schulman et al., Proximal Policy Optimization Algorithms", "https://arxiv.org/abs/1707.06347"),
        ("Puterman, Markov Decision Processes", "https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887"),
    ],
    "mlp": [
        ("Rosenblatt, The Perceptron", "https://doi.org/10.1037/h0042519"),
        ("Rumelhart, Hinton e Williams, Learning representations by back-propagating errors", "https://doi.org/10.1038/323533a0"),
        ("Goodfellow, Bengio e Courville, Deep Learning", "https://www.deeplearningbook.org/"),
        ("He et al., Delving Deep into Rectifiers", "https://arxiv.org/abs/1502.01852"),
    ],
    "deep": [
        ("He et al., Deep Residual Learning for Image Recognition", "https://arxiv.org/abs/1512.03385"),
        ("Glorot and Bengio, Understanding the difficulty of training deep feedforward neural networks", "https://proceedings.mlr.press/v9/glorot10a.html"),
        ("Ioffe and Szegedy, Batch Normalization", "https://arxiv.org/abs/1502.03167"),
        ("Srivastava et al., Dropout", "https://jmlr.org/papers/v15/srivastava14a.html"),
    ],
    "conv": [
        ("LeCun et al., Gradient-Based Learning Applied to Document Recognition", "https://doi.org/10.1109/5.726791"),
        ("He et al., Deep Residual Learning for Image Recognition", "https://arxiv.org/abs/1512.03385"),
        ("Dosovitskiy et al., An Image is Worth 16x16 Words", "https://arxiv.org/abs/2010.11929"),
        ("Gilmer et al., Neural Message Passing for Quantum Chemistry", "https://arxiv.org/abs/1704.01212"),
    ],
    "rnn": [
        ("Hochreiter e Schmidhuber, Long Short-Term Memory", "https://www.bioinf.jku.at/publications/older/2604.pdf"),
        ("Cho et al., Learning Phrase Representations using RNN Encoder-Decoder", "https://arxiv.org/abs/1406.1078"),
        ("Sutskever, Vinyals e Le, Sequence to Sequence Learning with Neural Networks", "https://arxiv.org/abs/1409.3215"),
        ("Pascanu, Mikolov e Bengio, On the difficulty of training recurrent neural networks", "https://arxiv.org/abs/1211.5063"),
    ],
    "representation": [
        ("Hinton e Salakhutdinov, Reducing the Dimensionality of Data with Neural Networks", "https://www.science.org/doi/10.1126/science.1127647"),
        ("Chen et al., A Simple Framework for Contrastive Learning of Visual Representations", "https://arxiv.org/abs/2002.05709"),
        ("Locatello et al., Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations", "https://arxiv.org/abs/1811.12359"),
        ("Oord, Li e Vinyals, Representation Learning with Contrastive Predictive Coding", "https://arxiv.org/abs/1807.03748"),
    ],
    "generative": [
        ("Kingma e Welling, Auto-Encoding Variational Bayes", "https://arxiv.org/abs/1312.6114"),
        ("Goodfellow et al., Generative Adversarial Nets", "https://arxiv.org/abs/1406.2661"),
        ("Dinh, Sohl-Dickstein e Bengio, Density Estimation using Real NVP", "https://arxiv.org/abs/1605.08803"),
        ("Ho, Jain e Abbeel, Denoising Diffusion Probabilistic Models", "https://arxiv.org/abs/2006.11239"),
    ],
})


DETAILS = {
    21: {"object": "la sequenza di token e la distribuzione del prossimo elemento", "input": "un prefisso di tre token e una mask causale", "operation": "fattorizzazione, teacher forcing e decoding", "output": "logits, token scelto e traiettoria", "invariant": "nessuna posizione futura entra nella predizione causale", "example": "due passi di teacher forcing confrontati con un passo campionato"},
    22: {"object": "una variabile osservata e il suo codice latente", "input": "x, media, log-varianza e rumore epsilon", "operation": "ELBO e reparameterization trick", "output": "ricostruzione, KL e codice latente", "invariant": "la ricostruzione non elimina il costo KL né dimostra disentanglement", "example": "una media, una deviazione e un campione z calcolato con epsilon"},
    23: {"object": "la partita tra generatore e discriminatore", "input": "un dato reale, un campione e due score", "operation": "aggiornamento alternato e segnale di feedback", "output": "score, gradiente e campione", "invariant": "un equilibrio locale non prova copertura né stabilità", "example": "due score reali e sintetici con un aggiornamento alternato"},
    24: {"object": "un dato trasformato da una mappa invertibile", "input": "x, log-determinante e variabile latente z", "operation": "coupling, cambio di variabile e inversione", "output": "log-likelihood, z e campione ricostruito", "invariant": "l'inversione richiede una trasformazione e un log-determinante coerenti", "example": "una trasformazione affine a due coordinate invertita senza perdita"},
    25: {"object": "un dato corrotto e il percorso di denoising", "input": "x_0, rumore epsilon e timestep t", "operation": "forward noising, score o velocity e sampler", "output": "stima del rumore e campione ricostruito", "invariant": "parametrizzazione e scheduler fanno parte del contratto", "example": "un singolo timestep con rumore noto e stima separata"},
    26: {"object": "il testo prima e dopo la tokenizzazione", "input": "una stringa Unicode con byte e token speciali", "operation": "normalizzazione, segmentazione e packing", "output": "ID, confini, mask e costo in token", "invariant": "stringa, encoding e tokenizer devono restare dichiarati", "example": "la stessa parola con carattere accentato osservata a livello di byte"},
    27: {"object": "un ID e il vettore che lo rappresenta", "input": "due ID, due vettori e una query", "operation": "lookup, pooling, similarità e normalizzazione", "output": "embedding, ranking o predizione", "invariant": "la similarità dipende da training, metrica e normalizzazione", "example": "similarità coseno tra due vettori dopo la normalizzazione"},
    29: {"object": "lo stato nascosto che attraversa il blocco Transformer", "input": "tokenizzati di shape [batch, length] e vettori [batch, length, d]", "operation": "embedding, attention, MLP e residuo", "output": "stato contestuale e logits", "invariant": "mask, shape e percorso residuale devono essere compatibili", "example": "un blocco con due token e due dimensioni nascoste"},
    30: {"object": "una famiglia architetturale legata al proprio obiettivo", "input": "sequenza, mask e target di pretraining", "operation": "encoder, decoder, span corruption o causal prediction", "output": "rappresentazione o distribuzione predittiva", "invariant": "architettura e objective non possono essere scambiati senza cambiare il compito", "example": "lo stesso testo con target masked e causal separati"},
    31: {"object": "un prompt e la distribuzione del token successivo", "input": "prefisso tokenizzato, esempi e temperatura dichiarati", "operation": "in-context learning, decoding e calibrazione", "output": "logits, risposta e confidenza misurabile", "invariant": "probabilità, comportamento osservato e correttezza non sono sinonimi", "example": "lo stesso prompt con greedy e top-p confrontati"},
    32: {"object": "un record di dataset dalla sorgente al manifest", "input": "testo grezzo, metadati, split e digest", "operation": "parsing, filtro, deduplicazione e tokenizzazione", "output": "record ammesso, conteggi e manifest", "invariant": "ogni trasformazione deve restare ricostruibile e ordinata", "example": "due record, uno duplicato, con digest prima e dopo il filtro"},
    33: {"object": "la miscela effettiva di sorgenti durante il training", "input": "pesi, temperatura, curriculum e conteggio dei token", "operation": "campionamento, ripesatura e generazione controllata", "output": "probabilità effettive e mix osservato", "invariant": "peso nominale e esposizione effettiva non sono la stessa misura", "example": "tre sorgenti ripesate con temperatura e conteggio finale"},
    34: {"object": "una curva empirica tra scala, compute e loss", "input": "punti con parametri, token, FLOP e loss", "operation": "fit, confronto isoFLOP ed estrapolazione", "output": "stima con intervallo osservato e costo", "invariant": "un fit fuori dominio non è una legge garantita", "example": "quattro punti, fit lineare locale e intervallo dichiarato"},
    35: {"object": "lo stato completo di una ricetta di pretraining", "input": "batch, learning rate, seed, optimizer e checkpoint", "operation": "forward, backward, update, schedule e recovery", "output": "loss, parametri e checkpoint ripristinabile", "invariant": "un checkpoint deve includere lo stato necessario a continuare il run", "example": "warmup di quattro step e ripresa dal contatore salvato"},
    36: {"object": "gradienti e stato distribuiti tra worker", "input": "microbatch, worker, shard e topologia", "operation": "all-reduce, sharding, pipeline e recovery", "output": "gradiente ridotto, stato sincronizzato e fault osservato", "invariant": "la riduzione e il conteggio del batch devono essere dichiarati", "example": "due worker con gradienti diversi e media esplicita"},
    37: {"object": "un residual stream dentro un blocco moderno", "input": "h di shape [batch, length, d] e norma misurata", "operation": "norm, attention, MLP e gating nell'ordine scelto", "output": "h' con shape preservata e statistiche confrontabili", "invariant": "ordine dei sottolayer e shape sono parte del blocco", "example": "pre-norm e residuale su un vettore di due coordinate"},
    38: {"object": "la relazione tra posizione e rappresentazione del token", "input": "query, key e indice di posizione", "operation": "posizione assoluta, relativa, RoPE o bias", "output": "score dipendente dalla posizione", "invariant": "estendere il contesto richiede una misura fuori dalla lunghezza addestrata", "example": "lo stesso vettore ruotato a due posizioni diverse"},
    39: {"object": "le teste di query e key-value che alimentano l'attention", "input": "Q con h_q teste e KV con h_kv teste", "operation": "MHA, MQA, GQA, località o sparsità", "output": "score, cache e pattern di comunicazione", "invariant": "raggruppamento delle teste e costo della KV cache restano espliciti", "example": "quattro query head condividono due KV head"},
    40: {"object": "il calcolo dell'attention e il suo movimento di dati", "input": "tile di Q, K, V, dtype e device", "operation": "tiling, softmax online e ricomputazione", "output": "stesso contratto matematico con memoria e latenza misurate", "invariant": "una misura hardware dipende da shape, backend e precisione", "example": "softmax stabile su due tile con massimo per riga"},
    41: {"object": "uno stato causale che sostituisce il prodotto quadratico", "input": "sequenza x_t, kernel fattorizzabile e stato", "operation": "recurrence, normalizzazione e fast weights", "output": "h_t e predizione con costo dichiarato", "invariant": "la fattorizzazione cambia memoria e capacità di interazione", "example": "tre aggiornamenti causali con stato scalare"},
    42: {"object": "lo stato dinamico di un modello state-space", "input": "x_t, stato s_t e matrici A, B, C", "operation": "recurrence, convolutione lunga o selezione", "output": "stato e uscita per ogni posizione", "invariant": "stabilità e discretizzazione fanno parte dell'implementazione", "example": "tre passi di una dinamica lineare con stato osservabile"},
    43: {"object": "informazione distribuita tra attenzione locale e memoria", "input": "segmento corrente, stato e memoria persistente", "operation": "write, read, routing e fusione", "output": "stato aggiornato e contenuto recuperato", "invariant": "durata e provenienza della memoria devono essere separate", "example": "un fatto stabile e due elementi recenti con letture diverse"},
    44: {"object": "token e assegnazioni del router agli esperti", "input": "logits del router, top-k e capacità per esperto", "operation": "routing, dispatch, expert compute e combine", "output": "carico, token restituiti e costo attivo", "invariant": "parametri totali e parametri attivi non sono la stessa quantità", "example": "quattro token assegnati a due esperti con capacità limitata"},
    45: {"object": "unità di predizione dal byte al token multiplo", "input": "byte, gerarchia, target e numero di passi", "operation": "raggruppamento, multi-token prediction o diffusione discreta", "output": "unità predette, loss e durata di decoding", "invariant": "granularità della rappresentazione e parallelismo sono assi distinti", "example": "due byte raggruppati e due target predetti nello stesso passo"},
    46: {"object": "una coppia prompt-risposta nel formato di instruction tuning", "input": "messaggi, target, mask delle label e mixture", "operation": "teacher forcing e aggiornamento supervisionato", "output": "loss per token e comportamento adattato", "invariant": "il formato dei dati e le label decidono che cosa viene ottimizzato", "example": "un messaggio utente e una risposta con loss solo sulla risposta"},
    47: {"object": "l'aggiornamento adattivo rispetto ai pesi congelati", "input": "peso W, matrice A e B, rank e quantizzazione", "operation": "adapter, LoRA, prefix o QLoRA", "output": "delta W e checkpoint adattatore", "invariant": "il delta non è il modello completo e va valutato sullo stesso base model", "example": "delta W = B A con rank uno su una matrice piccola"},
    48: {"object": "dimostrazioni, preferenze, reward model e policy", "input": "prompt, risposta scelta, rifiutata e score", "operation": "fit del reward, KL e aggiornamento della policy", "output": "reward, log-probability e comportamento aggiornato", "invariant": "il reward è un proxy e può essere ottimizzato in modo scorretto", "example": "due risposte con margine di reward e penalità KL"},
    49: {"object": "una coppia chosen-rejected per l'ottimizzazione diretta", "input": "prompt, log-probability della policy e riferimento", "operation": "margine DPO, beta e variante offline", "output": "loss di preferenza e policy aggiornata", "invariant": "la preferenza osservata non è una verità assoluta", "example": "margine 0,8 con beta dichiarato e riferimento invariato"},
    50: {"object": "una traiettoria e il segnale di un verifier", "input": "passaggi, risposta finale, criterio e indipendenza", "operation": "process supervision, outcome supervision e verifica", "output": "score verificato e failure localizzata", "invariant": "un verifier può ereditare bias o essere ottimizzato", "example": "stesso risultato finale con un passaggio corretto e uno scorretto"},
    51: {"object": "una risposta valutata da una regola verificabile", "input": "prompt, rollout, gruppo di risposte e verifier", "operation": "reward verificabile, policy update e gestione di reward sparso", "output": "reward, vantaggio e nuova policy", "invariant": "la verificabilità vale solo per il dominio coperto dal verifier", "example": "tre rollout con due risposte che passano una regola"},
    52: {"object": "una traccia di reasoning e la risposta che la segue", "input": "prompt, trace del teacher, answer e costo in token", "operation": "distillazione, self-consistency e rejection sampling", "output": "traccia selezionata, risposta e misura di costo", "invariant": "una traccia leggibile non prova faithfulness causale", "example": "tre tracce, due concordanti, con selezione majority vote"},
    53: {"object": "un budget di compute aggiunto durante l'inferenza", "input": "prompt, numero di campioni, token e deadline", "operation": "best-of-n, tree search e adaptive compute", "output": "risposta, costo, latenza e qualità", "invariant": "qualità e costo devono essere riportati insieme", "example": "quattro campioni con un budget massimo di token"},
    54: {"object": "versioni di pesi e modifiche localizzate del modello", "input": "base model, delta, task e rollback point", "operation": "continued adaptation, merge, editing e regressione", "output": "versione nuova, diff e test di regressione", "invariant": "un merge senza valutazione può introdurre regressioni invisibili", "example": "due delta combinati e una capability testata prima e dopo"},
    55: {"object": "rappresentazioni di modalità differenti", "input": "testo, immagine, audio e maschere di modalità", "operation": "encoder, proiezione, alignment e fusion", "output": "spazio condiviso o output condizionato", "invariant": "allineamento misurato non equivale a comprensione generale", "example": "due vettori di modalità proiettati nella stessa dimensione"},
    56: {"object": "patch visivi e token linguistici in un VLM", "input": "immagine, patch, testo e query", "operation": "vision encoder, projector e cross-attention", "output": "token visivi, risposta e grounding", "invariant": "una risposta linguistica non certifica che il dettaglio sia nell'immagine", "example": "due patch aggregate e una domanda con riferimento locale"},
    57: {"object": "un contenuto immagine e la condizione che lo modifica", "input": "latent, prompt, mask e rumore", "operation": "denoising, guidance, editing o inpainting", "output": "immagine, score e metadati di provenienza", "invariant": "controllo dell'immagine e verità del contenuto sono proprietà diverse", "example": "una regione mascherata modificata lasciando il resto fissato"},
    58: {"object": "token interleaved e output di più modalità", "input": "sequenza testo-immagine-audio con mask", "operation": "backbone condiviso, routing e sincronizzazione", "output": "token o artefatto nella modalità richiesta", "invariant": "ordine, durata e maschera della modalità devono essere espliciti", "example": "testo e immagine alternati con due posizioni riservate"},
    59: {"object": "un segnale audio e la sua rappresentazione discreta", "input": "waveform, sample rate, spettrogramma o codec", "operation": "ASR, TTS, codec e generazione", "output": "testo, waveform o token audio", "invariant": "sample rate e durata fanno parte del contratto", "example": "una breve waveform convertita in frame e token"},
    60: {"object": "una sequenza di frame condizionata nel tempo", "input": "frame, latent video, testo e timestamp", "operation": "denoising, autoregressione e controllo temporale", "output": "frame coerenti e misura di flicker", "invariant": "qualità del singolo frame non dimostra coerenza tra frame", "example": "tre frame con un oggetto che deve mantenere posizione"},
    61: {"object": "punti e coordinate che descrivono una scena 3D", "input": "punti, camera, raggi e profondità", "operation": "proiezione, rendering, splatting o ricostruzione", "output": "immagine, campo radiance o geometria", "invariant": "una vista proiettata non determina da sola la scena completa", "example": "due punti proiettati con camera e profondità dichiarate"},
    62: {"object": "lo stato di un agente embodied nel mondo", "input": "osservazione, stato, azione e dinamica", "operation": "world model, planning, VLA e controllo", "output": "azione, stato previsto e risultato fisico", "invariant": "sim-to-real richiede una misura sul sistema reale", "example": "un'azione prevista in simulazione e il controllo del suo esito"},
    63: {"object": "query e documenti ordinati per rilevanza", "input": "query, corpus, termini e indice", "operation": "BM25, dense retrieval, ANN e reranking", "output": "ranking con score e documento recuperato", "invariant": "rilevanza del ranking e correttezza della risposta sono misure separate", "example": "tre documenti ordinati per sovrapposizione di termini"},
    64: {"object": "la pipeline che collega query, contesto e risposta", "input": "query, chunk, fonti e prompt", "operation": "chunking, retrieval, attribution e generazione", "output": "risposta con evidenza e score end-to-end", "invariant": "contesto recuperato e testo generato devono restare distinguibili", "example": "due chunk citati e una frase che non compare nelle fonti"},
    65: {"object": "una query instradata tra retriever e grafo", "input": "domanda multi-hop, nodi, archi e documenti", "operation": "query transformation, routing e corrective retrieval", "output": "sottoquery, percorso e contesto selezionato", "invariant": "un router può sbagliare anche quando il generatore è corretto", "example": "una domanda divisa in due sottoquery con un arco mancante"},
    66: {"object": "la decisione tra contesto, retrieval e memoria", "input": "segmento, query, budget e durata", "operation": "routing, scrittura episodica e recupero", "output": "contesto scelto, memoria aggiornata e costo", "invariant": "memoria persistente e contesto temporaneo hanno politiche diverse", "example": "un fatto stabile salvato e un dettaglio recente escluso"},
    67: {"object": "una chiamata a tool con schema e autorizzazione", "input": "nome, argomenti, scope e stato", "operation": "parsing, selezione, esecuzione e osservazione", "output": "risultato del tool o rifiuto tracciato", "invariant": "schema valido non significa permesso di eseguire il side effect", "example": "lookup consentito e refund rifiutato da allowlist"},
    68: {"object": "un messaggio tra componenti con identità e versione", "input": "capability, schema, token e policy", "operation": "negoziazione, encoding, autorizzazione e compatibilità", "output": "messaggio accettato o errore di protocollo", "invariant": "compatibilità sintattica non garantisce semantica o autorizzazione", "example": "due versioni dello schema con campo obbligatorio mancante"},
    69: {"object": "lo stato di una traiettoria agentica", "input": "osservazione, piano, azione e risultato del tool", "operation": "observe, plan, act, verify e terminate", "output": "stato successivo o arresto motivato", "invariant": "ogni side effect deve avere precondizioni e verifica", "example": "lookup, conferma utente e aggiornamento dell'ordine"},
    70: {"object": "una traiettoria composta da agenti e strumenti", "input": "task, ruoli, browser, codice e handoff", "operation": "delega, comunicazione, esecuzione e aggregazione", "output": "risultato con responsabilità e log per componente", "invariant": "più agenti ampliano anche superficie e costo dell'errore", "example": "un planner delega ricerca e verifica a due ruoli separati"},
    71: {"object": "traiettorie agentiche usate come dati e valutazione", "input": "task, trace, policy, outcome e costo", "operation": "SFT, RL, benchmark e harness", "output": "score di task, violazioni e failure per step", "invariant": "task riuscito e traiettoria sicura sono criteri distinti", "example": "due traiettorie con stesso esito ma una violazione di policy"},
    72: {"object": "una decisione agentica su una risorsa reale", "input": "input non fidato, tool, scope e approvazione", "operation": "least privilege, sandbox, human approval e rollback", "output": "allow/deny, side effect o rollback auditabile", "invariant": "l'enforcement deve stare fuori dal testo generato", "example": "refund bloccato e lookup consentito con log firmato"},
    73: {"object": "pesi del teacher, student e struttura da comprimere", "input": "logits teacher, target, pruning mask e budget", "operation": "distillazione, pruning e recovery", "output": "student più piccolo con loss e regressioni misurate", "invariant": "compressione e accuratezza vanno misurate sullo stesso perimetro", "example": "due logits trasferiti e una connessione potata con recovery"},
    74: {"object": "un tensore reale e la sua rappresentazione quantizzata", "input": "valori, scale, zero-point, dtype e calibrazione", "operation": "PTQ, QAT, weight-only o activation quantization", "output": "codici, tensore ricostruito, errore e memoria", "invariant": "scala e dominio di calibrazione fanno parte del risultato", "example": "tre valori quantizzati con scala 0,25 e errore massimo"},
    75: {"object": "un peso low-bit e il suo accumulo numerico", "input": "peso reale, codice ternario, scala e attivazione", "operation": "training nativo, STE e accumulazione", "output": "peso ricostruito, gradiente e costo hardware", "invariant": "bit nominali e precisione effettiva dell'accumulo sono distinti", "example": "peso {-1, 0, 1} con scala e accumulo in precisione maggiore"},
    76: {"object": "logits e spazio delle sequenze ammissibili", "input": "logits, prefisso, temperatura e vincolo", "operation": "greedy, beam, sampling, penalty e stop", "output": "token scelto, sequenza e metrica di costo", "invariant": "il decoding modifica la traiettoria, non corregge il modello a monte", "example": "greedy e top-p sullo stesso vettore di logits"},
    77: {"object": "draft e target durante il decoding speculativo", "input": "token proposti, logits draft e logits target", "operation": "proposta, verifica, accettazione e fallback", "output": "token accettati, velocità e distribuzione preservata", "invariant": "lo speedup richiede verifica senza cambiare il contratto di output", "example": "tre token proposti, due accettati e uno ricalcolato"},
    78: {"object": "blocchi di KV cache associati a una richiesta", "input": "layer, token, KV dimension, dtype e prefix", "operation": "prefill, decode, paging, caching ed eviction", "output": "cache occupata, hit e latenza", "invariant": "la cache deve rispettare ownership, posizione e validità del prefisso", "example": "due richieste condividono un prefisso e divergono al terzo token"},
    79: {"object": "richieste eterogenee in una coda di serving", "input": "prompt, deadline, lunghezza, memoria e priorità", "operation": "batching continuo, admission e scheduling", "output": "throughput, latency p50/p99 e richieste ammesse", "invariant": "throughput e latenza devono essere misurati insieme", "example": "una richiesta lunga e due brevi in un batch continuo"},
    80: {"object": "una richiesta distribuita tra compute e comunicazioni", "input": "shard, worker, rete, batch e fase prefill/decode", "operation": "parallelismo, disaggregazione, routing e recovery", "output": "risposta, trasferimenti e fault osservati", "invariant": "la comunicazione fa parte della latenza end-to-end", "example": "due worker con una sincronizzazione e un timeout"},
    81: {"object": "un grafo di operatori trasformato dal compiler", "input": "grafo, shape, dtype, target e kernel", "operation": "lowering, fusion, autotuning e gestione dei graph break", "output": "kernel eseguito, latenza e fallback", "invariant": "ottimizzazione del grafo e correttezza numerica devono essere confrontate", "example": "due operatori fusi con output numericamente equivalente"},
    82: {"object": "un servizio LLM dalla versione al consumo", "input": "modello, richieste, device, energia e monitor", "operation": "deploy, osservabilità, edge routing e cost accounting", "output": "versione attiva, costo per richiesta e alert", "invariant": "un costo locale non descrive l'intero ciclo di vita", "example": "costo per richiesta con energia e quota hardware separate"},
    83: {"object": "un claim valutativo e il protocollo che lo rende misurabile", "input": "task, dataset, predizioni, riferimento e metriche", "operation": "scelta della metrica, giudice, slice e report", "output": "stima, intervallo, errori e decisione", "invariant": "una metrica risponde solo alla domanda per cui è stata progettata", "example": "accuracy media accompagnata da una slice fallita"},
    84: {"object": "una risposta con evidenza, confidenza e possibilità di errore", "input": "claim, predizione, fonti e score di confidenza", "operation": "verifica, calibrazione, astensione e retrieval", "output": "risposta supportata o astensione motivata", "invariant": "confidenza alta non certifica la verità fattuale", "example": "tre risposte corrette e una confidente ma non supportata"},
    85: {"object": "un sistema composto da modello, contesto, tool e interfaccia", "input": "task, componenti, trace e policy", "operation": "eval end-to-end, stress, slice e monitoraggio", "output": "score di sistema, failure e regressione", "invariant": "misurare il modello isolato non misura il comportamento del sistema", "example": "un RAG che risponde bene ma cita una fonte irrilevante"},
    86: {"object": "un comportamento del modello e l'intervento che lo modifica", "input": "attivazioni, probe, attribution e baseline", "operation": "probing, attribution, causal intervention e circuit tracing", "output": "effetto osservato con controllo e confondenti", "invariant": "correlazione di una feature non prova causalità", "example": "ablazione di una componente e differenza rispetto alla baseline"},
    87: {"object": "un'attivazione scomposta in feature sparse", "input": "attivazione, dizionario, sparsità e ricostruzione", "operation": "training SAE, splitting, dead features e tracing", "output": "feature, errore di ricostruzione e circuito candidato", "invariant": "interpretabilità di una feature richiede valutazione e controlli indipendenti", "example": "due feature attive, una ricostruzione e un intervento"},
    88: {"object": "una superficie di attacco e il comportamento sotto perturbazione", "input": "threat model, prompt, budget e risposta", "operation": "jailbreak, perturbazione, difesa e adaptive evaluation", "output": "success rate, failure mode e costo della difesa", "invariant": "un test superato non copre minacce non incluse nel protocollo", "example": "stesso prompt con perturbazione e controllo di policy"},
    89: {"object": "istruzioni e dati che entrano in un sistema con tool", "input": "prompt, documento non fidato, tool e scope", "operation": "separazione, mediazione, allowlist e incident response", "output": "azione autorizzata o rifiuto con traccia", "invariant": "contenuto recuperato non diventa istruzione privilegiata", "example": "un documento chiede export dati ma il tool lo nega"},
    90: {"object": "gli artefatti che attraversano la supply chain del modello", "input": "dataset, checkpoint, repository, digest e owner", "operation": "poisoning, backdoor, extraction e controllo di provenienza", "output": "artefatto rilasciato, traccia e decisione di blocco", "invariant": "integrità del file non certifica assenza di contenuto malevolo", "example": "digest uguale ma dataset contaminato da una regola nascosta"},
    91: {"object": "un dato personale e il comportamento del sistema su gruppi diversi", "input": "record, membership, gruppo, label e budget privacy", "operation": "DP, fairness evaluation e unlearning", "output": "utility, leakage, disparità e verifica di rimozione", "invariant": "privacy, fairness e utility richiedono metriche e trade-off espliciti", "example": "stessa accuracy media con leakage e disparità per slice"},
    92: {"object": "un contenuto e la sua attestazione di provenienza", "input": "payload, metadata, manifest e chiave o watermark", "operation": "digest, firma, C2PA, watermark e detection", "output": "record verificabile e stato di rilevazione", "invariant": "provenienza dell'artefatto non certifica la verità del contenuto", "example": "digest di payload e metadati con verifica di una modifica"},
    93: {"object": "una decisione di governance su un sistema e il suo rischio", "input": "ruoli, uso previsto, evidenza, impatto e consumo", "operation": "govern, map, measure, manage, document e change control", "output": "decisione, responsabilità, evidenza e registro d'incidente", "invariant": "un framework orienta il rischio ma non certifica automaticamente la conformità", "example": "un caso d'uso assegnato a owner, misura, controllo e decisione di escalation"},
    94: {"object": "un esperimento didattico con ambiente e artefatti dichiarati", "input": "seed, dataset piccolo, config, codice e versione", "operation": "run, test, valutazione e report", "output": "loss, metriche, manifest e limite", "invariant": "un run locale non equivale a una prova generale", "example": "seed, split e dtype salvati prima dell'esecuzione"},
    95: {"object": "un piccolo language model dalla stringa ai logits", "input": "corpus, tokenizer, batch di sequenze e target", "operation": "embedding, decoder causale, cross-entropy e sampling", "output": "logits, loss, token generati e checkpoint", "invariant": "tokenizer, mask, target shift e sampling devono essere coerenti", "example": "due sequenze, target spostato di un token e loss calcolata"},
    96: {"object": "un sistema ML che attraversa sviluppo, rilascio e monitoraggio", "input": "problema, dati, modello, eval, deployment e rollback", "operation": "design, test, release, osservabilità e change management", "output": "servizio versionato con metriche e piano di ritorno", "invariant": "un modello che passa un test offline non è automaticamente pronto in produzione", "example": "release candidata con gate offline, canary e rollback"},
    97: {"object": "un claim di paper e il protocollo necessario per riprodurlo", "input": "paper, codice, dati, seed, hardware e metriche", "operation": "setup indipendente, run, confronto e analisi delle divergenze", "output": "risultato replicato o differenza spiegata", "invariant": "una replica richiede stesso claim e confini dichiarati, non solo stesso codice", "example": "due run con seed diversi e divergenza registrata"},
    98: {"object": "un claim di frontiera accompagnato da data e incertezza", "input": "paper, release, benchmark, fonte e data di osservazione", "operation": "scouting, routing, maturità, confronto e promozione", "output": "scheda con evidenza, stato e prossima verifica", "invariant": "novità, adozione e prova end-to-end sono dimensioni diverse", "example": "una tecnica nuova separata da benchmark, disponibilità e readiness"},
}


def topic_for(number: int, fallback: str | None = None) -> str:
    return CHAPTER_TOPIC.get(number, fallback or "lab")


def source_list_for(number: int, fallback: str, base_bank: dict) -> list[tuple[str, str]]:
    topic = topic_for(number, fallback)
    return SOURCE_BANKS.get(topic, base_bank.get(fallback, base_bank.get("labs", [])))


def detail_for(number: int, fallback: dict[str, dict[str, str]]) -> dict[str, str]:
    if number in DETAILS:
        return DETAILS[number]
    topic = topic_for(number)
    return fallback.get(topic, fallback.get("labs", {}))


def source_indices_for(number: int, section_count: int) -> list[int]:
    # Four dossier entries cover the five public transitions; the first source
    # is reused for the opening/closing boundary when a lesson has five parts.
    explicit = {
        # MCP belongs to its own section; A2A belongs to the following one.
        68: [0, 0, 1, 2, 3],
        # NIST covers the incident/change boundary; Green AI is reserved for
        # the sustainability section.
        93: [0, 1, 2, 0, 3],
        # C2PA covers provenance and policy, while watermarking covers both
        # the detector mechanism and its measurement boundary.
        92: [0, 1, 2, 2, 3],
        # The sources are ordered by the actual mechanism, not by publication
        # date: traces, distillation, consistency, faithfulness, cost.
        52: [0, 3, 1, 2, 0],
        51: [0, 0, 1, 2, 3],
        53: [0, 1, 2, 3, 0],
        54: [0, 3, 2, 1, 0],
        96: [0, 3, 1, 2, 0],
    }
    if number in explicit:
        values = explicit[number]
        return values[:section_count]
    if section_count <= 0:
        return []
    return [index % 4 for index in range(section_count)]
