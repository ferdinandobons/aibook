# Changelog. Capitolo 9

## `0.1.0-draft1`. 31 luglio 2026

### Ricerca e claim

- registrate quattordici fonti primarie o ufficiali;
- verificata la documentazione PyTorch stable corrente;
- registrati ventinove claim con limiti d'uso;
- separati formati, API, hardware e risultati eseguiti.

### Testo

- costruito il capitolo attorno a un classificatore con matmul e softmax;
- introdotti floating point, range, precisione e arrotondamento;
- spiegate non associatività, cancellazione, condizionamento e stabilità;
- mostrati overflow, underflow, `inf`, `nan` e logsumexp stabile;
- confrontati float16, bfloat16, float32 e float64;
- distinti storage, calcolo, accumulo e output;
- introdotti mixed precision, autocast, loss scaling e master weights;
- collegati dtype, Tensor Core, TF32, bandwidth e Roofline;
- distinti determinismo, riproducibilità e identità bitwise.

### Codice

- aggiunto `SNIP-NUM-001`;
- registrato l'ambiente CPU;
- salvato l'output letterale;
- aggiunti e superati sette test.

### Visuali

- respinta una candidata dello strumento immagini perché estranea e fattualmente falsa;
- creato il renderer raster `generate_numerics_visuals.py`;
- respinta la prima iterazione di `NUM-01` per overflow grafico dei segmenti;
- corretta la composizione con `generate_numerics_visuals_v2.py`;
- aggiunte label esplicite al loop di `NUM-02`;
- creati specifica, audit e alt text per entrambe le figure;
- materializzazione dei PNG nel branch ancora aperta.

### Review

- superati audit fattuale, matematico, algoritmico e del codice;
- superata review per lettore non esperto;
- superata review editoriale e linguistica della bozza;
- revisione autoriale rinviata alla materializzazione dei raster.
