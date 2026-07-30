# Fonti primarie. Capitolo 3

## Stato

- Capitolo: `CH-P01-LIFECYCLE`
- Ultima verifica: 30 luglio 2026
- Ambito: dati, training, valutazione, documentazione, deployment, monitoraggio e ritiro

## Fonti

### `SRC-LIFE-001`. NIST AI RMF 1.0

- NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, gennaio 2023.
- DOI: `10.6028/NIST.AI.100-1`.
- Sostiene: gestione del rischio lungo il ciclo di vita e funzioni `GOVERN`, `MAP`, `MEASURE`, `MANAGE`.
- Limite: è un framework volontario e non prescrive una singola pipeline tecnica.

### `SRC-LIFE-002`. NIST AI RMF Playbook

- NIST AI Resource Center, *AI RMF Playbook*.
- Fonte ufficiale: `airc.nist.gov/airmf-resources/playbook/`.
- Sostiene: esempi di azioni associate alle funzioni del framework, documentazione, monitoraggio e responsabilità.
- Limite: playbook evolutivo; verificare la versione corrente quando viene citato in un'edizione futura.

### `SRC-LIFE-003`. Datasheets for Datasets

- T. Gebru et al., *Datasheets for Datasets*, Communications of the ACM 64(12), 86-92, 2021.
- DOI: `10.1145/3458723`.
- Sostiene: proposta di documentazione standardizzata per motivazione, composizione, raccolta, preprocessing, usi e manutenzione dei dataset.
- Limite: è un framework di documentazione, non una garanzia di qualità del dataset.

### `SRC-LIFE-004`. Model Cards

- M. Mitchell et al., *Model Cards for Model Reporting*, FAT* 2019.
- DOI: `10.1145/3287560.3287596`.
- Sostiene: documentazione di uso previsto, procedure di valutazione, prestazioni e limiti dei modelli.
- Limite: una model card non sostituisce test, monitoraggio o governance.

### `SRC-LIFE-005`. Hidden Technical Debt

- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, NeurIPS 2015.
- Fonte: proceedings.neurips.cc.
- Sostiene: dipendenze da dati, entanglement, feedback loop, glue code, configurazione e altri rischi sistemici dei sistemi ML.
- Limite: classificazione e esempi derivano dall'esperienza descritta dagli autori; non ogni sistema presenta tutti i problemi.

### `SRC-LIFE-006`. ML Test Score

- E. Breck et al., *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*, IEEE Big Data 2017.
- DOI: `10.1109/BigData.2017.8258038`.
- Sostiene: test e monitoraggio su dati, feature, modello e infrastruttura come requisiti di production readiness.
- Limite: rubrica basata su esperienza industriale; non è uno standard universale.

### `SRC-LIFE-007`. TFX

- D. Baylor et al., *TFX: A TensorFlow-Based Production-Scale Machine Learning Platform*, KDD 2017.
- DOI: `10.1145/3097983.3098021`.
- Sostiene: orchestrazione di analisi dati, validazione, training e serving; necessità di aggiornare modelli quando i dati cambiano.
- Limite: caso di piattaforma specifica e risultati specifici alle implementazioni descritte.

### `SRC-LIFE-008`. Software Engineering for Machine Learning

- S. Amershi et al., *Software Engineering for Machine Learning: A Case Study*, ICSE-SEIP 2019.
- DOI: `10.1109/ICSE-SEIP.2019.00042`.
- Sostiene: workflow a più fasi, complessità di dati e versioning, riuso e personalizzazione dei modelli, difficoltà di modularizzazione.
- Limite: studio di team Microsoft; non rappresenta ogni organizzazione.

### `SRC-LIFE-009`. Train, validation e test

- I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning*, MIT Press, 2016, capitolo 5.
- Versione ufficiale: `deeplearningbook.org`.
- Sostiene: separazione tra training, validation e test e ruolo della validation nella selezione degli iperparametri.
- Limite: principi generali; il protocollo concreto dipende da dati, dipendenze temporali e obiettivo.

### `SRC-LIFE-010`. PyTorch

- Documentazione ufficiale PyTorch stable, `Module.train`, `Module.eval`, `torch.inference_mode`, `state_dict`.
- Sostiene: semantica corrente delle API usate nello snippet.
- Limite: la versione documentata viene distinta dall'ambiente realmente eseguito.

## Regole d'uso

- `ciclo di vita` indica un insieme iterativo di attività, non una pipeline identica per ogni organizzazione.
- `drift` descrive una differenza osservata in dati o relazioni; non prova da solo una causa di degradazione.
- `monitoraggio` non viene presentato come garanzia di rilevare ogni errore.
- una metrica offline non viene equiparata automaticamente a utilità, sicurezza o qualità del prodotto.
- deployment, serving e inference restano concetti distinti.
