# Audit visuale `EVAL-02`

## Stato

- File: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Audit numerico

- [x] Accuratezza A `19/24 = 0,792` dopo arrotondamento.
- [x] Accuratezza B `20/24 = 0,833` dopo arrotondamento.
- [x] Slice standard A `12/16 = 0,750`.
- [x] Slice standard B `15/16 = 0,938` dopo arrotondamento.
- [x] Slice urgente A `7/8 = 0,875`.
- [x] Slice urgente B `5/8 = 0,625`.
- [x] Costi pesati `8,0` e `13,0` coerenti con lo snippet.
- [x] Differenza osservata `+0,042` e intervallo `[-0,208, +0,292]` coerenti con il run registrato.

## Audit semantico

- [x] Il modello B appare migliore soltanto sulle letture che lo sostengono.
- [x] La slice urgente e il costo mostrano il trade-off senza sostituirsi alla decisione dell'utente.
- [x] La linea dello zero è distinta dal punto osservato.
- [x] La nota non interpreta l'inclusione di zero come equivalenza.
- [x] Il footer collega la scelta alla domanda di valutazione.

## Audit geometrico e stilistico

- [x] Sfondo bianco puro.
- [x] Label, barre, cifre e note restano nei contenitori.
- [x] Nessuna sovrapposizione tra asse, intervallo e testo.
- [x] Il colore non è l'unico identificatore dei modelli.
- [x] I due pannelli hanno gerarchia e densità equilibrate.

## Provenienza

La figura è generata da `scripts/generate_evaluation_visuals.py`. I valori provengono dal dataset illustrativo di `SNIP-EVAL-001`.

## Verdetto

La figura può essere inclusa nella candidatura del Capitolo 4. Resta `candidate-v1.png` fino all'approvazione autoriale.
