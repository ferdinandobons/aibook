# Governance e architettura editoriale

## Stato

- Stato: `vincolante`
- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Lingua: italiano
- Formato sorgente: Markdown
- Opera canonica: unica e continua
- Modalità di produzione: seriale e controllata
- Capitolo pilota: `CH-P06-ATTENTION`
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Entry point operativo: `../GUIDELINE.md`

## 1. Scopo del progetto

Il repository contiene il manuale tecnico **Intelligenza artificiale generativa**, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi di produzione, alla valutazione e alla sicurezza.

Il libro non è organizzato come una cronologia di prodotti. Le parti e i capitoli seguono problemi, meccanismi e contratti tecnici. I singoli modelli vengono usati come studi di caso quando permettono di osservare una tecnica già definita oppure documentano un contributo autonomo.

Ogni capitolo tecnico integra, quando pertinente:

1. testo verificato e scritto come manuale;
2. formule, tabelle ed esempi controllati;
3. immagini tecniche sottoposte ad audit iterativo;
4. codice eseguito e testato;
5. fonti, claim e registri di review.

## 2. Forma dell'opera

Esiste una sola sorgente canonica. La stessa opera può essere esportata come:

- volume unico;
- due o più tomi;
- sito o knowledge base;
- corso modulare;
- percorso didattico selettivo.

L'export non modifica l'identità, l'ordine concettuale o la fonte di verità dei contenuti.

## 3. Lettore e profondità

Il livello principale è intermedio tecnico. Gli approfondimenti avanzati entrano ogni volta che sono necessari per spiegare correttamente:

- matematica e derivazioni;
- shape e contratti tensoriali;
- stabilità numerica;
- complessità computazionale;
- memoria e data movement;
- implementazione;
- training distribuito;
- inference e serving;
- hardware, compiler e kernel;
- trade-off tra qualità, latenza, memoria, costo ed energia.

Il caso base viene stabilizzato prima delle varianti avanzate. La semplificazione non può cambiare il meccanismo.

## 4. Parti stabili

Le quattordici parti hanno ID, nome e domanda canonica. La loro funzione è progettata per restare stabile quando compaiono nuove tecniche.

| ID | Parte canonica | Domanda stabile |
|---|---|---|
| `P01` | Campo, metodo e storia dell'AI | Che cosa viene chiamato AI, come si è sviluppato il campo e come si valuta una conoscenza tecnica? |
| `P02` | Matematica, informazione e calcolo | Quali quantità, strutture e vincoli computazionali servono per descrivere e implementare i modelli? |
| `P03` | Apprendimento, ottimizzazione e decisione | Come si definiscono obiettivi, segnali di apprendimento, update e decisioni? |
| `P04` | Reti neurali e rappresentazioni | Come vengono costruite e addestrate rappresentazioni neurali riutilizzabili? |
| `P05` | Modellazione generativa | Come si modellano e si campionano distribuzioni di dati? |
| `P06` | Sequenze, linguaggio e contesto | Come vengono rappresentate e trasformate sequenze, testo e dipendenze contestuali? |
| `P07` | Dati, pretraining e scaling | Come vengono costruiti dati, ricette e sistemi di pretraining su larga scala? |
| `P08` | Progettazione delle architetture | Quali operatori, blocchi, memorie, routing e pattern di calcolo definiscono l'architettura interna? |
| `P09` | Adattamento, allineamento e ragionamento | Come si modificano capacità e comportamento dopo il pretraining e come si usa compute aggiuntivo per il reasoning? |
| `P10` | Multimodalità e modelli del mondo | Come si rappresentano, comprendono e generano modalità diverse e come si modellano ambienti e dinamiche? |
| `P11` | Conoscenza esterna, memoria e azione | Come un modello recupera conoscenza, conserva stato, usa strumenti e agisce in ambienti? |
| `P12` | Efficienza, inference e sistemi | Come si riducono costo, memoria e latenza e come si addestrano, servono e operano i modelli? |
| `P13` | Valutazione, interpretabilità, sicurezza e governance | Come si misurano, comprendono, proteggono e governano modelli e sistemi? |
| `P14` | Laboratori, integrazione e osservatorio | Come si ricostruiscono sistemi completi, si replicano risultati e si monitora la frontiera? |

