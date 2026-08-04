# Piano editoriale. Capitolo 90

## Obiettivo didattico

Seguire **Poisoning, backdoor, extraction e supply chain** da dataset, checkpoint, repository, digest e owner a artefatto rilasciato, traccia e decisione di blocco, osservando poisoning, backdoor, extraction e controllo di provenienza senza oltrepassare questo limite: integrità del file non certifica assenza di contenuto malevolo.

## Prerequisiti reali

- Capitolo 32: Il ciclo di vita dei dati
- Capitolo 72: Sicurezza operativa degli agenti

## Percorso della lezione

1. **Data poisoning.** Campioni modificati possono alterare comportamento generale o target specifici. Provenienza e deduplicazione riducono alcune superfici. Prova: SRC-90-001.
2. **Backdoor.** Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove. Scanner e fine-tuning non garantiscono rimozione. Prova: SRC-90-002.
3. **Model extraction.** Query e output possono permettere di imitare capacità o recuperare informazioni. Rate limit e watermark comportamentali hanno limiti. Prova: SRC-90-003.
4. **Artifact security.** Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro. Prova: SRC-90-004.
5. **Repository e deployment.** File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici. Prova: SRC-90-001.

## Prove e artefatti

- riferimento minimo: `code/snip_90_contract.py`; test: `code/test_90_contract.py`; output: `code/outputs/SNIP-90-001.txt`.
- visuali candidate: SECURITY-01, SECURITY-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
