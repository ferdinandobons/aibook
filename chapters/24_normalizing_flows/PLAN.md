# Piano editoriale. Capitolo 24

## Obiettivo didattico

Seguire **Normalizing flow e trasformazioni invertibili** da x, log-determinante e variabile latente z a log-likelihood, z e campione ricostruito, osservando coupling, cambio di variabile e inversione senza oltrepassare questo limite: l'inversione richiede una trasformazione e un log-determinante coerenti.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 20: Fondamenti della modellazione generativa

## Percorso della lezione

1. **Cambio di variabile.** Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano. Prova: SRC-24-001.
2. **Coupling layer.** RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti. Prova: SRC-24-002.
3. **Invertibilità e architettura.** L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla. Prova: SRC-24-003.
4. **Continuous normalizing flow.** Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso. Prova: SRC-24-004.
5. **Sampling e costo.** I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici. Prova: SRC-24-001.

## Prove e artefatti

- riferimento minimo: `code/snip_24_contract.py`; test: `code/test_24_contract.py`; output: `code/outputs/SNIP-24-001.txt`.
- visuali candidate: FLOWS-01, FLOWS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
