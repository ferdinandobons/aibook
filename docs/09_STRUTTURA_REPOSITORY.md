# Struttura del repository e convenzioni degli artefatti

## Scopo

La struttura deve permettere di ricostruire ogni capitolo, affermazione, immagine e risultato eseguito, mantenendo separati il manuale destinato al lettore e i materiali operativi.

## Albero principale

```text
/
  README.md
  GUIDELINE.md
  BOOK_PRODUCTION.md
  PROGRESS.md
  docs/
  chapters/
  assets/
  scripts/
  tests/
```

## Cartella `docs/`

```text
docs/
  README.md
  00_CONTRATTO_EDITORIALE.md
  01_TEMPLATE_CAPITOLO.md
  02_TEMPLATE_VISUALE.md
  03_PROTOCOLLO_QA_VISUALE.md
  04_PROTOCOLLO_QA_TESTO.md
  05_STANDARD_SNIPPET_CODICE.md
  06_WORKFLOW_CAPITOLO.md
  07_POLITICA_FONTI_CITAZIONI.md
  08_REGISTRO_DECISIONI.md
  09_STRUTTURA_REPOSITORY.md
  10_INDICE_EDITORIALE.md
  11_AUDIT_DOCUMENTAZIONE.md
  12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md
  13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md
  14_CATALOGO_STATO_ARTE.md
  15_REGISTRO_RICERCHE_APPROFONDITE.md
  16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md
  17_STANDARD_VISIVO_CANONICO.md
  18_PROTOCOLLO_QA_DIDATTICO.md
  19_STRUTTURA_LOGICA_IN_PROSA.md
  20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md
  EXPLANATION_STYLE_AND_VISUALS.md
  source/
```

Nessuna regola vincolante può esistere soltanto in una conversazione o in un file esterno.

I file in `docs/source/` sono copie archivistiche. Diventano vincolanti soltanto attraverso l'adattamento nei documenti canonici.

## Cartella del capitolo

Nome:

```text
chapters/<NN_slug>/
```

Struttura:

```text
chapters/<NN_slug>/
  CHAPTER.md
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
    README.md
    CODE_AUDIT.md
    outputs/
    environments/
  assets/
    README.md
```

Le visuali vengono conservate nella cartella globale `assets/chapters/`, non duplicate nella cartella del capitolo.

## File `CHAPTER.md`

`CHAPTER.md` contiene soltanto il materiale destinato alla lettura:

- titolo;
- apertura;
- spiegazione in prosa;
- formule e tabelle necessarie;
- riferimenti alle visuali;
- snippet essenziali;
- riepilogo;
- controlli ed esercizi;
- riferimenti principali e rinvii ai materiali verificabili.

I metadati possono essere conservati in un commento HTML o in front matter non renderizzato:

```text
<!--
chapter_id:
part_id:
order_key:
title:
version:
status:
last_source_check:
environment:
deferred:
-->
```

Non fanno parte del flusso del manuale:

- stato della candidatura;
- esito degli audit;
- immagini respinte;
- branch, commit e pull request;
- registro finale di approvazione;
- elenco completo dei file di lavorazione;
- dettagli di riproducibilità non necessari alla comprensione.

Questi dati restano in `PLAN.md`, `TEXT_AUDIT.md`, `CHANGELOG.md`, `REVIEW.md` e `code/`.

## File `PLAN.md`

Contiene:

- domanda centrale;
- oggetto continuo;
- stato iniziale e gap;
- output finale;
- sequenza delle transizioni;
- input, output, shape, invarianti e confini;
- concetti differiti;
- storyboard delle visuali;
- piano degli snippet;
- rischi tecnici, didattici ed editoriali;
- criteri di completamento.

Lo scaffold di progettazione non determina i titoli visibili di `CHAPTER.md`.

## File `FONTI_PRIMARIE.md`

Ogni voce indica:

- ID;
- dati bibliografici;
- versione, revisione o commit;
- data di consultazione;
- sezioni rilevanti;
- affermazioni sostenibili;
- limiti e divergenze.

## File `CLAIMS.md`

Contiene il registro frase-prova.

Stati:

```text
aperta
verificata
corretta
respinta
rimossa
```

Una voce `aperta` non entra come affermazione assertiva nella versione approvata.

## File `TEXT_AUDIT.md`

Registra:

