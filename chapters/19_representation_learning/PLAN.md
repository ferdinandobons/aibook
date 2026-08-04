# Piano interno. Capitolo 19

- Domanda centrale: quale contratto costruisce Representation learning?
- Oggetto continuo: un vettore prodotto per un compito successivo; input guida: u = [1, 2, 0] e v = [2, 1, 0].
- Prerequisito stabile: Capitolo 18, Reti ricorrenti e modelli sequenziali.
- Gap: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output consegnato: un vettore, una similarità o una predizione downstream; consumer successivo: Capitolo 20, Fondamenti della modellazione generativa.
- Invariante principale: la geometria dipende da dati, obiettivo e normalizzazione.
- Visuali: REPRESEN-01 e REPRESEN-02, con famiglie compositive variabili.
- Snippet: code/snip_19_contract.py; output: code/outputs/SNIP-19-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Che cosa rappresenta un vettore

- Ultima affermazione stabile: un vettore prodotto per un compito successivo.
- Concetto nuovo: Una rappresentazione è un insieme di quantità prodotte dal modello e usate da un calcolo successivo. Il significato dipende da obiettivo e dati.
- Input e shape: u = [1, 2, 0] e v = [2, 1, 0].
- Operazione: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output e shape: un vettore, una similarità o una predizione downstream.
- Che cosa cambia: il passaggio specifico di «Che cosa rappresenta un vettore».
- Invariante: la geometria dipende da dati, obiettivo e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno calcolata dopo la normalizzazione delle norme; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Bottleneck e autoencoder.
- Prova: SRC-19-001 e sezione pubblica corrispondente.

## Transizione 2. Bottleneck e autoencoder

- Ultima affermazione stabile: un vettore prodotto per un compito successivo.
- Concetto nuovo: Un autoencoder comprime e ricostruisce. Un bottleneck limita la capacità, ma non garantisce che le coordinate corrispondano a fattori interpretabili.
- Input e shape: u = [1, 2, 0] e v = [2, 1, 0].
- Operazione: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output e shape: un vettore, una similarità o una predizione downstream.
- Che cosa cambia: il passaggio specifico di «Bottleneck e autoencoder».
- Invariante: la geometria dipende da dati, obiettivo e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno calcolata dopo la normalizzazione delle norme; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metric e contrastive learning.
- Prova: SRC-19-002 e sezione pubblica corrispondente.

## Transizione 3. Metric e contrastive learning

- Ultima affermazione stabile: un vettore prodotto per un compito successivo.
- Concetto nuovo: Obiettivi contrastivi avvicinano coppie positive e separano alternative. La definizione delle coppie e delle augmentazioni stabilisce le invarianti apprese.
- Input e shape: u = [1, 2, 0] e v = [2, 1, 0].
- Operazione: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output e shape: un vettore, una similarità o una predizione downstream.
- Che cosa cambia: il passaggio specifico di «Metric e contrastive learning».
- Invariante: la geometria dipende da dati, obiettivo e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno calcolata dopo la normalizzazione delle norme; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Disentanglement e identifiability.
- Prova: SRC-19-003 e sezione pubblica corrispondente.

## Transizione 4. Disentanglement e identifiability

- Ultima affermazione stabile: un vettore prodotto per un compito successivo.
- Concetto nuovo: Separare fattori latenti richiede ipotesi. Senza supervision o bias aggiuntivi, molte rappresentazioni equivalenti possono spiegare gli stessi dati.
- Input e shape: u = [1, 2, 0] e v = [2, 1, 0].
- Operazione: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output e shape: un vettore, una similarità o una predizione downstream.
- Che cosa cambia: il passaggio specifico di «Disentanglement e identifiability».
- Invariante: la geometria dipende da dati, obiettivo e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno calcolata dopo la normalizzazione delle norme; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutare una rappresentazione.
- Prova: SRC-19-004 e sezione pubblica corrispondente.

## Transizione 5. Valutare una rappresentazione

- Ultima affermazione stabile: un vettore prodotto per un compito successivo.
- Concetto nuovo: Linear probe, retrieval e fine-tuning misurano proprietà diverse. Una buona metrica downstream non dimostra interpretabilità globale.
- Input e shape: u = [1, 2, 0] e v = [2, 1, 0].
- Operazione: una proiezione, una ricostruzione o una metrica tra rappresentazioni.
- Output e shape: un vettore, una similarità o una predizione downstream.
- Che cosa cambia: il passaggio specifico di «Valutare una rappresentazione».
- Invariante: la geometria dipende da dati, obiettivo e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno calcolata dopo la normalizzazione delle norme; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fondamenti della modellazione generativa.
- Prova: SRC-19-001 e sezione pubblica corrispondente.
