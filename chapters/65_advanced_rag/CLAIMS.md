# Registro dei claim. Capitolo 65

| ID | Claim | Prova |
|---|---|---|
| `CL-65-001` | Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni trasformazione può migliorare recall o introdurre drift. | `SRC-65-001` |
| `CL-65-002` | Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un componente da valutare, non un comportamento gratuito del modello. | `SRC-65-002` |
| `CL-65-003` | Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e web fallback richiedono soglie e autorizzazioni. | `SRC-65-003` |
| `CL-65-004` | Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da estrazione, normalizzazione e aggiornamento. | `SRC-65-004` |
| `CL-65-005` | Un agente può pianificare retrieval successivi. Più step aumentano copertura e contemporaneamente costo, errori e superficie di attacco. | `SRC-65-001` |
