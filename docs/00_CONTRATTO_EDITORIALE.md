# Contratto editoriale del libro

## Titolo di lavoro

**Intelligenza artificiale generativa**  
*Dai fondamenti matematici ai modelli multimodali, al reasoning, agli agenti e ai sistemi di produzione*

## Stato del progetto

- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Lingua: italiano
- Formato sorgente: Markdown
- Modalità: produzione seriale controllata
- Opera canonica: unica e continua
- Export: volume unico, più tomi, sito o corso
- Capitolo pilota: `CH-P06-ATTENTION`, visualizzato come Capitolo 28 nell'edizione di lavoro
- Visuali: immagini raster generate con lo strumento immagini
- Codice principale: Python e PyTorch
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Entry point operativo: `../GUIDELINE.md`

## 1. Obiettivo editoriale

Il libro costruisce modelli mentali eseguibili. Alla fine di ogni meccanismo il lettore deve poter:

1. ricostruire l'input;
2. descrivere la trasformazione nell'ordine reale;
3. indicare output e shape;
4. dire cosa è cambiato;
5. dire cosa è rimasto invariato;
6. localizzare il componente;
7. dire cosa non fa;
8. prevedere una variazione controllata;
9. collegare la spiegazione a una visuale e a codice verificato.

Il libro non è una rassegna di nomi. Ogni capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale.

## 2. Architettura dell'opera

L'opera canonica è unica. La suddivisione in tomi è una scelta di pubblicazione e non modifica la sorgente.

Le parti stabili sono:

| ID | Nome |
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

ID, nome e ordine delle parti sono stabili. Le regole complete sono in `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`.

Una nuova tecnica viene collocata in base al problema risolto e all'oggetto modificato. Il nome di un modello, la data o la popolarità non determinano da soli la struttura.

## 3. Identità dei capitoli

Ogni capitolo ha:

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

`chapter_id` è stabile. Il numero visualizzato è specifico dell'edizione e può cambiare prima del congelamento.

L'indice dell'edizione di lavoro è in `10_INDICE_EDITORIALE.md`.

## 4. Maturità dei contenuti

- `CORE`: concetto durevole e necessario per numerosi sviluppi successivi.
- `ESTABLISHED`: concetto verificato e rilevante, ma ancora in evoluzione oppure non universale.
- `FRONTIER`: concetto recente, sperimentale o con evidenza ancora limitata.

La maturità non determina la collocazione. Una promozione non sposta automaticamente la tecnica.

