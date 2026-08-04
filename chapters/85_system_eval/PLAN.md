# Piano interno. Capitolo 85

- Domanda centrale: quale contratto costruisce Valutare contesto lungo, RAG, multimodalità e agenti?
- Oggetto continuo: un sistema composto da modello, contesto, tool e interfaccia; input guida: task, componenti, trace e policy.
- Prerequisito stabile: Capitolo 84, Fattualità, incertezza e affidabilità.
- Gap: eval end-to-end, stress, slice e monitoraggio.
- Output consegnato: score di sistema, failure e regressione; consumer successivo: Capitolo 86, Interpretabilità delle rappresentazioni e dei circuiti.
- Invariante principale: misurare il modello isolato non misura il comportamento del sistema.
- Visuali: EVAL-01 e EVAL-02, con famiglie compositive variabili.
- Snippet: code/snip_85_contract.py; output: code/outputs/SNIP-85-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Contesto lungo

- Ultima affermazione stabile: un sistema composto da modello, contesto, tool e interfaccia.
- Concetto nuovo: Variare lunghezza, posizione dell'evidenza e distrattori misura utilizzo, non soltanto capacità nominale.
- Input e shape: task, componenti, trace e policy.
- Operazione: eval end-to-end, stress, slice e monitoraggio.
- Output e shape: score di sistema, failure e regressione.
- Che cosa cambia: il passaggio specifico di «Contesto lungo».
- Invariante: misurare il modello isolato non misura il comportamento del sistema.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un RAG che risponde bene ma cita una fonte irrilevante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RAG.
- Prova: SRC-85-001 e sezione pubblica corrispondente.

## Transizione 2. RAG

- Ultima affermazione stabile: un sistema composto da modello, contesto, tool e interfaccia.
- Concetto nuovo: Retrieval recall, context precision, attribution e risposta finale compongono una pipeline con errori localizzabili.
- Input e shape: task, componenti, trace e policy.
- Operazione: eval end-to-end, stress, slice e monitoraggio.
- Output e shape: score di sistema, failure e regressione.
- Che cosa cambia: il passaggio specifico di «RAG».
- Invariante: misurare il modello isolato non misura il comportamento del sistema.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un RAG che risponde bene ma cita una fonte irrilevante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Multimodalità.
- Prova: SRC-85-002 e sezione pubblica corrispondente.

## Transizione 3. Multimodalità

- Ultima affermazione stabile: un sistema composto da modello, contesto, tool e interfaccia.
- Concetto nuovo: Modalità, risoluzione, sincronizzazione e grounding richiedono slice e metriche specifiche.
- Input e shape: task, componenti, trace e policy.
- Operazione: eval end-to-end, stress, slice e monitoraggio.
- Output e shape: score di sistema, failure e regressione.
- Che cosa cambia: il passaggio specifico di «Multimodalità».
- Invariante: misurare il modello isolato non misura il comportamento del sistema.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un RAG che risponde bene ma cita una fonte irrilevante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Agenti.
- Prova: SRC-85-003 e sezione pubblica corrispondente.

## Transizione 4. Agenti

- Ultima affermazione stabile: un sistema composto da modello, contesto, tool e interfaccia.
- Concetto nuovo: Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e resettabili.
- Input e shape: task, componenti, trace e policy.
- Operazione: eval end-to-end, stress, slice e monitoraggio.
- Output e shape: score di sistema, failure e regressione.
- Che cosa cambia: il passaggio specifico di «Agenti».
- Invariante: misurare il modello isolato non misura il comportamento del sistema.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un RAG che risponde bene ma cita una fonte irrilevante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Evaluation in production.
- Prova: SRC-85-004 e sezione pubblica corrispondente.

## Transizione 5. Evaluation in production

- Ultima affermazione stabile: un sistema composto da modello, contesto, tool e interfaccia.
- Concetto nuovo: Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali senza confonderli.
- Input e shape: task, componenti, trace e policy.
- Operazione: eval end-to-end, stress, slice e monitoraggio.
- Output e shape: score di sistema, failure e regressione.
- Che cosa cambia: il passaggio specifico di «Evaluation in production».
- Invariante: misurare il modello isolato non misura il comportamento del sistema.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un RAG che risponde bene ma cita una fonte irrilevante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Interpretabilità delle rappresentazioni e dei circuiti.
- Prova: SRC-85-001 e sezione pubblica corrispondente.
