# Piano interno. Capitolo 55

- Domanda centrale: quale contratto costruisce Fondamenti della multimodalità?
- Oggetto continuo: rappresentazioni di modalità differenti; input guida: testo, immagine, audio e maschere di modalità.
- Prerequisito stabile: Capitolo 54, Aggiornamento, merging ed editing del modello.
- Gap: encoder, proiezione, alignment e fusion.
- Output consegnato: spazio condiviso o output condizionato; consumer successivo: Capitolo 56, Vision encoder e Vision-Language Model.
- Invariante principale: allineamento misurato non equivale a comprensione generale.
- Visuali: FOUNDATION-01 e FOUNDATION-02, con famiglie compositive variabili.
- Snippet: code/snip_55_contract.py; output: code/outputs/SNIP-55-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Modalità e misure

- Ultima affermazione stabile: rappresentazioni di modalità differenti.
- Concetto nuovo: Testo, immagine, audio e azione hanno strutture e scale differenti. Ogni encoder produce una rappresentazione con assi dichiarati.
- Input e shape: testo, immagine, audio e maschere di modalità.
- Operazione: encoder, proiezione, alignment e fusion.
- Output e shape: spazio condiviso o output condizionato.
- Che cosa cambia: il passaggio specifico di «Modalità e misure».
- Invariante: allineamento misurato non equivale a comprensione generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due vettori di modalità proiettati nella stessa dimensione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Allineamento.
- Prova: SRC-55-001 e sezione pubblica corrispondente.

## Transizione 2. Allineamento

- Ultima affermazione stabile: rappresentazioni di modalità differenti.
- Concetto nuovo: Coppie sincronizzate o semanticamente collegate forniscono un segnale comune. Corrispondenza temporale e semantica non coincidono sempre.
- Input e shape: testo, immagine, audio e maschere di modalità.
- Operazione: encoder, proiezione, alignment e fusion.
- Output e shape: spazio condiviso o output condizionato.
- Che cosa cambia: il passaggio specifico di «Allineamento».
- Invariante: allineamento misurato non equivale a comprensione generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due vettori di modalità proiettati nella stessa dimensione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fusion.
- Prova: SRC-55-002 e sezione pubblica corrispondente.

## Transizione 3. Fusion

- Ultima affermazione stabile: rappresentazioni di modalità differenti.
- Concetto nuovo: Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati.
- Input e shape: testo, immagine, audio e maschere di modalità.
- Operazione: encoder, proiezione, alignment e fusion.
- Output e shape: spazio condiviso o output condizionato.
- Che cosa cambia: il passaggio specifico di «Fusion».
- Invariante: allineamento misurato non equivale a comprensione generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due vettori di modalità proiettati nella stessa dimensione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Missing modality.
- Prova: SRC-55-003 e sezione pubblica corrispondente.

## Transizione 4. Missing modality

- Ultima affermazione stabile: rappresentazioni di modalità differenti.
- Concetto nuovo: Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata.
- Input e shape: testo, immagine, audio e maschere di modalità.
- Operazione: encoder, proiezione, alignment e fusion.
- Output e shape: spazio condiviso o output condizionato.
- Che cosa cambia: il passaggio specifico di «Missing modality».
- Invariante: allineamento misurato non equivale a comprensione generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due vettori di modalità proiettati nella stessa dimensione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione.
- Prova: SRC-55-004 e sezione pubblica corrispondente.

## Transizione 5. Valutazione

- Ultima affermazione stabile: rappresentazioni di modalità differenti.
- Concetto nuovo: Comprensione, retrieval, grounding e generazione richiedono benchmark distinti. Una media multimodale può nascondere una modalità debole.
- Input e shape: testo, immagine, audio e maschere di modalità.
- Operazione: encoder, proiezione, alignment e fusion.
- Output e shape: spazio condiviso o output condizionato.
- Che cosa cambia: il passaggio specifico di «Valutazione».
- Invariante: allineamento misurato non equivale a comprensione generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due vettori di modalità proiettati nella stessa dimensione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Vision encoder e Vision-Language Model.
- Prova: SRC-55-001 e sezione pubblica corrispondente.
