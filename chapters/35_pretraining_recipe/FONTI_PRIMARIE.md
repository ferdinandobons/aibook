# Fonti primarie e autorevoli. Capitolo 35

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 35 -> tema `pretraining_recipe`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-35-001

- Titolo o riferimento: Brown et al., Language Models are Few-Shot Learners.
- Autori o organizzazione: Brown et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2005.14165
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Language Models are Few-Shot Learners; 3.1 Language Modeling, Cloze, and Completion Tasks; 3.1.1 Language Modeling.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Packing, padding e mask determinano quanti token validi contribuiscono alla loss. Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-35-002

- Titolo o riferimento: Loshchilov and Hutter, Decoupled Weight Decay Regularization.
- Autori o organizzazione: Loshchilov and Hutter.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1711.05101
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 4.1 Evaluating Decoupled Weight Decay With Different Learning Rate Schedules; 4.2 Decoupling the Weight Decay and Initial Learning Rate Parameters.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Scala dei pesi e residual deve restare coerente con profondità, norm e dtype.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-35-003

- Titolo o riferimento: Goyal et al., Accurate, Large Minibatch SGD.
- Autori o organizzazione: Goyal et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1706.02677
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour; 2.1 Learning Rates for Large Minibatches; Training error..
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-35-004

- Titolo o riferimento: PyTorch, Saving and Loading Checkpoints.
- Autori o organizzazione: PyTorch.
- Tipo: standard o documentazione ufficiale.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 4 agosto 2026.
- URL o identificatore: https://pytorch.org/tutorials/beginner/saving_loading_models.html
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Saving & Loading a General Checkpoint for Inference and/or Resuming Training #.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Il learning rate dipende da step o token e deve riprendere dal contatore corretto.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
