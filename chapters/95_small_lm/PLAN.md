# Piano editoriale. Capitolo 95

## Obiettivo didattico

Seguire **Costruire un piccolo language model** da corpus, tokenizer, batch di sequenze e target a logits, loss, token generati e checkpoint, osservando embedding, decoder causale, cross-entropy e sampling senza oltrepassare questo limite: tokenizer, mask, target shift e sampling devono essere coerenti.

## Prerequisiti reali

- Capitolo 26: Il testo come dato
- Capitolo 28: Il meccanismo di attention
- Capitolo 29: Il Transformer da zero
- Capitolo 35: La ricetta di pretraining
- Capitolo 94: Percorso pratico dai fondamenti

## Percorso della lezione

1. **Corpus e tokenizer.** Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili. Prova: SRC-95-001.
2. **Decoder Transformer.** Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape. Prova: SRC-95-002.
3. **Training.** AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU. Prova: SRC-95-003.
4. **Sampling.** Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria. Prova: SRC-95-004.
5. **Limiti.** Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto. Prova: SRC-95-001.

## Prove e artefatti

- riferimento minimo: `code/snip_95_contract.py`; test: `code/test_95_contract.py`; output: `code/outputs/SNIP-95-001.txt`.
- laboratorio esteso: `code/tiny_transformer_lm.py`; test: `code/test_tiny_transformer_lm.py`; output: `code/outputs/TINY-TRANSFORMER-LM.txt`.
- visuali candidate: LM-01, LM-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
