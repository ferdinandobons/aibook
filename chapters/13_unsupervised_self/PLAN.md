# Piano interno. Capitolo 13

## Identità

- `chapter_id`: `CH-P03-UNSUPERVISED-SELF`
- Parte: `P03`, Apprendimento, ottimizzazione e decisione
- Titolo: **Apprendimento non supervisionato e auto-supervisionato**
- Stato: candidatura completa in revisione autoriale
- Versione prevista: `0.2.0-rc1`
- Oggetto continuo: lo stesso dataset sintetico a quattro feature, senza label esterne usate dal training
- Domanda centrale: come si costruisce un segnale di apprendimento quando non esiste una label esterna per ogni esempio?

## Contratto di continuità

### Prerequisiti stabili

- target, split, rischio empirico e generalizzazione, Capitolo 12;
- vettori, distanze, centroidi, SVD e dimensione latente, Capitolo 5;
- gradienti e optimizer, Capitolo 6;
- distribuzioni e campioni, Capitolo 7;
- entropia, cross-entropy e KL, Capitolo 8;
- precisione numerica e riproducibilità, Capitolo 9.

### Concetti richiamati ma rispiegati localmente

- distanza euclidea;
- mean squared error;
- embedding;
- pretraining e fine-tuning;
- linear probe;
- augmentazione.

### Forward reference non necessarie alla comprensione

- language modeling autoregressivo;
- variational autoencoder e modelli generativi;
- contrastive learning avanzato;
- foundation model e pretraining su larga scala;
- multimodal pretraining.

### Gap che apre il capitolo

Il Capitolo 12 richiedeva una label esterna per ogni esempio. Qui manca quel target, ma restano dati grezzi e relazioni interne da cui costruire un obiettivo.

### Output consegnato al capitolo successivo

Un encoder o una struttura appresa senza label di task, insieme alla distinzione tra obiettivo di pretraining e valutazione downstream. Il Capitolo 14 introdurrà azioni e reward, quindi un segnale che dipende dalle conseguenze temporali delle decisioni.

## Oggetto numerico

```text
train: 120 vettori, shape [120,4]
test: 60 vettori, shape [60,4]
gruppi segreti del generatore: 3, non usati dal training

k-means:
K = 3
obiettivo: 203,144502 -> 60,284823
conteggi cluster: [40,40,40]

masked autoencoder:
input: 4 valori + mask binaria
embedding: 2 valori
loss iniziale train: 2,218895
loss finale train: 0,359401
loss test: 0,391415
baseline media test: 1,900604
```

## Progressione

1. Rimuovere la label esterna.
2. Obiettivo e bias induttivo.
3. Clustering e k-means.
4. Rappresentazione, PCA e autoencoder.
5. Denoising e masked modeling.
6. Target auto-generato.
7. Contrastive e predictive learning.
8. Collapse e meccanismi anti-collasso.
9. Pseudo-label e DeepCluster.
10. Pretraining, linear probe e fine-tuning.
11. Valutazione downstream.
12. Codice con k-means e masked reconstruction.
13. Failure mode e confini.
14. Ponte al reinforcement learning.

## Codice

### `SNIP-UNSUP-001`

- dataset sintetico con gruppi nascosti;
- k-means con inizializzazione geometrica;
- obiettivo e aggiornamento dei centroidi;
- masked autoencoder con mask esplicita;
- maschere variabili durante il training e fissate nel test;
- confronto con baseline media;
- embedding a due dimensioni;
- nove test automatici.

## Visuali

### `UNSUP-01`. Tre modi di costruire un segnale senza label esterne

Confronta clustering, ricostruzione mascherata e contrasto/predizione. Ogni pannello mostra input, obiettivo e output. Il footer chiarisce che maschera, distanza, contesto e coppie sono scelte progettuali.

### `UNSUP-02`. La label nasce dal dato stesso

Mostra dato originale, maschera, input corrotto, encoder, decoder e loss soltanto sulle coordinate nascoste. Un percorso separato collega il dato originale alla loss come target auto-generato.

## Gate specifici

- non supervisionato non viene definito come assenza di obiettivo;
- self-supervised viene dichiarato come convenzione editoriale e non come tassonomia universale;
- k-means non viene presentato come scoperta automatica di categorie semantiche;
- l'indice di cluster non viene trattato come nome stabile;
- PCA e autoencoder sono distinti;
- reconstruction loss non viene interpretata come qualità downstream;
- maschera e augmentazione vengono trattate come parti dell'obiettivo;
- coppie positive e negative sono definite prima della loss contrastiva;
- collapse viene spiegato rispetto al metodo;
- pseudo-label distinte da label umane;
- linear probe distinto dal fine-tuning;
- label downstream distinte dalle label usate nel pretraining;
- gruppi segreti del generatore esclusi dal training;
- ponte a Capitolo 14 esplicito.
