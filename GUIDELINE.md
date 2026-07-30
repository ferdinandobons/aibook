# GUIDELINE

## Funzione

Questo file è l'entry point operativo del progetto `ferdinandobons/aibook`.

Una persona o un sistema AI senza il contesto della conversazione originaria deve poterlo usare per comprendere il libro, leggere la documentazione, scrivere o revisionare capitoli, aggiungere tecniche e conservare accuratezza, voce editoriale e tracciabilità.

La fonte di verità è il repository, non la memoria della conversazione.

## 1. Obiettivo

Il repository contiene l'opera canonica **Intelligenza artificiale generativa**, un manuale tecnico in italiano dai fondamenti matematici ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

Ogni capitolo tecnico integra:

1. testo verificato e scritto come manuale;
2. immagini tecniche sottoposte a review iterativa;
3. codice eseguito e testato;
4. fonti, claim e audit.

## 2. Ordine di lettura

Leggere:

1. `GUIDELINE.md`;
2. `README.md`;
3. `docs/README.md`;
4. `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
5. `docs/01_INDICE_EDITORIALE.md`;
6. `docs/14_CATALOGO_STATO_ARTE.md`;
7. `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`;
8. il documento specialistico necessario;
9. `PROGRESS.md`;
10. gli artefatti del capitolo coinvolto.

Documenti specialistici:

- testo e didattica: `docs/02_STILE_E_QA_TESTO.md`;
- immagini: `docs/03_VISUALI.md`;
- fonti, claim, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- workflow, repository e aggiornamenti U1-U8: `docs/05_WORKFLOW_E_REPOSITORY.md`.

## 3. Accuratezza

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.

Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale richiede almeno una prova tra:

- paper originale o atti ufficiali;
- technical report ufficiale;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita;
- risultato riprodotto con ambiente, comando, output e test.

Una frase plausibile non è sufficiente. Se una fonte non stabilisce un punto, il punto viene ristretto, omesso o mantenuto fuori dal testo approvato.

## 4. Prosa del manuale

Ogni capitolo mantiene un oggetto concreto dall'apertura alla ricostruzione finale.

Lo scaffold di stato, problema, input, trasformazione, output, invariante, confine e passaggio successivo resta in `PLAN.md` e `TEXT_AUDIT.md`.

`CHAPTER.md` deve invece leggersi come un manuale tecnico in italiano:

- titoli semantici;
- sezioni abbastanza ampie da sostenere un ragionamento;
- paragrafi naturali e causali;
- esempio continuo;
- termini introdotti dopo il referente;
- formule e codice dopo il meccanismo;
- niente metadati o registri di audit nel flusso;
- niente ritmo da checklist o reference API;
- niente calchi non necessari dall'inglese;
- lettura ad alta voce obbligatoria.

Ogni capitolo supera review didattica, gate anti-template, review editoriale e linguistica, verifica con tre profili di lettore e nuova lettura integrale dopo le correzioni.

## 5. Architettura stabile

Il repository contiene una sola opera canonica. Volume unico, tomi, sito e corso sono export della stessa sorgente.

Le parti stabili sono:

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

Una nuova tecnica non rinomina o riordina automaticamente le parti.

## 6. Routing e maturità

Per collocare una tecnica:

1. descrivere il problema risolto;
2. identificare l'oggetto modificato;
3. localizzare il punto del ciclo di vita;
4. scegliere la parte proprietaria dell'oggetto;
5. registrare collegamenti secondari senza duplicare la spiegazione.

Maturità:

- `CORE`, durevole e necessario;
- `ESTABLISHED`, verificato e rilevante, ma ancora in evoluzione o non universale;
- `FRONTIER`, recente, sperimentale o con evidenza limitata.

La maturità può cambiare senza spostare la tecnica tra le parti.

## 7. Identità

Il numero stampato non è l'identità.

Ogni capitolo possiede:

```text
chapter_id
part_id
order_key
titolo
slug
maturità
stato editoriale
prerequisiti
successori
alias
```

Gli ID restano stabili. Split e merge richiedono migrazione, alias e controllo dei riferimenti.

## 8. Visuali

Ogni immagine tecnica:

- risponde a una domanda;
- usa sfondo bianco puro `#FFFFFF`;
- sceglie orientamento in base al contenuto;
- segue palette, box, frecce e tipografia comuni;
- contiene integralmente testo e simboli;
- non presenta collegamenti ambigui;
- viene rigenerata finché non supera l'audit;
- diventa `final.png` soltanto dopo approvazione tecnica e autoriale.

Non si usano render completi delle pagine come figure tecniche.

## 9. Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.

- Python e PyTorch sono predefiniti.
- NumPy può essere usato per controlli indipendenti.
- Pseudocodice e codice eseguibile restano distinti.
- Le API vengono verificate sulla documentazione ufficiale.
- Il codice viene eseguito in un processo pulito.
- Gli invarianti vengono testati.
- Un output è `Eseguito` soltanto con ambiente, comando e log o test.

## 10. Workflow

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

Non si passa al capitolo successivo finché quello corrente non è approvato o formalmente sospeso.

## 11. Aggiornamenti

Le operazioni U1-U8 sono definite in `docs/05_WORKFLOW_E_REPOSITORY.md`:

- U1 nuova tecnica;
- U2 nuova evidenza;
- U3 API o implementazione;
- U4 maturità;
- U5 nuovo capitolo;
- U6 split o merge;
- U7 correzione tecnica;
- U8 nuova edizione.

Il catalogo non dichiara completezza assoluta. Censisce le principali famiglie che soddisfano i criteri di inclusione alla data registrata.

## 12. Convenzioni Git

Ogni report di modifica indica:

```text
Operazione:
File modificati:
Fonti riaperte:
Claim modificati:
Test eseguiti:
Audit riaperti:
Problemi rimasti:
Commit:
Data di verifica:
```

Non dichiarare approvazione quando i gate non sono completi.

## 13. Azioni vietate

Non:

- inventare fonti, versioni, risultati o citazioni;
- usare un blog come unica prova portante;
- estendere il risultato di un paper a tutte le implementazioni;
- creare un capitolo per ogni prodotto;
- spostare una tecnica perché cambia maturità;
- rinumerare gli ID stabili;
- presentare pseudocodice come eseguibile;
- chiamare `Eseguito` un output non prodotto;
- approvare una visuale ambigua;
- approvare una lezione schematica, frammentata o poco naturale;
- dichiarare il libro aggiornato oltre la data verificata.

## 14. Inizializzazione di una nuova sessione

```text
Sto operando sul repository aibook.
La fonte di verità è il repository.
Leggo GUIDELINE.md e i documenti canonici prima di modificare contenuti.
Non introduco fatti senza prova.
Non modifico le parti stabili senza governance.
Uso uno scaffold rigoroso internamente e prosa da manuale nel testo pubblico.
Applico routing, maturità, review e tracciabilità a ogni aggiornamento.
```
