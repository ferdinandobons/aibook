# Piano editoriale. Capitolo 67

## Obiettivo didattico

Seguire **Output strutturato e uso degli strumenti** da nome, argomenti, scope e stato a risultato del tool o rifiuto tracciato, osservando parsing, selezione, esecuzione e osservazione senza oltrepassare questo limite: schema valido non significa permesso di eseguire il side effect.

## Prerequisiti reali

- Capitolo 31: Dalla rappresentazione linguistica agli LLM
- Capitolo 64: Retrieval-Augmented Generation

## Percorso della lezione

1. **Schema dell'output.** JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non garantisce correttezza semantica. Prova: SRC-67-001.
2. **Selezione del tool.** Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e autorizzazioni influenzano la decisione. Prova: SRC-67-002.
3. **Argomenti.** Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi mancanti richiedono chiarimento o fallback. Prova: SRC-67-003.
4. **Esecuzione e osservazione.** Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Timeout ed errori devono essere rappresentati. Prova: SRC-67-004.
5. **Idempotenza e side effect.** Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate. Prova: SRC-67-001.

## Prove e artefatti

- riferimento minimo: `code/snip_67_contract.py`; test: `code/test_67_contract.py`; output: `code/outputs/SNIP-67-001.txt`.
- visuali candidate: TOOLS-01, TOOLS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
