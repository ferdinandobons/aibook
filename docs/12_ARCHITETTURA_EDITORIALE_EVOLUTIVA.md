# Architettura editoriale evolutiva

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ultima ricerca approfondita che ha informato questa struttura: 30 luglio 2026
- Documento collegato: `../GUIDELINE.md`
- Indice operativo: `10_INDICE_EDITORIALE.md`
- Catalogo dello stato dell'arte: `14_CATALOGO_STATO_ARTE.md`

## Scopo

Questo documento definisce una struttura del libro che possa accogliere nuove architetture, tecniche di training, metodi di inference, sistemi agentici e altri sviluppi senza rinominare o riordinare continuamente le parti principali.

La struttura è basata sulle domande e sui livelli funzionali di un sistema di AI, non sui nomi dei prodotti, sulle mode del momento o su una specifica generazione di modelli.

## Un'unica opera canonica

Il repository contiene una sola opera canonica e continua.

L'opera può essere esportata:

- come volume unico;
- come due o più tomi editoriali;
- come sito o corso modulare;
- come selezione di percorsi didattici.

La suddivisione tipografica non modifica la struttura canonica. I tomi sono viste di pubblicazione, non fonti di verità indipendenti.

## Parti stabili

Le parti hanno un ID e un nome canonico. Il loro ordine e il loro significato sono progettati per restare stabili anche quando vengono aggiunti nuovi capitoli.

| ID | Nome canonico | Domanda stabile |
|---|---|---|
| `P01` | Campo, metodo e storia dell'AI | Che cosa viene chiamato AI, come si è sviluppato il campo e come si valuta una conoscenza tecnica? |
| `P02` | Matematica, informazione e calcolo | Quali quantità, strutture e vincoli computazionali servono per descrivere e implementare i modelli? |
| `P03` | Apprendimento, ottimizzazione e decisione | Come si definiscono obiettivi, segnali di apprendimento, update e decisioni? |
| `P04` | Reti neurali e rappresentazioni | Come vengono costruite e addestrate rappresentazioni neurali riutilizzabili? |
| `P05` | Modellazione generativa | Come si modellano e si campionano distribuzioni di dati? |
| `P06` | Sequenze, linguaggio e contesto | Come vengono rappresentate e trasformate sequenze, testo e dipendenze contestuali? |
| `P07` | Dati, pretraining e scaling | Come vengono costruiti dati, ricette e sistemi di pretraining su larga scala? |
| `P08` | Progettazione delle architetture | Quali operatori, blocchi, memorie, routing e pattern di calcolo definiscono l'architettura interna di un modello? |
| `P09` | Adattamento, allineamento e ragionamento | Come si modificano capacità e comportamento dopo il pretraining e come si usa compute aggiuntivo per il reasoning? |
| `P10` | Multimodalità e modelli del mondo | Come si rappresentano, comprendono e generano modalità diverse e come si modellano ambienti e dinamiche? |
| `P11` | Conoscenza esterna, memoria e azione | Come un modello recupera conoscenza, conserva stato, usa strumenti e agisce in ambienti? |
| `P12` | Efficienza, inference e sistemi | Come si riducono costo, memoria e latenza e come si addestrano, servono e operano i modelli? |
| `P13` | Valutazione, interpretabilità, sicurezza e governance | Come si misurano, comprendono, proteggono e governano modelli e sistemi? |
| `P14` | Laboratori, integrazione e osservatorio | Come si ricostruiscono sistemi completi, si replicano risultati e si monitora la frontiera? |

## Regola di immutabilità delle parti

Una nuova tecnica non causa la creazione o la rinomina di una parte quando può essere collocata in una domanda stabile già esistente.

L'ID e il nome di una parte possono cambiare soltanto quando:

1. il significato corrente non riesce più a contenere un'intera classe di problemi rilevanti;
2. almeno due revisioni approfondite indipendenti documentano il problema;
3. viene preparata una mappa di migrazione per tutti i capitoli e i riferimenti;
4. la modifica viene registrata in `08_REGISTRO_DECISIONI.md`;
5. il committente approva esplicitamente la modifica.

Una nuova moda, un nuovo modello o un nuovo paper non soddisfano da soli questi criteri.

## Collocazione primaria dei contenuti

