# Piano editoriale. Capitolo 42

## Obiettivo didattico

Seguire **State-space model, recurrence e long convolution** da x_t, stato s_t e matrici A, B, C a stato e uscita per ogni posizione, osservando recurrence, convolutione lunga o selezione senza oltrepassare questo limite: stabilità e discretizzazione fanno parte dell'implementazione.

## Prerequisiti reali

- Capitolo 18: Reti ricorrenti e modelli sequenziali
- Capitolo 29: Il Transformer da zero
- Capitolo 41: Linear attention, fast weights e delta rule

## Percorso della lezione

1. **State-space model.** Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale. Prova: SRC-42-001.
2. **S4.** Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili. Prova: SRC-42-002.
3. **Mamba.** Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware. Prova: SRC-42-003.
4. **Hyena e long convolution.** Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise. Prova: SRC-42-004.
5. **RWKV, RetNet, xLSTM e Griffin.** Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti. Prova: SRC-42-001.

## Prove e artefatti

- riferimento minimo: `code/snip_42_contract.py`; test: `code/test_42_contract.py`; output: `code/outputs/SNIP-42-001.txt`.
- visuali candidate: SSM-01, SSM-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
