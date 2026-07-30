# Protocollo di aggiornamento dei contenuti

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Entry point operativo: `../GUIDELINE.md`
- Architettura editoriale: `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Ultima ricerca approfondita globale: 30 luglio 2026

## Scopo

Questo protocollo permette a una persona o a un sistema AI senza contesto precedente di:

- aggiungere una nuova tecnica;
- aggiornare una tecnica esistente;
- creare, dividere o unire capitoli;
- modificare la maturità `FRONTIER`, `ESTABLISHED` o `CORE`;
- aggiornare fonti, immagini, codice e testo;
- conservare la coerenza dell'intera opera.

## Principio fondamentale

Un aggiornamento del libro non è una modifica isolata a un file Markdown. È una modifica coordinata a un insieme di artefatti con provenienza e review.

La minima unità di aggiornamento comprende, quando pertinente:

```text
catalogo della tecnica
-> collocazione editoriale
-> fonti
-> claim
-> testo
-> formule
-> codice
-> visuali
-> audit
-> indice
-> registro delle decisioni
-> commit
```

## Prima di operare

Leggere nell'ordine:

1. `../GUIDELINE.md`;
2. `README.md` di questa cartella;
3. `00_CONTRATTO_EDITORIALE.md`;
4. `08_REGISTRO_DECISIONI.md`;
5. `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
6. `14_CATALOGO_STATO_ARTE.md`;
7. `10_INDICE_EDITORIALE.md`;
8. il protocollo specialistico relativo all'operazione.

Controllare inoltre `../PROGRESS.md` e gli artefatti del capitolo coinvolto.

## Tipi di aggiornamento

### U1. Nuova tecnica o nuova architettura

Usare quando compare un meccanismo non ancora registrato.

### U2. Nuova evidenza su una tecnica esistente

Usare quando un nuovo paper, report, benchmark o repository cambia la comprensione o la maturità del contenuto.

### U3. Aggiornamento di API, libreria o implementazione

Usare quando cambia una firma, un backend, un comportamento documentato o una versione supportata.

### U4. Promozione o demozione di maturità

Usare quando una voce passa tra `FRONTIER`, `ESTABLISHED` e `CORE`.

### U5. Nuovo capitolo

Usare quando il materiale non può più essere spiegato correttamente come sezione di un capitolo esistente.

### U6. Split o merge

Usare quando i confini didattici di uno o più capitoli non sono più corretti.

### U7. Correzione tecnica

Usare quando viene scoperto un errore in testo, formula, codice, immagine, fonte o classificazione.

### U8. Nuova edizione

Usare per aggiornare numerazione visualizzata, date di congelamento, export e snapshot complessivo.

## Procedura U1. Inserire una nuova tecnica

### 1. Identificazione

Registrare:

```text
Nome provvisorio:
Problema risolto:
Oggetto modificato:
Input:
Operazione:
Output:
Invariante:
Confine:
Prima fonte primaria:
Data della prima verifica:
```

Il nome commerciale di un modello non sostituisce la descrizione del meccanismo.

### 2. Verifica della novità

Controllare che la tecnica non sia:

- una rinominazione di un meccanismo esistente;
- una configurazione di iperparametri;
- una combinazione di tecniche già coperte;
- un risultato limitato a un singolo prodotto senza descrizione tecnica sufficiente;
- una modifica implementativa che appartiene a un capitolo di sistemi.

### 3. Ricerca primaria

Raccogliere almeno:

- paper o technical report originale;
- repository o documentazione ufficiale, quando disponibile;
- versione e data;
- sezioni che descrivono il meccanismo;
- limiti dichiarati dagli autori;
- eventuali errata o revisioni.

Per una voce `FRONTIER` una sola fonte primaria può bastare per la registrazione, ma non per affermazioni generalizzate.

### 4. Routing

Applicare l'algoritmo di `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`.

Registrare:

```text
part_id primario:
capitolo candidato:
tag secondari:
prerequisiti:
consumer successivi:
```

