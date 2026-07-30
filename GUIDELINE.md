# GUIDELINE

## Stato e funzione

- Stato: `vincolante`
- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Lingua dell'opera: italiano
- Formato sorgente: Markdown
- Ultima ricerca approfondita globale registrata: **30 luglio 2026**
- Architettura editoriale canonica: `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`
- Protocollo per gli aggiornamenti: `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`

Questo file è l'entry point operativo del progetto. Deve permettere a una persona o a un sistema AI privo del contesto della conversazione originaria di comprendere come leggere il repository, modificare il libro, integrare nuove tecniche e verificare la coerenza del risultato.

Non iniziare una modifica sostanziale leggendo soltanto il file coinvolto. Il progetto è governato da documenti coordinati e da quality gate obbligatori.

## 1. Obiettivo del progetto

Il repository contiene l'opera canonica **Intelligenza artificiale generativa**, un manuale tecnico in italiano che accompagna il lettore dai fondamenti matematici e computazionali fino alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi di produzione, alla valutazione e alla sicurezza.

L'obiettivo non è creare una cronaca di prodotti. Il libro spiega problemi, meccanismi, contratti tensoriali, algoritmi, trade-off e sistemi. I singoli modelli vengono usati come studi di caso quando aiutano a verificare o localizzare una tecnica.

Ogni capitolo tecnico integra tre livelli coerenti:

1. testo didattico verificato;
2. visuali tecniche sottoposte ad audit iterativo;
3. codice eseguito, testato e collegato al meccanismo spiegato.

## 2. Lettura obbligatoria prima di operare

Leggere nell'ordine:

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
12. i file del capitolo o dell'area coinvolta.

Protocolli specialistici:

- testo e claim: `docs/04_PROTOCOLLO_QA_TESTO.md`;
- codice: `docs/05_STANDARD_SNIPPET_CODICE.md`;
- workflow di capitolo: `docs/06_WORKFLOW_CAPITOLO.md`;
- fonti e citazioni: `docs/07_POLITICA_FONTI_CITAZIONI.md`;
- visuali: `docs/02_TEMPLATE_VISUALE.md` e `docs/03_PROTOCOLLO_QA_VISUALE.md`;
- stile didattico: `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- struttura dei file: `docs/09_STRUTTURA_REPOSITORY.md`.

## 3. Ordine di autorità

La fonte di verità è il repository, non la memoria della conversazione e non la conoscenza implicita del sistema AI.

In caso di conflitto:

1. sospendere la modifica interessata;
2. identificare i documenti in conflitto;
3. consultare `docs/08_REGISTRO_DECISIONI.md`;
4. proporre una risoluzione esplicita;
5. aggiornare tutti i documenti coinvolti nello stesso ciclo;
6. registrare il cambiamento con un commit descrittivo.

Non è ammesso scegliere silenziosamente una regola e ignorarne un'altra.

## 4. Principi non negoziabili

### 4.1 Accuratezza

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.

Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale deve essere sostenuta da almeno una delle seguenti prove:

- paper originale o atti ufficiali;
- technical report ufficiale;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita e ricontrollata;
- risultato riprodotto con ambiente, comando, output e test registrati.

Una frase plausibile non è sufficiente. Quando una fonte non permette di verificare un punto, il punto viene ristretto, omesso oppure mantenuto come questione aperta fuori dal testo approvato.

### 4.2 Didattica

Ogni capitolo costruisce un modello mentale eseguibile. Lo stesso oggetto concreto attraversa la spiegazione dall'apertura alla ricostruzione finale.

Ogni transizione principale:

- parte dall'output esatto della precedente;
- introduce un solo concetto nuovo;
- esplicita input, trasformazione, output, cambiamento, invariante e confine;
- consegna l'output al consumer successivo.

Termini, formule, codice, varianti e visuali compaiono soltanto dopo che il referente concreto è stabile.

### 4.3 Coerenza degli artefatti

Testo, formule, immagini e codice devono condividere:

- nomi dei tensor e dei componenti;
- shape;
- valori illustrativi;
- ordine delle operazioni;
- invarianti;
- confini;
- versione tecnica descritta.

Una contraddizione tra due artefatti blocca l'approvazione.

### 4.4 Produzione seriale

Il libro viene prodotto e revisionato un capitolo alla volta. Non si genera l'intera opera in una singola passata e non si accumulano capitoli non revisionati.

## 5. Architettura stabile dell'opera

Il repository contiene una sola opera canonica e continua. L'opera può essere esportata come un volume unico, più tomi, un sito o un corso. Gli export non modificano la struttura canonica.

Le parti hanno ID, nome e domanda stabile:

| ID | Nome canonico |
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

Una nuova tecnica non rinomina e non riordina automaticamente queste parti. La collocazione dipende dal problema risolto e dall'oggetto modificato, non dalla data, dal nome del prodotto o dalla popolarità momentanea.

Una modifica a ID, nome o ordine delle parti richiede tutti i gate definiti in `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`, una mappa di migrazione e l'approvazione esplicita del committente.

## 6. Routing di una nuova tecnica

Per assegnare una collocazione primaria:

1. descrivere il problema risolto;
2. identificare l'oggetto che cambia;
3. localizzare il punto del ciclo di vita del modello;
4. scegliere la parte proprietaria di quell'oggetto;
5. registrare collegamenti secondari tramite tag e cross-reference;
6. evitare la duplicazione della spiegazione portante.

Routing rapido:

- nuovo formalismo o vincolo computazionale di base: `P02`;
- nuovo obiettivo, ottimizzatore o metodo decisionale: `P03`;
- nuovo layer neurale generale: `P04`;
- nuova famiglia generativa o processo di sampling di base: `P05`;
- nuova tokenizzazione, embedding, attention di base o rappresentazione sequenziale: `P06`;
- nuova tecnica di dati, scaling o pretraining: `P07`;
- nuovo blocco interno, attention variant, recurrence, SSM, MoE o routing: `P08`;
- nuovo fine-tuning, preference optimization, RL post-training, reasoning o test-time compute: `P09`;
- nuova modalità, world model o metodo embodied: `P10`;
- nuovo retrieval, RAG, sistema di memoria, tool o protocollo agentico: `P11`;
- nuova quantizzazione, compressione, decoding, cache, kernel, compiler o tecnica di serving: `P12`;
- nuova valutazione, interpretabilità, sicurezza, privacy o regola di governance: `P13`;
- replica, laboratorio o osservatorio trasversale: `P14`.

Un modello che combina più tecniche viene normalmente trattato come studio di caso. Non riceve un capitolo solo perché è recente o noto.

## 7. Maturità dei contenuti

La maturità è un attributo editoriale. Non equivale a un giudizio universale della comunità scientifica.

### `CORE`

Contenuto durevole, trasversale e necessario per comprendere numerosi sviluppi successivi.

### `ESTABLISHED`

Contenuto verificato e rilevante, adottato o riprodotto in più contesti, ma non ancora requisito universale oppure ancora soggetto a evoluzione significativa.

### `FRONTIER`

Contenuto recente, sperimentale, con evidenza limitata, terminologia instabile o dipendenza forte da uno specifico setup.

Percorso ordinario:

```text
FRONTIER -> ESTABLISHED -> CORE
```

Una promozione o demozione:

- richiede nuove prove;
- viene motivata in modo esplicito;
- aggiorna catalogo, indice e registri pertinenti;
- non cambia automaticamente `part_id`, `chapter_id` o ordine concettuale;
- riapre gli audit delle frasi che dipendono dalla classificazione.

I criteri completi sono in `docs/12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` e la procedura è in `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

