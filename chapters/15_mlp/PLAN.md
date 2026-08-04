# Piano interno. Capitolo 15

- Domanda centrale: quale contratto costruisce Dal percettrone alle reti multilayer?
- Oggetto continuo: il vettore di feature x della richiesta; input guida: x = [1, 2] con shape [2].
- Prerequisito stabile: Capitolo 14, Reinforcement learning.
- Gap: una trasformazione affine seguita da una funzione di attivazione.
- Output consegnato: un nuovo vettore h con shape dichiarata; consumer successivo: Capitolo 16, Addestrare reti profonde.
- Invariante principale: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Visuali: MLP-01 e MLP-02, con famiglie compositive variabili.
- Snippet: code/snip_15_contract.py; output: code/outputs/SNIP-15-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Una decisione lineare

- Ultima affermazione stabile: il vettore di feature x della richiesta.
- Concetto nuovo: Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature.
- Input e shape: x = [1, 2] con shape [2].
- Operazione: una trasformazione affine seguita da una funzione di attivazione.
- Output e shape: un nuovo vettore h con shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Una decisione lineare».
- Invariante: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: W x + b prima di ReLU, con due coordinate osservabili; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Strati nascosti.
- Prova: SRC-15-001 e sezione pubblica corrispondente.

## Transizione 2. Strati nascosti

- Ultima affermazione stabile: il vettore di feature x della richiesta.
- Concetto nuovo: Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine.
- Input e shape: x = [1, 2] con shape [2].
- Operazione: una trasformazione affine seguita da una funzione di attivazione.
- Output e shape: un nuovo vettore h con shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Strati nascosti».
- Invariante: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: W x + b prima di ReLU, con due coordinate osservabili; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Attivazioni.
- Prova: SRC-15-002 e sezione pubblica corrispondente.

## Transizione 3. Attivazioni

- Ultima affermazione stabile: il vettore di feature x della richiesta.
- Concetto nuovo: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione.
- Input e shape: x = [1, 2] con shape [2].
- Operazione: una trasformazione affine seguita da una funzione di attivazione.
- Output e shape: un nuovo vettore h con shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Attivazioni».
- Invariante: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: W x + b prima di ReLU, con due coordinate osservabili; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Capacità ed espressività.
- Prova: SRC-15-003 e sezione pubblica corrispondente.

## Transizione 4. Capacità ed espressività

- Ultima affermazione stabile: il vettore di feature x della richiesta.
- Concetto nuovo: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile.
- Input e shape: x = [1, 2] con shape [2].
- Operazione: una trasformazione affine seguita da una funzione di attivazione.
- Output e shape: un nuovo vettore h con shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Capacità ed espressività».
- Invariante: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: W x + b prima di ReLU, con due coordinate osservabili; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dal forward al training.
- Prova: SRC-15-004 e sezione pubblica corrispondente.

## Transizione 5. Dal forward al training

- Ultima affermazione stabile: il vettore di feature x della richiesta.
- Concetto nuovo: Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici.
- Input e shape: x = [1, 2] con shape [2].
- Operazione: una trasformazione affine seguita da una funzione di attivazione.
- Output e shape: un nuovo vettore h con shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Dal forward al training».
- Invariante: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: W x + b prima di ReLU, con due coordinate osservabili; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Addestrare reti profonde.
- Prova: SRC-15-001 e sezione pubblica corrispondente.