Ogni tecnica ha una sola collocazione primaria. I collegamenti con altre parti vengono espressi tramite riferimenti, non duplicando la spiegazione portante.

### Algoritmo di routing

1. Identificare il problema principale risolto dalla tecnica.
2. Identificare il punto del ciclo di vita del modello in cui interviene.
3. Individuare quale oggetto cambia realmente: dati, obiettivo, blocco interno, memoria, decoding, runtime, valutazione o governance.
4. Assegnare la tecnica alla parte che possiede quell'oggetto.
5. Registrare i collegamenti secondari come tag e cross-reference.

### Matrice rapida

| La novità modifica principalmente... | Parte primaria |
|---|---|
| definizioni, storia o metodo scientifico | `P01` |
| formalismo, probabilità, informazione, numerica o hardware di base | `P02` |
| obiettivo di apprendimento, ottimizzatore, RL o decisione | `P03` |
| layer neurali generali o representation learning | `P04` |
| fattorizzazione generativa, latent variable, diffusion, flow o sampling di base | `P05` |
| tokenizzazione, embedding, sequence modeling o attention di base | `P06` |
| dataset, mixture, curriculum, synthetic data, scaling o pretraining | `P07` |
| blocco interno, attention variant, recurrence, SSM, MoE, routing o memoria parametrica | `P08` |
| fine-tuning, preference optimization, RL post-training, reasoning o test-time compute | `P09` |
| visione, audio, video, 3D, sensori, world model o embodied AI | `P10` |
| retrieval, RAG, memoria esterna, tool, protocollo agentico o azione | `P11` |
| quantizzazione, pruning, decoding, cache, kernel, compiler, serving o LLMOps | `P12` |
| benchmark, interpretabilità, sicurezza, privacy, diritto o governance | `P13` |
| laboratorio, replica, case study trasversale o osservatorio | `P14` |

## Una tecnica non viene collocata in base al nome del modello

Un modello non ottiene automaticamente un capitolo.

Un modello viene trattato come:

- studio di caso, quando combina tecniche già spiegate;
- fonte primaria per una nuova tecnica, quando documenta un meccanismo distinto;
- candidato a capitolo soltanto quando il contributo possiede un contratto didattico autonomo e duraturo.

Esempio editoriale: un modello che combina MoE, linear attention e multimodalità viene referenziato nelle sezioni pertinenti. Non viene creato un capitolo che duplica tutte e tre le spiegazioni.

## Livelli di maturità

La maturità è un attributo del contenuto. Non determina la parte e non modifica la sua collocazione primaria.

### `CORE`

Contenuto necessario per comprendere il campo o numerosi sviluppi successivi.

Criteri tipici:

- definizione stabile;
- rilevanza trasversale;
- ampia evidenza o uso consolidato;
- valore didattico durevole;
- dipendenza esplicita di altri capitoli.

### `ESTABLISHED`

Contenuto verificato e rilevante, adottato o riprodotto in più contesti, ma non ancora requisito universale oppure ancora soggetto a evoluzione significativa.

Criteri tipici:

- almeno una fonte primaria solida;
- implementazione o documentazione verificabile;
- evidenza oltre un singolo esempio promozionale;
- terminologia sufficientemente stabile;
- trade-off noti e documentabili.

### `FRONTIER`

Contenuto recente, sperimentale, con terminologia instabile, evidenza ancora limitata o dipendenza forte da uno specifico setup.

Un contenuto `FRONTIER` deve riportare:

- data dell'ultima verifica;
- fonti primarie;
- limiti dell'evidenza;
- differenze tra proposta, implementazione e risultati riprodotti;
- condizioni richieste per una futura promozione.

## Promozione e revisione della maturità

Il passaggio di maturità non sposta la tecnica in un'altra parte.

Percorso ordinario:

```text
FRONTIER -> ESTABLISHED -> CORE
```

È ammesso un passaggio diretto soltanto con motivazione documentata.

### Da `FRONTIER` a `ESTABLISHED`

Richiede normalmente:

- più di una fonte o valutazione indipendente;
- implementazione disponibile o descrizione riproducibile;
- risultati non limitati a un unico benchmark favorevole;
- definizione del meccanismo e dei failure mode;
- utilità dimostrata oltre un solo prodotto.

