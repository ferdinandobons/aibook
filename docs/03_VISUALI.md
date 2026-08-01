# Visuali tecniche: standard, specifica e qualità

## Stato

- Stato: `vincolante`
- Ambito: tutte le immagini tecniche del libro
- Formato principale: PNG ad alta risoluzione
- Strumento di produzione: strumento immagini
- Sfondo canonico: bianco puro `#FFFFFF`

## 1. Principio

Le immagini condividono una stessa grammatica visiva, non una stessa composizione rigida.

Ogni figura deve ridurre l'ambiguità. Una linea collegata al punto sbagliato, una label che esce dal box o una formula compressa possono alterare il modello mentale del lettore anche quando l'immagine appare gradevole.

La prima generazione è sempre una bozza.

## 2. Regole non negoziabili

Ogni immagine tecnica:

1. usa sfondo completamente bianco `#FFFFFF`;
2. non usa texture, gradiente, carta simulata o fondo globale colorato;
3. risponde a una sola domanda didattica principale;
4. presenta un ordine di lettura evidente;
5. mantiene testo e simboli integralmente nei contenitori;
6. non contiene frecce o linee ambigue;
7. non affida il significato al solo colore;
8. usa simboli, shape e nomi coerenti con il capitolo;
9. non contiene watermark, firma o branding di terzi;
10. non è un render della pagina del libro, uno screenshot del repository o un mockup editoriale.

Una violazione blocca l'approvazione.

## 3. Orientamento

Sono ammessi orientamento orizzontale e verticale. La scelta viene registrata in `SPEC.md` e dipende dal contenuto.

### Orizzontale

Adatto a:

- pipeline da sinistra a destra;
- confronti paralleli;
- trasformazioni tensoriali;
- esempi numerici a step;
- rami che procedono in parallelo.

### Verticale

Adatto a:

- stack architetturali;
- flussi top-down o bottom-up;
- tassonomie gerarchiche;
- processi con molti livelli;
- figure destinate a una colonna;
- box che richiedono più righe.

L'orientamento scelto deve ridurre:

- lunghezza e tortuosità delle frecce;
- incroci;
- densità;
- rischio di overflow;
- distanza tra operazione e output.

Si cambia orientamento quando il canvas costringe a ridurre il font, creare box stretti, spezzare formule o avvicinare il testo ai bordi.

## 4. Famiglie visuali

Ogni figura dichiara una famiglia primaria.

### 4.1 Processo

Per pipeline, training, inference, retrieval, agent loop e serving.

```text
input -> operazione -> operazione -> output
```

### 4.2 Confronto

Per baseline e modifica, due architetture, pre-norm/post-norm, dense/MoE, metodo corretto/errore.

I pannelli condividono input, scala e livello di dettaglio.

### 4.3 Architettura

Per moduli, stack, residual path, routing, memoria e interfacce. Ogni collegamento rappresenta un flusso, una dipendenza o un vincolo dichiarato.

### 4.4 Tensor e shape

Per matrici, reshape, transpose, split, concat, batching, proiezioni, cache e parallelismi. Le shape sono vicine all'oggetto pertinente.

### 4.5 Esempio numerico

Per calcoli completi con numeri piccoli. Distingue valore esatto, approssimazione, operazione, risultato intermedio, output e invariante.

### 4.6 Tassonomia

Per famiglie, varianti e metodi. La gerarchia deriva dalla relazione tecnica, non dalla notorietà dei prodotti.

### 4.7 Grafico quantitativo

Per dati misurati con assi, unità, setup e fonte. Numeri illustrativi non vengono presentati come misure.

## 5. Struttura della figura

Una figura può includere:

- titolo nel formato `<FIG-ID> · <titolo descrittivo>`;
- sottotitolo che delimita esempio o dimensioni;
- corpo appartenente a una famiglia canonica;
- footer tecnico opzionale con invariante, shape, confine o provenienza.

Il footer non introduce un nuovo meccanismo.

## 6. Palette semantica

| Ruolo | Colore | Riempimento | Uso |
|---|---|---|---|
| Testo principale | `#0F172A` | `#FFFFFF` | titoli, formule, label |
| Testo secondario | `#475569` | `#FFFFFF` | sottotitoli e note |
| Neutro | `#CBD5E1` | `#F8FAFC` | contenitori neutri |
| Blu | `#2563EB` | `#EFF6FF` | input, flusso principale, step base |
| Viola | `#7C3AED` | `#F5F3FF` | trasformazione corrente, attention, normalizzazione |
| Verde | `#16A34A` | `#F0FDF4` | output, risultato verificato, stato valido |
| Ambra | `#D97706` | `#FFFBEB` | vincolo, shape, nota tecnica, invariante |
| Rosso | `#DC2626` | `#FEF2F2` | errore, limite, percorso invalido |

