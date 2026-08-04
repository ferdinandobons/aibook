# Piano editoriale. Capitolo 54

## Obiettivo didattico

Seguire **Aggiornamento, merging ed editing del modello** da base model, delta, task e rollback point a versione nuova, diff e test di regressione, osservando continued adaptation, merge, editing e regressione senza oltrepassare questo limite: un merge senza valutazione può introdurre regressioni invisibili.

## Prerequisiti reali

- Capitolo 31: Dalla rappresentazione linguistica agli LLM
- Capitolo 46: Supervised fine-tuning e instruction tuning
- Capitolo 49: Ottimizzazione diretta delle preferenze

## Percorso della lezione

1. **Continued adaptation.** Nuovi dati e obiettivi aggiornano il checkpoint. Replay, regolarizzazione e valutazioni controllano forgetting e regressioni. Prova: SRC-54-001.
2. **Task arithmetic.** Differenze tra checkpoint possono essere combinate come vettori. La compatibilità richiede stessa base e corrispondenza dei parametri. Prova: SRC-54-004.
3. **TIES e DARE.** Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. I risultati dipendono dai task e dalla scala dei delta. Prova: SRC-54-003.
4. **Model editing.** ROME, MEMIT e famiglie affini cercano modifiche localizzate. Località, generalizzazione e side effect devono essere misurati separatamente. Prova: SRC-54-002.
5. **Versioning e rollback.** Un update produce un nuovo artefatto con fonti, test e dipendenze. Merging ed editing non sostituiscono la gestione delle versioni. Prova: SRC-54-001.

## Prove e artefatti

- riferimento minimo: `code/snip_54_contract.py`; test: `code/test_54_contract.py`; output: `code/outputs/SNIP-54-001.txt`.
- visuali candidate: UPDATE-01, UPDATE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
