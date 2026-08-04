# Piano interno. Capitolo 84

- Domanda centrale: quale contratto costruisce Fattualità, incertezza e affidabilità?
- Oggetto continuo: una risposta con evidenza, confidenza e possibilità di errore; input guida: claim, predizione, fonti e score di confidenza.
- Prerequisito stabile: Capitolo 83, Progettare una valutazione.
- Gap: verifica, calibrazione, astensione e retrieval.
- Output consegnato: risposta supportata o astensione motivata; consumer successivo: Capitolo 85, Valutare contesto lungo, RAG, multimodalità e agenti.
- Invariante principale: confidenza alta non certifica la verità fattuale.
- Visuali: FACTUALITY-01 e FACTUALITY-02, con famiglie compositive variabili.
- Snippet: code/snip_84_contract.py; output: code/outputs/SNIP-84-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Correttezza e supporto

- Ultima affermazione stabile: una risposta con evidenza, confidenza e possibilità di errore.
- Concetto nuovo: Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata.
- Input e shape: claim, predizione, fonti e score di confidenza.
- Operazione: verifica, calibrazione, astensione e retrieval.
- Output e shape: risposta supportata o astensione motivata.
- Che cosa cambia: il passaggio specifico di «Correttezza e supporto».
- Invariante: confidenza alta non certifica la verità fattuale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre risposte corrette e una confidente ma non supportata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Hallucination.
- Prova: SRC-84-001 e sezione pubblica corrispondente.

## Transizione 2. Hallucination

- Ultima affermazione stabile: una risposta con evidenza, confidenza e possibilità di errore.
- Concetto nuovo: Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La tassonomia deve precedere la metrica.
- Input e shape: claim, predizione, fonti e score di confidenza.
- Operazione: verifica, calibrazione, astensione e retrieval.
- Output e shape: risposta supportata o astensione motivata.
- Che cosa cambia: il passaggio specifico di «Hallucination».
- Invariante: confidenza alta non certifica la verità fattuale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre risposte corrette e una confidente ma non supportata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Calibrazione.
- Prova: SRC-84-002 e sezione pubblica corrispondente.

## Transizione 3. Calibrazione

- Ultima affermazione stabile: una risposta con evidenza, confidenza e possibilità di errore.
- Concetto nuovo: Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione.
- Input e shape: claim, predizione, fonti e score di confidenza.
- Operazione: verifica, calibrazione, astensione e retrieval.
- Output e shape: risposta supportata o astensione motivata.
- Che cosa cambia: il passaggio specifico di «Calibrazione».
- Invariante: confidenza alta non certifica la verità fattuale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre risposte corrette e una confidente ma non supportata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Astensione.
- Prova: SRC-84-003 e sezione pubblica corrispondente.

## Transizione 4. Astensione

- Ultima affermazione stabile: una risposta con evidenza, confidenza e possibilità di errore.
- Concetto nuovo: Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e accuracy conditional vanno riportate insieme.
- Input e shape: claim, predizione, fonti e score di confidenza.
- Operazione: verifica, calibrazione, astensione e retrieval.
- Output e shape: risposta supportata o astensione motivata.
- Che cosa cambia: il passaggio specifico di «Astensione».
- Invariante: confidenza alta non certifica la verità fattuale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre risposte corrette e una confidente ma non supportata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Verifica e retrieval.
- Prova: SRC-84-004 e sezione pubblica corrispondente.

## Transizione 5. Verifica e retrieval

- Ultima affermazione stabile: una risposta con evidenza, confidenza e possibilità di errore.
- Concetto nuovo: Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La provenienza deve restare tracciabile.
- Input e shape: claim, predizione, fonti e score di confidenza.
- Operazione: verifica, calibrazione, astensione e retrieval.
- Output e shape: risposta supportata o astensione motivata.
- Che cosa cambia: il passaggio specifico di «Verifica e retrieval».
- Invariante: confidenza alta non certifica la verità fattuale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre risposte corrette e una confidente ma non supportata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutare contesto lungo, RAG, multimodalità e agenti.
- Prova: SRC-84-001 e sezione pubblica corrispondente.
