# Protocollo di qualità per il testo

## Scopo

Ogni capitolo deve essere verificabile a livello di affermazioni, formule, numeri, terminologia, descrizioni architetturali e riferimenti temporali. Una frase plausibile ma non sostenuta da evidenza non entra nella versione approvata.

Il processo non tratta la prima stesura come testo finale. Ogni capitolo attraversa revisioni separate, con registrazione dei difetti e nuova verifica dopo ogni correzione.

## Artefatti obbligatori per capitolo

```text
chapters/<capitolo>/
  CHAPTER.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  code/
  assets/
```

- `CHAPTER.md`: testo del capitolo.
- `FONTI_PRIMARIE.md`: paper, documentazione ufficiale, repository e standard consultati.
- `CLAIMS.md`: registro delle affermazioni portanti.
- `TEXT_AUDIT.md`: esito delle revisioni testuali e tecniche.

## Classi di contenuto

Ogni elemento tecnico appartiene a una delle seguenti classi:

1. **Fatto da fonte primaria**. È sostenuto da un paper originale, technical report ufficiale, documentazione ufficiale, repository ufficiale o standard.
2. **Derivazione**. È ottenuto da definizioni o formule già verificate. I passaggi devono essere espliciti e riproducibili.
3. **Risultato riprodotto**. È prodotto da codice eseguito con ambiente, versione, seed, input e comando registrati.
4. **Illustrativo**. È un esempio costruito per spiegare il meccanismo. Deve essere dichiarato e internamente coerente.
5. **Confine**. Dichiara ciò che il meccanismo non implementa o ciò che resta fuori dal capitolo.

Le inferenze editoriali fattuali non sono una classe ammessa nella versione approvata. Non vengono inserite neppure come affermazioni secondarie etichettate. Quando una fonte non consente di stabilire un punto, il testo viene ristretto a ciò che è verificabile oppure il punto viene omesso.

Le interpretazioni formulate dagli autori di una fonte possono essere riportate soltanto come posizione attribuita a quegli autori e senza trasformarle in fatto indipendente.

## Registro delle affermazioni

Ogni affermazione portante riceve un ID stabile.

Esempio:

```text
CLM-ATT-001
Affermazione esatta:
Tipo: fatto da fonte primaria / derivazione / risultato riprodotto / illustrativo / confine
Fonte o prova:
Sezione o pagina della fonte:
Versione o data:
Controllo indipendente:
Esito: aperta / verificata / corretta / respinta / rimossa
Note:
```

Il registro deve permettere di risalire dalla frase del capitolo alla prova che la sostiene.

## Ciclo obbligatorio di review

### 1. Ricerca e dossier delle fonti

Prima della stesura vengono raccolte le fonti primarie. Per ogni fonte si registrano titolo, autori o organizzazione, data, versione, URL o identificatore, sezioni rilevanti e limiti d'uso.

### 2. Mappa delle affermazioni

Prima di scrivere la prosa vengono elencate le affermazioni necessarie al capitolo. Una voce senza prova disponibile resta aperta e non può essere trasformata in una frase assertiva.

### 3. Prima stesura

La prima stesura segue il metodo di spiegazione del progetto. Le citazioni vengono inserite contestualmente, non aggiunte soltanto alla fine.

### 4. Audit fattuale frase per frase

Per ogni periodo tecnico si controlla:

- quale parte è un fatto;
- quale fonte la sostiene;
- se la fonte dice davvero ciò che il testo afferma;
- se il testo aggiunge condizioni non presenti nella fonte;
- se il testo omette limiti necessari;
- se la formulazione è più forte della prova;
- se paper, implementazione e documentazione corrente vengono distinti;
- se la terminologia è coerente con la fonte primaria;
- se è stata introdotta un'inferenza editoriale non ammessa.

### 5. Audit matematico

Si ricontrollano:

- definizioni;
- simboli;
- domini e dimensioni;
- shape;
- derivazioni;
- segni;
- fattori di scala;
- normalizzazioni;
- arrotondamenti;
- esempi numerici;
- condizioni di validità.

