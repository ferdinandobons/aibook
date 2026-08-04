# Piano interno. Capitolo 87

- Domanda centrale: quale contratto costruisce Sparse autoencoder e interpretabilità scalabile?
- Oggetto continuo: un'attivazione scomposta in feature sparse; input guida: attivazione, dizionario, sparsità e ricostruzione.
- Prerequisito stabile: Capitolo 86, Interpretabilità delle rappresentazioni e dei circuiti.
- Gap: training SAE, splitting, dead features e tracing.
- Output consegnato: feature, errore di ricostruzione e circuito candidato; consumer successivo: Capitolo 88, Robustezza, jailbreak e attacchi adversarial.
- Invariante principale: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Visuali: TRACING-01 e TRACING-02, con famiglie compositive variabili.
- Snippet: code/snip_87_contract.py; output: code/outputs/SNIP-87-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Superposition

- Ultima affermazione stabile: un'attivazione scomposta in feature sparse.
- Concetto nuovo: Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre una ipotesi per separarle.
- Input e shape: attivazione, dizionario, sparsità e ricostruzione.
- Operazione: training SAE, splitting, dead features e tracing.
- Output e shape: feature, errore di ricostruzione e circuito candidato.
- Che cosa cambia: il passaggio specifico di «Superposition».
- Invariante: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due feature attive, una ricostruzione e un intervento; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sparse autoencoder.
- Prova: SRC-87-001 e sezione pubblica corrispondente.

## Transizione 2. Sparse autoencoder

- Ultima affermazione stabile: un'attivazione scomposta in feature sparse.
- Concetto nuovo: Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Loss e sparsity coefficient determinano il dizionario.
- Input e shape: attivazione, dizionario, sparsità e ricostruzione.
- Operazione: training SAE, splitting, dead features e tracing.
- Output e shape: feature, errore di ricostruzione e circuito candidato.
- Che cosa cambia: il passaggio specifico di «Sparse autoencoder».
- Invariante: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due feature attive, una ricostruzione e un intervento; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dead e splitting features.
- Prova: SRC-87-002 e sezione pubblica corrispondente.

## Transizione 3. Dead e splitting features

- Ultima affermazione stabile: un'attivazione scomposta in feature sparse.
- Concetto nuovo: Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità.
- Input e shape: attivazione, dizionario, sparsità e ricostruzione.
- Operazione: training SAE, splitting, dead features e tracing.
- Output e shape: feature, errore di ricostruzione e circuito candidato.
- Che cosa cambia: il passaggio specifico di «Dead e splitting features».
- Invariante: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due feature attive, una ricostruzione e un intervento; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Circuit tracing.
- Prova: SRC-87-003 e sezione pubblica corrispondente.

## Transizione 4. Circuit tracing

- Ultima affermazione stabile: un'attivazione scomposta in feature sparse.
- Concetto nuovo: Feature e attribution graph possono collegare input, computazione e output. Il grafo resta una approssimazione del calcolo completo.
- Input e shape: attivazione, dizionario, sparsità e ricostruzione.
- Operazione: training SAE, splitting, dead features e tracing.
- Output e shape: feature, errore di ricostruzione e circuito candidato.
- Che cosa cambia: il passaggio specifico di «Circuit tracing».
- Invariante: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due feature attive, una ricostruzione e un intervento; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione.
- Prova: SRC-87-004 e sezione pubblica corrispondente.

## Transizione 5. Valutazione

- Ultima affermazione stabile: un'attivazione scomposta in feature sparse.
- Concetto nuovo: Interpretabilità automatica, causal intervention e coverage devono essere misurate. Una etichetta leggibile non prova monosemanticità universale.
- Input e shape: attivazione, dizionario, sparsità e ricostruzione.
- Operazione: training SAE, splitting, dead features e tracing.
- Output e shape: feature, errore di ricostruzione e circuito candidato.
- Che cosa cambia: il passaggio specifico di «Valutazione».
- Invariante: interpretabilità di una feature richiede valutazione e controlli indipendenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due feature attive, una ricostruzione e un intervento; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Robustezza, jailbreak e attacchi adversarial.
- Prova: SRC-87-001 e sezione pubblica corrispondente.
