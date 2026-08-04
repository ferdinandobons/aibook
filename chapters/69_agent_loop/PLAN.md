# Piano interno. Capitolo 69

- Domanda centrale: quale contratto costruisce Ciclo agentico, pianificazione e verifica?
- Oggetto continuo: lo stato di una traiettoria agentica; input guida: osservazione, piano, azione e risultato del tool.
- Prerequisito stabile: Capitolo 68, Protocolli e interoperabilità.
- Gap: observe, plan, act, verify e terminate.
- Output consegnato: stato successivo o arresto motivato; consumer successivo: Capitolo 70, Multi-agent, browser, computer e code agents.
- Invariante principale: ogni side effect deve avere precondizioni e verifica.
- Visuali: LOOP-01 e LOOP-02, con famiglie compositive variabili.
- Snippet: code/snip_69_contract.py; output: code/outputs/SNIP-69-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Osservare e aggiornare lo stato

- Ultima affermazione stabile: lo stato di una traiettoria agentica.
- Concetto nuovo: Un agente riceve input, risultato dei tool e memoria. Lo stato operativo deve essere separato dal testo libero del modello.
- Input e shape: osservazione, piano, azione e risultato del tool.
- Operazione: observe, plan, act, verify e terminate.
- Output e shape: stato successivo o arresto motivato.
- Che cosa cambia: il passaggio specifico di «Osservare e aggiornare lo stato».
- Invariante: ogni side effect deve avere precondizioni e verifica.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup, conferma utente e aggiornamento dell'ordine; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Pianificare.
- Prova: SRC-69-001 e sezione pubblica corrispondente.

## Transizione 2. Pianificare

- Ultima affermazione stabile: lo stato di una traiettoria agentica.
- Concetto nuovo: Un piano scompone il compito in passi e dipendenze. Il piano iniziale può essere rivisto dopo nuove osservazioni.
- Input e shape: osservazione, piano, azione e risultato del tool.
- Operazione: observe, plan, act, verify e terminate.
- Output e shape: stato successivo o arresto motivato.
- Che cosa cambia: il passaggio specifico di «Pianificare».
- Invariante: ogni side effect deve avere precondizioni e verifica.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup, conferma utente e aggiornamento dell'ordine; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Agire.
- Prova: SRC-69-002 e sezione pubblica corrispondente.

## Transizione 3. Agire

- Ultima affermazione stabile: lo stato di una traiettoria agentica.
- Concetto nuovo: Ogni azione usa un tool o modifica un ambiente. Parametri, autorizzazioni e costo devono essere validati.
- Input e shape: osservazione, piano, azione e risultato del tool.
- Operazione: observe, plan, act, verify e terminate.
- Output e shape: stato successivo o arresto motivato.
- Che cosa cambia: il passaggio specifico di «Agire».
- Invariante: ogni side effect deve avere precondizioni e verifica.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup, conferma utente e aggiornamento dell'ordine; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Verificare.
- Prova: SRC-69-003 e sezione pubblica corrispondente.

## Transizione 4. Verificare

- Ultima affermazione stabile: lo stato di una traiettoria agentica.
- Concetto nuovo: Test, controlli di stato o giudici indipendenti valutano il risultato. Una autocritica del modello non equivale a verifica esterna.
- Input e shape: osservazione, piano, azione e risultato del tool.
- Operazione: observe, plan, act, verify e terminate.
- Output e shape: stato successivo o arresto motivato.
- Che cosa cambia: il passaggio specifico di «Verificare».
- Invariante: ogni side effect deve avere precondizioni e verifica.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup, conferma utente e aggiornamento dell'ordine; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Terminare.
- Prova: SRC-69-004 e sezione pubblica corrispondente.

## Transizione 5. Terminare

- Ultima affermazione stabile: lo stato di una traiettoria agentica.
- Concetto nuovo: Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop.
- Input e shape: osservazione, piano, azione e risultato del tool.
- Operazione: observe, plan, act, verify e terminate.
- Output e shape: stato successivo o arresto motivato.
- Che cosa cambia: il passaggio specifico di «Terminare».
- Invariante: ogni side effect deve avere precondizioni e verifica.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup, conferma utente e aggiornamento dell'ordine; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Multi-agent, browser, computer e code agents.
- Prova: SRC-69-001 e sezione pubblica corrispondente.
