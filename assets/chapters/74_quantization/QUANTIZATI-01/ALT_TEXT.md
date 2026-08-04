# Testo alternativo

QUANTIZATI-01, Quantizzazione. Come si passa da «Scala e zero point» a «QAT» mantenendo osservabile un tensore reale e la sua rappresentazione quantizzata? La composizione quantization map collega «Scala e zero point», «PTQ», «QAT». L'input è valori, scale, zero-point, dtype e calibrazione; l'output è codici, tensore ricostruito, errore e memoria. Il limite esplicito è: scala e dominio di calibrazione fanno parte del risultato.