## 8. Identità e numerazione dei capitoli

Il numero stampato non è l'identità di un capitolo.

Ogni capitolo possiede almeno:

```text
chapter_id:
part_id:
order_key:
titolo:
slug:
maturità:
stato editoriale:
prerequisiti:
successori:
alias storici:
```

Esempi di ID:

```text
CH-P06-ATTENTION
CH-P08-LINEAR-ATTENTION
CH-P09-RLVR
CH-P12-SPECULATIVE-DECODING
```

Regole:

- `chapter_id` è immutabile;
- il numero visualizzato è specifico dell'edizione;
- un nuovo capitolo viene inserito tramite `order_key` e dipendenze;
- la numerazione stampata viene aggiornata soltanto durante una nuova edizione;
- split e merge mantengono alias e mappa di migrazione;
- i riferimenti interni usano l'ID stabile quando possibile.

## 9. Decisione: sezione, approfondimento o nuovo capitolo

Una tecnica resta nel catalogo o in una sezione esistente quando:

- non possiede una domanda didattica autonoma;
- è una configurazione di una tecnica già coperta;
- il contributo principale è un caso di studio;
- le fonti non descrivono ancora un meccanismo sufficientemente stabile;
- una spiegazione completa sarebbe ridondante.

Un nuovo capitolo è giustificato quando:

1. esiste una domanda didattica autonoma;
2. il meccanismo ha input, trasformazione, output, invariante e confine propri;
3. inserirlo altrove interromperebbe l'oggetto continuo del capitolo ospite;
4. esistono fonti sufficienti per la parte portante;
5. è possibile progettare una visuale non ridondante;
6. è possibile creare codice verificabile o motivarne formalmente l'assenza;
7. prerequisiti e consumer successivi sono identificati.

