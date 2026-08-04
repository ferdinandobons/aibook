# Specifica visuale JAILBREAK-01

- modello compositivo: perturbation_grid
- domanda principale: Come si passa da «Threat model» a «Ottimizzazione adversarial» mantenendo osservabile una superficie di attacco e il comportamento sotto perturbazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una superficie di attacco e il comportamento sotto perturbazione
- input: threat model, prompt, budget e risposta
- output: success rate, failure mode e costo della difesa
- nodi locali: Threat model: Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Un jailbreak…; Perturbazioni: Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali.; Ottimizzazione adversarial: Suffix e prompt vengono cercati per aumentare una loss di attacco. Trasferibilità e…
- limite visualizzato: un test superato non copre minacce non incluse nel protocollo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
