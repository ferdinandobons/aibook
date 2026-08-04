# Specifica visuale REPLICATIO-02

- modello compositivo: uncertainty_report
- domanda principale: Quale controllo collega «Divergenze» a «Conclusione sostenibile» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un claim di paper e il protocollo necessario per riprodurlo
- input: paper, codice, dati, seed, hardware e metriche
- output: risultato replicato o differenza spiegata
- nodi locali: Divergenze: Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di…; Conclusione sostenibile: Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper…
- limite visualizzato: una replica richiede stesso claim e confini dichiarati, non solo stesso codice
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
