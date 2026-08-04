# Piano editoriale. Capitolo 35

## Obiettivo didattico

Seguire **La ricetta di pretraining** da batch, learning rate, seed, optimizer e checkpoint a loss, parametri e checkpoint ripristinabile, osservando forward, backward, update, schedule e recovery senza oltrepassare questo limite: un checkpoint deve includere lo stato necessario a continuare il run.

## Prerequisiti reali

- Capitolo 16: Addestrare reti profonde
- Capitolo 32: Il ciclo di vita dei dati
- Capitolo 33: Dataset mixture, curriculum e dati sintetici
- Capitolo 34: Scaling law e progettazione del modello

## Percorso della lezione

1. **Batch di token.** Packing, padding e mask determinano quanti token validi contribuiscono alla loss. Prova: SRC-35-001.
2. **Inizializzazione.** Scala dei pesi e residual deve restare coerente con profondità, norm e dtype. Prova: SRC-35-002.
3. **AdamW.** Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer. Prova: SRC-35-003.
4. **Warmup e schedule.** Il learning rate dipende da step o token e deve riprendere dal contatore corretto. Prova: SRC-35-004.
5. **Checkpoint e recovery.** Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele. Prova: SRC-35-001.

## Prove e artefatti

- riferimento minimo: `code/snip_35_contract.py`; test: `code/test_35_contract.py`; output: `code/outputs/SNIP-35-001.txt`.
- visuali candidate: RECIPE-01, RECIPE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
