# Piano interno. Capitolo 54

- Domanda centrale: quale contratto costruisce Aggiornamento, merging ed editing del modello?
- Oggetto continuo: versioni di pesi e modifiche localizzate del modello; input guida: base model, delta, task e rollback point.
- Prerequisito stabile: Capitolo 53, Test-time compute, ricerca e controllo del budget.
- Gap: continued adaptation, merge, editing e regressione.
- Output consegnato: versione nuova, diff e test di regressione; consumer successivo: Capitolo 55, Fondamenti della multimodalità.
- Invariante principale: un merge senza valutazione può introdurre regressioni invisibili.
- Visuali: UPDATE-01 e UPDATE-02, con famiglie compositive variabili.
- Snippet: code/snip_54_contract.py; output: code/outputs/SNIP-54-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Continued adaptation

- Ultima affermazione stabile: versioni di pesi e modifiche localizzate del modello.
- Concetto nuovo: Nuovi dati e obiettivi aggiornano il checkpoint. Replay, regolarizzazione e valutazioni controllano forgetting e regressioni.
- Input e shape: base model, delta, task e rollback point.
- Operazione: continued adaptation, merge, editing e regressione.
- Output e shape: versione nuova, diff e test di regressione.
- Che cosa cambia: il passaggio specifico di «Continued adaptation».
- Invariante: un merge senza valutazione può introdurre regressioni invisibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due delta combinati e una capability testata prima e dopo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Task arithmetic.
- Prova: SRC-54-001 e sezione pubblica corrispondente.

## Transizione 2. Task arithmetic

- Ultima affermazione stabile: versioni di pesi e modifiche localizzate del modello.
- Concetto nuovo: Differenze tra checkpoint possono essere combinate come vettori. La compatibilità richiede stessa base e corrispondenza dei parametri.
- Input e shape: base model, delta, task e rollback point.
- Operazione: continued adaptation, merge, editing e regressione.
- Output e shape: versione nuova, diff e test di regressione.
- Che cosa cambia: il passaggio specifico di «Task arithmetic».
- Invariante: un merge senza valutazione può introdurre regressioni invisibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due delta combinati e una capability testata prima e dopo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: TIES e DARE.
- Prova: SRC-54-004 e sezione pubblica corrispondente.

## Transizione 3. TIES e DARE

- Ultima affermazione stabile: versioni di pesi e modifiche localizzate del modello.
- Concetto nuovo: Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. I risultati dipendono dai task e dalla scala dei delta.
- Input e shape: base model, delta, task e rollback point.
- Operazione: continued adaptation, merge, editing e regressione.
- Output e shape: versione nuova, diff e test di regressione.
- Che cosa cambia: il passaggio specifico di «TIES e DARE».
- Invariante: un merge senza valutazione può introdurre regressioni invisibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due delta combinati e una capability testata prima e dopo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Model editing.
- Prova: SRC-54-003 e sezione pubblica corrispondente.

## Transizione 4. Model editing

- Ultima affermazione stabile: versioni di pesi e modifiche localizzate del modello.
- Concetto nuovo: ROME, MEMIT e famiglie affini cercano modifiche localizzate. Località, generalizzazione e side effect devono essere misurati separatamente.
- Input e shape: base model, delta, task e rollback point.
- Operazione: continued adaptation, merge, editing e regressione.
- Output e shape: versione nuova, diff e test di regressione.
- Che cosa cambia: il passaggio specifico di «Model editing».
- Invariante: un merge senza valutazione può introdurre regressioni invisibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due delta combinati e una capability testata prima e dopo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Versioning e rollback.
- Prova: SRC-54-002 e sezione pubblica corrispondente.

## Transizione 5. Versioning e rollback

- Ultima affermazione stabile: versioni di pesi e modifiche localizzate del modello.
- Concetto nuovo: Un update produce un nuovo artefatto con fonti, test e dipendenze. Merging ed editing non sostituiscono la gestione delle versioni.
- Input e shape: base model, delta, task e rollback point.
- Operazione: continued adaptation, merge, editing e regressione.
- Output e shape: versione nuova, diff e test di regressione.
- Che cosa cambia: il passaggio specifico di «Versioning e rollback».
- Invariante: un merge senza valutazione può introdurre regressioni invisibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due delta combinati e una capability testata prima e dopo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fondamenti della multimodalità.
- Prova: SRC-54-001 e sezione pubblica corrispondente.
