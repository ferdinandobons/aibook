# Specifica visuale UPDATE-01

- modello compositivo: model_edit
- domanda principale: Come si passa da «Continued adaptation» a «TIES e DARE» mantenendo osservabile versioni di pesi e modifiche localizzate del modello?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: versioni di pesi e modifiche localizzate del modello
- input: base model, delta, task e rollback point
- output: versione nuova, diff e test di regressione
- nodi locali: Continued adaptation: Nuovi dati e obiettivi aggiornano il checkpoint. Replay, regolarizzazione e valutazioni…; Task arithmetic: Differenze tra checkpoint possono essere combinate come vettori. La compatibilità…; TIES e DARE: Metodi di merging riducono interferenze mediante selezione, segni o sparsificazione. I…
- limite visualizzato: un merge senza valutazione può introdurre regressioni invisibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
