# Piano interno. Capitolo 75

- Domanda centrale: quale contratto costruisce Modelli low-bit nativi e co-design numerico?
- Oggetto continuo: un peso low-bit e il suo accumulo numerico; input guida: peso reale, codice ternario, scala e attivazione.
- Prerequisito stabile: Capitolo 74, Quantizzazione.
- Gap: training nativo, STE e accumulazione.
- Output consegnato: peso ricostruito, gradiente e costo hardware; consumer successivo: Capitolo 76, Decoding e generazione vincolata.
- Invariante principale: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Visuali: NATIVE-01 e NATIVE-02, con famiglie compositive variabili.
- Snippet: code/snip_75_contract.py; output: code/outputs/SNIP-75-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Training nativo

- Ultima affermazione stabile: un peso low-bit e il suo accumulo numerico.
- Concetto nuovo: Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine.
- Input e shape: peso reale, codice ternario, scala e attivazione.
- Operazione: training nativo, STE e accumulazione.
- Output e shape: peso ricostruito, gradiente e costo hardware.
- Che cosa cambia: il passaggio specifico di «Training nativo».
- Invariante: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: peso {-1, 0, 1} con scala e accumulo in precisione maggiore; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Pesi ternari e 1.58-bit.
- Prova: SRC-75-001 e sezione pubblica corrispondente.

## Transizione 2. Pesi ternari e 1.58-bit

- Ultima affermazione stabile: un peso low-bit e il suo accumulo numerico.
- Concetto nuovo: BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel.
- Input e shape: peso reale, codice ternario, scala e attivazione.
- Operazione: training nativo, STE e accumulazione.
- Output e shape: peso ricostruito, gradiente e costo hardware.
- Che cosa cambia: il passaggio specifico di «Pesi ternari e 1.58-bit».
- Invariante: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: peso {-1, 0, 1} con scala e accumulo in precisione maggiore; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Straight-through estimator.
- Prova: SRC-75-002 e sezione pubblica corrispondente.

## Transizione 3. Straight-through estimator

- Ultima affermazione stabile: un peso low-bit e il suo accumulo numerico.
- Concetto nuovo: Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione.
- Input e shape: peso reale, codice ternario, scala e attivazione.
- Operazione: training nativo, STE e accumulazione.
- Output e shape: peso ricostruito, gradiente e costo hardware.
- Che cosa cambia: il passaggio specifico di «Straight-through estimator».
- Invariante: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: peso {-1, 0, 1} con scala e accumulo in precisione maggiore; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Accumulazione.
- Prova: SRC-75-003 e sezione pubblica corrispondente.

## Transizione 4. Accumulazione

- Ultima affermazione stabile: un peso low-bit e il suo accumulo numerico.
- Concetto nuovo: Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati.
- Input e shape: peso reale, codice ternario, scala e attivazione.
- Operazione: training nativo, STE e accumulazione.
- Output e shape: peso ricostruito, gradiente e costo hardware.
- Che cosa cambia: il passaggio specifico di «Accumulazione».
- Invariante: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: peso {-1, 0, 1} con scala e accumulo in precisione maggiore; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Co-design hardware.
- Prova: SRC-75-004 e sezione pubblica corrispondente.

## Transizione 5. Co-design hardware

- Ultima affermazione stabile: un peso low-bit e il suo accumulo numerico.
- Concetto nuovo: Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo.
- Input e shape: peso reale, codice ternario, scala e attivazione.
- Operazione: training nativo, STE e accumulazione.
- Output e shape: peso ricostruito, gradiente e costo hardware.
- Che cosa cambia: il passaggio specifico di «Co-design hardware».
- Invariante: bit nominali e precisione effettiva dell'accumulo sono distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: peso {-1, 0, 1} con scala e accumulo in precisione maggiore; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Decoding e generazione vincolata.
- Prova: SRC-75-001 e sezione pubblica corrispondente.
