# AI Book

Repository canonico del libro **Intelligenza artificiale generativa**.

## Da dove iniziare

Una persona o un sistema AI senza contesto precedente legge:

1. [`GUIDELINE.md`](GUIDELINE.md), entry point operativo;
2. [`docs/README.md`](docs/README.md), mappa della documentazione;
3. [`PROGRESS.md`](PROGRESS.md), stato corrente;
4. [`BOOK_PRODUCTION.md`](BOOK_PRODUCTION.md), piano della produzione completa.

## Obiettivo

Costruire un manuale tecnico completo in italiano, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi di produzione, alla valutazione e alla sicurezza.

Il libro è organizzato per problemi, meccanismi e contratti tecnici. I modelli specifici vengono usati come studi di caso, non come struttura dell'opera.

## Forma dell'opera

Il repository contiene una sola opera canonica e continua. La stessa sorgente può essere esportata come volume unico, più tomi, sito, knowledge base o corso. L'export non cambia l'identità dei contenuti.

## Parti stabili

| ID | Parte |
|---|---|
| `P01` | Campo, metodo e storia dell'AI |
| `P02` | Matematica, informazione e calcolo |
| `P03` | Apprendimento, ottimizzazione e decisione |
| `P04` | Reti neurali e rappresentazioni |
| `P05` | Modellazione generativa |
| `P06` | Sequenze, linguaggio e contesto |
| `P07` | Dati, pretraining e scaling |
| `P08` | Progettazione delle architetture |
| `P09` | Adattamento, allineamento e ragionamento |
| `P10` | Multimodalità e modelli del mondo |
| `P11` | Conoscenza esterna, memoria e azione |
| `P12` | Efficienza, inference e sistemi |
| `P13` | Valutazione, interpretabilità, sicurezza e governance |
| `P14` | Laboratori, integrazione e osservatorio |

ID, nomi e ordine delle parti sono stabili. Le nuove tecniche vengono collocate in base al problema risolto e all'oggetto modificato.

## Indice e stato dell'arte

- Indice dell'opera: [`docs/01_INDICE_EDITORIALE.md`](docs/01_INDICE_EDITORIALE.md)
- Catalogo delle tecniche: [`docs/14_CATALOGO_STATO_ARTE.md`](docs/14_CATALOGO_STATO_ARTE.md)
- Registro delle ricerche globali: [`docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`](docs/15_REGISTRO_RICERCHE_APPROFONDITE.md)
- Ultima ricerca approfondita globale: **30 luglio 2026**

Ogni tecnica può essere classificata come `CORE`, `ESTABLISHED` o `FRONTIER`. La maturità può cambiare senza spostare la tecnica tra le parti.

## Documentazione consolidata

La documentazione canonica è stata condensata per tema:

| Documento | Contenuto |
|---|---|
| [`docs/00_GOVERNANCE_E_ARCHITETTURA.md`](docs/00_GOVERNANCE_E_ARCHITETTURA.md) | contratto editoriale, parti, routing, maturità, ID e decisioni |
| [`docs/01_INDICE_EDITORIALE.md`](docs/01_INDICE_EDITORIALE.md) | 98 capitoli, 12 appendici e regole dell'indice |
| [`docs/02_STILE_E_QA_TESTO.md`](docs/02_STILE_E_QA_TESTO.md) | metodo didattico, voce italiana, template e review del testo |
| [`docs/03_VISUALI.md`](docs/03_VISUALI.md) | stile visivo, sfondo bianco, orientamento, contenimento e QA |
| [`docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`](docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md) | fonti, claim, citazioni, snippet, test, API e ambienti |
| [`docs/05_WORKFLOW_E_REPOSITORY.md`](docs/05_WORKFLOW_E_REPOSITORY.md) | struttura dei file, produzione seriale e aggiornamenti U1-U8 |

I registri dettagliati del catalogo e della ricerca restano separati perché hanno struttura e ciclo di aggiornamento propri.

## Metodo di produzione

```text
ricerca
-> claim
-> piano interno
-> stesura
-> formule
-> codice e test
-> visuali e audit
-> audit tecnico
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> lettura ad alta voce
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

La produzione è seriale. Non si apre il capitolo successivo finché quello corrente non è approvato o formalmente sospeso.

## Stile delle lezioni

La struttura logica resta esplicita nei file di piano e audit. Il testo destinato al lettore deve però sembrare un manuale tecnico scritto direttamente in italiano:

- titoli semantici;
- sezioni non frammentate;
- esempio continuo;
- prosa fluida e discorsiva;
- formule e codice dopo il meccanismo;
- metadati e registri fuori dal flusso;
- lettura ad alta voce e review con tre profili di lettore.

## Visuali

Tutte le immagini tecniche:

- usano sfondo bianco puro `#FFFFFF`;
- possono essere orizzontali o verticali;
- condividono palette, box, frecce e tipografia;
- mantengono testo e simboli nei contenitori;
- vengono revisionate e rigenerate;
- non sono render delle pagine;
- diventano `final.png` soltanto dopo approvazione tecnica e autoriale.

## Codice e fonti

Ogni capitolo tecnico include codice eseguibile, salvo eccezione motivata. Python e PyTorch sono predefiniti. Le API vengono verificate sulla documentazione ufficiale; gli output dichiarati `Eseguito` possiedono ambiente, comando e test.

Ogni affermazione portante è collegata a una fonte primaria, a documentazione ufficiale, a uno standard, a una derivazione verificata o a una prova riproducibile.

## Struttura principale

```text
/
  README.md
  GUIDELINE.md
  PROGRESS.md
  BOOK_PRODUCTION.md
  docs/
  chapters/
  assets/
  scripts/
  tests/
```

## Stato corrente

Il Capitolo 28 sull'attention è il pilota approvato. Il Capitolo 1 è in revisione editoriale con visuali ancora aperte. Lo stato aggiornato è in [`PROGRESS.md`](PROGRESS.md).
