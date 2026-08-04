# Specifica visuale ALT-01

- modello compositivo: objective_compare
- domanda principale: Come si passa da «Byte e caratteri» a «Predizione multi-token» mantenendo osservabile unità di predizione dal byte al token multiplo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: unità di predizione dal byte al token multiplo
- input: byte, gerarchia, target e numero di passi
- output: unità predette, loss e durata di decoding
- nodi locali: Byte e caratteri: Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe.; Gerarchie di byte: Patch fisse o dinamiche riducono la lunghezza vista dal modello globale.; Predizione multi-token: Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato.
- limite visualizzato: granularità della rappresentazione e parallelismo sono assi distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
