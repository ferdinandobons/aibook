# Specifica visuale `INFO-02`

## Identità

- Capitolo: `CH-P02-INFORMATION-THEORY`
- Sezione: Cross-entropy e KL divergence
- Famiglia: decomposizione matematica
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come si separa la cross-entropy tra incertezza già presente nel target e divario tra target e previsione?

## Distribuzioni

```text
q = [0,90; 0,05; 0,05]
p = [0,7856; 0,1753; 0,0391]
```

## Valori

```text
H(q) = 0,394398
KL(q||p) = 0,071914
H(q,p) = 0,466311
```

## Layout

1. target `q` a sinistra, con barre;
2. predizione `p` a destra, con barre;
3. box centrale della cross-entropy;
4. fascia inferiore con `H(q) + KL(q||p) = H(q,p)`;
5. footer sul caso one-hot.

## Regole

- frecce da entrambe le distribuzioni verso la cross-entropy;
- cross-entropy non rappresentata come distanza geometrica;
- KL orientata `q||p`, non invertita;
- decimali con virgola;
- il caso one-hot viene marcato come confine, non come formula generale dei target morbidi.

## Provenienza

Valori da `SNIP-INFO-001`. PNG raster generato da `scripts/generate_information_visuals.py`; nessun SVG.
