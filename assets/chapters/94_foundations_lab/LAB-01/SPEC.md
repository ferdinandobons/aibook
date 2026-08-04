# Specifica visuale LAB-01

- modello compositivo: lab_pipeline
- domanda principale: Come si passa da «Ambiente riproducibile» a «Modello e loss» mantenendo osservabile un esperimento didattico con ambiente e artefatti dichiarati?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un esperimento didattico con ambiente e artefatti dichiarati
- input: seed, dataset piccolo, config, codice e versione
- output: loss, metriche, manifest e limite
- nodi locali: Ambiente riproducibile: Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti.; Dataset piccolo: Un dataset controllabile permette di vedere preprocessing, split, batch e leakage.; Modello e loss: Una baseline lineare precede la rete. Shape, logits e loss vengono verificati con test.
- limite visualizzato: un run locale non equivale a una prova generale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