### 4.1 Immutabilità delle parti

Una nuova tecnica non causa la creazione o la rinomina di una parte quando può essere collocata in una domanda esistente.

ID, nome o ordine di una parte possono cambiare soltanto quando:

1. il significato corrente non contiene più un'intera classe di problemi rilevanti;
2. almeno due revisioni approfondite indipendenti documentano il problema;
3. viene preparata una mappa di migrazione per capitoli, ID e riferimenti;
4. la modifica viene registrata in questo documento e nel registro delle decisioni;
5. il committente la approva esplicitamente.

Una nuova moda, un singolo modello o un singolo paper non soddisfano da soli questi criteri.

## 5. Routing funzionale

Ogni tecnica ha una collocazione primaria. I collegamenti secondari vengono mantenuti con riferimenti, senza duplicare la spiegazione portante.

### 5.1 Algoritmo

1. Descrivere il problema principale risolto.
2. Identificare il punto del ciclo di vita in cui la tecnica interviene.
3. Individuare l'oggetto che cambia: dati, obiettivo, blocco interno, memoria, decoding, runtime, valutazione o governance.
4. Assegnare la tecnica alla parte proprietaria dell'oggetto.
5. Registrare tag e riferimenti secondari.

### 5.2 Matrice rapida

| Oggetto modificato principalmente | Parte primaria |
|---|---|
| definizioni, storia o metodo scientifico | `P01` |
| formalismo, probabilità, informazione, numerica o hardware di base | `P02` |
| obiettivo di apprendimento, ottimizzatore, RL o decisione | `P03` |
| layer neurali generali o representation learning | `P04` |
| fattorizzazione generativa, variabili latenti, diffusion, flow o sampling di base | `P05` |
| tokenizzazione, embedding, sequence modeling o attention di base | `P06` |
| dataset, mixture, curriculum, synthetic data, scaling o pretraining | `P07` |
| blocco interno, attention variant, recurrence, SSM, MoE, routing o memoria parametrica | `P08` |
| fine-tuning, preference optimization, RL post-training, reasoning o test-time compute | `P09` |
| visione, audio, video, 3D, sensori, world model o embodied AI | `P10` |
| retrieval, RAG, memoria esterna, tool, protocollo agentico o azione | `P11` |
| quantizzazione, pruning, decoding, cache, kernel, compiler, serving o LLMOps | `P12` |
| benchmark, interpretabilità, sicurezza, privacy, diritto o governance | `P13` |
| laboratorio, replica, case study trasversale o osservatorio | `P14` |

## 6. Modelli e studi di caso

Un modello non ottiene automaticamente un capitolo. Può essere:

- uno studio di caso, quando combina tecniche già spiegate;
- una fonte primaria, quando documenta un meccanismo distinto;
- un candidato a capitolo, soltanto quando il contributo possiede una domanda didattica autonoma, fonti sufficienti e un contratto durevole.

Un modello che combina MoE, linear attention e multimodalità viene collegato alle sezioni pertinenti. Non viene creato un capitolo che duplica tutte le spiegazioni.

## 7. Maturità dei contenuti

La maturità è un attributo editoriale. Non determina la collocazione.

### `CORE`

Concetto durevole, trasversale e necessario per numerosi sviluppi successivi.

Criteri tipici:

- definizione stabile;
- rilevanza trasversale;
- ampia evidenza o uso consolidato;
- valore didattico durevole;
- dipendenza esplicita di altri capitoli.

### `ESTABLISHED`

Concetto verificato e rilevante, adottato o riprodotto in più contesti, ma non universale oppure ancora in evoluzione significativa.

Criteri tipici:

