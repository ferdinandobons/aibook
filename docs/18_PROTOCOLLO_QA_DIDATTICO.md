# Protocollo di conformità didattica dei capitoli

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ambito: ogni capitolo, lezione, appendice tecnica e revisione sostanziale
- Fonte metodologica: `EXPLANATION_STYLE_AND_VISUALS.md`
- Regola di superficie: `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Artefatto di registrazione: `chapters/<capitolo>/TEXT_AUDIT.md`

## 1. Scopo

Ogni capitolo deve risultare corretto sia nel contenuto sia nel modo in cui costruisce il modello mentale del lettore.

La logica di stato, problema, trasformazione, output, invariante e confine è obbligatoria. Le relative etichette non sono obbligatorie nella lezione pubblicata. Il reviewer controlla le funzioni della spiegazione, non la presenza nominale di una sequenza fissa di sottotitoli.

Un capitolo viene respinto quando:

- introduce termini prima del referente concreto;
- salta passaggi necessari;
- accumula più concetti nuovi nella stessa transizione;
- usa formule o codice prima che il meccanismo sia stabile;
- rende impliciti shape, invarianti o confini necessari;
- tratta una visuale come elemento autonomo;
- anticipa varianti che interrompono il caso base;
- espone lo scaffold di progettazione come struttura ripetitiva della lezione;
- non permette ricostruzione, trasferimento e variazione.

## 2. Regola minima di review

Ogni capitolo riceve almeno una review didattica completa. La modalità predefinita prevede due passaggi indipendenti.

Quando una review trova un difetto bloccante:

1. il capitolo torna allo stato `revisione didattica`;
2. il difetto viene registrato in `TEXT_AUDIT.md`;
3. vengono corretti tutti gli artefatti coinvolti;
4. l'intera review viene ripetuta;
5. il ciclo continua finché non restano difetti bloccanti.

Una modifica successiva a ordine, terminologia, esempio, formula, visuale, codice, confine o struttura visibile riapre il gate.

## 3. Indipendenza del reviewer

La review viene svolta come se il reviewer non conoscesse il piano o l'intenzione dell'autore.

Il capitolo deve funzionare usando soltanto:

- prerequisiti dichiarati;
- contenuto già stabilizzato;
- informazioni presenti nel testo, nelle figure e nel codice richiamato.

Il piano interno non può compensare una giunzione mancante nella prosa.

## 4. Doppio livello obbligatorio

### 4.1 Scaffold interno

In `PLAN.md` e `TEXT_AUDIT.md` devono essere ricostruibili:

```text
Ultima affermazione stabile
Oggetto corrente
Un concetto nuovo
Input e shape
Operazione
Output e shape
Cosa cambia
Cosa resta invariato
Cosa non fa
Consumer successivo
Esempio o prova
Errore comune
Giunzione
```

### 4.2 Superficie destinata al lettore

`CHAPTER.md` usa titoli semantici, paragrafi causali e transizioni naturali. Non deve ripetere sistematicamente le etichette dello scaffold.

Il reviewer deve poter compilare lo scaffold partendo dalla prosa. Il lettore non deve percepire di leggere uno scaffold compilato.

## 5. Passaggi obbligatori della review

### A. Oggetto continuo

Registrare:

```text
Oggetto iniziale:
Stato accumulato dopo ogni sezione:
Output finale:
Consumer successivo:
```

Lo stesso oggetto deve attraversare il capitolo. Un cambio di esempio o notazione richiede una motivazione.

### B. Stato del lettore

Per ogni sezione portante controllare internamente:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```

Questa scheda appartiene alla review. Non deve necessariamente comparire nel capitolo.

### C. Catena dei sette punti

Verificare la connessione causale di:

1. stato iniziale;
2. problema;
3. motivo della nuova operazione;
4. trasformazione concreta;
5. stato risultante;
6. invariante;
7. elemento ancora mancante.

La presenza di sette intestazioni omonime non dimostra la conformità.

### D. Funzioni del blocco atomico

Per ogni trasformazione il reviewer deve poter rispondere:

```text
Dove siamo?
Quale problema locale resta?
Quali input e shape sono disponibili?
Quale operazione viene applicata?
Quale output e shape risultano?
Che cosa cambia?
Che cosa resta invariato?
Che cosa non fa l'operazione?
Chi usa l'output?
Quale esempio o prova stabilizza il passaggio?
Quale errore è probabile?
Come continua il flusso?
```

Le risposte possono essere distribuite in uno o più paragrafi naturali. Non si richiedono sottotitoli letterali.

### E. Gate di comparsa

Controllare:

- termine tecnico dopo il referente concreto;
- astrazione accompagnata da oggetto, valori, produttore e consumer;
- frecce dopo la spiegazione dei nodi;
- esempio e shape prima della formula generale;
- pseudocodice prima della formula quando chiarisce un algoritmo;
- codice dopo il meccanismo indipendente dalla libreria;
- varianti e ottimizzazioni dopo il caso base.

### F. Una trasformazione per passaggio