## 10. Procedura per aggiungere una nuova tecnica

Seguire la procedura `U1` di `docs/13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

Sintesi obbligatoria:

1. registrare nome provvisorio, problema, input, operazione, output, invariante e confine;
2. verificare che non sia una rinominazione o una semplice combinazione;
3. raccogliere fonti primarie e ufficiali;
4. applicare il routing;
5. assegnare una maturità iniziale;
6. scegliere tra catalogo, sottosezione, approfondimento, studio di caso o capitolo;
7. aggiornare catalogo, indice, ricerca e decisioni pertinenti;
8. aprire gli audit quando il contenuto entra nel testo;
9. registrare la data di verifica e il commit.

Non inserire una tecnica come `CORE` soltanto perché viene usata da un modello importante.

## 11. Procedura per aggiornare una tecnica o un capitolo

1. identificare la versione descritta;
2. riaprire le fonti già usate;
3. cercare fonti primarie e documentazione ufficiale più recenti;
4. distinguere nuova evidenza, errata, deprecazione e cambiamento di implementazione;
5. aggiornare `CLAIMS.md` prima della prosa;
6. modificare il minimo insieme coerente di testo, formule, codice e visuali;
7. rieseguire i test;
8. ripetere gli audit interessati;
9. ricontrollare l'intero capitolo dopo le correzioni;
10. aggiornare la data di verifica senza estenderla a sezioni non ricontrollate.

## 12. Procedura per promuovere o demozionare una voce

Compilare una scheda con:

```text
Topic ID:
Stato precedente:
Stato proposto:
Data:
Nuove fonti:
Repliche o adozioni:
Terminologia:
Trade-off e failure mode:
Motivazione:
Impatto sui capitoli:
Reviewer:
```

La maturità non cambia per il solo trascorrere del tempo. Richiede evidenza aggiuntiva e controllo dei limiti.

Dopo la decisione aggiornare:

- `docs/14_CATALOGO_STATO_ARTE.md`;
- `docs/10_INDICE_EDITORIALE.md`, se il badge compare nell'indice;
- il dossier del capitolo;
- `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`;
- `docs/08_REGISTRO_DECISIONI.md`, quando la modifica ha impatto strutturale.

## 13. Ricerca approfondita e aggiornamento dello stato dell'arte

Una ricerca globale deve coprire almeno:

- dati, tokenizzazione e scaling;
- attention, recurrence, SSM, memorie e MoE;
- modelli autoregressivi, diffusion e flow;
- post-training, preference optimization e RL;
- reasoning e test-time compute;
- multimodalità e world model;
- retrieval, memoria, tool e agenti;
- quantizzazione, pruning, distillazione e decoding;
- serving, kernel, compiler e sistemi distribuiti;
- valutazione, interpretabilità, sicurezza, privacy e governance.

Ogni ricerca globale produce:

- ID e date;
- query e fonti consultate;
- criteri di inclusione;
- nuove voci e voci aggiornate;
- cambi di maturità proposti;
- buchi di copertura;
- impatto sull'indice;
- commit finale.

Frequenza minima:

- ricerca locale prima di ogni capitolo;
- ricontrollo delle informazioni recenti prima dell'approvazione;
- revisione delle voci `FRONTIER` almeno ogni 90 giorni durante la produzione attiva;
- ricerca globale prima di ogni nuova edizione;
- ricerca straordinaria quando emerge una nuova famiglia architetturale o un cambiamento normativo rilevante.

Non dichiarare che il catalogo contiene ogni lavoro esistente. La formulazione approvata è che censisce le principali famiglie e tecniche che soddisfano i criteri di inclusione alla data registrata.

## 14. Produzione di un capitolo

Per ogni capitolo seguire `docs/06_WORKFLOW_CAPITOLO.md`.

Artefatti minimi:

```text
chapters/<slug>/
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  CHAPTER.md
  TEXT_AUDIT.md
  CHANGELOG.md
  code/
    README.md
    CODE_AUDIT.md
    outputs/
    environments/
  assets/
