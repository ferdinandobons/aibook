# Piano editoriale. Capitolo 22

## Obiettivo didattico

Seguire **Variational Autoencoder e latent discreti** da x, media, log-varianza e rumore epsilon a ricostruzione, KL e codice latente, osservando ELBO e reparameterization trick senza oltrepassare questo limite: la ricostruzione non elimina il costo KL né dimostra disentanglement.

## Prerequisiti reali

- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 20: Fondamenti della modellazione generativa

## Percorso della lezione

1. **Inferenza approssimata.** Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z). Prova: SRC-22-001.
2. **ELBO.** L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva. Prova: SRC-22-002.
3. **Reparameterization trick.** Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise. Prova: SRC-22-003.
4. **Posterior collapse.** Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno. Prova: SRC-22-004.
5. **VQ-VAE.** La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati. Prova: SRC-22-001.

## Prove e artefatti

- riferimento minimo: `code/snip_22_contract.py`; test: `code/test_22_contract.py`; output: `code/outputs/SNIP-22-001.txt`.
- visuali candidate: VQ-01, VQ-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
