# Piano interno. Capitolo 82

- Domanda centrale: quale contratto costruisce LLMOps, edge, costo ed energia?
- Oggetto continuo: un servizio LLM dalla versione al consumo; input guida: modello, richieste, device, energia e monitor.
- Prerequisito stabile: Capitolo 81, Compiler, kernel e runtime.
- Gap: deploy, osservabilità, edge routing e cost accounting.
- Output consegnato: versione attiva, costo per richiesta e alert; consumer successivo: Capitolo 83, Progettare una valutazione.
- Invariante principale: un costo locale non descrive l'intero ciclo di vita.
- Visuali: LLMOPS-01 e LLMOPS-02, con famiglie compositive variabili.
- Snippet: code/snip_82_contract.py; output: code/outputs/SNIP-82-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Dalla versione al deployment

- Ultima affermazione stabile: un servizio LLM dalla versione al consumo.
- Concetto nuovo: Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema.
- Input e shape: modello, richieste, device, energia e monitor.
- Operazione: deploy, osservabilità, edge routing e cost accounting.
- Output e shape: versione attiva, costo per richiesta e alert.
- Che cosa cambia: il passaggio specifico di «Dalla versione al deployment».
- Invariante: un costo locale non descrive l'intero ciclo di vita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: costo per richiesta con energia e quota hardware separate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Osservabilità.
- Prova: SRC-82-001 e sezione pubblica corrispondente.

## Transizione 2. Osservabilità

- Ultima affermazione stabile: un servizio LLM dalla versione al consumo.
- Concetto nuovo: Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario.
- Input e shape: modello, richieste, device, energia e monitor.
- Operazione: deploy, osservabilità, edge routing e cost accounting.
- Output e shape: versione attiva, costo per richiesta e alert.
- Che cosa cambia: il passaggio specifico di «Osservabilità».
- Invariante: un costo locale non descrive l'intero ciclo di vita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: costo per richiesta con energia e quota hardware separate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Edge.
- Prova: SRC-82-002 e sezione pubblica corrispondente.

## Transizione 3. Edge

- Ultima affermazione stabile: un servizio LLM dalla versione al consumo.
- Concetto nuovo: Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Offline e privacy possono motivare il deployment locale.
- Input e shape: modello, richieste, device, energia e monitor.
- Operazione: deploy, osservabilità, edge routing e cost accounting.
- Output e shape: versione attiva, costo per richiesta e alert.
- Che cosa cambia: il passaggio specifico di «Edge».
- Invariante: un costo locale non descrive l'intero ciclo di vita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: costo per richiesta con energia e quota hardware separate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Costo.
- Prova: SRC-82-003 e sezione pubblica corrispondente.

## Transizione 4. Costo

- Ultima affermazione stabile: un servizio LLM dalla versione al consumo.
- Concetto nuovo: Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e batching modificano l'allocazione.
- Input e shape: modello, richieste, device, energia e monitor.
- Operazione: deploy, osservabilità, edge routing e cost accounting.
- Output e shape: versione attiva, costo per richiesta e alert.
- Che cosa cambia: il passaggio specifico di «Costo».
- Invariante: un costo locale non descrive l'intero ciclo di vita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: costo per richiesta con energia e quota hardware separate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Energia e sostenibilità.
- Prova: SRC-82-004 e sezione pubblica corrispondente.

## Transizione 5. Energia e sostenibilità

- Ultima affermazione stabile: un servizio LLM dalla versione al consumo.
- Concetto nuovo: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono dichiarare confini e metodologia.
- Input e shape: modello, richieste, device, energia e monitor.
- Operazione: deploy, osservabilità, edge routing e cost accounting.
- Output e shape: versione attiva, costo per richiesta e alert.
- Che cosa cambia: il passaggio specifico di «Energia e sostenibilità».
- Invariante: un costo locale non descrive l'intero ciclo di vita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: costo per richiesta con energia e quota hardware separate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Progettare una valutazione.
- Prova: SRC-82-001 e sezione pubblica corrispondente.
