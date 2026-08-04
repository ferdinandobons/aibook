# Testo alternativo

ALT-01, Byte, predizione multi-token e language diffusion. Come si passa da «Byte e caratteri» a «Predizione multi-token» mantenendo osservabile unità di predizione dal byte al token multiplo? La composizione objective compare collega «Byte e caratteri», «Gerarchie di byte», «Predizione multi-token». L'input è byte, gerarchia, target e numero di passi; l'output è unità predette, loss e durata di decoding. Il limite esplicito è: granularità della rappresentazione e parallelismo sono assi distinti.
