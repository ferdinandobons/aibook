# Audit del testo. Capitolo 28

## Stato

- Versione corrente: `0.6.0-rc6`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato**
- Esito di chiarezza per lettore non esperto: **superato**
- Codice: invariato, tre test registrati superati
- Visuali: **validate tecnicamente e ricontrollate nel nuovo flusso**
- Controllo incrociato testo-visuali-codice: **superato**
- Review autoriale: aperta

## Cronologia delle review respinte

### `DID-ATT-01`. Struttura e gate

- Versione: `0.1.0-rc1`
- Esito: **respinta**
- Difetti: query, key e value anticipate; nome dell'operatore prima del meccanismo; pseudocodice assente; mask matematica e semantica API combinate; multi-head anticipata.

### `DID-ATT-03`. Gate anti-template

- Versione: `0.2.0-rc2`
- Esito: **respinta**
- Difetti: intestazioni metacognitive ripetute, microsezioni, contratti degli snippet esposti e superficie simile a una checklist.

### `EDIT-ATT-01`. Lettura come manuale

- Versione: `0.3.0-rc3`
- Esito: **respinta**
- Difetti: troppe sezioni, calcolo frammentato, voce da documentazione, dettagli API invasivi, esempio poco ancorato al problema sequenziale, conclusione simile a una checklist.

### `EDIT-ATT-03`. Lettore non esperto

- Versione: `0.4.0-rc4`
- Esito: **respinta**
- Difetti: token, vettore, shape e prodotto scalare non spiegati abbastanza presto; formula e API ancora troppo centrali; costo quadratico introdotto senza prima mostrare le `n²` coppie.

## Review superate

### `DID-ATT-04`. Struttura logica in prosa

La versione in prosa conserva il percorso verificabile senza mostrare lo scaffold come una serie di titoli.

### `EDIT-ATT-02`. Voce da manuale

- sezioni principali ridotte;
- score, scaling, softmax e somma pesata riuniti in un unico percorso;
- metadati e audit esclusi dal testo pubblico;
- dettagli PyTorch raccolti in nota;
- riepilogo ricostruito dal problema iniziale.

### `EDIT-ATT-04`. Chiarezza per lettore non esperto

- Versione: `0.5.0-rc5`
- Esito: **superato dopo riscrittura completa**

Controlli:

- [x] apertura ancorata alla frase `Il pacco non è arrivato`;
- [x] token spiegato come parola o parte di parola;
- [x] vettore spiegato come lista di numeri;
- [x] query, key e value introdotte come ruoli matematici;
- [x] shape `[3,2]` tradotta in tre righe e due valori per riga;
- [x] prodotto scalare spiegato prima della notazione compatta;
- [x] softmax spiegata come trasformazione in quote non negative che sommano a uno;
- [x] derivazione sulla varianza confinata in un approfondimento;
- [x] formula generale dopo il calcolo numerico;
- [x] causal mask spiegata come divieto di leggere il futuro prima della formula;
- [x] un solo snippet completo nel corpo;
- [x] costo quadratico spiegato prima con la matrice di `n²` celle;
- [x] seconda lettura completa superata.

## `VIS-ATT-01`. Controllo visuale e integrazione

- Versione: `0.6.0-rc6`
- Figure: `ATT-01/candidate-v3.png`, `ATT-02/candidate-v2.png`
- Esito: **superato tecnicamente**

### `ATT-01`

- [x] `consumer 1/2` sostituito con `Posizione 1/2`;
- [x] stesso vettore `c` mostrato per entrambe le posizioni nel pannello sinistro;
- [x] query separate dai coefficienti nel pannello destro;
- [x] coefficienti di `q₁`: `0,10`, `0,60`, `0,30`;
- [x] coefficienti di `q₂`: `0,05`, `0,15`, `0,80`;
- [x] entrambe le righe sommano a `1,00`;
- [x] output `c₁` e `c₂` distinti;
- [x] alt text corretto e verificato;
- [x] testo e simboli contenuti nei box;
- [x] sfondo bianco e collegamenti non ambigui.

### `ATT-02`

- [x] input, score, scaling, softmax, somma pesata e output nello stesso ordine del testo;
- [x] valori numerici coerenti con lo snippet;
- [x] shape coerenti;
- [x] coefficienti non negativi e somma pari a uno;
- [x] output con dimensione `d_v`;
- [x] nessun overflow o collegamento ambiguo noto.

### Controllo incrociato

- [x] la prosa usa `Posizione 1/2` come la nuova figura;
- [x] `ATT-01` precede la terminologia query-key-value;
- [x] `ATT-02` segue lo stesso esempio di testo e codice;
- [x] nessuna figura introduce multi-head, posizione o ottimizzazioni hardware;
- [x] rilettura completa eseguita dopo il cambio di `ATT-01`.

## Audit tecnico

- [x] claim portanti verificati;
- [x] formula della scaled dot-product attention corretta;
- [x] shape di `Q`, `K`, `V`, score, coefficienti e output corrette;
- [x] valori dell'esempio principale coerenti con i test;
- [x] valori `c₁=[0,40;0,90]` e `c₂=[0,85;0,95]` ricalcolati;
- [x] ordine score, scaling, mask opzionale, softmax e prodotto con `V` corretto;
- [x] mask applicata agli score;
- [x] complessità del caso materializzato corretta;
- [x] ambiente eseguito distinto dalla versione documentata;
- [x] codice invariato dalle revisioni editoriali e visuali;
- [x] nessuna nuova esecuzione dichiarata per le sole modifiche testuali o visuali.

## Elementi aperti

- approvazione autoriale di `ATT-01/candidate-v3.png`;
- conferma autoriale di `ATT-02/candidate-v2.png`;
- rinomina in `final.png` soltanto dopo approvazione;
- nuovo congelamento del Capitolo 28 prima dell'aggiornamento di `main`.

## Esito

La candidatura `0.6.0-rc6` supera i gate fattuali, matematici, didattici, anti-template, editoriali, linguistici, di accessibilità e di coerenza visuale. Il capitolo è pronto per la revisione autoriale completa.
