# Alt text FLASH-01

Diagramma FLASH-01 del Capitolo 40, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Tiling, softmax online e ricomputazione. L'input è tile di Q, K, V, dtype e device, l'output è stesso contratto matematico con memoria e latenza misurate; il vincolo da controllare è che una misura hardware dipende da shape, backend e precisione La composizione usa i passaggi FLOP e movimento dei dati, Tiling, Softmax online, Backward e ricomputazione, Backend.
