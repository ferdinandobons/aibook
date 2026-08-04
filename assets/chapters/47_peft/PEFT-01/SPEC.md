# Specifica visuale PEFT-01

- famiglia: architecture
- domanda principale: Il diagramma segue il passaggio: Adapter, LoRA, prefix o QLoRA. L'input è peso W, matrice A e B, rank e quantizzazione, l'output è delta W e checkpoint adattatore; il vincolo da controllare è che il delta non è il modello completo e va valutato sullo stesso base model
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, architecture, invariante o limite in chiusura
- nodi e contenuti: 1: Parametri congelati e adattamento; 2: Adapter; 3: LoRA; 4: Prompt, prefix e IA3; 5: QLoRA e compatibilità
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: il delta non è il modello completo e va valutato sullo stesso base model
- fonti collegate: SRC-47-001 ... SRC-47-004
- alt text: Diagramma PEFT-01 del Capitolo 47, famiglia architecture. Domanda: Il diagramma segue il passaggio: Adapter, LoRA, prefix o QLoRA. L'input è peso W, matrice A e B, rank e quantizzazione, l'output è delta W e checkpoint adattatore; il vincolo da controllare è che il delta non è il modello completo e va valutato sullo stesso base model La composizione usa i passaggi Parametri congelati e adattamento, Adapter, LoRA, Prompt, prefix e IA3, QLoRA e compatibilità.
