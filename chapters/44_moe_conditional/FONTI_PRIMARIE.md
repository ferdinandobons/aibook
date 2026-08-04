# Fonti primarie e autorevoli. Capitolo 44

- Data di consultazione: 3 agosto 2026
- Routing semantico: capitolo 44 -> tema `moe`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-44-001

- Titolo o riferimento: Shazeer et al., Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.
- Autori o organizzazione: Shazeer et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1701.06538
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer; 1.2 Our Approach: The Sparsely-Gated Mixture-of-Experts Layer; 1.3 Related work on Mixtures of Experts.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Un router assegna probabilità agli esperti e attiva un sottoinsieme per token. Un MoE può avere molti parametri totali e pochi parametri attivi per token.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-44-002

- Titolo o riferimento: Fedus, Zoph and Shazeer, Switch Transformers.
- Autori o organizzazione: Fedus.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2101.03961
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; 2.1 Simplifying Sparse Routing; 2.2 Efficient Sparse Routing; 5 Designing Models with Data, Model, and Expert-Parallelism.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Ogni esperto riceve un limite di token.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-44-003

- Titolo o riferimento: Dai et al., DeepSeekMoE.
- Autori o organizzazione: Dai et al..
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2401.06066
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models; 2 Preliminaries: Mixture-of-Experts for Transformers; 3.1 Fine-Grained Expert Segmentation.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-44-004

- Titolo o riferimento: DeepSeek-AI, DeepSeek-V3 Technical Report.
- Autori o organizzazione: DeepSeek-AI.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: revisione o versione disponibile all'URL consultato il 3 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/2412.19437
- Data di consultazione: 3 agosto 2026.
- Verifica d'accesso: opened-context; pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito.
- Sezioni rilevanti: Abstract / pagina iniziale; Appendix C Expert Specialization Patterns of the 16B Aux-Loss-Based and Aux-Loss-Free Models.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
