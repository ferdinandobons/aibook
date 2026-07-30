# Avanzamento del libro

## Stato corrente

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Pilota: PR `#1`, squash commit `a10235cf384ebda23060a05a3e25ef7b490595a1`
- Branch di produzione: `feature/full-book-production`
- Pull request di produzione: `#2`, draft
- Opera pianificata: 98 capitoli e 12 appendici
- Produzione: seriale controllata
- Capitoli approvati in `main`: 1, `CH-P06-ATTENTION`, prima delle nuove review editoriali
- Unità corrente: `CH-P01-AI-FIELD`, versione `0.3.0-rc2`
- Revisione del Capitolo 28 nel branch: `0.5.0-rc5`
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
6. review di chiarezza per un lettore non esperto;
7. controllo del ritmo e della leggibilità frase per frase;
8. seconda lettura completa;
9. revisione autoriale.

La correttezza non basta quando la lezione suona come una specifica, una checklist o una reference API. La precisione tecnica non deve dipendere dal fatto che il lettore conosca già il gergo che il capitolo dovrebbe spiegare.

## Capitolo 1

### Stato

- Testo: review fattuale, didattica, editoriale, linguistica e di chiarezza per lettore non esperto superate.
- Codice: audit tecnico superato, tre test registrati, nessuna modifica.
- Visuali: aperte.
- Review autoriale completa: non aperta.

### Versione `0.3.0-rc2`

- apertura guidata da tre domande semplici;
- definizione OECD seguita da una spiegazione in linguaggio comune;
- modello e sistema distinti attraverso il caso della spedizione;
- machine learning spiegato come esempi, errore e aggiornamento dei parametri;
- termini del training definiti nel punto d'uso;
- training e inference distinti prima del codice;
- formule mantenute come secondo livello di precisione;
- discriminativo e generativo spiegati con esempi prima della notazione;
- foundation model presentato come base adattabile;
- riepilogo riscritto in prosa continua.

### Visuali aperte

- `AI-01`: da rigenerare;
- `AI-02`: da generare;
- PNG pubblicati: 0.

Dopo l'inserimento occorre ripetere controllo incrociato, review linguistica e lettura integrale.

## Capitolo 28

La versione `0.5.0-rc5` nel branch amplia la review editoriale del pilota con un controllo specifico per il lettore non esperto:

- apertura ancorata alla frase `Il pacco non è arrivato`;
- token, vettore, shape e prodotto scalare spiegati nel punto d'uso;
- query, key e value presentate come ruoli;
- score, scaling, softmax e somma pesata ricomposti in un percorso intuitivo e poi matematico;
- derivazione sulla varianza spostata in un approfondimento;
- formula matriciale introdotta come forma compatta del calcolo già eseguito;
- causal mask spiegata prima come divieto di leggere il futuro;
- un solo snippet completo nel corpo;
- costo quadratico spiegato prima come matrice di `n^2` celle;
- review linguistica e di chiarezza superate.

Aperto:

- ricontrollo di `ATT-01` e `ATT-02` nel nuovo flusso;
- possibile sostituzione di `consumer 1/2` con `posizione 1/2` in `ATT-01`;
- revisione autoriale di `0.5.0-rc5`;
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
-> review per lettore non esperto
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

## Blocco seriale

Il Capitolo 2 non viene aperto finché il Capitolo 1 non supera il gate visuale oppure non viene formalmente sospeso.

Il repository contiene Markdown, formule, tabelle, immagini tecniche, codice, test, output, fonti e audit. Non contiene render raster delle pagine complete.
