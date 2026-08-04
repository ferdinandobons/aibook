# Piano interno. Capitolo 91

- Domanda centrale: quale contratto costruisce Privacy, fairness e unlearning?
- Oggetto continuo: un dato personale e il comportamento del sistema su gruppi diversi; input guida: record, membership, gruppo, label e budget privacy.
- Prerequisito stabile: Capitolo 90, Poisoning, backdoor, extraction e supply chain.
- Gap: DP, fairness evaluation e unlearning.
- Output consegnato: utility, leakage, disparità e verifica di rimozione; consumer successivo: Capitolo 92, Watermarking e provenienza dei contenuti.
- Invariante principale: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Visuali: FAIRNESS-01 e FAIRNESS-02, con famiglie compositive variabili.
- Snippet: code/snip_91_contract.py; output: code/outputs/SNIP-91-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Memorizzazione e leakage

- Ultima affermazione stabile: un dato personale e il comportamento del sistema su gruppi diversi.
- Concetto nuovo: Un modello può riprodurre sequenze rare. Membership inference e extraction misurano rischi differenti.
- Input e shape: record, membership, gruppo, label e budget privacy.
- Operazione: DP, fairness evaluation e unlearning.
- Output e shape: utility, leakage, disparità e verifica di rimozione.
- Che cosa cambia: il passaggio specifico di «Memorizzazione e leakage».
- Invariante: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stessa accuracy media con leakage e disparità per slice; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Differential privacy.
- Prova: SRC-91-001 e sezione pubblica corrispondente.

## Transizione 2. Differential privacy

- Ultima affermazione stabile: un dato personale e il comportamento del sistema su gruppi diversi.
- Concetto nuovo: DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità.
- Input e shape: record, membership, gruppo, label e budget privacy.
- Operazione: DP, fairness evaluation e unlearning.
- Output e shape: utility, leakage, disparità e verifica di rimozione.
- Che cosa cambia: il passaggio specifico di «Differential privacy».
- Invariante: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stessa accuracy media con leakage e disparità per slice; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fairness.
- Prova: SRC-91-002 e sezione pubblica corrispondente.

## Transizione 3. Fairness

- Ultima affermazione stabile: un dato personale e il comportamento del sistema su gruppi diversi.
- Concetto nuovo: Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. Il contesto decisionale guida la scelta.
- Input e shape: record, membership, gruppo, label e budget privacy.
- Operazione: DP, fairness evaluation e unlearning.
- Output e shape: utility, leakage, disparità e verifica di rimozione.
- Che cosa cambia: il passaggio specifico di «Fairness».
- Invariante: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stessa accuracy media con leakage e disparità per slice; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Bias nei dati e nel sistema.
- Prova: SRC-91-003 e sezione pubblica corrispondente.

## Transizione 4. Bias nei dati e nel sistema

- Ultima affermazione stabile: un dato personale e il comportamento del sistema su gruppi diversi.
- Concetto nuovo: Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello.
- Input e shape: record, membership, gruppo, label e budget privacy.
- Operazione: DP, fairness evaluation e unlearning.
- Output e shape: utility, leakage, disparità e verifica di rimozione.
- Che cosa cambia: il passaggio specifico di «Bias nei dati e nel sistema».
- Invariante: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stessa accuracy media con leakage e disparità per slice; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Machine unlearning.
- Prova: SRC-91-004 e sezione pubblica corrispondente.

## Transizione 5. Machine unlearning

- Ultima affermazione stabile: un dato personale e il comportamento del sistema su gruppi diversi.
- Concetto nuovo: Rimuovere l'influenza di dati richiede un criterio e una verifica. Cancellare un record dal corpus non modifica automaticamente il checkpoint.
- Input e shape: record, membership, gruppo, label e budget privacy.
- Operazione: DP, fairness evaluation e unlearning.
- Output e shape: utility, leakage, disparità e verifica di rimozione.
- Che cosa cambia: il passaggio specifico di «Machine unlearning».
- Invariante: privacy, fairness e utility richiedono metriche e trade-off espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stessa accuracy media con leakage e disparità per slice; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Watermarking e provenienza dei contenuti.
- Prova: SRC-91-001 e sezione pubblica corrispondente.
