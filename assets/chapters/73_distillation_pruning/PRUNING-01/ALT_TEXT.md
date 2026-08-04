# Testo alternativo

PRUNING-01, Distillazione e pruning. Come si passa da «Teacher e student» a «Sequence distillation» mantenendo osservabile pesi del teacher, student e struttura da comprimere? La composizione distill prune collega «Teacher e student», «Temperature e loss», «Sequence distillation». L'input è logits teacher, target, pruning mask e budget; l'output è student più piccolo con loss e regressioni misurate. Il limite esplicito è: compressione e accuratezza vanno misurate sullo stesso perimetro.