### 5. Maturità iniziale

Una tecnica nuova viene normalmente inserita come `FRONTIER`.

Può essere inserita come `ESTABLISHED` se la ricerca dimostra che:

- esiste già una storia di adozione o replica;
- il nome è nuovo ma il meccanismo è consolidato;
- più fonti indipendenti descrivono lo stesso contratto.

Non viene inserita direttamente come `CORE` senza motivazione nel registro delle decisioni.

### 6. Destinazione editoriale

Scegliere una delle seguenti:

- nota nel catalogo;
- sottosezione di un capitolo esistente;
- approfondimento avanzato;
- studio di caso;
- nuovo capitolo candidato;
- solo osservatorio, in attesa di evidenza.

### 7. Aggiornamento dei file

Aggiornare almeno:

- `14_CATALOGO_STATO_ARTE.md`;
- `10_INDICE_EDITORIALE.md`, se cambia l'indice;
- `15_REGISTRO_RICERCHE_APPROFONDITE.md` o il dossier della ricerca;
- `08_REGISTRO_DECISIONI.md`, se viene creata una nuova regola o un capitolo;
- il dossier del capitolo, quando la tecnica entra nel testo.

## Procedura U2. Integrare nuova evidenza

1. Aprire la voce nel catalogo.
2. Riaprire le fonti originali già usate.
3. Leggere la nuova fonte nel contesto originale.
4. Confrontare definizioni, setup, benchmark e condizioni.
5. Registrare convergenze e divergenze.
6. Aggiornare i claim interessati.
7. Riaprire gli audit di testo, matematica, codice o visuali coinvolti.
8. Aggiornare la data dell'ultima verifica.
9. Non aggiornare la maturità automaticamente.

## Procedura U3. Aggiornare un'API o un'implementazione

1. Identificare la versione descritta nel capitolo.
2. Consultare la documentazione ufficiale corrente e le note di rilascio.
3. Distinguere modifica incompatibile, deprecazione e nuova funzione.
4. Aggiornare lo snippet in un branch o in una bozza.
5. Eseguire il codice in ambiente pulito.
6. Rieseguire tutti i test.
7. Salvare ambiente, comando e output.
8. Aggiornare testo e visuali soltanto dopo la verifica del comportamento.
9. Conservare una nota sulla versione precedente quando serve alla riproducibilità.

## Procedura U4. Cambiare maturità

### Scheda obbligatoria

```text
Topic ID:
Stato precedente:
Stato proposto:
Data:
Nuove fonti:
Adozioni o repliche:
Terminologia:
Failure mode noti:
Motivazione:
Impatto sui capitoli:
Reviewer:
```

### Gate di promozione

La promozione richiede:

- evidenza aggiuntiva, non soltanto il trascorrere del tempo;
- fonti che descrivano lo stesso meccanismo;
- verifica che il risultato non dipenda esclusivamente da un setup non disponibile;
- trade-off e failure mode sufficientemente documentati;
- audit delle frasi che usano termini come standard, consolidato o generalmente.

### Effetto editoriale

La promozione cambia il badge di maturità e può cambiare la profondità del trattamento. Non cambia automaticamente la parte, l'ID o l'ordine concettuale.

## Procedura U5. Creare un nuovo capitolo

Un nuovo capitolo è giustificato quando sono vere tutte le condizioni seguenti:

1. esiste una domanda didattica autonoma;
2. il meccanismo ha input, trasformazione, output, invariante e confine propri;
3. una sottosezione renderebbe il capitolo ospite troppo denso o interromperebbe il suo oggetto continuo;
4. esistono fonti sufficienti per sostenere la parte portante;
5. è possibile progettare almeno una visuale non ridondante;
6. è possibile creare almeno uno snippet o motivarne formalmente l'assenza;
7. i prerequisiti e il consumer successivo sono identificati.

### Artefatti iniziali

