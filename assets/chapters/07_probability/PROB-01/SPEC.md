# Specifica visuale `PROB-01`

## Identità

- Capitolo: `CH-P02-PROBABILITY`
- Sezione: Bayes aggiorna una probabilità con l'evidenza
- Famiglia: tabella congiunta / processo di normalizzazione
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come si passa da prior e likelihood al posterior nel caso binario del capitolo?

## Valori obbligatori

```text
P(H) = 0,20
P(not H) = 0,80
P(E1|H) = 0,80
P(E1|not H) = 0,10

P(H,E1) = 0,16
P(H,not E1) = 0,04
P(not H,E1) = 0,08
P(not H,not E1) = 0,72
P(E1) = 0,24
P(H|E1) = 0,6667
```

## Layout

1. Pannello sinistro: prior, likelihood e significato di `H` ed `E1`.
2. Pannello centrale: tabella congiunta `2 × 2` con marginali.
3. Colonna `E1 osservato` evidenziata in ambra.
4. Pannello destro: numeratore, evidenza e posterior.
5. Footer: il posterior è corretto rispetto al modello, non garantisce che il modello sia ben calibrato.

## Collegamenti

- prior e likelihood conducono alla tabella;
- la colonna osservata conduce alla normalizzazione;
- nessuna freccia attraversa celle o label;
- il denominatore deve apparire come somma `0,16 + 0,08`.

## Contenimento

- tutte le celle hanno padding;
- intestazioni leggibili su fondo chiaro;
- simboli `¬`, pedici e barra condizionale completamente visibili;
- nessuna formula a contatto con un bordo.

## Provenienza

I valori derivano dalla tabella del capitolo e da `SNIP-PROB-001`. La candidata è un PNG raster generato da `scripts/generate_probability_visuals.py`; non viene usato SVG.
- domanda principale: Quale trasformazione centrale rende osservabile «Esiti, eventi e probabilità» nel capitolo 7?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
