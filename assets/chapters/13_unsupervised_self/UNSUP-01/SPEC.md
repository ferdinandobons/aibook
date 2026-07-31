# Specifica visuale `UNSUP-01`

## Identità

- Capitolo: `CH-P03-UNSUPERVISED-SELF`
- Famiglia: confronto concettuale
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quali segnali di training possono essere costruiti senza assegnare una label esterna a ogni esempio?

## Pannelli

1. **Clustering**
   - punti senza label;
   - distanza da centroidi;
   - output gruppi e centroidi.
2. **Ricostruzione mascherata**
   - dato originale;
   - coordinate nascoste;
   - target ricavato dall'input;
   - output embedding e ricostruzione.
3. **Contrasto o predizione**
   - due viste correlate oppure contesto e parte futura;
   - obiettivo di similarità/predizione;
   - output rappresentazione trasferibile.

## Regole

- i pannelli non formano una gerarchia;
- nessun pannello viene marcato come universalmente migliore;
- label esterna assente, obiettivo presente;
- il colore non è l'unico elemento distintivo;
- testo interamente contenuto;
- frecce verticali o orizzontali senza incroci;
- footer sul bias introdotto da distanza, mask, augmentazioni, contesto e negative.

## Provenienza

- clustering da `SNIP-UNSUP-001` e MacQueen;
- masked modeling da BERT, denoising autoencoder e MAE;
- contrasto/predizione da CPC e SimCLR;
- PNG raster generato da `scripts/generate_unsupervised_visuals.py`;
- nessun SVG.
