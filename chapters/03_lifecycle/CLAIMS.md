# Registro dei claim. Capitolo 3

## Stato

- Capitolo: `CH-P01-LIFECYCLE`
- Versione: `0.1.0`
- Ultima verifica: 30 luglio 2026

| ID | Claim sostenibile | Prova | Limite |
|---|---|---|---|
| `CLM-LIFE-001` | Il NIST AI RMF organizza la gestione del rischio nelle funzioni `GOVERN`, `MAP`, `MEASURE` e `MANAGE`. | `SRC-LIFE-001` | framework volontario, non pipeline tecnica unica |
| `CLM-LIFE-002` | La gestione del rischio riguarda l'intero ciclo di vita del sistema, non soltanto il training del modello. | `SRC-LIFE-001`, `002` | il perimetro concreto va definito per il sistema |
| `CLM-LIFE-003` | I datasheet propongono di documentare motivazione, composizione, raccolta, preprocessing, usi e manutenzione dei dataset. | `SRC-LIFE-003` | documentazione non garantisce qualità |
| `CLM-LIFE-004` | Le model card propongono di documentare usi previsti, procedure di valutazione, prestazioni e limiti. | `SRC-LIFE-004` | non sostituiscono test o monitoraggio |
| `CLM-LIFE-005` | Dati e configurazioni introducono dipendenze e debito tecnico specifici nei sistemi ML. | `SRC-LIFE-005` | tassonomia degli autori, non elenco universale |
| `CLM-LIFE-006` | Il ML Test Score include test e monitoraggio su dati, feature, modello e infrastruttura. | `SRC-LIFE-006` | rubrica industriale, non standard universale |
| `CLM-LIFE-007` | TFX orchestra analisi e validazione dei dati, training e serving in una piattaforma di produzione. | `SRC-LIFE-007` | piattaforma e casi specifici |
| `CLM-LIFE-008` | Quando i dati cambiano nel tempo, un sistema può richiedere nuovi modelli e controlli continui. | `SRC-LIFE-007` | non ogni cambiamento richiede retraining |
| `CLM-LIFE-009` | Lo studio di Amershi et al. descrive un workflow a più fasi e difficoltà specifiche di dati, versioning, riuso e modularizzazione. | `SRC-LIFE-008` | studio di team Microsoft |
| `CLM-LIFE-010` | Il training set serve ad aggiornare i parametri, la validation a scegliere configurazioni e il test a stimare il risultato finale del protocollo dichiarato. | `SRC-LIFE-009` | split e procedure dipendono dalla struttura dei dati |
| `CLM-LIFE-011` | Usare il test set per scegliere ripetutamente configurazioni compromette il suo ruolo di valutazione finale. | `SRC-LIFE-009` | formulazione riferita al protocollo standard descritto |
| `CLM-LIFE-012` | Deployment indica l'integrazione e distribuzione di una versione del sistema; inference indica l'elaborazione di input con parametri disponibili. | convenzione del libro, `SRC-LIFE-007`, `010` | definizioni operative, non standard universale |
| `CLM-LIFE-013` | Una modifica a retrieval, prompt, regole, strumenti o autorizzazioni può cambiare il comportamento del sistema senza cambiare il checkpoint. | sintesi da `SRC-LIFE-005`, `007`, `008` | claim sul sistema, non sul solo modello |
| `CLM-LIFE-014` | Una differenza nella distribuzione degli input può essere monitorata senza dimostrare da sola una degradazione causale della qualità. | derivazione statistica e confine editoriale | richiede metriche e analisi ulteriori |
| `CLM-LIFE-015` | Un monitor non garantisce di rilevare ogni errore o incidente. | `SRC-LIFE-001`, `002`, `005`, `006` | formulazione di confine |
| `CLM-LIFE-016` | Rollback, aggiornamento e ritiro richiedono identificazione della versione e artefatti riproducibili. | `SRC-LIFE-001`, `006`, `007`, `008` | implementazione specifica al contesto |
| `CLM-LIFE-017` | Una buona metrica offline non implica automaticamente utilità, sicurezza o qualità del prodotto. | `SRC-LIFE-001`, `004`, `005`, `008` | devono essere definite metriche e vincoli di sistema |
| `CLM-LIFE-018` | Il ciclo di vita viene rappresentato nel capitolo come iterativo, con artefatti e gate tra le fasi. | `PLAN.md` | convenzione didattica, non pipeline universale |

## Claim esclusi

- `un dataset documentato è automaticamente affidabile`;
- `una model card garantisce uso responsabile`;
- `deployment e inference sono sinonimi`;
- `un aumento della loss in produzione dimostra data drift`;
- `data drift dimostra che il modello è peggiorato`;
- `monitorare la media delle feature rileva ogni cambiamento rilevante`;
- `un test set può essere consultato senza limiti durante lo sviluppo`;
- `un checkpoint identifica da solo l'intero sistema distribuito`.