```text
chapters/<slug>/
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  CHAPTER.md
  TEXT_AUDIT.md
  CHANGELOG.md
  code/
  assets/
```

Il nuovo capitolo riceve un ID semantico stabile. Il numero visualizzato viene assegnato nell'indice dell'edizione.

## Procedura U6. Split o merge

Prima di dividere o unire capitoli:

- identificare la giunzione didattica che non funziona;
- verificare che il problema non sia risolvibile con una sezione o un prerequisito;
- mappare claim, fonti, visuali e snippet;
- definire alias e redirect;
- aggiornare tutti i riferimenti interni;
- registrare la decisione.

Nessun file viene cancellato prima che la mappa di migrazione sia verificata.

## Procedura U7. Correggere un errore

1. Bloccare l'approvazione dell'artefatto interessato.
2. Registrare l'errore nell'audit.
3. Identificare la fonte del difetto.
4. Correggere il minimo insieme coerente di artefatti.
5. Ripetere l'intero audit pertinente.
6. Controllare se lo stesso errore è stato propagato altrove.
7. Registrare il commit con un messaggio che descriva la correzione, non soltanto il file modificato.

## Procedura U8. Preparare una nuova edizione

1. Eseguire una ricerca approfondita globale.
2. Rivedere il catalogo di maturità.
3. Controllare le dipendenze tra capitoli.
4. Aggiornare l'indice e i numeri visualizzati.
5. Conservare gli ID e gli alias.
6. Ricontrollare normative, API e modelli recenti.
7. Rieseguire i test del codice.
8. Verificare gli asset finali.
9. Registrare data e commit di congelamento.
10. Generare la mappa delle differenze rispetto all'edizione precedente.

## Ricerca approfondita periodica

### Frequenza minima

- ricerca locale prima di ogni capitolo;
- controllo delle fonti recenti prima dell'approvazione;
- revisione frontier almeno ogni 90 giorni durante la produzione attiva;
- ricerca approfondita globale prima di ogni nuova edizione;
- ricerca straordinaria quando emerge una nuova famiglia architetturale o un cambiamento normativo rilevante.

### Copertura obbligatoria

La ricerca globale controlla almeno:

- dati e tokenizzazione;
- scaling e training;
- attention, recurrence, SSM e memorie;
- MoE e conditional computation;
- modelli autoregressivi, diffusion e flow;
- post-training, preference optimization e RL;
- reasoning e test-time compute;
- multimodalità e world model;
- retrieval, memoria, tool e agenti;
- quantizzazione, pruning, distillazione e decoding;
- serving, kernel, compiler e sistemi distribuiti;
- valutazione e interpretabilità;
- sicurezza, privacy, provenance e governance.

### Esito della ricerca

Ogni ricerca globale produce:

- ID della ricerca;
- data di inizio e chiusura;
- query e fonti consultate;
- criteri di inclusione;
- nuove voci;
- voci aggiornate;
- cambi di maturità proposti;
- buchi di copertura;
- impatto sull'indice;
- commit finale.

## Regola di completezza

Non è corretto dichiarare che il catalogo contiene ogni lavoro esistente.

La formulazione approvata è:

> Il catalogo censisce le principali famiglie, i meccanismi e le ottimizzazioni che soddisfano i criteri di inclusione alla data dell'ultima ricerca approfondita.

I criteri di inclusione sono:

- contributo tecnico distinto;
- fonte primaria accessibile;
- rilevanza per l'architettura, il training, l'inference o l'uso dei sistemi generativi;
- evidenza o influenza sufficiente per il livello di maturità assegnato;
- possibilità di collocazione nella tassonomia.

## Report finale di ogni aggiornamento

Il report deve indicare:

```text
Operazione eseguita:
File modificati:
Fonti aggiunte o riaperte:
Claim modificati:
Maturità prima e dopo:
Test eseguiti:
Audit riaperti:
Problemi rimasti:
Commit:
Data di verifica:
```

Non dichiarare completata un'operazione se rimangono artefatti incoerenti.