```

Sequenza:

```text
ricerca
-> mappa delle affermazioni
-> piano didattico
-> prima stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit iterativo
-> audit fattuale e matematico
-> controllo incrociato
-> audit didattico
-> revisione autoriale
-> congelamento
```

## 15. Review del testo

Per ogni periodo tecnico controllare:

- quale parte è un fatto;
- quale fonte la sostiene;
- se la fonte dice realmente ciò che il testo afferma;
- se sono state aggiunte condizioni non presenti;
- se sono stati omessi limiti necessari;
- se paper, implementazione, checkpoint e prodotto sono distinti;
- se la terminologia coincide con la fonte;
- se formule, shape, numeri e arrotondamenti sono corretti.

Dopo ogni correzione sostanziale rileggere l'intero capitolo. Una modifica locale può introdurre incoerenze altrove.

## 16. Review del codice

Ogni snippet:

- usa import completi e minimi;
- dichiara input, shape, operazione centrale, output e invariante;
- registra Python, libreria, device, dtype e seed;
- viene verificato sulla documentazione ufficiale della versione dichiarata;
- viene eseguito in un processo pulito;
- include test degli invarianti;
- viene confrontato con formula, NumPy o API ufficiale quando possibile;
- viene rieseguito dopo ogni modifica.

Un output viene definito `Eseguito` soltanto quando esistono log o test riconducibili al file e all'ambiente registrati.

## 17. Review delle visuali

La prima immagine è sempre una bozza.

Per ogni visuale:

1. definire domanda unica, nodi, frecce, shape, valori, invariante e confine;
2. generare la bozza con lo strumento immagini;
3. rileggerla senza fare affidamento sul prompt;
4. controllare formula, numeri, shape, origine e destinazione di ogni freccia;
5. controllare incroci, giunzioni apparenti, callout e ordine di lettura;
6. rigenerare o modificare ogni difetto bloccante;
7. ripetere l'audit completo;
8. pubblicare `final.png` soltanto dopo l'approvazione.

Una singola linea ambigua è sufficiente per respingere la figura.

## 18. Aggiornamento coordinato dei documenti

Una nuova decisione globale richiede:

1. registrazione in `docs/08_REGISTRO_DECISIONI.md`;
2. aggiornamento del contratto;
3. aggiornamento dei protocolli coinvolti;
4. aggiornamento dei template;
5. controllo dei riferimenti incrociati;
6. aggiornamento dell'audit documentale;
7. commit descrittivo.

Non lasciare una nuova regola soltanto in `GUIDELINE.md` o soltanto in una conversazione.

## 19. Convenzioni Git e report

I commit descrivono l'unità di cambiamento, non il semplice nome del file.

Esempi:

```text
Add frontier entry for hybrid linear attention
Promote grouped-query attention to established after source review
Split agent memory chapter and preserve aliases
Update PyTorch attention snippets for version X.Y
Complete factual audit of Chapter CH-P06-ATTENTION
```

Il report finale di un'operazione deve indicare:

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

## 20. Azioni vietate

Non:

- inventare una fonte, un risultato, una versione o una citazione;
- usare un blog come unica prova di una descrizione portante;
- estendere il risultato di un paper a tutte le implementazioni;
- creare un capitolo per ogni modello commerciale;
- spostare una tecnica tra parti soltanto perché cambia maturità;
- rinumerare gli ID stabili;
- modificare parte, nome o ordine senza governance;
- presentare pseudocodice come codice eseguibile;
- chiamare `Eseguito` un output non prodotto dai file registrati;
- approvare una visuale con collegamenti ambigui;
- correggere un artefatto senza ricontrollare quelli dipendenti;
- dichiarare il libro aggiornato oltre la data effettivamente verificata.

## 21. Checklist rapida per un sistema AI senza contesto

Prima della modifica:

- [ ] Ho letto i documenti nell'ordine obbligatorio.
- [ ] Ho controllato `PROGRESS.md`.
- [ ] Ho identificato il tipo di operazione U1-U8.
- [ ] Ho identificato fonti e claim coinvolti.
- [ ] Ho determinato `part_id`, `chapter_id` e maturità.

Durante la modifica:

- [ ] Non sto introducendo fatti non verificati.
- [ ] Testo, formule, immagini e codice restano allineati.
- [ ] Le modifiche strutturali sono registrate nelle decisioni.
- [ ] Gli audit pertinenti sono stati riaperti.

Prima di chiudere:

- [ ] Ho rieseguito i test.
- [ ] Ho ripetuto gli audit dopo le correzioni.
- [ ] Ho aggiornato date, fonti, catalogo e indice quando necessario.
- [ ] Ho controllato i riferimenti interni.
- [ ] Ho preparato un report finale e un commit descrittivo.

## 22. Stato iniziale per una nuova sessione

Quando un sistema AI apre questo repository senza contesto, deve iniziare con la seguente dichiarazione operativa interna:

```text
Sto operando sul repository aibook.
La fonte di verità è il repository.
Leggo GUIDELINE.md e i documenti canonici prima di modificare contenuti.
Non introduco affermazioni fattuali senza prova.
Non modifico le parti stabili senza governance.
Applico routing, maturità, review e tracciabilità a ogni aggiornamento.
```

Dopo questa inizializzazione, il sistema può eseguire il compito richiesto seguendo il protocollo pertinente.