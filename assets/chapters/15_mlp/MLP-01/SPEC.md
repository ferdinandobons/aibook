# Specifica visuale MLP-01

- modello compositivo: layer_stack
- domanda principale: Come si passa da «Una decisione lineare» a «Attivazioni» mantenendo osservabile il vettore di feature x della richiesta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il vettore di feature x della richiesta
- input: x = [1, 2] con shape [2]
- output: un nuovo vettore h con shape dichiarata
- nodi locali: Una decisione lineare: Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello…; Strati nascosti: Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più…; Attivazioni: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta…
- limite visualizzato: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
