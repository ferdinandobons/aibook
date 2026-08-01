# Fonti primarie. Capitolo 5

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: vettori, matrici, tensori, trasformazioni lineari, rango, SVD e semantica PyTorch

## `SRC-LA-001`. Deep Learning, Capitolo 2

- Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning*, MIT Press, 2016, capitolo 2.
- URL ufficiale: https://www.deeplearningbook.org/
- Uso: scalari, vettori, matrici, tensori, prodotti, norme, decomposizioni e algebra lineare per il machine learning.
- Limite: usa convenzioni matematiche generali; shape e semantica API vengono verificate separatamente.

## `SRC-LA-002`. Introduction to Linear Algebra

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press, quinta edizione, 2016.
- Materiali ufficiali MIT OCW: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Uso: spazio delle colonne, indipendenza, rango, basi, autovalori e SVD.
- Limite: il capitolo non riproduce dimostrazioni complete del corso.

## `SRC-LA-003`. Matrix Computations

- Gene H. Golub, Charles F. Van Loan, *Matrix Computations*, quarta edizione, Johns Hopkins University Press, 2013.
- Uso: decomposizioni, rango numerico e metodi computazionali.
- Limite: gli algoritmi numerici dettagliati sono differiti al Capitolo 9.

## `SRC-LA-004`. LAPACK Users' Guide

- E. Anderson et al., *LAPACK Users' Guide*, terza edizione, SIAM, 1999.
- URL ufficiale: https://www.netlib.org/lapack/lug/
- Uso: decomposizioni e soluzione numerica dei problemi di algebra lineare densa.
- Limite: interfacce Fortran e dettagli algoritmici non coincidono con l'API PyTorch.

## `SRC-LA-005`. BLAS

- Netlib, Basic Linear Algebra Subprograms.
- URL ufficiale: https://www.netlib.org/blas/
- Uso: distinzione tra operazioni vettoriali, matrice-vettore e matrice-matrice come nuclei computazionali.
- Limite: non viene usato per attribuire una specifica implementazione interna a ogni backend PyTorch.

## `SRC-LA-006`. PyTorch `torch.matmul`

- Documentazione ufficiale PyTorch stable, `torch.matmul`.
- URL: https://docs.pytorch.org/docs/stable/generated/torch.matmul.html
- Uso: comportamento con vettori, matrici e batch; broadcasting delle dimensioni batch.
- Limite: la versione effettivamente eseguita viene registrata separatamente dalla documentazione stable consultata.

## `SRC-LA-007`. PyTorch broadcasting

- Documentazione ufficiale PyTorch, *Broadcasting semantics*.
- URL: https://docs.pytorch.org/docs/stable/notes/broadcasting.html
- Uso: compatibilità delle dimensioni finali e espansione logica senza copie obbligatorie.
- Limite: non tutte le operazioni supportano broadcasting; il capitolo lo usa soltanto per operatori documentati.

## `SRC-LA-008`. PyTorch linear algebra

- Documentazione ufficiale PyTorch, `torch.linalg`.
- URL: https://docs.pytorch.org/docs/stable/linalg
- Uso: norme, rango numerico e decomposizioni.
- Limite: tolleranze e backend possono influire sul rango numerico e sui risultati in precisione finita.

## `SRC-LA-009`. PyTorch SVD

- Documentazione ufficiale PyTorch, `torch.linalg.svd`.
- URL: https://docs.pytorch.org/docs/stable/generated/torch.linalg.svd.html
- Uso: definizione di SVD completa e ridotta, shape di `U`, `S`, `Vh`, ordine dei valori singolari.
- Limite: segni e basi nei sottospazi degeneri non sono unici; le derivate possono essere instabili in casi documentati.

## `SRC-LA-010`. PyTorch tensor views

- Documentazione ufficiale PyTorch, *Tensor Views*.
- URL: https://docs.pytorch.org/docs/stable/tensor_view.html
- Uso: differenza tra dati, shape, stride, view e contiguità.
- Limite: proprietà di storage e layout appartengono all'implementazione, non alla definizione matematica astratta.

## `SRC-LA-011`. PyTorch `einsum`

- Documentazione ufficiale PyTorch, `torch.einsum`.
- URL: https://docs.pytorch.org/docs/stable/generated/torch.einsum.html
- Uso: notazione compatta per prodotti e contrazioni di assi.
- Limite: il capitolo usa `einsum` come lettura alternativa, non come requisito per comprendere il prodotto matriciale.

## Regola d'uso

Le identità matematiche vengono derivate esplicitamente. I valori numerici del capitolo derivano da `SNIP-LA-001`; non vengono attribuiti alle fonti bibliografiche.
