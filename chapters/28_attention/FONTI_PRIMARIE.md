# Fonti primarie e documentazione. Capitolo 28

Data dell'ultima verifica: **30 luglio 2026**.

## SRC-ATT-001. Attention Is All You Need

- Autori: Ashish Vaswani et al.
- Sede: Advances in Neural Information Processing Systems 30, 2017.
- Fonte ufficiale: https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
- PDF ufficiale: link `Paper` nella pagina degli atti.
- Sezioni usate: §3.2, §3.2.1, §3.2.2; tabella di complessità per il contesto storico.
- Sostiene: scaled dot-product attention, fattore `1/sqrt(d_k)`, multi-head attention, causal masking nel decoder.
- Limite: descrive il Transformer originale, non tutte le implementazioni successive.

## SRC-ATT-002. Neural Machine Translation by Jointly Learning to Align and Translate

- Autori: Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio.
- Versione primaria: arXiv:1409.0473, accettato a ICLR 2015.
- URL: https://arxiv.org/abs/1409.0473
- Sezioni usate: abstract e definizione del meccanismo di allineamento nel paper.
- Sostiene: critica del vettore di contesto fisso nell'encoder-decoder studiato e soft search delle parti rilevanti della sequenza sorgente.
- Limite: il meccanismo non coincide con la scaled dot-product attention del Transformer.

## SRC-ATT-003. Effective Approaches to Attention-based Neural Machine Translation

- Autori: Minh-Thang Luong, Hieu Pham, Christopher D. Manning.
- Sede: EMNLP 2015, ACL Anthology D15-1166.
- URL: https://aclanthology.org/D15-1166/
- Sezioni usate: definizioni delle varianti global e local e delle funzioni di score.
- Sostiene: pluralità delle formulazioni di attention precedenti al Transformer.
- Limite: non definisce la scaled dot-product attention del Transformer.

## SRC-ATT-004. PyTorch stable 2.13. scaled_dot_product_attention

- Organizzazione: PyTorch Foundation.
- Documentazione: https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention
- Versione risolta dalla pagina stable alla verifica: `2.13`.
- Sostiene: firma dell'API, shape, default scale, mask booleana, `is_causal`, dropout, backends e GQA sperimentale.
- Limite: il codice del capitolo è stato eseguito localmente con PyTorch `2.10.0+cpu`, non con `2.13`.

## SRC-ATT-005. PyTorch stable 2.13. MultiheadAttention

- Documentazione: https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention
- Versione: `2.13`.
- Sostiene: firma, shape, formula multi-head, comportamento di `average_attn_weights`, semantica di `key_padding_mask`, uso dell'SDPA ottimizzata quando possibile.
- Limite: la classe è descritta dalla documentazione come implementazione di riferimento e non rappresenta tutte le architetture moderne.

## SRC-ATT-006. FlashAttention

- Autori: Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré.
- Titolo: *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness*.
- URL: https://arxiv.org/abs/2205.14135
- Sezioni usate: §§1, 2.2 e 3.
- Sostiene: attenzione esatta IO-aware, tiling, riduzione degli accessi HBM e mancata materializzazione completa degli intermedi in HBM.
- Limite: risultati prestazionali dipendono da hardware, implementazione e setup; il capitolo non riporta benchmark propri.

## Divergenze e note

1. Le mask booleane non hanno la stessa semantica in tutte le API PyTorch. Il testo distingue esplicitamente `F.scaled_dot_product_attention` e `MultiheadAttention.key_padding_mask`.
2. La documentazione stable consultata è `2.13`; l'ambiente disponibile per l'esecuzione è `2.10.0+cpu`.
3. I risultati numerici nel capitolo sono illustrativi o prodotti dai file registrati. Non sono benchmark.
