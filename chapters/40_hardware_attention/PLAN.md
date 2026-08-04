# Piano interno. Capitolo 40

- Domanda centrale: quale contratto costruisce Attention hardware-aware?
- Oggetto continuo: il calcolo dell'attention e il suo movimento di dati; input guida: tile di Q, K, V, dtype e device.
- Prerequisito stabile: Capitolo 39, Varianti dell'attention e gestione KV.
- Gap: tiling, softmax online e ricomputazione.
- Output consegnato: stesso contratto matematico con memoria e latenza misurate; consumer successivo: Capitolo 41, Linear attention, fast weights e delta rule.
- Invariante principale: una misura hardware dipende da shape, backend e precisione.
- Visuali: FLASH-01 e FLASH-02, con famiglie compositive variabili.
- Snippet: code/snip_40_contract.py; output: code/outputs/SNIP-40-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. FLOP e movimento dei dati

- Ultima affermazione stabile: il calcolo dell'attention e il suo movimento di dati.
- Concetto nuovo: Lo stesso operatore può avere traffico di memoria molto diverso.
- Input e shape: tile di Q, K, V, dtype e device.
- Operazione: tiling, softmax online e ricomputazione.
- Output e shape: stesso contratto matematico con memoria e latenza misurate.
- Che cosa cambia: il passaggio specifico di «FLOP e movimento dei dati».
- Invariante: una misura hardware dipende da shape, backend e precisione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: softmax stabile su due tile con massimo per riga; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Tiling.
- Prova: SRC-40-001 e sezione pubblica corrispondente.

## Transizione 2. Tiling

- Ultima affermazione stabile: il calcolo dell'attention e il suo movimento di dati.
- Concetto nuovo: Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score.
- Input e shape: tile di Q, K, V, dtype e device.
- Operazione: tiling, softmax online e ricomputazione.
- Output e shape: stesso contratto matematico con memoria e latenza misurate.
- Che cosa cambia: il passaggio specifico di «Tiling».
- Invariante: una misura hardware dipende da shape, backend e precisione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: softmax stabile su due tile con massimo per riga; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Softmax online.
- Prova: SRC-40-002 e sezione pubblica corrispondente.

## Transizione 3. Softmax online

- Ultima affermazione stabile: il calcolo dell'attention e il suo movimento di dati.
- Concetto nuovo: Massimo, denominatore e numeratore vengono aggiornati blocco per blocco.
- Input e shape: tile di Q, K, V, dtype e device.
- Operazione: tiling, softmax online e ricomputazione.
- Output e shape: stesso contratto matematico con memoria e latenza misurate.
- Che cosa cambia: il passaggio specifico di «Softmax online».
- Invariante: una misura hardware dipende da shape, backend e precisione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: softmax stabile su due tile con massimo per riga; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Backward e ricomputazione.
- Prova: SRC-40-003 e sezione pubblica corrispondente.

## Transizione 4. Backward e ricomputazione

- Ultima affermazione stabile: il calcolo dell'attention e il suo movimento di dati.
- Concetto nuovo: Salvare meno intermedi scambia memoria con compute aggiuntivo.
- Input e shape: tile di Q, K, V, dtype e device.
- Operazione: tiling, softmax online e ricomputazione.
- Output e shape: stesso contratto matematico con memoria e latenza misurate.
- Che cosa cambia: il passaggio specifico di «Backward e ricomputazione».
- Invariante: una misura hardware dipende da shape, backend e precisione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: softmax stabile su due tile con massimo per riga; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Backend.
- Prova: SRC-40-004 e sezione pubblica corrispondente.

## Transizione 5. Backend

- Ultima affermazione stabile: il calcolo dell'attention e il suo movimento di dati.
- Concetto nuovo: FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse.
- Input e shape: tile di Q, K, V, dtype e device.
- Operazione: tiling, softmax online e ricomputazione.
- Output e shape: stesso contratto matematico con memoria e latenza misurate.
- Che cosa cambia: il passaggio specifico di «Backend».
- Invariante: una misura hardware dipende da shape, backend e precisione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: softmax stabile su due tile con massimo per riga; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Linear attention, fast weights e delta rule.
- Prova: SRC-40-001 e sezione pubblica corrispondente.
