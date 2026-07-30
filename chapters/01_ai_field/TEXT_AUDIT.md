# Audit del testo. Capitolo 1

## Stato

- Versione corrente: `0.3.0-rc2`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, claim e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e tecnico: **superato per testo e codice**
- Esito didattico: **superato**
- Esito di chiarezza per lettore non esperto: **superato dopo riscrittura e seconda lettura**
- Esito editoriale e linguistico: **superato**
- Esito visuale: **aperto**
- Review autoriale completa: non aperta

## `DID-AI-01`. Accuratezza e gate di comparsa

- Versione: `0.1.0-draft1`
- Esito: **respinta**

Difetti principali:

1. confine troppo ampio tra automazione ordinaria e sistema di AI;
2. definizione OECD non separata dalla tassonomia editoriale;
3. distinzione discriminativo/generativo incompleta;
4. convenzione `modello/sistema` poco chiara;
5. relatività di `generalista` e `specialistico` poco esplicita;
6. rischio di presentare la diminuzione della loss come generalizzazione;
7. candidate visuali non pertinenti.

Correzioni nella versione `0.1.1-draft2`:

- ristretto il confine definitorio;
- attribuite le definizioni alle fonti;
- estesa la distinzione probabilistica;
- chiarita la convenzione modello/sistema;
- dichiarata la relatività dell'ampiezza;
- separato il risultato eseguito dalla generalizzazione;
- respinte le visuali estranee.

## `DID-AI-02`. Seconda lettura tecnica e didattica

- Versione: `0.1.1-draft2`
- Esito tecnico: **superato**

Controlli superati:

- oggetto continuo presente;
- termini introdotti dopo i referenti;
- codice dopo parametri, training e inference;
- fonti e limiti coerenti;
- formule e risultati allineati al codice;
- gate anti-template nominalmente superato.

Problema non rilevato:

Il capitolo restava simile a un dossier tecnico. Metadati visibili, numerose sezioni brevi, precisazioni difensive e dettagli API rendevano la lettura corretta ma poco naturale.

## `EDIT-AI-01`. Lettura come manuale

- Versione: `0.1.1-draft2`
- Profili: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **respinta**

Difetti bloccanti:

1. metadati e registro di approvazione esposti;
2. sedici sezioni principali, molte troppo brevi;
3. ritmo dominato da definizione, cautela e cambio di titolo;
4. esempio `Il pacco non è arrivato` abbandonato nei passaggi astratti;
5. calchi come `ancora operativa`, `dimensione da annotare` e `ampiezza del riuso`;
6. eccesso di negazioni;
7. codice vicino alla forma di una reference API;
8. tassonomia dei tre aspetti presentata tardi;
9. ciclo di vita introdotto come blocco autonomo;
10. chiusura simile a una checklist.

Correzioni:

- metadati spostati in un commento HTML;
- rimossi dal flusso stato della candidatura e audit;
- sezioni ridotte da sedici a otto;
- apertura riscritta attorno alla richiesta di assistenza;
- tre domande organizzative anticipate;
- esempio continuo reintegrato;
- training e inference raccolti in una sezione;
- dettagli `eval()` e `inference_mode()` spostati in nota;
- cautele duplicate ridotte;
- lessico ibrido sostituito;
- ciclo di vita ridotto a ponte;
- fonti e materiali condensati.

## `EDIT-AI-02`. Seconda lettura e prova di fluidità

- Versione: `0.2.0-rc1`
- Profili: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore nuovo

- [x] caso concreto prima delle definizioni;
- [x] regola, modello appreso e sistema ibrido costruiti sullo stesso esempio;
- [x] termini non presentati come sinonimi;
- [x] codice dopo parametri, training e inference;
- [x] formule probabilistiche dopo la domanda tecnica.

### Lettore tecnico

- [x] definizione OECD attribuita e limitata;
- [x] convenzione modello/sistema dichiarata;
- [x] discriminativo, generativo e condizionato distinti;
- [x] diminuzione della loss non presentata come generalizzazione;
- [x] `eval()` e `inference_mode()` distinti;
- [x] fonti, codice e risultati rintracciabili.

### Lettore che riprende il capitolo

- [x] otto titoli semantici;
- [x] tabella dei tre aspetti;
- [x] riepilogo collegato al problema iniziale;
- [x] materiali operativi fuori dal flusso.

Problema residuo emerso nella review successiva:

La versione era corretta e più naturale, ma richiedeva ancora troppa familiarità con il lessico tecnico. `Checkpoint` compariva prima della definizione, il machine learning veniva spiegato attraverso formule astratte e la distinzione discriminativo/generativo chiedeva al lettore di comprendere la notazione probabilistica troppo presto.

## `EDIT-AI-03`. Review per lettore non esperto

