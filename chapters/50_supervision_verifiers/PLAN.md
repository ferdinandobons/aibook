# Piano editoriale. Capitolo 50

## Obiettivo didattico

Seguire **Process supervision, outcome supervision e verifier** da passaggi, risposta finale, criterio e indipendenza a score verificato e failure localizzata, osservando process supervision, outcome supervision e verifica senza oltrepassare questo limite: un verifier può ereditare bias o essere ottimizzato.

## Prerequisiti reali

- Capitolo 46: Supervised fine-tuning e instruction tuning
- Capitolo 48: Preferenze, reward model e RLHF

## Percorso della lezione

1. **Supervisionare il risultato.** Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore. Prova: SRC-50-001.
2. **Supervisionare il processo.** Process supervision etichetta passaggi intermedi. La validità dipende da come il processo viene reso osservabile e annotato. Prova: SRC-50-002.
3. **Verifier.** Un verifier valuta candidate rispetto a un criterio. Può essere una regola, un esecutore, un modello o una combinazione. Prova: SRC-50-003.
4. **Reward model di processo.** Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento. Prova: SRC-50-004.
5. **Goodhart e indipendenza.** Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting. Servono test e verificatori indipendenti. Prova: SRC-50-001.

## Prove e artefatti

- riferimento minimo: `code/snip_50_contract.py`; test: `code/test_50_contract.py`; output: `code/outputs/SNIP-50-001.txt`.
- visuali candidate: VERIFIERS-01, VERIFIERS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
