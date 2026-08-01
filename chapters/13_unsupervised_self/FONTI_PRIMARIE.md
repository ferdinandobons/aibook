# Fonti primarie e autorevoli. Capitolo 13

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: clustering, rappresentazioni, autoencoder, masked modeling, contrastive learning, pseudo-label e API PyTorch
- Ambiente eseguito: Python 3.13.5, PyTorch 2.10.0+cpu
- Documentazione API consultata: PyTorch stable 2.12/2.13 disponibile il 31 luglio 2026

## SRC-UNSUP-001. MacQueen e k-means

J. B. MacQueen, *Some Methods for Classification and Analysis of Multivariate Observations*, Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1, 281-297, 1967. Archivio University of California: https://digicoll.lib.berkeley.edu/record/113015

Uso: riferimento storico per procedure di classificazione iterativa e centroidi.

Limite: il capitolo usa una variante batch didattica con inizializzazione propria; non attribuisce ogni implementazione moderna al medesimo pseudocodice.

## SRC-UNSUP-002. Deep Learning

Ian Goodfellow, Yoshua Bengio e Aaron Courville, *Deep Learning*, MIT Press, 2016, capitoli 14 e 20. Sito ufficiale: https://www.deeplearningbook.org/

Uso: representation learning, autoencoder, obiettivi non supervisionati e relazioni con il pretraining.

Limite: le famiglie generative complete sono differite alla Parte P05.

## SRC-UNSUP-003. Riduzione della dimensionalità con reti neurali

Geoffrey E. Hinton e Ruslan R. Salakhutdinov, *Reducing the Dimensionality of Data with Neural Networks*, Science 313(5786), 504-507, 2006. DOI: https://doi.org/10.1126/science.1127647

Uso: codifica a bassa dimensione e ricostruzione attraverso reti profonde.

Limite: il capitolo non replica architettura, training layer-wise o risultati del paper.

## SRC-UNSUP-004. Denoising autoencoder

Pascal Vincent, Hugo Larochelle, Yoshua Bengio e Pierre-Antoine Manzagol, *Extracting and Composing Robust Features with Denoising Autoencoders*, ICML 2008, 1096-1103. DOI: https://doi.org/10.1145/1390156.1390294

Uso: corruzione dell'input e ricostruzione dell'originale come obiettivo di rappresentazione.

Limite: il masked autoencoder numerico del capitolo non replica il setup di immagini del paper.

## SRC-UNSUP-005. Contrastive Predictive Coding

Aaron van den Oord, Yazhe Li e Oriol Vinyals, *Representation Learning with Contrastive Predictive Coding*, arXiv:1807.03748, 2018. URL ufficiale: https://arxiv.org/abs/1807.03748

Uso: predizione in spazio latente, contesto, loss contrastiva e campioni negativi.

Limite: il capitolo presenta una formula semplificata e non implementa CPC.

## SRC-UNSUP-006. BERT

Jacob Devlin, Ming-Wei Chang, Kenton Lee e Kristina Toutanova, *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*, NAACL-HLT 2019, 4171-4186. ACL Anthology: https://aclanthology.org/N19-1423/

Uso: masked language modeling, pretraining su testo senza label downstream e fine-tuning.

Limite: il capitolo non tratta l'architettura Transformer o il setup completo di BERT.

## SRC-UNSUP-007. DeepCluster

Mathilde Caron, Piotr Bojanowski, Armand Joulin e Matthijs Douze, *Deep Clustering for Unsupervised Learning of Visual Features*, ECCV 2018, 132-149. CVF Open Access: https://openaccess.thecvf.com/content_ECCV_2018/html/Mathilde_Caron_Deep_Clustering_for_ECCV_2018_paper.html

Uso: alternanza tra clustering delle feature e pseudo-label per aggiornare una rete.

Limite: nessun risultato ImageNet viene trasferito al toy example.

## SRC-UNSUP-008. SimCLR

Ting Chen, Simon Kornblith, Mohammad Norouzi e Geoffrey Hinton, *A Simple Framework for Contrastive Learning of Visual Representations*, ICML 2020, PMLR 119, 1597-1607. URL: https://proceedings.mlr.press/v119/chen20j.html

Uso: viste augmentate, coppie positive, temperatura, proiezione, linear evaluation e ruolo delle augmentazioni.

Limite: il capitolo non implementa la loss completa né confronta batch size.

## SRC-UNSUP-009. Masked Autoencoders

Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár e Ross Girshick, *Masked Autoencoders Are Scalable Vision Learners*, CVPR 2022, 16000-16009. CVF Open Access: https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html

Uso: mascheramento di patch, encoder sui token visibili, decoder leggero e ricostruzione dei pixel.

Limite: il toy model del capitolo usa vettori di quattro coordinate e una architettura differente.

## SRC-UNSUP-010. PyTorch MSELoss

Documentazione ufficiale PyTorch stable, `torch.nn.MSELoss`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html

Uso: errore quadratico e riduzioni.

## SRC-UNSUP-011. PyTorch Linear

Documentazione ufficiale PyTorch, `torch.nn.Linear` e `torch.nn.functional.linear`. URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html e https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.linear.html

Uso: shape e trasformazioni affini dell'encoder e decoder.

## SRC-UNSUP-012. PyTorch cdist

Documentazione ufficiale PyTorch stable, `torch.cdist`. URL: https://docs.pytorch.org/docs/stable/generated/torch.cdist.html

Uso: distanze a coppie tra esempi e centroidi.

## Regola d'uso

- Le definizioni generali sono sostenute da testi e paper primari.
- La distinzione terminologica tra non supervisionato e auto-supervisionato è dichiarata come convenzione del libro.
- I lavori citati vengono usati per il proprio meccanismo, non per costruire una classifica storica.
- I numeri illustrativi derivano soltanto da `SNIP-UNSUP-001`.
- Le label segrete del generatore non entrano nel training.
