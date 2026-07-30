# Protocollo di conformità didattica dei capitoli

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ambito: ogni capitolo, lezione, appendice tecnica e revisione sostanziale
- Fonte metodologica: `EXPLANATION_STYLE_AND_VISUALS.md`
- Artefatto di registrazione: `chapters/<capitolo>/TEXT_AUDIT.md`

## 1. Scopo

Questo protocollo rende obbligatoria una verifica esplicita della conformità di ogni capitolo ai principi di `EXPLANATION_STYLE_AND_VISUALS.md`.

La correttezza fattuale e matematica è necessaria, ma non è sufficiente. Un capitolo tecnicamente corretto viene respinto quando:

- introduce termini prima del referente concreto;
- salta passaggi necessari;
- accumula più concetti nuovi nella stessa transizione;
- usa formule o codice prima che il meccanismo sia stabile;
- non dichiara cambiamento, invariante e confine;
- tratta una visuale come elemento autonomo non attraversato dalla prosa;
- anticipa varianti o ottimizzazioni che interrompono il caso base;
- non permette al lettore di ricostruire e trasferire il meccanismo.

## 2. Regola minima di review

Ogni capitolo deve ricevere almeno una review didattica completa.

Quando la review individua anche un solo difetto bloccante:

1. il capitolo torna allo stato `revisione didattica`;
2. il difetto viene registrato in `TEXT_AUDIT.md`;
3. viene corretto il minimo insieme coerente di testo, visuali, formule e codice;
4. viene ripetuta l'intera review, non soltanto il controllo locale;
5. il ciclo continua finché non restano difetti bloccanti.

Ogni modifica successiva che altera ordine, terminologia, esempio, formula, visuale, codice, confine o variante riapre la review didattica.

## 3. Indipendenza della review

La review viene eseguita come se il reviewer non conoscesse l'intenzione dell'autore.

Il reviewer controlla ciò che il testo comunica realmente. Non può giustificare una giunzione mancante con informazioni presenti nel piano, nel prompt o nella memoria della conversazione.

Una frase, una figura o uno snippet deve essere comprensibile nel punto in cui compare usando soltanto i prerequisiti dichiarati e gli elementi già stabilizzati.

## 4. Passaggi obbligatori

### Passaggio A. Mappa dell'oggetto continuo

Registrare:

```text
Oggetto iniziale:
Stato accumulato dopo ogni sezione:
Output finale:
Consumer successivo:
```

Controllare che lo stesso oggetto attraversi il capitolo. Un cambio di esempio o di notazione deve essere motivato e non deve creare un secondo percorso portante.

### Passaggio B. Stato del lettore

