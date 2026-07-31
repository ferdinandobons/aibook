# Fonti primarie e autorevoli. Capitolo 7

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: probabilità, variabili aleatorie, momenti, condizionamento, Bayes, campionamento, likelihood e inferenza

## SRC-PROB-001. Introduction to Probability

Joseph K. Blitzstein e Jessica Hwang, *Introduction to Probability*, seconda edizione, Chapman & Hall/CRC, 2019. Pagina ufficiale del corso Harvard Statistics 110: https://stat110.hsites.harvard.edu/

Uso: eventi, probabilità condizionata, legge totale, Bayes, indipendenza, variabili aleatorie, aspettativa, varianza e teoremi limite.

Limite: la statistica inferenziale e le API vengono verificate su fonti separate.

## SRC-PROB-002. Probabilistic Machine Learning: An Introduction

Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press, 2022. Sito ufficiale: https://probml.github.io/pml-book/book1.html

Uso: distribuzioni, modelli probabilistici, likelihood, MLE, inferenza bayesiana e collegamenti al machine learning.

Limite: gli argomenti avanzati di inferenza approssimata sono differiti.

## SRC-PROB-003. All of Statistics

Larry Wasserman, *All of Statistics: A Concise Course in Statistical Inference*, Springer, 2004.

Uso: popolazione, campione, statistica, stimatore, likelihood, consistenza, legge dei grandi numeri, teorema centrale del limite e intervalli.

Limite: le dimostrazioni complete dei risultati asintotici non sono incluse nel capitolo.

## SRC-PROB-004. Statistical Inference

George Casella e Roger L. Berger, *Statistical Inference*, seconda edizione, Duxbury, 2002.

Uso: modelli statistici, sufficienza, stima, massima verosimiglianza e interpretazione frequentista.

Limite: teoria decisionale e risultati avanzati sono differiti.

## SRC-PROB-005. Introduction to Modern Statistics

Mine Çetinkaya-Rundel e Johanna Hardin, *Introduction to Modern Statistics*, seconda edizione, OpenIntro, versione 31 marzo 2026. URL ufficiale: https://openintro.org/book/ims/online/

Uso: campionamento, variabilità, distribuzioni campionarie, intervalli e inferenza basata su simulazione.

Limite: il capitolo non riproduce procedure software o dataset del libro.

## SRC-PROB-006. NIST/SEMATECH e-Handbook

NIST/SEMATECH, *e-Handbook of Statistical Methods*. URL: https://www.itl.nist.gov/div898/handbook/

Uso: ruolo delle distribuzioni nei modelli statistici, assunzioni, stima dei parametri e maximum likelihood.

Limite: le procedure applicative dipendono dal modello e dal protocollo dichiarato.

## SRC-PROB-007. Kolmogorov

A. N. Kolmogorov, *Foundations of the Theory of Probability*, 1933; traduzione inglese Chelsea, 1950.

Uso: fondazione assiomatica della probabilità.

Limite: il capitolo usa una presentazione didattica moderna e non ricostruisce la teoria della misura.

## SRC-PROB-008. PyTorch distributions

Documentazione ufficiale PyTorch stable 2.13, `torch.distributions`. URL: https://docs.pytorch.org/docs/stable/distributions.html

Uso: `Bernoulli`, parametri `probs` e `logits`, `sample`, `log_prob`, media e varianza.

Limite: il codice è stato eseguito con PyTorch `2.10.0+cpu`; la documentazione stable è stata controllata separatamente.

## SRC-PROB-009. Deep Learning

Ian Goodfellow, Yoshua Bengio e Aaron Courville, *Deep Learning*, MIT Press, 2016, capitolo 3. URL ufficiale: https://www.deeplearningbook.org/

Uso: probabilità e teoria dell'informazione come linguaggio dei modelli di deep learning.

Limite: entropia, cross-entropy e funzioni obiettivo sono sviluppate nel Capitolo 8.

## SRC-PROB-010. Maximum likelihood estimation, NIST

NIST/SEMATECH e-Handbook, sezione *Maximum likelihood estimation*. URL: https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm

Uso: definizione operativa della likelihood del campione e dei valori che la massimizzano.

Limite: le proprietà asintotiche richiedono condizioni e non vengono generalizzate senza specificarle.

## Regola d'uso

- Le definizioni matematiche sono sostenute dai testi accademici indicati.
- I valori del caso di Bayes e delle simulazioni derivano da `SNIP-PROB-001`.
- Le API sono attribuite alla documentazione ufficiale PyTorch.
- Il capitolo non presenta una interpretazione filosofica unica della probabilità come fatto universale.
