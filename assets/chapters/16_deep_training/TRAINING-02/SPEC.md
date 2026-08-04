# Specifica visuale TRAINING-02

- modello compositivo: diagnostic_trace
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Residual e profondità da Regolarizzazione e diagnostica?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il segnale che attraversa una rete profonda
- input: x_l con shape [batch, d] e norma misurata
- output: x_{l+1} con la stessa o con una nuova shape dichiarata
- nodi locali: Residual e profondità: Un residual path conserva un percorso identità e facilita il trasporto di informazione.; Regolarizzazione e diagnostica: Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi.
- limite visualizzato: una somma residuale richiede shape compatibili e non prova da sola stabilità del training
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
