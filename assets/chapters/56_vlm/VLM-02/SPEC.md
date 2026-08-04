# Specifica visuale VLM-02

- famiglia: pipeline
- domanda principale: Il diagramma segue il passaggio: Vision encoder, projector e cross-attention. L'input è immagine, patch, testo e query, l'output è token visivi, risposta e grounding; il vincolo da controllare è che una risposta linguistica non certifica che il dettaglio sia nell'immagine
- orientamento: orizzontale
- formato: PNG raster 1800x1000
- sfondo: #FFFFFF
- versione candidata: candidate-v48.png
- ordine di lettura: titolo, domanda, pipeline, invariante o limite in chiusura
- nodi e contenuti: 1: Patch e vision encoder; 2: Dual encoder; 3: Projector; 4: Q-Former e cross-attention; 5: Grounding e hallucination
- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore
- invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine
- fonti collegate: SRC-56-001 ... SRC-56-004
- alt text: Diagramma VLM-02 del Capitolo 56, famiglia pipeline. Domanda: Il diagramma segue il passaggio: Vision encoder, projector e cross-attention. L'input è immagine, patch, testo e query, l'output è token visivi, risposta e grounding; il vincolo da controllare è che una risposta linguistica non certifica che il dettaglio sia nell'immagine La composizione usa i passaggi Patch e vision encoder, Dual encoder, Projector, Q-Former e cross-attention, Grounding e hallucination.
