# Specifica visuale MLP-01

- modello compositivo: layer_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale percorso collega Una decisione lineare a Attivazioni nel capitolo 15?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il vettore di feature x della richiesta
- input: x = [1, 2] con shape [2]
- output: un nuovo vettore h con shape dichiarata
- nodi locali: Una decisione lineare: Il percettrone combina feature con pesi e bias.; Strati nascosti: Una MLP alterna trasformazioni affini e funzioni non lineari.; Attivazioni: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità.
- limite visualizzato: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
