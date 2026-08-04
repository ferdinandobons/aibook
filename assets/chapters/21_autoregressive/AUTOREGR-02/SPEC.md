# Specifica visuale AUTOREGR-02

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Fattorizzazione, teacher forcing e decoding. L'input è un prefisso di tre token e una mask causale, l'output è logits, token scelto e traiettoria; il vincolo da controllare è che nessuna posizione futura entra nella predizione causale
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v49.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: Fattorizzare una sequenza; 2: Teacher forcing; 3: Maschera causale; 4: Sampling e accumulo degli errori; 5: Immagini, audio e token discreti
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: nessuna posizione futura entra nella predizione causale
- fonti collegate: SRC-21-001 ... SRC-21-004
- alt text: Diagramma AUTOREGR-02 del Capitolo 21, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Fattorizzazione, teacher forcing e decoding. L'input è un prefisso di tre token e una mask causale, l'output è logits, token scelto e traiettoria; il vincolo da controllare è che nessuna posizione futura entra nella predizione causale La composizione usa i passaggi Fattorizzare una sequenza, Teacher forcing, Maschera causale, Sampling e accumulo degli errori, Immagini, audio e token discreti.
