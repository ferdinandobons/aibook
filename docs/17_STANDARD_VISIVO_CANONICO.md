# Standard visivo canonico delle immagini tecniche

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ambito: tutte le immagini tecniche dell'opera
- Formato principale: PNG ad alta risoluzione
- Strumento di produzione: strumento immagini
- Sfondo canonico: bianco puro `#FFFFFF`
- Documenti collegati: `02_TEMPLATE_VISUALE.md`, `03_PROTOCOLLO_QA_VISUALE.md`, `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`, `EXPLANATION_STYLE_AND_VISUALS.md`

## 1. Scopo

Questo documento definisce la grammatica visiva comune dell'intero libro.

Le immagini non devono avere tutte la stessa sagoma. Devono però appartenere alla stessa famiglia editoriale e condividere:

- gerarchia tipografica;
- sfondo;
- palette semantica;
- stile dei box;
- stile delle frecce;
- spaziature;
- regole di contenimento;
- criteri di densità;
- processo di audit.

La regola generale è:

> Le immagini condividono una stessa grammatica visiva, non una stessa composizione rigida.

## 2. Priorità e rapporto con gli altri documenti

Per le immagini raster tecniche del libro, questo documento è la fonte canonica per:

- sfondo;
- orientamento;
- palette;
- componenti grafici;
- tipografia;
- layout;
- adattamento al contenuto.

`16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` resta la fonte canonica per overflow, clipping, padding e appartenenza del testo.

`03_PROTOCOLLO_QA_VISUALE.md` resta la fonte canonica per generazione, review, rigenerazione e approvazione.

Quando un'indicazione visuale precedente è incompatibile con questo documento, per le figure raster del libro prevale questo standard.

## 3. Regole non negoziabili

Ogni immagine tecnica deve rispettare tutte le regole seguenti:

1. sfondo completamente bianco `#FFFFFF`;
2. nessuna texture di pagina;
3. nessun gradiente di sfondo;
4. nessuna tinta grigia, crema o colorata usata come fondo globale;
5. una sola domanda didattica principale;
6. ordine di lettura evidente;
7. testo integralmente contenuto nei propri box;
8. nessuna freccia o linea ambigua;
9. significato non affidato al solo colore;
10. simboli, shape e nomi coerenti con il capitolo;
11. nessun watermark, firma o branding di terzi;
12. nessuna renderizzazione completa della pagina del libro usata come figura tecnica.

Una violazione di uno di questi punti impedisce l'approvazione.

## 4. Orientamento

L'orientamento non è fisso.

Sono ammessi:

- orientamento orizzontale;
- orientamento verticale.

La scelta dipende dal contenuto e deve essere registrata in `SPEC.md`.

### 4.1 Quando preferire l'orientamento orizzontale

Usare normalmente l'orientamento orizzontale per:

- pipeline da sinistra a destra;
- confronti tra due o più approcci;
- sequenze di operazioni;
- trasformazioni tensoriali;
- diagrammi con rami paralleli;
- esempi numerici articolati in step.

### 4.2 Quando preferire l'orientamento verticale

Usare normalmente l'orientamento verticale per:

- stack architetturali;
- flussi top-down o bottom-up;
- tassonomie gerarchiche;
- processi con molte fasi sequenziali;
- figure destinate a occupare una colonna;
- contenuti che richiedono box larghi su più righe.

### 4.3 Criterio di scelta

L'orientamento scelto deve ridurre:

- lunghezza e tortuosità delle frecce;
- numero di incroci;
- densità per pannello;
- rischio di overflow;
- distanza tra un'operazione e il suo output.

Non si forza un layout orizzontale o verticale quando l'altra soluzione rende il meccanismo più chiaro.

## 5. Famiglie visuali canoniche

Ogni figura dichiara una famiglia primaria.

### 5.1 Diagramma di processo

Serve per:

- pipeline;
- algoritmi;
- training;
- inference;
- retrieval;
- agent loop;
- serving.

Forma tipica:

```text
input -> operazione 1 -> operazione 2 -> output
```

### 5.2 Diagramma comparativo

Serve per:

- baseline e modifica;
- due architetture;
- MHA, MQA e GQA;
- pre-norm e post-norm;
- dense e MoE;
- metodo corretto ed errore comune.

I pannelli confrontati devono condividere scala, input e livello di dettaglio.

### 5.3 Diagramma architetturale

Serve per:

- moduli;
- blocchi;
- stack;
- residual path;
- routing;
- memoria;
- interfacce tra sottosistemi.

Ogni collegamento deve rappresentare un flusso, una dipendenza o un vincolo dichiarato.

