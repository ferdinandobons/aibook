# Avanzamento del libro

## Stato corrente

- Repository operativo: `ferdinandobons/aibook`
- Branch canonico: `main`
- Pull request del pilota: `#1`, unita con squash
- Commit del pilota su `main`: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Branch di produzione completa: `feature/full-book-production`
- Modalità: produzione seriale controllata
- Opera pianificata: 98 capitoli e 12 appendici
- Capitoli approvati e uniti: 1 (`CH-P06-ATTENTION`)
- Unità corrente: `CH-P01-AI-FIELD`, Capitolo 1
- Stato dell'unità corrente: **research**
- Ultima ricerca approfondita globale: 30 luglio 2026
- Standard didattico, visuale e di verifica: attivi

## Capitolo pilota

Il Capitolo 28, `CH-P06-ATTENTION`, è stato approvato dal committente e unito in `main`.

Il pilota ha congelato i principi generali relativi a:

- fonti primarie e documentazione ufficiale;
- registro dei claim;
- review fattuale, matematica, algoritmica e temporale;
- review didattica iterativa;
- struttura logica incorporata nella prosa;
- gate anti-template;
- snippet eseguiti e testati;
- visuali tecniche con sfondo bianco e audit iterativo;
- assenza di render delle pagine.

Il pilota è un riferimento di qualità, non un modello tipografico rigido da replicare in ogni capitolo.

## Produzione completa

Il piano operativo è in [`BOOK_PRODUCTION.md`](BOOK_PRODUCTION.md).

La realizzazione segue l'indice canonico in `docs/10_INDICE_EDITORIALE.md` e procede un capitolo alla volta. Non vengono accumulati capitoli non revisionati.

La sequenza di ogni unità è:

```text
ricerca
-> claim
-> piano interno
-> prima stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit
-> audit fattuale e matematico
-> review didattica
-> gate anti-template
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

## Unità corrente. Capitolo 1

### `CH-P01-AI-FIELD`. Che cos'è l'intelligenza artificiale

Perimetro:

- AI, machine learning, deep learning e AI generativa;
- sistemi simbolici, statistici e neurali;
- modelli discriminativi e generativi;
- foundation model, modelli generalisti e specialistici;
- training, inference, parametri e dati.

Artefatti da produrre:

- `CHAPTER.md`;
- `PLAN.md`;
- `FONTI_PRIMARIE.md`;
- `CLAIMS.md`;
- `TEXT_AUDIT.md`;
- codice PyTorch minimo con test e output;
- visuali tecniche con `SPEC.md`, `AUDIT.md` e alt text.

## Regole attive per tutte le visuali

- sfondo globale bianco puro `#FFFFFF`;
- orientamento orizzontale o verticale in base al contenuto;
- palette, box, frecce e gerarchia tipografica comuni;
- una domanda principale per figura;
- nessun overflow, clipping o collegamento ambiguo;
- prima generazione sempre trattata come bozza;
- `final.png` soltanto dopo approvazione tecnica e autoriale.

## Confine degli artefatti

Il repository contiene testo Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit.

Non vengono prodotti mockup editoriali, screenshot dell'impaginazione o render raster delle pagine complete.

## Prossimo gate

1. completare il dossier delle fonti del Capitolo 1;
2. costruire il registro dei claim;
3. definire il piano didattico interno;
4. scrivere e revisionare il capitolo;
5. creare ed eseguire il codice;
6. generare e revisionare le visuali;
7. aprire la candidatura del Capitolo 1 alla revisione autoriale.
