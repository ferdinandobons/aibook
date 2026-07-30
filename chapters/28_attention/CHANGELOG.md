# Changelog. Capitolo 28

## 0.1.0-rc1. 30 luglio 2026

- Prima candidatura completa per review autoriale.
- Aggiunti testo, fonti, claim e audit.
- Aggiunti quattro snippet, test e output.
- Incluse due figure tecniche candidate.
- Escluse le rappresentazioni raster delle pagine del libro.

### Revisione visuale v2

- Rimosse `ATT-01/candidate-v1.png` e `ATT-02/candidate-v1.png` perché i blob erano corrotti e non revisionabili.
- Rigenerate `ATT-01/candidate-v2.png` e `ATT-02/candidate-v2.png`.
- Corretto il collegamento ambiguo tra il contesto fisso e le query in `ATT-01`.
- Separati query, coefficienti e output in celle distinte.
- Ridisposti input, score, scaling, softmax, somma pesata e output in `ATT-02`.
- Ricontrollati tutti i valori numerici di `ATT-02`.
- Aggiunto un gate vincolante per testo debordante, tagliato, sovrapposto o privo di padding.
- Aggiunti `docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` e il renderer riproducibile `scripts/render_attention_visuals.py`.
- Entrambe le figure v2 sono validate tecnicamente e attendono l'approvazione autoriale.
