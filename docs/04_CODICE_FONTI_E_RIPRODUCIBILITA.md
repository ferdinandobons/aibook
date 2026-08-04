# Codice, fonti e riproducibilità

## Stato

- Stato: `vincolante`
- Ambito: fonti, citazioni, claim, numeri, API, snippet, test, output e ambienti
- Linguaggi principali: Python e PyTorch
- Controlli indipendenti: NumPy o implementazioni equivalenti quando utili

## 1. Principio

Ogni affermazione portante e ogni risultato mostrato nel libro devono essere riconducibili a una prova.

Una frase plausibile, diffusa o coerente con la letteratura non è verificata finché non viene controllata nel contenuto originale di una fonte ammessa. Un output non è `Eseguito` finché non deriva da codice, ambiente e comando registrati.

Il codice collega il meccanismo spiegato a una implementazione osservabile. Non sostituisce la spiegazione e non apre un secondo percorso concettuale.

## 2. Esclusione delle inferenze fattuali

La versione approvata non contiene affermazioni fattuali prodotte per inferenza editoriale.

Sono escluse, salvo attribuzione esplicita a una fonte che le formula:

- interpretazioni causali non dimostrate;
- generalizzazioni da un singolo modello a una famiglia;
- attribuzioni di intenzione agli autori;
- conclusioni architetturali da indizi incompleti;
- stime di prestazioni o costi non misurate;
- dettagli di implementazione non documentati;
- previsioni sul futuro presentate come fatti.

Le derivazioni matematiche sono ammesse quando partono da definizioni verificate, esplicitano i passaggi e vengono ricontrollate.

## 3. Gerarchia delle fonti

### Livello 1. Fonte primaria pubblicata

- atti ufficiali di conferenze;
- riviste scientifiche;
- standard;
- documenti istituzionali e normativi.

Fonte preferita per metodi, risultati, definizioni e norme.

### Livello 2. Fonte ufficiale degli autori

- versione ufficiale su arXiv;
- technical report;
- model card, system card o data card;
- supplemento tecnico.

Si registra la revisione esatta.

### Livello 3. Documentazione ufficiale

- PyTorch, JAX, CUDA e altre librerie;
- specifiche API;
- note di rilascio;
- guide ufficiali.

Fonte preferita per firme, comportamento documentato, versioni e semantica corrente.

### Livello 4. Repository ufficiale

- repository degli autori o dell'organizzazione;
- codice di riferimento;
- test;
- configurazioni;
- commit.

Il comportamento del codice non viene attribuito automaticamente al paper.

### Livello 5. Fonti secondarie

Blog, articoli, post, video e discussioni possono aiutare a trovare fonti primarie. Non sostengono da soli una spiegazione portante, una formula, un dato, una firma API, una descrizione architetturale o un requisito normativo.

## 4. Fonte adeguata al claim

| Affermazione | Fonte preferita |
|---|---|
| Definizione di un metodo | paper originale o standard |
| Risultato sperimentale | tabella o sezione del paper, con setup |
| Architettura di un modello | report, model card o repository ufficiale |
| Comportamento di un'API | documentazione della versione dichiarata |
| Dettaglio implementativo | repository e commit |
| Requisito legale | testo ufficiale dell'ente competente |
| Valore prodotto nel libro | script, ambiente, log e test |
| Esempio didattico | etichetta `Illustrativo` e verifica interna |

## 5. Dossier delle fonti

Ogni capitolo contiene `FONTI_PRIMARIE.md`.

Per ogni voce:

```text
ID fonte:
Titolo:
Autori o organizzazione:
Tipo:
Data:
Versione, revisione o commit:
URL o identificatore:
Data di consultazione:
Sezioni rilevanti:
Affermazioni sostenibili:
Limiti:
Divergenze note:
```

Una fonte non viene citata genericamente per sostenere un'intera sezione quando soltanto una parte è pertinente.

## 6. Registro delle affermazioni

Ogni claim portante riceve un ID stabile in `CLAIMS.md`.

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

Stati:

```text
aperta
verificata
corretta
respinta
rimossa
```

Una voce `aperta` non entra come frase assertiva.

Il controllo chiede:

