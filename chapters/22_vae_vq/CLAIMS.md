# Registro dei claim. Capitolo 22

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `vae` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-22-01

- Affermazione esatta: Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z).
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Auto-Encoding Variational Bayes; 2.2 The variational bound; 3 Example: Variational Auto-Encoder (claim collegato alla sezione «Inferenza approssimata» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-22-02

- Affermazione esatta: L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Appendix G Variational Bayes for Deep Directed Models (claim collegato alla sezione «ELBO» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-22-03

- Affermazione esatta: Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3.1 Discrete Latent variables (claim collegato alla sezione «Reparameterization trick» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-22-04

- Affermazione esatta: Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Lagging Inference Networks and Posterior Collapse in Variational Autoencoders; 2.1 Variational Autoencoders; 3 A Lagging Inference Network Prevents Using Latent Codes (claim collegato alla sezione «Posterior collapse» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-22-05

- Affermazione esatta: La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Auto-Encoding Variational Bayes; 2.2 The variational bound; 3 Example: Variational Auto-Encoder (claim collegato alla sezione «VQ-VAE» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-22-CODE

- Affermazione esatta: lo snippet snip_22_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_22_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
