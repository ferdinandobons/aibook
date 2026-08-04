# Piano interno. Capitolo 39

- Domanda centrale: quale contratto costruisce Varianti dell'attention e gestione KV?
- Oggetto continuo: le teste di query e key-value che alimentano l'attention; input guida: Q con h_q teste e KV con h_kv teste.
- Prerequisito stabile: Capitolo 38, Posizione e contesto lungo.
- Gap: MHA, MQA, GQA, località o sparsità.
- Output consegnato: score, cache e pattern di comunicazione; consumer successivo: Capitolo 40, Attention hardware-aware.
- Invariante principale: raggruppamento delle teste e costo della KV cache restano espliciti.
- Visuali: KV-01 e KV-02, con famiglie compositive variabili.
- Snippet: code/snip_39_contract.py; output: code/outputs/SNIP-39-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. MHA

- Ultima affermazione stabile: le teste di query e key-value che alimentano l'attention.
- Concetto nuovo: Ogni query head possiede key e value dedicate.
- Input e shape: Q con h_q teste e KV con h_kv teste.
- Operazione: MHA, MQA, GQA, località o sparsità.
- Output e shape: score, cache e pattern di comunicazione.
- Che cosa cambia: il passaggio specifico di «MHA».
- Invariante: raggruppamento delle teste e costo della KV cache restano espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro query head condividono due KV head; provare anche una condizione incoerente e osservare il controllo.
- Consumer: MQA.
- Prova: SRC-39-001 e sezione pubblica corrispondente.

## Transizione 2. MQA

- Ultima affermazione stabile: le teste di query e key-value che alimentano l'attention.
- Concetto nuovo: Tutte le query head condividono una singola coppia key-value, riducendo la cache.
- Input e shape: Q con h_q teste e KV con h_kv teste.
- Operazione: MHA, MQA, GQA, località o sparsità.
- Output e shape: score, cache e pattern di comunicazione.
- Che cosa cambia: il passaggio specifico di «MQA».
- Invariante: raggruppamento delle teste e costo della KV cache restano espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro query head condividono due KV head; provare anche una condizione incoerente e osservare il controllo.
- Consumer: GQA.
- Prova: SRC-39-002 e sezione pubblica corrispondente.

## Transizione 3. GQA

- Ultima affermazione stabile: le teste di query e key-value che alimentano l'attention.
- Concetto nuovo: Gruppi di query head condividono un numero intermedio di KV head.
- Input e shape: Q con h_q teste e KV con h_kv teste.
- Operazione: MHA, MQA, GQA, località o sparsità.
- Output e shape: score, cache e pattern di comunicazione.
- Che cosa cambia: il passaggio specifico di «GQA».
- Invariante: raggruppamento delle teste e costo della KV cache restano espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro query head condividono due KV head; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Local e sparse attention.
- Prova: SRC-39-003 e sezione pubblica corrispondente.

## Transizione 4. Local e sparse attention

- Ultima affermazione stabile: le teste di query e key-value che alimentano l'attention.
- Concetto nuovo: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.
- Input e shape: Q con h_q teste e KV con h_kv teste.
- Operazione: MHA, MQA, GQA, località o sparsità.
- Output e shape: score, cache e pattern di comunicazione.
- Che cosa cambia: il passaggio specifico di «Local e sparse attention».
- Invariante: raggruppamento delle teste e costo della KV cache restano espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro query head condividono due KV head; provare anche una condizione incoerente e osservare il controllo.
- Consumer: MLA e cache.
- Prova: SRC-39-004 e sezione pubblica corrispondente.

## Transizione 5. MLA e cache

- Ultima affermazione stabile: le teste di query e key-value che alimentano l'attention.
- Concetto nuovo: Compressione latente e numero di KV head sono strategie differenti. La memoria dipende anche da layer, dtype, batch e lunghezza.
- Input e shape: Q con h_q teste e KV con h_kv teste.
- Operazione: MHA, MQA, GQA, località o sparsità.
- Output e shape: score, cache e pattern di comunicazione.
- Che cosa cambia: il passaggio specifico di «MLA e cache».
- Invariante: raggruppamento delle teste e costo della KV cache restano espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro query head condividono due KV head; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Attention hardware-aware.
- Prova: SRC-39-001 e sezione pubblica corrispondente.
