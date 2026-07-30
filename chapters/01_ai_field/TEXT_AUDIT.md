# Audit del testo. Capitolo 1

## Stato

- Versione corrente: `0.2.0-rc1`
- Data: 30 luglio 2026
- Protocolli: `docs/04_PROTOCOLLO_QA_TESTO.md`, `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`, `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`
- Esito fattuale e tecnico: **superato per testo e codice**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato dopo riscrittura e seconda lettura**
- Esito visuale: **bloccato**
- Review autoriale: non aperta

## Storia delle review

### `DID-AI-01`. Accuratezza e gate di comparsa

- Versione: `0.1.0-draft1`
- Esito: **respinta**

Difetti principali:

1. confine troppo ampio tra automazione ordinaria e sistema di AI;
2. definizione OECD non separata abbastanza dalla tassonomia editoriale;
3. distinzione discriminativo/generativo incompleta;
4. convenzione `modello/sistema` non marcata con sufficiente chiarezza;
5. relatività di `generalista` e `specialistico` poco esplicita;
6. rischio di interpretare la diminuzione della loss come generalizzazione;
7. candidate visuali non pertinenti.

Correzioni applicate nella versione `0.1.1-draft2`:

- ristretto il confine definitorio;
- attribuite le definizioni alle rispettive fonti;
- estesa la distinzione probabilistica;
- chiarita la convenzione modello/sistema;
- dichiarata la relatività dell'ampiezza;
- separato il risultato eseguito da una valutazione di generalizzazione;
- respinte le visuali estranee.

### `DID-AI-02`. Seconda lettura tecnica e didattica

- Versione: `0.1.1-draft2`
- Esito tecnico: **superato**

Controlli superati:

- oggetto continuo presente;
- termini introdotti dopo i referenti;
- codice dopo la spiegazione di parametri, training e inference;
- fonti e limiti coerenti;
- formule e risultati allineati al codice;
- gate anti-template nominalmente superato.

Problema non rilevato in questa fase:

Il capitolo restava troppo simile a un dossier tecnico. La presenza visibile di metadati, molte sezioni brevi, continue precisazioni difensive e dettagli API nel flusso principale rendevano la lettura corretta ma poco naturale.

## Review editoriale `EDIT-AI-01`. Lettura come manuale

- Versione: `0.1.1-draft2`
- Profili simulati: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **respinta**

### Difetti bloccanti

1. metadati, stato della candidatura e registro di approvazione esposti al lettore;
2. sedici sezioni principali, molte troppo brevi;
3. ritmo dominato da definizioni, cautela e cambio di titolo;
4. esempio `Il pacco non è arrivato` abbandonato durante lunghi passaggi astratti;
5. formulazioni poco idiomatiche, tra cui `ancora operativa`, `dimensione da annotare` e `ampiezza del riuso`;
6. eccesso di negazioni e confini ripetuti;
7. codice e dettagli PyTorch troppo vicini alla forma di una reference;
8. tassonomia dei tre aspetti presentata tardi, pur essendo l'idea organizzativa del capitolo;
9. ciclo di vita introdotto come ulteriore blocco autonomo dopo molte definizioni;
10. chiusura vicina a una checklist.

### Correzioni applicate

- metadati spostati in un commento HTML;
- rimossi dal flusso stato della candidatura, audit e registro di approvazione;
- ridotte le sezioni principali da sedici a otto;
- apertura riscritta attorno alla richiesta di assistenza;
- tre domande organizzative anticipate e riprese nel capitolo;
- esempio continuo reintegrato nelle sezioni astratte;
- training e inference raccolti in una sola sezione narrativa;
- dettagli `eval()` e `inference_mode()` spostati in una nota;
- cautele duplicate ridotte;
- lessico ibrido sostituito con forme italiane naturali;
- ciclo di vita ridotto a un ponte finale;
- fonti e materiali condensati in una sezione di rinvio.

Artefatti riaperti:

- `CHAPTER.md`;
- `TEXT_AUDIT.md`;
- `CHANGELOG.md`;
- `REVIEW.md`;
- documentazione metodologica del progetto.

## Review editoriale `EDIT-AI-02`. Seconda lettura e prova ad alta voce

- Versione: `0.2.0-rc1`
- Profili simulati: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore nuovo

- [x] L'apertura presenta un caso concreto prima delle definizioni.
- [x] La differenza tra regola, modello appreso e sistema ibrido è costruita sullo stesso esempio.
- [x] AI, machine learning, deep learning, generative AI e foundation model non compaiono come lista di sinonimi.
- [x] Il passaggio al codice avviene dopo parametri, training e inference.
- [x] Le formule probabilistiche sono introdotte dopo la domanda a cui rispondono.

### Lettore tecnico

- [x] La definizione OECD è attribuita e limitata al proprio contesto.
- [x] La convenzione modello/sistema è dichiarata.
- [x] Discriminativo, generativo e condizionato sono distinti.
- [x] La diminuzione della loss non viene presentata come generalizzazione.
- [x] `eval()` e `inference_mode()` conservano significati distinti.
- [x] Fonti, codice e risultati eseguiti restano rintracciabili.

### Lettore che riprende il capitolo

- [x] Otto titoli semantici permettono di ritrovare le idee portanti.
- [x] La tabella dei tre aspetti ricompone la tassonomia.
- [x] Il riepilogo torna al problema iniziale.
- [x] I materiali di progetto non interrompono la lettura.

### Controllo linguistico

- [x] Italiano scritto direttamente, non tradotto.
- [x] Nessun em dash.
- [x] Eliminati i calchi individuati nella review precedente.
- [x] Alternanza tra periodi brevi e articolati.
- [x] Ridotta la ripetizione di `non implica`, `non coincide` e formule equivalenti.
- [x] Soggetti e referenti restano chiari nei passaggi con modello, sistema e checkpoint.
- [x] La lettura ad alta voce non presenta sequenze consecutive dal ritmo burocratico o meccanico.

### Elementi ancora aperti

- `AI-01` e `AI-02` devono essere generate e sottoposte ad audit.
- Dopo l'inserimento delle figure occorre ripetere il controllo incrociato e una lettura integrale.

## Audit fattuale e matematico

- [x] Claim portanti registrati in `CLAIMS.md`.
- [x] Fonti primarie, istituzionali o ufficiali con limiti d'uso.
- [x] Definizioni attribuite.
- [x] Formula lineare coerente.
- [x] `p(y|x)`, `p(x,y)` e `p(x|c)` usate nel significato dichiarato.
- [x] Risultati del codice allineati agli output registrati.
- [x] Nessuna inferenza fattuale editoriale presentata come fatto.

## Audit del codice

- [x] Training modifica almeno un parametro.
- [x] Inference non modifica i parametri.
- [x] Output di shape `[1,2]`.
- [x] Tre test superati nel run registrato.
- [x] Codice invariato dalla precedente review tecnica.

## Esito

Il testo `0.2.0-rc1` supera i gate fattuali, didattici, anti-template, editoriali e linguistici. Il capitolo resta bloccato dalle visuali mancanti; non passa alla revisione autoriale finché `AI-01` e `AI-02` non vengono validate e integrate.
