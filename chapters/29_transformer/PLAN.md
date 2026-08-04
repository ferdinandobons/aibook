# Piano editoriale. Capitolo 29

## Obiettivo didattico

Seguire **Il Transformer da zero** da tokenizzati di shape [batch, length] e vettori [batch, length, d] a stato contestuale e logits, osservando embedding, attention, MLP e residuo senza oltrepassare questo limite: mask, shape e percorso residuale devono essere compatibili.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 27: Embedding e spazio semantico
- Capitolo 28: Il meccanismo di attention

## Percorso della lezione

1. **La mappa completa.** Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape. Prova: SRC-29-001.
2. **Encoder.** L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni. Prova: SRC-29-002.
3. **Decoder.** Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder. Prova: SRC-29-003.
4. **Multi-head attention.** Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello. Prova: SRC-29-004.
5. **Residual stream e output.** Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario. Prova: SRC-29-001.

## Prove e artefatti

- riferimento minimo: `code/snip_29_contract.py`; test: `code/test_29_contract.py`; output: `code/outputs/SNIP-29-001.txt`.
- visuali candidate: TRANSFOR-01, TRANSFOR-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
