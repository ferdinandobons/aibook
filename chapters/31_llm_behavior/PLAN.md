# Piano editoriale. Capitolo 31

## Obiettivo didattico

Seguire **Dalla rappresentazione linguistica agli LLM** da prefisso tokenizzato, esempi e temperatura dichiarati a logits, risposta e confidenza misurabile, osservando in-context learning, decoding e calibrazione senza oltrepassare questo limite: probabilità, comportamento osservato e correttezza non sono sinonimi.

## Prerequisiti reali

- Capitolo 26: Il testo come dato
- Capitolo 29: Il Transformer da zero
- Capitolo 30: Famiglie architetturali e obiettivi di pretraining

## Percorso della lezione

1. **Distribuzione del token successivo.** Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce una distribuzione, non una risposta già scelta. Prova: SRC-31-001.
2. **Prompt e dimostrazioni.** Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta invariato durante in-context learning. Prova: SRC-31-002.
3. **Decoding.** Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria. Prova: SRC-31-003.
4. **Calibrazione.** Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti. Prova: SRC-31-004.
5. **Modello e sistema.** Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato. Prova: SRC-31-001.

## Prove e artefatti

- riferimento minimo: `code/snip_31_contract.py`; test: `code/test_31_contract.py`; output: `code/outputs/SNIP-31-001.txt`.
- visuali candidate: LLM-01, LLM-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
