# Piano interno. Capitolo 44

- Domanda centrale: quale contratto costruisce Mixture of Experts e calcolo condizionale?
- Oggetto continuo: token e assegnazioni del router agli esperti; input guida: logits del router, top-k e capacità per esperto.
- Prerequisito stabile: Capitolo 43, Architetture ibride e memoria interna.
- Gap: routing, dispatch, expert compute e combine.
- Output consegnato: carico, token restituiti e costo attivo; consumer successivo: Capitolo 45, Byte, predizione multi-token e language diffusion.
- Invariante principale: parametri totali e parametri attivi non sono la stessa quantità.
- Visuali: MOE-01 e MOE-02, con famiglie compositive variabili.
- Snippet: code/snip_44_contract.py; output: code/outputs/SNIP-44-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Router top-k

- Ultima affermazione stabile: token e assegnazioni del router agli esperti.
- Concetto nuovo: Un router assegna probabilità agli esperti e attiva un sottoinsieme per token.
- Input e shape: logits del router, top-k e capacità per esperto.
- Operazione: routing, dispatch, expert compute e combine.
- Output e shape: carico, token restituiti e costo attivo.
- Che cosa cambia: il passaggio specifico di «Router top-k».
- Invariante: parametri totali e parametri attivi non sono la stessa quantità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro token assegnati a due esperti con capacità limitata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Capacità.
- Prova: SRC-44-001 e sezione pubblica corrispondente.

## Transizione 2. Capacità

- Ultima affermazione stabile: token e assegnazioni del router agli esperti.
- Concetto nuovo: Ogni esperto riceve un limite di token. Overflow, rerouting o dropping devono essere dichiarati.
- Input e shape: logits del router, top-k e capacità per esperto.
- Operazione: routing, dispatch, expert compute e combine.
- Output e shape: carico, token restituiti e costo attivo.
- Che cosa cambia: il passaggio specifico di «Capacità».
- Invariante: parametri totali e parametri attivi non sono la stessa quantità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro token assegnati a due esperti con capacità limitata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Load balancing.
- Prova: SRC-44-002 e sezione pubblica corrispondente.

## Transizione 3. Load balancing

- Ultima affermazione stabile: token e assegnazioni del router agli esperti.
- Concetto nuovo: Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione.
- Input e shape: logits del router, top-k e capacità per esperto.
- Operazione: routing, dispatch, expert compute e combine.
- Output e shape: carico, token restituiti e costo attivo.
- Che cosa cambia: il passaggio specifico di «Load balancing».
- Invariante: parametri totali e parametri attivi non sono la stessa quantità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro token assegnati a due esperti con capacità limitata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Expert parallelism.
- Prova: SRC-44-003 e sezione pubblica corrispondente.

## Transizione 4. Expert parallelism

- Ultima affermazione stabile: token e assegnazioni del router agli esperti.
- Concetto nuovo: Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti.
- Input e shape: logits del router, top-k e capacità per esperto.
- Operazione: routing, dispatch, expert compute e combine.
- Output e shape: carico, token restituiti e costo attivo.
- Che cosa cambia: il passaggio specifico di «Expert parallelism».
- Invariante: parametri totali e parametri attivi non sono la stessa quantità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro token assegnati a due esperti con capacità limitata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Parametri totali e attivi.
- Prova: SRC-44-004 e sezione pubblica corrispondente.

## Transizione 5. Parametri totali e attivi

- Ultima affermazione stabile: token e assegnazioni del router agli esperti.
- Concetto nuovo: Un MoE può avere molti parametri totali e pochi parametri attivi per token. FLOP, memoria e comunicazione vanno riportati separatamente.
- Input e shape: logits del router, top-k e capacità per esperto.
- Operazione: routing, dispatch, expert compute e combine.
- Output e shape: carico, token restituiti e costo attivo.
- Che cosa cambia: il passaggio specifico di «Parametri totali e attivi».
- Invariante: parametri totali e parametri attivi non sono la stessa quantità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro token assegnati a due esperti con capacità limitata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Byte, predizione multi-token e language diffusion.
- Prova: SRC-44-001 e sezione pubblica corrispondente.
