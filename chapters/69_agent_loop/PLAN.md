# Piano editoriale. Capitolo 69

## Obiettivo didattico

Seguire **Ciclo agentico, pianificazione e verifica** da osservazione, piano, azione e risultato del tool a stato successivo o arresto motivato, osservando observe, plan, act, verify e terminate senza oltrepassare questo limite: ogni side effect deve avere precondizioni e verifica.

## Prerequisiti reali

- Capitolo 14: Reinforcement learning
- Capitolo 67: Output strutturato e uso degli strumenti

## Percorso della lezione

1. **Osservare e aggiornare lo stato.** Un agente riceve input, risultato dei tool e memoria. Lo stato operativo deve essere separato dal testo libero del modello. Prova: SRC-69-001.
2. **Pianificare.** Un piano scompone il compito in passi e dipendenze. Il piano iniziale può essere rivisto dopo nuove osservazioni. Prova: SRC-69-002.
3. **Agire.** Ogni azione usa un tool o modifica un ambiente. Parametri, autorizzazioni e costo devono essere validati. Prova: SRC-69-003.
4. **Verificare.** Test, controlli di stato o giudici indipendenti valutano il risultato. Una autocritica del modello non equivale a verifica esterna. Prova: SRC-69-004.
5. **Terminare.** Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop. Prova: SRC-69-001.

## Prove e artefatti

- riferimento minimo: `code/snip_69_contract.py`; test: `code/test_69_contract.py`; output: `code/outputs/SNIP-69-001.txt`.
- visuali candidate: LOOP-01, LOOP-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
