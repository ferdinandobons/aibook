# Avanzamento del libro

## Stato corrente

- Repository operativo: `ferdinandobons/aibook`
- Branch canonico: `main`
- Pull request del pilota: `#1`, unita con squash
- Commit del pilota su `main`: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Branch di produzione completa: `feature/full-book-production`
- Pull request di produzione: `#2`, draft
- Modalità: produzione seriale controllata
- Opera pianificata: 98 capitoli e 12 appendici
- Capitoli approvati e uniti: 1 (`CH-P06-ATTENTION`)
- Unità corrente: `CH-P01-AI-FIELD`, Capitolo 1
- Stato dell'unità corrente: **technical-review, visuali bloccate**
- Versione corrente: `0.1.1-draft2`
- Ultima ricerca approfondita globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 30 luglio 2026

## Capitolo pilota

Il Capitolo 28, `CH-P06-ATTENTION`, è stato approvato dal committente e unito in `main`.

Il pilota ha congelato i principi generali relativi a fonti, claim, review iterative, prosa naturale, gate anti-template, codice testato, visuali con audit e assenza di render delle pagine. Rimane un riferimento di qualità, non un modello tipografico rigido.

## Produzione completa

Il piano operativo è in [`BOOK_PRODUCTION.md`](BOOK_PRODUCTION.md). La realizzazione segue `docs/10_INDICE_EDITORIALE.md` e procede un capitolo alla volta.

```text
ricerca
-> claim
-> piano interno
-> prosa
-> formule
-> codice e test
-> visuali e audit
-> audit fattuale e matematico
-> review didattica
-> gate anti-template
-> seconda lettura
-> revisione autoriale
-> congelamento
```

## Unità corrente. Capitolo 1

### `CH-P01-AI-FIELD`. Che cos'è l'intelligenza artificiale

### Completato

- [x] perimetro e piano didattico;
- [x] dossier delle fonti autorevoli;
- [x] registro di 18 claim;
- [x] prima stesura completa;
- [x] revisione fattuale e terminologica della prima stesura;
- [x] seconda stesura `0.1.1-draft2`;
- [x] seconda lettura completa del testo;
- [x] snippet PyTorch training/inference;
- [x] ambiente e output registrati;
- [x] tre test superati;
- [x] audit del codice;
- [x] specifiche, audit e alt text previsti per `AI-01` e `AI-02`.

### Stato delle visuali

- `AI-01`: `da rigenerare`;
- `AI-02`: `da generare`;
- PNG pubblicati: 0.

Le candidate prodotte dallo strumento immagini non rappresentavano la tassonomia o il confronto richiesti. Mostravano schermate GitHub, merge, branch, dashboard di progetto o indici del libro. Sono state respinte e non sono state inserite nel repository.

Il problema è documentato in:

- `assets/chapters/01_ai_field/AI-01/AUDIT.md`;
- `assets/chapters/01_ai_field/AI-02/AUDIT.md`;
- `chapters/01_ai_field/TEXT_AUDIT.md`.

### Gate aperti

1. produrre una candidata conforme per `AI-01`;
2. produrre una candidata conforme per `AI-02`;
3. eseguire audit tecnico e compositivo di entrambe;
4. integrare le figure nella prosa;
5. ripetere il controllo incrociato completo;
6. aprire la review autoriale del Capitolo 1.

## Regole attive per le visuali

- sfondo globale bianco puro `#FFFFFF`;
- orientamento scelto in base al contenuto;
- palette, box, frecce e tipografia comuni;
- una domanda principale per figura;
- nessun overflow, clipping o collegamento ambiguo;
- prima generazione sempre trattata come bozza;
- nessun elemento relativo al repository quando non appartiene al contenuto didattico;
- `final.png` soltanto dopo approvazione tecnica e autoriale.

## Confine degli artefatti

Il repository contiene testo Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit. Non vengono prodotti mockup editoriali, screenshot dell'impaginazione o render raster delle pagine complete.

## Blocco seriale

Il Capitolo 2 non viene aperto finché il Capitolo 1 non supera il gate visuale o non viene formalmente sospeso con una decisione esplicita. Questa scelta evita di accumulare capitoli incompleti.
