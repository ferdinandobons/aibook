# Piano interno. Capitolo 22

- Domanda centrale: quale contratto costruisce Variational Autoencoder e latent discreti?
- Oggetto continuo: una variabile osservata e il suo codice latente; input guida: x, media, log-varianza e rumore epsilon.
- Prerequisito stabile: Capitolo 21, Modelli autoregressivi.
- Gap: ELBO e reparameterization trick.
- Output consegnato: ricostruzione, KL e codice latente; consumer successivo: Capitolo 23, Generative Adversarial Network.
- Invariante principale: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Visuali: VQ-01 e VQ-02, con famiglie compositive variabili.
- Snippet: code/snip_22_contract.py; output: code/outputs/SNIP-22-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Inferenza approssimata

- Ultima affermazione stabile: una variabile osservata e il suo codice latente.
- Concetto nuovo: Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z).
- Input e shape: x, media, log-varianza e rumore epsilon.
- Operazione: ELBO e reparameterization trick.
- Output e shape: ricostruzione, KL e codice latente.
- Che cosa cambia: il passaggio specifico di «Inferenza approssimata».
- Invariante: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una media, una deviazione e un campione z calcolato con epsilon; provare anche una condizione incoerente e osservare il controllo.
- Consumer: ELBO.
- Prova: SRC-22-001 e sezione pubblica corrispondente.

## Transizione 2. ELBO

- Ultima affermazione stabile: una variabile osservata e il suo codice latente.
- Concetto nuovo: L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva.
- Input e shape: x, media, log-varianza e rumore epsilon.
- Operazione: ELBO e reparameterization trick.
- Output e shape: ricostruzione, KL e codice latente.
- Che cosa cambia: il passaggio specifico di «ELBO».
- Invariante: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una media, una deviazione e un campione z calcolato con epsilon; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reparameterization trick.
- Prova: SRC-22-002 e sezione pubblica corrispondente.

## Transizione 3. Reparameterization trick

- Ultima affermazione stabile: una variabile osservata e il suo codice latente.
- Concetto nuovo: Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise.
- Input e shape: x, media, log-varianza e rumore epsilon.
- Operazione: ELBO e reparameterization trick.
- Output e shape: ricostruzione, KL e codice latente.
- Che cosa cambia: il passaggio specifico di «Reparameterization trick».
- Invariante: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una media, una deviazione e un campione z calcolato con epsilon; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Posterior collapse.
- Prova: SRC-22-003 e sezione pubblica corrispondente.

## Transizione 4. Posterior collapse

- Ultima affermazione stabile: una variabile osservata e il suo codice latente.
- Concetto nuovo: Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno.
- Input e shape: x, media, log-varianza e rumore epsilon.
- Operazione: ELBO e reparameterization trick.
- Output e shape: ricostruzione, KL e codice latente.
- Che cosa cambia: il passaggio specifico di «Posterior collapse».
- Invariante: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una media, una deviazione e un campione z calcolato con epsilon; provare anche una condizione incoerente e osservare il controllo.
- Consumer: VQ-VAE.
- Prova: SRC-22-004 e sezione pubblica corrispondente.

## Transizione 5. VQ-VAE

- Ultima affermazione stabile: una variabile osservata e il suo codice latente.
- Concetto nuovo: La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati.
- Input e shape: x, media, log-varianza e rumore epsilon.
- Operazione: ELBO e reparameterization trick.
- Output e shape: ricostruzione, KL e codice latente.
- Che cosa cambia: il passaggio specifico di «VQ-VAE».
- Invariante: la ricostruzione non elimina il costo KL né dimostra disentanglement.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una media, una deviazione e un campione z calcolato con epsilon; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Generative Adversarial Network.
- Prova: SRC-22-001 e sezione pubblica corrispondente.
