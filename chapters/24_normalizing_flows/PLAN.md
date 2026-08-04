# Piano interno. Capitolo 24

- Domanda centrale: quale contratto costruisce Normalizing flow e trasformazioni invertibili?
- Oggetto continuo: un dato trasformato da una mappa invertibile; input guida: x, log-determinante e variabile latente z.
- Prerequisito stabile: Capitolo 23, Generative Adversarial Network.
- Gap: coupling, cambio di variabile e inversione.
- Output consegnato: log-likelihood, z e campione ricostruito; consumer successivo: Capitolo 25, Diffusione, score matching e flow matching.
- Invariante principale: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Visuali: FLOWS-01 e FLOWS-02, con famiglie compositive variabili.
- Snippet: code/snip_24_contract.py; output: code/outputs/SNIP-24-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Cambio di variabile

- Ultima affermazione stabile: un dato trasformato da una mappa invertibile.
- Concetto nuovo: Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano.
- Input e shape: x, log-determinante e variabile latente z.
- Operazione: coupling, cambio di variabile e inversione.
- Output e shape: log-likelihood, z e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Cambio di variabile».
- Invariante: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una trasformazione affine a due coordinate invertita senza perdita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Coupling layer.
- Prova: SRC-24-001 e sezione pubblica corrispondente.

## Transizione 2. Coupling layer

- Ultima affermazione stabile: un dato trasformato da una mappa invertibile.
- Concetto nuovo: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti.
- Input e shape: x, log-determinante e variabile latente z.
- Operazione: coupling, cambio di variabile e inversione.
- Output e shape: log-likelihood, z e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Coupling layer».
- Invariante: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una trasformazione affine a due coordinate invertita senza perdita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Invertibilità e architettura.
- Prova: SRC-24-002 e sezione pubblica corrispondente.

## Transizione 3. Invertibilità e architettura

- Ultima affermazione stabile: un dato trasformato da una mappa invertibile.
- Concetto nuovo: L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla.
- Input e shape: x, log-determinante e variabile latente z.
- Operazione: coupling, cambio di variabile e inversione.
- Output e shape: log-likelihood, z e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Invertibilità e architettura».
- Invariante: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una trasformazione affine a due coordinate invertita senza perdita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Continuous normalizing flow.
- Prova: SRC-24-003 e sezione pubblica corrispondente.

## Transizione 4. Continuous normalizing flow

- Ultima affermazione stabile: un dato trasformato da una mappa invertibile.
- Concetto nuovo: Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso.
- Input e shape: x, log-determinante e variabile latente z.
- Operazione: coupling, cambio di variabile e inversione.
- Output e shape: log-likelihood, z e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Continuous normalizing flow».
- Invariante: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una trasformazione affine a due coordinate invertita senza perdita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sampling e costo.
- Prova: SRC-24-004 e sezione pubblica corrispondente.

## Transizione 5. Sampling e costo

- Ultima affermazione stabile: un dato trasformato da una mappa invertibile.
- Concetto nuovo: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici.
- Input e shape: x, log-determinante e variabile latente z.
- Operazione: coupling, cambio di variabile e inversione.
- Output e shape: log-likelihood, z e campione ricostruito.
- Che cosa cambia: il passaggio specifico di «Sampling e costo».
- Invariante: l'inversione richiede una trasformazione e un log-determinante coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una trasformazione affine a due coordinate invertita senza perdita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Diffusione, score matching e flow matching.
- Prova: SRC-24-001 e sezione pubblica corrispondente.
