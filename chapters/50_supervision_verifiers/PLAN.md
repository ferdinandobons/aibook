# Piano interno. Capitolo 50

- Domanda centrale: quale contratto costruisce Process supervision, outcome supervision e verifier?
- Oggetto continuo: una traiettoria e il segnale di un verifier; input guida: passaggi, risposta finale, criterio e indipendenza.
- Prerequisito stabile: Capitolo 49, Ottimizzazione diretta delle preferenze.
- Gap: process supervision, outcome supervision e verifica.
- Output consegnato: score verificato e failure localizzata; consumer successivo: Capitolo 51, Reinforcement learning con reward verificabili.
- Invariante principale: un verifier può ereditare bias o essere ottimizzato.
- Visuali: VERIFIERS-01 e VERIFIERS-02, con famiglie compositive variabili.
- Snippet: code/snip_50_contract.py; output: code/outputs/SNIP-50-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Supervisionare il risultato

- Ultima affermazione stabile: una traiettoria e il segnale di un verifier.
- Concetto nuovo: Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore.
- Input e shape: passaggi, risposta finale, criterio e indipendenza.
- Operazione: process supervision, outcome supervision e verifica.
- Output e shape: score verificato e failure localizzata.
- Che cosa cambia: il passaggio specifico di «Supervisionare il risultato».
- Invariante: un verifier può ereditare bias o essere ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso risultato finale con un passaggio corretto e uno scorretto; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Supervisionare il processo.
- Prova: SRC-50-001 e sezione pubblica corrispondente.

## Transizione 2. Supervisionare il processo

- Ultima affermazione stabile: una traiettoria e il segnale di un verifier.
- Concetto nuovo: Process supervision etichetta passaggi intermedi. La validità dipende da come il processo viene reso osservabile e annotato.
- Input e shape: passaggi, risposta finale, criterio e indipendenza.
- Operazione: process supervision, outcome supervision e verifica.
- Output e shape: score verificato e failure localizzata.
- Che cosa cambia: il passaggio specifico di «Supervisionare il processo».
- Invariante: un verifier può ereditare bias o essere ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso risultato finale con un passaggio corretto e uno scorretto; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Verifier.
- Prova: SRC-50-002 e sezione pubblica corrispondente.

## Transizione 3. Verifier

- Ultima affermazione stabile: una traiettoria e il segnale di un verifier.
- Concetto nuovo: Un verifier valuta candidate rispetto a un criterio. Può essere una regola, un esecutore, un modello o una combinazione.
- Input e shape: passaggi, risposta finale, criterio e indipendenza.
- Operazione: process supervision, outcome supervision e verifica.
- Output e shape: score verificato e failure localizzata.
- Che cosa cambia: il passaggio specifico di «Verifier».
- Invariante: un verifier può ereditare bias o essere ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso risultato finale con un passaggio corretto e uno scorretto; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reward model di processo.
- Prova: SRC-50-003 e sezione pubblica corrispondente.

## Transizione 4. Reward model di processo

- Ultima affermazione stabile: una traiettoria e il segnale di un verifier.
- Concetto nuovo: Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento.
- Input e shape: passaggi, risposta finale, criterio e indipendenza.
- Operazione: process supervision, outcome supervision e verifica.
- Output e shape: score verificato e failure localizzata.
- Che cosa cambia: il passaggio specifico di «Reward model di processo».
- Invariante: un verifier può ereditare bias o essere ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso risultato finale con un passaggio corretto e uno scorretto; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Goodhart e indipendenza.
- Prova: SRC-50-004 e sezione pubblica corrispondente.

## Transizione 5. Goodhart e indipendenza

- Ultima affermazione stabile: una traiettoria e il segnale di un verifier.
- Concetto nuovo: Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting. Servono test e verificatori indipendenti.
- Input e shape: passaggi, risposta finale, criterio e indipendenza.
- Operazione: process supervision, outcome supervision e verifica.
- Output e shape: score verificato e failure localizzata.
- Che cosa cambia: il passaggio specifico di «Goodhart e indipendenza».
- Invariante: un verifier può ereditare bias o essere ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso risultato finale con un passaggio corretto e uno scorretto; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reinforcement learning con reward verificabili.
- Prova: SRC-50-001 e sezione pubblica corrispondente.