- versione esaminata;
- data;
- fonti riaperte;
- claim corretti o rimossi;
- errori matematici;
- problemi di terminologia;
- divergenze;
- audit temporale;
- review didattica;
- gate anti-template;
- review editoriale e linguistica;
- profili di lettore simulati;
- lettura ad alta voce;
- artefatti riaperti;
- esito.

## File `CHANGELOG.md`

Registra le modifiche tra versioni:

- correzioni fattuali;
- riscritture didattiche;
- riscritture editoriali;
- modifiche a formule, visuali e codice;
- review riaperte;
- decisioni di governance applicate.

## File `REVIEW.md`

È la guida alla revisione autoriale. Indica:

- versione da leggere;
- percorso consigliato;
- modifiche principali;
- aspetti da valutare;
- stato di codice e visuali;
- decisioni richieste all'autore.

## Cartella `code/`

### `README.md`

Descrive ambiente, installazione, comandi e mappa degli snippet.

### `CODE_AUDIT.md`

Registra:

- API verificata;
- ambiente;
- comando;
- output;
- test;
- confronto indipendente;
- problemi trovati;
- stato finale.

### `outputs/`

Contiene output letterali. Un output mostrato come `Eseguito` deve essere riconducibile a un file o a un test.

### `environments/`

Contiene almeno:

```text
sistema operativo o container
Python
libreria
CPU o GPU
CUDA, quando applicabile
dtype
seed
```

I dettagli completi restano in questa cartella e non interrompono il testo del manuale.

## Asset visuali

Percorso:

```text
assets/chapters/<NN_slug>/<FIG-ID>/
  candidate-vN.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

Dopo l'approvazione:

```text
assets/chapters/<NN_slug>/<FIG-ID>/
  final.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

Regole:

- `final.png` soltanto dopo approvazione;
- `SPEC.md` descrive domanda, nodi, frecce, shape, valori e ordine;
- `AUDIT.md` registra iterazioni, difetti e verdetto;
- `ALT_TEXT.md` contiene alt text ed equivalente testuale;
- bozze respinte non vengono nominate `final`;
- nessun watermark, firma o branding;
- formato principale PNG ad alta risoluzione.

## ID

### Visuali

```text
<SIGLA>-<numero a due cifre>
```

Esempio: `ATT-01`.

### Claim

```text
CLM-<SIGLA>-<numero a tre cifre>
```

### Snippet

```text
SNIP-<SIGLA>-<numero a tre cifre>
```

### Fonti

```text
SRC-<SIGLA>-<numero a tre cifre>
```

Gli ID sono stabili e non vengono riutilizzati per oggetti diversi.

## Cartella `scripts/`

Può contenere strumenti per:

- validazione dei link;
- controllo degli ID;
- esecuzione degli snippet;
- verifica delle citazioni locali;
- controllo degli asset;
- generazione di report.

Gli script non sostituiscono la review umana o tecnica.

## Cartella `tests/`

Contiene test trasversali, separati dai test specifici dei capitoli.

## Convenzioni per i nomi

- cartelle e file tecnici: ASCII e underscore negli slug;
- documenti canonici: prefisso numerico per l'ordine;
- nessuno spazio nei nomi di asset e script;
- `.md` per documentazione e capitoli;
- `.png` per immagini;
- `.py` per Python.

## Commit

I commit descrivono l'unità di cambiamento. Non dichiarano approvazione quando i gate non sono completi.

Esempi:

```text
Add primary source dossier for attention scoring
Rewrite Chapter 1 with canonical manual voice
Record language review after read-aloud pass
Approve ATT-01 after visual QA
Freeze Chapter 28 editorial version
```

## Congelamento

Il commit di congelamento identifica:

- testo esatto;
- fonti e claim;
- immagini finali;
- codice e test;
- output e ambiente;
- audit;
- data editoriale.

Il commit SHA viene riportato negli artefatti operativi e in `PROGRESS.md`, non necessariamente nel flusso di `CHAPTER.md`.

## Progressi

`PROGRESS.md` riporta lo stato sintetico e non sostituisce gli audit.

Stati consigliati:

```text
non iniziato
ricerca
stesura
review tecnica
review didattica
review editoriale
review autoriale
approvato
sospeso
```

## Modifiche ai documenti canonici

Quando una decisione modifica più protocolli, gli aggiornamenti vengono completati prima di riprendere la produzione. Il registro delle decisioni viene aggiornato nello stesso ciclo.