- Versione: `0.2.0-rc1`
- Profilo dominante: lettore intelligente ma privo di formazione specifica in AI
- Criterio: ogni passaggio deve poter essere parafrasato senza usare il termine appena introdotto
- Esito: **respinta**

Difetti bloccanti:

1. le tre domande organizzative non guidavano ancora l'apertura;
2. la definizione OECD era seguita da una spiegazione ancora troppo formale;
3. `checkpoint` compariva prima della propria definizione;
4. il machine learning era descritto con `famiglia di funzioni`, `obiettivo` e `procedura` prima di un ciclo concreto;
5. `feature`, `logit`, `loss`, `optimizer` e `shape` richiedevano conoscenze pregresse;
6. training e inference erano corretti ma non abbastanza distinguibili in linguaggio comune;
7. la distinzione discriminativo/generativo iniziava dalla notazione probabilistica;
8. la sezione sui foundation model accumulava troppi metodi di adattamento;
9. la sezione `Le distinzioni che contano` ripeteva una tassonomia già esposta.

Correzioni nella versione `0.3.0-rc2`:

- apertura costruita attorno a tre domande semplici;
- definizione OECD seguita da una traduzione in linguaggio comune;
- distinzione modello/sistema applicata immediatamente al caso della spedizione;
- machine learning descritto come esempi, errore e aggiornamento di numeri interni;
- termini del training definiti prima dell'uso;
- formula lineare mantenuta come secondo livello di precisione;
- `shape [1,2]` spiegata in parole;
- discriminativo e generativo introdotti con le azioni `scegliere una categoria` e `produrre un nuovo contenuto`;
- formule probabilistiche spostate dopo la distinzione intuitiva;
- adattamento dei foundation model descritto senza un elenco di tecniche premature;
- riepilogo trasformato in tre paragrafi continui.

## `EDIT-AI-04`. Seconda lettura della versione accessibile

- Versione: `0.3.0-rc2`
- Profili: lettore non esperto, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore non esperto

- [x] comprende il problema prima della definizione di AI;
- [x] dispone delle tre domande guida dall'apertura;
- [x] distingue regola e apprendimento senza conoscere la matematica;
- [x] comprende `parametro` come numero interno regolabile;
- [x] distingue training e inference prima del codice;
- [x] può saltare le formule mantenendo il filo concettuale;
- [x] comprende discriminativo e generativo attraverso esempi concreti;
- [x] distingue modello generativo, generative AI e foundation model;
- [x] può descrivere un sistema con meccanismo, obiettivo e ampiezza.

### Lettore tecnico

- [x] definizione OECD attribuita e limitata;
- [x] convenzione modello/sistema dichiarata;
- [x] formula lineare e risultati eseguiti invariati;
- [x] distinzione probabilistica conservata;
- [x] GAN e foundation model attribuiti alle fonti;
- [x] generalizzazione separata dalla diminuzione della loss;
- [x] `eval()` e `inference_mode()` distinti.

### Lettore che riprende il capitolo

- [x] sette sezioni semantiche;
- [x] tre domande riprese nella tabella e nel riepilogo;
- [x] termini principali localizzabili senza consultare gli audit;
- [x] fonti e materiali restano accessibili senza interrompere la conclusione.

### Controllo linguistico

- [x] periodi astratti spezzati o seguiti da esempi;
- [x] gergo tradotto immediatamente in azioni osservabili;
- [x] italiano idiomatico;
- [x] nessun em dash;
- [x] ritmo variato;
- [x] ridotte negazioni e cautele duplicate;
- [x] lettura lineare senza dipendere dalle formule;
- [x] nessuna sequenza con tono da specifica o reference API.

## Audit fattuale e matematico

- [x] claim portanti in `CLAIMS.md`;
- [x] fonti primarie, istituzionali o ufficiali con limiti;
- [x] definizioni attribuite;
- [x] formula lineare coerente;
- [x] `p(y|x)` e `p(x,y)` usate nel significato dichiarato;
- [x] risultati allineati agli output;
- [x] nessuna inferenza fattuale presentata come fatto.

## Audit del codice

- [x] training modifica almeno un parametro;
- [x] inference non modifica i parametri;
- [x] output di shape `[1,2]`;
- [x] tre test superati nel run registrato;
- [x] codice invariato dalla review tecnica;
- [x] nessuna nuova esecuzione dichiarata per la sola riscrittura editoriale.

## Elementi aperti

- `AI-01` e `AI-02` devono essere generate e sottoposte ad audit;
- dopo l'inserimento occorre ripetere controllo incrociato, review linguistica e lettura integrale.

## Esito

Il testo `0.3.0-rc2` supera i gate fattuali, didattici, anti-template, editoriali, linguistici e di chiarezza per un lettore non esperto. Il capitolo resta bloccato dalle visuali mancanti e non passa alla revisione autoriale completa finché `AI-01` e `AI-02` non vengono validate e integrate.
