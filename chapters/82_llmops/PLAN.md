# Piano editoriale. Capitolo 82

## Obiettivo didattico

Seguire **LLMOps, edge, costo ed energia** da modello, richieste, device, energia e monitor a versione attiva, costo per richiesta e alert, osservando deploy, osservabilità, edge routing e cost accounting senza oltrepassare questo limite: un costo locale non descrive l'intero ciclo di vita.

## Prerequisiti reali

- Capitolo 3: Il ciclo di vita di un sistema di AI
- Capitolo 79: Serving, batching e scheduling
- Capitolo 81: Compiler, kernel e runtime

## Percorso della lezione

1. **Dalla versione al deployment.** Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema. Prova: SRC-82-001.
2. **Osservabilità.** Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario. Prova: SRC-82-002.
3. **Edge.** Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Offline e privacy possono motivare il deployment locale. Prova: SRC-82-003.
4. **Costo.** Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e batching modificano l'allocazione. Prova: SRC-82-004.
5. **Energia e sostenibilità.** Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono dichiarare confini e metodologia. Prova: SRC-82-001.

## Prove e artefatti

- riferimento minimo: `code/snip_82_contract.py`; test: `code/test_82_contract.py`; output: `code/outputs/SNIP-82-001.txt`.
- visuali candidate: LLMOPS-01, LLMOPS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
