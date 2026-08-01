# Guida alla revisione. Capitolo 4

## Versione

- Capitolo: `CH-P01-CRITICAL-EVALUATION`
- Titolo: Come valutare criticamente un risultato di AI
- Versione: `0.2.0-rc1`
- Stato: candidatura completa in revisione autoriale

## Percorso consigliato

1. `CHAPTER.md`;
2. `assets/chapters/04_critical_evaluation/EVAL-01/candidate-v1.png`;
3. `assets/chapters/04_critical_evaluation/EVAL-02/candidate-v1.png`;
4. `TEXT_AUDIT.md`;
5. `CLAIMS.md` e `FONTI_PRIMARIE.md`;
6. `code/`, con output e quattro test.

## Aspetti da valutare

- L'apertura rende chiaro perché una differenza di accuratezza non è ancora una decisione?
- Baseline, slice, costo e variabilità si distinguono senza frammentare il discorso?
- La spiegazione del bootstrap è comprensibile anche senza eseguire il codice?
- Il testo evita sia lo scetticismo generico sia l'accettazione automatica del benchmark?
- Leakage, riuso del test set e contaminazione di pretraining risultano distinti?
- Ablation e shortcut learning sono trattati con il giusto livello di prudenza?
- Le visuali chiariscono il percorso e il trade-off senza suggerire una scelta universale tra A e B?

## Decisioni richieste

- [ ] Approvo la voce editoriale.
- [ ] Approvo il livello statistico.
- [ ] Approvo lo snippet e i dati illustrativi.
- [ ] Approvo `EVAL-01`.
- [ ] Approvo `EVAL-02`.
- [ ] Autorizzo il congelamento dopo le eventuali correzioni.