Quando possibile, i calcoli numerici vengono verificati anche con codice indipendente.

### 6. Audit architetturale e algoritmico

Si controlla l'ordine reale delle operazioni, la posizione di normalizzazioni, residual connection, mask, routing, caching, loss e update. Una descrizione di un paper non viene automaticamente estesa a tutte le implementazioni successive.

Si distingue sempre tra:

- metodo descritto nel paper;
- setup sperimentale del paper;
- implementazione nel repository;
- contratto della documentazione;
- comportamento di un prodotto o checkpoint specifico.

### 7. Audit di coerenza tra testo, immagini e codice

Le stesse label devono mantenere lo stesso significato. Shape, numeri, ordine delle operazioni e nomi dei tensor devono coincidere tra prosa, formule, visuali e snippet.

### 8. Audit temporale

Per elementi soggetti a cambiamento si ricontrollano sul web:

- versione corrente della documentazione;
- API e firme correnti;
- technical report più recente;
- stato del modello o del repository;
- eventuali errata o revisioni del paper;
- data effettiva della verifica.

Il capitolo registra una data di congelamento editoriale e non pretende aggiornamento oltre quella data.

### 9. Audit didattico

Dopo l'accuratezza tecnica si verifica che il testo:

- introduca un solo concetto nuovo per transizione;
- parta dall'output della sezione precedente;
- dichiari cosa cambia e cosa resta invariato;
- non anticipi termini, formule o varianti;
- non usi una semplificazione che renda falsa la descrizione;
- permetta ricostruzione, localizzazione, confine, trasferimento e variazione.

### 10. Seconda lettura completa

Dopo le correzioni, il capitolo viene riletto integralmente. Non si controllano soltanto i difetti già trovati, perché una modifica locale può introdurre incoerenze altrove.

La seconda lettura include testo, citazioni, formule, immagini, codice, output, esercizi e bibliografia.

## Stati del capitolo

- `ricerca`: fonti e mappa delle affermazioni in costruzione;
- `bozza`: testo non ancora sottoposto a review completa;
- `revisione fattuale`: controllo delle affermazioni in corso;
- `revisione matematica`: formule e numeri in corso di verifica;
- `revisione codice`: snippet e output in corso di verifica;
- `revisione visuale`: immagini in corso di verifica;
- `revisione incrociata`: coerenza tra tutti gli artefatti in verifica;
- `revisione didattica`: accuratezza tecnica superata, struttura in revisione;
- `revisione autoriale`: pronto per il controllo umano;
- `approvato`: tutti i gate superati.

## Difetti bloccanti

Un capitolo non può essere approvato se presenta almeno uno dei seguenti problemi:

- affermazione tecnica senza fonte o prova;
- citazione che non sostiene la frase;
- dato quantitativo senza setup o provenienza;
- formula, shape o derivazione errata;
- esempio illustrativo internamente incoerente;
- API descritta senza verifica sulla versione dichiarata;
- confusione tra paper, repository, checkpoint e prodotto;
- informazione recente non ricontrollata;
- inferenza fattuale editoriale, anche se formulata come plausibile;
- contraddizione tra testo, immagine e codice;
- semplificazione didattica che cambia il meccanismo;
- attribuzione agli autori non sostenuta dal testo della fonte;
- generalizzazione da un singolo setup non dichiarata dalla fonte.

## Esito della review

`TEXT_AUDIT.md` registra:

- data e versione esaminata;
- fonti ricontrollate;
- affermazioni respinte, ristrette, corrette o rimosse;
- errori matematici trovati;
- divergenze tra fonti;
- decisioni editoriali;
- controllo delle informazioni recenti;
- controllo dell'assenza di inferenze fattuali;
- stato finale;
- elementi ancora aperti.

La versione approvata deve poter essere ricostruita dal commit del repository e dai relativi artefatti di verifica.