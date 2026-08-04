# Piano editoriale. Capitolo 85

## Obiettivo didattico

Seguire **Valutare contesto lungo, RAG, multimodalità e agenti** da task, componenti, trace e policy a score di sistema, failure e regressione, osservando eval end-to-end, stress, slice e monitoraggio senza oltrepassare questo limite: misurare il modello isolato non misura il comportamento del sistema.

## Prerequisiti reali

- Capitolo 3: Il ciclo di vita di un sistema di AI
- Capitolo 67: Output strutturato e uso degli strumenti
- Capitolo 83: Progettare una valutazione

## Percorso della lezione

1. **Contesto lungo.** Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale. Prova: SRC-85-001.
2. **RAG.** Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili. Prova: SRC-85-002.
3. **Multimodalità.** Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche. Prova: SRC-85-003.
4. **Agenti.** Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili. Prova: SRC-85-004.
5. **Evaluation in production.** Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli. Prova: SRC-85-001.

## Prove e artefatti

- riferimento minimo: `code/snip_85_contract.py`; test: `code/test_85_contract.py`; output: `code/outputs/SNIP-85-001.txt`.
- visuali candidate: EVAL-01, EVAL-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
