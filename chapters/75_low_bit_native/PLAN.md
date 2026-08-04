# Piano editoriale. Capitolo 75

## Obiettivo didattico

Seguire **Modelli low-bit nativi e co-design numerico** da peso reale, codice ternario, scala e attivazione a peso ricostruito, gradiente e costo hardware, osservando training nativo, STE e accumulazione senza oltrepassare questo limite: bit nominali e precisione effettiva dell'accumulo sono distinti.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 74: Quantizzazione

## Percorso della lezione

1. **Training nativo.** Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine. Prova: SRC-75-001.
2. **Pesi ternari e 1.58-bit.** BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel. Prova: SRC-75-002.
3. **Straight-through estimator.** Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione. Prova: SRC-75-003.
4. **Accumulazione.** Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati. Prova: SRC-75-004.
5. **Co-design hardware.** Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo. Prova: SRC-75-001.

## Prove e artefatti

- riferimento minimo: `code/snip_75_contract.py`; test: `code/test_75_contract.py`; output: `code/outputs/SNIP-75-001.txt`.
- visuali candidate: NATIVE-01, NATIVE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