### 5.4 Diagramma tensoriale e delle shape

Serve per:

- matrici;
- reshape;
- transpose;
- split e concat;
- batching;
- proiezioni;
- KV cache;
- parallelismi.

Le shape devono essere visibili vicino al tensor pertinente.

### 5.5 Esempio numerico didattico

Serve per mostrare un calcolo completo con numeri piccoli.

Deve distinguere:

- valore esatto;
- valore approssimato;
- operazione;
- risultato intermedio;
- output;
- invariante verificato.

### 5.6 Tassonomia o mappa concettuale

Serve per classificare famiglie, varianti o metodi.

La gerarchia deve essere determinata dalla relazione tecnica, non dalla notorietà dei prodotti.

### 5.7 Grafico quantitativo

Serve per dati misurati con assi, unità, setup e fonte dichiarati.

Un grafico quantitativo non può essere costruito con numeri inventati. I dati illustrativi devono essere presentati come esempio concettuale, non come misura.

## 6. Struttura canonica della figura

Una figura può includere i componenti seguenti.

### 6.1 Titolo

Formato raccomandato:

```text
<FIG-ID> · <titolo descrittivo>
```

Esempio:

```text
ATT-02 · Esempio numerico di scaled dot-product attention
```

Il titolo descrive il meccanismo o la domanda, non usa slogan.

### 6.2 Sottotitolo

Il sottotitolo delimita l'esempio, la variante o le dimensioni.

Esempio:

```text
Esempio con d_k = d_v = 2 e una sola query
```

### 6.3 Corpo

Il corpo usa una delle famiglie visuali canoniche.

### 6.4 Footer tecnico opzionale

Il footer può contenere:

- invariante;
- riepilogo delle shape;
- confine;
- provenienza dei valori;
- nota di continuità.

Il footer non deve introdurre un nuovo meccanismo.

## 7. Griglia, margini e spaziatura

La composizione usa una griglia visibile attraverso gli allineamenti.

Regole:

- margine esterno ampio e uniforme;
- distanza costante tra pannelli equivalenti;
- allineamento comune dei titoli dei pannelli;
- box con la stessa funzione della stessa altezza o larghezza, quando possibile;
- spazio sufficiente tra frecce e testo;
- nessun elemento sospeso senza relazione visiva;
- nessun box addossato al limite dell'immagine.

La figura deve conservare una zona di sicurezza lungo tutti i bordi esterni.

## 8. Sfondo

Lo sfondo globale è sempre:

```text
#FFFFFF
```

Non sono ammessi:

- gradienti;
- vignettature;
- texture;
- carta simulata;
- ombre diffuse sull'intero canvas;
- fondi grigi o color crema;
- pannelli che coprono l'intera immagine con una tinta diversa dal bianco.

I singoli box possono usare riempimenti pastello molto chiari secondo la palette semantica.

## 9. Palette semantica

La palette deve restare riconoscibile in tutti i capitoli.

| Ruolo | Colore principale | Riempimento chiaro | Uso |
|---|---|---|---|
| Testo principale | `#0F172A` | `#FFFFFF` | titoli, formule, label |
| Testo secondario | `#475569` | `#FFFFFF` | sottotitoli, note |
| Bordo neutro | `#CBD5E1` | `#F8FAFC` | contenitori neutri |
| Blu | `#2563EB` | `#EFF6FF` | input, flusso principale, step base |
| Viola | `#7C3AED` | `#F5F3FF` | trasformazione corrente, attention, normalizzazione |
| Verde | `#16A34A` | `#F0FDF4` | output, risultato verificato, stato valido |
| Ambra | `#D97706` | `#FFFBEB` | vincolo, shape, nota tecnica, invariante |
| Rosso | `#DC2626` | `#FEF2F2` | errore, limite, percorso invalido |

Regole:

- massimo quattro o cinque ruoli cromatici attivi nella stessa figura;
- ogni colore è accompagnato da label, posizione o forma;
- il rosso non viene usato come semplice decorazione;
- il verde non significa automaticamente `Verificato` senza evidenza;
- tonalità e saturazione possono essere adattate leggermente, ma il ruolo semantico non cambia.

## 10. Tipografia

### 10.1 Famiglia

Usare una famiglia sans-serif pulita e leggibile.

Formule, nomi di tensor, shape e codice possono usare una variante matematica o monospace chiaramente distinta.

### 10.2 Gerarchia

Ordine tipografico:

1. titolo della figura;
2. sottotitolo;
3. titolo del pannello;
4. label del nodo;
5. testo tecnico;
6. nota e footer.

