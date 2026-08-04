# Specifica visuale PEFT-02

- modello compositivo: adapter_stack
- domanda principale: Quale controllo collega «Prompt, prefix e IA3» a «QLoRA e compatibilità» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: l'aggiornamento adattivo rispetto ai pesi congelati
- input: peso W, matrice A e B, rank e quantizzazione
- output: delta W e checkpoint adattatore
- nodi locali: Prompt, prefix e IA3: Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo…; QLoRA e compatibilità: Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili.…
- limite visualizzato: il delta non è il modello completo e va valutato sullo stesso base model
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