Ogni paragrafo deve avere una trasformazione dominante. Si divide il testo quando combina:

- meccanismo matematico e semantica API;
- caso base e ottimizzazione hardware;
- formula e benchmark;
- variante e failure mode indipendente;
- più operazioni che richiedono stati diversi del lettore.

Questo controllo non impone una microsezione per ogni operazione. Più passaggi brevi possono vivere in una sezione semantica unica, purché la sequenza sia chiara.

### G. Visuali attraversate dalla prosa

Ogni figura viene:

1. inquadrata con la domanda a cui risponde;
2. ispezionata nell'ordine di lettura;
3. conclusa con risultato e passo successivo.

Le tre funzioni possono essere integrate in prosa. Le etichette `Domanda della figura` e `Conclusione della figura` non sono necessarie.

### H. Codice integrato

Prima di ogni snippet il testo deve rendere chiari:

- input già noto;
- righe o operazione centrale;
- output o invariante da osservare.

Queste informazioni possono essere in un paragrafo. Non è necessario pubblicare un box chiamato `Contratto dello snippet`.

### I. Confini e materiale differito

Un concetto differito può localizzare un confine, ma non viene spiegato a metà.

Una sezione spostabile senza rompere l'oggetto continuo deve essere valutata come:

- ponte breve;
- riferimento incrociato;
- capitolo successivo;
- approfondimento separato.

### J. Prosa italiana

Controllare:

- italiano diretto, calmo e progressivo;
- soggetti e referenti espliciti;
- niente metafore o personificazioni sostitutive;
- niente em dash;
- una trasformazione principale per paragrafo;
- seconda persona limitata a controlli ed esercizi;
- termini inglesi coerenti;
- frasi non sovraccariche;
- ritmo variato e adatto al contenuto.

### K. Gate anti-template

Il reviewer controlla che:

- i titoli descrivano oggetti e meccanismi reali;
- le intestazioni metacognitive non siano ripetute come telaio standard;
- la prosa non sembri una checklist trasformata in pagina;
- elenchi e box non sostituiscano una spiegazione fluida;
- capitoli di profilo diverso non vengano forzati nella stessa sagoma;
- la rimozione delle etichette non nasconda shape, invarianti o confini.

Sono segnali di problema intestazioni ricorrenti come:

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

Una singola etichetta può essere usata quando serve. La ripetizione sistematica viene respinta.

### L. Controlli finali

Il capitolo deve permettere:

- ricostruzione;
- localizzazione;
- confine;
- trasferimento;
- variazione.

## 6. Review in due passaggi

### Review 1. Struttura e gate

Controlla:

- oggetto continuo;
- catena dei sette punti;
- stato del lettore;
- funzioni del blocco atomico;
- gate di termini, formule, codice e varianti;
- confini;
- visuali;
- struttura visibile e gate anti-template.

### Review 2. Prosa e ricostruibilità

Dopo le correzioni, rilegge integralmente il capitolo e controlla:

- ordine reale delle operazioni;
- referenti;
- densità;
- ritmo;
- continuità;
- stato accumulato;
- naturalezza dei titoli;
- esercizi;
- coerenza tra testo, formule, figure e codice;
- ricostruibilità senza consultare il piano.

La seconda review non può limitarsi ai difetti già trovati.

## 7. Registro in `TEXT_AUDIT.md`

Ogni review registra:

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

## 8. Difetti bloccanti

La review viene respinta quando è presente almeno uno dei seguenti difetti:

- oggetto continuo interrotto;
- dipendenza da un concetto non stabilizzato;
- termine tecnico usato come spiegazione prima del referente;
- formula generale prima dei passaggi necessari;
- codice prima del meccanismo;
- variante prima del caso base;
- più concetti inseparati nella stessa transizione;
- invariante necessario implicito;
- giunzione critica vaga;
- visuale non attraversata dalla prosa;
- sezione spostabile che diluisce il percorso;
- metafora usata al posto dell'operazione;
- esercizio non costruito nel capitolo;
- contraddizione tra artefatti;
- semplificazione falsa;
- struttura pubblicata dominata da intestazioni metacognitive ripetute;
- lezione che appare come una checklist invece che come prosa tecnica.

## 9. Gate di approvazione

Un capitolo passa a `revisione autoriale` soltanto quando:

- almeno una review completa è registrata;
- ogni difetto bloccante è corretto;
- dopo le correzioni è stata eseguita una nuova review integrale;
- `TEXT_AUDIT.md` indica `superata`;
- il gate anti-template è superato;
- i concetti differiti non sono prerequisiti impliciti;
- testo, figure e codice seguono lo stesso percorso.

Ogni modifica strutturale successiva riapre il gate.

## 10. Applicazione retroattiva

Il protocollo si applica:

- a tutti i capitoli futuri;
- ai capitoli modificati in modo sostanziale;
- ai capitoli esistenti prima di una nuova edizione;
- alle sezioni aggiunte per nuove tecniche.

La conformità non deriva dal rispetto nominale del template. Deriva dalla qualità della spiegazione e dal registro delle review.