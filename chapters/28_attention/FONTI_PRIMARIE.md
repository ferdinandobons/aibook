# Capitolo 28. Dossier delle fonti primarie

Data prima ricognizione: 30 luglio 2026

## Origini dell’attention nelle architetture encoder-decoder

1. Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio. **Neural Machine Translation by Jointly Learning to Align and Translate**. arXiv:1409.0473, 2014.
   - Fonte primaria: https://arxiv.org/abs/1409.0473
   - Uso previsto: limite del vettore di contesto fisso, allineamento soft, attention additiva.

2. Thang Luong, Hieu Pham, Christopher D. Manning. **Effective Approaches to Attention-based Neural Machine Translation**. EMNLP 2015, ACL Anthology D15-1166.
   - Atti ufficiali: https://aclanthology.org/D15-1166/
   - DOI: 10.18653/v1/D15-1166
   - Uso previsto: global e local attention, funzioni di scoring, terminologia storica.

## Scaled dot-product attention e multi-head attention

3. Ashish Vaswani et al. **Attention Is All You Need**. NeurIPS 2017.
   - Atti ufficiali: https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
   - Uso previsto: scaled dot-product attention, multi-head attention, mask, complessità e architettura Transformer originale.

## Implementazione ufficiale corrente

4. PyTorch. **torch.nn.functional.scaled_dot_product_attention**.
   - Documentazione ufficiale: https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
   - Versione osservata il 30 luglio 2026: documentazione stabile PyTorch 2.13.
   - Uso previsto: firma corrente, shape, mask, dropout, `enable_gqa` e backend.
   - Nota da verificare nel capitolo: nella boolean mask di questa API, `True` indica una posizione ammessa.

5. PyTorch. **torch.nn.MultiheadAttention**.
   - Documentazione ufficiale: https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html
   - Versione osservata il 30 luglio 2026: documentazione stabile PyTorch 2.13.
   - Uso previsto: contratto API, fast path e rapporto con scaled dot-product attention.
   - Nota da verificare nel capitolo: la semantica delle boolean mask non coincide in tutti i parametri con quella di `scaled_dot_product_attention`.

6. PyTorch. **torch.nn.attention.sdpa_kernel** e **SDPBackend**.
   - https://docs.pytorch.org/docs/stable/generated/torch.nn.attention.sdpa_kernel.html
   - https://docs.pytorch.org/docs/stable/generated/torch.nn.attention.SDPBackend.html
   - Uso previsto: selezione esplicita del backend e test riproducibili.

## Ottimizzazioni e varianti avanzate

7. Tri Dao et al. **FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness**. arXiv:2205.14135, 2022.
   - Fonte primaria: https://arxiv.org/abs/2205.14135
   - Uso previsto: data movement, tiling, attenzione esatta IO-aware.

8. Tri Dao. **FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning**. arXiv:2307.08691, 2023.
   - Fonte primaria: https://arxiv.org/abs/2307.08691
   - Uso previsto: approfondimento su parallelismo e work partitioning.

9. Noam Shazeer. **Fast Transformer Decoding: One Write-Head is All You Need**. arXiv:1911.02150, 2019.
   - Fonte primaria: https://arxiv.org/abs/1911.02150
   - Uso previsto: multi-query attention e costo della KV cache in decoding incrementale.

10. Joshua Ainslie et al. **GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints**. arXiv:2305.13245, 2023.
    - Fonte primaria: https://arxiv.org/abs/2305.13245
    - Uso previsto: grouped-query attention e relazione tra MHA e MQA.

## Regole di utilizzo

- Le fonti 7-10 compariranno soltanto dopo la stabilizzazione del caso base.
- I risultati quantitativi dei paper non saranno trasferiti a hardware o versioni diverse senza dichiararlo.
- La documentazione PyTorch sarà ricontrollata nel giorno in cui verrà congelato il codice del capitolo.
- Le varianti più recenti dell’attention saranno cercate nuovamente prima dell’approvazione finale.
- Ogni dato numerico nelle visuali verrà ricalcolato indipendentemente prima dell’approvazione.
