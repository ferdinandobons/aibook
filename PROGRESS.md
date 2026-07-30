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
- Capitoli approvati in `main`: 1 (`CH-P06-ATTENTION`, versione precedente alla nuova review editoriale)
- Unità corrente: `CH-P01-AI-FIELD`
- Versione corrente Capitolo 1: `0.2.0-rc1`
- Revisione corrente Capitolo 28 nel branch: `0.4.0-rc4`
- Ultima ricerca approfondita globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 30 luglio 2026

## Nuovo standard editoriale

È stato adottato `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

Ogni capitolo deve ora superare:

1. audit tecnico;
2. review didattica;
3. gate anti-template;
4. review editoriale e linguistica;
5. lettura ad alta voce;
6. seconda lettura completa;
7. revisione autoriale.

La correttezza non è sufficiente se la lezione suona come una specifica, una checklist o una reference API.

## Capitolo 1

### Stato

- Testo: review fattuale, didattica, editoriale e linguistica superate.
- Codice: audit tecnico superato, tre test registrati.
- Visuali: bloccate.
- Review autoriale completa: non aperta.

### Riscrittura `0.2.0-rc1`

- metadati spostati in un commento non renderizzato;
- sezioni principali ridotte da sedici a otto;
- esempio `Il pacco non è arrivato` mantenuto nel percorso;
- tassonomia organizzata per meccanismo, obiettivo e ampiezza;
- training e inference raccolti in una sezione continua;
- dettagli PyTorch spostati in una nota;
- cautele duplicate ridotte;
- italiano e ritmo revisionati;
- lettura ad alta voce superata.

### Visuali aperte

- `AI-01`: da rigenerare;
- `AI-02`: da generare;
- PNG pubblicati: 0.

Dopo l'inserimento delle figure occorre ripetere controllo incrociato, review linguistica e lettura integrale.

## Capitolo 28

### Stato nel branch

La versione `0.4.0-rc4` riapre la review editoriale del capitolo pilota già presente in `main`.

Modifiche:

- metadati e registro di approvazione fuori dal testo pubblico;
- sezioni principali ridotte a otto;
- score, scaling, softmax e somma pesata ricomposti in una sezione;
- distinzione key/value rafforzata;
- dettagli API alleggeriti;
- complessità, limiti e ponte multi-head riuniti;
- riepilogo riscritto;
- review linguistica e lettura ad alta voce superate.

Aperto:

- ricontrollo di `ATT-01` e `ATT-02` nel nuovo flusso;
- revisione autoriale della versione `0.4.0-rc4`;
- nuovo congelamento prima di aggiornare `main`.

## Documentazione aggiornata

Sono stati aggiornati:

- `docs/00_CONTRATTO_EDITORIALE.md`;
- `docs/01_TEMPLATE_CAPITOLO.md`;
- `docs/04_PROTOCOLLO_QA_TESTO.md`;
- `docs/06_WORKFLOW_CAPITOLO.md`;
- `docs/08_REGISTRO_DECISIONI.md`;
- `docs/11_AUDIT_DOCUMENTAZIONE.md`;
- `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`;
- `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- `docs/README.md`;
- `GUIDELINE.md`;
- `README.md`;
- `BOOK_PRODUCTION.md`.

La decisione è registrata come `DEC-048`.

## Sequenza di produzione

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
-> review linguistica
-> lettura ad alta voce
-> seconda lettura
-> revisione autoriale
-> congelamento
```

## Blocco seriale

Il Capitolo 2 non viene aperto finché il Capitolo 1 non supera il gate visuale oppure non viene formalmente sospeso con una decisione esplicita.

Il repository contiene testo Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit. Non contiene render raster delle pagine complete.
