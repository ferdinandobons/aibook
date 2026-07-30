# Contratto editoriale del libro

## Titolo di lavoro

**Intelligenza artificiale generativa**  
*Dai fondamenti matematici ai modelli multimodali, al reasoning, agli agenti e ai sistemi di produzione*

## Stato del progetto

- Repository operativo: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Stato: attivo, in attesa del via alla stesura del capitolo pilota
- Modalità di produzione: seriale controllata, un capitolo completo alla volta
- Capitolo pilota: **Capitolo 28. Il meccanismo di attention**
- Lingua: italiano
- Formato sorgente: Markdown
- Visuali: immagini raster generate con lo strumento immagini
- Codice principale: Python e PyTorch
- Data di riferimento del presente contratto: 30 luglio 2026
- Data da registrare per ogni ricerca: giorno effettivo della verifica

## 1. Obiettivo editoriale

Il libro deve costruire modelli mentali eseguibili. Alla fine di ogni meccanismo il lettore deve poter:

1. ricostruire l'input iniziale;
2. descrivere la trasformazione nell'ordine reale di esecuzione;
3. indicare l'output e la sua shape;
4. dire cosa è cambiato;
5. dire cosa è rimasto invariato;
6. localizzare il componente nel sistema più grande;
7. dire cosa il meccanismo non fa;
8. prevedere l'effetto di una variazione controllata;
9. collegare la spiegazione a un'immagine e a un'implementazione verificata.

Il testo non è una rassegna di termini. Ogni capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale.

## 2. Struttura dell'opera

L'opera è organizzata in due volumi. L'indice canonico è in `10_INDICE_EDITORIALE.md`.

I capitoli sono organizzati per:

- idee;
- problemi;
- meccanismi;
- famiglie architetturali;
- processi di training e inference;
- sistemi di produzione e valutazione.

I singoli modelli vengono usati come studi di caso verificati. Un modello recente non determina da solo la struttura del libro.

## 3. Lettore target e profondità

Il livello principale è intermedio tecnico, con approfondimenti avanzati ogni volta che servono per spiegare correttamente:

- matematica e derivazioni;
- shape e contratti tensoriali;
- stabilità numerica;
- complessità computazionale;
- memoria e data movement;
- implementazione PyTorch;
- training distribuito;
- inference e serving;
- hardware e kernel;
- trade-off tra accuratezza, latenza, memoria, costo ed energia.

Gli approfondimenti avanzati non sono limitati a poche sezioni opzionali. Entrano quando il caso base, da solo, sarebbe incompleto o fuorviante. Rimangono collegati allo stesso esempio continuo.

## 4. Metodo di spiegazione

Il metodo vincolante è definito in `EXPLANATION_STYLE_AND_VISUALS.md`.

Ogni transizione importante usa questo contratto:

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

Ordine di ammissione del formalismo:

```text
domanda in linguaggio naturale
-> esempio numerico
-> tabella o shape
-> pseudocodice
-> formula
-> derivazione, quando necessaria
-> implementazione verificata
-> varianti e ottimizzazioni
```

Vincoli di prosa:

- italiano diretto, calmo e progressivo;
- termini tecnici standard mantenuti in inglese quando appropriato;
- nessuna metafora o personificazione;
- nessun em dash;
- una trasformazione principale per paragrafo;
- referenti espliciti per tensor, operazioni e stati;
- distinzione visibile tra fonte, derivazione, esempio e risultato eseguito;
- nessuna formula, variante o ottimizzazione prima che il referente concreto sia stabile;
- nessuna semplificazione che modifichi il meccanismo;
- nessun contenuto fattuale inserito per inferenza editoriale.

## 5. Politica dell'accuratezza

### 5.1 Principio

Ogni informazione portante deve essere verificata.

Una frase non entra nella versione approvata soltanto perché è plausibile, coerente con conoscenze generali o frequentemente ripetuta. Deve essere sostenuta da:

- fonte primaria;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita e ricontrollata;
- risultato riprodotto con codice e ambiente registrati.

### 5.2 Esclusione delle inferenze fattuali

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.

Quando una fonte non consente di stabilire un punto:

- la frase viene ristretta a ciò che è verificabile;
- il punto viene omesso;
- oppure viene registrato come problema aperto fuori dal testo approvato.

Le interpretazioni degli autori possono essere riportate soltanto come posizione attribuita alla fonte.

Le derivazioni matematiche sono ammesse quando partono da definizioni verificate e rendono espliciti i passaggi necessari.

### 5.3 Classi ammesse

- **Fatto da fonte primaria**: sostenuto direttamente dalla fonte.
- **Derivazione**: ottenuta da definizioni verificate con passaggi riproducibili.
- **Risultato eseguito**: prodotto da codice realmente eseguito.
- **Illustrativo**: esempio costruito, dichiarato e internamente coerente.
- **Confine**: comportamento che il meccanismo non implementa.

## 6. Politica delle fonti

### 6.1 Gerarchia

Le affermazioni tecniche sono supportate, in ordine di preferenza, da:

