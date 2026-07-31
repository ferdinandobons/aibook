# Fonti primarie e autorevoli. Capitolo 12

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: apprendimento supervisionato, logistic regression, generalizzazione, regolarizzazione, metriche, modelli ad albero, margini, ensemble e API PyTorch
- Ambiente eseguito: Python 3.13.5, PyTorch 2.10.0+cpu
- Documentazione API consultata: PyTorch stable 2.13

## SRC-SUP-001. Cox, regressione di sequenze binarie

D. R. Cox, *The Regression Analysis of Binary Sequences*, Journal of the Royal Statistical Society, Series B, 20(2), 215-232, 1958. DOI: https://doi.org/10.1111/j.2517-6161.1958.tb00292.x

Uso: riferimento storico per modelli di probabilità binaria dipendenti da variabili esplicative.

Limite: il capitolo usa una formulazione moderna della logistic regression e non attribuisce al paper l'intera storia del metodo.

## SRC-SUP-002. Deep Learning

Ian Goodfellow, Yoshua Bengio e Aaron Courville, *Deep Learning*, MIT Press, 2016, capitoli 5 e 7. Sito ufficiale: https://www.deeplearningbook.org/

Uso: rischio empirico, generalizzazione, capacità, regolarizzazione, training, validation e test.

Limite: le garanzie statistiche avanzate e i bound di generalizzazione sono differiti.

## SRC-SUP-003. The Elements of Statistical Learning

Trevor Hastie, Robert Tibshirani e Jerome Friedman, *The Elements of Statistical Learning*, seconda edizione, Springer, 2009. Pagina ufficiale: https://hastie.su.domains/ElemStatLearn/

Uso: classificazione, regressione, logistic regression, alberi, support-vector machine, ensemble, bias-varianza e selezione del modello.

Limite: il capitolo non replica benchmark o ricette specifiche del volume.

## SRC-SUP-004. Pattern Recognition and Machine Learning

Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006.

Uso: decision theory, classificazione probabilistica, logistic regression, regolarizzazione e valutazione.

Limite: inferenza bayesiana completa e modelli a variabili latenti sono trattati altrove.

## SRC-SUP-005. Bias e varianza

Stuart Geman, Elie Bienenstock e René Doursat, *Neural Networks and the Bias/Variance Dilemma*, Neural Computation 4(1), 1-58, 1992. DOI: https://doi.org/10.1162/neco.1992.4.1.1

Uso: prospettiva statistica su bias, varianza, rumore e reti neurali.

Limite: la decomposizione quadratica non viene trasferita automaticamente a ogni loss di classificazione.

## SRC-SUP-006. Support-vector network

Corinna Cortes e Vladimir Vapnik, *Support-Vector Networks*, Machine Learning 20, 273-297, 1995. DOI: https://doi.org/10.1007/BF00994018

Uso: margine, feature space, caso non separabile e slack.

Limite: il capitolo cita il contratto generale e non sviluppa duale, kernel trick o ottimizzazione completa.

## SRC-SUP-007. Random Forests

Leo Breiman, *Random Forests*, Machine Learning 45, 5-32, 2001. DOI: https://doi.org/10.1023/A:1010933404324

Uso: foreste di alberi, casualità, forza dei predittori e correlazione.

Limite: nessun confronto prestazionale del paper viene trasferito al dataset sintetico del capitolo.

## SRC-SUP-008. Gradient boosting

Jerome H. Friedman, *Greedy Function Approximation: A Gradient Boosting Machine*, The Annals of Statistics 29(5), 1189-1232, 2001. DOI: https://doi.org/10.1214/aos/1013203451

Uso: espansioni additive, discesa nello spazio delle funzioni e boosting con alberi.

Limite: il capitolo non implementa gradient boosting e non confronta ensemble con la logistic regression illustrativa.

## SRC-SUP-009. Early stopping

Lutz Prechelt, *Early Stopping. But When?*, in *Neural Networks: Tricks of the Trade*, LNCS 1524, 55-69, 1998. DOI: https://doi.org/10.1007/3-540-49430-8_3

Uso: criteri di arresto, compromesso tra tempo e generalizzazione e uso della validation.

Limite: nessun criterio del paper viene presentato come universalmente migliore.

## SRC-SUP-010. Precision-recall e ROC

Jesse Davis e Mark Goadrich, *The Relationship Between Precision-Recall and ROC Curves*, ICML 2006, 233-240. DOI: https://doi.org/10.1145/1143844.1143874

Uso: relazione tra spazi ROC e PR e rilevanza delle curve precision-recall nei dataset sbilanciati.

Limite: il capitolo usa un solo punto operativo e non costruisce curve complete.

## SRC-SUP-011. PyTorch BCEWithLogitsLoss

Documentazione ufficiale PyTorch stable 2.13, `torch.nn.BCEWithLogitsLoss`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html

Uso: input come logits, combinazione numericamente stabile con la binary cross-entropy, `weight`, `pos_weight` e riduzioni.

Limite: codice eseguito con PyTorch 2.10.0+cpu; la documentazione stable è stata controllata separatamente.

## SRC-SUP-012. PyTorch CrossEntropyLoss

Documentazione ufficiale PyTorch stable 2.13, `torch.nn.CrossEntropyLoss`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html

Uso: distinzione tra classificazione binaria e multiclasse, logits, target come indici o probabilità e class weight.

Limite: lo snippet principale è binario e usa `binary_cross_entropy_with_logits`.

## SRC-SUP-013. PyTorch Linear

Documentazione ufficiale PyTorch stable 2.13, `torch.nn.Linear`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html

Uso: trasformazione affine, shape di input e output e parametri del modello illustrativo.

## SRC-SUP-014. PyTorch Adam

Documentazione ufficiale PyTorch stable 2.13, `torch.optim.Adam`. URL: https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam.html

Uso: contratto dell'optimizer usato nello snippet.

Limite: il run non confronta optimizer e non sostiene la superiorità di Adam.

## Regola d'uso

- Le definizioni generali derivano dai testi accademici e dai paper primari.
- Le proprietà delle famiglie di modelli sono limitate ai rispettivi lavori.
- Le API vengono attribuite alla documentazione ufficiale PyTorch.
- I numeri del capitolo derivano esclusivamente da `SNIP-SUP-001` e dai suoi test.
- Il dataset è sintetico e non sostiene claim su utenti, organizzazioni o sistemi reali.
