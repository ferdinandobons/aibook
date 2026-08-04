# Piano editoriale. Capitolo 46

## Obiettivo didattico

Seguire **Supervised fine-tuning e instruction tuning** da messaggi, target, mask delle label e mixture a loss per token e comportamento adattato, osservando teacher forcing e aggiornamento supervisionato senza oltrepassare questo limite: il formato dei dati e le label decidono che cosa viene ottimizzato.

## Prerequisiti reali

- Capitolo 26: Il testo come dato
- Capitolo 29: Il Transformer da zero
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Dal pretraining alle istruzioni.** Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate. Prova: SRC-46-001.
2. **Formati conversazionali.** Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. Prova: SRC-46-002.
3. **Instruction mixture.** Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile. Prova: SRC-46-003.
4. **Teacher forcing e generalizzazione.** Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati. Prova: SRC-46-004.
5. **Catastrophic forgetting e controllo.** Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili. Prova: SRC-46-001.

## Prove e artefatti

- riferimento minimo: `code/snip_46_contract.py`; test: `code/test_46_contract.py`; output: `code/outputs/SNIP-46-001.txt`.
- visuali candidate: SFT-01, SFT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
