# Stile di spiegazione e visuali

## Stato

Metodo vincolante per ogni capitolo del libro.

- Lingua: italiano.
- Ambito: prosa, formule, esempi, immagini, tabelle, codice ed esercizi.
- Voce editoriale: `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.
- Struttura visibile: `19_STRUTTURA_LOGICA_IN_PROSA.md`.
- Review didattica: `18_PROTOCOLLO_QA_DIDATTICO.md`.
- Standard visuale: `17_STANDARD_VISIVO_CANONICO.md`.

## 1. Scopo

Ogni capitolo deve costruire un modello mentale che il lettore possa eseguire. Al termine della spiegazione il lettore deve saper:

- ricostruire il flusso;
- localizzare ogni componente;
- dire cosa entra e cosa esce;
- descrivere l'ordine reale delle operazioni;
- indicare shape e invarianti;
- prevedere cosa cambia quando viene modificato un elemento;
- spiegare i confini del meccanismo.

Riconoscere i termini non basta. La spiegazione riesce quando il lettore sa ripetere il meccanismo sul caso originale, trasferirlo a un caso modificato e delimitare ciò che non conclude.

## 2. Un oggetto continuo

Un oggetto concreto attraversa il capitolo dall'apertura alla ricostruzione finale.

Ogni passaggio principale:

1. parte dall'output del passaggio precedente;
2. introduce una sola distinzione, operazione o struttura dominante;
3. applica il nuovo elemento allo stesso esempio;
4. rende disponibile lo stato accumulato;
5. consegna il risultato al passaggio successivo.

La progressione deve poter essere ricostruita come:

```text
oggetto noto
-> oggetto noto più una distinzione
-> stato precedente più una operazione
-> stato precedente più un risultato
-> modello eseguibile completo
```

L'esempio non compare soltanto all'inizio e alla fine. Ogni nuova distinzione importante viene ricondotta all'oggetto che il lettore conosce già.

## 3. La catena causale

La spiegazione collega:

1. stato iniziale;
2. capacità mancante o vincolo;
3. motivo per cui viene introdotto il nuovo passaggio;
4. trasformazione concreta;
5. stato risultante;
6. invariante;
7. elemento ancora mancante.

Questi punti sono obbligatori nel significato, non come titoli ripetuti.

Lo scaffold interno viene registrato in `PLAN.md`:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Input e shape:
Operazione:
Output e shape:
Cosa cambia:
Cosa resta invariato:
Cosa non fa:
Consumer successivo:
Esempio o prova:
Errore comune:
Giunzione:
```

`CHAPTER.md` incorpora queste funzioni in paragrafi naturali.

## 4. Superficie da manuale

Il libro è un manuale tecnico, non una specifica o un registro di audit.

Il testo destinato al lettore usa:

- titoli semantici;
- sezioni costruite attorno a problemi e meccanismi;
- paragrafi causali;
- esempi continui;
- formule, visuali e codice nel punto in cui chiariscono il discorso;
- riepiloghi che ricompongono il problema iniziale.

Non usa come telaio ricorrente:

```text
Stato del lettore
Dove siamo
Problema locale
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

I dettagli operativi, lo stato editoriale e gli esiti delle review restano in commenti non renderizzati, front matter, `PLAN.md`, `TEXT_AUDIT.md`, `CHANGELOG.md` e `REVIEW.md`.

La voce completa è definita in `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

## 5. Sezioni e paragrafi

Una nuova sezione è giustificata quando cambia la domanda, l'oggetto, il livello di astrazione, la fase del processo o il tipo di evidenza. Non si crea un titolo per ogni micro-operazione.

Più passaggi brevi possono convivere nella stessa sezione se appartengono allo stesso movimento concettuale.

Ogni paragrafo possiede una trasformazione dominante, ma può collegare naturalmente:

- stato raggiunto;
- problema rimasto;
- operazione;
- conseguenza;
- limite necessario;
- passaggio successivo.

La prosa alterna periodi brevi e più articolati. Non usa sempre la stessa cadenza o la stessa frase di transizione.

## 6. Gate di comparsa

Ogni elemento nuovo entra dopo che il proprio referente concreto è stabile.

### Termini

Si descrive prima di nominare. Un termine tecnico compare quando il lettore ha visto l'oggetto o l'operazione e il testo gli assegna un significato stabile.

### Astrazioni

Parole come `rappresentazione`, `contesto`, `feature`, `memoria` ed `efficienza` richiedono un referente:

```text
quali valori
in quale oggetto
prodotti da quale operazione
usati da quale passaggio successivo
```

