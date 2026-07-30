# Struttura del repository e convenzioni degli artefatti

## Scopo

La struttura deve permettere di ricostruire ogni capitolo, ogni affermazione, ogni immagine e ogni risultato eseguito a partire dal repository.

## Albero principale

```text
/
  README.md
  PROGRESS.md
  docs/
  chapters/
  assets/
  scripts/
  tests/
```

## Cartella `docs/`

La radice di `docs/` contiene la documentazione canonica. La sottocartella `source/` conserva copie archivistiche dei materiali originali ricevuti.

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
  EXPLANATION_STYLE_AND_VISUALS.md
  source/
    README.md
    EXPLANATION_STYLE_AND_VISUALS_ORIGINAL_PART_01.md
    EXPLANATION_STYLE_AND_VISUALS_ORIGINAL_PART_02.md
    EXPLANATION_STYLE_AND_VISUALS_ORIGINAL_PART_03.md
    EXPLANATION_STYLE_AND_VISUALS_ORIGINAL_PART_04.md
    EXPLANATION_STYLE_AND_VISUALS_ORIGINAL_PART_05.md
```

Nessuna regola vincolante deve esistere soltanto in una conversazione o in un file esterno.

I file in `docs/source/` non sono automaticamente vincolanti. Il loro adattamento canonico è indicato da `docs/source/README.md`.

## Cartella del capitolo

Nome:

```text
chapters/<NN_slug>/
```

Esempio:

```text
chapters/28_attention/
```

Struttura prevista:

```text
chapters/28_attention/
  CHAPTER.md
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  code/
    README.md
    CODE_AUDIT.md
    SNIP-ATT-001.py
    SNIP-ATT-001_test.py
    outputs/
      SNIP-ATT-001.txt
    environments/
      python-pytorch.txt
  assets/
    README.md
```

## Asset visuali

Gli asset finali vengono mantenuti in:

```text
assets/chapters/<NN_slug>/<FIG-ID>/
  final.png
  AUDIT.md
  ALT_TEXT.md
  SPEC.md
```

Esempio:

```text
assets/chapters/28_attention/ATT-01/
  final.png
  AUDIT.md
  ALT_TEXT.md
  SPEC.md
```

### Regole

- `final.png` esiste soltanto dopo l'approvazione.
- `SPEC.md` descrive domanda, nodi, frecce, shape, valori e ordine di lettura.
- `AUDIT.md` registra le iterazioni esaminate, i difetti e il verdetto.
- `ALT_TEXT.md` contiene alt text ed equivalente testuale esteso.
- Le bozze respinte non vengono nominate `final`.
- Le bozze possono restare fuori dal repository quando non servono alla tracciabilità.
- Nessuna immagine approvata contiene watermark, firma o branding di terzi.
- L'artefatto editoriale principale è PNG ad alta risoluzione.

## ID delle visuali

Formato:

```text
<sigla-capitolo>-<numero a due cifre>
```

Esempi:

```text
ATT-01
ATT-02
ATT-03
```

L'ID resta stabile durante le rigenerazioni. Le versioni vengono registrate come `v1`, `v2`, `v3` nell'audit.

## ID delle affermazioni

Formato:

```text
CLM-<sigla-capitolo>-<numero a tre cifre>
```

Esempio:

```text
CLM-ATT-001
```

Ogni ID compare in `CLAIMS.md` e può essere richiamato negli audit.

## ID degli snippet

Formato:

```text
SNIP-<sigla-capitolo>-<numero a tre cifre>
```

Esempio:

```text
SNIP-ATT-001
```

File associati:

```text
SNIP-ATT-001.py
SNIP-ATT-001_test.py
outputs/SNIP-ATT-001.txt
```

## ID delle fonti

Formato:

```text
SRC-<sigla-capitolo>-<numero a tre cifre>
```

Esempio:

```text
SRC-ATT-001
```

`CLAIMS.md` collega ogni claim a uno o più ID fonte.

## File `CHAPTER.md`

Contiene:

- metadati;
- bussola;
- evidenze e provenienza;
- prosa;
- formule;
- riferimenti alle visuali;
- snippet essenziali;
- esercizi;
- fonti;
- registri finali di approvazione.

Segue `docs/01_TEMPLATE_CAPITOLO.md`.

## File `PLAN.md`

Contiene:

- domanda centrale;
- oggetto continuo;
- stati del lettore;
- sequenza delle transizioni;
- concetti differiti;
- storyboard delle visuali;
- piano degli snippet;
- rischi tecnici e didattici;
- criteri di completamento.

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

Contiene il registro frase-prova. Non viene sostituito da una bibliografia generica.

Stati ammessi:

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
- claim corretti, ristretti o rimossi;
- errori matematici;
- problemi di terminologia;
- divergenze;
- controllo temporale;
- controllo dell'assenza di inferenze fattuali;
- audit didattico;
- esito.

## Cartella `code/`

### `README.md`

Descrive ambiente, installazione, comandi e mappa degli snippet.

### `CODE_AUDIT.md`

Registra per ogni snippet:

- API verificata;
- ambiente;
- comando;
- output;
- test;
- confronto indipendente;
- problemi trovati;
- stato finale.

### `outputs/`

Contiene output letterali generati dall'esecuzione. Un output mostrato nel libro come `Eseguito` deve essere riconducibile a un file o a un test.

### `environments/`

Contiene almeno:

```text
sistema operativo o container
Python
PyTorch o altra libreria
CPU o GPU
CUDA, quando applicabile
dtype
seed
```

## Cartella `scripts/`

Può contenere strumenti trasversali per:

- validazione dei link interni;
- controllo degli ID;
- esecuzione degli snippet;
- verifica delle citazioni locali;
- controllo degli asset mancanti;
- generazione di report.

Gli script non sostituiscono la review tecnica.

## Cartella `tests/`

Contiene test trasversali del progetto, separati dai test specifici dei capitoli.

## Convenzioni per i nomi

- cartelle e file tecnici: ASCII, minuscolo quando possibile, underscore per gli slug;
- documenti canonici: prefisso numerico per l'ordine di lettura;
- ID stabili e mai riutilizzati per un oggetto diverso;
- nessuno spazio nei nomi degli asset e degli script;
- `.md` per documentazione e capitoli;
- `.png` per immagini finali;
- `.py` per snippet eseguibili Python.

## Commit

I commit devono descrivere l'unità di cambiamento. Esempi:

```text
Add primary source dossier for attention scoring
Add and test minimal scaled-dot-product attention snippet
Record rejection of ATT-03 v2 after connection audit
Approve ATT-01 after visual QA
Complete factual review of Chapter 28 section 3
Freeze Chapter 28 editorial version
```

Non si usa un messaggio che dichiara approvazione quando l'audit non è completo.

## Congelamento

Il commit di congelamento di un capitolo deve permettere di identificare:

- testo esatto;
- fonti esatte;
- immagini finali;
- codice e test;
- output;
- audit;
- data editoriale.

Il commit SHA viene riportato in `CHAPTER.md` e in `PROGRESS.md`.

## Progressi

`PROGRESS.md` riporta lo stato sintetico e non sostituisce i registri di audit.

Stati consigliati:

```text
non iniziato
ricerca
pianificazione
stesura
review tecnica
review autoriale
approvato
sospeso
```

## Modifiche ai documenti canonici

Quando una decisione modifica più protocolli, gli aggiornamenti devono essere completati prima di riprendere la produzione dei capitoli. Il registro delle decisioni deve essere aggiornato nello stesso ciclo di modifica.