# Specifica visuale SERVING-02

- famiglia: queue
- domanda principale: Il diagramma segue il passaggio: Batching continuo, admission e scheduling. L'input è prompt, deadline, lunghezza, memoria e priorità, l'output è throughput, latency p50/p99 e richieste ammesse; il vincolo da controllare è che throughput e latenza devono essere misurati insieme
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, queue, invariante o limite in chiusura
- nodi e contenuti: 1: Richieste eterogenee; 2: Continuous batching; 3: Throughput e latency; 4: Admission control; 5: Metriche di servizio
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: throughput e latenza devono essere misurati insieme
- fonti collegate: SRC-79-001 ... SRC-79-004
- alt text: Diagramma SERVING-02 del Capitolo 79, famiglia queue. Domanda: Il diagramma segue il passaggio: Batching continuo, admission e scheduling. L'input è prompt, deadline, lunghezza, memoria e priorità, l'output è throughput, latency p50/p99 e richieste ammesse; il vincolo da controllare è che throughput e latenza devono essere misurati insieme La composizione usa i passaggi Richieste eterogenee, Continuous batching, Throughput e latency, Admission control, Metriche di servizio.