Il catalogo corrente è in `14_CATALOGO_STATO_ARTE.md`. Le procedure di aggiornamento sono in `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

## 5. Lettore target e profondità

Il livello principale è intermedio tecnico. Gli approfondimenti avanzati entrano ogni volta che servono per spiegare correttamente:

- matematica e derivazioni;
- shape e contratti tensoriali;
- stabilità numerica;
- complessità computazionale;
- memoria e data movement;
- implementazione PyTorch;
- distributed training;
- inference e serving;
- hardware, compiler e kernel;
- trade-off tra qualità, latenza, memoria, costo ed energia.

Gli approfondimenti avanzati non sono decorativi e non sono confinati a rare appendici. Entrano dopo la stabilizzazione del caso base.

## 6. Metodo di spiegazione

Il metodo vincolante è `EXPLANATION_STYLE_AND_VISUALS.md`.

Ogni transizione importante usa:

```text
Dove siamo:
Problema:
Input e shape:
Trasformazione:
Output e shape:
Cosa è cambiato:
Cosa è rimasto invariato:
Cosa non fa:
Cosa usa l'output dopo:
Esempio minimo:
Errore comune:
Frase di continuità:
```

Ordine di ammissione:

```text
domanda in linguaggio naturale
-> esempio numerico
-> tabella o shape
-> pseudocodice
-> formula
-> derivazione
-> implementazione verificata
-> varianti e ottimizzazioni
```

Vincoli:

- italiano diretto, calmo e progressivo;
- termini tecnici standard in inglese quando appropriato;
- nessuna metafora o personificazione;
- nessun em dash;
- una trasformazione principale per paragrafo;
- referenti espliciti;
- nessuna semplificazione che cambi il meccanismo;
- nessun fatto introdotto per inferenza editoriale.

## 7. Accuratezza

### 7.1 Principio

Ogni informazione portante deve essere verificata.

Sono ammesse come prove:

- fonte primaria;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita e ricontrollata;
- risultato riprodotto con ambiente, comando, output e test.

Una frase plausibile non entra nella versione approvata senza prova.

### 7.2 Classi di contenuto

- **Fatto da fonte primaria**.
- **Derivazione**.
- **Risultato eseguito**.
- **Illustrativo**.
- **Confine**.

Le inferenze fattuali editoriali non sono ammesse nella versione approvata.

### 7.3 Artefatti per capitolo

Ogni capitolo contiene:

- `FONTI_PRIMARIE.md`;
- `CLAIMS.md`;
- `TEXT_AUDIT.md`.

Una voce aperta in `CLAIMS.md` non entra come frase assertiva.

## 8. Fonti e ricerca

Gerarchia:

1. paper originale in atti ufficiali o rivista;
2. versione ufficiale degli autori;
3. technical report ufficiale;
4. documentazione ufficiale;
5. repository ufficiale;
6. standard e documenti istituzionali.

Le fonti secondarie possono aiutare a trovare le fonti primarie, ma non sostengono da sole una spiegazione portante, una formula, un dato o una firma API.

Per contenuti recenti vengono registrati:

- data della ricerca;
- versione della documentazione;
- versione del modello o checkpoint;
- revisione del paper;
- commit o release;
- hardware e comando per risultati riprodotti;
- differenze tra paper e implementazione.

La ricerca globale è registrata in `15_REGISTRO_RICERCHE_APPROFONDITE.md`. Ogni capitolo esegue inoltre una verifica locale.

## 9. Citazioni

Nel testo si usa una citazione breve vicina all'affermazione. Alla fine del capitolo si separano:

1. fonti primarie;
2. documentazione ufficiale;
3. repository e artefatti;
4. standard e documenti istituzionali;
5. letture complementari.

Una citazione generica non sostituisce il controllo della sezione esatta.

## 10. Testo e review

Ogni capitolo attraversa:

1. ricerca delle fonti;
2. mappa dei claim;
3. prima stesura;
4. audit fattuale frase per frase;
5. audit matematico;
6. audit architetturale e algoritmico;
7. audit temporale;
8. controllo incrociato con codice e visuali;
9. audit didattico;
10. seconda lettura integrale;
11. revisione autoriale.

Il protocollo completo è in `04_PROTOCOLLO_QA_TESTO.md`.

## 11. Visuali

Le visuali tecniche vengono create con lo strumento immagini. Gli SVG non sono l'artefatto editoriale principale.

Ogni visuale:

1. risponde a una sola domanda;
2. ha uno storyboard;
3. viene generata come bozza;
4. viene riletta senza affidarsi al prompt;
5. viene controllata per formule, numeri, shape, frecce, incroci e ordine;
6. viene rigenerata o modificata quando necessario;
7. viene ricontrollata integralmente;
8. entra nel capitolo soltanto come `final.png` approvato.

Una singola linea ambigua blocca l'approvazione.

Ogni asset finale ha alt text, equivalente testuale e audit. Il protocollo è in `03_PROTOCOLLO_QA_VISUALE.md`.

## 12. Codice

Il codice è parte strutturale del libro.

- Python e PyTorch sono predefiniti.
- NumPy può essere usato per esempi e controlli indipendenti.
- Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.
- Gli snippet sono normalmente brevi e autosufficienti.
- Script lunghi restano nel repository quando necessari.

Ogni snippet dichiara:

- ID e domanda;
- input e shape;
- operazione centrale;
- output e invariante;
- versione Python e libreria;
- device, dtype e seed;
- fonte dell'API;
- file, test e stato dell'audit.

Ogni snippet viene verificato sulla documentazione ufficiale, eseguito in un processo pulito, testato e rieseguito dopo le correzioni.

Un output è `Eseguito` soltanto quando esistono ambiente, comando, log o test registrati.

## 13. Controllo incrociato

Testo, formule, immagini e codice devono coincidere per:

- label;
- shape;
- numeri;
- ordine delle operazioni;
- invarianti;
- confini;
- versione tecnica.

Una contraddizione blocca il capitolo.

## 14. Aggiornamenti futuri

Ogni aggiornamento segue una delle procedure U1-U8 di `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`:

- nuova tecnica;
- nuova evidenza;
- aggiornamento API;
- cambio di maturità;
- nuovo capitolo;
- split o merge;
- correzione tecnica;
- nuova edizione.

Una nuova decisione globale viene registrata in `08_REGISTRO_DECISIONI.md` e propagata a tutti i documenti coinvolti.

## 15. Workflow e congelamento

Per ogni capitolo:

```text
fonti
-> claim
-> piano didattico
-> stesura
-> formule
-> codice e test
-> visuali e audit
-> review tecnica
-> review didattica
-> review autoriale
-> congelamento
```

La versione approvata riceve:

- data di congelamento;
- commit SHA;
- fonti esatte;
- codice, output e ambiente;
- visuali finali;
- audit completati.

Non si dichiara aggiornamento oltre la data verificata.

## 16. Documenti vincolanti

- `../GUIDELINE.md`;
- `08_REGISTRO_DECISIONI.md`;
- `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
- `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
- `14_CATALOGO_STATO_ARTE.md`;
- `10_INDICE_EDITORIALE.md`;
- protocolli specialistici da `01` a `07`;
- `EXPLANATION_STYLE_AND_VISUALS.md`.

In caso di divergenza il lavoro interessato resta bloccato finché i documenti non vengono riallineati.