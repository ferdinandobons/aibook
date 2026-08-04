# Piano interno. Capitolo 47

- Domanda centrale: quale contratto costruisce Fine-tuning efficiente?
- Oggetto continuo: l'aggiornamento adattivo rispetto ai pesi congelati; input guida: peso W, matrice A e B, rank e quantizzazione.
- Prerequisito stabile: Capitolo 46, Supervised fine-tuning e instruction tuning.
- Gap: adapter, LoRA, prefix o QLoRA.
- Output consegnato: delta W e checkpoint adattatore; consumer successivo: Capitolo 48, Preferenze, reward model e RLHF.
- Invariante principale: il delta non è il modello completo e va valutato sullo stesso base model.
- Visuali: PEFT-01 e PEFT-02, con famiglie compositive variabili.
- Snippet: code/snip_47_contract.py; output: code/outputs/SNIP-47-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Parametri congelati e adattamento

- Ultima affermazione stabile: l'aggiornamento adattivo rispetto ai pesi congelati.
- Concetto nuovo: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint.
- Input e shape: peso W, matrice A e B, rank e quantizzazione.
- Operazione: adapter, LoRA, prefix o QLoRA.
- Output e shape: delta W e checkpoint adattatore.
- Che cosa cambia: il passaggio specifico di «Parametri congelati e adattamento».
- Invariante: il delta non è il modello completo e va valutato sullo stesso base model.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: delta W = B A con rank uno su una matrice piccola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Adapter.
- Prova: SRC-47-001 e sezione pubblica corrispondente.

## Transizione 2. Adapter

- Ultima affermazione stabile: l'aggiornamento adattivo rispetto ai pesi congelati.
- Concetto nuovo: Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base.
- Input e shape: peso W, matrice A e B, rank e quantizzazione.
- Operazione: adapter, LoRA, prefix o QLoRA.
- Output e shape: delta W e checkpoint adattatore.
- Che cosa cambia: il passaggio specifico di «Adapter».
- Invariante: il delta non è il modello completo e va valutato sullo stesso base model.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: delta W = B A con rank uno su una matrice piccola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: LoRA.
- Prova: SRC-47-002 e sezione pubblica corrispondente.

## Transizione 3. LoRA

- Ultima affermazione stabile: l'aggiornamento adattivo rispetto ai pesi congelati.
- Concetto nuovo: Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference.
- Input e shape: peso W, matrice A e B, rank e quantizzazione.
- Operazione: adapter, LoRA, prefix o QLoRA.
- Output e shape: delta W e checkpoint adattatore.
- Che cosa cambia: il passaggio specifico di «LoRA».
- Invariante: il delta non è il modello completo e va valutato sullo stesso base model.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: delta W = B A con rank uno su una matrice piccola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prompt, prefix e IA3.
- Prova: SRC-47-003 e sezione pubblica corrispondente.

## Transizione 4. Prompt, prefix e IA3

- Ultima affermazione stabile: l'aggiornamento adattivo rispetto ai pesi congelati.
- Concetto nuovo: Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti.
- Input e shape: peso W, matrice A e B, rank e quantizzazione.
- Operazione: adapter, LoRA, prefix o QLoRA.
- Output e shape: delta W e checkpoint adattatore.
- Che cosa cambia: il passaggio specifico di «Prompt, prefix e IA3».
- Invariante: il delta non è il modello completo e va valutato sullo stesso base model.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: delta W = B A con rank uno su una matrice piccola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: QLoRA e compatibilità.
- Prova: SRC-47-004 e sezione pubblica corrispondente.

## Transizione 5. QLoRA e compatibilità

- Ultima affermazione stabile: l'aggiornamento adattivo rispetto ai pesi congelati.
- Concetto nuovo: Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere.
- Input e shape: peso W, matrice A e B, rank e quantizzazione.
- Operazione: adapter, LoRA, prefix o QLoRA.
- Output e shape: delta W e checkpoint adattatore.
- Che cosa cambia: il passaggio specifico di «QLoRA e compatibilità».
- Invariante: il delta non è il modello completo e va valutato sullo stesso base model.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: delta W = B A con rank uno su una matrice piccola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Preferenze, reward model e RLHF.
- Prova: SRC-47-001 e sezione pubblica corrispondente.