1. paper originale negli atti ufficiali di una conferenza o rivista;
2. versione ufficiale degli autori su arXiv, quando è la fonte primaria disponibile;
3. technical report ufficiale dell'organizzazione responsabile;
4. documentazione ufficiale del framework o della libreria;
5. repository ufficiale degli autori o dell'organizzazione;
6. standard, regolamenti e documenti istituzionali.

Fonti secondarie possono aiutare a individuare materiale primario. Non sostengono da sole una spiegazione portante, un dato quantitativo, una formula, una firma API o una descrizione architetturale.

### 6.2 Verifica temporale

Per contenuti suscettibili di cambiamento vengono registrati:

- data della ricerca;
- versione della documentazione;
- versione del modello o checkpoint;
- revisione del paper;
- commit o release, quando disponibile;
- hardware e comando, per risultati riprodotti;
- differenze tra paper, implementazione e versione corrente.

Ogni capitolo recente viene ricontrollato sul web prima dell'approvazione editoriale. Il capitolo registra una data di congelamento e non dichiara aggiornamento oltre quella data.

### 6.3 Registro delle affermazioni

Ogni capitolo contiene:

- `FONTI_PRIMARIE.md`;
- `CLAIMS.md`;
- `TEXT_AUDIT.md`.

Le affermazioni portanti devono essere riconducibili a una voce del dossier. Una voce aperta non può comparire come frase assertiva nella versione approvata.

La politica completa è in `07_POLITICA_FONTI_CITAZIONI.md`.

## 7. Sistema di citazione

Nel testo si usa una citazione breve collocata vicino all'affermazione:

```text
[Vaswani et al., 2017, §3.2.1]
[PyTorch Docs, scaled_dot_product_attention, versione X.Y, consultato il GG-MM-AAAA]
```

Alla fine del capitolo si separano:

1. fonti primarie;
2. documentazione ufficiale;
3. repository e artefatti di riproduzione;
4. standard e documenti istituzionali;
5. letture complementari chiaramente separate.

Una citazione generica non sostituisce il controllo della sezione esatta.

## 8. Contratto visuale

Le visuali tecniche vengono create con lo strumento immagini. Gli SVG non sono l'artefatto editoriale principale.

Ogni immagine resta una bozza finché non supera una revisione tecnica, didattica e visiva esplicita.

### 8.1 Ciclo obbligatorio

1. definizione della domanda unica e dello storyboard;
2. generazione della prima bozza;
3. ispezione critica di contenuto, collegamenti, testo, shape e composizione;
4. registrazione dei difetti;
5. rigenerazione o modifica con correzioni esplicite;
6. nuova ispezione completa;
7. ripetizione del ciclo finché non restano difetti bloccanti;
8. approvazione e inserimento nel capitolo.

Una visuale non viene approvata quando:

- una linea suggerisce una dipendenza diversa da quella reale;
- una freccia parte o termina sul nodo errato;
- un incrocio sembra una giunzione;
- una callout sembra un flusso dati;
- una mask appare applicata al tensor sbagliato;
- una label è ambigua;
- una shape è incompatibile;
- un valore numerico non coincide con il calcolo;
- il testo è alterato o illeggibile;
- la densità impedisce un ordine di lettura stabile.

### 8.2 Stile

Le immagini devono essere originali e didattiche, con:

- blocchi puliti;
- frecce chiare;
- gerarchia leggibile;
- palette semantica;
- assenza di watermark, firme e branding di terzi;
- significato non affidato al solo colore;
- alt text ed equivalente testuale.

Le immagini di riferimento orientano il linguaggio visuale, non vengono copiate.

### 8.3 Quantità

Non esiste un numero rigido di immagini per capitolo. Si crea una visuale per ogni meccanismo o relazione che richiede una rappresentazione spaziale.

Ogni capitolo tecnico deve includere almeno una visuale portante approvata.

Il protocollo completo è in `03_PROTOCOLLO_QA_VISUALE.md`.

## 9. Codice

Il codice è una parte strutturale del libro insieme a testo e immagini.

### 9.1 Presenza

Ogni capitolo tecnico include almeno uno snippet eseguibile collegato direttamente al contenuto. Un'eccezione per un capitolo intrinsecamente non computazionale deve essere motivata nei metadati.

### 9.2 Linguaggi

- Python e PyTorch sono predefiniti.
- NumPy può essere usato per esempi numerici e verifiche indipendenti.
- Pseudocodice e codice eseguibile devono essere etichettati in modo distinto.

### 9.3 Dimensione

La forma predefinita è uno snippet breve e autosufficiente, normalmente tra circa 8 e 40 righe significative. Script più lunghi vengono mantenuti nel repository quando sono realmente necessari.

### 9.4 Contratto

Ogni blocco eseguibile specifica:

- ID;
- domanda;
- input e shape;
- operazione centrale;
- output osservabile;
- invariante;
- versione Python;
- versione della libreria;
- device e dtype;
- seed, quando rilevante;
- fonte API ufficiale;
- file completo;
- test;
- stato dell'audit.