### Da `ESTABLISHED` a `CORE`

Richiede normalmente:

- utilità durevole attraverso più generazioni di sistemi;
- ruolo di prerequisito o meccanismo generale;
- convergenza terminologica;
- letteratura e implementazioni sufficienti per una spiegazione stabile;
- ridotto rischio che il capitolo diventi una cronaca di prodotto.

### Demozione

Un contenuto può essere demansionato quando:

- risultati centrali non sono riproducibili;
- l'uso si rivela molto più ristretto di quanto inizialmente documentato;
- la terminologia viene sostituita da una tassonomia più precisa;
- nuove evidenze cambiano in modo sostanziale il meccanismo descritto.

La demozione non cancella la storia. Il contenuto viene mantenuto con stato aggiornato e motivazione.

## Identità stabile dei capitoli

Il numero visualizzato di un capitolo non è la sua identità.

Ogni capitolo possiede:

- `chapter_id` immutabile;
- `part_id`;
- `order_key`;
- titolo;
- slug;
- maturità;
- stato editoriale;
- prerequisiti;
- successori;
- alias storici.

Formato consigliato:

```text
CH-P08-LINEAR-ATTENTION
CH-P09-RLVR
CH-P12-SPECULATIVE-DECODING
```

Il numero stampato è specifico dell'edizione. I riferimenti interni e i nomi dei file usano l'ID stabile.

## Ordine dei capitoli

L'ordine all'interno di una parte è determinato da:

1. prerequisiti;
2. caso base prima delle varianti;
3. operazione indipendente dalla libreria prima dell'implementazione;
4. architettura prima dell'ottimizzazione hardware che la presuppone;
5. meccanismo prima degli studi di caso;
6. evidenza stabile prima delle sezioni frontier.

L'età di una tecnica e il nome del prodotto non determinano l'ordine.

## Inserimento senza rinumerazione distruttiva

Per inserire un nuovo capitolo:

1. assegnare un `chapter_id` semantico;
2. scegliere il `part_id` con l'algoritmo di routing;
3. assegnare un `order_key` tra i prerequisiti e i consumer;
4. non rinominare gli ID esistenti;
5. aggiornare il numero visualizzato soltanto durante una nuova edizione;
6. mantenere alias e redirect per riferimenti storici.

## Split e merge

### Split

Quando un capitolo viene diviso:

- il capitolo originale resta come alias o pagina di transizione;
- i nuovi capitoli ricevono nuovi ID;
- la mappa di dipendenze viene aggiornata;
- le fonti e i claim vengono ripartiti senza duplicazioni invisibili.

### Merge

Quando due capitoli vengono uniti:

- uno degli ID diventa canonico;
- gli altri restano alias storici;
- il registro delle decisioni documenta la motivazione;
- i riferimenti interni vengono verificati.

## Frontiera distribuita, non contenitore finale

Le tecniche frontier restano nella loro parte funzionale. `P14` conserva soltanto:

- il registro sintetico delle aree da monitorare;
- confronti trasversali;
- domande aperte;
- piani di replica;
- cronologia delle promozioni e demozioni.

Questa regola evita di dover spostare un intero capitolo quando una tecnica frontier diventa established o core.

## Compatibilità con la struttura precedente

La precedente separazione obbligatoria in due volumi è sostituita.

Le parti precedenti vengono mappate sulle parti stabili senza perdere contenuto. Gli eventuali export in due tomi possono continuare a usare un punto di taglio editoriale, ma quel punto non appartiene alla struttura logica del repository.

Il Capitolo 28, **Il meccanismo di attention**, mantiene il proprio riferimento editoriale corrente durante il progetto pilota e riceve l'ID stabile `CH-P06-ATTENTION`.

## Verifica periodica

La struttura viene riesaminata:

- prima di ogni nuova edizione;
- dopo una ricerca approfondita dello stato dell'arte;
- quando almeno cinque nuovi candidati non trovano una collocazione non ambigua;
- quando una parte accumula sottosezioni con oggetti incompatibili;
- quando il committente richiede una revisione architetturale.

La verifica deve concludersi preferibilmente con l'aggiunta di capitoli o sottocapitoli, non con la modifica delle parti.