### 10.3 Regole

- evitare paragrafi lunghi nei box;
- usare label brevi e tecnicamente precise;
- non ridurre il font per salvare un layout sovraccarico;
- preservare pedici, apici, simboli e lettere greche;
- usare gli stessi nomi del testo e del codice;
- verificare la leggibilità alla dimensione editoriale prevista.

## 11. Box e contenitori

I box condividono:

- angoli moderatamente arrotondati;
- bordo sottile e netto;
- riempimento chiaro;
- padding visibile;
- testo allineato coerentemente;
- nessuna ombra pesante.

Box con ruolo uguale devono avere uno stile uguale.

Il contenimento del testo segue integralmente `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`.

## 12. Frecce e linee

### 12.1 Flusso principale

- linea continua;
- spessore coerente;
- punta visibile;
- origine e destinazione sul bordo corretto dei nodi.

### 12.2 Vincolo o relazione opzionale

Può usare una linea tratteggiata, ma deve avere una label testuale.

### 12.3 Annotazione

Una callout line deve essere visivamente diversa dal flusso dati.

### 12.4 Regole bloccanti

- nessuna freccia termina nello spazio vuoto;
- nessuna linea sembra entrare nel box sbagliato;
- nessun incrocio sembra una giunzione;
- nessuna freccia attraversa una label;
- nessun ramo riutilizza una linea senza origine comune esplicita.

## 13. Formule, simboli e shape

- stessa notazione del capitolo;
- simboli definiti prima nella prosa;
- formule brevi nei box;
- formule lunghe in un contenitore dedicato;
- shape vicine all'oggetto a cui appartengono;
- decimali e arrotondamenti coerenti;
- nessun simbolo troncato;
- nessun macro o comando LaTeX mostrato letteralmente;
- nessuna formula generata senza verifica matematica.

## 14. Densità informativa

Una figura risponde a una sola domanda principale.

La figura deve essere divisa quando contiene contemporaneamente più di una trasformazione non ancora stabilizzata.

Segnali di densità eccessiva:

- più percorsi di lettura plausibili;
- testo ridotto per far entrare il contenuto;
- numerosi incroci;
- più di un esempio numerico completo;
- baseline, variante, benchmark e failure mode nello stesso pannello;
- footer che introduce un nuovo argomento;
- box con paragrafi invece di label.

## 15. Adattamento consentito

È consentito modificare:

- orientamento;
- numero di pannelli;
- proporzioni del canvas;
- quantità di formule;
- presenza del footer;
- disposizione locale dei nodi;
- densità, entro i limiti di leggibilità.

Non è consentito modificare:

- sfondo bianco puro;
- significato della palette;
- gerarchia tipografica;
- stile generale dei box;
- logica delle frecce;
- regole di contenimento;
- audit obbligatorio;
- assenza di branding esterno.

## 16. Accessibilità

Ogni figura deve avere:

- alt text;
- equivalente testuale esteso;
- ordine di lettura dichiarato;
- label che non dipendono dal colore;
- contrasto sufficiente;
- dimensione del testo verificata;
- contenuto comprensibile anche in scala di grigi, quando possibile.

## 17. Nomi dei file e stati

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

`final.png` viene creato soltanto dopo:

- audit tecnico positivo;
- audit compositivo positivo;
- controllo del contenimento;
- verifica dello sfondo bianco;
- approvazione autoriale.

## 18. Checklist stilistica obbligatoria

Prima dell'approvazione verificare:

- [ ] sfondo globale esattamente bianco;
- [ ] nessun gradiente o texture;
- [ ] orientamento motivato dal contenuto;
- [ ] famiglia visuale dichiarata;
- [ ] titolo e sottotitolo coerenti;
- [ ] palette semantica rispettata;
- [ ] box coerenti tra loro;
- [ ] frecce non ambigue;
- [ ] testo integralmente contenuto;
- [ ] padding visibile;
- [ ] formule e shape corrette;
- [ ] ordine di lettura unico;
- [ ] densità adeguata;
- [ ] leggibilità alla dimensione prevista;
- [ ] alt text ed equivalente testuale presenti;
- [ ] nessun watermark, firma o branding;
- [ ] immagine tecnica, non mockup di una pagina completa.

## 19. Regola di revisione

La prima generazione è sempre una bozza.

Dopo ogni correzione si ripete l'intero audit, compresi:

- contenimento;
- stile;
- collegamenti;
- formule;
- numeri;
- shape;
- densità;
- accessibilità.

Una correzione locale non autorizza l'approvazione automatica del resto della figura.
