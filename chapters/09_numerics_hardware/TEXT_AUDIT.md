# Audit del testo. Capitolo 9

## Stato

- Versione corrente: `0.1.0-draft1`
- Data: 31 luglio 2026
- Esito fattuale: **superato per il testo corrente**
- Esito matematico e numerico: **superato**
- Esito del codice: **superato, sette test**
- Esito didattico: **superato dopo seconda lettura**
- Esito editoriale e linguistico: **superato per la bozza**
- Visuali: tecnicamente validate localmente, PNG da materializzare nel branch
- Review autoriale: non aperta

## Review 1. Accuratezza tecnica

Controlli:

- [x] floating point descritto come insieme finito di valori;
- [x] segno, esponente e significando distinti;
- [x] `eps`, `tiny` e `max` usati con il significato della documentazione;
- [x] valori dei quattro dtype allineati a `torch.finfo`;
- [x] non associatività presentata come proprietà generale, con esempio eseguito separato;
- [x] cancellazione distinta dal semplice arrotondamento;
- [x] condizionamento distinto dalla stabilità dell'algoritmo;
- [x] overflow intermedio distinto da risultato matematico finale;
- [x] logsumexp stabilizzato spiegato attraverso la sottrazione del massimo;
- [x] fp16 e bfloat16 confrontati per range e precisione, non per qualità assoluta;
- [x] storage, calcolo, accumulo e output separati;
- [x] autocast e GradScaler distinti;
- [x] TF32 descritto con condizioni di hardware e backend;
- [x] Roofline usato come modello concettuale, non come benchmark;
- [x] determinismo, riproducibilità e identità bitwise distinti.

## Review 2. Lettore non esperto

Domande simulate:

1. Il lettore capisce perché il computer non conserva ogni numero reale?
2. Sa distinguere un numero grande rappresentabile da un numero rappresentato con molte cifre precise?
3. Comprende la non associatività prima di incontrare il termine?
4. Capisce perché `logsumexp` stabile evita l'overflow?
5. Sa spiegare la differenza tra float16 e bfloat16 senza memorizzare soltanto i nomi?
6. Distingue autocast da loss scaling?
7. Comprende perché meno byte non equivalgono automaticamente a più velocità?

Esito: positivo. Il problema concreto precede la terminologia e le formule avanzate non reggono da sole la spiegazione.

## Review 3. Voce editoriale

Correzioni applicate durante la stesura:

- eliminata una struttura a glossario dei dtype;
- riunite range e precisione in un confronto causale;
- spostate le API dopo il meccanismo;
- evitato di presentare float32 come riferimento universale;
- ridotti caveat ripetuti e raccolti nei confini delle sezioni;
- mantenuti periodi completi attorno a formule e codice;
- evitati calchi come `compute-bound` e `memory-bound` nel percorso principale;
- sostituiti con limite di calcolo e limite di bandwidth, introducendo il termine inglese soltanto dove utile.

## Review 4. Controllo incrociato

- [x] valori del testo presenti in `SNIP-NUM-001.txt`;
- [x] sette test coerenti con i claim;
- [x] dimensioni di storage derivate da shape ed element size;
- [x] autocast esplicitamente CPU bfloat16;
- [x] nessun risultato GPU dichiarato come eseguito;
- [x] valori di `NUM-01` coerenti con la tabella;
- [x] flusso di `NUM-02` coerente con la sezione mixed precision;
- [x] fonti associate ai claim portanti.

## Difetti visuali trovati e corretti

- lo strumento immagini ha prodotto una dashboard estranea e falsa: respinta;
- nel renderer raster v1 di `NUM-01`, i segmenti oltrepassavano le schede: corretti;
- nel renderer raster v1 di `NUM-02`, il loop dell'optimizer era ambiguo: aggiunte le label `gradienti` e `pesi aggiornati`.

## Elementi aperti

- materializzare `NUM-01/candidate-v1.png` e `NUM-02/candidate-v1.png` nel feature branch;
- inserire i due riferimenti al posto dei commenti nel capitolo;
- rileggere il capitolo con le figure nel flusso;
- aprire la revisione autoriale;
- promuovere la versione soltanto dopo controllo del raster pubblicato.

## Verdetto

Testo, fonti, claim e codice sono pronti per il controllo finale con le immagini. Il capitolo non è ancora una candidatura completa perché i PNG revisionati non sono materializzati nel repository.
