# Specifica visuale KV-01

- modello compositivo: attention_compare
- domanda principale: Come si passa da «MHA» a «GQA» mantenendo osservabile le teste di query e key-value che alimentano l'attention?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: le teste di query e key-value che alimentano l'attention
- input: Q con h_q teste e KV con h_kv teste
- output: score, cache e pattern di comunicazione
- nodi locali: MHA: Ogni query head possiede key e value dedicate.; MQA: Tutte le query head condividono una singola coppia key-value, riducendo la cache.; GQA: Gruppi di query head condividono un numero intermedio di KV head.
- limite visualizzato: raggruppamento delle teste e costo della KV cache restano espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
