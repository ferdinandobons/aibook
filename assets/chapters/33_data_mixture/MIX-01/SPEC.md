# Specifica visuale MIX-01

- modello compositivo: mixture_channels
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale percorso collega Peso effettivo delle sorgenti a Mixture ottimizzata nel capitolo 33?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la miscela effettiva di sorgenti durante il training
- input: pesi, temperatura, curriculum e conteggio dei token
- output: probabilità effettive e mix osservato
- nodi locali: Peso effettivo delle sorgenti: Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni.; Temperature sampling: Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli.; Mixture ottimizzata: Pesi appresi con proxy model dipendono da domini, validation e budget.
- limite visualizzato: peso nominale e esposizione effettiva non sono la stessa misura
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
