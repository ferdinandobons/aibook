# Registro consolidato delle decisioni

## Funzione

Questo documento registra le decisioni esplicite che governano il progetto. Ogni nuova decisione deve essere aggiunta qui e propagata ai documenti specialistici interessati.

Stato delle decisioni:

- `vincolante`: applicata a tutto il progetto;
- `pilota`: applicata al capitolo pilota e da confermare dopo la revisione autoriale;
- `sostituita`: conservata soltanto per tracciare una modifica;
- `aperta`: richiede una decisione prima del lavoro interessato.

Alla data di questo aggiornamento non risultano decisioni aperte che impediscano l'avvio del Capitolo 28.

## Decisioni editoriali

### DEC-001. Repository operativo

- Stato: `vincolante`
- Decisione: tutti i progressi del libro vengono registrati nel repository `ferdinandobons/aibook`.
- Branch predefinito: `main`.
- Conseguenza: documenti, capitoli, audit, codice e asset approvati devono essere ricostruibili dai commit del repository.

### DEC-002. Formato sorgente

- Stato: `vincolante`
- Decisione: il formato sorgente del libro è Markdown.
- Conseguenza: formule, citazioni, riferimenti alle immagini e snippet vengono mantenuti in file testuali versionabili.

### DEC-003. Lingua

- Stato: `vincolante`
- Decisione: il libro viene scritto in italiano.
- I termini tecnici standard restano in inglese quando questa è la forma corrente nel settore.

### DEC-004. Struttura generale

- Stato: `vincolante`
- Decisione: l'opera è organizzata in due volumi, con fondamenti, famiglie generative, Transformer, architetture moderne, post-training, multimodalità, agenti, produzione, valutazione e sicurezza.
- Fonte interna: `10_INDICE_EDITORIALE.md`.

### DEC-005. Modalità di produzione

- Stato: `vincolante`
- Decisione: produzione seriale controllata, un capitolo completo alla volta.
- Non si genera l'intero libro in una singola passata.
- Ogni capitolo deve superare i gate prima di procedere al successivo.

### DEC-006. Capitolo pilota

- Stato: `pilota`
- Decisione: il primo capitolo prodotto è il Capitolo 28, **Il meccanismo di attention**.
- Scopo: validare tono, profondità, densità matematica, qualità del codice, numero e stile delle visuali e processo di review.

### DEC-007. Livello tecnico

- Stato: `vincolante`
- Decisione: livello principale intermedio tecnico.
- Gli approfondimenti avanzati vengono inseriti ogni volta che sono necessari per una spiegazione corretta, non soltanto in rare sezioni opzionali.
- Ambiti avanzati inclusi quando pertinenti: derivazioni, stabilità numerica, shape, complessità, memoria, data movement, distributed training, kernel, inference e serving.

### DEC-008. Impostazione didattica

- Stato: `vincolante`
- Decisione: approccio didactic-first, ancorato a fonti primarie.
- La prosa viene ottimizzata per insegnare, ma non può semplificare fino a modificare il meccanismo.

### DEC-009. Metodo di spiegazione

- Stato: `vincolante`
- Decisione: si applica integralmente `EXPLANATION_STYLE_AND_VISUALS.md`.
- Il capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale.
- Ogni transizione introduce un solo concetto nuovo e parte dall'output della precedente.

### DEC-010. Dipendenze metodologiche

- Stato: `vincolante`
- Decisione: `LEARN_GOVERNANCE.md` non è necessario e non è una dipendenza del libro.
- Tutte le informazioni metodologiche richieste devono essere presenti in `docs/`.
- Nessuna frase guida esterna è obbligatoria.

## Decisioni su accuratezza e fonti

### DEC-011. Verifica di tutte le informazioni

- Stato: `vincolante`
- Decisione: ogni informazione portante deve essere verificata tramite fonte primaria, documentazione ufficiale, standard o prova riproducibile.
- Una frase plausibile non è sufficiente.

### DEC-012. Esclusione delle inferenze fattuali

- Stato: `vincolante`
- Decisione: la versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.
- Se una fonte non stabilisce un punto, il punto viene omesso o lasciato fuori dalla versione approvata.
- Restano ammesse derivazioni matematiche esplicite e ricontrollate.

### DEC-013. Ricerca web aggiornata

- Stato: `vincolante`
- Decisione: paper, technical report, documentazione, modelli, API, benchmark, standard e normative recenti vengono verificati tramite ricerca web al momento della lavorazione.
- Ogni capitolo registra la data effettiva di verifica e una data di congelamento editoriale.

### DEC-014. Gerarchia delle fonti

- Stato: `vincolante`
- Decisione: priorità a paper originali, atti ufficiali, technical report ufficiali, documentazione ufficiale, repository ufficiali e standard.
- Blog e fonti secondarie non sostengono da soli le affermazioni portanti.

### DEC-015. Sistema di citazione

- Stato: `vincolante`
- Decisione: citazione breve nel testo e bibliografia completa alla fine del capitolo.
- La citazione deve indicare sezione, pagina, versione, revisione o commit quando necessario.

### DEC-016. Review del testo

- Stato: `vincolante`
- Decisione: ogni capitolo attraversa audit fattuale, matematico, architetturale, algoritmico, temporale, incrociato e didattico.
- Dopo le correzioni viene svolta una seconda lettura completa.
- Riferimento: `04_PROTOCOLLO_QA_TESTO.md`.

### DEC-017. Registro delle affermazioni

- Stato: `vincolante`
- Decisione: ogni capitolo contiene `CLAIMS.md` con ID stabili e prova di ogni affermazione portante.
- Un'affermazione aperta non entra come frase assertiva nel capitolo approvato.

## Decisioni sulle immagini

