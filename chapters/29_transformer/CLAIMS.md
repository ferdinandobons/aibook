# Claim

- `CL-TRANSFOR-001`. La mappa completa: Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape.
- `CL-TRANSFOR-002`. Encoder: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni.
- `CL-TRANSFOR-003`. Decoder: Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder.
- `CL-TRANSFOR-004`. Multi-head attention: Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello.
- `CL-TRANSFOR-005`. Residual stream e output: Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario.
