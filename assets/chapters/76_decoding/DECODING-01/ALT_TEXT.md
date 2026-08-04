# Testo alternativo

DECODING-01, Decoding e generazione vincolata. Come si passa da «Greedy e beam search» a «Penalità e stop» mantenendo osservabile logits e spazio delle sequenze ammissibili? La composizione decoding tree collega «Greedy e beam search», «Sampling», «Penalità e stop». L'input è logits, prefisso, temperatura e vincolo; l'output è token scelto, sequenza e metrica di costo. Il limite esplicito è: il decoding modifica la traiettoria, non corregge il modello a monte.
