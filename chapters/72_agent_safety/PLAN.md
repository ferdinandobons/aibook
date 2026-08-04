# Piano editoriale. Capitolo 72

## Obiettivo didattico

Seguire **Sicurezza operativa degli agenti** da input non fidato, tool, scope e approvazione a allow/deny, side effect o rollback auditabile, osservando least privilege, sandbox, human approval e rollback senza oltrepassare questo limite: l'enforcement deve stare fuori dal testo generato.

## Prerequisiti reali

- Capitolo 67: Output strutturato e uso degli strumenti
- Capitolo 69: Ciclo agentico, pianificazione e verifica
- Capitolo 71: Training e valutazione degli agenti

## Percorso della lezione

1. **Least privilege.** Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant. Prova: SRC-72-001.
2. **Sandbox.** Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate. Prova: SRC-72-002.
3. **Human approval.** Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti. Prova: SRC-72-003.
4. **Rollback e audit.** Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria. Prova: SRC-72-004.
5. **Prompt injection.** Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati. Prova: SRC-72-001.

## Prove e artefatti

- riferimento minimo: `code/snip_72_contract.py`; test: `code/test_72_contract.py`; output: `code/outputs/SNIP-72-001.txt`.
- visuali candidate: SAFETY-01, SAFETY-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
