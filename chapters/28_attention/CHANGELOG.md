# Changelog. Capitolo 28

## 0.3.0-rc3. 30 luglio 2026

### Riscrittura della superficie editoriale

- Riaperta la review didattica dopo il feedback sulla ripetizione delle intestazioni metacognitive.
- Registrata `DID-ATT-03`, con esito respinto per struttura visibile troppo simile a una checklist.
- Rimossi dal corpo i blocchi ripetitivi `Stato del lettore`, `Dove siamo`, `Problema locale`, `Cosa è cambiato`, `Cosa è rimasto invariato`, `Cosa non fa`, `Frase di continuità` e `Contratto dello snippet`.
- Mantenute le stesse funzioni logiche all'interno di paragrafi naturali.
- Sostituiti i titoli metacognitivi con titoli semantici legati a problemi e meccanismi.
- Integrati shape, invarianti, confini e passaggi successivi nella prosa.
- Conservata la sequenza verificata: esempio, pseudocodice, formula, implementazione, API e confini.
- Mantenuta l'ispezione completa di `ATT-01` e `ATT-02` senza etichette editoriali rigide.
- Registrata `DID-ATT-04`, seconda lettura completa della versione in prosa con esito superato.

### Governance

- Aggiunto `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`.
- Riscritto `docs/01_TEMPLATE_CAPITOLO.md` distinguendo scaffold interno e superficie destinata al lettore.
- Aggiornati `EXPLANATION_STYLE_AND_VISUALS.md` e `docs/18_PROTOCOLLO_QA_DIDATTICO.md` con un gate anti-template.
- Aggiornato `docs/README.md` con il nuovo ordine di lettura.

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
- Registrata `DID-ATT-02`, seconda lettura completa con esito tecnico superato.

### Governance

- Aggiunto `docs/18_PROTOCOLLO_QA_DIDATTICO.md`.
- Resa obbligatoria almeno una review didattica completa per ogni capitolo.
- Resa obbligatoria una nuova review integrale dopo ogni correzione di un difetto bloccante.

## 0.1.0-rc1. 30 luglio 2026

- Prima candidatura completa per review autoriale.
- Aggiunti testo, fonti, claim, audit, quattro snippet e due figure candidate.
- Rigenerate le figure v2 dopo il rilevamento di blob corrotti e problemi di contenimento.