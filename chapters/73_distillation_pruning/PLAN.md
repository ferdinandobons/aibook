# Piano interno. Capitolo 73

- Domanda centrale: quale contratto costruisce Distillazione e pruning?
- Oggetto continuo: pesi del teacher, student e struttura da comprimere; input guida: logits teacher, target, pruning mask e budget.
- Prerequisito stabile: Capitolo 72, Sicurezza operativa degli agenti.
- Gap: distillazione, pruning e recovery.
- Output consegnato: student più piccolo con loss e regressioni misurate; consumer successivo: Capitolo 74, Quantizzazione.
- Invariante principale: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Visuali: PRUNING-01 e PRUNING-02, con famiglie compositive variabili.
- Snippet: code/snip_73_contract.py; output: code/outputs/SNIP-73-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Teacher e student

- Ultima affermazione stabile: pesi del teacher, student e struttura da comprimere.
- Concetto nuovo: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student.
- Input e shape: logits teacher, target, pruning mask e budget.
- Operazione: distillazione, pruning e recovery.
- Output e shape: student più piccolo con loss e regressioni misurate.
- Che cosa cambia: il passaggio specifico di «Teacher e student».
- Invariante: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due logits trasferiti e una connessione potata con recovery; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Temperature e loss.
- Prova: SRC-73-001 e sezione pubblica corrispondente.

## Transizione 2. Temperature e loss

- Ultima affermazione stabile: pesi del teacher, student e struttura da comprimere.
- Concetto nuovo: Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente.
- Input e shape: logits teacher, target, pruning mask e budget.
- Operazione: distillazione, pruning e recovery.
- Output e shape: student più piccolo con loss e regressioni misurate.
- Che cosa cambia: il passaggio specifico di «Temperature e loss».
- Invariante: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due logits trasferiti e una connessione potata con recovery; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sequence distillation.
- Prova: SRC-73-002 e sezione pubblica corrispondente.

## Transizione 3. Sequence distillation

- Ultima affermazione stabile: pesi del teacher, student e struttura da comprimere.
- Concetto nuovo: Per modelli generativi, risposte del teacher diventano un nuovo dataset. Filtri e diversità determinano ciò che lo student vede.
- Input e shape: logits teacher, target, pruning mask e budget.
- Operazione: distillazione, pruning e recovery.
- Output e shape: student più piccolo con loss e regressioni misurate.
- Che cosa cambia: il passaggio specifico di «Sequence distillation».
- Invariante: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due logits trasferiti e una connessione potata con recovery; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Pruning.
- Prova: SRC-73-003 e sezione pubblica corrispondente.

## Transizione 4. Pruning

- Ultima affermazione stabile: pesi del teacher, student e struttura da comprimere.
- Concetto nuovo: Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware.
- Input e shape: logits teacher, target, pruning mask e budget.
- Operazione: distillazione, pruning e recovery.
- Output e shape: student più piccolo con loss e regressioni misurate.
- Che cosa cambia: il passaggio specifico di «Pruning».
- Invariante: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due logits trasferiti e una connessione potata con recovery; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Recovery.
- Prova: SRC-73-004 e sezione pubblica corrispondente.

## Transizione 5. Recovery

- Ultima affermazione stabile: pesi del teacher, student e struttura da comprimere.
- Concetto nuovo: Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve includere memoria, latency e regressioni per slice.
- Input e shape: logits teacher, target, pruning mask e budget.
- Operazione: distillazione, pruning e recovery.
- Output e shape: student più piccolo con loss e regressioni misurate.
- Che cosa cambia: il passaggio specifico di «Recovery».
- Invariante: compressione e accuratezza vanno misurate sullo stesso perimetro.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due logits trasferiti e una connessione potata con recovery; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Quantizzazione.
- Prova: SRC-73-001 e sezione pubblica corrispondente.
