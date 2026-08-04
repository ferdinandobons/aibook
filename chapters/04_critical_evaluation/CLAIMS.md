# Registro dei claim. Capitolo 4

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-EVAL-001` | Una metrica va interpretata rispetto a obiettivo, contesto d'uso e rischio del sistema. | `SRC-EVAL-001`, `SRC-EVAL-002` | verificata |
| `CLM-EVAL-002` | Una baseline rende interpretabile il vantaggio rispetto a una soluzione di riferimento. | derivazione metodologica; `SRC-EVAL-013` per reporting dei baseline | verificata |
| `CLM-EVAL-003` | Training, validation e test hanno ruoli differenti; usare il test per scegliere configurazioni ne riduce l'indipendenza. | Goodfellow et al. cap. 5, già verificato nel Capitolo 3; `SRC-EVAL-013` | verificata |
| `CLM-EVAL-004` | L'accuratezza media può nascondere risultati diversi su sottoinsiemi rilevanti. | derivazione aritmetica e `SNIP-EVAL-001`; `SRC-EVAL-012` per reporting per gruppi/condizioni | verificata |
| `CLM-EVAL-005` | Il costo pratico degli errori può essere asimmetrico e non è determinato dall'accuratezza media. | convenzione esplicita e risultato eseguito `SNIP-EVAL-001` | verificata |
| `CLM-EVAL-006` | Inizializzazione, campionamento, augmentazione e tuning possono introdurre variabilità nei benchmark. | `SRC-EVAL-004` | verificata |
| `CLM-EVAL-007` | Un singolo run non descrive necessariamente la distribuzione dei risultati della pipeline. | `SRC-EVAL-004`, `SRC-EVAL-013` | verificata |
| `CLM-EVAL-008` | La scelta del test statistico dipende dalla misura, dal setup e dalla dipendenza tra osservazioni. | `SRC-EVAL-005` | verificata |
| `CLM-EVAL-009` | Un intervallo che include zero non dimostra che i modelli siano equivalenti; indica che il campione e il metodo usati non escludono differenze in entrambe le direzioni. | interpretazione statistica limitata allo snippet; `SRC-EVAL-005`, `SRC-EVAL-006` | verificata |
| `CLM-EVAL-010` | Leakage si verifica quando la pipeline usa informazione sul target non legittimamente disponibile al momento della previsione. | `SRC-EVAL-009` | verificata |
| `CLM-EVAL-011` | Prestazioni su un benchmark riutilizzato possono non trasferire identicamente a un nuovo test set costruito con procedure simili. | `SRC-EVAL-007` | verificato con limite |
| `CLM-EVAL-012` | Errori nelle label del test set possono alterare il confronto e il ranking dei modelli. | `SRC-EVAL-008` | verificato con limite |
| `CLM-EVAL-013` | Un modello può sfruttare shortcut che funzionano sul benchmark ma falliscono in condizioni più impegnative. | `SRC-EVAL-010` | verificata |
| `CLM-EVAL-014` | Nei LLM, esempi di benchmark presenti nei dati di pretraining possono rendere la valutazione meno informativa sulla generalizzazione. | `SRC-EVAL-011` | verificato con limite |
| `CLM-EVAL-015` | Una ablation restringe il contributo attribuibile a un componente soltanto se il resto del protocollo resta sufficientemente controllato. | derivazione metodologica | verificata |
| `CLM-EVAL-016` | Riproducibilità richiede informazioni su codice, dati, ambiente e procedura, non soltanto il punteggio finale. | `SRC-EVAL-003`, `SRC-EVAL-013` | verificata |
| `CLM-EVAL-017` | Model card e documentazione degli artefatti rendono visibili uso previsto, condizioni, metriche e limiti, ma non certificano la qualità. | `SRC-EVAL-012` | verificata |
| `CLM-EVAL-018` | Nel dataset illustrativo, il modello B ha accuratezza media maggiore, ma prestazione peggiore sulla slice urgente e costo pesato maggiore. | `SNIP-EVAL-001`, test automatici | verificata |
| `CLM-EVAL-019` | Nel bootstrap appaiato illustrativo, la differenza B-A è `0.042` e l'intervallo percentile al 95% è `[-0.208, 0.292]`. | `SNIP-EVAL-001`, seed 7, 10.000 resample | verificata |

## Claim esclusi

- un benchmark non misura automaticamente ogni proprietà del sistema;
- significatività statistica non implica automaticamente utilità pratica;
- assenza di significatività non dimostra equivalenza;
- una ablation singola non dimostra una catena causale completa;
- contaminazione non viene presunta senza evidenza;
- i costi `1` e `4` dello snippet sono illustrativi e non derivano da dati operativi reali.
