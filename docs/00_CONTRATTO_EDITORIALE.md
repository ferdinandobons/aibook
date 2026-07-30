# Contratto editoriale del libro

## Titolo di lavoro

**Intelligenza artificiale generativa**  
*Dai fondamenti matematici ai modelli multimodali, al reasoning, agli agenti e ai sistemi di produzione*

## Stato

- Stato del progetto: attivo
- Modalità di produzione: seriale controllata, un capitolo completo alla volta
- Capitolo pilota: **Capitolo 28. Il meccanismo di attention**
- Lingua: italiano
- Formato sorgente: Markdown
- Visuali: immagini raster generate con lo strumento immagini
- Prima generazione di una visuale: sempre considerata bozza
- Data di riferimento editoriale: 30 luglio 2026
- Data da registrare per ogni ricerca: giorno effettivo della verifica

## 1. Obiettivo editoriale

Il libro deve costruire modelli mentali eseguibili. Alla fine di ogni meccanismo il lettore deve poter:

1. ricostruire l’input iniziale;
2. descrivere la trasformazione nell’ordine reale di esecuzione;
3. indicare l’output e la sua shape;
4. dire cosa è cambiato;
5. dire cosa è rimasto invariato;
6. localizzare il componente nel sistema più grande;
7. prevedere l’effetto di una variazione controllata.

Il testo non sarà una rassegna di termini. Ogni capitolo porterà un oggetto concreto dall’apertura alla ricostruzione finale.

## 2. Lettore target e profondità

Il livello principale è intermedio tecnico, con approfondimenti avanzati ogni volta che servono per spiegare correttamente:

- matematica e derivazioni;
- shape e contratti tensoriali;
- stabilità numerica;
- complessità computazionale;
- memoria e data movement;
- implementazione PyTorch;
- training distribuito;
- inference e serving;
- trade-off tra accuratezza, latenza, memoria e costo.

Le sezioni avanzate entrano dopo la stabilizzazione del caso base e restano collegate allo stesso esempio continuo.

