# Piano interno. Capitolo 18

- Domanda centrale: quale contratto costruisce Reti ricorrenti e modelli sequenziali?
- Oggetto continuo: uno stato nascosto che attraversa una sequenza; input guida: x_1, x_2, x_3 e h_0 = 0.
- Prerequisito stabile: Capitolo 17, Convolutional network e apprendimento geometrico.
- Gap: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output consegnato: h_t e, se richiesto, una predizione per il passo; consumer successivo: Capitolo 19, Representation learning.
- Invariante principale: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Visuali: RECURREN-01 e RECURREN-02, con famiglie compositive variabili.
- Snippet: code/snip_18_contract.py; output: code/outputs/SNIP-18-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Uno stato che attraversa la sequenza

- Ultima affermazione stabile: uno stato nascosto che attraversa una sequenza.
- Concetto nuovo: Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo.
- Input e shape: x_1, x_2, x_3 e h_0 = 0.
- Operazione: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output e shape: h_t e, se richiesto, una predizione per il passo.
- Che cosa cambia: il passaggio specifico di «Uno stato che attraversa la sequenza».
- Invariante: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti tanh con coefficienti fissi e forma scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Backpropagation through time.
- Prova: SRC-18-001 e sezione pubblica corrispondente.

## Transizione 2. Backpropagation through time

- Ultima affermazione stabile: uno stato nascosto che attraversa una sequenza.
- Concetto nuovo: Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere.
- Input e shape: x_1, x_2, x_3 e h_0 = 0.
- Operazione: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output e shape: h_t e, se richiesto, una predizione per il passo.
- Che cosa cambia: il passaggio specifico di «Backpropagation through time».
- Invariante: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti tanh con coefficienti fissi e forma scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: LSTM e GRU.
- Prova: SRC-18-002 e sezione pubblica corrispondente.

## Transizione 3. LSTM e GRU

- Ultima affermazione stabile: uno stato nascosto che attraversa una sequenza.
- Concetto nuovo: Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente.
- Input e shape: x_1, x_2, x_3 e h_0 = 0.
- Operazione: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output e shape: h_t e, se richiesto, una predizione per il passo.
- Che cosa cambia: il passaggio specifico di «LSTM e GRU».
- Invariante: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti tanh con coefficienti fissi e forma scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Bidirezionalità e causalità.
- Prova: SRC-18-003 e sezione pubblica corrispondente.

## Transizione 4. Bidirezionalità e causalità

- Ultima affermazione stabile: uno stato nascosto che attraversa una sequenza.
- Concetto nuovo: Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming.
- Input e shape: x_1, x_2, x_3 e h_0 = 0.
- Operazione: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output e shape: h_t e, se richiesto, una predizione per il passo.
- Che cosa cambia: il passaggio specifico di «Bidirezionalità e causalità».
- Invariante: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti tanh con coefficienti fissi e forma scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RNN, attention e stato.
- Prova: SRC-18-004 e sezione pubblica corrispondente.

## Transizione 5. RNN, attention e stato

- Ultima affermazione stabile: uno stato nascosto che attraversa una sequenza.
- Concetto nuovo: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari.
- Input e shape: x_1, x_2, x_3 e h_0 = 0.
- Operazione: ogni passo combina input corrente e stato precedente con gli stessi pesi.
- Output e shape: h_t e, se richiesto, una predizione per il passo.
- Che cosa cambia: il passaggio specifico di «RNN, attention e stato».
- Invariante: lo stato precedente deve essere consumato prima di produrre quello successivo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti tanh con coefficienti fissi e forma scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Representation learning.
- Prova: SRC-18-001 e sezione pubblica corrispondente.
