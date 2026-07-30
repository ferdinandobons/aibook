# Avanzamento del libro

## Stato corrente

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Pilota: PR `#1`, squash commit `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Branch di produzione: `feature/full-book-production`
- Pull request di produzione: `#2`, draft
- Opera pianificata: 98 capitoli e 12 appendici
- Produzione: seriale controllata
- Capitoli approvati in `main`: 1, `CH-P06-ATTENTION`, prima della nuova review editoriale
- Unità corrente: `CH-P01-AI-FIELD`, versione `0.2.0-rc1`
- Revisione del Capitolo 28 nel branch: `0.4.0-rc4`
- Ultima ricerca globale: 30 luglio 2026
- Ultima verifica locale delle fonti: 30 luglio 2026

## Documentazione consolidata

La documentazione canonica è stata ridotta a documenti tematici:

- `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- `docs/01_INDICE_EDITORIALE.md`;
- `docs/02_STILE_E_QA_TESTO.md`;
- `docs/03_VISUALI.md`;
- `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- `docs/05_WORKFLOW_E_REPOSITORY.md`;
- `docs/14_CATALOGO_STATO_ARTE.md`;
- `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`;
- `docs/source/` per l'archivio metodologico originale.

I protocolli precedenti sono stati assorbiti per tema. Lo storico resta nel repository Git. `docs/README.md` contiene la mappa di migrazione e la regola che limita la creazione di nuovi file canonici.

## Standard attivi

Ogni capitolo deve superare:

1. audit fattuale, matematico e algoritmico;
2. controllo incrociato e temporale;
3. review didattica;
4. gate anti-template;
5. review editoriale e linguistica;
6. lettura ad alta voce;
7. seconda lettura completa;
8. revisione autoriale.

La correttezza non basta quando la lezione suona come una specifica, una checklist o una reference API.

## Capitolo 1

### Stato

- Testo: review fattuale, didattica, editoriale e linguistica superate.
- Codice: audit tecnico superato, tre test registrati.
- Visuali: aperte.
- Review autoriale completa: non aperta.

### Versione `0.2.0-rc1`

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

Dopo l'inserimento occorre ripetere controllo incrociato, review linguistica e lettura integrale.

## Capitolo 28

La versione `0.4.0-rc4` nel branch riapre la review editoriale del pilota:

- metadati e registro di approvazione fuori dal testo pubblico;
- sezioni principali ridotte a otto;
- score, scaling, softmax e somma pesata ricomposti;
- distinzione key/value rafforzata;
- dettagli API alleggeriti;
- complessità, limiti e ponte multi-head riuniti;
- riepilogo riscritto;
- review linguistica e lettura ad alta voce superate.

Aperto:

- ricontrollo di `ATT-01` e `ATT-02` nel nuovo flusso;
- revisione autoriale di `0.4.0-rc4`;
- nuovo congelamento prima di aggiornare `main`.

## Sequenza di produzione

```text
ricerca
-> claim
-> piano interno
-> stesura
-> formule
-> codice e test
-> visuali e audit
-> audit tecnico
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> lettura ad alta voce
-> seconda lettura
-> revisione autoriale
-> congelamento
```

## Blocco seriale

Il Capitolo 2 non viene aperto finché il Capitolo 1 non supera il gate visuale oppure non viene formalmente sospeso.

Il repository contiene Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit. Non contiene render raster delle pagine complete.
