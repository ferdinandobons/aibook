# Specifica visuale SERVING-02

- modello compositivo: continuous_batch
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Admission control da Metriche di servizio?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: richieste eterogenee in una coda di serving
- input: prompt, deadline, lunghezza, memoria e priorità
- output: throughput, latency p50/p99 e richieste ammesse
- nodi locali: Admission control: Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema.; Metriche di servizio: TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e c.
- limite visualizzato: throughput e latenza devono essere misurati insieme
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
