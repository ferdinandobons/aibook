# Documentazione canonica del progetto

Questa cartella contiene tutte le decisioni editoriali, metodologiche, tecniche e operative vincolanti per il libro.

Nessuna regola necessaria alla produzione dei capitoli deve dipendere dalla cronologia della conversazione, da file esterni non presenti nel repository o da conoscenza implicita. Prima di iniziare un capitolo, i documenti di questa cartella costituiscono la fonte di verità del progetto.

## Repository operativo

- Repository: `ferdinandobons/aibook`
- Branch di lavoro predefinito: `main`
- Formato sorgente del libro: Markdown
- Modalità di produzione: seriale controllata, un capitolo completo alla volta
- Capitolo pilota: Capitolo 28, **Il meccanismo di attention**

## Mappa dei documenti

| Documento | Funzione |
|---|---|
| `00_CONTRATTO_EDITORIALE.md` | Obiettivi, livello tecnico, politica generale, quality gate e vincoli globali. |
| `01_TEMPLATE_CAPITOLO.md` | Struttura obbligatoria di ogni capitolo e registri di approvazione. |
| `02_TEMPLATE_VISUALE.md` | Scheda di progettazione e audit per ogni immagine. |
| `03_PROTOCOLLO_QA_VISUALE.md` | Processo iterativo di generazione, revisione, rigenerazione e approvazione delle immagini. |
| `04_PROTOCOLLO_QA_TESTO.md` | Processo di verifica fattuale, matematica, architetturale, temporale e didattica del testo. |
| `05_STANDARD_SNIPPET_CODICE.md` | Regole per snippet, script completi, esecuzione, test e audit del codice. |
| `06_WORKFLOW_CAPITOLO.md` | Sequenza operativa completa, dalla ricerca al congelamento del commit. |
| `07_POLITICA_FONTI_CITAZIONI.md` | Gerarchia delle fonti, verifica web, citazioni, divergenze e data di congelamento. |
| `08_REGISTRO_DECISIONI.md` | Elenco consolidato delle decisioni prese e del loro stato vincolante. |
| `09_STRUTTURA_REPOSITORY.md` | Convenzioni per cartelle, file, ID, asset, audit e artefatti riproducibili. |
| `10_INDICE_EDITORIALE.md` | Indice completo dei due volumi, capitoli e appendici. |
| `11_AUDIT_DOCUMENTAZIONE.md` | Controllo finale di completezza, coerenza e assenza di decisioni bloccanti. |
| `EXPLANATION_STYLE_AND_VISUALS.md` | Metodo completo di spiegazione in italiano e grammatica visuale del libro. |
| `source/README.md` | Indice delle fonti metodologiche originali archiviate. |

## Copia integrale del file metodologico ricevuto

Il contenuto originale di `EXPLANATION_STYLE_AND_VISUALS.md` fornito dal committente è conservato integralmente in `source/`, diviso in cinque segmenti consecutivi per mantenerne leggibile la tracciabilità nel repository.

Il documento canonico applicato al libro è `EXPLANATION_STYLE_AND_VISUALS.md`. I riferimenti originari specifici di altri progetti restano nell'archivio, mentre le regole operative del libro rispettano le decisioni correnti.

## Ordine di autorità

I documenti devono essere mantenuti coerenti tra loro. Non è ammesso risolvere silenziosamente un conflitto scegliendo un documento e ignorandone un altro.

Quando viene presa una nuova decisione:

1. si registra in `08_REGISTRO_DECISIONI.md`;
2. si aggiornano il contratto e i protocolli interessati;
3. si aggiornano i template, quando necessario;
4. si controllano i riferimenti incrociati;
5. si registra il commit.

In presenza di una divergenza non ancora corretta, il lavoro sul capitolo interessato resta bloccato.

## Regola fondamentale sull'accuratezza

La versione approvata del libro non contiene affermazioni fattuali basate su inferenze editoriali. Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale deve essere sostenuta da una fonte primaria, da documentazione ufficiale, da uno standard oppure da una prova riproducibile.

Sono ammessi:

- derivazioni matematiche esplicite e ricontrollate;
- esempi dichiarati come `Illustrativo` e internamente coerenti;
- risultati dichiarati come `Eseguito`, accompagnati da ambiente, comando, output e test;
- confini che descrivono con precisione ciò che un meccanismo non implementa.

Quando una fonte non consente di verificare un'affermazione, la frase non entra nella versione approvata.

## Regola fondamentale sugli artefatti

Ogni capitolo tecnico deve integrare tre livelli coerenti:

1. testo didattico verificato;
2. immagini generate con lo strumento immagini e approvate dopo audit iterativo;
3. snippet di codice eseguiti, testati e allineati al testo.

Testo, formule, immagini e codice devono condividere nomi, shape, numeri, ordine delle operazioni e confini.

## Dipendenze escluse

`LEARN_GOVERNANCE.md` non è una dipendenza del libro. Tutte le regole metodologiche necessarie sono riportate nei documenti di questa cartella. Nessuna frase guida esterna è obbligatoria.

## Stato prima dell'avvio

La stesura del capitolo pilota può iniziare soltanto dopo che:

- tutti i documenti elencati sopra sono presenti;
- non rimangono contraddizioni note;
- il registro delle decisioni è aggiornato;
- l'audit della documentazione è positivo;
- il committente dà esplicitamente il via.