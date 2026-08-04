# Testo alternativo

TRAINING-01, Addestrare reti profonde. Come si passa da «Segnali che attraversano molti layer» a «Normalizzazione» mantenendo osservabile il segnale che attraversa una rete profonda? La composizione training loop collega «Segnali che attraversano molti layer», «Inizializzazione», «Normalizzazione». L'input è x_l con shape [batch, d] e norma misurata; l'output è x_{l+1} con la stessa o con una nuova shape dichiarata. Il limite esplicito è: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
