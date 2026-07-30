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
2. **Derivazione**. È ottenuto da definizioni o formule già verificate. I passaggi devono essere riproducibili.
3. **Risultato riprodotto**. È prodotto da codice eseguito con ambiente, versione, seed, input e comando registrati.
4. **Illustrativo**. È un esempio costruito per spiegare il meccanismo. Deve essere dichiarato e internamente coerente.
5. **Confine**. Dichiara ciò che il meccanismo non implementa o ciò che resta fuori dal capitolo.

Le inferenze editoriali non sono ammesse come affermazioni portanti. Un’interpretazione necessaria deve essere separata dai fatti, formulata con cautela e accompagnata dalle fonti da cui deriva. Se l’interpretazione non è necessaria alla comprensione, viene eliminata.

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
Esito: aperta / verificata / corretta / respinta
Note:
```

Il registro deve permettere di risalire dalla frase del capitolo alla prova che la sostiene.

## Ciclo obbligatorio di review

### 1. Ricerca e dossier delle fonti

Prima della stesura vengono raccolte le fonti primarie. Per ogni fonte si registrano titolo, autori o organizzazione, data, versione, URL o identificatore, sezioni rilevanti e limiti d’uso.

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
- se paper, implementazione e documentazione corrente vengono distinti;
- se la terminologia è coerente con la fonte primaria.

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

Si controlla l’ordine reale delle operazioni, la posizione di normalizzazioni, residual connection, mask, routing, caching, loss e update. Una descrizione di un paper non viene automaticamente estesa a tutte le implementazioni successive.

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

### 9. Audit didattico

Dopo l’accuratezza tecnica si verifica che il testo:

- introduca un solo concetto nuovo per transizione;
- parta dall’output della sezione precedente;
- dichiari cosa cambia e cosa resta invariato;
- non anticipi termini, formule o varianti;
- non usi una semplificazione che renda falsa la descrizione;
- permetta ricostruzione, localizzazione, confine, trasferimento e variazione.

### 10. Seconda lettura completa

Dopo le correzioni, il capitolo viene riletto integralmente. Non si controllano soltanto i difetti già trovati, perché una modifica locale può introdurre incoerenze altrove.

## Stati del capitolo

- `ricerca`: fonti e mappa delle affermazioni in costruzione;
- `bozza`: testo non ancora sottoposto a review completa;
- `revisione fattuale`: controllo delle affermazioni in corso;
- `revisione matematica`: formule e numeri in corso di verifica;
- `revisione codice`: snippet e output in corso di verifica;
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
- inferenza presentata come fatto;
- contraddizione tra testo, immagine e codice;
- semplificazione didattica che cambia il meccanismo.

## Esito della review

`TEXT_AUDIT.md` registra:

- data e versione esaminata;
- fonti ricontrollate;
- affermazioni respinte o corrette;
- errori matematici trovati;
- divergenze tra fonti;
- decisioni editoriali;
- stato finale;
- elementi ancora aperti.

La versione approvata deve poter essere ricostruita dal commit del repository e dai relativi artefatti di verifica.
