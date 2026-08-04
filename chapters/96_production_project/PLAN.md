# Piano editoriale. Capitolo 96

## Obiettivo didattico

Seguire **Progetto di produzione completo** da problema, dati, modello, eval, deployment e rollback a servizio versionato con metriche e piano di ritorno, osservando design, test, release, osservabilità e change management senza oltrepassare questo limite: un modello che passa un test offline non è automaticamente pronto in produzione.

## Prerequisiti reali

- Capitolo 64: Retrieval-Augmented Generation
- Capitolo 67: Output strutturato e uso degli strumenti
- Capitolo 72: Sicurezza operativa degli agenti
- Capitolo 82: LLMOps, edge, costo ed energia
- Capitolo 85: Valutare contesto lungo, RAG, multimodalità e agenti

## Percorso della lezione

1. **Definizione del problema.** Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello. Prova: SRC-96-001.
2. **Architettura.** Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi. Prova: SRC-96-004.
3. **Valutazione.** Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti. Prova: SRC-96-002.
4. **Deployment.** Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale. Prova: SRC-96-003.
5. **Documentazione.** Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile. Prova: SRC-96-001.

## Prove e artefatti

- riferimento minimo: `code/snip_96_contract.py`; test: `code/test_96_contract.py`; output: `code/outputs/SNIP-96-001.txt`.
- laboratorio esteso: `code/production_pipeline.py`; test: `code/test_production_pipeline.py`; output: `code/outputs/PRODUCTION-PIPELINE.txt`.
- visuali candidate: PROJECT-01, PROJECT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
