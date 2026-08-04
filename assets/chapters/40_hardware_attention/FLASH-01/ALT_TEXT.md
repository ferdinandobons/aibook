# Testo alternativo

FLASH-01, Attention hardware-aware. Come si passa da «FLOP e movimento dei dati» a «Softmax online» mantenendo osservabile il calcolo dell'attention e il suo movimento di dati? La composizione memory tiling collega «FLOP e movimento dei dati», «Tiling», «Softmax online». L'input è tile di Q, K, V, dtype e device; l'output è stesso contratto matematico con memoria e latenza misurate. Il limite esplicito è: una misura hardware dipende da shape, backend e precisione.