### Frecce

Le catene con frecce sono riassunti. Prima di mostrare `A -> B -> C`, il lettore deve sapere cosa sono i nodi, cosa rappresenta ogni freccia e cosa cambia.

### Formule

Quando pertinente, l'ordine è:

```text
domanda concreta
-> esempio osservabile
-> valori e shape
-> algoritmo o pseudocodice
-> formula generale
-> derivazione necessaria
```

Ogni simbolo deve avere prima una quantità concreta visibile.

### Codice

Il codice compare dopo che il meccanismo indipendente dalla libreria è stabile. Prima dello snippet, la prosa rende chiari input, operazione centrale e controllo atteso.

### Varianti

Varianti, ottimizzazioni ed eccezioni compaiono dopo il caso base. Un concetto necessario soltanto per segnare un confine viene nominato e rinviato.

## 7. Precisione e fonti

Una frase tecnica richiede una fonte primaria, documentazione ufficiale, una derivazione verificata o un risultato riprodotto.

Il testo distingue:

- fatto da fonte;
- derivazione;
- esempio illustrativo;
- risultato eseguito;
- confine.

Le inferenze fattuali editoriali non entrano nella versione approvata.

Le condizioni indispensabili restano nel corpo. I dettagli che interrompono il ragionamento, come ambiente completo, commit, comandi e tolleranze, restano negli artefatti di riproduzione.

## 8. Italiano tecnico naturale

La prosa deve sembrare scritta direttamente in italiano.

Regole:

- soggetti e referenti espliciti;
- nomi concreti e verbi operativi;
- termini inglesi soltanto quando sono lo standard tecnico;
- sintassi italiana anche in presenza di termini inglesi;
- niente calchi non necessari;
- niente hype;
- niente personificazioni sostitutive;
- niente em dash;
- seconda persona limitata a controlli ed esercizi;
- cautele e negazioni non ripetute oltre la loro funzione.

La lettura ad alta voce è parte della review. Una frase difficile da pronunciare o che suona come documentazione viene riscritta.

## 9. Visuali

Le visuali fanno parte della spiegazione. Ogni immagine risponde a una domanda principale.

La prosa:

1. introduce la domanda;
2. attraversa gli elementi nell'ordine di lettura;
3. esplicita il risultato e il passaggio successivo.

Le etichette `Domanda della figura` e `Conclusione della figura` non sono necessarie.

Produzione:

- strumento immagini;
- PNG ad alta risoluzione;
- sfondo bianco puro;
- orientamento adattato al contenuto;
- prima generazione sempre bozza;
- nessun watermark o branding;
- contenimento completo del testo;
- audit iterativo secondo i documenti visuali.

Non si crea un'immagine soltanto perché una sezione ne è priva.

## 10. Codice

Il codice collega il meccanismo a un'implementazione osservabile.

Ogni snippet:

- usa gli stessi nomi della prosa;
- dichiara input e shape;
- mostra una sola operazione centrale o un passaggio compatto;
- produce un output osservabile;
- verifica almeno un invariante;
- registra ambiente, versione, comando e test;
- non presenta output inventati come eseguiti.

Il corpo mostra soltanto la porzione utile alla spiegazione. Il file completo e i test restano nel repository.

## 11. Conclusione del capitolo

La chiusura non ripete una checklist. Riprende il problema iniziale, ricompone il meccanismo e mostra che cosa diventa possibile.

Ogni capitolo verifica:

- ricostruzione;
- localizzazione;
- confine;
- trasferimento;
- variazione.

Gli esercizi richiedono soltanto conoscenze costruite nel capitolo o dichiarate come prerequisiti.

## 12. Review obbligatorie

Ogni capitolo attraversa:

1. audit fattuale e matematico;
2. review didattica della sequenza e dei gate;
3. gate anti-template;
4. review editoriale e linguistica;
5. seconda lettura completa;
6. revisione autoriale.

Una correzione strutturale riapre le review interessate.

## Istruzione compatta

```text
Costruisci un modello mentale eseguibile attorno a un oggetto concreto. Introduci una trasformazione dominante per volta, ma scrivi come un manuale, non come una scheda. Nascondi lo scaffold senza nascondere logica, shape, invarianti e confini. Descrivi prima di nominare, mostra prima di formalizzare e stabilizza il meccanismo prima del codice. Usa un italiano tecnico naturale, verifica ogni affermazione e rileggi il capitolo ad alta voce. Mantieni metadati, audit e dettagli operativi fuori dal flusso destinato al lettore.
```
