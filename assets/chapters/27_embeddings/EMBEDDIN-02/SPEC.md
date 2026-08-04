# Specifica visuale EMBEDDIN-02

- modello compositivo: lookup_context
- domanda principale: Quale controllo collega «Sentence embedding» a «Ricerca e anisotropia» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un ID e il vettore che lo rappresenta
- input: due ID, due vettori e una query
- output: embedding, ranking o predizione
- nodi locali: Sentence embedding: Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve…; Ricerca e anisotropia: Cosine similarity è una convenzione, non una misura universale di significato.…
- limite visualizzato: la similarità dipende da training, metrica e normalizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
