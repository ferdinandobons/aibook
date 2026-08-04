# Piano interno. Capitolo 30

- Domanda centrale: quale contratto costruisce Famiglie architetturali e obiettivi di pretraining?
- Oggetto continuo: una famiglia architetturale legata al proprio obiettivo; input guida: sequenza, mask e target di pretraining.
- Prerequisito stabile: Capitolo 29, Il Transformer da zero.
- Gap: encoder, decoder, span corruption o causal prediction.
- Output consegnato: rappresentazione o distribuzione predittiva; consumer successivo: Capitolo 31, Dalla rappresentazione linguistica agli LLM.
- Invariante principale: architettura e objective non possono essere scambiati senza cambiare il compito.
- Visuali: FAMILIES-01 e FAMILIES-02, con famiglie compositive variabili.
- Snippet: code/snip_30_contract.py; output: code/outputs/SNIP-30-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Encoder-only

- Ultima affermazione stabile: una famiglia architetturale legata al proprio obiettivo.
- Concetto nuovo: Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione.
- Input e shape: sequenza, mask e target di pretraining.
- Operazione: encoder, decoder, span corruption o causal prediction.
- Output e shape: rappresentazione o distribuzione predittiva.
- Che cosa cambia: il passaggio specifico di «Encoder-only».
- Invariante: architettura e objective non possono essere scambiati senza cambiare il compito.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso testo con target masked e causal separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Decoder-only.
- Prova: SRC-30-001 e sezione pubblica corrispondente.

## Transizione 2. Decoder-only

- Ultima affermazione stabile: una famiglia architetturale legata al proprio obiettivo.
- Concetto nuovo: Un decoder causale predice token successivi e supporta generazione incrementale.
- Input e shape: sequenza, mask e target di pretraining.
- Operazione: encoder, decoder, span corruption o causal prediction.
- Output e shape: rappresentazione o distribuzione predittiva.
- Che cosa cambia: il passaggio specifico di «Decoder-only».
- Invariante: architettura e objective non possono essere scambiati senza cambiare il compito.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso testo con target masked e causal separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Encoder-decoder.
- Prova: SRC-30-002 e sezione pubblica corrispondente.

## Transizione 3. Encoder-decoder

- Ultima affermazione stabile: una famiglia architetturale legata al proprio obiettivo.
- Concetto nuovo: T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention.
- Input e shape: sequenza, mask e target di pretraining.
- Operazione: encoder, decoder, span corruption o causal prediction.
- Output e shape: rappresentazione o distribuzione predittiva.
- Che cosa cambia: il passaggio specifico di «Encoder-decoder».
- Invariante: architettura e objective non possono essere scambiati senza cambiare il compito.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso testo con target masked e causal separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Masked, causal e span corruption.
- Prova: SRC-30-003 e sezione pubblica corrispondente.

## Transizione 4. Masked, causal e span corruption

- Ultima affermazione stabile: una famiglia architetturale legata al proprio obiettivo.
- Concetto nuovo: Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss.
- Input e shape: sequenza, mask e target di pretraining.
- Operazione: encoder, decoder, span corruption o causal prediction.
- Output e shape: rappresentazione o distribuzione predittiva.
- Che cosa cambia: il passaggio specifico di «Masked, causal e span corruption».
- Invariante: architettura e objective non possono essere scambiati senza cambiare il compito.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso testo con target masked e causal separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Architettura e obiettivo.
- Prova: SRC-30-004 e sezione pubblica corrispondente.

## Transizione 5. Architettura e obiettivo

- Ultima affermazione stabile: una famiglia architetturale legata al proprio obiettivo.
- Concetto nuovo: La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti.
- Input e shape: sequenza, mask e target di pretraining.
- Operazione: encoder, decoder, span corruption o causal prediction.
- Output e shape: rappresentazione o distribuzione predittiva.
- Che cosa cambia: il passaggio specifico di «Architettura e obiettivo».
- Invariante: architettura e objective non possono essere scambiati senza cambiare il compito.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso testo con target masked e causal separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dalla rappresentazione linguistica agli LLM.
- Prova: SRC-30-001 e sezione pubblica corrispondente.