1. la fonte formula davvero il claim?
2. il testo è più forte della fonte?
3. condizioni e limiti sono conservati?
4. la fonte descrive metodo, implementazione o esperimento?
5. esistono revisioni o errata?
6. data e versione sono pertinenti?
7. fonti affidabili qualificano o contraddicono il punto?

## 7. Citazioni

Nel testo si usa una citazione breve vicino all'affermazione:

```text
[Vaswani et al., 2017, §3.2.1]
[PyTorch Docs, scaled_dot_product_attention, versione X.Y]
[Nome report, revisione, sezione N]
```

Quando esistono pagine stabili si usa la pagina; altrimenti la sezione. Per codice e repository si registra il commit quando il dettaglio dipende dall'implementazione.

La bibliografia del capitolo separa:

1. fonti primarie;
2. documentazione ufficiale;
3. repository e artefatti;
4. standard e documenti istituzionali;
5. letture complementari non usate come prova portante.

## 8. Dati quantitativi

Un numero misurato indica, in misura adeguata:

- modello e checkpoint;
- dataset, benchmark e split;
- metrica;
- harness o implementazione;
- prompt o protocollo;
- hardware;
- dtype;
- batch size e parametri rilevanti;
- data;
- fonte o comando di riproduzione.

Un numero privo di setup non viene presentato come confronto conclusivo.

## 9. Verifica temporale

Ogni capitolo registra:

- data dell'ultima ricerca;
- data dell'ultima verifica delle fonti;
- data di congelamento;
- versioni delle documentazioni;
- revisioni dei paper;
- release o commit rilevanti.

API, standard, leggi, benchmark e prodotti recenti vengono ricontrollati prima dell'approvazione. Il capitolo non dichiara aggiornamento oltre la data di congelamento.

## 10. Divergenze

Quando fonti primarie affidabili differiscono:

- la divergenza viene registrata;
- non viene forzata una sintesi non sostenuta;
- si distingue tra definizione, setup, implementazione e versione;
- le posizioni verificabili vengono presentate separatamente;
- si evita una conclusione se le fonti non la permettono.

Paper, report, documentazione, repository e prodotto non sono intercambiabili.

## 11. Codice per capitolo

Ogni capitolo tecnico include almeno uno snippet eseguibile collegato a una trasformazione centrale.

