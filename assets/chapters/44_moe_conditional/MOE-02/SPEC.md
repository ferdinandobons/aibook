# Specifica visuale MOE-02

- famiglia: chart
- domanda principale: Il diagramma segue il passaggio: Routing, dispatch, expert compute e combine. L'input è logits del router, top-k e capacità per esperto, l'output è carico, token restituiti e costo attivo; il vincolo da controllare è che parametri totali e parametri attivi non sono la stessa quantità
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v45.png
- ordine di lettura: titolo, domanda, chart, invariante o limite in chiusura
- nodi e contenuti: 1: Router top-k; 2: Capacità; 3: Load balancing; 4: Expert parallelism; 5: Parametri totali e attivi
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: parametri totali e parametri attivi non sono la stessa quantità
- fonti collegate: SRC-44-001 ... SRC-44-004
- alt text: Diagramma MOE-02 del Capitolo 44, famiglia chart. Domanda: Il diagramma segue il passaggio: Routing, dispatch, expert compute e combine. L'input è logits del router, top-k e capacità per esperto, l'output è carico, token restituiti e costo attivo; il vincolo da controllare è che parametri totali e parametri attivi non sono la stessa quantità La composizione usa i passaggi Router top-k, Capacità, Load balancing, Expert parallelism, Parametri totali e attivi.
