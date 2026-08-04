# Specifica visuale REPLICATIO-01

- modello compositivo: replication_protocol
- domanda principale: Come si passa da «Domanda e claim» a «Replica» mantenendo osservabile un claim di paper e il protocollo necessario per riprodurlo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un claim di paper e il protocollo necessario per riprodurlo
- input: paper, codice, dati, seed, hardware e metriche
- output: risultato replicato o differenza spiegata
- nodi locali: Domanda e claim: Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti.; Artefatti: Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la…; Replica: Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il…
- limite visualizzato: una replica richiede stesso claim e confini dichiarati, non solo stesso codice
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