Regole:

- massimo quattro o cinque ruoli cromatici attivi;
- ogni colore è accompagnato da label, posizione o forma;
- rosso e verde non vengono usati come decorazione;
- il ruolo semantico non cambia tra capitoli.

## 7. Tipografia

- famiglia sans-serif pulita e leggibile;
- matematica, tensor, shape e codice possono usare stile distinto;
- gerarchia: titolo, sottotitolo, titolo pannello, label nodo, testo tecnico, note;
- niente paragrafi lunghi nei box;
- label brevi e precise;
- font non ridotto per salvare un layout sovraccarico;
- pedici, apici, lettere greche e simboli completamente visibili;
- stessi nomi della prosa e del codice;
- leggibilità verificata alla dimensione editoriale.

## 8. Box e contenitori

I box condividono:

- angoli moderatamente arrotondati;
- bordo sottile e netto;
- riempimento chiaro;
- padding visibile;
- allineamento coerente;
- nessuna ombra pesante.

Box con lo stesso ruolo usano lo stesso stile.

Sono contenitori anche celle, badge, callout, pannelli, nodi, aree per formule, titoli di pannello e footer.

## 9. Contenimento del testo

Ogni testo appartiene in modo inequivocabile a un solo contenitore e resta integralmente entro il bordo.

Una figura è approvabile soltanto quando:

1. nessun carattere oltrepassa o tocca il bordo;
2. nessun carattere viene tagliato dal box o dal canvas;
3. resta margine interno visibile su tutti i lati;
4. nessuna label invade un contenitore vicino;
5. il testo non si sovrappone a frecce, simboli o altro testo;
6. pedici, apici, segni e accenti sono visibili;
7. l'appartenenza semantica resta chiara senza colore;
8. la leggibilità è verificata alla dimensione editoriale;
9. il raster effettivo viene ispezionato dopo la generazione;
10. titolo e sottotitolo rispettano la zona di sicurezza.

### 9.1 Ordine delle correzioni

Quando il testo non entra:

1. aumentare il contenitore;
2. ridisporre i nodi;
3. provare l'orientamento alternativo;
4. inserire ritorni a capo intenzionali;
5. accorciare la label senza perdere precisione;
6. spostare dettagli nella prosa o nell'alt text;
7. dividere la figura.

Ridurre il font è l'ultima opzione e non può compromettere la leggibilità.

## 10. Frecce e linee

### Flusso principale

- linea continua;
- spessore coerente;
- punta visibile;
- origine e destinazione sul bordo corretto.

### Vincolo o relazione opzionale

Può usare linea tratteggiata, accompagnata da label.

### Annotazione

Una callout line deve essere diversa dal flusso dati.

### Difetti bloccanti

- freccia che termina nello spazio vuoto;
- linea che sembra entrare nel box sbagliato;
- incrocio che sembra una giunzione;
- freccia che attraversa una label;
- ramo senza origine comune;
- annotazione scambiabile per flusso;
- mask, residual, skip e feedback non distinguibili.

## 11. Formule, simboli e shape

- stessa notazione del capitolo;
- simboli definiti nella prosa;
- formule brevi nei box, formule lunghe in area dedicata;
- shape vicine al tensor;
- decimali e arrotondamenti coerenti;
- nessun simbolo troncato;
- nessun comando LaTeX mostrato letteralmente;
- nessuna formula senza verifica matematica.

## 12. Densità

Una figura risponde a una domanda principale. Deve essere divisa quando contiene più trasformazioni non ancora stabilizzate.

Segnali di eccesso:

- più percorsi di lettura plausibili;
- font ridotto;
- molti incroci;
- più esempi numerici completi;
- baseline, variante, benchmark e failure mode nello stesso pannello;
- footer che introduce un nuovo argomento;
- box con paragrafi anziché label.

## 13. Accessibilità

Ogni figura ha:

- alt text;
- equivalente testuale esteso;
- ordine di lettura dichiarato;
- label non dipendenti dal colore;
- contrasto sufficiente;
- dimensione del testo verificata;
- comprensibilità in scala di grigi, quando possibile.

## 14. `SPEC.md`

Ogni visuale registra:

