# Piano interno. Capitolo 96

- Domanda centrale: quale contratto costruisce Progetto di produzione completo?
- Oggetto continuo: un sistema ML che attraversa sviluppo, rilascio e monitoraggio; input guida: problema, dati, modello, eval, deployment e rollback.
- Prerequisito stabile: Capitolo 95, Costruire un piccolo language model.
- Gap: design, test, release, osservabilità e change management.
- Output consegnato: servizio versionato con metriche e piano di ritorno; consumer successivo: Capitolo 97, Riprodurre e leggere un paper.
- Invariante principale: un modello che passa un test offline non è automaticamente pronto in produzione.
- Visuali: PROJECT-01 e PROJECT-02, con famiglie compositive variabili.
- Snippet: code/snip_96_contract.py; output: code/outputs/SNIP-96-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Definizione del problema

- Ultima affermazione stabile: un sistema ML che attraversa sviluppo, rilascio e monitoraggio.
- Concetto nuovo: Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello.
- Input e shape: problema, dati, modello, eval, deployment e rollback.
- Operazione: design, test, release, osservabilità e change management.
- Output e shape: servizio versionato con metriche e piano di ritorno.
- Che cosa cambia: il passaggio specifico di «Definizione del problema».
- Invariante: un modello che passa un test offline non è automaticamente pronto in produzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: release candidata con gate offline, canary e rollback; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Architettura.
- Prova: SRC-96-001 e sezione pubblica corrispondente.

## Transizione 2. Architettura

- Ultima affermazione stabile: un sistema ML che attraversa sviluppo, rilascio e monitoraggio.
- Concetto nuovo: Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi.
- Input e shape: problema, dati, modello, eval, deployment e rollback.
- Operazione: design, test, release, osservabilità e change management.
- Output e shape: servizio versionato con metriche e piano di ritorno.
- Che cosa cambia: il passaggio specifico di «Architettura».
- Invariante: un modello che passa un test offline non è automaticamente pronto in produzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: release candidata con gate offline, canary e rollback; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione.
- Prova: SRC-96-004 e sezione pubblica corrispondente.

## Transizione 3. Valutazione

- Ultima affermazione stabile: un sistema ML che attraversa sviluppo, rilascio e monitoraggio.
- Concetto nuovo: Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti.
- Input e shape: problema, dati, modello, eval, deployment e rollback.
- Operazione: design, test, release, osservabilità e change management.
- Output e shape: servizio versionato con metriche e piano di ritorno.
- Che cosa cambia: il passaggio specifico di «Valutazione».
- Invariante: un modello che passa un test offline non è automaticamente pronto in produzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: release candidata con gate offline, canary e rollback; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Deployment.
- Prova: SRC-96-002 e sezione pubblica corrispondente.

## Transizione 4. Deployment

- Ultima affermazione stabile: un sistema ML che attraversa sviluppo, rilascio e monitoraggio.
- Concetto nuovo: Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale.
- Input e shape: problema, dati, modello, eval, deployment e rollback.
- Operazione: design, test, release, osservabilità e change management.
- Output e shape: servizio versionato con metriche e piano di ritorno.
- Che cosa cambia: il passaggio specifico di «Deployment».
- Invariante: un modello che passa un test offline non è automaticamente pronto in produzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: release candidata con gate offline, canary e rollback; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Documentazione.
- Prova: SRC-96-003 e sezione pubblica corrispondente.

## Transizione 5. Documentazione

- Ultima affermazione stabile: un sistema ML che attraversa sviluppo, rilascio e monitoraggio.
- Concetto nuovo: Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile.
- Input e shape: problema, dati, modello, eval, deployment e rollback.
- Operazione: design, test, release, osservabilità e change management.
- Output e shape: servizio versionato con metriche e piano di ritorno.
- Che cosa cambia: il passaggio specifico di «Documentazione».
- Invariante: un modello che passa un test offline non è automaticamente pronto in produzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: release candidata con gate offline, canary e rollback; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Riprodurre e leggere un paper.
- Prova: SRC-96-001 e sezione pubblica corrispondente.
