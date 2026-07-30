# GUIDELINE

## Stato e funzione

- Stato: `vincolante`
- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Lingua: italiano
- Formato sorgente: Markdown
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Architettura editoriale: `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Aggiornamenti futuri: `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`

Questo file è l'entry point operativo del progetto. Una persona o un sistema AI senza il contesto della conversazione originaria deve poterlo usare per capire come leggere il repository e come modificare il libro senza rompere accuratezza, struttura o coerenza.

## 1. Obiettivo

Il repository contiene l'opera canonica **Intelligenza artificiale generativa**, un manuale tecnico in italiano dai fondamenti matematici ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

Il libro è organizzato per problemi, meccanismi e contratti tecnici. I singoli modelli vengono usati come studi di caso, non come struttura dell'opera.

Ogni capitolo tecnico integra:

1. testo verificato;
2. immagini tecniche sottoposte ad audit iterativo;
3. codice eseguito e testato.

## 2. Ordine di lettura obbligatorio

Leggere:

1. `GUIDELINE.md`;
2. `README.md`;
3. `docs/README.md`;
4. `docs/00_CONTRATTO_EDITORIALE.md`;
5. `docs/08_REGISTRO_DECISIONI.md`;
6. `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
7. `docs/14_CATALOGO_STATO_ARTE.md`;
8. `docs/10_INDICE_EDITORIALE.md`;
9. `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
10. il protocollo specialistico relativo al compito;
11. `PROGRESS.md`;
12. gli artefatti dell'area coinvolta.

Per scrivere o revisionare una lezione, leggere inoltre:

- `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- `docs/01_TEMPLATE_CAPITOLO.md`;
- `docs/04_PROTOCOLLO_QA_TESTO.md`.

Per le immagini:

- `docs/17_STANDARD_VISIVO_CANONICO.md`;
- `docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`;
- `docs/02_TEMPLATE_VISUALE.md`;
- `docs/03_PROTOCOLLO_QA_VISUALE.md`.

## 3. Fonte di verità

La fonte di verità è il repository, non la memoria della conversazione.

In caso di conflitto:

1. sospendere la modifica;
2. identificare i documenti incompatibili;
3. consultare il registro delle decisioni;
4. proporre una risoluzione esplicita;
5. aggiornare tutti i documenti coinvolti;
6. registrare il cambiamento con un commit descrittivo.

## 4. Accuratezza

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

## 5. Metodo didattico

Ogni capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale.

Ogni transizione:

- parte dall'output della precedente;
- introduce un solo concetto nuovo;
- rende comprensibili input, operazione, output, cambiamento, invariante e confine;
- consegna il risultato al passaggio successivo.

Termini, formule, codice, varianti e visuali compaiono dopo che il referente concreto è stabile.

### Scaffold interno e prosa pubblicata

Lo scaffold didattico è obbligatorio in `PLAN.md` e `TEXT_AUDIT.md`. Il capitolo destinato al lettore non deve però apparire come una checklist compilata.

Per impostazione predefinita non si usano ripetutamente come titoli:

```text
Stato del lettore
Dove siamo
Problema locale
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

Queste funzioni vengono incorporate in paragrafi naturali e titoli semantici. Il reviewer deve poter ricostruire la logica; il lettore non deve vedere il modulo di progettazione.

La review didattica include un gate anti-template e viene ripetuta dopo ogni correzione strutturale.

## 6. Architettura stabile dell'opera

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

## 7. Routing di una tecnica

Per assegnare una collocazione primaria:

1. descrivere il problema risolto;
2. identificare l'oggetto modificato;
3. localizzare il punto del ciclo di vita;
4. scegliere la parte proprietaria dell'oggetto;
5. registrare collegamenti secondari senza duplicare la spiegazione.

Un modello che combina tecniche già note viene normalmente trattato come studio di caso.

## 8. Maturità

- `CORE`: durevole e necessario per numerosi sviluppi successivi.
- `ESTABLISHED`: verificato e rilevante, ma non universale o ancora in evoluzione.
- `FRONTIER`: recente, sperimentale o con evidenza limitata.

Il percorso ordinario è:

```text
FRONTIER -> ESTABLISHED -> CORE
```

Una modifica di maturità richiede nuove prove e non sposta automaticamente la tecnica tra le parti.

## 9. Identità dei capitoli

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
alias storici
```

Gli ID restano stabili. Split e merge richiedono una mappa di migrazione.

## 10. Nuove tecniche e aggiornamenti

Seguire una delle procedure U1-U8 di `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`:

- nuova tecnica;
- nuova evidenza;
- aggiornamento API;
- cambio di maturità;
- nuovo capitolo;
- split o merge;
- correzione tecnica;
- nuova edizione.

Il catalogo non dichiara completezza assoluta. Censisce le principali famiglie che soddisfano i criteri di inclusione alla data registrata.

## 11. Visuali

Ogni immagine tecnica:

- risponde a una domanda;
- usa sfondo bianco puro `#FFFFFF`;
- sceglie orientamento orizzontale o verticale in base al contenuto;
- segue la palette e la grammatica comuni;
- contiene integralmente testo e simboli nei propri box;
- non presenta frecce ambigue;
- viene rigenerata finché non supera l'audit;
- diventa `final.png` soltanto dopo approvazione tecnica e autoriale.

Non si usano render completi delle pagine come figure tecniche.

## 12. Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.

- Python e PyTorch sono predefiniti.
- NumPy può essere usato per controlli indipendenti.
- Pseudocodice e codice eseguibile restano distinti.
- Le API vengono verificate sulla documentazione ufficiale.
- Il codice viene eseguito in un processo pulito.
- Gli invarianti vengono testati.
- Un output è `Eseguito` soltanto quando esistono ambiente, comando e log o test.

## 13. Workflow di un capitolo

```text
ricerca
-> claim
-> piano interno
-> prima stesura
-> formule
-> codice e test
-> visuali e audit
-> audit fattuale e matematico
-> review didattica
-> gate anti-template
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

Non si passa al capitolo successivo finché quello corrente non è approvato o formalmente sospeso.

## 14. Convenzioni Git

I commit descrivono l'unità di cambiamento. Il report finale indica:

```text
Operazione eseguita:
File modificati:
Fonti riaperte:
Claim modificati:
Test eseguiti:
Audit riaperti:
Problemi rimasti:
Commit:
Data di verifica:
```

## 15. Azioni vietate

Non:

- inventare fonti, risultati, versioni o citazioni;
- usare un blog come unica prova portante;
- estendere il risultato di un paper a tutte le implementazioni;
- creare un capitolo per ogni prodotto;
- spostare una tecnica perché cambia maturità;
- rinumerare gli ID stabili;
- presentare pseudocodice come eseguibile;
- chiamare `Eseguito` un output non prodotto;
- approvare una visuale ambigua;
- approvare una lezione che appare come una checklist ripetitiva;
- dichiarare il libro aggiornato oltre la data verificata.

## 16. Inizializzazione di una nuova sessione

Una nuova sessione deve assumere internamente:

```text
Sto operando sul repository aibook.
La fonte di verità è il repository.
Leggo GUIDELINE.md e i documenti canonici prima di modificare contenuti.
Non introduco fatti senza prova.
Non modifico le parti stabili senza governance.
Uso uno scaffold rigoroso internamente e prosa naturale nel capitolo destinato al lettore.
Applico routing, maturità, review e tracciabilità a ogni aggiornamento.
```