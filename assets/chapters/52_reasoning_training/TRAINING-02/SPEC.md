# Specifica visuale TRAINING-02

- modello compositivo: mode_fusion
- domanda principale: Quale controllo collega «Faithfulness» a «Costo e lunghezza» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traccia di reasoning e la risposta che la segue
- input: prompt, trace del teacher, answer e costo in token
- output: traccia selezionata, risposta e misura di costo
- nodi locali: Faithfulness: Una spiegazione corretta può essere post-hoc. Valutare risposta e fedeltà richiede…; Costo e lunghezza: Tracce più lunghe aumentano token e latenza. Il training deve distinguere utilità della…
- limite visualizzato: una traccia leggibile non prova faithfulness causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