- fonte primaria solida;
- implementazione o documentazione verificabile;
- evidenza oltre un unico esempio promozionale;
- terminologia sufficientemente stabile;
- trade-off documentabili.

### `FRONTIER`

Concetto recente o sperimentale, con terminologia instabile, evidenza limitata o forte dipendenza da uno specifico setup.

Una voce `FRONTIER` registra:

- data dell'ultima verifica;
- fonti primarie;
- limiti dell'evidenza;
- differenze tra proposta, implementazione e risultati riprodotti;
- condizioni per la promozione.

### 7.1 Cambi di maturità

Percorso ordinario:

```text
FRONTIER -> ESTABLISHED -> CORE
```

La promozione richiede nuove prove, non soltanto il trascorrere del tempo. Il cambio di maturità non modifica automaticamente parte, ID o ordine.

Una demozione è ammessa quando risultati centrali non sono riproducibili, l'uso si rivela più ristretto, la terminologia viene sostituita o nuove evidenze cambiano il meccanismo descritto. La storia resta nel registro.

## 8. Identità dei capitoli

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

Esempi:

```text
CH-P08-LINEAR-ATTENTION
CH-P09-RLVR
CH-P12-SPECULATIVE-DECODING
```

`chapter_id` resta stabile. Il numero visualizzato può cambiare tra edizioni.

### 8.1 Ordine

L'ordine dentro una parte dipende da:

1. prerequisiti;
2. caso base prima delle varianti;
3. operazione indipendente dalla libreria prima dell'implementazione;
4. architettura prima dell'ottimizzazione hardware;
5. meccanismo prima degli studi di caso;
6. evidenza stabile prima della frontiera.

### 8.2 Inserimento

Per inserire un capitolo:

1. assegnare un ID semantico;
2. scegliere la parte con il routing;
3. assegnare un `order_key` tra prerequisiti e consumer;
4. non rinominare ID esistenti;
5. aggiornare il numero visualizzato soltanto in una nuova edizione;
6. mantenere alias e redirect.

### 8.3 Split e merge

Uno split crea nuovi ID e conserva l'ID precedente come alias o pagina di transizione. Fonti, claim, visuali, codice e dipendenze vengono ripartiti esplicitamente.

Un merge sceglie un ID canonico, mantiene gli altri come alias e aggiorna tutti i riferimenti.

## 9. Frontiera distribuita

Le tecniche `FRONTIER` restano nella parte funzionale pertinente. `P14` contiene soltanto:

- osservatorio sintetico;
- confronti trasversali;
- domande aperte;
- piani di replica;
- cronologia di promozioni e demozioni.

`P14` non è un contenitore generico per tutto ciò che è recente.

## 10. Accuratezza e artefatti obbligatori

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.

Ogni informazione portante richiede almeno una prova tra:

- paper originale o atti ufficiali;
- technical report ufficiale;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita;
- risultato riprodotto con ambiente, comando, output e test.

Ogni capitolo contiene:

- `FONTI_PRIMARIE.md`;
- `CLAIMS.md`;
- `TEXT_AUDIT.md`;
- codice e audit, quando pertinente;
- visuali e audit, quando pertinenti.

## 11. Produzione seriale

Il lavoro procede un capitolo completo alla volta. Non si apre il successivo finché quello corrente non è:

- approvato e congelato;
- oppure formalmente sospeso con problemi documentati.

Il workflow completo è in `06_WORKFLOW_E_REPOSITORY.md`.

## 12. Aggiornamenti e governance

Gli aggiornamenti seguono le operazioni U1-U8 descritte in `06_WORKFLOW_E_REPOSITORY.md`:

- U1 nuova tecnica;
- U2 nuova evidenza;
- U3 aggiornamento API o implementazione;
- U4 cambio di maturità;
- U5 nuovo capitolo;
- U6 split o merge;
- U7 correzione tecnica;
- U8 nuova edizione.

Ogni modifica coordinata può coinvolgere catalogo, collocazione, fonti, claim, testo, formule, codice, visuali, audit, indice e decisioni.