```text
ID:
Capitolo:
Sezione:
Famiglia:
Orientamento:
Motivazione:
Stato:
Domanda unica:
Oggetto già noto:
Trasformazione nuova:
Stato dopo:
Invariante:
Confine:
Passaggio successivo:
Nodi:
Frecce:
Label:
Shape:
Valori illustrativi:
Valori misurati:
Formula:
Direzione di lettura:
Numero di pannelli:
Griglia:
Zona di sicurezza:
Elementi uniformi:
Incroci vietati:
Testo esatto di ogni box:
Numero massimo di righe:
Padding minimo:
Dimensione minima:
Palette usata:
Fonte del meccanismo:
Fonte dei valori:
Alt text:
Equivalente testuale:
```

## 15. Ciclo di produzione

### 15.1 Specifica

Prima della generazione vengono fissati domanda, famiglia, orientamento, nodi, frecce, shape, valori, invariante, confine, label, ordine di lettura e contenimento.

### 15.2 Generazione

Il prompt richiede esplicitamente:

- sfondo bianco;
- assenza di gradienti e texture;
- orientamento previsto;
- ordine di lettura;
- origine e destinazione delle frecce;
- gerarchia tipografica;
- palette;
- contenimento completo;
- padding visibile;
- assenza di watermark e branding.

La prima bozza si chiama `candidate-v1.png` o equivalente, mai `final.png`.

### 15.3 Audit tecnico indipendente

La figura viene riletta senza usare il prompt. Si controllano:

- formule;
- numeri;
- shape;
- frecce;
- rami e ricomposizioni;
- mask e residual path;
- label;
- contenimento;
- notazione;
- distinzione tra valori illustrativi e misurati.

### 15.4 Audit stilistico

Si controllano sfondo, orientamento, famiglia, titolo, palette, box, tipografia, assenza di ombre pesanti, branding e mockup.

### 15.5 Audit compositivo

Si controllano ordine di lettura, spazi, contrasto, allineamento, densità, sovrapposizioni, lunghezza delle frecce, leggibilità in scala, padding e zona di sicurezza.

La figura viene ispezionata sia ingrandita sia alla dimensione prevista nel libro.

### 15.6 Nuova iterazione

Dopo ogni modifica si ripete l'intero audit. Una correzione locale può introdurre nuovi difetti.

## 16. Stati e verdetti

Stati ammessi:

```text
storyboard
candidate-v1.png
candidate-v2.png
da modificare
da rigenerare
validata tecnicamente
approvata
final.png
```

- `da rigenerare`: struttura, orientamento, stile o collegamenti non recuperabili localmente;
- `da modificare`: problema circoscritto;
- `validata tecnicamente`: contenuto, testo, stile e collegamenti corretti;
- `approvata`: validata tecnicamente e approvata dall'autore.

`final.png` esiste soltanto dopo audit tecnico, audit compositivo, contenimento, sfondo bianco e approvazione autoriale.

## 17. Difetti bloccanti

- collegamento errato o ambiguo;
- formula o numero errato;
- shape incompatibile;
- testo alterato, illeggibile, tagliato o fuori dal box;
- label che invade una cella;
- testo sovrapposto a linee o simboli;
- padding insufficiente;
- pedice, apice o glifo nascosto;
- sfondo non bianco;
- gradiente o texture globale;
- orientamento che comprime il testo;
- stile incompatibile;
- mask sul tensor sbagliato;
- incrocio che sembra giunzione;
- nodo senza origine o destinazione;
- colore come unico significato;
- densità senza ordine unico;
- contenuto incoerente con fonti, prosa o codice;
- watermark o branding;
- pagina completa presentata come figura.

## 18. File

Prima dell'approvazione:

```text
assets/chapters/<capitolo>/<FIG-ID>/
  candidate-v1.png
  candidate-v2.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

Dopo l'approvazione:

```text
assets/chapters/<capitolo>/<FIG-ID>/
  final.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

Le bozze respinte possono restare fuori dal repository. `AUDIT.md` registra iterazioni, problemi, correzioni e verdetto.

## 19. Checklist finale

- [ ] sfondo esattamente bianco;
- [ ] nessun gradiente o texture;
- [ ] orientamento motivato;
- [ ] famiglia dichiarata;
- [ ] titolo e sottotitolo coerenti;
- [ ] palette semantica rispettata;
- [ ] box coerenti;
- [ ] frecce non ambigue;
- [ ] testo integralmente contenuto;
- [ ] padding visibile;
- [ ] formule, numeri e shape corretti;
- [ ] ordine di lettura unico;
- [ ] densità adeguata;
- [ ] leggibilità alla dimensione prevista;
- [ ] alt text ed equivalente testuale;
- [ ] nessun watermark o branding;
- [ ] immagine tecnica, non mockup;
- [ ] nuova review completa dopo l'ultima correzione;
- [ ] approvazione tecnica;
- [ ] approvazione autoriale.
