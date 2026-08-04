# Piano interno. Capitolo 31

- Domanda centrale: quale contratto costruisce Dalla rappresentazione linguistica agli LLM?
- Oggetto continuo: un prompt e la distribuzione del token successivo; input guida: prefisso tokenizzato, esempi e temperatura dichiarati.
- Prerequisito stabile: Capitolo 30, Famiglie architetturali e obiettivi di pretraining.
- Gap: in-context learning, decoding e calibrazione.
- Output consegnato: logits, risposta e confidenza misurabile; consumer successivo: Capitolo 32, Il ciclo di vita dei dati.
- Invariante principale: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Visuali: LLM-01 e LLM-02, con famiglie compositive variabili.
- Snippet: code/snip_31_contract.py; output: code/outputs/SNIP-31-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Distribuzione del token successivo

- Ultima affermazione stabile: un prompt e la distribuzione del token successivo.
- Concetto nuovo: Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce una distribuzione, non una risposta già scelta.
- Input e shape: prefisso tokenizzato, esempi e temperatura dichiarati.
- Operazione: in-context learning, decoding e calibrazione.
- Output e shape: logits, risposta e confidenza misurabile.
- Che cosa cambia: il passaggio specifico di «Distribuzione del token successivo».
- Invariante: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso prompt con greedy e top-p confrontati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prompt e dimostrazioni.
- Prova: SRC-31-001 e sezione pubblica corrispondente.

## Transizione 2. Prompt e dimostrazioni

- Ultima affermazione stabile: un prompt e la distribuzione del token successivo.
- Concetto nuovo: Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta invariato durante in-context learning.
- Input e shape: prefisso tokenizzato, esempi e temperatura dichiarati.
- Operazione: in-context learning, decoding e calibrazione.
- Output e shape: logits, risposta e confidenza misurabile.
- Che cosa cambia: il passaggio specifico di «Prompt e dimostrazioni».
- Invariante: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso prompt con greedy e top-p confrontati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Decoding.
- Prova: SRC-31-002 e sezione pubblica corrispondente.

## Transizione 3. Decoding

- Ultima affermazione stabile: un prompt e la distribuzione del token successivo.
- Concetto nuovo: Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria.
- Input e shape: prefisso tokenizzato, esempi e temperatura dichiarati.
- Operazione: in-context learning, decoding e calibrazione.
- Output e shape: logits, risposta e confidenza misurabile.
- Che cosa cambia: il passaggio specifico di «Decoding».
- Invariante: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso prompt con greedy e top-p confrontati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Calibrazione.
- Prova: SRC-31-003 e sezione pubblica corrispondente.

## Transizione 4. Calibrazione

- Ultima affermazione stabile: un prompt e la distribuzione del token successivo.
- Concetto nuovo: Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti.
- Input e shape: prefisso tokenizzato, esempi e temperatura dichiarati.
- Operazione: in-context learning, decoding e calibrazione.
- Output e shape: logits, risposta e confidenza misurabile.
- Che cosa cambia: il passaggio specifico di «Calibrazione».
- Invariante: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso prompt con greedy e top-p confrontati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modello e sistema.
- Prova: SRC-31-004 e sezione pubblica corrispondente.

## Transizione 5. Modello e sistema

- Ultima affermazione stabile: un prompt e la distribuzione del token successivo.
- Concetto nuovo: Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato.
- Input e shape: prefisso tokenizzato, esempi e temperatura dichiarati.
- Operazione: in-context learning, decoding e calibrazione.
- Output e shape: logits, risposta e confidenza misurabile.
- Che cosa cambia: il passaggio specifico di «Modello e sistema».
- Invariante: probabilità, comportamento osservato e correttezza non sono sinonimi.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso prompt con greedy e top-p confrontati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Il ciclo di vita dei dati.
- Prova: SRC-31-001 e sezione pubblica corrispondente.
