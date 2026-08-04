# Piano interno. Capitolo 70

- Domanda centrale: quale contratto costruisce Multi-agent, browser, computer e code agents?
- Oggetto continuo: una traiettoria composta da agenti e strumenti; input guida: task, ruoli, browser, codice e handoff.
- Prerequisito stabile: Capitolo 69, Ciclo agentico, pianificazione e verifica.
- Gap: delega, comunicazione, esecuzione e aggregazione.
- Output consegnato: risultato con responsabilità e log per componente; consumer successivo: Capitolo 71, Training e valutazione degli agenti.
- Invariante principale: più agenti ampliano anche superficie e costo dell'errore.
- Visuali: SYSTEMS-01 e SYSTEMS-02, con famiglie compositive variabili.
- Snippet: code/snip_70_contract.py; output: code/outputs/SNIP-70-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Browser agent

- Ultima affermazione stabile: una traiettoria composta da agenti e strumenti.
- Concetto nuovo: L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate.
- Input e shape: task, ruoli, browser, codice e handoff.
- Operazione: delega, comunicazione, esecuzione e aggregazione.
- Output e shape: risultato con responsabilità e log per componente.
- Che cosa cambia: il passaggio specifico di «Browser agent».
- Invariante: più agenti ampliano anche superficie e costo dell'errore.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un planner delega ricerca e verifica a due ruoli separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Computer use.
- Prova: SRC-70-001 e sezione pubblica corrispondente.

## Transizione 2. Computer use

- Ultima affermazione stabile: una traiettoria composta da agenti e strumenti.
- Concetto nuovo: Screenshot, coordinate e azioni di input formano un loop percettivo. Risoluzione, focus e stato dell'interfaccia possono cambiare.
- Input e shape: task, ruoli, browser, codice e handoff.
- Operazione: delega, comunicazione, esecuzione e aggregazione.
- Output e shape: risultato con responsabilità e log per componente.
- Che cosa cambia: il passaggio specifico di «Computer use».
- Invariante: più agenti ampliano anche superficie e costo dell'errore.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un planner delega ricerca e verifica a due ruoli separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Code agent.
- Prova: SRC-70-002 e sezione pubblica corrispondente.

## Transizione 3. Code agent

- Ultima affermazione stabile: una traiettoria composta da agenti e strumenti.
- Concetto nuovo: Repository, test, shell e diff definiscono l'ambiente. Modifiche devono essere limitate, testate e revisionabili.
- Input e shape: task, ruoli, browser, codice e handoff.
- Operazione: delega, comunicazione, esecuzione e aggregazione.
- Output e shape: risultato con responsabilità e log per componente.
- Che cosa cambia: il passaggio specifico di «Code agent».
- Invariante: più agenti ampliano anche superficie e costo dell'errore.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un planner delega ricerca e verifica a due ruoli separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Multi-agent.
- Prova: SRC-70-003 e sezione pubblica corrispondente.

## Transizione 4. Multi-agent

- Ultima affermazione stabile: una traiettoria composta da agenti e strumenti.
- Concetto nuovo: Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori.
- Input e shape: task, ruoli, browser, codice e handoff.
- Operazione: delega, comunicazione, esecuzione e aggregazione.
- Output e shape: risultato con responsabilità e log per componente.
- Che cosa cambia: il passaggio specifico di «Multi-agent».
- Invariante: più agenti ampliano anche superficie e costo dell'errore.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un planner delega ricerca e verifica a due ruoli separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Confronto con un singolo workflow.
- Prova: SRC-70-004 e sezione pubblica corrispondente.

## Transizione 5. Confronto con un singolo workflow

- Ultima affermazione stabile: una traiettoria composta da agenti e strumenti.
- Concetto nuovo: Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget.
- Input e shape: task, ruoli, browser, codice e handoff.
- Operazione: delega, comunicazione, esecuzione e aggregazione.
- Output e shape: risultato con responsabilità e log per componente.
- Che cosa cambia: il passaggio specifico di «Confronto con un singolo workflow».
- Invariante: più agenti ampliano anche superficie e costo dell'errore.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un planner delega ricerca e verifica a due ruoli separati; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Training e valutazione degli agenti.
- Prova: SRC-70-001 e sezione pubblica corrispondente.
