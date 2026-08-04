# Specifica visuale `SUP-01`

- capitolo: `CH-P02-SUPERVISED`
- sezione: train, validation e test
- famiglia: processo di valutazione
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_supervised_visuals.py`

## Domanda unica

Come si separano apprendimento dei parametri, scelta della configurazione e stima finale?

## Contenuto

- dataset etichettato e split dichiarato;
- train che aggiorna i parametri;
- validation che seleziona soglia e configurazione;
- test finale con modello e soglia fissati;
- risultati illustrativi e confine sul riuso del test.
- domanda principale: Quale trasformazione centrale rende osservabile «Dalle osservazioni alle coppie input-target» nel capitolo 12?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