Il compiler che produce gli esempi deve essere idempotente: eseguire una seconda
ricostruzione sullo stesso artefatto non può aggiungere guard, import, sezioni o
altre righe al codice pubblico. Il controllo canonico è:

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/audit_generator_idempotence.py --strict
```

Il gate confronta il codice versionato con quello che il compiler rigenererebbe
e riapre anche i blocchi Python incorporati nel testo.

Un capitolo non computazionale può non includere codice soltanto quando:

- l'eccezione è motivata;
- nessuno snippet utile può rappresentare correttamente il contenuto;
- l'assenza viene approvata dall'autore.

Non si aggiunge codice decorativo per soddisfare un conteggio.

Ogni capitolo dichiara nei metadati una delle due policy:

```text
code_policy: reference
code_policy: exception
```

`reference` richiede blocco Python nel testo, output letterale, file completo, test e output versionato. `exception` richiede una motivazione concreta, una prova sostitutiva documentale e l'assenza di vecchi script generici che contraddicano la policy. L'eccezione è appropriata quando il codice locale ridurrebbe una tassonomia, una norma o un tema di frontiera a una simulazione non fedele.

## 12. Dimensione e ruolo degli snippet

La forma predefinita è breve e autosufficiente, normalmente da 8 a 40 righe significative. Il limite non è rigido.

Script più lunghi restano nel repository quando servono a:

- riprodurre un esperimento;
- eseguire benchmark;
- addestrare un modello;
- gestire dataset o checkpoint;
- confrontare implementazioni;
- verificare hardware specifico.

Nel capitolo viene mostrata soltanto la porzione necessaria. Il file completo viene referenziato.

Il blocco mostrato nel testo deve essere estratto dal file eseguito oppure controllato automaticamente contro di esso. L'output riportato è una copia letterale dell'artefatto versionato, non una riscrittura editoriale.

## 13. Contratto dello snippet

Ogni snippet registra:

```text
ID:
Sezione:
Domanda:
Input noto:
Shape iniziali:
Operazione centrale:
Output osservabile:
Invariante:
Versione Python:
Versione libreria:
Device:
Dtype:
Seed:
Fonte API:
File completo:
Test associato:
Stato audit:
```

Il contratto completo resta in `code/README.md` e `code/CODE_AUDIT.md`. Nel corpo del manuale viene introdotto in prosa.

## 14. Regole di scrittura del codice

- una operazione principale per snippet;
- variabili coerenti con prosa e formule;
- shape visibili in commenti o asserzioni;
- nessuna dipendenza da celle precedenti;
- import completi e minimi;
- commenti in italiano, nomi API ufficiali;
- nessun output inventato;
- firma e comportamento API controllati sulla documentazione;
- pseudocodice distinto dal codice eseguibile;
- nessun comportamento hardware-specifico dichiarato verificato senza esecuzione.

## 15. Ambiente

Gli snippet didattici devono essere CPU-compatible quando il meccanismo non richiede una GPU.

Codice per CUDA, acceleratori, mixed precision, kernel fused o distributed training viene separato e accompagnato dall'ambiente necessario.

Ogni esecuzione registra almeno:

- sistema operativo o container;
- Python;
- libreria;
- device;
- dtype;
- seed;
- comando;
- data;
- output o proprietà verificate.

## 16. Tipi di snippet

### 16.1 Esplicativo minimo

Mostra l'operazione centrale con input piccoli.

### 16.2 Verifica

Controlla formula, shape, normalizzazione, mask, gradiente o altro invariante.

### 16.3 Implementazione da zero

Usa operazioni primitive dopo che l'algoritmo è stato stabilizzato.

### 16.4 API ufficiale

Mostra l'equivalente tramite una API verificata e, quando valido, confronta il risultato con l'implementazione diretta.

### 16.5 Benchmark

Misura tempo, memoria o throughput con warm-up, sincronizzazione, hardware, dtype, batch, shape e protocollo dichiarati.

## 17. Struttura della cartella `code/`

```text
chapters/<capitolo>/code/
  README.md
  CODE_AUDIT.md
  <snippet>.py
  <test>.py
  outputs/
  environments/
```

`README.md` descrive ambiente, installazione, comandi e mappa degli snippet.

`CODE_AUDIT.md` registra API, ambiente, comando, output, test, confronto indipendente, problemi e stato.

`outputs/` contiene output letterali. `environments/` contiene configurazione e versioni.

## 18. Ciclo di verifica del codice

1. controllare la documentazione ufficiale e la firma API;
2. ispezionare import, shape, broadcasting, dtype, device, mask, gradienti e casualità;
3. eseguire in un processo pulito;
4. testare gli invarianti;
5. confrontare con formula diretta, NumPy o API ufficiale quando possibile;
6. verificare la corrispondenza con la prosa;
7. rieseguire dopo ogni modifica.

## 19. Output

Un output può essere:

- `Eseguito`, quando deriva da file, ambiente, comando e test registrati;
- `Illustrativo`, quando mostra soltanto formato o meccanismo.

Un output non viene chiamato `Eseguito` senza log o test.

## 20. API e versioni

Per ogni API si registrano:

- nome completo;
- firma verificata;
- versione della libreria;
- pagina ufficiale;
- note di release rilevanti;
- differenze tra CPU, CUDA e backend, quando pertinenti.

Nessuna firma viene scritta dalla memoria.

La versione documentata e quella realmente eseguita restano distinte.

## 21. Controllo incrociato

Testo, formule, visuali e codice coincidono per:

- nomi;
- shape;
- numeri;
- ordine delle operazioni;
- mask;
- parametri;
- output;
- invarianti;
- confini.

Una contraddizione riapre gli audit coinvolti.

## 22. Gate di approvazione

Un capitolo non può essere approvato finché:

- tutti i claim portanti hanno prova;
- le citazioni sono state aperte nel contesto originale;
- i dettagli recenti sono stati ricontrollati;
- i numeri hanno provenienza completa;
- le divergenze sono registrate;
- non restano inferenze fattuali;
- codice e API sono verificati;
- test e output sono registrati;
- bibliografia, claim, testo, visuali e codice coincidono.
