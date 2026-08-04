# Testo alternativo

TRAINING-02, Addestrare reti profonde. Quale controllo collega «Residual e profondità» a «Regolarizzazione e diagnostica» senza superare il limite dichiarato? La composizione diagnostic trace collega «Residual e profondità», «Regolarizzazione e diagnostica». L'input è x_l con shape [batch, d] e norma misurata; l'output è x_{l+1} con la stessa o con una nuova shape dichiarata. Il limite esplicito è: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.
