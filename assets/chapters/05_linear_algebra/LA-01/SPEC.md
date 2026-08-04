# Specifica visuale LA-01

## Identità

- Capitolo: CH-P02-LINEAR-ALGEBRA
- Sezione: prodotto matriciale e trasformazione affine
- Famiglia: diagramma delle shape
- Orientamento: orizzontale
- File candidato: candidate-v1.png
- Sfondo: bianco puro

## Domanda

Quale asse viene combinato nel prodotto tra la matrice degli esempi e la matrice dei pesi, quali assi restano nell'output e come viene aggiunto il bias?

## Sequenza

X ha shape batch 3 per feature 4. La matrice dei pesi trasposta ha shape feature 4 per classe 3. Il prodotto ha shape batch 3 per classe 3. Un bias con tre valori viene aggiunto a ogni riga e produce Y con shape batch 3 per classe 3.

La figura usa i valori esatti dello snippet del capitolo. La matrice intermedia non contiene ancora il bias; il pannello finale mostra il risultato dopo il broadcasting.

## Invariante e confine

L'asse feature, lungo quattro, viene contratto. Batch e classe restano. La compatibilità delle shape non dimostra da sola che gli assi possiedano il significato corretto.

## Contenimento

- matrici completamente nei box;
- decimali con virgola;
- frecce esterne ai contenitori;
- nota sulla contrazione collegata ai due fattori;
- nessuna sovrapposizione tra bias, titolo e output.
- domanda principale: Quale trasformazione centrale rende osservabile «Da un numero a un tensore» nel capitolo 5?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
