# Piano interno. Capitolo 74

- Domanda centrale: quale contratto costruisce Quantizzazione?
- Oggetto continuo: un tensore reale e la sua rappresentazione quantizzata; input guida: valori, scale, zero-point, dtype e calibrazione.
- Prerequisito stabile: Capitolo 73, Distillazione e pruning.
- Gap: PTQ, QAT, weight-only o activation quantization.
- Output consegnato: codici, tensore ricostruito, errore e memoria; consumer successivo: Capitolo 75, Modelli low-bit nativi e co-design numerico.
- Invariante principale: scala e dominio di calibrazione fanno parte del risultato.
- Visuali: QUANTIZATI-01 e QUANTIZATI-02, con famiglie compositive variabili.
- Snippet: code/snip_74_contract.py; output: code/outputs/SNIP-74-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Scala e zero point

- Ultima affermazione stabile: un tensore reale e la sua rappresentazione quantizzata.
- Concetto nuovo: Una mappa affine converte valori floating point in interi. Granularità per tensor, channel o group cambia errore e metadata.
- Input e shape: valori, scale, zero-point, dtype e calibrazione.
- Operazione: PTQ, QAT, weight-only o activation quantization.
- Output e shape: codici, tensore ricostruito, errore e memoria.
- Che cosa cambia: il passaggio specifico di «Scala e zero point».
- Invariante: scala e dominio di calibrazione fanno parte del risultato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre valori quantizzati con scala 0,25 e errore massimo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: PTQ.
- Prova: SRC-74-001 e sezione pubblica corrispondente.

## Transizione 2. PTQ

- Ultima affermazione stabile: un tensore reale e la sua rappresentazione quantizzata.
- Concetto nuovo: Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale.
- Input e shape: valori, scale, zero-point, dtype e calibrazione.
- Operazione: PTQ, QAT, weight-only o activation quantization.
- Output e shape: codici, tensore ricostruito, errore e memoria.
- Che cosa cambia: il passaggio specifico di «PTQ».
- Invariante: scala e dominio di calibrazione fanno parte del risultato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre valori quantizzati con scala 0,25 e errore massimo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: QAT.
- Prova: SRC-74-002 e sezione pubblica corrispondente.

## Transizione 3. QAT

- Ultima affermazione stabile: un tensore reale e la sua rappresentazione quantizzata.
- Concetto nuovo: Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi.
- Input e shape: valori, scale, zero-point, dtype e calibrazione.
- Operazione: PTQ, QAT, weight-only o activation quantization.
- Output e shape: codici, tensore ricostruito, errore e memoria.
- Che cosa cambia: il passaggio specifico di «QAT».
- Invariante: scala e dominio di calibrazione fanno parte del risultato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre valori quantizzati con scala 0,25 e errore massimo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Weight-only e activation quantization.
- Prova: SRC-74-003 e sezione pubblica corrispondente.

## Transizione 4. Weight-only e activation quantization

- Ultima affermazione stabile: un tensore reale e la sua rappresentazione quantizzata.
- Concetto nuovo: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo.
- Input e shape: valori, scale, zero-point, dtype e calibrazione.
- Operazione: PTQ, QAT, weight-only o activation quantization.
- Output e shape: codici, tensore ricostruito, errore e memoria.
- Che cosa cambia: il passaggio specifico di «Weight-only e activation quantization».
- Invariante: scala e dominio di calibrazione fanno parte del risultato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre valori quantizzati con scala 0,25 e errore massimo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metodi per LLM.
- Prova: SRC-74-004 e sezione pubblica corrispondente.

## Transizione 5. Metodi per LLM

- Ultima affermazione stabile: un tensore reale e la sua rappresentazione quantizzata.
- Concetto nuovo: GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti.
- Input e shape: valori, scale, zero-point, dtype e calibrazione.
- Operazione: PTQ, QAT, weight-only o activation quantization.
- Output e shape: codici, tensore ricostruito, errore e memoria.
- Che cosa cambia: il passaggio specifico di «Metodi per LLM».
- Invariante: scala e dominio di calibrazione fanno parte del risultato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre valori quantizzati con scala 0,25 e errore massimo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modelli low-bit nativi e co-design numerico.
- Prova: SRC-74-001 e sezione pubblica corrispondente.
