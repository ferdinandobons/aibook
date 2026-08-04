# Specifica visuale FLASH-01

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Tiling, softmax online e ricomputazione. L'input è tile di Q, K, V, dtype e device, l'output è stesso contratto matematico con memoria e latenza misurate; il vincolo da controllare è che una misura hardware dipende da shape, backend e precisione
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v47.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: FLOP e movimento dei dati; 2: Tiling; 3: Softmax online; 4: Backward e ricomputazione; 5: Backend
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: una misura hardware dipende da shape, backend e precisione
- fonti collegate: SRC-40-001 ... SRC-40-004
- alt text: Diagramma FLASH-01 del Capitolo 40, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Tiling, softmax online e ricomputazione. L'input è tile di Q, K, V, dtype e device, l'output è stesso contratto matematico con memoria e latenza misurate; il vincolo da controllare è che una misura hardware dipende da shape, backend e precisione La composizione usa i passaggi FLOP e movimento dei dati, Tiling, Softmax online, Backward e ricomputazione, Backend.
