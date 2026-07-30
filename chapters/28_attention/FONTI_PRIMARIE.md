# Fonti primarie e documentazione. Capitolo 28

Data dell'ultima verifica: **30 luglio 2026**.

## SRC-ATT-001. Attention Is All You Need

- Autori: Ashish Vaswani et al.
- Sede: Advances in Neural Information Processing Systems 30, 2017.
- Fonte ufficiale: https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
- Sezioni usate: §3.2, §3.2.1 e, soltanto come ponte al capitolo successivo, §3.2.2.
- Sostiene: scaled dot-product attention, fattore `1/sqrt(d_k)`, causal masking e collocazione della multi-head attention.
- Limite: descrive il Transformer originale, non tutte le implementazioni successive.

## SRC-ATT-002. Neural Machine Translation by Jointly Learning to Align and Translate

- Autori: Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio.
- Versione primaria: arXiv:1409.0473, accettato a ICLR 2015.
- URL: https://arxiv.org/abs/1409.0473
- Uso nel dossier: contesto storico sul limite del vettore di contesto fisso nel modello studiato dagli autori.
- Limite: il meccanismo non coincide con la scaled dot-product attention del Transformer. Il confronto `ATT-01` del capitolo resta dichiarato come illustrativo.

## SRC-ATT-003. PyTorch stable 2.13. scaled_dot_product_attention

- Organizzazione: PyTorch Foundation.
- Documentazione: https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention
- Versione risolta dalla pagina stable alla verifica: `2.13`.
- Sostiene: firma dell'API, shape, default scale, semantica della mask booleana, `is_causal`, dropout e backends.
- Limite: il codice è stato eseguito localmente con PyTorch `2.10.0+cpu`, non con `2.13`.

## SRC-ATT-004. PyTorch stable 2.13. MultiheadAttention

- Documentazione: https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention
- Versione: `2.13`.
- Uso nel capitolo: confronto della semantica di `key_padding_mask` e localizzazione del capitolo successivo.
- Limite: la classe è un'implementazione di riferimento e non rappresenta tutte le architetture moderne.

## Divergenze e note

1. Le mask booleane non hanno la stessa semantica in tutte le API PyTorch. Il testo distingue `F.scaled_dot_product_attention` e `MultiheadAttention.key_padding_mask` soltanto dopo aver stabilizzato la mask matematica.
2. La documentazione stable consultata è `2.13`; l'ambiente eseguito è `2.10.0+cpu`.
3. I risultati numerici sono illustrativi oppure prodotti dai file registrati. Non sono benchmark.
4. La spiegazione interna di FlashAttention è stata rimossa dal capitolo base dopo la review didattica. Le implementazioni hardware-aware restano un confine rinviato alla Parte `P12`.
