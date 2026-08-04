# Fonti primarie e autorevoli. Capitolo 20

- Data di consultazione: 4 agosto 2026
- Routing semantico: capitolo 20 -> tema `generative`.
- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.
- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.

## SRC-20-001

- Titolo o riferimento: Kingma e Welling, Auto-Encoding Variational Bayes.
- Autori o organizzazione: Kingma e Welling.
- Tipo: paper o report tecnico.
- Data: data della revisione consultata.
- Versione, revisione o commit: arXiv 1312.6114, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1312.6114
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: abstract; latent-variable model; variational lower bound; reparameterization.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: un modello generativo può definire una distribuzione sui dati e introdurre variabili latenti con inferenza approssimata.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-20-002

- Titolo o riferimento: Mohamed e Lakshminarayanan, Learning in Implicit Generative Models.
- Autori o organizzazione: Shakir Mohamed e Balaji Lakshminarayanan.
- Tipo: paper o report tecnico.
- Data: 2016.
- Versione, revisione o commit: arXiv 1610.03483, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1610.03483
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e pagina originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: abstract; definizione di implicit generative model; rapporto con modelli likelihood-free.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: un modello implicito specifica una procedura stocastica di generazione senza richiedere una likelihood trattabile; questo lo distingue dai modelli con densità valutabile.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-20-003

- Titolo o riferimento: Kingma e Welling, Auto-Encoding Variational Bayes.
- Autori o organizzazione: Diederik P. Kingma e Max Welling.
- Tipo: paper o report tecnico.
- Data: 2013, revisione arXiv successiva.
- Versione, revisione o commit: arXiv 1312.6114, revisione consultata il 4 agosto 2026.
- URL o identificatore: https://arxiv.org/abs/1312.6114
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: latent-variable model; approximate posterior; variational lower bound.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: una variabile latente introduce struttura non osservata e l'inferenza collega dati e latenti, in questo caso tramite un'approssimazione variazionale.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-20-004

- Titolo o riferimento: LeCun et al., A Tutorial on Energy-Based Learning.
- Autori o organizzazione: Yann LeCun, Sumit Chopra, Raia Hadsell, Marc'Aurelio Ranzato e Fu-Jie Huang.
- Tipo: paper o report tecnico.
- Data: 2006.
- Versione, revisione o commit: capitolo in Predicting Structured Data, PDF degli autori consultato il 4 agosto 2026.
- URL o identificatore: https://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: catalogo dell'autore e PDF originale controllati; nessun risultato numerico trasferito.
- Sezioni rilevanti: definizione di energia; modelli probabilistici energy-based; funzione di partizione; strategie che ne evitano il calcolo.
- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.
- Affermazioni sostenibili: una funzione di energia assegna valori alle configurazioni; nei modelli probabilistici la normalizzazione introduce una funzione di partizione che può essere difficile da calcolare.
- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.
- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.

## SRC-20-005

- Titolo o riferimento: Kynkäänniemi et al., Improved Precision and Recall Metric for Assessing Generative Models.
- Autori o organizzazione: Tuomas Kynkäänniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen e Timo Aila.
- Tipo: paper peer-reviewed.
- Data: 2019.
- Versione, revisione o commit: NeurIPS 2019, pagina e PDF degli atti consultati il 4 agosto 2026.
- URL o identificatore: https://proceedings.neurips.cc/paper/2019/hash/0234c510bc6d908b28c70ff313743079-Abstract.html
- Data di consultazione: 4 agosto 2026.
- Verifica d'accesso: abstract e paper negli atti ufficiali controllati; nessun numero trasferito nel capitolo.
- Sezioni rilevanti: abstract; definizione separata di qualità e copertura; protocollo sperimentale.
- Perimetro del supporto: sostiene la necessità di distinguere qualità e copertura dei campioni nel protocollo studiato; non rende la metrica universale per ogni modalità.
- Affermazioni sostenibili: campioni visivamente plausibili non bastano a stabilire la copertura; precision e recall generative rispondono a proprietà differenti.
- Limiti: la metrica è studiata su image generation e non sostituisce likelihood, valutazione umana o metriche specifiche del dominio.
- Divergenze note: il capitolo usa la distinzione concettuale e non trasferisce i risultati quantitativi dei modelli valutati.

## Mappa d'uso

Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.
