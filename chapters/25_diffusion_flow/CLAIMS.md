# Claim

- `CL-FLOW-001`. Corrompere e ricostruire: La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente.
- `CL-FLOW-002`. Score matching: Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa.
- `CL-FLOW-003`. Parametrizzazioni epsilon, x0 e v: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training.
- `CL-FLOW-004`. Sampler: DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità.
- `CL-FLOW-005`. Flow matching e rectified flow: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici.
