# Specifica visuale INTERPRETA-01

- modello compositivo: observation_inference
- domanda principale: Come si passa da «Oggetto dell'interpretazione» a «Attribution» mantenendo osservabile un comportamento del modello e l'intervento che lo modifica?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un comportamento del modello e l'intervento che lo modifica
- input: attivazioni, probe, attribution e baseline
- output: effetto osservato con controllo e confondenti
- nodi locali: Oggetto dell'interpretazione: Pesi, attivazioni, feature, head e comportamento sono livelli differenti. Il metodo deve…; Probing: Un probe misura informazione decodificabile da una rappresentazione. Non prova che il…; Attribution: Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni…
- limite visualizzato: correlazione di una feature non prova causalità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