## 3. Metodo di spiegazione

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
Cosa usa l’output dopo:
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
```

Vincoli di prosa:

- italiano diretto, calmo e progressivo;
- termini tecnici standard mantenuti in inglese quando appropriato;
- nessuna metafora o personificazione;
- una trasformazione principale per paragrafo;
- referenti espliciti per tensor, operazioni e stati;
- distinzione visibile tra dati illustrativi, risultati misurati e inferenze;
- nessuna formula, variante o ottimizzazione prima che il referente concreto sia stabile.

## 4. Politica delle fonti

### 4.1 Gerarchia ammessa

Le affermazioni tecniche saranno supportate, in ordine di preferenza, da:

1. paper originale negli atti ufficiali di una conferenza o rivista;
2. versione ufficiale degli autori su arXiv, quando è la fonte primaria disponibile;
3. technical report ufficiale dell’organizzazione che ha sviluppato il modello;
4. documentazione ufficiale del framework o della libreria;
5. repository ufficiale degli autori o dell’organizzazione;
6. standard, regolamenti e documenti istituzionali per gli aspetti normativi.

Fonti secondarie possono servire per individuare materiale primario o rappresentare un dibattito. Non possono sostenere da sole una spiegazione portante, un dato quantitativo o una descrizione architetturale.

### 4.2 Verifica temporale

Per i contenuti suscettibili di cambiamento vengono registrati:

- data della ricerca;
- versione della documentazione;
- versione del modello o checkpoint;
- commit o release, quando disponibile;
- hardware e comando, per risultati riprodotti;
- differenze tra paper, implementazione e versione corrente.

Ogni capitolo recente viene ricontrollato sul web prima dell’approvazione editoriale.

### 4.3 Registro delle affermazioni

Ogni capitolo ha un dossier `FONTI_PRIMARIE.md`. Le affermazioni portanti devono essere riconducibili a una voce del dossier.

Etichette editoriali:

- **Verificato**: sostenuto da una fonte primaria o da una misurazione riproducibile;
- **Illustrativo**: numero o esempio costruito per spiegare il meccanismo;
- **Inferenza editoriale**: conseguenza dedotta esplicitamente da fonti citate;
- **Confine**: comportamento che il meccanismo non implementa.

## 5. Sistema di citazione

Nel testo:

```text
[Vaswani et al., 2017, §3.2.1]
[PyTorch Docs, scaled_dot_product_attention, consultato il 30-07-2026]
```

Alla fine del capitolo:

1. Fonti primarie
2. Documentazione ufficiale
3. Repository e artefatti di riproduzione
4. Letture complementari, chiaramente separate

## 6. Contratto visuale

Le visuali tecniche sono create con lo strumento immagini. Non vengono usati SVG come artefatto editoriale principale. Ogni immagine resta una bozza finché non supera una revisione tecnica e visiva esplicita.

### 6.1 Ciclo obbligatorio

1. definizione della domanda unica e dello storyboard;
2. generazione della prima bozza;
3. ispezione critica di contenuto, collegamenti, testo, shape e composizione;
4. registrazione dei difetti;
5. rigenerazione o modifica con correzioni esplicite;
6. nuova ispezione completa;
7. ripetizione del ciclo finché non restano difetti bloccanti;
8. approvazione e inserimento nel capitolo.

Una visuale non viene approvata quando una linea può suggerire una dipendenza diversa da quella reale, una freccia termina sul nodo errato, un incrocio sembra una giunzione, una label è ambigua, un valore numerico non coincide con il calcolo o la densità impedisce un ordine di lettura stabile.

### 6.2 Criteri di audit

L’audit controlla almeno:

- correttezza di formule e valori illustrativi;
- coerenza di tutte le shape;
- origine e destinazione esatte di ogni freccia;
- assenza di incroci o giunzioni ambigue;
- distinzione tra flusso dati, parametro, vincolo e annotazione;
- coerenza tra mask, celle ammesse e celle bloccate;
- leggibilità di label, pedici, apici, simboli e unità;
- ordine di lettura non ambiguo;
- densità compatibile con la funzione didattica;
- corrispondenza tra immagine, prosa e fonti;
- assenza di watermark, firme, branding e testi estranei;
- comprensibilità senza dipendere dal solo colore.

Il protocollo completo è in `03_PROTOCOLLO_QA_VISUALE.md`.

### 6.3 Densità e ruolo

Ogni figura risponde a una sola domanda. Una figura di riepilogo può mostrare più passaggi soltanto dopo che ogni passaggio è già stato stabilizzato nel capitolo.

Ogni figura ha:

- ID stabile;
- titolo e domanda;
- stato prima e stato dopo;
- invariante e confine;
- provenienza dei dati;
- alt text ed equivalente testuale;
- registro delle revisioni;
- stato `bozza`, `da correggere`, `validata tecnicamente` oppure `approvata`.

Nel repository vengono pubblicati `final.png` e `AUDIT.md`. Le bozze respinte possono restare fuori dal repository.

## 7. Codice

Il codice principale usa PyTorch, salvo casi in cui NumPy o pseudocodice isolino meglio l’algoritmo.

Ogni blocco eseguibile specifica:

- versione della libreria;
- device e dtype;
- seed, quando rilevante;
- input e shape;
- riga che implementa l’operazione centrale;
- output osservabile;
- asserzioni sugli invarianti;
- comportamento atteso in caso di errore.

## 8. Quality gate per capitolo

Un capitolo non passa allo stato approvabile finché non supera:

### Accuratezza

- ogni affermazione portante ha una fonte primaria;
- paper, documentazione e implementazione non sono confusi;
- i dati quantitativi riportano setup e data;
- le inferenze editoriali sono dichiarate;
- i dettagli recenti sono ricontrollati sul web.

### Didattica

- lo stesso oggetto attraversa il capitolo;
- ogni sezione parte dall’output della precedente;
- un solo concetto nuovo per transizione;
- cambiamento, invariante e confine dichiarati;
- formule e codice entrano dopo il meccanismo concreto.

### Visuali

- tutte le figure hanno superato l’audit iterativo;
- label e shape coincidono con la prosa;
- frecce e linee non sono ambigue;
- ordine di lettura chiaro;
- alt text presente;
- nessun elemento decorativo o ridondante.

### Riproducibilità

- codice eseguito;
- output salvato;
- versioni registrate;
- test passati;
- differenze hardware dichiarate.

## 9. Workflow seriale

Per ogni capitolo:

1. dossier delle fonti;
2. mappa delle affermazioni;
3. oggetto continuo e stato del lettore;
4. storyboard delle visuali;
5. prima stesura;
6. implementazioni e test;
7. generazione e audit iterativo delle immagini;
8. audit tecnico del testo;
9. audit didattico;
10. revisione dell’autore;
11. congelamento della versione.

## 10. Capitolo pilota

Il capitolo pilota è **Capitolo 28. Il meccanismo di attention**.

Il capitolo userà una breve sequenza italiana dichiarata come illustrativa. Non dipenderà da `LEARN_GOVERNANCE.md` o da una frase canonica esterna. Il metodo e i vincoli del file `EXPLANATION_STYLE_AND_VISUALS.md` restano integralmente attivi.
