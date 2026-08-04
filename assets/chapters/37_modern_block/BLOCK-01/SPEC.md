# Specifica visuale BLOCK-01

- modello compositivo: block_compare
- domanda principale: Come si passa da «Residual stream» a «RMSNorm» mantenendo osservabile un residual stream dentro un blocco moderno?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un residual stream dentro un blocco moderno
- input: h di shape [batch, length, d] e norma misurata
- output: h' con shape preservata e statistiche confrontabili
- nodi locali: Residual stream: Ogni sottolayer produce un aggiornamento sommato a un percorso identità.; Pre-norm e post-norm: La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del…; RMSNorm: RMSNorm scala usando la media quadratica e non sottrae la media.
- limite visualizzato: ordine dei sottolayer e shape sono parte del blocco
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
