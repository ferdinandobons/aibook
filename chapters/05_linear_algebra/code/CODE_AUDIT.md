# Audit del codice. Capitolo 5

## Stato

- Snippet: `SNIP-LA-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu
- Esito: **superato**
- Test: 4/4 superati

## Controlli

- [x] `X` ha shape `[3,4]`.
- [x] `W` ha shape `[3,4]`; `W.T` ha shape `[4,3]`.
- [x] La contrazione dell'asse feature produce `[3,3]`.
- [x] Il bias `[3]` coincide con l'espansione esplicita `[3,3]`.
- [x] I valori degli score corrispondono ai calcoli manuali.
- [x] `XX^T` è simmetrica e contiene i prodotti scalari tra righe.
- [x] La matrice di esempio ha rango numerico 2.
- [x] Il terzo valore singolare è inferiore a `1e-12`.
- [x] La ricostruzione SVD coincide con la matrice entro `rtol=atol=1e-12`.
- [x] Output e ambiente sono registrati.

## Limiti

- matrici piccole e dense;
- CPU e float64;
- nessun benchmark prestazionale;
- nessuna analisi dei gradienti della SVD;
- tolleranza adatta soltanto all'esempio dichiarato.

## Verdetto

Il codice rende osservabili i contratti matematici del capitolo senza introdurre un percorso concettuale separato.
