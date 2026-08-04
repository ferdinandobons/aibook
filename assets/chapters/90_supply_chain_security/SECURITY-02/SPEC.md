# Specifica visuale SECURITY-02

- modello compositivo: artifact_lineage
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Artifact security da Repository e deployment?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: gli artefatti che attraversano la supply chain del modello
- input: dataset, checkpoint, repository, digest e owner
- output: artefatto rilasciato, traccia e decisione di blocco
- nodi locali: Artifact security: Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di carica.; Repository e deployment: File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente d.
- limite visualizzato: integrità del file non certifica assenza di contenuto malevolo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
