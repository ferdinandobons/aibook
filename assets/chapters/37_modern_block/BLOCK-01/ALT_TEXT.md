# Testo alternativo

BLOCK-01, Anatomia del blocco moderno. Come si passa da «Residual stream» a «RMSNorm» mantenendo osservabile un residual stream dentro un blocco moderno? La composizione block compare collega «Residual stream», «Pre-norm e post-norm», «RMSNorm». L'input è h di shape [batch, length, d] e norma misurata; l'output è h' con shape preservata e statistiche confrontabili. Il limite esplicito è: ordine dei sottolayer e shape sono parte del blocco.
