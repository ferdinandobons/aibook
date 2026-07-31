# Fonti primarie. Capitolo 6

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: derivate, regola della catena, differenziazione automatica inversa, backpropagation e autograd PyTorch

## SRC-CALC-001. Deep Learning

Ian Goodfellow, Yoshua Bengio e Aaron Courville, Deep Learning, MIT Press, 2016, capitoli 5, 6 e 8. Sito ufficiale: https://www.deeplearningbook.org/

Uso: gradienti, regola della catena, grafi computazionali, backpropagation e relazione con l'ottimizzazione.

Limite: il capitolo separa la procedura che calcola i gradienti dal passo che aggiorna i parametri.

## SRC-CALC-002. Backpropagation nelle reti neurali

David E. Rumelhart, Geoffrey E. Hinton e Ronald J. Williams, Learning representations by back-propagating errors, Nature 323, 533-536, 1986. DOI: https://doi.org/10.1038/323533a0

Uso: ruolo storico e procedura di propagazione delle derivate attraverso unità nascoste.

Limite: non viene presentato come origine unica della differenziazione automatica inversa.

## SRC-CALC-003. Automatic Differentiation in Machine Learning

Atilim Gunes Baydin, Barak A. Pearlmutter, Alexey Andreyevich Radul e Jeffrey Mark Siskind, Automatic Differentiation in Machine Learning: a Survey, JMLR 18(153), 2018. URL: https://www.jmlr.org/papers/v18/17-468.html

Uso: distinzione tra differenze finite, differenziazione simbolica, automatic differentiation, forward mode e reverse mode.

Limite: la semantica di PyTorch viene verificata separatamente nella documentazione ufficiale.

## SRC-CALC-004. Evaluating Derivatives

Andreas Griewank e Andrea Walther, Evaluating Derivatives, seconda edizione, SIAM, 2008.

Uso: accumulazione tangente e aggiunta, complessità e implementazione della differenziazione automatica.

Limite: i metodi avanzati e le derivate di ordine superiore sono differiti.

## SRC-CALC-005. PyTorch autograd mechanics

Documentazione ufficiale PyTorch stable, Autograd mechanics. URL: https://docs.pytorch.org/docs/stable/notes/autograd.html

Uso: grafo costruito durante il forward, grad_fn, tensori salvati e reverse automatic differentiation.

Limite: il capitolo usa soltanto contratti documentati e non dipende da dettagli interni non garantiti.

## SRC-CALC-006. Tensor.backward

Documentazione ufficiale PyTorch stable, torch.Tensor.backward. URL: https://docs.pytorch.org/docs/stable/generated/torch.Tensor.backward.html

Uso: regola della catena, output scalare, gradiente esterno per output non scalari e accumulo nei campi grad dei tensori foglia.

Limite: semantica degli stream e dettagli CUDA non sono trattati.

## SRC-CALC-007. torch.autograd.grad

Documentazione ufficiale PyTorch stable, torch.autograd.grad. URL: https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad.html

Uso: restituzione dei gradienti e prodotti vettore-Jacobiana senza accumulo automatico negli input.

Limite: opzioni sperimentali e gradienti batch sono differiti.

## SRC-CALC-008. Gradcheck

Documentazione ufficiale PyTorch stable, torch.autograd.gradcheck e Gradcheck mechanics. URL: https://docs.pytorch.org/docs/stable/autograd e https://docs.pytorch.org/docs/stable/notes/gradcheck.html

Uso: confronto tra gradienti autograd e differenze finite; uso della doppia precisione con le tolleranze predefinite.

Limite: il controllo può fallire vicino a punti non differenziabili o con operazioni non deterministiche.

## SRC-CALC-009. Modalità di calcolo dei gradienti

Documentazione ufficiale PyTorch stable, Locally disabling gradient computation. URL: https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc

Uso: distinzione tra grad mode, no-grad mode e inference mode.

Limite: queste modalità non coincidono con la distinzione tra Module.train e Module.eval.

## Regola d'uso

Valori e gradienti numerici derivano da SNIP-CALC-001. Le fonti sostengono definizioni, algoritmi e contratti delle API, non i numeri illustrativi.
