# Claim

- `CL-VQ-001`. Inferenza approssimata: Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z).
- `CL-VQ-002`. ELBO: L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva.
- `CL-VQ-003`. Reparameterization trick: Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise.
- `CL-VQ-004`. Posterior collapse: Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno.
- `CL-VQ-005`. VQ-VAE: La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati.
