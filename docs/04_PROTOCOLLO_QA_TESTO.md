# Protocollo di qualità per il testo

## Stato

- Stato: `vincolante`
- Ambito: ogni capitolo, appendice e modifica sostanziale
- Review didattica: `18_PROTOCOLLO_QA_DIDATTICO.md`
- Struttura visibile: `19_STRUTTURA_LOGICA_IN_PROSA.md`

## 1. Scopo

Ogni capitolo deve essere verificabile a livello di affermazioni, formule, numeri, terminologia, descrizioni architetturali e riferimenti temporali.

Una frase plausibile ma non sostenuta da evidenza non entra nella versione approvata. Una lezione tecnicamente corretta ma didatticamente meccanica, discontinua o simile a una checklist non supera la review.

## 2. Artefatti obbligatori

```text
chapters/<capitolo>/
  CHAPTER.md
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  code/
  assets/
```

- `PLAN.md`: scaffold interno e oggetto continuo.
- `CHAPTER.md`: prosa destinata al lettore.
- `FONTI_PRIMARIE.md`: fonti e limiti.
- `CLAIMS.md`: registro frase-prova.
- `TEXT_AUDIT.md`: revisioni e difetti.

## 3. Classi di contenuto

Ogni elemento tecnico appartiene a una classe:

1. **Fatto da fonte primaria**.
2. **Derivazione** da definizioni verificate.
3. **Risultato riprodotto** con ambiente e test registrati.
4. **Illustrativo**, dichiarato e coerente.
5. **Confine**, che dichiara ciò che il meccanismo non implementa.

Le inferenze editoriali fattuali non sono ammesse. Le interpretazioni degli autori vengono attribuite alla fonte.

## 4. Registro delle affermazioni

Ogni affermazione portante riceve un ID stabile:

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

## 5. Ciclo obbligatorio di review

### 5.1 Ricerca e fonti

Prima della prosa vengono raccolte fonti primarie e ufficiali. Per ogni fonte si registrano versione, sezioni usate, affermazioni sostenibili e limiti.

### 5.2 Mappa dei claim

Le affermazioni necessarie vengono elencate in `CLAIMS.md`. La prosa non anticipa claim privi di prova.

### 5.3 Prima stesura

La prima stesura segue l'oggetto continuo e inserisce le citazioni vicino alle affermazioni. È una bozza, non un testo finale.

Lo scaffold di stato, problema, trasformazione, output, invariante e confine viene conservato in `PLAN.md`. `CHAPTER.md` usa titoli semantici e prosa naturale.

### 5.4 Audit fattuale frase per frase

Per ogni periodo tecnico si controlla:

- quale parte è un fatto;
- quale fonte la sostiene;
- se la fonte dice realmente ciò che il testo afferma;
- se sono state aggiunte condizioni;
- se mancano limiti necessari;
- se la formulazione è più forte della prova;
- se paper, implementazione e documentazione sono distinti;
- se la terminologia è coerente;
- se è presente una inferenza editoriale non ammessa.

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

- metodo del paper;
- setup sperimentale;
- implementazione del repository;
- contratto della documentazione;
- comportamento di un checkpoint o prodotto.

### 5.7 Audit incrociato

Label, shape, numeri, ordine delle operazioni e nomi dei tensor devono coincidere tra prosa, formule, visuali e snippet.

### 5.8 Audit temporale

Per elementi soggetti a cambiamento si ricontrollano documentazione, API, release, report, errata e data effettiva della verifica.

### 5.9 Audit didattico

Si applica integralmente `18_PROTOCOLLO_QA_DIDATTICO.md`.

La review controlla:

- oggetto continuo;
- gate di termini, formule, codice e varianti;
- una trasformazione dominante per passaggio;
- visuali attraversate dalla prosa;
- invarianti e confini;
- ricostruibilità;
- gate anti-template secondo `19_STRUTTURA_LOGICA_IN_PROSA.md`.

La review non richiede che `CHAPTER.md` contenga titoli letterali come `Cosa è cambiato` o `Frase di continuità`. Richiede che le relative funzioni siano ricostruibili nella prosa.

### 5.10 Seconda lettura completa

Dopo ogni correzione strutturale il capitolo viene riletto integralmente, includendo citazioni, formule, figure, codice, output, esercizi e fonti.

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
- visuale non attraversata dalla prosa;
- lezione strutturata come sequenza ripetitiva di intestazioni metacognitive;
- rimozione delle etichette che rende impliciti shape, invarianti o confini.

## 8. Esito della review

`TEXT_AUDIT.md` registra:

- versione e data;
- fonti ricontrollate;
- claim corretti o rimossi;
- errori matematici;
- divergenze;
- audit temporale;
- review didattiche ripetute;
- controllo anti-template;
- elementi aperti;
- esito finale.

La versione approvata deve poter essere ricostruita dal commit e dagli artefatti associati.