# Guida alla revisione. Capitolo 5

## Versione

- Capitolo: `CH-P02-LINEAR-ALGEBRA`
- Titolo: Algebra lineare, vettori e tensori
- Versione: `0.2.0-rc1`
- Stato: candidatura completa in revisione autoriale

## Percorso consigliato

1. `CHAPTER.md`;
2. `assets/chapters/05_linear_algebra/LA-01/candidate-v1.png`;
3. `assets/chapters/05_linear_algebra/LA-02/candidate-v1.png`;
4. `TEXT_AUDIT.md`;
5. `CLAIMS.md` e `FONTI_PRIMARIE.md`;
6. `code/`, con output e quattro test.

## Aspetti da valutare

- La distinzione tra shape e significato degli assi è abbastanza chiara?
- Prodotto elemento per elemento, prodotto scalare e prodotto matriciale restano distinguibili?
- La lettura di `XW^T+b` è comprensibile prima della formula generale?
- Broadcasting e batch vengono spiegati senza anticipare troppi dettagli di implementazione?
- Span, indipendenza, rango e SVD formano una progressione naturale?
- La sezione su stride e contiguità è utile senza spostare il centro del capitolo?
- Le visuali riportano correttamente valori, shape e confini?

## Decisioni richieste

- [ ] Approvo la voce editoriale.
- [ ] Approvo la profondità matematica.
- [ ] Approvo lo snippet e il livello di dettaglio PyTorch.
- [ ] Approvo `LA-01`.
- [ ] Approvo `LA-02`.
- [ ] Autorizzo il congelamento dopo le eventuali correzioni.
