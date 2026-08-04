# Specifica visuale LOOP-02

- modello compositivo: state_machine
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale failure o confronto separa Verificare da Terminare?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: lo stato di una traiettoria agentica
- input: osservazione, piano, azione e risultato del tool
- output: stato successivo o arresto motivato
- nodi locali: Verificare: Test, controlli di stato o giudici indipendenti valutano il risultato.; Terminare: Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condi.
- limite visualizzato: ogni side effect deve avere precondizioni e verifica
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
