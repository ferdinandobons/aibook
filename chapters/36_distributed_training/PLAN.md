# Piano editoriale. Capitolo 36

## Obiettivo didattico

Seguire **Training distribuito e continued pretraining** da microbatch, worker, shard e topologia a gradiente ridotto, stato sincronizzato e fault osservato, osservando all-reduce, sharding, pipeline e recovery senza oltrepassare questo limite: la riduzione e il conteggio del batch devono essere dichiarati.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 16: Addestrare reti profonde
- Capitolo 35: La ricetta di pretraining

## Percorso della lezione

1. **Data parallelism.** Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti. Prova: SRC-36-001.
2. **ZeRO e FSDP.** Parametri, gradienti e optimizer state vengono shardati tra worker. Prova: SRC-36-002.
3. **Tensor e pipeline parallelism.** Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch. Prova: SRC-36-003.
4. **Topologia e fault tolerance.** Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta. Prova: SRC-36-004.
5. **Continued pretraining.** Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate. Prova: SRC-36-001.

## Prove e artefatti

- riferimento minimo: `code/snip_36_contract.py`; test: `code/test_36_contract.py`; output: `code/outputs/SNIP-36-001.txt`.
- visuali candidate: DIST-01, DIST-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
