# Specifica visuale MLP-02

- modello compositivo: decision_boundary
- domanda principale: Quale controllo collega «Capacità ed espressività» a «Dal forward al training» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il vettore di feature x della richiesta
- input: x = [1, 2] con shape [2]
- output: un nuovo vettore h con shape dichiarata
- nodi locali: Capacità ed espressività: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non…; Dal forward al training: Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in…
- limite visualizzato: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
