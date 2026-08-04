# Testo alternativo

RECURREN-01, Reti ricorrenti e modelli sequenziali. Come si passa da «Uno stato che attraversa la sequenza» a «LSTM e GRU» mantenendo osservabile uno stato nascosto che attraversa una sequenza? La composizione sequence unroll collega «Uno stato che attraversa la sequenza», «Backpropagation through time», «LSTM e GRU». L'input è x_1, x_2, x_3 e h_0 = 0; l'output è h_t e, se richiesto, una predizione per il passo. Il limite esplicito è: lo stato precedente deve essere consumato prima di produrre quello successivo.
