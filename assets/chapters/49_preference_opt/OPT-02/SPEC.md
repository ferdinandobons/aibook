# Specifica visuale OPT-02

- modello compositivo: method_compare
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa IPO, KTO, ORPO e varianti da Offline preference data?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia chosen-rejected per l'ottimizzazione diretta
- input: prompt, log-probability della policy e riferimento
- output: loss di preferenza e policy aggiornata
- nodi locali: IPO, KTO, ORPO e varianti: Le varianti cambiano assunzioni, forma della loss o tipo di feedback.; Offline preference data: L'ottimizzazione resta limitata alla copertura del dataset.
- limite visualizzato: la preferenza osservata non è una verità assoluta
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