### 9.5 Review

Ogni snippet viene:

1. verificato sulla documentazione ufficiale;
2. ispezionato staticamente;
3. eseguito in un processo pulito;
4. testato sugli invarianti;
5. confrontato con una formula diretta, NumPy o un'API ufficiale quando possibile;
6. rieseguito dopo ogni correzione;
7. confrontato con testo, formule e immagini.

Un output viene chiamato `Eseguito` soltanto quando deriva dall'ambiente e dal comando registrati.

Lo standard completo è in `05_STANDARD_SNIPPET_CODICE.md`.

## 10. Review del testo

Ogni capitolo attraversa:

1. ricerca e dossier delle fonti;
2. mappa delle affermazioni;
3. prima stesura;
4. audit fattuale frase per frase;
5. audit matematico;
6. audit architetturale e algoritmico;
7. audit temporale;
8. audit di coerenza tra testo, immagini e codice;
9. audit didattico;
10. seconda lettura completa.

Un capitolo non può essere approvato in presenza di:

- affermazione senza prova;
- citazione non pertinente;
- dato senza setup;
- formula, shape o derivazione errata;
- esempio incoerente;
- API non verificata;
- informazione recente non ricontrollata;
- inferenza fattuale editoriale;
- contraddizione tra artefatti;
- semplificazione falsa.

Il protocollo completo è in `04_PROTOCOLLO_QA_TESTO.md`.

## 11. Quality gate per capitolo

### Accuratezza

- ogni affermazione portante ha una fonte o una prova;
- le citazioni sono state aperte e controllate nel contesto originale;
- paper, documentazione, repository, checkpoint e prodotto non sono confusi;
- i dati quantitativi riportano setup e data;
- i dettagli recenti sono ricontrollati sul web;
- non rimangono inferenze fattuali editoriali.

### Matematica

- simboli, shape, segni e fattori di scala sono corretti;
- esempi numerici e arrotondamenti sono ricalcolati;
- condizioni di validità sono dichiarate;
- complessità e memoria sono verificate.

### Didattica

- lo stesso oggetto attraversa il capitolo;
- ogni sezione parte dall'output della precedente;
- un solo concetto nuovo per transizione;
- cambiamento, invariante e confine dichiarati;
- formule e codice entrano dopo il meccanismo concreto;
- varianti e ottimizzazioni entrano dopo il caso base.

### Visuali

- tutte le figure hanno superato l'audit iterativo;
- label e shape coincidono con la prosa;
- frecce e linee non sono ambigue;
- ordine di lettura chiaro;
- alt text presente;
- nessun elemento decorativo o ridondante.

### Codice e riproducibilità

- codice eseguito in ambiente pulito;
- output salvato;
- versioni registrate;
- test passati;
- API verificate;
- differenze hardware dichiarate;
- snippet allineati al capitolo.

### Coerenza incrociata

- testo, formule, visuali e codice condividono nomi, shape, numeri, ordine e confini;
- nessuna contraddizione aperta.

## 12. Workflow seriale

Per ogni capitolo:

1. apertura della struttura;
2. definizione del perimetro;
3. dossier delle fonti;
4. mappa delle affermazioni;
5. piano didattico;
6. storyboard delle visuali;
7. prima stesura;
8. implementazioni e test;
9. generazione e audit iterativo delle immagini;
10. audit fattuale;
11. audit matematico;
12. audit architetturale e algoritmico;
13. audit temporale;
14. audit incrociato;
15. audit didattico;
16. seconda lettura completa;
17. revisione autoriale;
18. congelamento della versione e del commit.

Il workflow completo è in `06_WORKFLOW_CAPITOLO.md`.

## 13. Revisione autoriale

Dopo i gate tecnici, il capitolo viene sottoposto alla revisione del committente.

Una modifica autoriale che tocca contenuto tecnico, formule, immagini o codice riapre i relativi audit. Nessun capitolo è considerato approvato prima della revisione umana prevista.

## 14. Documentazione canonica

Tutte le decisioni e le metodologie devono essere presenti in `docs/`.

- `docs/README.md` è l'indice della documentazione.
- `08_REGISTRO_DECISIONI.md` registra le decisioni esplicite.
- `LEARN_GOVERNANCE.md` non è una dipendenza.
- Nessuna regola vincolante può dipendere soltanto dalla conversazione.

Quando una nuova decisione viene presa, i documenti interessati devono essere aggiornati prima di proseguire con la produzione.

## 15. Capitolo pilota

Il capitolo pilota è **Capitolo 28. Il meccanismo di attention**.

Il capitolo usa una breve sequenza italiana dichiarata come illustrativa. Non dipende da una frase canonica esterna.

Il pilota deve validare:

- tono;
- profondità;
- metodo cumulativo;
- citazioni;
- registro dei claim;
- formule e shape;
- snippet PyTorch;
- audit del codice;
- numero e ruolo delle immagini;
- qualità della review visuale;
- coerenza tra tutti gli artefatti.

La stesura inizia soltanto dopo il via esplicito del committente.