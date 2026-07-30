# Protocollo di qualità per il testo

## Stato

- Stato: `vincolante`
- Ambito: ogni capitolo, appendice e modifica sostanziale
- Review didattica: `18_PROTOCOLLO_QA_DIDATTICO.md`
- Struttura in prosa: `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Voce editoriale: `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`

## 1. Scopo

Ogni capitolo deve essere verificabile nei fatti, nelle formule, nei numeri, nella terminologia, nelle descrizioni architetturali e nei riferimenti temporali.

Una frase plausibile ma priva di evidenza non entra nella versione approvata. Anche una lezione tecnicamente corretta viene respinta se è frammentata, poco fluida, scritta come una specifica o difficile da leggere in italiano.

## 2. Artefatti obbligatori

```text
chapters/<capitolo>/
  CHAPTER.md
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
  assets/
```

- `PLAN.md`: scaffold interno, oggetto continuo e transizioni.
- `CHAPTER.md`: testo destinato al lettore.
- `FONTI_PRIMARIE.md`: fonti e limiti.
- `CLAIMS.md`: registro frase-prova.
- `TEXT_AUDIT.md`: review, difetti e correzioni.
- `CHANGELOG.md`: storia delle versioni.
- `REVIEW.md`: guida alla revisione autoriale.

Metadati e stato editoriale vengono conservati in commenti non renderizzati o negli artefatti interni. Non interrompono il testo del manuale.

## 3. Classi di contenuto

Ogni elemento tecnico appartiene a una delle seguenti classi:

1. **Fatto da fonte primaria o ufficiale**.
2. **Derivazione** da definizioni verificate.
3. **Risultato riprodotto** con ambiente e test registrati.
4. **Illustrativo**, dichiarato e coerente.
5. **Confine**, che dichiara ciò che il meccanismo non conclude.

Le inferenze fattuali editoriali non sono ammesse. Le interpretazioni presenti nelle fonti vengono attribuite agli autori o all'organizzazione.

## 4. Registro delle affermazioni

Ogni affermazione portante riceve un ID:

```text
ID:
Affermazione esatta:
Tipo:
Fonte o prova:
Sezione o pagina:
Versione o data:
Controllo indipendente:
Esito:
Note:
```

Una voce aperta non può comparire come frase assertiva nella versione approvata.

## 5. Ciclo di review

### 5.1 Ricerca e dossier delle fonti

Prima della prosa vengono raccolte fonti primarie e ufficiali. Per ogni fonte si registrano versione, sezioni usate, affermazioni sostenibili e limiti.

### 5.2 Mappa dei claim

Le affermazioni necessarie vengono elencate in `CLAIMS.md`. La prosa non anticipa claim privi di prova.

### 5.3 Prima stesura

La prima stesura segue l'oggetto continuo e inserisce le citazioni vicino alle affermazioni. È una bozza.

Lo scaffold resta in `PLAN.md`. `CHAPTER.md` usa titoli semantici, sezioni abbastanza ampie e paragrafi naturali.

### 5.4 Audit fattuale frase per frase

Per ogni periodo tecnico si controlla:

- quale parte è un fatto;
- quale fonte la sostiene;
- se la fonte dice ciò che il testo afferma;
- se sono state aggiunte condizioni;
- se mancano limiti;
- se la formulazione è più forte della prova;
- se paper, implementazione e documentazione sono distinti;
- se la terminologia è coerente;
- se è presente una inferenza editoriale.

### 5.5 Audit matematico

Si ricontrollano:

- definizioni;
- simboli;
- domini e shape;
- derivazioni;
- segni e fattori di scala;
- normalizzazioni;
- arrotondamenti;
- esempi numerici;
- condizioni di validità.

Quando possibile, i calcoli vengono verificati con codice indipendente.

### 5.6 Audit architetturale e algoritmico

Si controllano l'ordine reale delle operazioni e la posizione di normalizzazioni, residual connection, mask, routing, caching, loss, gradiente, update, sampling e comunicazione.

Si distingue tra:

- metodo descritto nel paper;
- setup sperimentale;
- implementazione del repository;
- contratto della documentazione;
- comportamento di un checkpoint o prodotto.

### 5.7 Audit incrociato

Label, shape, numeri, ordine delle operazioni e nomi dei tensor devono coincidere tra prosa, formule, visuali e snippet.

### 5.8 Audit temporale

Per elementi soggetti a cambiamento si ricontrollano documentazione, API, release, report, errata e data effettiva della verifica.

### 5.9 Review didattica

Si applica `18_PROTOCOLLO_QA_DIDATTICO.md`.

La review controlla:

- oggetto continuo;
- gate di termini, formule, codice e varianti;
- trasformazione dominante;
- visuali integrate;
- invarianti e confini;
- ricostruibilità;
- gate anti-template.

### 5.10 Review editoriale e linguistica

Si applica `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

La review controlla:

- fluidità;
- italiano idiomatico;
- ritmo delle frasi;
- ampiezza delle sezioni;
- assenza di calchi;
- riduzione delle cautele ripetute;
- continuità dell'esempio;
- separazione tra manuale e materiali operativi;
- leggibilità ad alta voce.

### 5.11 Seconda lettura completa

Dopo ogni correzione strutturale o linguistica il capitolo viene riletto integralmente, includendo citazioni, formule, figure, codice, output, esercizi e fonti.

## 6. Stati del capitolo

```text
ricerca
bozza
revisione fattuale
revisione matematica
revisione codice
revisione visuale
revisione incrociata
revisione didattica
revisione editoriale
revisione autoriale
approvato
```

## 7. Difetti bloccanti

Un capitolo non può essere approvato se presenta:

- affermazione senza fonte o prova;
- citazione non pertinente;
- dato senza setup;
- formula, shape o derivazione errata;
- esempio incoerente;
- API non verificata;
- confusione tra paper, repository, checkpoint e prodotto;
- informazione recente non ricontrollata;
- inferenza fattuale editoriale;
- contraddizione tra artefatti;
- semplificazione che modifica il meccanismo;
- termine o formula anticipati;
- variante prima del caso base;
- visuale non integrata;
- struttura dominata da intestazioni metacognitive;
- frammentazione in microsezioni;
- metadati di progetto nel flusso di lettura;
- prosa che suona come specifica o reference;
- italiano non fluido;
- lettura ad alta voce non superata;
- rimozione delle etichette che rende impliciti shape o confini.

## 8. Esito della review

`TEXT_AUDIT.md` registra:

- versione e data;
- fonti ricontrollate;
- claim corretti o rimossi;
- errori matematici;
- divergenze;
- audit temporale;
- review didattiche;
- gate anti-template;
- review linguistica;
- profili di lettore simulati;
- elementi aperti;
- esito finale.

La versione approvata deve poter essere ricostruita dal commit e dagli artefatti associati.
