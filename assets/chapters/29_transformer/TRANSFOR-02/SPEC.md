# Specifica visuale TRANSFOR-02

- modello compositivo: tensor_route
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale failure o confronto separa Multi-head attention da Residual stream e output?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato nascosto che attraversa il blocco Transformer
- input: tokenizzati di shape [batch, length] e vettori [batch, length, d]
- output: stato contestuale e logits
- nodi locali: Multi-head attention: Le head applicano proiezioni differenti e vengono concatenate.; Residual stream e output: Layer ripetuti aggiornano il residual stream.
- limite visualizzato: mask, shape e percorso residuale devono essere compatibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
