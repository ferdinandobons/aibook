# Codice. Capitolo 13

## Snippet

`SNIP-UNSUP-001`, file `snip_unsup_001_structure_and_masking.py`.

Lo snippet applica due obiettivi allo stesso dataset sintetico:

1. k-means sulle sole feature;
2. masked reconstruction con un autoencoder e un embedding a due dimensioni.

I gruppi segreti del generatore non entrano in k-means, nella rete o nella loss.

## Esecuzione

```bash
python snip_unsup_001_structure_and_masking.py
python -m unittest -v test_unsupervised_self.py
```

## Contratti verificati

- inizializzazione dei centroidi basata soltanto sulla geometria;
- obiettivo k-means non crescente;
- cluster non vuoti;
- centroidi uguali alla media dei membri assegnati;
- maschera esplicita nell'input della rete;
- almeno una coordinata nascosta e una visibile per esempio;
- maschere variabili nel training;
- maschera di test fissata;
- loss soltanto sulle coordinate nascoste;
- confronto con baseline che usa la media del training;
- run deterministico nel perimetro registrato.

## Limiti

- dati sintetici e separazione geometrica semplice;
- K fissato a tre;
- nessuna metrica rispetto ai gruppi segreti;
- nessuna evaluation downstream dell'embedding;
- nessuna implementazione contrastiva;
- nessun benchmark di velocità o scala.
