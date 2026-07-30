# Audit del testo. Capitolo 1

## Stato

- Versione corrente: `0.2.0-rc1`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, claim e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e tecnico: **superato per testo e codice**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato dopo riscrittura e seconda lettura**
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

## `EDIT-AI-02`. Seconda lettura e prova ad alta voce

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

### Controllo linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] calchi principali rimossi;
- [x] ritmo variato;
- [x] ridotte formule negative ripetute;
- [x] referenti chiari;
- [x] lettura ad alta voce superata.

## Audit fattuale e matematico

- [x] claim portanti in `CLAIMS.md`;
- [x] fonti primarie, istituzionali o ufficiali con limiti;
- [x] definizioni attribuite;
- [x] formula lineare coerente;
- [x] `p(y|x)`, `p(x,y)` e `p(x|c)` usate nel significato dichiarato;
- [x] risultati allineati agli output;
- [x] nessuna inferenza fattuale presentata come fatto.

## Audit del codice

- [x] training modifica almeno un parametro;
- [x] inference non modifica i parametri;
- [x] output di shape `[1,2]`;
- [x] tre test superati nel run registrato;
- [x] codice invariato dalla review tecnica.

## Elementi aperti

- `AI-01` e `AI-02` devono essere generate e sottoposte ad audit;
- dopo l'inserimento occorre ripetere controllo incrociato, review linguistica e lettura integrale.

## Esito

Il testo `0.2.0-rc1` supera i gate fattuali, didattici, anti-template, editoriali e linguistici. Il capitolo resta bloccato dalle visuali mancanti e non passa alla revisione autoriale completa finché `AI-01` e `AI-02` non vengono validate e integrate.
