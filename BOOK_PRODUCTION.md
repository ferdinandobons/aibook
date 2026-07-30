# Piano operativo per la produzione completa del libro

## Stato

- Branch di produzione: `feature/full-book-production`
- Branch canonico: `main`
- Pull request: `#2`, draft
- Commit di partenza: `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Opera pianificata: 98 capitoli e 12 appendici
- Modalità: produzione seriale controllata
- Unità corrente: `CH-P01-LIFECYCLE`, Capitolo 3, stato `research`
- Data di apertura: 30 luglio 2026

## Documenti operativi

- governance: `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- indice: `docs/01_INDICE_EDITORIALE.md`;
- stile e QA del testo: `docs/02_STILE_E_QA_TESTO.md`;
- visuali: `docs/03_VISUALI.md`;
- fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- workflow e repository: `docs/05_WORKFLOW_E_REPOSITORY.md`;
- catalogo: `docs/14_CATALOGO_STATO_ARTE.md`;
- ricerca globale: `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`.

## Scopo

Questo branch raccoglie la stesura seriale dell'opera **Intelligenza artificiale generativa**. Ogni unità integra testo, fonti, claim, formule, codice, visuali e review prima di lasciare lo stato corrente.

Gli artefatti del libro sono:

- Markdown in prosa da manuale;
- formule e tabelle;
- immagini tecniche con sfondo bianco;
- snippet eseguiti e testati;
- fonti e claim;
- audit tecnici, didattici, editoriali e visuali.

Non vengono prodotti render raster delle pagine, mockup editoriali o screenshot dell'impaginazione.

## Sequenza di produzione

```text
ricerca
-> claim
-> piano interno
-> stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit
-> audit fattuale, matematico e algoritmico
-> controllo incrociato e temporale
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> review per lettore non esperto
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

## Gate prima dell'unità successiva

Una candidatura può lasciare l'unità corrente quando:

- i claim portanti sono verificati;
- formule, date e numeri sono corretti;
- il codice previsto è eseguito e testato;
- le visuali sono validate tecnicamente;
- le review didattica, editoriale, linguistica e di accessibilità sono superate;
- testo, immagini e codice sono coerenti;
- la candidatura completa è disponibile per la revisione autoriale.

La rinomina in `final.png` e il congelamento richiedono approvazione autoriale. La produzione può proseguire sul capitolo successivo mantenendo aperta la review delle candidature complete nel feature branch.

## Quadro dell'opera

| Parte | Intervallo | Capitoli | Stato |
|---|---:|---:|---|
| `P01` Campo, metodo e storia dell'AI | 1-4 | 4 | Capitoli 1 e 2 in revisione autoriale; Capitolo 3 in ricerca; Capitolo 4 pianificato |
| `P02` Matematica, informazione e calcolo | 5-9 | 5 | `planned` |
| `P03` Apprendimento, ottimizzazione e decisione | 10-14 | 5 | `planned` |
| `P04` Reti neurali e rappresentazioni | 15-19 | 5 | `planned` |
| `P05` Modellazione generativa | 20-25 | 6 | `planned` |
| `P06` Sequenze, linguaggio e contesto | 26-31 | 6 | Capitolo 28 in revisione autoriale; altri `planned` |
| `P07` Dati, pretraining e scaling | 32-36 | 5 | `planned` |
| `P08` Progettazione delle architetture | 37-45 | 9 | `planned` |
| `P09` Adattamento, allineamento e ragionamento | 46-54 | 9 | `planned` |
| `P10` Multimodalità e modelli del mondo | 55-62 | 8 | `planned` |
| `P11` Conoscenza esterna, memoria e azione | 63-72 | 10 | `planned` |
| `P12` Efficienza, inference e sistemi | 73-82 | 10 | `planned` |
| `P13` Valutazione, interpretabilità, sicurezza e governance | 83-93 | 11 | `planned` |
| `P14` Laboratori, integrazione e osservatorio | 94-98 | 5 | `planned` |

## Candidature complete

### Capitolo 1. `CH-P01-AI-FIELD`

- versione `0.4.0-rc3`;
- due visuali validate;
- snippet PyTorch e tre test;
- revisione autoriale aperta.

### Capitolo 2. `CH-P01-HISTORY`

- versione `0.2.0-rc1`;
- quattordici fonti primarie e diciotto claim;
- snippet simbolico e tre test;
- due visuali validate;
- revisione autoriale aperta.

### Capitolo 28. `CH-P06-ATTENTION`

- versione `0.6.0-rc6`;
- tre snippet e tre test;
- `ATT-01` corretta e `ATT-02` ricontrollata;
- revisione autoriale aperta.

## Unità corrente

### Capitolo 3. `CH-P01-LIFECYCLE`

Completato:

- piano interno;
- oggetto continuo;
- progressione;
- visuali e snippet pianificati;
- gate specifici.

Da produrre:

- fonti e claim;
- prima stesura;
- codice e test;
- `LIFE-01` e `LIFE-02`;
- audit e seconda lettura.

## Tooling visuale

I generatori raster e il workflow sono:

```text
scripts/generate_book_visuals.py
scripts/generate_history_visuals.py
scripts/integrate_generated_visuals.py
.github/workflows/generate-book-visuals.yml
```

I generatori usano sfondo bianco, controllano il wrapping previsto e verificano che i PNG siano decodificabili. Ogni candidata conserva `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`.

## Aggiornamento del piano

Dopo ogni unità si aggiornano:

- questo file;
- `PROGRESS.md`;
- stato e versione del capitolo;
- date di verifica;
- pull request;
- eventuali modifiche a catalogo e indice.