## 13. Registro consolidato delle decisioni

La tabella seguente sostituisce il precedente registro distribuito. Le decisioni sono vincolanti salvo indicazione diversa.

### 13.1 Editoriale e metodo

| ID | Stato | Decisione |
|---|---|---|
| `DEC-001` | vincolante | Tutti i progressi vengono registrati in `ferdinandobons/aibook`; branch canonico `main`. |
| `DEC-002` | vincolante | Il formato sorgente è Markdown. |
| `DEC-003` | vincolante | Il libro è in italiano; i termini tecnici standard restano in inglese quando appropriato. |
| `DEC-004` | sostituita | La struttura canonica in due volumi è sostituita dall'opera unica. |
| `DEC-005` | vincolante | Produzione seriale controllata, un capitolo alla volta. |
| `DEC-006` | pilota approvato | `CH-P06-ATTENTION` è il capitolo pilota. |
| `DEC-007` | vincolante | Livello intermedio tecnico con approfondimenti avanzati quando necessari. |
| `DEC-008` | vincolante | Approccio didactic-first ancorato a fonti primarie; nessuna semplificazione falsa. |
| `DEC-009` | vincolante | Ogni capitolo mantiene un oggetto concreto dall'apertura alla ricostruzione. |
| `DEC-010` | vincolante | `LEARN_GOVERNANCE.md` non è una dipendenza; tutte le regole sono nel repository. |

### 13.2 Accuratezza e fonti

| ID | Stato | Decisione |
|---|---|---|
| `DEC-011` | vincolante | Ogni informazione portante richiede fonte, standard, derivazione o prova riproducibile. |
| `DEC-012` | vincolante | Le inferenze fattuali editoriali sono escluse dalla versione approvata. |
| `DEC-013` | vincolante | I contenuti recenti vengono ricontrollati; ogni capitolo registra verifica e congelamento. |
| `DEC-014` | vincolante | Priorità a paper originali, atti, report, documentazione, repository ufficiali e standard. |
| `DEC-015` | vincolante | Citazione breve vicino all'affermazione e dossier completo nel capitolo. |
| `DEC-016` | vincolante | Audit fattuale, matematico, algoritmico, temporale, incrociato, didattico ed editoriale. |
| `DEC-017` | vincolante | Ogni capitolo usa `CLAIMS.md` con ID stabili e prova delle affermazioni. |

### 13.3 Visuali

| ID | Stato | Decisione |
|---|---|---|
| `DEC-018` | vincolante | Le immagini tecniche vengono create con lo strumento immagini; SVG non principale. |
| `DEC-019` | vincolante | La prima generazione non è finale. |
| `DEC-020` | vincolante | Ogni figura viene revisionata e rigenerata finché non restano difetti bloccanti. |
| `DEC-021` | vincolante | Ogni figura risponde a una domanda ed è parte della spiegazione. |
| `DEC-022` | vincolante | Stile originale, pulito, leggibile; significato non affidato al solo colore. |
| `DEC-023` | vincolante | Nessun numero rigido di immagini per capitolo. |
| `DEC-024` | vincolante | PNG ad alta risoluzione, alt text, equivalente testuale e audit. |
| `DEC-045` | vincolante | Overflow, clipping, sovrapposizioni e padding insufficiente sono bloccanti. |

### 13.4 Codice

| ID | Stato | Decisione |
|---|---|---|
| `DEC-025` | vincolante | Ogni capitolo tecnico include uno snippet eseguibile, salvo eccezione motivata. |
| `DEC-026` | vincolante | Python e PyTorch principali; NumPy ammesso per controlli indipendenti. |
| `DEC-027` | vincolante | Snippet brevi e autosufficienti; script lunghi soltanto quando necessari. |
| `DEC-028` | vincolante | Ogni snippet viene verificato, eseguito in processo pulito e testato. |
| `DEC-029` | vincolante | Un output è `Eseguito` soltanto quando deriva dall'ambiente e dal comando registrati. |

