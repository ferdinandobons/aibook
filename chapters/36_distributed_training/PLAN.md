# Piano interno. Capitolo 36

- `chapter_id`: `CH-P07-DISTRIBUTED-TRAINING`
- Parte: `P07`
- Titolo: Training distribuito e continued pretraining
- Maturità: `CORE`
- Stato: candidatura completa in revisione autoriale

## Continuità

- Prerequisiti stabili: ricetta di pretraining, autograd e mixed precision.
- Gap: un dispositivo non contiene modello, attivazioni e optimizer.
- Output: mappa di data, tensor, pipeline e sharded parallelism.
- Consumer successivo: Capitolo 37.
- Concetti differiti: dettagli avanzati non necessari al caso base.

## Visuali

- `DIST-01`: Quattro dimensioni di parallelismo.
- `DIST-02`: Continued pretraining.
