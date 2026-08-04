# Specifica visuale `INFO-02`

- capitolo: `CH-P02-INFORMATION-THEORY`
- sezione: entropia, cross-entropy e KL
- famiglia: decomposizione numerica
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_information_visuals.py`

## Domanda unica

Come si vede numericamente la relazione `H(q,p) = H(q) + KL(q||p)`?

## Contenuto

- target `q` e predizione `p` rappresentati come distribuzioni a tre classi;
- calcolo della cross-entropy nel pannello centrale;
- decomposizione in entropia del target e divergenza KL;
- footer che delimita il caso one-hot.

## Invariante

I tre termini sono coerenti con gli stessi vettori `q` e `p`; il valore mostrato è illustrativo e non una misura di training.
- domanda principale: Quale trasformazione centrale rende osservabile «Informazione di un evento» nel capitolo 8?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
