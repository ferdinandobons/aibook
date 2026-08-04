# Piano interno. Capitolo 35

- Domanda centrale: quale contratto costruisce La ricetta di pretraining?
- Oggetto continuo: lo stato completo di una ricetta di pretraining; input guida: batch, learning rate, seed, optimizer e checkpoint.
- Prerequisito stabile: Capitolo 34, Scaling law e progettazione del modello.
- Gap: forward, backward, update, schedule e recovery.
- Output consegnato: loss, parametri e checkpoint ripristinabile; consumer successivo: Capitolo 36, Training distribuito e continued pretraining.
- Invariante principale: un checkpoint deve includere lo stato necessario a continuare il run.
- Visuali: RECIPE-01 e RECIPE-02, con famiglie compositive variabili.
- Snippet: code/snip_35_contract.py; output: code/outputs/SNIP-35-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Batch di token

- Ultima affermazione stabile: lo stato completo di una ricetta di pretraining.
- Concetto nuovo: Packing, padding e mask determinano quanti token validi contribuiscono alla loss.
- Input e shape: batch, learning rate, seed, optimizer e checkpoint.
- Operazione: forward, backward, update, schedule e recovery.
- Output e shape: loss, parametri e checkpoint ripristinabile.
- Che cosa cambia: il passaggio specifico di «Batch di token».
- Invariante: un checkpoint deve includere lo stato necessario a continuare il run.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: warmup di quattro step e ripresa dal contatore salvato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Inizializzazione.
- Prova: SRC-35-001 e sezione pubblica corrispondente.

## Transizione 2. Inizializzazione

- Ultima affermazione stabile: lo stato completo di una ricetta di pretraining.
- Concetto nuovo: Scala dei pesi e residual deve restare coerente con profondità, norm e dtype.
- Input e shape: batch, learning rate, seed, optimizer e checkpoint.
- Operazione: forward, backward, update, schedule e recovery.
- Output e shape: loss, parametri e checkpoint ripristinabile.
- Che cosa cambia: il passaggio specifico di «Inizializzazione».
- Invariante: un checkpoint deve includere lo stato necessario a continuare il run.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: warmup di quattro step e ripresa dal contatore salvato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: AdamW.
- Prova: SRC-35-002 e sezione pubblica corrispondente.

## Transizione 3. AdamW

- Ultima affermazione stabile: lo stato completo di una ricetta di pretraining.
- Concetto nuovo: Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer.
- Input e shape: batch, learning rate, seed, optimizer e checkpoint.
- Operazione: forward, backward, update, schedule e recovery.
- Output e shape: loss, parametri e checkpoint ripristinabile.
- Che cosa cambia: il passaggio specifico di «AdamW».
- Invariante: un checkpoint deve includere lo stato necessario a continuare il run.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: warmup di quattro step e ripresa dal contatore salvato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Warmup e schedule.
- Prova: SRC-35-003 e sezione pubblica corrispondente.

## Transizione 4. Warmup e schedule

- Ultima affermazione stabile: lo stato completo di una ricetta di pretraining.
- Concetto nuovo: Il learning rate dipende da step o token e deve riprendere dal contatore corretto.
- Input e shape: batch, learning rate, seed, optimizer e checkpoint.
- Operazione: forward, backward, update, schedule e recovery.
- Output e shape: loss, parametri e checkpoint ripristinabile.
- Che cosa cambia: il passaggio specifico di «Warmup e schedule».
- Invariante: un checkpoint deve includere lo stato necessario a continuare il run.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: warmup di quattro step e ripresa dal contatore salvato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Checkpoint e recovery.
- Prova: SRC-35-004 e sezione pubblica corrispondente.

## Transizione 5. Checkpoint e recovery

- Ultima affermazione stabile: lo stato completo di una ricetta di pretraining.
- Concetto nuovo: Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele.
- Input e shape: batch, learning rate, seed, optimizer e checkpoint.
- Operazione: forward, backward, update, schedule e recovery.
- Output e shape: loss, parametri e checkpoint ripristinabile.
- Che cosa cambia: il passaggio specifico di «Checkpoint e recovery».
- Invariante: un checkpoint deve includere lo stato necessario a continuare il run.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: warmup di quattro step e ripresa dal contatore salvato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Training distribuito e continued pretraining.
- Prova: SRC-35-001 e sezione pubblica corrispondente.
