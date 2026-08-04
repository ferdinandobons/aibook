# Piano editoriale. Capitolo 76

## Obiettivo didattico

Seguire **Decoding e generazione vincolata** da logits, prefisso, temperatura e vincolo a token scelto, sequenza e metrica di costo, osservando greedy, beam, sampling, penalty e stop senza oltrepassare questo limite: il decoding modifica la traiettoria, non corregge il modello a monte.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 21: Modelli autoregressivi
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Greedy e beam search.** Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza. Prova: SRC-76-001.
2. **Sampling.** Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità. Prova: SRC-76-002.
3. **Penalità e stop.** Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire. Prova: SRC-76-003.
4. **Constrained decoding.** Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti. Prova: SRC-76-004.
5. **Metriche.** Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme. Prova: SRC-76-001.

## Prove e artefatti

- riferimento minimo: `code/snip_76_contract.py`; test: `code/test_76_contract.py`; output: `code/outputs/SNIP-76-001.txt`.
- visuali candidate: DECODING-01, DECODING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
