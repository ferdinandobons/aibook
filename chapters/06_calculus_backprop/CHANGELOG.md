# Changelog. Capitolo 6

## `0.2.0-rc1`. 31 luglio 2026

### Testo

- aggiunta la lezione completa su derivata, derivate parziali, gradiente e Jacobiana;
- costruita la regola della catena sullo stesso grafo numerico;
- eseguiti forward e backward con valori verificati;
- introdotti forward mode, reverse mode e VJP dopo il caso scalare;
- separati backpropagation e optimizer step;
- distinte automatic differentiation, differenze finite e differenziazione simbolica;
- integrati `requires_grad`, `backward`, `grad`, `gradcheck`, accumulo, `detach`, `no_grad`, `inference_mode` e operazioni in-place;
- aggiunti riepilogo, verifiche ed esercizi.

### Codice

- registrato `SNIP-CALC-001`;
- confrontati gradienti manuali, autograd e differenze finite;
- eseguito `gradcheck` in float64;
- dimostrato l'accumulo in `.grad`;
- superati cinque test.

### Visuali

- aggiunta `CALC-01`, forward e backward sullo stesso grafo;
- aggiunta `CALC-02`, reverse mode come composizione di derivate locali;
- respinte tre candidate image-gen non pertinenti;
- respinta la prima raster di `CALC-02` per sovrapposizione del footer;
- validate tecnicamente le candidate raster corrette;
- aggiunti specifiche, audit e alt text.

### Review

- completata una prima lettura critica con difetti bloccanti;
- applicate le correzioni;
- completata una seconda lettura integrale;
- superati gate fattuali, matematici, didattici, anti-template, linguistici e di accessibilità;
- aperta la revisione autoriale.

## `0.1.0-draft1`. 31 luglio 2026

- creati piano, fonti e registro dei claim;
- aggiunti snippet, output e test;
- testo e visuali non ancora presenti.
