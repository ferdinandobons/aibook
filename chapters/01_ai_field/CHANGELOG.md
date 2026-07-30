# Changelog. Capitolo 1

> I nomi dei protocolli citati nelle versioni storiche restano come traccia. Le regole correnti sono consolidate in `docs/02_STILE_E_QA_TESTO.md`, `docs/03_VISUALI.md` e `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`.

## `0.2.0-rc1`. 30 luglio 2026

### Riscrittura editoriale

- separato il testo del manuale dai metadati di progetto;
- spostati stato, versione, ambiente e concetti differiti in un commento non renderizzato;
- ridotte le sezioni principali da sedici a otto;
- riscritta l'apertura attorno alla richiesta `Il pacco non è arrivato`;
- mantenuto l'esempio lungo le sezioni astratte;
- anticipate le tre domande organizzative: meccanismo, obiettivo e ampiezza;
- raccolti parametri, training e inference in una sezione continua;
- spostata la distinzione `eval()` e `inference_mode()` in una nota tecnica;
- ridotte cautele e negazioni ripetute;
- sostituiti calchi e formulazioni da documentazione con italiano più naturale;
- ridotto il ciclo di vita a un ponte coerente con il perimetro del capitolo;
- riscritti riepilogo, controlli ed esercizi come conclusione del percorso;
- condensati fonti e materiali di riproduzione.

### Review

- registrata `EDIT-AI-01`, respinta per frammentazione, metadati visibili e prosa da specifica;
- registrata `EDIT-AI-02`, seconda lettura completa con tre profili di lettore;
- eseguita lettura ad alta voce della versione `0.2.0-rc1`;
- esito editoriale e linguistico positivo per il testo;
- visuali `AI-01` e `AI-02` ancora aperte.

### Governance

- applicato lo standard ora consolidato in `docs/02_STILE_E_QA_TESTO.md`;
- riaperti `CHAPTER.md`, `TEXT_AUDIT.md`, `REVIEW.md` e i gate visuali.

## `0.1.1-draft2`. 30 luglio 2026

### Revisione fattuale e didattica

- corretta l'affermazione che classificava automaticamente ogni esempio iniziale come AI system;
- adottata la definizione OECD come riferimento operativo senza presentarla come tassonomia universale;
- marcata la distinzione `modello/sistema` come convenzione editoriale;
- precisata la distinzione tra classificatori discriminativi, classificatori generativi e modelli condizionati;
- dichiarata la natura relativa di `generalista` e `specialistico`;
- ribadito che il dataset illustrativo non misura la generalizzazione;
- completata una seconda lettura tecnica del testo.

### Codice

- aggiunto `SNIP-AI-001` con modello lineare PyTorch;
- registrati ambiente e output;
- aggiunti tre test;
- verificata la modifica dei parametri nel training e la loro invarianza nell'inference.

### Visuali

- specificate `AI-01` e `AI-02`;
- respinte le candidate che rappresentavano repository, merge o riepiloghi del progetto;
- nessun PNG pubblicato.

## `0.1.0-draft1`. 30 luglio 2026

- prima stesura completa;
- aggiunti fonti e claim;
- integrato il primo snippet;
- aperta la review tecnica.
