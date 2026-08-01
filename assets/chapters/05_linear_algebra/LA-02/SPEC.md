# Specifica visuale LA-02

## Identità

- Capitolo: CH-P02-LINEAR-ALGEBRA
- Sezione: rango e singular value decomposition
- Famiglia: decomposizione matriciale
- Orientamento: orizzontale
- File candidato: candidate-v1.png
- Sfondo: bianco puro

## Domanda

Come rende visibile la SVD che la matrice dell'esempio possiede soltanto due direzioni indipendenti numericamente rilevanti?

## Contenuto

- matrice A con righe 1,2,3; 2,4,6; 1,1,1;
- nota che la seconda riga è il doppio della prima;
- decomposizione A uguale a U per diagonale di S per V trasposta;
- valori singolari 8,5198; 0,6429; circa zero;
- lettura come somma di tre componenti di rango uno;
- terza componente marcata come numericamente nulla nell'esempio.

## Invariante e confine

La matrice viene ricostruita dalle componenti. La soglia con cui un valore piccolo viene trattato come nullo dipende da scala, precisione e tolleranza. La figura non suggerisce di troncare automaticamente ogni componente piccola.

## Contenimento

- matrice completamente visibile;
- formule e valori singolari nei rispettivi pannelli;
- nessuna barra oltre il proprio contenitore;
- terza componente distinguibile anche senza colore;
- footer separato dalla decomposizione.
