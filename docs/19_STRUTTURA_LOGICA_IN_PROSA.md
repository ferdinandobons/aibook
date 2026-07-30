# Struttura logica implicita nella prosa

## Stato

- Stato: `vincolante`
- Ambito: capitoli, lezioni e appendici destinati al lettore
- Voce editoriale: `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`
- Documenti collegati: `EXPLANATION_STYLE_AND_VISUALS.md`, `01_TEMPLATE_CAPITOLO.md`, `18_PROTOCOLLO_QA_DIDATTICO.md`

## 1. Principio

La struttura logica del metodo è obbligatoria. Le sue etichette non devono diventare la struttura visibile e ripetitiva delle lezioni.

Campi come:

```text
Dove siamo
Problema
Input e shape
Trasformazione
Output e shape
Cosa cambia
Cosa resta invariato
Cosa non fa
Consumer successivo
Errore comune
Giunzione
```

sono strumenti di progettazione e review. Per impostazione predefinita non diventano titoli o sottotitoli di `CHAPTER.md`.

Il lettore deve percepire una spiegazione continua, non il modulo usato dall'autore per controllarla.

## 2. Due livelli distinti

### Livello interno

`PLAN.md` e `TEXT_AUDIT.md` rendono espliciti:

- stato del lettore;
- problema locale;
- input e output;
- trasformazione;
- cambiamento;
- invariante;
- confine;
- passaggio successivo;
- concetti differiti.

Questi campi devono essere verificabili uno per uno.

### Livello destinato al lettore

`CHAPTER.md` usa:

- titoli legati al contenuto;
- sezioni costruite attorno a problemi e meccanismi;
- paragrafi causali;
- formule e tabelle nel punto in cui servono;
- transizioni naturali;
- box soltanto quando aggiungono valore;
- una conclusione che ricompone il problema iniziale.

La prosa integra le funzioni dello scaffold senza annunciarle.

## 3. Titoli

I titoli devono dire quale oggetto, problema o meccanismo viene esaminato.

Esempi:

```text
Perché una combinazione fissa non basta
Quando il comportamento viene appreso
Dagli score ai coefficienti
Escludere le posizioni future
Dalla formula a PyTorch
```

Da evitare come struttura ricorrente:

```text
Stato del lettore
Problema locale
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

Una di queste etichette può apparire eccezionalmente in un box o in una tabella. Non può costituire il telaio standard del libro.

## 4. Sezioni abbastanza ampie

Non si crea una nuova sezione per ogni micro-operazione.

Una sezione principale è giustificata quando cambia:

- la domanda;
- l'oggetto;
- il livello di astrazione;
- la fase del processo;
- il tipo di evidenza;
- il consumer del risultato.

Più passaggi brevi possono vivere nella stessa sezione se appartengono allo stesso movimento concettuale. Una sequenza numerica, per esempio, può descrivere confronto, scaling, normalizzazione e combinazione in un'unica sezione, purché ogni passaggio resti localizzabile.

Sono segnali di frammentazione:

- molte sezioni di uno o due paragrafi;
- un titolo per ogni riga di una formula;
- successioni `definizione -> cautela -> nuovo titolo`;
- un indice che sembra una checklist.

## 5. Paragrafi causali

Una transizione completa può occupare uno o più paragrafi naturali.

Esempio:

```text
I tre prodotti scalari forniscono uno score per ogni key, ma non ancora coefficienti utilizzabili: i valori possono essere negativi e non sommano a uno. Li dividiamo quindi per la radice della dimensione delle key e applichiamo la softmax. Otteniamo tre coefficienti associati alle stesse coppie key-value; soltanto a questo punto possiamo usarli per costruire l'output.
```

Il reviewer può ricostruire:

- stato corrente;
- problema;
- trasformazione;
- output;
- invariante;
- confine;
- passaggio successivo.

Il lettore vede invece un ragionamento continuo.

## 6. Ritmo

Le frasi non hanno tutte la stessa lunghezza o la stessa forma. La prosa alterna:

- frasi brevi per fissare un risultato;
- frasi medie per spiegare un passaggio;
- periodi più articolati per collegare condizioni e conseguenze.

Non si usa automaticamente `Ora che`, `A questo punto` o `Quindi` in ogni transizione. La giunzione resta concreta, ma varia nella forma.

Esempi:

```text
I tre score sono disponibili. Prima della softmax dobbiamo controllarne la scala.
```

```text
I coefficienti restano associati alle stesse value; possiamo quindi usarli per costruire il vettore di output.
```

```text
Il caso numerico è completo e può ora essere espresso in forma matriciale.
```

## 7. Shape, invarianti e confini

Shape, invarianti e confini devono essere espliciti nel significato, non necessariamente nel titolo.

Forme adatte:

```text
Il vettore mantiene shape [S]: cambia la magnitudine degli score, non il numero di posizioni.
```

```text
La mask interviene sugli score prima della softmax; le righe di V restano invariate.
```

```text
L'operazione combina le value disponibili e non introduce informazione esterna.
```

Le cautele indispensabili restano vicino al meccanismo. Le precisazioni secondarie vengono raccolte in un box o rinviate.

## 8. Esempio continuo

L'esempio non viene abbandonato durante le definizioni astratte. Ogni passaggio importante torna al caso noto.

Quando due oggetti hanno valori numerici identici soltanto per semplificare i conti, la prosa lo dichiara. Il lettore non deve confondere identità numerica e identità concettuale.

## 9. Codice e visuali

Prima di uno snippet, input, operazione centrale e controllo atteso vengono spiegati in prosa. Il contratto completo resta negli artefatti del codice.

Una figura viene introdotta, letta e conclusa nel testo vicino. Non servono etichette come `Domanda della figura` o `Conclusione della figura`, purché le funzioni siano chiaramente presenti.

I dettagli di ambiente, versione, log e tolleranze non interrompono il ragionamento principale. Vengono rinviati ai materiali di riproduzione.

## 10. Metadati invisibili al lettore

Stato editoriale, versione candidata, date, audit, branch e commit non appartengono al flusso del manuale.

Possono essere conservati:

- in un commento HTML all'inizio del file;
- in front matter non renderizzato;
- in `PLAN.md`, `TEXT_AUDIT.md`, `CHANGELOG.md` e `REVIEW.md`.

`CHAPTER.md` non apre con una scheda di lavorazione e non chiude con un registro di approvazione.

## 11. Gate anti-template

La review respinge un capitolo quando:

- ripete sistematicamente le stesse intestazioni metacognitive;
- espone lo scaffold al posto di una spiegazione;
- spezza un meccanismo semplice in troppe microsezioni;
- usa elenchi e box dove la prosa sarebbe più chiara;
- rende capitoli diversi formalmente identici;
- nasconde shape, invarianti o confini dopo aver rimosso le etichette;
- contiene metadati di progetto nel percorso di lettura;
- suona come una specifica, una reference API o un audit.

La correzione non elimina la logica. Trasferisce la logica dalla superficie editoriale alla costruzione della prosa.

## 12. Regola di approvazione

Un capitolo può essere approvato soltanto quando:

1. il reviewer può ricostruire lo scaffold leggendo il testo;
2. il lettore non vede lo scaffold come una sequenza rigida;
3. le sezioni hanno ampiezza proporzionata al contenuto;
4. la prosa supera la review linguistica e la lettura ad alta voce;
5. i materiali operativi restano separati dal manuale.

La conformità viene registrata in `TEXT_AUDIT.md`.
