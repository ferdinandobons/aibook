# Guida alla revisione. Capitolo 9

## Stato

- `chapter_id`: `CH-P02-NUMERICS-HARDWARE`
- Versione: `0.1.0-draft1`
- Testo: review tecnica, didattica, editoriale e linguistica superate internamente
- Codice: sette test superati
- Visuali: `NUM-01` e `NUM-02` materializzate e validate tecnicamente
- Review autoriale: aperta

## Percorso consigliato

1. `CHAPTER.md`, per chiarezza e profondità;
2. `CLAIMS.md`, per la mappa frase-prova;
3. `FONTI_PRIMARIE.md`, per fonti e limiti;
4. `code/`, per snippet, output e test;
5. `assets/.../NUM-01/`, per range e precisione;
6. `assets/.../NUM-02/`, per mixed precision;
7. `TEXT_AUDIT.md`, per le review interne.

## Aspetti da valutare

- La differenza tra range e precisione è chiara prima della tabella?
- L'esempio di non associatività si comprende senza conoscere IEEE 754?
- La sezione su cancellazione, condizionamento e stabilità resta leggibile?
- La motivazione di logsumexp stabile è concreta?
- Float16 e bfloat16 sono presentati senza una gerarchia falsa?
- Storage, calcolo, accumulo e output sono distinti?
- Autocast e loss scaling risultano separati?
- Le condizioni hardware impediscono promesse di prestazione non misurate?
- La parte su Roofline aggiunge comprensione senza trasformarsi in un capitolo di benchmarking?
- Determinismo e riproducibilità sono distinti in modo operativo?
- L'italiano è fluido anche nei passaggi più tecnici?

## Prova di comprensione semplificata

Il lettore dovrebbe poter dire, senza formule:

1. il computer conserva soltanto alcuni valori;
2. più range e più precisione non sono la stessa cosa;
3. cambiare l'ordine delle operazioni può cambiare l'arrotondamento;
4. una formula stabile evita intermedi inutilmente estremi;
5. mixed precision assegna precisioni diverse a operazioni diverse;
6. l'hardware accelera soltanto se kernel, dati e collo di bottiglia lo permettono;
7. stesso seed non significa automaticamente stessi bit ovunque.

## Elementi aperti

- [x] materializzazione di `NUM-01`;
- [x] materializzazione di `NUM-02`;
- [x] controllo incrociato sul raster locale;
- [x] sostituzione dei commenti nel capitolo con le immagini;
- [ ] rilettura nel flusso impaginato;
- [ ] revisione autoriale completa;
- [ ] congelamento.
