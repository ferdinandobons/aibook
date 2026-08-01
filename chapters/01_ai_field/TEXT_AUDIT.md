# Audit del testo. Capitolo 1

## Stato

- Versione corrente: `0.4.0-rc3`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, claim e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e tecnico: **superato per testo e codice**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato dopo riscrittura e seconda lettura**
- Esito di chiarezza per lettore non esperto: **superato**
- Esito visuale tecnico: **superato**
- Controllo incrociato testo-visuali-codice: **superato**
- Review autoriale completa: aperta

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

## `ACCESS-AI-01`. Lettore non esperto

- Versione: `0.3.0-rc2`
- Esito: **superato dopo riscrittura completa**

Controlli:

- [x] apertura guidata da tre domande in linguaggio comune;
- [x] definizione OECD seguita da parafrasi esplicativa;
- [x] parametri descritti come numeri regolabili prima del formalismo;
- [x] loss, gradienti, optimizer, iperparametri e checkpoint definiti nel punto d'uso;
- [x] training e inference distinti prima del codice;
- [x] discriminativo e generativo spiegati con esempi prima delle formule;
- [x] foundation model presentato come base adattabile;
- [x] nessuna precisione tecnica dipende da gergo non introdotto;
- [x] seconda lettura integrale superata.

## `VIS-AI-01`. Visuali e controllo incrociato

- Versione: `0.4.0-rc3`
- Figure: `AI-01/candidate-v1.png`, `AI-02/candidate-v1.png`
- Esito: **superato tecnicamente**

### `AI-01`

- [x] stessa richiesta usata nel testo;
- [x] meccanismo, obiettivo e ampiezza presentati come aspetti indipendenti;
- [x] nessuna scala da semplice ad avanzato;
- [x] nessun aspetto determina automaticamente gli altri;
- [x] testo contenuto nei box;
- [x] sfondo bianco puro;
- [x] alt text verificato.

### `AI-02`

- [x] target collegato alla loss;
- [x] gradienti successivi alla loss;
- [x] optimizer step unico nodo che modifica i parametri;
- [x] inference senza target, loss, gradienti o optimizer;
- [x] checkpoint fissato coerente con la prosa;
- [x] `eval()` e `inference_mode()` non presentati come sinonimi;
- [x] testo contenuto nei box;
- [x] alt text verificato.

### Coerenza trasversale

- [x] figure introdotte e concluse dalla prosa;
- [x] `AI-02` precede lo snippet e mostra lo stesso contratto;
- [x] `AI-01` segue la tabella dei tre aspetti;
- [x] nessun valore visuale contraddice codice, fonti o claim;
- [x] immagini generate e decodificate dal workflow registrato;
- [x] rilettura completa dopo l'inserimento delle figure.

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
- [x] codice invariato dalle revisioni editoriali e visuali.

## Elementi aperti

- approvazione autoriale della candidatura completa;
- rinomina delle figure in `final.png` soltanto dopo approvazione;
- congelamento del capitolo con commit e data.

## Esito

Il testo `0.4.0-rc3`, le due figure candidate e il codice superano i gate fattuali, didattici, anti-template, editoriali, linguistici, di accessibilità e di coerenza trasversale. Il capitolo è disponibile per la revisione autoriale completa.
