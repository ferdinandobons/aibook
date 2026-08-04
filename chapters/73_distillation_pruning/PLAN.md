# Piano editoriale. Capitolo 73

## Obiettivo didattico

Seguire **Distillazione e pruning** da logits teacher, target, pruning mask e budget a student più piccolo con loss e regressioni misurate, osservando distillazione, pruning e recovery senza oltrepassare questo limite: compressione e accuratezza vanno misurate sullo stesso perimetro.

## Prerequisiti reali

- Capitolo 16: Addestrare reti profonde
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Teacher e student.** La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student. Prova: SRC-73-001.
2. **Temperature e loss.** Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente. Prova: SRC-73-002.
3. **Sequence distillation.** Per modelli generativi, risposte del teacher diventano un nuovo dataset. Filtri e diversità determinano ciò che lo student vede. Prova: SRC-73-003.
4. **Pruning.** Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware. Prova: SRC-73-004.
5. **Recovery.** Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve includere memoria, latency e regressioni per slice. Prova: SRC-73-001.

## Prove e artefatti

- riferimento minimo: `code/snip_73_contract.py`; test: `code/test_73_contract.py`; output: `code/outputs/SNIP-73-001.txt`.
- visuali candidate: PRUNING-01, PRUNING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
