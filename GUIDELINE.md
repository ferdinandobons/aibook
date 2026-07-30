# GUIDELINE

## Stato e funzione

- Stato: `vincolante`
- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Lingua: italiano
- Formato: Markdown
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Architettura editoriale: `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Aggiornamenti: `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`

Questo file è l'entry point operativo. Una persona o un sistema AI privo del contesto originario deve poterlo usare per modificare il libro senza rompere accuratezza, struttura, voce o tracciabilità.

## 1. Obiettivo

Il repository contiene l'opera canonica **Intelligenza artificiale generativa**, un manuale tecnico in italiano dai fondamenti matematici ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

Il libro è organizzato per problemi, meccanismi e contratti tecnici. I modelli specifici vengono usati come studi di caso.

Ogni capitolo tecnico integra:

1. testo verificato e revisionato linguisticamente;
2. immagini tecniche sottoposte ad audit iterativo;
3. codice eseguito e testato.

## 2. Ordine di lettura

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

Per scrivere o revisionare una lezione:

- `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`;
- `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- `docs/01_TEMPLATE_CAPITOLO.md`;
- `docs/04_PROTOCOLLO_QA_TESTO.md`;
- `docs/06_WORKFLOW_CAPITOLO.md`.

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
3. consultare `docs/08_REGISTRO_DECISIONI.md`;
4. proporre una risoluzione esplicita;
5. aggiornare tutti i documenti coinvolti;
6. registrare il cambiamento.

## 4. Accuratezza

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.

Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale richiede una prova tra:

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

Ogni passaggio:

- parte dall'output precedente;
- introduce una trasformazione o distinzione dominante;
- rende comprensibili input, operazione e output;
- dichiara invarianti e confini;
- prepara il passaggio successivo.

Termini, formule, codice, varianti e visuali compaiono dopo che il referente concreto è stabile.

### Scaffold interno

`PLAN.md` e `TEXT_AUDIT.md` registrano in forma esplicita:

```text
stato
problema
input
operazione
output
cambiamento
invariante
confine
passaggio successivo
```

### Testo del manuale

`CHAPTER.md` non mostra lo scaffold come una checklist. Usa titoli semantici, sezioni abbastanza ampie e paragrafi causali.

Il reviewer deve poter ricostruire la logica; il lettore deve incontrare una spiegazione.

## 6. Voce editoriale

Il libro deve sembrare scritto direttamente in italiano.

Regole:

- testo discorsivo e preciso;
- sintassi italiana anche con termini tecnici inglesi;
- niente calchi evitabili;
- ritmo variato;
- sezioni non frammentate per ogni micro-operazione;
- cautele non ripetute oltre il necessario;
- esempio continuo mantenuto durante le astrazioni;
- dettagli operativi spostati negli artefatti;
- metadati nascosti in commenti, front matter o file interni;
- lettura ad alta voce obbligatoria.

Sono difetti bloccanti:

- prosa da specifica, audit o reference API;
- metadati di progetto nel flusso della lezione;
- microsezioni eccessive;
- ritmo meccanico;
- calchi non necessari;
- riepilogo ridotto a checklist.

La review simula un lettore nuovo, un lettore tecnico e un lettore che riprende il capitolo dopo tempo.

## 7. Architettura stabile

Il repository contiene una sola opera canonica. Volume, tomi, sito e corso sono export della stessa sorgente.

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

## 8. Routing e maturità

Per collocare una tecnica:

1. descrivere il problema;
2. identificare l'oggetto modificato;
3. localizzare la fase del ciclo di vita;
4. scegliere la parte proprietaria;
5. registrare riferimenti secondari senza duplicare la spiegazione.

Maturità:

- `CORE`;
- `ESTABLISHED`;
- `FRONTIER`.

La maturità cambia con nuove prove e non sposta automaticamente la tecnica.

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
stato
prerequisiti
successori
alias
```

Gli ID restano stabili. Split e merge richiedono una mappa di migrazione.

## 10. Nuove tecniche e aggiornamenti

Seguire le procedure U1-U8 di `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`:

- nuova tecnica;
- nuova evidenza;
- aggiornamento API;
- cambio di maturità;
- nuovo capitolo;
- split o merge;
- correzione tecnica;
- nuova edizione.

Il catalogo non dichiara completezza assoluta.

## 11. Visuali

Ogni immagine tecnica:

- risponde a una domanda;
- usa sfondo bianco puro `#FFFFFF`;
- sceglie orientamento in base al contenuto;
- segue palette e grammatica comuni;
- contiene testo e simboli nei propri box;
- non presenta frecce ambigue;
- viene rigenerata finché non supera l'audit;
- diventa `final.png` dopo approvazione tecnica e autoriale.

Non si usano render completi delle pagine come figure tecniche.

## 12. Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.

- Python e PyTorch sono predefiniti.
- NumPy è ammesso per controlli indipendenti.
- Pseudocodice e codice eseguibile restano distinti.
- Le API vengono verificate.
- Il codice viene eseguito in un processo pulito.
- Gli invarianti vengono testati.
- Un output è `Eseguito` soltanto con ambiente, comando e log o test.

Nel corpo appare soltanto la porzione utile alla spiegazione. I dettagli completi restano negli artefatti.

## 13. Workflow

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
-> review linguistica
-> lettura ad alta voce
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

Non si passa al capitolo successivo finché quello corrente non è approvato o formalmente sospeso.

## 14. Convenzioni Git

Il report finale indica:

```text
Operazione eseguita:
File modificati:
Fonti riaperte:
Claim modificati:
Test eseguiti:
Review riaperte:
Problemi rimasti:
Commit:
Data di verifica:
```

## 15. Azioni vietate

Non:

- inventare fonti, risultati, versioni o citazioni;
- usare un blog come unica prova portante;
- estendere un risultato oltre la fonte;
- creare un capitolo per ogni prodotto;
- spostare una tecnica soltanto perché cambia maturità;
- rinumerare gli ID stabili;
- presentare pseudocodice come eseguibile;
- chiamare `Eseguito` un output non prodotto;
- approvare una visuale ambigua;
- approvare una lezione che sembra una checklist o una specifica;
- lasciare metadati operativi nel manuale;
- dichiarare il libro aggiornato oltre la data verificata.

## 16. Inizializzazione di una nuova sessione

Una nuova sessione assume:

```text
Sto operando sul repository aibook.
La fonte di verità è il repository.
Leggo GUIDELINE.md e i documenti canonici prima di modificare contenuti.
Non introduco fatti senza prova.
Non modifico le parti stabili senza governance.
Uso uno scaffold rigoroso internamente e una voce da manuale nel testo pubblico.
Eseguo review didattica, anti-template, linguistica e lettura ad alta voce.
Applico routing, maturità e tracciabilità a ogni aggiornamento.
```
