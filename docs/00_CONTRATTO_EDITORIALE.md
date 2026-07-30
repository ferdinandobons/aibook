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
- Capitolo pilota: `CH-P06-ATTENTION`
- Visuali: PNG generati con lo strumento immagini
- Codice principale: Python e PyTorch
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Entry point operativo: `../GUIDELINE.md`

## 1. Obiettivo editoriale

Il libro è un manuale tecnico. Costruisce modelli mentali che il lettore possa ricostruire e applicare, senza ridurre i capitoli a elenchi di definizioni o a documentazione di progetto.

Al termine di ogni meccanismo il lettore deve poter:

1. identificare l'input;
2. descrivere l'ordine reale delle operazioni;
3. indicare output e shape;
4. spiegare che cosa cambia e che cosa resta invariato;
5. localizzare il componente nel sistema;
6. dichiararne i confini;
7. prevedere una variazione controllata;
8. collegare la spiegazione a visuali e codice verificato.

Il testo destinato al lettore deve risultare fluido, discorsivo e naturale in italiano. Audit, metadati, stato editoriale e dettagli operativi restano negli artefatti interni.

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

ID, nomi e ordine sono stabili. Una nuova tecnica viene collocata in base al problema risolto e all'oggetto modificato, non in base alla popolarità di un modello.

## 3. Identità e maturità

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

`chapter_id` è stabile. Il numero visualizzato è specifico dell'edizione.

Maturità:

- `CORE`: concetto durevole e necessario per sviluppi successivi;
- `ESTABLISHED`: verificato e rilevante, ma ancora in evoluzione o non universale;
- `FRONTIER`: recente, sperimentale o con evidenza limitata.

La maturità non determina la collocazione.

## 4. Lettore target e profondità

Il livello principale è intermedio tecnico. Gli approfondimenti avanzati entrano quando servono a spiegare correttamente:

- matematica e derivazioni;
- shape e contratti tensoriali;
- stabilità numerica;
- complessità;
- memoria e data movement;
- implementazione;
- training distribuito;
- inference e serving;
- hardware, compiler e kernel;
- trade-off tra qualità, latenza, memoria, costo ed energia.

Il caso base viene stabilizzato prima delle varianti avanzate.

## 5. Metodo di spiegazione

Il metodo vincolante è `EXPLANATION_STYLE_AND_VISUALS.md`, integrato da:

- `18_PROTOCOLLO_QA_DIDATTICO.md`;
- `19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

Ogni capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale. Internamente, per ogni transizione, vengono verificati stato, problema, input, operazione, output, invariante, confine e passaggio successivo.

Queste funzioni non diventano una sequenza obbligatoria di titoli. `PLAN.md` e `TEXT_AUDIT.md` espongono lo scaffold; `CHAPTER.md` presenta una spiegazione da manuale.

Quando pertinente, l'ordine di introduzione è:

```text
domanda concreta
-> esempio osservabile
-> valori e shape
-> algoritmo o pseudocodice
-> formula
-> derivazione
-> implementazione verificata
-> varianti
```

## 6. Voce editoriale

La prosa deve:

- sembrare scritta direttamente in italiano;
- usare titoli legati al contenuto;
- organizzare sezioni abbastanza ampie da sostenere un ragionamento;
- alternare periodi brevi e articolati;
- mantenere soggetti e referenti chiari;
- conservare i termini inglesi standard senza tradurre la sintassi dall'inglese;
- limitare cautele e negazioni alla loro funzione;
- separare la spiegazione dai materiali di progetto;
- superare una lettura ad alta voce.

Sono difetti bloccanti:

- prosa da specifica, audit o reference API;
- frammentazione in microsezioni;
- calchi non necessari;
- ritmo meccanico;
- metadati operativi nel flusso del manuale;
- riepiloghi ridotti a checklist.

## 7. Accuratezza

Ogni informazione portante deve essere verificata.

Sono ammesse come prove:

- fonte primaria;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione matematica esplicita;
- risultato riprodotto con ambiente, comando, output e test.

Classi di contenuto:

- fatto da fonte;
- derivazione;
- risultato eseguito;
- esempio illustrativo;
- confine.

Le inferenze fattuali editoriali non sono ammesse.

Ogni capitolo contiene `FONTI_PRIMARIE.md`, `CLAIMS.md` e `TEXT_AUDIT.md`. Una voce aperta in `CLAIMS.md` non entra come frase assertiva.

## 8. Fonti e citazioni

Gerarchia:

1. paper originale in atti ufficiali o rivista;
2. versione ufficiale degli autori;
3. technical report ufficiale;
4. documentazione ufficiale;
5. repository ufficiale;
6. standard e documenti istituzionali.

Le fonti secondarie possono aiutare la ricerca, ma non sostengono da sole una spiegazione portante.

Nel testo si usa una citazione breve vicina all'affermazione. Schede, versioni, sezioni e limiti restano nel dossier delle fonti.

## 9. Testo e review

Ogni capitolo attraversa:

1. ricerca delle fonti;
2. mappa dei claim;
3. prima stesura;
4. audit fattuale;
5. audit matematico;
6. audit architetturale e algoritmico;
7. audit temporale;
8. controllo incrociato;
9. review didattica;
10. gate anti-template;
11. review editoriale e linguistica;
12. lettura ad alta voce;
13. seconda lettura integrale;
14. revisione autoriale.

Una correzione strutturale o linguistica riapre le review pertinenti.

## 10. Visuali

Le visuali tecniche vengono create con lo strumento immagini. Gli SVG non sono l'artefatto editoriale principale.

Ogni visuale:

1. risponde a una domanda;
2. possiede uno storyboard;
3. viene generata come bozza;
4. viene riletta senza affidarsi al prompt;
5. viene controllata per formule, numeri, shape, frecce e ordine;
6. viene rigenerata quando necessario;
7. viene ricontrollata integralmente;
8. diventa `final.png` soltanto dopo approvazione.

Sfondo bianco puro, contenimento del testo e assenza di collegamenti ambigui sono obbligatori.

## 11. Codice

Il codice è parte strutturale del libro.

- Python e PyTorch sono predefiniti.
- NumPy può essere usato per controlli indipendenti.
- Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.
- Gli snippet nel corpo sono brevi; file completi e test restano nel repository.
- Ogni API viene verificata sulla documentazione ufficiale.
- Gli output dichiarati `Eseguito` hanno ambiente, comando e log o test.

I dettagli di riproducibilità non interrompono il flusso del manuale, salvo che siano necessari a interpretare il risultato.

## 12. Controllo incrociato

Testo, formule, immagini e codice devono coincidere per:

- label;
- shape;
- numeri;
- ordine delle operazioni;
- invarianti;
- confini;
- versione tecnica.

Una contraddizione blocca il capitolo.

## 13. Aggiornamenti futuri

Ogni aggiornamento segue una delle procedure U1-U8 di `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

Una nuova decisione globale viene registrata in `08_REGISTRO_DECISIONI.md` e propagata ai documenti coinvolti.

## 14. Workflow e congelamento

```text
fonti
-> claim
-> piano interno
-> stesura
-> formule
-> codice e test
-> visuali e audit
-> review tecnica
-> review didattica
-> gate anti-template
-> review linguistica
-> lettura completa
-> review autoriale
-> congelamento
```

La versione approvata riceve data, commit SHA, fonti esatte, codice, output, ambiente, visuali finali e audit completati.

Non si dichiara aggiornamento oltre la data verificata.
