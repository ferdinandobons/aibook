# Piano interno. Capitolo 43

- Domanda centrale: quale contratto costruisce Architetture ibride e memoria interna?
- Oggetto continuo: informazione distribuita tra attenzione locale e memoria; input guida: segmento corrente, stato e memoria persistente.
- Prerequisito stabile: Capitolo 42, State-space model, recurrence e long convolution.
- Gap: write, read, routing e fusione.
- Output consegnato: stato aggiornato e contenuto recuperato; consumer successivo: Capitolo 44, Mixture of Experts e calcolo condizionale.
- Invariante principale: durata e provenienza della memoria devono essere separate.
- Visuali: HYBRID-01 e HYBRID-02, con famiglie compositive variabili.
- Snippet: code/snip_43_contract.py; output: code/outputs/SNIP-43-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Ibridi tra layer

- Ultima affermazione stabile: informazione distribuita tra attenzione locale e memoria.
- Concetto nuovo: Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati.
- Input e shape: segmento corrente, stato e memoria persistente.
- Operazione: write, read, routing e fusione.
- Output e shape: stato aggiornato e contenuto recuperato.
- Che cosa cambia: il passaggio specifico di «Ibridi tra layer».
- Invariante: durata e provenienza della memoria devono essere separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile e due elementi recenti con letture diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Attention locale e stato.
- Prova: SRC-43-001 e sezione pubblica corrispondente.

## Transizione 2. Attention locale e stato

- Ultima affermazione stabile: informazione distribuita tra attenzione locale e memoria.
- Concetto nuovo: Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra.
- Input e shape: segmento corrente, stato e memoria persistente.
- Operazione: write, read, routing e fusione.
- Output e shape: stato aggiornato e contenuto recuperato.
- Che cosa cambia: il passaggio specifico di «Attention locale e stato».
- Invariante: durata e provenienza della memoria devono essere separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile e due elementi recenti con letture diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Memoria segmentale.
- Prova: SRC-43-002 e sezione pubblica corrispondente.

## Transizione 3. Memoria segmentale

- Ultima affermazione stabile: informazione distribuita tra attenzione locale e memoria.
- Concetto nuovo: Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata.
- Input e shape: segmento corrente, stato e memoria persistente.
- Operazione: write, read, routing e fusione.
- Output e shape: stato aggiornato e contenuto recuperato.
- Che cosa cambia: il passaggio specifico di «Memoria segmentale».
- Invariante: durata e provenienza della memoria devono essere separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile e due elementi recenti con letture diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Memoria associativa.
- Prova: SRC-43-003 e sezione pubblica corrispondente.

## Transizione 4. Memoria associativa

- Ultima affermazione stabile: informazione distribuita tra attenzione locale e memoria.
- Concetto nuovo: Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream.
- Input e shape: segmento corrente, stato e memoria persistente.
- Operazione: write, read, routing e fusione.
- Output e shape: stato aggiornato e contenuto recuperato.
- Che cosa cambia: il passaggio specifico di «Memoria associativa».
- Invariante: durata e provenienza della memoria devono essere separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile e due elementi recenti con letture diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Memoria interna ed esterna.
- Prova: SRC-43-004 e sezione pubblica corrispondente.

## Transizione 5. Memoria interna ed esterna

- Ultima affermazione stabile: informazione distribuita tra attenzione locale e memoria.
- Concetto nuovo: Lo stato neurale non coincide con retrieval documentale. Reset, isolamento e provenienza hanno contratti differenti.
- Input e shape: segmento corrente, stato e memoria persistente.
- Operazione: write, read, routing e fusione.
- Output e shape: stato aggiornato e contenuto recuperato.
- Che cosa cambia: il passaggio specifico di «Memoria interna ed esterna».
- Invariante: durata e provenienza della memoria devono essere separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile e due elementi recenti con letture diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Mixture of Experts e calcolo condizionale.
- Prova: SRC-43-001 e sezione pubblica corrispondente.
