# Piano interno. Capitolo 16

- Domanda centrale: quale contratto costruisce Addestrare reti profonde?
- Oggetto continuo: il segnale che attraversa una rete profonda; input guida: x_l con shape [batch, d] e norma misurata.
- Prerequisito stabile: Capitolo 15, Dal percettrone alle reti multilayer.
- Gap: un blocco, una normalizzazione o un percorso residuale.
- Output consegnato: x_{l+1} con la stessa o con una nuova shape dichiarata; consumer successivo: Capitolo 17, Convolutional network e apprendimento geometrico.
- Invariante principale: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Visuali: TRAINING-01 e TRAINING-02, con famiglie compositive variabili.
- Snippet: code/snip_16_contract.py; output: code/outputs/SNIP-16-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Segnali che attraversano molti layer

- Ultima affermazione stabile: il segnale che attraversa una rete profonda.
- Concetto nuovo: Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata.
- Input e shape: x_l con shape [batch, d] e norma misurata.
- Operazione: un blocco, una normalizzazione o un percorso residuale.
- Output e shape: x_{l+1} con la stessa o con una nuova shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Segnali che attraversano molti layer».
- Invariante: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: x + F(x) con due vettori di dimensione 2; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Inizializzazione.
- Prova: SRC-16-001 e sezione pubblica corrispondente.

## Transizione 2. Inizializzazione

- Ultima affermazione stabile: il segnale che attraversa una rete profonda.
- Concetto nuovo: Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate.
- Input e shape: x_l con shape [batch, d] e norma misurata.
- Operazione: un blocco, una normalizzazione o un percorso residuale.
- Output e shape: x_{l+1} con la stessa o con una nuova shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Inizializzazione».
- Invariante: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: x + F(x) con due vettori di dimensione 2; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Normalizzazione.
- Prova: SRC-16-002 e sezione pubblica corrispondente.

## Transizione 3. Normalizzazione

- Ultima affermazione stabile: il segnale che attraversa una rete profonda.
- Concetto nuovo: BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura.
- Input e shape: x_l con shape [batch, d] e norma misurata.
- Operazione: un blocco, una normalizzazione o un percorso residuale.
- Output e shape: x_{l+1} con la stessa o con una nuova shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Normalizzazione».
- Invariante: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: x + F(x) con due vettori di dimensione 2; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Residual e profondità.
- Prova: SRC-16-003 e sezione pubblica corrispondente.

## Transizione 4. Residual e profondità

- Ultima affermazione stabile: il segnale che attraversa una rete profonda.
- Concetto nuovo: Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata.
- Input e shape: x_l con shape [batch, d] e norma misurata.
- Operazione: un blocco, una normalizzazione o un percorso residuale.
- Output e shape: x_{l+1} con la stessa o con una nuova shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Residual e profondità».
- Invariante: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: x + F(x) con due vettori di dimensione 2; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Regolarizzazione e diagnostica.
- Prova: SRC-16-004 e sezione pubblica corrispondente.

## Transizione 5. Regolarizzazione e diagnostica

- Ultima affermazione stabile: il segnale che attraversa una rete profonda.
- Concetto nuovo: Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità.
- Input e shape: x_l con shape [batch, d] e norma misurata.
- Operazione: un blocco, una normalizzazione o un percorso residuale.
- Output e shape: x_{l+1} con la stessa o con una nuova shape dichiarata.
- Che cosa cambia: il passaggio specifico di «Regolarizzazione e diagnostica».
- Invariante: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: x + F(x) con due vettori di dimensione 2; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Convolutional network e apprendimento geometrico.
- Prova: SRC-16-001 e sezione pubblica corrispondente.
