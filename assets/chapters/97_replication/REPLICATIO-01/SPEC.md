# Specifica visuale REPLICATIO-01

- modello compositivo: replication_protocol
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Domanda e claim a Replica nel capitolo 97?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un claim di paper e il protocollo necessario per riprodurlo
- input: paper, codice, dati, seed, hardware e metriche
- output: risultato replicato o differenza spiegata
- nodi locali: Domanda e claim: Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti.; Artefatti: Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizi.; Replica: Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metod.
- limite visualizzato: una replica richiede stesso claim e confini dichiarati, non solo stesso codice
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
