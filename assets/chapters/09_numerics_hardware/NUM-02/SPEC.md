# Specifica visuale `NUM-02`

## Identità

- Capitolo: `CH-P02-NUMERICS-HARDWARE`
- Sezione: Mixed precision e autocast
- Famiglia: processo / sistema
- Orientamento: orizzontale
- Sfondo: bianco puro `#FFFFFF`
- File candidato: `candidate-v1.png`

## Domanda unica

Quali parti del training possono usare precisione ridotta e quali quantità possono richiedere float32?

## Flusso principale

```text
Input e pesi
-> Autocast
-> Matmul e convolution
-> Riduzioni e loss
-> Backward
-> Optimizer e master weights
-> pesi aggiornati
```

## Contratti

- autocast sceglie il dtype per operatore;
- matmul e convolution idonee possono usare fp16 o bfloat16;
- riduzioni, loss e accumulatori sensibili possono restare in fp32;
- loss scaling è opzionale e pertinente soprattutto al training fp16;
- optimizer e master weights possono restare in float32;
- il loop di ritorno aggiorna i pesi, non l'input.

## Regole visuali

- freccia rossa `gradienti` da backward all'optimizer;
- freccia blu `pesi aggiornati` dall'optimizer al box iniziale;
- nessuna freccia attraversa testo;
- il diagramma deve essere dichiarato tipico, non universale;
- nessuna policy specifica viene presentata come stabile tra tutti i device.

## Provenienza

- PyTorch AMP e Numerical Accuracy;
- Micikevicius et al. 2017;
- Kalamkar et al. 2019;
- NVIDIA CUDA/cuBLAS;
- renderer: `scripts/generate_numerics_visuals.py` e revisione `generate_numerics_visuals_v2.py`.
- domanda principale: Quale confronto o limite chiarisce «Range e precisione rispondono a domande diverse»?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
