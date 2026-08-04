# Piano editoriale. Capitolo 89

## Obiettivo didattico

Seguire **Prompt injection e sicurezza dei tool** da prompt, documento non fidato, tool e scope a azione autorizzata o rifiuto con traccia, osservando separazione, mediazione, allowlist e incident response senza oltrepassare questo limite: contenuto recuperato non diventa istruzione privilegiata.

## Prerequisiti reali

- Capitolo 67: Output strutturato e uso degli strumenti
- Capitolo 72: Sicurezza operativa degli agenti
- Capitolo 88: Robustezza, jailbreak e attacchi adversarial

## Percorso della lezione

1. **Istruzioni e dati.** Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire automaticamente la priorità delle istruzioni di sistema. Prova: SRC-89-001.
2. **Indirect prompt injection.** Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing. Prova: SRC-89-002.
3. **Tool mediation.** Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma l'enforcement avviene fuori dal testo generato. Prova: SRC-89-003.
4. **Data exfiltration.** Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL possono diventare canali di esfiltrazione. Prova: SRC-89-004.
5. **Test e incident response.** Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery. Prova: SRC-89-001.

## Prove e artefatti

- riferimento minimo: `code/snip_89_contract.py`; test: `code/test_89_contract.py`; output: `code/outputs/SNIP-89-001.txt`.
- visuali candidate: INJECTION-01, INJECTION-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
