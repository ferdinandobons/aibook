# Specifica visuale MLP-02

- modello compositivo: decision_boundary
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale failure o confronto separa Capacità ed espressività da Dal forward al training?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il vettore di feature x della richiesta
- input: x = [1, 2] con shape [2]
- output: un nuovo vettore h con shape dichiarata
- nodi locali: Capacità ed espressività: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non g.; Dal forward al training: Il forward produce logits e loss.
- limite visualizzato: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
