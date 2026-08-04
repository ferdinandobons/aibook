# Piano interno. Capitolo 25

- Domanda centrale: quale contratto costruisce Diffusione, score matching e flow matching?
- Oggetto continuo: un dato corrotto e il percorso di denoising; input guida: x_0, rumore epsilon e timestep t.
- Prerequisito stabile: Capitolo 24, Normalizing flow e trasformazioni invertibili.
- Gap: forward noising, score o velocity e sampler.
- Output consegnato: stima del rumore e campione ricostruito; consumer successivo: Capitolo 26, Il testo come dato.
- Invariante principale: parametrizzazione e scheduler fanno parte del contratto.
- Visuali: FLOW-01 e FLOW-02, con famiglie compositive variabili.
- Snippet: code/snip_25_contract.py; output: code/outputs/SNIP-25-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Corrompere e ricostruire

- Ultima affermazione stabile: un dato corrotto e il percorso di denoising.
- Concetto nuovo: La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente.
- Input e shape: x_0, rumore epsilon e timestep t.
- Operazione: forward noising, score o velocity e sampler.
- Output e shape: stima del rumore e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Corrompere e ricostruire».
- Invariante: parametrizzazione e scheduler fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un singolo timestep con rumore noto e stima separata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Score matching.
- Prova: SRC-25-001 e sezione pubblica corrispondente.

## Transizione 2. Score matching

- Ultima affermazione stabile: un dato corrotto e il percorso di denoising.
- Concetto nuovo: Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa.
- Input e shape: x_0, rumore epsilon e timestep t.
- Operazione: forward noising, score o velocity e sampler.
- Output e shape: stima del rumore e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Score matching».
- Invariante: parametrizzazione e scheduler fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un singolo timestep con rumore noto e stima separata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Parametrizzazioni epsilon, x0 e v.
- Prova: SRC-25-002 e sezione pubblica corrispondente.

## Transizione 3. Parametrizzazioni epsilon, x0 e v

- Ultima affermazione stabile: un dato corrotto e il percorso di denoising.
- Concetto nuovo: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training.
- Input e shape: x_0, rumore epsilon e timestep t.
- Operazione: forward noising, score o velocity e sampler.
- Output e shape: stima del rumore e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Parametrizzazioni epsilon, x0 e v».
- Invariante: parametrizzazione e scheduler fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un singolo timestep con rumore noto e stima separata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sampler.
- Prova: SRC-25-003 e sezione pubblica corrispondente.

## Transizione 4. Sampler

- Ultima affermazione stabile: un dato corrotto e il percorso di denoising.
- Concetto nuovo: DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità.
- Input e shape: x_0, rumore epsilon e timestep t.
- Operazione: forward noising, score o velocity e sampler.
- Output e shape: stima del rumore e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Sampler».
- Invariante: parametrizzazione e scheduler fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un singolo timestep con rumore noto e stima separata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Flow matching e rectified flow.
- Prova: SRC-25-004 e sezione pubblica corrispondente.

## Transizione 5. Flow matching e rectified flow

- Ultima affermazione stabile: un dato corrotto e il percorso di denoising.
- Concetto nuovo: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici.
- Input e shape: x_0, rumore epsilon e timestep t.
- Operazione: forward noising, score o velocity e sampler.
- Output e shape: stima del rumore e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Flow matching e rectified flow».
- Invariante: parametrizzazione e scheduler fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un singolo timestep con rumore noto e stima separata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Il testo come dato.
- Prova: SRC-25-001 e sezione pubblica corrispondente.
