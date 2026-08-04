# Testo alternativo

TRANSFOR-01, Il Transformer da zero. Come si passa da «La mappa completa» a «Decoder» mantenendo osservabile lo stato nascosto che attraversa il blocco Transformer? La composizione transformer stack collega «La mappa completa», «Encoder», «Decoder». L'input è tokenizzati di shape [batch, length] e vettori [batch, length, d]; l'output è stato contestuale e logits. Il limite esplicito è: mask, shape e percorso residuale devono essere compatibili.
