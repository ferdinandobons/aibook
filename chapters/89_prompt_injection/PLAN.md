# Piano interno. Capitolo 89

- Domanda centrale: quale contratto costruisce Prompt injection e sicurezza dei tool?
- Oggetto continuo: istruzioni e dati che entrano in un sistema con tool; input guida: prompt, documento non fidato, tool e scope.
- Prerequisito stabile: Capitolo 88, Robustezza, jailbreak e attacchi adversarial.
- Gap: separazione, mediazione, allowlist e incident response.
- Output consegnato: azione autorizzata o rifiuto con traccia; consumer successivo: Capitolo 90, Poisoning, backdoor, extraction e supply chain.
- Invariante principale: contenuto recuperato non diventa istruzione privilegiata.
- Visuali: INJECTION-01 e INJECTION-02, con famiglie compositive variabili.
- Snippet: code/snip_89_contract.py; output: code/outputs/SNIP-89-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Istruzioni e dati

- Ultima affermazione stabile: istruzioni e dati che entrano in un sistema con tool.
- Concetto nuovo: Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire automaticamente la priorità delle istruzioni di sistema.
- Input e shape: prompt, documento non fidato, tool e scope.
- Operazione: separazione, mediazione, allowlist e incident response.
- Output e shape: azione autorizzata o rifiuto con traccia.
- Che cosa cambia: il passaggio specifico di «Istruzioni e dati».
- Invariante: contenuto recuperato non diventa istruzione privilegiata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un documento chiede export dati ma il tool lo nega; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Indirect prompt injection.
- Prova: SRC-89-001 e sezione pubblica corrispondente.

## Transizione 2. Indirect prompt injection

- Ultima affermazione stabile: istruzioni e dati che entrano in un sistema con tool.
- Concetto nuovo: Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing.
- Input e shape: prompt, documento non fidato, tool e scope.
- Operazione: separazione, mediazione, allowlist e incident response.
- Output e shape: azione autorizzata o rifiuto con traccia.
- Che cosa cambia: il passaggio specifico di «Indirect prompt injection».
- Invariante: contenuto recuperato non diventa istruzione privilegiata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un documento chiede export dati ma il tool lo nega; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Tool mediation.
- Prova: SRC-89-002 e sezione pubblica corrispondente.

## Transizione 3. Tool mediation

- Ultima affermazione stabile: istruzioni e dati che entrano in un sistema con tool.
- Concetto nuovo: Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma l'enforcement avviene fuori dal testo generato.
- Input e shape: prompt, documento non fidato, tool e scope.
- Operazione: separazione, mediazione, allowlist e incident response.
- Output e shape: azione autorizzata o rifiuto con traccia.
- Che cosa cambia: il passaggio specifico di «Tool mediation».
- Invariante: contenuto recuperato non diventa istruzione privilegiata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un documento chiede export dati ma il tool lo nega; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Data exfiltration.
- Prova: SRC-89-003 e sezione pubblica corrispondente.

## Transizione 4. Data exfiltration

- Ultima affermazione stabile: istruzioni e dati che entrano in un sistema con tool.
- Concetto nuovo: Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL possono diventare canali di esfiltrazione.
- Input e shape: prompt, documento non fidato, tool e scope.
- Operazione: separazione, mediazione, allowlist e incident response.
- Output e shape: azione autorizzata o rifiuto con traccia.
- Che cosa cambia: il passaggio specifico di «Data exfiltration».
- Invariante: contenuto recuperato non diventa istruzione privilegiata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un documento chiede export dati ma il tool lo nega; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Test e incident response.
- Prova: SRC-89-004 e sezione pubblica corrispondente.

## Transizione 5. Test e incident response

- Ultima affermazione stabile: istruzioni e dati che entrano in un sistema con tool.
- Concetto nuovo: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery.
- Input e shape: prompt, documento non fidato, tool e scope.
- Operazione: separazione, mediazione, allowlist e incident response.
- Output e shape: azione autorizzata o rifiuto con traccia.
- Che cosa cambia: il passaggio specifico di «Test e incident response».
- Invariante: contenuto recuperato non diventa istruzione privilegiata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un documento chiede export dati ma il tool lo nega; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Poisoning, backdoor, extraction e supply chain.
- Prova: SRC-89-001 e sezione pubblica corrispondente.
