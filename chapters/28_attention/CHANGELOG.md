# Changelog. Capitolo 28

## 0.2.0-rc2. 30 luglio 2026

### Riscrittura didattica

- Riaperta la review didattica dopo il confronto con `EXPLANATION_STYLE_AND_VISUALS.md`.
- Registrata `DID-ATT-01`, con esito respinto e dieci difetti bloccanti.
- Descritti i ruoli prima dei termini query, key e value.
- Spostato il nome scaled dot-product attention dopo l'esempio completo e il pseudocodice.
- Aggiunti stato accumulato, blocchi atomici e frasi di continuità.
- Attraversate `ATT-01` e `ATT-02` nella prosa con inquadramento, ispezione e conclusione.
- Separata la mask matematica dalle convenzioni delle API PyTorch.
- Separata la nota sul dropout dal confronto formula/API.
- Ridotta la multi-head attention a ponte verso il capitolo successivo.
- Ridotte le implementazioni hardware-aware a confine.
- Rimosso `SNIP-ATT-004` dal capitolo, dai test e dagli output.
- Rieseguiti i tre test pertinenti.
- Registrata `DID-ATT-02`, seconda lettura completa con esito superato.

### Governance

- Aggiunto `docs/18_PROTOCOLLO_QA_DIDATTICO.md`.
- Resa obbligatoria almeno una review didattica completa per ogni capitolo.
- Resa obbligatoria una nuova review integrale dopo ogni correzione di un difetto bloccante.

## 0.1.0-rc1. 30 luglio 2026

- Prima candidatura completa per review autoriale.
- Aggiunti testo, fonti, claim, audit, quattro snippet e due figure candidate.
- Rigenerate le figure v2 dopo il rilevamento di blob corrotti e problemi di contenimento.
