# Specifica visuale RECURREN-02

- modello compositivo: state_compare
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Bidirezionalità e causalità da RNN, attention e stato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v51.png
- oggetto osservato: uno stato nascosto che attraversa una sequenza
- input: x_1, x_2, x_3 e h_0 = 0
- output: h_t e, se richiesto, una predizione per il passo
- nodi locali: Bidirezionalità e causalità: Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline.; RNN, attention e stato: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite.
- limite visualizzato: lo stato precedente deve essere consumato prima di produrre quello successivo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
