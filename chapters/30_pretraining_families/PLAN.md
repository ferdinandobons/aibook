# Piano editoriale. Capitolo 30

## Obiettivo didattico

Seguire **Famiglie architetturali e obiettivi di pretraining** da sequenza, mask e target di pretraining a rappresentazione o distribuzione predittiva, osservando encoder, decoder, span corruption o causal prediction senza oltrepassare questo limite: architettura e objective non possono essere scambiati senza cambiare il compito.

## Prerequisiti reali

- Capitolo 28: Il meccanismo di attention
- Capitolo 29: Il Transformer da zero

## Percorso della lezione

1. **Encoder-only.** Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione. Prova: SRC-30-001.
2. **Decoder-only.** Un decoder causale predice token successivi e supporta generazione incrementale. Prova: SRC-30-002.
3. **Encoder-decoder.** T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention. Prova: SRC-30-003.
4. **Masked, causal e span corruption.** Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss. Prova: SRC-30-004.
5. **Architettura e obiettivo.** La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti. Prova: SRC-30-001.

## Prove e artefatti

- eccezione motivata: Il capitolo è una mappa tra architetture e obiettivi; il Transformer eseguibile è nel capitolo 29 e le ricette di training iniziano dal 32.
- visuali candidate: FAMILIES-01, FAMILIES-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
