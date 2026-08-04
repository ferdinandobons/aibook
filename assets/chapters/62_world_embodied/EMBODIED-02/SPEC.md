# Specifica visuale EMBODIED-02

- modello compositivo: action_boundary
- domanda principale: Quale controllo collega «Vision-language-action» a «Sicurezza e sim-to-real» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato di un agente embodied nel mondo
- input: osservazione, stato, azione e dinamica
- output: azione, stato previsto e risultato fisico
- nodi locali: Vision-language-action: VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e…; Sicurezza e sim-to-real: Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non…
- limite visualizzato: sim-to-real richiede una misura sul sistema reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
