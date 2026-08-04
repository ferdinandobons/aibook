# Piano editoriale. Capitolo 23

## Obiettivo didattico

Seguire **Generative Adversarial Network** da un dato reale, un campione e due score a score, gradiente e campione, osservando aggiornamento alternato e segnale di feedback senza oltrepassare questo limite: un equilibrio locale non prova copertura né stabilità.

## Prerequisiti reali

- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 20: Fondamenti della modellazione generativa

## Percorso della lezione

1. **Un gioco tra due modelli.** Il generatore produce campioni; il discriminatore distingue dati reali e generati. L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente. Prova: SRC-23-001.
2. **Divergenze e gradienti.** La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. I gradienti pratici dipendono dalla loss scelta. Prova: SRC-23-002.
3. **Mode collapse.** Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere misurate separatamente. Prova: SRC-23-003.
4. **Wasserstein GAN.** WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty sono implementazioni differenti del vincolo. Prova: SRC-23-004.
5. **Stabilità e valutazione.** Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature e non sostituisce l'analisi dei campioni. Prova: SRC-23-001.

## Prove e artefatti

- riferimento minimo: `code/snip_23_contract.py`; test: `code/test_23_contract.py`; output: `code/outputs/SNIP-23-001.txt`.
- visuali candidate: GAN-01, GAN-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
