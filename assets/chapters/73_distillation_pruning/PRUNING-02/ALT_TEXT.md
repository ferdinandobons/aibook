# Testo alternativo

PRUNING-02, Distillazione e pruning. Quale controllo collega «Pruning» a «Recovery» senza superare il limite dichiarato? La composizione quality gate collega «Pruning», «Recovery». L'input è logits teacher, target, pruning mask e budget; l'output è student più piccolo con loss e regressioni misurate. Il limite esplicito è: compressione e accuratezza vanno misurate sullo stesso perimetro.
