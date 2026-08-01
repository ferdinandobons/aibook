# Specifica visuale `NUM-01`

## Identità

- Capitolo: `CH-P02-NUMERICS-HARDWARE`
- Sezione: Range e precisione
- Famiglia: confronto strutturale
- Orientamento: orizzontale
- Sfondo: bianco puro `#FFFFFF`
- File candidato: `candidate-v1.png`

## Domanda unica

Perché `float16` e `bfloat16`, pur occupando entrambi 16 bit, offrono compromessi numerici differenti?

## Contenuto

Quattro schede parallele:

| dtype | bit | byte | eps | massimo finito |
|---|---|---:|---:|---:|
| float16 | 1 segno, 5 esponente, 10 significando | 2 | 9,765625e-4 | 65504 |
| bfloat16 | 1 segno, 8 esponente, 7 significando | 2 | 7,8125e-3 | 3,3895e38 |
| float32 | 1 segno, 8 esponente, 23 significando | 4 | 1,1921e-7 | 3,4028e38 |
| float64 | 1 segno, 11 esponente, 52 significando | 8 | 2,2204e-16 | 1,7977e308 |

## Messaggio finale

`Float16 conserva più dettaglio di bfloat16 vicino a 1; bfloat16 conserva un range simile a float32.`

## Regole

- nessuna scala gerarchica di qualità;
- segmenti dei bit interamente dentro ogni scheda;
- colori diversi per segno, esponente e significando;
- valori derivati da `torch.finfo` e documentazione ufficiale;
- nessuna promessa di velocità;
- nessun elemento relativo al progetto o allo stato del libro.

## Provenienza

- IEEE 754-2019;
- PyTorch Tensor Attributes e Type Info;
- Kalamkar et al. per bfloat16;
- `SNIP-NUM-001` per i valori stampati;
- renderer: `scripts/generate_numerics_visuals.py` e revisione `generate_numerics_visuals_v2.py`.