### 13.5 Workflow

| ID | Stato | Decisione |
|---|---|---|
| `DEC-030` | vincolante | Testo, formule, immagini e codice condividono label, shape, numeri, ordine e confini. |
| `DEC-031` | vincolante | Ogni capitolo viene sottoposto alla revisione del committente dopo i gate tecnici. |
| `DEC-032` | vincolante | La versione approvata è associata a data e commit SHA. |
| `DEC-033` | vincolante | Un capitolo non entra in produzione senza documentazione e autorizzazione coerenti. |
| `DEC-046` | vincolante | Un difetto didattico richiede correzione e nuova review integrale. |
| `DEC-047` | vincolante | Lo scaffold resta interno; il capitolo usa prosa naturale e gate anti-template. |
| `DEC-048` | vincolante | Ogni capitolo supera review editoriale, linguistica, lettura ad alta voce e tre profili di lettore. |

### 13.6 Architettura evolutiva

| ID | Stato | Decisione |
|---|---|---|
| `DEC-034` | vincolante | Una sola opera canonica; tomi, sito e corso sono export. |
| `DEC-035` | vincolante | ID, nomi e ordine di `P01`-`P14` sono stabili. |
| `DEC-036` | vincolante | Routing in base al problema risolto e all'oggetto modificato. |
| `DEC-037` | vincolante | Maturità `CORE`, `ESTABLISHED`, `FRONTIER` separata dalla collocazione. |
| `DEC-038` | vincolante | Capitoli identificati da ID semantici, non dal numero stampato. |
| `DEC-039` | vincolante | Le voci frontier restano nella parte funzionale pertinente. |
| `DEC-040` | vincolante | Il catalogo censisce le principali famiglie senza dichiarare completezza assoluta. |
| `DEC-041` | vincolante | `GUIDELINE.md` è l'entry point per sistemi senza contesto. |
| `DEC-042` | vincolante | Gli aggiornamenti seguono le procedure U1-U8. |
| `DEC-043` | vincolante | La ricerca globale è registrata e le voci frontier vengono ricontrollate. |
| `DEC-044` | pianificazione corrente | L'indice di lavoro contiene 98 capitoli con ID semantici. |

### 13.7 Decisioni sostituite

| ID | Sostituita da | Nota |
|---|---|---|
| `DEC-S01` | `DEC-018` | Uso prioritario di SVG abbandonato. |
| `DEC-S02` | `DEC-010` | Dipendenza da `LEARN_GOVERNANCE.md` rimossa. |
| `DEC-S03` | `DEC-012` | Inferenze fattuali non ammesse neppure se etichettate nel testo approvato. |
| `DEC-S04` | `DEC-034` | Due volumi non più struttura canonica. |
| `DEC-S05` | `DEC-047` | Blocco atomico non pubblicato come telaio standard. |
| `DEC-S06` | `DEC-048` | Correttezza didattica non sufficiente senza qualità editoriale e linguistica. |

## 14. Propagazione delle decisioni

Quando una decisione cambia:

1. aggiornare questo documento;
2. aggiornare i documenti specialistici coinvolti;
3. aggiornare indice e catalogo quando necessario;
4. controllare i riferimenti incrociati;
5. aggiornare l'audit documentale nel `README.md` di `docs/`;
6. registrare il commit.

Un conflitto non risolto blocca il lavoro interessato.

## 15. Gate di completezza documentale

La documentazione è coerente quando un sistema senza contesto può:

- comprendere scopo e struttura del libro;
- collocare una nuova tecnica;
- aggiornare maturità, indice e catalogo;
- applicare fonti, claim, codice e visuali;
- produrre prosa da manuale senza esporre lo scaffold;
- ripetere le review fino alla rimozione dei difetti bloccanti;
- ricostruire ogni versione approvata da commit e artefatti.

La verifica corrente è registrata nel `README.md` di `docs/` e nello storico Git.
