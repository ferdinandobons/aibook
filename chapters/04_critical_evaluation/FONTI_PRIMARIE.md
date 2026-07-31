# Fonti primarie. Capitolo 4

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: valutazione, variabilità, leakage, benchmark, contaminazione e riproducibilità

## `SRC-EVAL-001`. NIST AI RMF 1.0

- Elham Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023.
- URL: https://doi.org/10.6028/NIST.AI.100-1
- Uso: valutazione collegata a contesto, rischio, misurazione e gestione lungo il ciclo di vita.
- Limite: framework volontario e use-case agnostic; non prescrive un'unica metrica o procedura sperimentale.

## `SRC-EVAL-002`. NIST AI Resource Center e AI Metrology Center

- NIST AIRC, risorse per testing, evaluation, verification and validation.
- URL: https://airc.nist.gov/
- URL: https://airc.nist.gov/metrology/
- Uso: la scelta delle misure dipende dal caso d'uso e dalle proprietà da valutare.
- Limite: l'inclusione di una risorsa non costituisce approvazione o garanzia di adeguatezza.

## `SRC-EVAL-003`. Reproducibility Program

- Joelle Pineau et al., *Improving Reproducibility in Machine Learning Research*, JMLR 22(164), 2021.
- URL: https://www.jmlr.org/papers/v22/20-303.html
- Uso: codice, dati, checklist e workflow sperimentali come supporto alla verificabilità.
- Limite: il paper descrive il programma NeurIPS 2019; non dimostra che una checklist renda automaticamente corretto un risultato.

## `SRC-EVAL-004`. Variance in benchmarks

- Xavier Bouthillier et al., *Accounting for Variance in Machine Learning Benchmarks*, MLSys 2021.
- URL: https://proceedings.mlsys.org/paper_files/paper/2021/hash/0184b0cd3cfb185989f858a1d9f5c1eb-Abstract.html
- Uso: seed, campionamento, inizializzazione e tuning possono incidere sul confronto tra pipeline.
- Limite: risultati e raccomandazioni dipendono dagli esperimenti analizzati; non forniscono un numero universale di run.

## `SRC-EVAL-005`. Significatività in NLP

- Rotem Dror et al., *The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing*, ACL 2018.
- URL: https://aclanthology.org/P18-1128/
- Uso: il test statistico deve essere scelto in funzione di setup, misura e dipendenza tra osservazioni.
- Limite: guida orientata all'NLP; non sostituisce la verifica delle ipotesi del test in altri domini.

## `SRC-EVAL-006`. Bootstrap

- Bradley Efron, *Bootstrap Methods: Another Look at the Jackknife*, The Annals of Statistics 7(1), 1979.
- DOI: https://doi.org/10.1214/aos/1176344552
- Uso: fondamento del resampling bootstrap usato nello snippet illustrativo.
- Limite: il capitolo usa un semplice percentile bootstrap appaiato; non lo presenta come intervallo ottimale per ogni misura o dimensione campionaria.

## `SRC-EVAL-007`. Nuovi test set

- Benjamin Recht et al., *Do ImageNet Classifiers Generalize to ImageNet?*, ICML 2019.
- URL: https://proceedings.mlr.press/v97/recht19a.html
- Uso: prestazioni su nuovi test set possono differire dal benchmark originale; il paper discute il riuso prolungato dei test set.
- Limite: conclusioni specifiche a CIFAR-10, ImageNet e al processo di ricostruzione usato.

## `SRC-EVAL-008`. Errori nelle label dei benchmark

- Curtis Northcutt, Anish Athalye, Jonas Mueller, *Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks*, NeurIPS Datasets and Benchmarks 2021.
- URL: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/f2217062e9a397a1dca429e7d70bc6ca-Abstract-round1.html
- Uso: errori nelle label del test set possono alterare ranking e conclusioni.
- Limite: stime e casi riguardano i dieci dataset studiati; non autorizzano a presumere la stessa percentuale altrove.

## `SRC-EVAL-009`. Leakage

- Shachar Kaufman, Saharon Rosset, Claudia Perlich, *Leakage in Data Mining: Formulation, Detection, and Avoidance*, ACM TKDD 6(4), 2012.
- DOI: https://doi.org/10.1145/2382577.2382579
- Uso: informazione sul target non legittimamente disponibile al momento della previsione può rendere ingannevole una valutazione.
- Limite: il capitolo usa la definizione generale; non riduce ogni errore di split a leakage.

## `SRC-EVAL-010`. Shortcut learning

- Robert Geirhos et al., *Shortcut Learning in Deep Neural Networks*, Nature Machine Intelligence 2, 2020.
- DOI: https://doi.org/10.1038/s42256-020-00257-z
- Uso: una buona prestazione sul benchmark può derivare da regolarità semplici che non trasferiscono alle condizioni desiderate.
- Limite: perspective con esempi e raccomandazioni; non implica che ogni errore di generalizzazione sia shortcut learning.

## `SRC-EVAL-011`. Contaminazione dei benchmark per LLM

- Yonatan Oren et al., *Proving Test Set Contamination in Black-Box Language Models*, ICLR 2024.
- URL: https://proceedings.iclr.cc/paper_files/paper/2024/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html
- Uso: la contaminazione di benchmark pubblici può essere studiata anche senza accesso ai dati di pretraining attraverso un test con garanzie dichiarate.
- Limite: metodo fondato sull'ordine canonico e sulle ipotesi del paper; non rileva ogni forma possibile di contaminazione.

## `SRC-EVAL-012`. Model Cards

- Margaret Mitchell et al., *Model Cards for Model Reporting*, FAT* 2019.
- URL: https://doi.org/10.1145/3287560.3287596
- Uso: uso previsto, metriche, gruppi, condizioni e limiti vanno documentati insieme al risultato.
- Limite: formato proposto, non certificazione della qualità del modello.

## `SRC-EVAL-013`. NeurIPS Paper Checklist

- NeurIPS, *Paper Checklist Guidelines*, versione consultata il 31 luglio 2026.
- URL: https://neurips.cc/public/guides/PaperChecklist
- Uso: dettagli di training, split, run, error bar, risorse e artefatti riproducibili come elementi di trasparenza.
- Limite: linee guida editoriali di una conferenza; non sostituiscono l'audit del singolo claim.

## Regola d'uso

Il capitolo non trasferisce automaticamente risultati quantitativi da un benchmark a un altro. Percentuali, intervalli e costi mostrati nello snippet sono dati illustrativi generati localmente e non risultati tratti dalle fonti elencate.