Per ogni sezione portante verificare:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```

Una sezione non può dipendere da un concetto soltanto nominato o differito.

### Passaggio C. Catena dei sette punti

Verificare la presenza e l'ordine di:

1. stato iniziale;
2. problema;
3. motivo della nuova operazione;
4. trasformazione concreta;
5. stato risultante;
6. invariante;
7. elemento ancora mancante.

I punti non devono essere soltanto presenti nel capitolo. Devono essere collegati causalmente.

### Passaggio D. Blocco atomico

Per ogni trasformazione principale controllare:

```text
Dove siamo:
Problema:
Input e shape:
Trasformazione:
Output e shape:
Cosa è cambiato:
Cosa è rimasto invariato:
Cosa non fa:
Cosa usa l'output dopo:
Esempio minimo:
Errore comune:
Frase di continuità:
```

Le etichette possono essere integrate nella prosa, ma nessuna funzione del blocco può restare implicita quando è necessaria alla ricostruzione.

### Passaggio E. Gate di comparsa

Controllare in ordine:

- termine tecnico dopo il referente concreto;
- astrazione accompagnata da valori, oggetto, produttore e consumer;
- frecce dopo la spiegazione dei nodi e delle transizioni;
- esempio numerico e shape prima della formula generale;
- pseudocodice prima della formula compatta quando il capitolo descrive un algoritmo;
- codice eseguibile dopo il meccanismo indipendente dalla libreria;
- varianti e ottimizzazioni dopo il caso base.

Un termine presente nel titolo può essere inevitabile. I suoi sottocomponenti e il relativo contratto non vengono però usati come prerequisiti prima della loro introduzione.

### Passaggio F. Una trasformazione per passaggio

Per ogni paragrafo e sottosezione identificare la trasformazione principale.

La sezione viene divisa quando introduce contemporaneamente, per esempio:

- meccanismo matematico e semantica di un'API;
- caso base e ottimizzazione hardware;
- formula e benchmark;
- variante architetturale e failure mode indipendente;
- più relazioni che richiedono stati del lettore diversi.

### Passaggio G. Visuali attraversate dalla prosa

Ogni figura deve essere usata in tre fasi:

1. **Inquadra:** dichiara la domanda della figura.
2. **Ispeziona:** attraversa gli elementi nell'ordine di lettura.
3. **Conclude:** dichiara risultato, invariante e prossimo consumer.

Una frase come `la figura riassume il processo` non costituisce una ispezione sufficiente.

### Passaggio H. Codice integrato

Prima di ogni snippet verificare che il testo dichiari:

1. input già noto;
2. riga o gruppo minimo che implementa l'operazione centrale;
3. output o invariante da osservare.

Il codice non deve introdurre parametri, ottimizzazioni o varianti non ancora stabilizzate.

### Passaggio I. Confini e materiale differito

Un concetto differito può essere nominato per localizzare un confine. Non può essere spiegato a metà nel capitolo corrente.

Quando una sezione può essere spostata in un altro capitolo senza rompere l'oggetto continuo, il reviewer valuta se debba diventare:

- ponte di poche frasi;
- riferimento incrociato;
- sezione del capitolo successivo;
- approfondimento separato.

### Passaggio J. Prosa italiana

Controllare:

- italiano diretto, calmo e progressivo;
- soggetti e referenti espliciti;
- niente metafore, personificazioni o domande retoriche sostitutive;
- niente em dash;
- una trasformazione principale per paragrafo;
- seconda persona soltanto in controlli ed esercizi;
- termini inglesi usati in modo coerente;
- frasi non sovraccariche di input, operazione, output, eccezione e sviluppi futuri.

### Passaggio K. Controlli finali

Il capitolo deve permettere:

- ricostruzione;
- localizzazione;
- confine;
- trasferimento;
- variazione.

Se una domanda finale richiede informazioni non stabilizzate nel corpo, il capitolo o la domanda devono essere corretti.

## 5. Review in due passaggi consigliata

Per ridurre gli errori, la modalità predefinita è una review in due passaggi.

### Review 1. Struttura e gate

Controlla:

- oggetto continuo;
- stato del lettore;
- catena dei sette punti;
- blocchi atomici;
- gate di termini, formule, codice e varianti;
- continuità tra sezioni;
- confini e materiale differito;
- integrazione delle visuali.

### Review 2. Prosa e ricostruibilità

Dopo le correzioni, rilegge il capitolo integralmente e controlla:

- ordine reale delle operazioni;
- referenti;
- densità delle frasi;
- continuità;
- stato accumulato;
- esercizi;
- coerenza tra testo, formule, figure e codice;
- possibilità di ricostruire il meccanismo senza consultare il piano.

La seconda review non può limitarsi a confermare le correzioni della prima.

## 6. Registro in `TEXT_AUDIT.md`

Per ogni passaggio registrare:

```text
Review ID:
Versione esaminata:
Data:
Ambito:
Difetti bloccanti:
Difetti non bloccanti:
Correzioni applicate:
Artefatti riaperti:
Esito:
Reviewer:
```

Stati ammessi:

- `non eseguita`;
- `in corso`;
- `respinta`;
- `corretta, nuova review richiesta`;
- `superata`.

## 7. Difetti bloccanti

La review didattica viene respinta quando è presente almeno uno dei seguenti difetti:

- oggetto continuo interrotto senza motivazione;
- sezione che dipende da un concetto non stabilizzato;
- termine tecnico usato come spiegazione prima del referente;
- formula generale prima di esempio, shape e algoritmo necessari;
- codice prima del meccanismo;
- variante spiegata prima del caso base;
- più concetti nuovi inseparati nella stessa transizione;
- invariante necessario lasciato implicito;
- frase di continuità vaga o assente in una giunzione critica;
- visuale non inquadrata, non ispezionata o non conclusa;
- sezione spostabile che diluisce il capitolo portante;
- metafora o personificazione usata al posto dell'operazione reale;
- esercizio che richiede conoscenze non costruite nel capitolo;
- contraddizione tra prosa, formula, visuale e codice;
- semplificazione che modifica il meccanismo.

## 8. Gate di approvazione

Un capitolo può passare a `revisione autoriale` soltanto quando:

- almeno una review didattica completa è registrata;
- ogni difetto bloccante trovato è stato corretto;
- dopo le correzioni è stata eseguita una nuova review completa;
- `TEXT_AUDIT.md` indica lo stato `superata`;
- non restano concetti differiti usati come prerequisiti impliciti;
- testo, visuali e codice rispettano lo stesso percorso didattico.

L'approvazione autoriale può richiedere nuove modifiche. Ogni modifica strutturale riapre questo gate.

## 9. Applicazione retroattiva

Il protocollo si applica:

- a tutti i capitoli futuri;
- ai capitoli già approvati quando vengono modificati in modo sostanziale;
- ai capitoli esistenti prima di una nuova edizione;
- alle sezioni aggiunte per nuove tecniche o cambi di maturità.

Non è ammesso considerare conforme un capitolo soltanto perché segue il template nominale. La conformità viene dimostrata dall'esecuzione e dal registro della review.
