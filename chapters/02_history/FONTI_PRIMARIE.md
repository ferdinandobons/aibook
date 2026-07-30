# Fonti primarie. Capitolo 2

## Stato

- Capitolo: `CH-P01-HISTORY`
- Ultima verifica: 30 luglio 2026
- Criterio: paper originali, atti ufficiali, riviste, archivi degli autori e documentazione istituzionale
- Funzione: sostenere date, formulazioni, meccanismi e limiti della periodizzazione

## Fonti

### `SRC-HIST-001`. Turing, 1950

- A. M. Turing, *Computing Machinery and Intelligence*, Mind, 59(236), 433-460, 1950.
- DOI: `10.1093/mind/LIX.236.433`.
- Fonte: Oxford Academic, fascicolo originale.
- Sostiene: formulazione dell'imitation game e discussione della domanda sulle macchine e il pensiero.
- Limite: il paper precede il termine `artificial intelligence` e non definisce il campo moderno.

### `SRC-HIST-002`. Proposta di Dartmouth, 1955

- J. McCarthy, M. Minsky, N. Rochester, C. E. Shannon, *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 31 agosto 1955.
- Riproduzione: AI Magazine 27(4), 2006, DOI `10.1609/aimag.v27i4.1904`.
- Versione HTML nell'archivio di John McCarthy: `www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html`.
- Sostiene: uso esplicito dell'espressione `artificial intelligence`, programma della ricerca estiva del 1956 e problemi proposti.
- Limite: la proposta non prova che il campo abbia una sola data di nascita né che gli obiettivi siano stati raggiunti nell'estate del 1956.

### `SRC-HIST-003`. Rosenblatt, 1958

- F. Rosenblatt, *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*, Psychological Review 65(6), 386-408, 1958.
- DOI: `10.1037/h0042519`.
- Sostiene: formulazione del perceptron come modello di apprendimento.
- Limite: non rappresenta tutte le reti neurali successive e non deve essere descritto con proprietà introdotte molto più tardi.

### `SRC-HIST-004`. Newell e Simon, 1976

- A. Newell, H. A. Simon, *Computer Science as Empirical Inquiry: Symbols and Search*, Communications of the ACM 19(3), 113-126, 1976.
- Fonte archivistica: Computer History Museum e ACM.
- Sostiene: centralità di simboli e ricerca e formulazione della physical symbol system hypothesis.
- Limite: è una tesi programmatica degli autori, non un fatto universale su ogni forma di intelligenza.

### `SRC-HIST-005`. MYCIN, 1984

- B. G. Buchanan, E. H. Shortliffe, a cura di, *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*, Addison-Wesley, 1984.
- Edizione elettronica messa a disposizione dagli autori: `people.dbmi.columbia.edu/~ehs7001/Buchanan-Shortliffe-1984/MYCIN Book.htm`.
- Sostiene: struttura dei sistemi rule-based, knowledge engineering e analisi retrospettiva degli esperimenti MYCIN.
- Limite: MYCIN è uno studio di caso medico e non rappresenta ogni sistema esperto.

### `SRC-HIST-006`. Backpropagation, 1986

- D. E. Rumelhart, G. E. Hinton, R. J. Williams, *Learning Representations by Back-Propagating Errors*, Nature 323, 533-536, 1986.
- DOI: `10.1038/323533a0`.
- Sostiene: procedura di aggiustamento dei pesi per ridurre l'errore e apprendimento di rappresentazioni nelle unità nascoste.
- Limite: il paper non è l'unica origine storica della differenziazione automatica o della backpropagation.

### `SRC-HIST-007`. Support vector network, 1995

- C. Cortes, V. Vapnik, *Support-Vector Networks*, Machine Learning 20, 273-297, 1995.
- DOI: `10.1007/BF00994018`.
- Sostiene: esempio di apprendimento statistico con mappatura in uno spazio di feature e superficie decisionale.
- Limite: viene usato come esempio della fase statistica, non come rappresentante unico degli anni Novanta.

### `SRC-HIST-008`. Reti convoluzionali, 1998

- Y. LeCun, L. Bottou, Y. Bengio, P. Haffner, *Gradient-Based Learning Applied to Document Recognition*, Proceedings of the IEEE 86(11), 2278-2324, 1998.
- DOI: `10.1109/5.726791`.
- Sostiene: reti multilivello addestrate con gradienti, convoluzioni per document recognition e sistemi addestrabili end-to-end.
- Limite: il lavoro riguarda principalmente riconoscimento di documenti e non coincide con l'intero deep learning moderno.

### `SRC-HIST-009`. ImageNet e GPU, 2012

- A. Krizhevsky, I. Sutskever, G. E. Hinton, *ImageNet Classification with Deep Convolutional Neural Networks*, NeurIPS 2012.
- Fonte: proceedings.neurips.cc.
- Sostiene: training di una rete convoluzionale profonda su ImageNet, uso di GPU e risultato della competizione dichiarato nel paper.
- Limite: il risultato è specifico a dataset, architettura e protocollo; non prova che il 2012 sia l'unica nascita del deep learning.

### `SRC-HIST-010`. Transformer, 2017

- A. Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.
- Fonte: proceedings.neurips.cc.
- Sostiene: architettura di sequence transduction basata sull'attention senza recurrence o convoluzioni nel blocco principale e maggiore parallelizzabilità dichiarata dagli autori.
- Limite: il paper valuta compiti specifici di traduzione e parsing; il ruolo storico successivo non viene dedotto soltanto dai risultati originali.

### `SRC-HIST-011`. BERT, 2019

- J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*, NAACL-HLT 2019, 4171-4186.
- DOI: `10.18653/v1/N19-1423`.
- Fonte: ACL Anthology.
- Sostiene: pretraining bidirezionale del Transformer e fine-tuning su molte attività linguistiche.
- Limite: BERT non rappresenta tutte le strategie di pretraining né tutti i foundation model.

### `SRC-HIST-012`. Scaling law, 2020

- J. Kaplan et al., *Scaling Laws for Neural Language Models*, arXiv:2001.08361, 2020.
- Sostiene: relazioni empiriche a legge di potenza tra loss, dimensione del modello, dati e compute negli esperimenti dichiarati.
- Limite: le leggi sono empiriche e dipendono da famiglia di modelli, obiettivo, dati e regime studiato.

### `SRC-HIST-013`. GPT-3, 2020

- T. B. Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020.
- Fonte: proceedings.neurips.cc.
- Sostiene: modello autoregressivo da 175 miliardi di parametri, valutazioni zero-shot e few-shot senza aggiornamento dei parametri per i task descritti.
- Limite: il paper documenta anche fallimenti, contaminazione possibile e limiti metodologici; non stabilisce capacità generale universale.

### `SRC-HIST-014`. Foundation model, 2021

- R. Bommasani et al., *On the Opportunities and Risks of Foundation Models*, arXiv:2108.07258, 2021.
- Sostiene: proposta del termine `foundation model` per modelli addestrati su dati ampi e adattabili a molti compiti, insieme a opportunità, rischi e omogeneizzazione.
- Limite: la categoria è proposta dagli autori e non è una tassonomia universale o immutabile.

## Regole d'uso

- Le date indicano pubblicazione o proposta, non l'inizio assoluto di un paradigma.
- Le fasi storiche si sovrappongono.
- Un paper portante non autorizza a dedurre adozione universale, causalità unica o superiorità generale.
- Dati quantitativi entrano nel capitolo soltanto quando servono alla spiegazione e vengono attribuiti al protocollo originale.
- Le affermazioni sul presente appartengono ai capitoli successivi e richiedono una verifica temporale separata.
