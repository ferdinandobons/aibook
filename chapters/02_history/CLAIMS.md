# Registro dei claim. Capitolo 2

## Stato

- Capitolo: `CH-P01-HISTORY`
- Versione del registro: `0.1.0`
- Ultima verifica: 30 luglio 2026
- Stato: claim portanti verificati nelle fonti indicate

| ID | Claim sostenibile | Prova | Tipo | Limite |
|---|---|---|---|---|
| `CLM-HIST-001` | Turing pubblicò *Computing Machinery and Intelligence* nel 1950 e formulò l'imitation game come modo operativo di discutere il comportamento di una macchina. | `SRC-HIST-001` | fonte primaria | non definisce il campo moderno dell'AI |
| `CLM-HIST-002` | La proposta di Dartmouth del 31 agosto 1955 usa esplicitamente l'espressione `artificial intelligence` e propone una ricerca estiva nel 1956. | `SRC-HIST-002` | fonte primaria | non autorizza a indicare un'unica nascita assoluta del campo |
| `CLM-HIST-003` | La proposta di Dartmouth include linguaggio, astrazione, problem solving e auto-miglioramento tra i problemi di ricerca. | `SRC-HIST-002` | fonte primaria | sono obiettivi proposti, non risultati ottenuti |
| `CLM-HIST-004` | Newell e Simon descrivono simboli e ricerca come elementi centrali del loro programma di ricerca e formulano la physical symbol system hypothesis. | `SRC-HIST-004` | fonte primaria | è una tesi degli autori, non una legge universale |
| `CLM-HIST-005` | I sistemi rule-based come MYCIN separano una knowledge base di regole dal meccanismo che le applica e richiedono attività di knowledge engineering. | `SRC-HIST-005` | studio di caso primario | non rappresenta ogni sistema esperto |
| `CLM-HIST-006` | Rosenblatt pubblicò nel 1958 un modello di apprendimento denominato perceptron. | `SRC-HIST-003` | fonte primaria | non coincide con le reti profonde moderne |
| `CLM-HIST-007` | Rumelhart, Hinton e Williams descrivono nel 1986 una procedura che modifica ripetutamente i pesi per ridurre la differenza tra output prodotto e desiderato. | `SRC-HIST-006` | fonte primaria | non è l'unica origine storica della backpropagation |
| `CLM-HIST-008` | Nel lavoro del 1986 le unità nascoste possono apprendere rappresentazioni utili del dominio del compito. | `SRC-HIST-006` | fonte primaria | vale nel quadro sperimentale e teorico descritto |
| `CLM-HIST-009` | Le support vector network del 1995 costituiscono un esempio di apprendimento statistico basato su feature e superficie decisionale. | `SRC-HIST-007` | fonte primaria | esempio, non descrizione esaustiva del periodo |
| `CLM-HIST-010` | LeCun et al. documentano nel 1998 reti convoluzionali addestrate con metodi gradient-based per riconoscimento di documenti. | `SRC-HIST-008` | fonte primaria | dominio specifico |
| `CLM-HIST-011` | Krizhevsky, Sutskever e Hinton addestrano nel 2012 una rete convoluzionale profonda su ImageNet usando una implementazione GPU e riportano il risultato della competizione nel paper. | `SRC-HIST-009` | fonte primaria | risultato specifico al protocollo |
| `CLM-HIST-012` | Il Transformer del 2017 costruisce il blocco principale di sequence transduction con attention, senza recurrence o convoluzioni, e viene descritto come più parallelizzabile dagli autori. | `SRC-HIST-010` | fonte primaria | compiti e architettura del paper originale |
| `CLM-HIST-013` | BERT usa pretraining bidirezionale del Transformer e fine-tuning per più compiti linguistici. | `SRC-HIST-011` | fonte primaria | non rappresenta tutti gli obiettivi di pretraining |
| `CLM-HIST-014` | Kaplan et al. osservano relazioni empiriche a legge di potenza tra loss, dimensione del modello, dati e compute negli esperimenti sui language model descritti. | `SRC-HIST-012` | fonte primaria | relazioni empiriche condizionate al regime studiato |
| `CLM-HIST-015` | GPT-3 viene valutato su compiti zero-shot e few-shot specificati nel contesto testuale senza fine-tuning dei parametri per ciascun task. | `SRC-HIST-013` | fonte primaria | prestazioni e limiti variano per task e dataset |
| `CLM-HIST-016` | Il report del 2021 propone `foundation model` per modelli addestrati su dati ampi e adattabili a molti compiti successivi. | `SRC-HIST-014` | fonte primaria | categoria proposta, non tassonomia universale |
| `CLM-HIST-017` | I paradigmi storici non si sostituiscono completamente: sistemi moderni possono combinare regole, ricerca, modelli appresi, retrieval e strumenti. | sintesi da `SRC-HIST-004`, `005`, `010`, `014` e architettura del libro | sintesi editoriale verificata | formulata come osservazione di composizione, non come legge storica universale |
| `CLM-HIST-018` | La periodizzazione del capitolo usa il collo di bottiglia dominante, rappresentazione, conoscenza, dati, compute o riuso, come strumento didattico. | `PLAN.md` | convenzione editoriale | non è una classificazione storica universale |

## Claim esclusi

Non entrano come fatti:

- `Dartmouth ha inventato l'AI`;
- `il simbolico è stato sostituito dalle reti neurali`;
- `la backpropagation è stata inventata nel 1986`;
- `AlexNet ha creato il deep learning`;
- `il Transformer ha eliminato ogni altra architettura`;
- `più parametri producono sempre capacità migliori`;
- `foundation model è sinonimo di modello generativo o LLM`;
- spiegazioni monocausali delle cosiddette AI winter.
