# Piano interno. Capitolo 72

- Domanda centrale: quale contratto costruisce Sicurezza operativa degli agenti?
- Oggetto continuo: una decisione agentica su una risorsa reale; input guida: input non fidato, tool, scope e approvazione.
- Prerequisito stabile: Capitolo 71, Training e valutazione degli agenti.
- Gap: least privilege, sandbox, human approval e rollback.
- Output consegnato: allow/deny, side effect o rollback auditabile; consumer successivo: Capitolo 73, Distillazione e pruning.
- Invariante principale: l'enforcement deve stare fuori dal testo generato.
- Visuali: SAFETY-01 e SAFETY-02, con famiglie compositive variabili.
- Snippet: code/snip_72_contract.py; output: code/outputs/SNIP-72-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Least privilege

- Ultima affermazione stabile: una decisione agentica su una risorsa reale.
- Concetto nuovo: Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant.
- Input e shape: input non fidato, tool, scope e approvazione.
- Operazione: least privilege, sandbox, human approval e rollback.
- Output e shape: allow/deny, side effect o rollback auditabile.
- Che cosa cambia: il passaggio specifico di «Least privilege».
- Invariante: l'enforcement deve stare fuori dal testo generato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: refund bloccato e lookup consentito con log firmato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sandbox.
- Prova: SRC-72-001 e sezione pubblica corrispondente.

## Transizione 2. Sandbox

- Ultima affermazione stabile: una decisione agentica su una risorsa reale.
- Concetto nuovo: Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate.
- Input e shape: input non fidato, tool, scope e approvazione.
- Operazione: least privilege, sandbox, human approval e rollback.
- Output e shape: allow/deny, side effect o rollback auditabile.
- Che cosa cambia: il passaggio specifico di «Sandbox».
- Invariante: l'enforcement deve stare fuori dal testo generato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: refund bloccato e lookup consentito con log firmato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Human approval.
- Prova: SRC-72-002 e sezione pubblica corrispondente.

## Transizione 3. Human approval

- Ultima affermazione stabile: una decisione agentica su una risorsa reale.
- Concetto nuovo: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti.
- Input e shape: input non fidato, tool, scope e approvazione.
- Operazione: least privilege, sandbox, human approval e rollback.
- Output e shape: allow/deny, side effect o rollback auditabile.
- Che cosa cambia: il passaggio specifico di «Human approval».
- Invariante: l'enforcement deve stare fuori dal testo generato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: refund bloccato e lookup consentito con log firmato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Rollback e audit.
- Prova: SRC-72-003 e sezione pubblica corrispondente.

## Transizione 4. Rollback e audit

- Ultima affermazione stabile: una decisione agentica su una risorsa reale.
- Concetto nuovo: Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria.
- Input e shape: input non fidato, tool, scope e approvazione.
- Operazione: least privilege, sandbox, human approval e rollback.
- Output e shape: allow/deny, side effect o rollback auditabile.
- Che cosa cambia: il passaggio specifico di «Rollback e audit».
- Invariante: l'enforcement deve stare fuori dal testo generato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: refund bloccato e lookup consentito con log firmato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prompt injection.
- Prova: SRC-72-004 e sezione pubblica corrispondente.

## Transizione 5. Prompt injection

- Ultima affermazione stabile: una decisione agentica su una risorsa reale.
- Concetto nuovo: Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati.
- Input e shape: input non fidato, tool, scope e approvazione.
- Operazione: least privilege, sandbox, human approval e rollback.
- Output e shape: allow/deny, side effect o rollback auditabile.
- Che cosa cambia: il passaggio specifico di «Prompt injection».
- Invariante: l'enforcement deve stare fuori dal testo generato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: refund bloccato e lookup consentito con log firmato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Distillazione e pruning.
- Prova: SRC-72-001 e sezione pubblica corrispondente.
