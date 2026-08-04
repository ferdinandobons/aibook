# Piano editoriale. Capitolo 78

## Obiettivo didattico

Seguire **KV cache e riuso del contesto** da layer, token, KV dimension, dtype e prefix a cache occupata, hit e latenza, osservando prefill, decode, paging, caching ed eviction senza oltrepassare questo limite: la cache deve rispettare ownership, posizione e validità del prefisso.

## Prerequisiti reali

- Capitolo 29: Il Transformer da zero
- Capitolo 39: Varianti dell'attention e gestione KV
- Capitolo 76: Decoding e generazione vincolata

## Percorso della lezione

1. **Prefill e decode.** Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente. Prova: SRC-78-001.
2. **Layout.** Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel. Prova: SRC-78-002.
3. **PagedAttention.** Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa. Prova: SRC-78-003.
4. **Prefix caching.** Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili. Prova: SRC-78-004.
5. **Compressione ed eviction.** Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile. Prova: SRC-78-001.

## Prove e artefatti

- riferimento minimo: `code/snip_78_contract.py`; test: `code/test_78_contract.py`; output: `code/outputs/SNIP-78-001.txt`.
- visuali candidate: CACHE-01, CACHE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
