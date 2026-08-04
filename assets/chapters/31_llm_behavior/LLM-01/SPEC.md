# Specifica visuale LLM-01

- modello compositivo: behavior_boundary
- domanda principale: Come si passa da «Distribuzione del token successivo» a «Decoding» mantenendo osservabile un prompt e la distribuzione del token successivo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un prompt e la distribuzione del token successivo
- input: prefisso tokenizzato, esempi e temperatura dichiarati
- output: logits, risposta e confidenza misurabile
- nodi locali: Distribuzione del token successivo: Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce…; Prompt e dimostrazioni: Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta…; Decoding: Greedy, sampling, temperature e truncation trasformano la distribuzione in una…
- limite visualizzato: probabilità, comportamento osservato e correttezza non sono sinonimi
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
