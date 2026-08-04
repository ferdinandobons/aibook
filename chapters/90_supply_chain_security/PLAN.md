# Piano interno. Capitolo 90

- Domanda centrale: quale contratto costruisce Poisoning, backdoor, extraction e supply chain?
- Oggetto continuo: gli artefatti che attraversano la supply chain del modello; input guida: dataset, checkpoint, repository, digest e owner.
- Prerequisito stabile: Capitolo 89, Prompt injection e sicurezza dei tool.
- Gap: poisoning, backdoor, extraction e controllo di provenienza.
- Output consegnato: artefatto rilasciato, traccia e decisione di blocco; consumer successivo: Capitolo 91, Privacy, fairness e unlearning.
- Invariante principale: integrità del file non certifica assenza di contenuto malevolo.
- Visuali: SECURITY-01 e SECURITY-02, con famiglie compositive variabili.
- Snippet: code/snip_90_contract.py; output: code/outputs/SNIP-90-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Data poisoning

- Ultima affermazione stabile: gli artefatti che attraversano la supply chain del modello.
- Concetto nuovo: Campioni modificati possono alterare comportamento generale o target specifici. Provenienza e deduplicazione riducono alcune superfici.
- Input e shape: dataset, checkpoint, repository, digest e owner.
- Operazione: poisoning, backdoor, extraction e controllo di provenienza.
- Output e shape: artefatto rilasciato, traccia e decisione di blocco.
- Che cosa cambia: il passaggio specifico di «Data poisoning».
- Invariante: integrità del file non certifica assenza di contenuto malevolo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest uguale ma dataset contaminato da una regola nascosta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Backdoor.
- Prova: SRC-90-001 e sezione pubblica corrispondente.

## Transizione 2. Backdoor

- Ultima affermazione stabile: gli artefatti che attraversano la supply chain del modello.
- Concetto nuovo: Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove. Scanner e fine-tuning non garantiscono rimozione.
- Input e shape: dataset, checkpoint, repository, digest e owner.
- Operazione: poisoning, backdoor, extraction e controllo di provenienza.
- Output e shape: artefatto rilasciato, traccia e decisione di blocco.
- Che cosa cambia: il passaggio specifico di «Backdoor».
- Invariante: integrità del file non certifica assenza di contenuto malevolo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest uguale ma dataset contaminato da una regola nascosta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Model extraction.
- Prova: SRC-90-002 e sezione pubblica corrispondente.

## Transizione 3. Model extraction

- Ultima affermazione stabile: gli artefatti che attraversano la supply chain del modello.
- Concetto nuovo: Query e output possono permettere di imitare capacità o recuperare informazioni. Rate limit e watermark comportamentali hanno limiti.
- Input e shape: dataset, checkpoint, repository, digest e owner.
- Operazione: poisoning, backdoor, extraction e controllo di provenienza.
- Output e shape: artefatto rilasciato, traccia e decisione di blocco.
- Che cosa cambia: il passaggio specifico di «Model extraction».
- Invariante: integrità del file non certifica assenza di contenuto malevolo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest uguale ma dataset contaminato da una regola nascosta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Artifact security.
- Prova: SRC-90-003 e sezione pubblica corrispondente.

## Transizione 4. Artifact security

- Ultima affermazione stabile: gli artefatti che attraversano la supply chain del modello.
- Concetto nuovo: Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro.
- Input e shape: dataset, checkpoint, repository, digest e owner.
- Operazione: poisoning, backdoor, extraction e controllo di provenienza.
- Output e shape: artefatto rilasciato, traccia e decisione di blocco.
- Che cosa cambia: il passaggio specifico di «Artifact security».
- Invariante: integrità del file non certifica assenza di contenuto malevolo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest uguale ma dataset contaminato da una regola nascosta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Repository e deployment.
- Prova: SRC-90-004 e sezione pubblica corrispondente.

## Transizione 5. Repository e deployment

- Ultima affermazione stabile: gli artefatti che attraversano la supply chain del modello.
- Concetto nuovo: File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici.
- Input e shape: dataset, checkpoint, repository, digest e owner.
- Operazione: poisoning, backdoor, extraction e controllo di provenienza.
- Output e shape: artefatto rilasciato, traccia e decisione di blocco.
- Che cosa cambia: il passaggio specifico di «Repository e deployment».
- Invariante: integrità del file non certifica assenza di contenuto malevolo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest uguale ma dataset contaminato da una regola nascosta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Privacy, fairness e unlearning.
- Prova: SRC-90-001 e sezione pubblica corrispondente.
