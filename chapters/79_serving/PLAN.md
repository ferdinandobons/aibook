# Piano interno. Capitolo 79

- Domanda centrale: quale contratto costruisce Serving, batching e scheduling?
- Oggetto continuo: richieste eterogenee in una coda di serving; input guida: prompt, deadline, lunghezza, memoria e priorità.
- Prerequisito stabile: Capitolo 78, KV cache e riuso del contesto.
- Gap: batching continuo, admission e scheduling.
- Output consegnato: throughput, latency p50/p99 e richieste ammesse; consumer successivo: Capitolo 80, Serving disaggregato e inference distribuita.
- Invariante principale: throughput e latenza devono essere misurati insieme.
- Visuali: SERVING-01 e SERVING-02, con famiglie compositive variabili.
- Snippet: code/snip_79_contract.py; output: code/outputs/SNIP-79-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Richieste eterogenee

- Ultima affermazione stabile: richieste eterogenee in una coda di serving.
- Concetto nuovo: Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano.
- Input e shape: prompt, deadline, lunghezza, memoria e priorità.
- Operazione: batching continuo, admission e scheduling.
- Output e shape: throughput, latency p50/p99 e richieste ammesse.
- Che cosa cambia: il passaggio specifico di «Richieste eterogenee».
- Invariante: throughput e latenza devono essere misurati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una richiesta lunga e due brevi in un batch continuo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Continuous batching.
- Prova: SRC-79-001 e sezione pubblica corrispondente.

## Transizione 2. Continuous batching

- Ultima affermazione stabile: richieste eterogenee in una coda di serving.
- Concetto nuovo: Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse.
- Input e shape: prompt, deadline, lunghezza, memoria e priorità.
- Operazione: batching continuo, admission e scheduling.
- Output e shape: throughput, latency p50/p99 e richieste ammesse.
- Che cosa cambia: il passaggio specifico di «Continuous batching».
- Invariante: throughput e latenza devono essere misurati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una richiesta lunga e due brevi in un batch continuo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Throughput e latency.
- Prova: SRC-79-002 e sezione pubblica corrispondente.

## Transizione 3. Throughput e latency

- Ultima affermazione stabile: richieste eterogenee in una coda di serving.
- Concetto nuovo: Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency.
- Input e shape: prompt, deadline, lunghezza, memoria e priorità.
- Operazione: batching continuo, admission e scheduling.
- Output e shape: throughput, latency p50/p99 e richieste ammesse.
- Che cosa cambia: il passaggio specifico di «Throughput e latency».
- Invariante: throughput e latenza devono essere misurati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una richiesta lunga e due brevi in un batch continuo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Admission control.
- Prova: SRC-79-003 e sezione pubblica corrispondente.

## Transizione 4. Admission control

- Ultima affermazione stabile: richieste eterogenee in una coda di serving.
- Concetto nuovo: Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema.
- Input e shape: prompt, deadline, lunghezza, memoria e priorità.
- Operazione: batching continuo, admission e scheduling.
- Output e shape: throughput, latency p50/p99 e richieste ammesse.
- Che cosa cambia: il passaggio specifico di «Admission control».
- Invariante: throughput e latenza devono essere misurati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una richiesta lunga e due brevi in un batch continuo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metriche di servizio.
- Prova: SRC-79-004 e sezione pubblica corrispondente.

## Transizione 5. Metriche di servizio

- Ultima affermazione stabile: richieste eterogenee in una coda di serving.
- Concetto nuovo: TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta.
- Input e shape: prompt, deadline, lunghezza, memoria e priorità.
- Operazione: batching continuo, admission e scheduling.
- Output e shape: throughput, latency p50/p99 e richieste ammesse.
- Che cosa cambia: il passaggio specifico di «Metriche di servizio».
- Invariante: throughput e latenza devono essere misurati insieme.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una richiesta lunga e due brevi in un batch continuo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Serving disaggregato e inference distribuita.
- Prova: SRC-79-001 e sezione pubblica corrispondente.
