# Specifica visuale OPT-02

- modello compositivo: method_compare
- domanda principale: Quale controllo collega «IPO, KTO, ORPO e varianti» a «Offline preference data» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia chosen-rejected per l'ottimizzazione diretta
- input: prompt, log-probability della policy e riferimento
- output: loss di preferenza e policy aggiornata
- nodi locali: IPO, KTO, ORPO e varianti: Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono…; Offline preference data: L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono…
- limite visualizzato: la preferenza osservata non è una verità assoluta
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
