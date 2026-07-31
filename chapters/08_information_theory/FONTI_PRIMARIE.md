# Fonti primarie e autorevoli. Capitolo 8

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: informazione, entropia, KL, likelihood, cross-entropy e funzioni obiettivo

## SRC-INFO-001. Shannon 1948

Claude E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal, 1948.

Uso: informazione, entropia e proprietà della misura logaritmica.

Limite: il capitolo non ricostruisce codifica, capacità di canale e teoria completa della comunicazione.

## SRC-INFO-002. Elements of Information Theory

Thomas M. Cover e Joy A. Thomas, *Elements of Information Theory*, seconda edizione, Wiley, 2006.

Uso: entropia, entropia condizionata, mutua informazione, cross-entropy, KL divergence e disuguaglianza di Gibbs.

Limite: dimostrazioni e teoremi di codifica sono differiti.

## SRC-INFO-003. Information Theory, Inference, and Learning Algorithms

David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*, Cambridge University Press, 2003. Sito ufficiale: https://www.inference.org.uk/mackay/itila/

Uso: collegamenti tra informazione, inferenza, codifica e apprendimento.

Limite: algoritmi bayesiani avanzati non vengono sviluppati nel capitolo.

## SRC-INFO-004. Deep Learning

Ian Goodfellow, Yoshua Bengio e Aaron Courville, *Deep Learning*, MIT Press, 2016, capitoli 3 e 5. URL ufficiale: https://www.deeplearningbook.org/

Uso: self-information, entropia, KL, cross-entropy, maximum likelihood e funzioni obiettivo nel deep learning.

Limite: ottimizzazione e regolarizzazione avanzata sono trattate nei capitoli successivi.

## SRC-INFO-005. Probabilistic Machine Learning

Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press, 2022. URL ufficiale: https://probml.github.io/pml-book/book1.html

Uso: log-likelihood, discriminative classification, softmax, loss e probabilistic modeling.

## SRC-INFO-006. Proper scoring rules

Tilmann Gneiting e Adrian E. Raftery, *Strictly Proper Scoring Rules, Prediction, and Estimation*, Journal of the American Statistical Association, 2007.

Uso: log score e interpretazione delle loss probabilistiche come scoring rule.

Limite: teoria generale delle scoring rule differita.

## SRC-INFO-007. PyTorch CrossEntropyLoss

Documentazione ufficiale PyTorch stable 2.13, `torch.nn.CrossEntropyLoss`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html

Uso: logits attesi, target come indici o probabilità, equivalenza `LogSoftmax + NLLLoss`, riduzioni e label smoothing.

Limite: codice eseguito con PyTorch `2.10.0+cpu`.

## SRC-INFO-008. PyTorch log_softmax e NLLLoss

Documentazione ufficiale PyTorch stable 2.13:

- https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.log_softmax.html
- https://docs.pytorch.org/docs/stable/generated/torch.nn.NLLLoss.html

Uso: stabilità numerica e contratto delle log-probabilità.

## SRC-INFO-009. PyTorch KLDivLoss

Documentazione ufficiale PyTorch stable 2.13, `torch.nn.KLDivLoss` e `torch.nn.functional.kl_div`.

Uso: input in log-probabilità, `log_target`, riduzioni e differenza tra `mean` e `batchmean`.

## SRC-INFO-010. PyTorch MSELoss e L1Loss

Documentazione ufficiale PyTorch stable 2.13 per `MSELoss` e `L1Loss`.

Uso: contratti implementativi delle loss di regressione.

## Regola d'uso

- Le definizioni informative derivano da Shannon e dai testi di teoria dell'informazione.
- Le relazioni con likelihood e machine learning sono controllate su Goodfellow e Murphy.
- Le API vengono attribuite alla documentazione PyTorch.
- I valori numerici derivano da `SNIP-INFO-001`.
- L'entropia non viene interpretata come comprensione, verità o significato semantico.
