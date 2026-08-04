# Specifica visuale DECODING-02

- modello compositivo: acceptance_path
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Medusa, EAGLE e ReDrafter da Parallel decoding?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: draft e target durante il decoding speculativo
- input: token proposti, logits draft e logits target
- output: token accettati, velocità e distribuzione preservata
- nodi locali: Medusa, EAGLE e ReDrafter: Head multiple, feature prediction e recurrent drafter producono candidate con strutture di.; Parallel decoding: Metodi lookahead o Jacobi aggiornano più posizioni ma devono dichiarare se preservano esat.
- limite visualizzato: lo speedup richiede verifica senza cambiare il contratto di output
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
