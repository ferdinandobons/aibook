# Piano interno. Capitolo 34

- Domanda centrale: quale contratto costruisce Scaling law e progettazione del modello?
- Oggetto continuo: una curva empirica tra scala, compute e loss; input guida: punti con parametri, token, FLOP e loss.
- Prerequisito stabile: Capitolo 33, Dataset mixture, curriculum e dati sintetici.
- Gap: fit, confronto isoFLOP ed estrapolazione.
- Output consegnato: stima con intervallo osservato e costo; consumer successivo: Capitolo 35, La ricetta di pretraining.
- Invariante principale: un fit fuori dominio non è una legge garantita.
- Visuali: SCALE-01 e SCALE-02, con famiglie compositive variabili.
- Snippet: code/snip_34_contract.py; output: code/outputs/SNIP-34-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Fit empirico

- Ultima affermazione stabile: una curva empirica tra scala, compute e loss.
- Concetto nuovo: Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato.
- Input e shape: punti con parametri, token, FLOP e loss.
- Operazione: fit, confronto isoFLOP ed estrapolazione.
- Output e shape: stima con intervallo osservato e costo.
- Che cosa cambia: il passaggio specifico di «Fit empirico».
- Invariante: un fit fuori dominio non è una legge garantita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro punti, fit lineare locale e intervallo dichiarato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Allocazione compute-optimal.
- Prova: SRC-34-001 e sezione pubblica corrispondente.

## Transizione 2. Allocazione compute-optimal

- Ultima affermazione stabile: una curva empirica tra scala, compute e loss.
- Concetto nuovo: A budget fissato, modello e token competono. Il risultato dipende da ricetta e qualità dei dati.
- Input e shape: punti con parametri, token, FLOP e loss.
- Operazione: fit, confronto isoFLOP ed estrapolazione.
- Output e shape: stima con intervallo osservato e costo.
- Che cosa cambia: il passaggio specifico di «Allocazione compute-optimal».
- Invariante: un fit fuori dominio non è una legge garantita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro punti, fit lineare locale e intervallo dichiarato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Esperimenti isoFLOP.
- Prova: SRC-34-002 e sezione pubblica corrispondente.

## Transizione 3. Esperimenti isoFLOP

- Ultima affermazione stabile: una curva empirica tra scala, compute e loss.
- Concetto nuovo: Configurazioni con compute simile rendono osservabile la loss minima per budget.
- Input e shape: punti con parametri, token, FLOP e loss.
- Operazione: fit, confronto isoFLOP ed estrapolazione.
- Output e shape: stima con intervallo osservato e costo.
- Che cosa cambia: il passaggio specifico di «Esperimenti isoFLOP».
- Invariante: un fit fuori dominio non è una legge garantita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro punti, fit lineare locale e intervallo dichiarato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Extrapolation.
- Prova: SRC-34-003 e sezione pubblica corrispondente.

## Transizione 4. Extrapolation

- Ultima affermazione stabile: una curva empirica tra scala, compute e loss.
- Concetto nuovo: Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala.
- Input e shape: punti con parametri, token, FLOP e loss.
- Operazione: fit, confronto isoFLOP ed estrapolazione.
- Output e shape: stima con intervallo osservato e costo.
- Che cosa cambia: il passaggio specifico di «Extrapolation».
- Invariante: un fit fuori dominio non è una legge garantita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro punti, fit lineare locale e intervallo dichiarato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Training e inference cost.
- Prova: SRC-34-004 e sezione pubblica corrispondente.

## Transizione 5. Training e inference cost

- Ultima affermazione stabile: una curva empirica tra scala, compute e loss.
- Concetto nuovo: Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio.
- Input e shape: punti con parametri, token, FLOP e loss.
- Operazione: fit, confronto isoFLOP ed estrapolazione.
- Output e shape: stima con intervallo osservato e costo.
- Che cosa cambia: il passaggio specifico di «Training e inference cost».
- Invariante: un fit fuori dominio non è una legge garantita.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: quattro punti, fit lineare locale e intervallo dichiarato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: La ricetta di pretraining.
- Prova: SRC-34-001 e sezione pubblica corrispondente.