### DEC-018. Strumento di produzione

- Stato: `vincolante`
- Decisione: le immagini tecniche vengono create con lo strumento immagini.
- Gli SVG non sono usati come artefatto editoriale principale.

### DEC-019. Prima generazione non finale

- Stato: `vincolante`
- Decisione: ogni prima generazione è una bozza.
- Nessuna immagine viene inserita nel capitolo senza audit tecnico e visivo.

### DEC-020. Review iterativa delle immagini

- Stato: `vincolante`
- Decisione: ogni visuale viene controllata criticamente più volte e rigenerata o modificata finché non rimangono problemi bloccanti.
- Una singola linea ambigua, una freccia collegata al nodo errato, un incrocio interpretabile come giunzione, una shape errata o un numero incoerente bloccano l'approvazione.
- Riferimento: `03_PROTOCOLLO_QA_VISUALE.md`.

### DEC-021. Funzione delle visuali

- Stato: `vincolante`
- Decisione: ogni figura risponde a una sola domanda didattica.
- Le visuali sono parte della spiegazione, non decorazione.
- Una figura di riepilogo può essere densa soltanto dopo che i singoli passaggi sono già stati stabilizzati.

### DEC-022. Stile visuale

- Stato: `vincolante`
- Decisione: diagrammi tecnici originali, puliti, leggibili, con blocchi, frecce e gerarchia chiara, ispirati al linguaggio didattico delle immagini di riferimento senza copiarne layout, watermark, firme o branding.
- Colori semantici: neutro per input e parametri, blu per operazione corrente, verde per output, ambra per vincoli, rosso per errore o stato invalido.
- Il colore non è mai l'unico portatore di significato.

### DEC-023. Quantità delle immagini

- Stato: `vincolante`
- Decisione: non esiste un numero rigido di immagini per capitolo.
- Si crea una visuale per ogni meccanismo o relazione che richiede una rappresentazione spaziale per essere compresa correttamente.
- Ogni capitolo tecnico include almeno una visuale portante approvata.

### DEC-024. Formato e accessibilità

- Stato: `vincolante`
- Decisione: asset finali in PNG ad alta risoluzione, accompagnati da alt text, equivalente testuale e audit.
- Il testo deve restare leggibile alla dimensione editoriale prevista.

## Decisioni sul codice

### DEC-025. Presenza del codice

- Stato: `vincolante`
- Decisione: testo, immagini e codice devono essere integrati.
- Ogni capitolo tecnico include almeno uno snippet eseguibile collegato direttamente a un meccanismo del capitolo.
- Un'eventuale eccezione per capitoli intrinsecamente non computazionali deve essere motivata nei metadati.

### DEC-026. Linguaggi e librerie

- Stato: `vincolante`
- Decisione: Python e PyTorch sono la scelta principale.
- NumPy può essere usato per esempi numerici o controlli indipendenti.
- Pseudocodice e codice eseguibile devono essere distinti.

### DEC-027. Dimensione degli snippet

- Stato: `vincolante`
- Decisione: snippet brevi e autosufficienti, normalmente tra circa 8 e 40 righe significative.
- Script più lunghi vengono mantenuti nel repository soltanto quando servono per esperimenti, benchmark, training, dataset, checkpoint o hardware specifico.

### DEC-028. Correttezza del codice

- Stato: `vincolante`
- Decisione: ogni snippet deve essere verificato sulla documentazione ufficiale, eseguito in un processo pulito e testato.
- Output e shape devono coincidere con testo, formule e immagini.
- Nessuna API viene scritta sulla base della memoria.

### DEC-029. Provenienza degli output

- Stato: `vincolante`
- Decisione: un output è etichettato `Eseguito` soltanto quando deriva dall'ambiente e dal comando registrati.
- Gli output costruiti per spiegare il formato sono etichettati `Illustrativo`.

## Decisioni sul workflow e sull'approvazione

### DEC-030. Controllo incrociato

- Stato: `vincolante`
- Decisione: testo, formule, immagini e codice devono condividere label, shape, numeri, ordine delle operazioni, invarianti e confini.
- Una contraddizione blocca il capitolo.

### DEC-031. Revisione autoriale

- Stato: `vincolante`
- Decisione: dopo i gate tecnici, ogni capitolo viene sottoposto alla revisione del committente.
- Le modifiche autoriali che toccano contenuto tecnico riaprono gli audit pertinenti.

### DEC-032. Congelamento del capitolo

- Stato: `vincolante`
- Decisione: la versione approvata viene associata a una data di congelamento e a un commit SHA.
- Non si dichiara aggiornamento oltre la data registrata.

### DEC-033. Avvio del lavoro

- Stato: `vincolante`
- Decisione: il Capitolo 28 non inizia finché la documentazione canonica non è completa e il committente non dà esplicitamente il via.

## Decisioni sostituite

### DEC-S01. Uso prioritario di SVG

- Stato: `sostituita`
- Decisione precedente: produzione principale tramite SVG.
- Sostituita da: DEC-018.
- Motivo: preferenza esplicita per immagini create con lo strumento immagini e sottoposte a audit iterativo.

### DEC-S02. Dipendenza da una frase in `LEARN_GOVERNANCE.md`

- Stato: `sostituita`
- Decisione precedente: attendere una frase guida esterna.
- Sostituita da: DEC-010.
- Motivo: il file non è necessario e il capitolo può usare un esempio italiano dichiarato come illustrativo.

### DEC-S03. Inferenze editoriali ammesse se etichettate

- Stato: `sostituita`
- Decisione precedente: ammettere interpretazioni necessarie se etichettate.
- Sostituita da: DEC-012.
- Motivo: richiesta di escludere dal testo approvato anche inferenze fattuali potenzialmente errate.