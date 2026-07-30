# Changelog. Capitolo 28

> I nomi dei protocolli citati nelle versioni storiche restano come traccia. Le regole correnti sono consolidate in `docs/02_STILE_E_QA_TESTO.md`, `docs/03_VISUALI.md` e `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`.

## `0.4.0-rc4`. 30 luglio 2026

### Riscrittura editoriale e linguistica

- riaperta la review dopo il feedback sulla prosa ancora troppo schematica;
- spostati metadati, stato e informazioni operative in un commento non renderizzato;
- rimosso il registro di approvazione dal testo destinato al lettore;
- ridotte le sezioni principali a otto;
- raccolti score, scaling, softmax e somma pesata in un'unica spiegazione continua;
- riscritta l'apertura attorno al problema delle combinazioni dipendenti dalla posizione;
- limitato `consumer` alla sola lettura dell'etichetta presente in `ATT-01`;
- spiegato che `K` e `V` condividono i valori soltanto per semplificare i conti;
- sostituite formulazioni da specifica con italiano tecnico più naturale;
- raccolti i dettagli PyTorch in una nota sulle API;
- riuniti complessità, limiti e ponte verso la multi-head attention;
- riscritto il riepilogo a partire dal problema iniziale;
- condensati fonti e materiali verificabili.

### Review

- registrata `EDIT-ATT-01`, respinta per frammentazione e voce da documentazione;
- registrata `EDIT-ATT-02`, seconda lettura completa con tre profili di lettore;
- eseguito il controllo ad alta voce della versione `0.4.0-rc4`;
- esito editoriale e linguistico positivo per il testo;
- riaperto il controllo incrociato con `ATT-01` e `ATT-02`.

### Governance

- applicato lo standard ora consolidato in `docs/02_STILE_E_QA_TESTO.md`;
- aggiornati i protocolli testuali e il template del capitolo, poi riuniti nel documento tematico.

## `0.3.0-rc3`. 30 luglio 2026

### Riscrittura anti-template

- rimossi dal corpo i blocchi ripetitivi dello scaffold;
- sostituiti i titoli metacognitivi con titoli semantici;
- integrati shape, invarianti e confini nella prosa;
- mantenuta la sequenza verificata: esempio, pseudocodice, formula, implementazione e confini;
- registrata `DID-ATT-04`, seconda lettura della versione in prosa.

### Governance

- aggiunto il precedente documento `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- aggiornati template e protocollo didattico con il gate anti-template.

## `0.2.0-rc2`. 30 luglio 2026

### Riscrittura didattica

- descritti i ruoli prima dei termini query, key e value;
- spostato il nome scaled dot-product attention dopo esempio e pseudocodice;
- separate le transizioni portanti;
- attraversate `ATT-01` e `ATT-02` nella prosa;
- separata la mask matematica dalle convenzioni PyTorch;
- ridotta la multi-head attention a ponte;
- rimosso `SNIP-ATT-004`;
- rieseguiti i tre test pertinenti.

### Governance

- aggiunto il precedente documento `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- resa obbligatoria una nuova review integrale dopo ogni correzione bloccante.

## `0.1.0-rc1`. 30 luglio 2026

- prima candidatura completa;
- aggiunti testo, fonti, claim, audit, quattro snippet e due figure candidate;
- rigenerate le figure dopo problemi di formato e contenimento.
