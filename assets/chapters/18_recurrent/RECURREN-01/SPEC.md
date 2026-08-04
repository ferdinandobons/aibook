# Specifica visuale RECURREN-01

- modello compositivo: sequence_unroll
- domanda principale: Come si passa da «Uno stato che attraversa la sequenza» a «LSTM e GRU» mantenendo osservabile uno stato nascosto che attraversa una sequenza?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: uno stato nascosto che attraversa una sequenza
- input: x_1, x_2, x_3 e h_0 = 0
- output: h_t e, se richiesto, una predizione per il passo
- nodi locali: Uno stato che attraversa la sequenza: Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di…; Backpropagation through time: Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o…; LSTM e GRU: Gate di input, forget e output controllano il flusso della memoria. GRU usa una…
- limite visualizzato: lo stato precedente deve essere consumato prima di produrre quello successivo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
