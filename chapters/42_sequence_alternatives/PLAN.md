# Piano interno. Capitolo 42

- Domanda centrale: quale contratto costruisce State-space model, recurrence e long convolution?
- Oggetto continuo: lo stato dinamico di un modello state-space; input guida: x_t, stato s_t e matrici A, B, C.
- Prerequisito stabile: Capitolo 41, Linear attention, fast weights e delta rule.
- Gap: recurrence, convolutione lunga o selezione.
- Output consegnato: stato e uscita per ogni posizione; consumer successivo: Capitolo 43, Architetture ibride e memoria interna.
- Invariante principale: stabilità e discretizzazione fanno parte dell'implementazione.
- Visuali: SSM-01 e SSM-02, con famiglie compositive variabili.
- Snippet: code/snip_42_contract.py; output: code/outputs/SNIP-42-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. State-space model

- Ultima affermazione stabile: lo stato dinamico di un modello state-space.
- Concetto nuovo: Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma convoluzionale.
- Input e shape: x_t, stato s_t e matrici A, B, C.
- Operazione: recurrence, convolutione lunga o selezione.
- Output e shape: stato e uscita per ogni posizione.
- Che cosa cambia: il passaggio specifico di «State-space model».
- Invariante: stabilità e discretizzazione fanno parte dell'implementazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre passi di una dinamica lineare con stato osservabile; provare anche una condizione incoerente e osservare il controllo.
- Consumer: S4.
- Prova: SRC-42-001 e sezione pubblica corrispondente.

## Transizione 2. S4

- Ultima affermazione stabile: lo stato dinamico di un modello state-space.
- Concetto nuovo: Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili.
- Input e shape: x_t, stato s_t e matrici A, B, C.
- Operazione: recurrence, convolutione lunga o selezione.
- Output e shape: stato e uscita per ogni posizione.
- Che cosa cambia: il passaggio specifico di «S4».
- Invariante: stabilità e discretizzazione fanno parte dell'implementazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre passi di una dinamica lineare con stato osservabile; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Mamba.
- Prova: SRC-42-002 e sezione pubblica corrispondente.

## Transizione 3. Mamba

- Ultima affermazione stabile: lo stato dinamico di un modello state-space.
- Concetto nuovo: Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan hardware-aware.
- Input e shape: x_t, stato s_t e matrici A, B, C.
- Operazione: recurrence, convolutione lunga o selezione.
- Output e shape: stato e uscita per ogni posizione.
- Che cosa cambia: il passaggio specifico di «Mamba».
- Invariante: stabilità e discretizzazione fanno parte dell'implementazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre passi di una dinamica lineare con stato osservabile; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Hyena e long convolution.
- Prova: SRC-42-003 e sezione pubblica corrispondente.

## Transizione 4. Hyena e long convolution

- Ultima affermazione stabile: lo stato dinamico di un modello state-space.
- Concetto nuovo: Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise.
- Input e shape: x_t, stato s_t e matrici A, B, C.
- Operazione: recurrence, convolutione lunga o selezione.
- Output e shape: stato e uscita per ogni posizione.
- Che cosa cambia: il passaggio specifico di «Hyena e long convolution».
- Invariante: stabilità e discretizzazione fanno parte dell'implementazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre passi di una dinamica lineare con stato osservabile; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RWKV, RetNet, xLSTM e Griffin.
- Prova: SRC-42-004 e sezione pubblica corrispondente.

## Transizione 5. RWKV, RetNet, xLSTM e Griffin

- Ultima affermazione stabile: lo stato dinamico di un modello state-space.
- Concetto nuovo: Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget e hardware equivalenti.
- Input e shape: x_t, stato s_t e matrici A, B, C.
- Operazione: recurrence, convolutione lunga o selezione.
- Output e shape: stato e uscita per ogni posizione.
- Che cosa cambia: il passaggio specifico di «RWKV, RetNet, xLSTM e Griffin».
- Invariante: stabilità e discretizzazione fanno parte dell'implementazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre passi di una dinamica lineare con stato osservabile; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Architetture ibride e memoria interna.
- Prova: SRC-42-001 e sezione pubblica corrispondente.
