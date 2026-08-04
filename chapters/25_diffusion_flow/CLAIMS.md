# Registro dei claim. Capitolo 25

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `diffusion` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-25-01

- Affermazione esatta: La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Denoising Diffusion Probabilistic Models; 3 Diffusion models and denoising autoencoders (claim collegato alla sezione «Corrompere e ricostruire» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-25-02

- Affermazione esatta: Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Score-Based Generative Modeling through Stochastic Differential Equations; 2.1 Denoising score matching with Langevin dynamics (SMLD); 2.2 Denoising diffusion probabilistic models (DDPM) (claim collegato alla sezione «Score matching» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-25-03

- Affermazione esatta: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Flow Matching for Generative Modeling; 3 Flow Matching; 3.2 Conditional Flow Matching (claim collegato alla sezione «Parametrizzazioni epsilon, x0 e v» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-25-04

- Affermazione esatta: DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; High-Resolution Image Synthesis with Latent Diffusion Models; 3.2 Latent Diffusion Models; 4.2 Image Generation with Latent Diffusion (claim collegato alla sezione «Sampler» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-25-05

- Affermazione esatta: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Denoising Diffusion Probabilistic Models; 3 Diffusion models and denoising autoencoders (claim collegato alla sezione «Flow matching e rectified flow» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-25-CODE

- Affermazione esatta: lo snippet snip_25_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_25_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
