# Documentazione canonica del progetto

Questa cartella contiene tutte le decisioni editoriali, metodologiche, tecniche e operative vincolanti per il libro.

Nessuna regola necessaria alla produzione dei capitoli deve dipendere dalla cronologia della conversazione, da file esterni non presenti nel repository o da conoscenza implicita. Prima di iniziare un capitolo o modificare un artefatto, i documenti di questa cartella costituiscono la fonte di verità del progetto.

## Repository operativo

- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Formato sorgente: Markdown
- Modalità di produzione: seriale controllata, un capitolo completo alla volta
- Capitolo pilota: `CH-P06-ATTENTION`, visualizzato come Capitolo 28 nell'edizione di lavoro
- Ultima ricerca approfondita globale registrata: 30 luglio 2026

## Da dove iniziare

Un sistema AI o una persona senza contesto precedente legge nell'ordine:

1. `../GUIDELINE.md`;
2. `../README.md`;
3. questo file;
4. `00_CONTRATTO_EDITORIALE.md`;
5. `08_REGISTRO_DECISIONI.md`;
6. `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
7. `14_CATALOGO_STATO_ARTE.md`;
8. `10_INDICE_EDITORIALE.md`;
9. `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
10. i protocolli specialistici necessari;
11. `../PROGRESS.md`;
12. i file del capitolo coinvolto.

Per un'attività che crea o modifica immagini tecniche, la lettura specialistica minima è:

1. `17_STANDARD_VISIVO_CANONICO.md`;
2. `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`;
3. `02_TEMPLATE_VISUALE.md`;
4. `03_PROTOCOLLO_QA_VISUALE.md`;
5. `EXPLANATION_STYLE_AND_VISUALS.md`.

## Mappa dei documenti

| Documento | Funzione |
|---|---|
| `00_CONTRATTO_EDITORIALE.md` | Obiettivi, livello tecnico, politica generale, quality gate e vincoli globali. |
| `01_TEMPLATE_CAPITOLO.md` | Struttura obbligatoria di ogni capitolo e registri di approvazione. |
| `02_TEMPLATE_VISUALE.md` | Scheda di progettazione e audit per ogni immagine. Include stile, orientamento e contenimento. |
| `03_PROTOCOLLO_QA_VISUALE.md` | Processo iterativo di generazione, revisione, rigenerazione e approvazione delle immagini. |
| `04_PROTOCOLLO_QA_TESTO.md` | Processo di verifica fattuale, matematica, architetturale, temporale e didattica del testo. |
| `05_STANDARD_SNIPPET_CODICE.md` | Regole per snippet, script completi, esecuzione, test e audit del codice. |
| `06_WORKFLOW_CAPITOLO.md` | Sequenza operativa completa, dalla ricerca al congelamento del commit. |
| `07_POLITICA_FONTI_CITAZIONI.md` | Gerarchia delle fonti, verifica web, citazioni, divergenze e data di congelamento. |
| `08_REGISTRO_DECISIONI.md` | Elenco consolidato delle decisioni correnti e sostituite. |
| `09_STRUTTURA_REPOSITORY.md` | Convenzioni per cartelle, file, ID, asset, audit e artefatti riproducibili. |
| `10_INDICE_EDITORIALE.md` | Indice dell'opera unica organizzata nelle quattordici parti stabili. |
| `11_AUDIT_DOCUMENTAZIONE.md` | Controllo di completezza, coerenza e assenza di decisioni bloccanti. |
| `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` | Parti stabili, routing, maturità e identità semantica dei capitoli. |
| `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` | Procedure per nuove tecniche, nuove evidenze, API, maturità, capitoli ed edizioni. |
| `14_CATALOGO_STATO_ARTE.md` | Principali famiglie, tecniche e ottimizzazioni censite. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Registro delle ricognizioni globali e dei relativi confini temporali. |
| `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` | Regola canonica che impedisce testo debordante, tagliato, sovrapposto o privo di padding. |
| `17_STANDARD_VISIVO_CANONICO.md` | Grammatica visiva comune: sfondo bianco, orientamento adattivo, palette, box, frecce, tipografia e densità. |
| `EXPLANATION_STYLE_AND_VISUALS.md` | Metodo completo di spiegazione in italiano e grammatica didattica del libro. |
| `source/README.md` | Indice delle fonti metodologiche originali archiviate. |

## Regola fondamentale sull'accuratezza

La versione approvata del libro non contiene affermazioni fattuali basate su inferenze editoriali. Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale deve essere sostenuta da una fonte primaria, da documentazione ufficiale, da uno standard oppure da una prova riproducibile.

Sono ammessi:

- derivazioni matematiche esplicite e ricontrollate;
- esempi dichiarati come `Illustrativo` e internamente coerenti;
- risultati dichiarati come `Eseguito`, accompagnati da ambiente, comando, output e test;
- confini che descrivono con precisione ciò che un meccanismo non implementa.

Quando una fonte non consente di verificare un'affermazione, la frase non entra nella versione approvata.

## Regola fondamentale sugli artefatti

Ogni capitolo tecnico integra:

1. testo didattico verificato;
2. immagini tecniche generate con lo strumento immagini e approvate dopo audit iterativo;
3. snippet di codice eseguiti, testati e allineati al testo.

Testo, formule, immagini e codice condividono nomi, shape, numeri, ordine delle operazioni e confini.

## Regole fondamentali sulle visuali

Tutte le immagini tecniche usano la grammatica definita in `17_STANDARD_VISIVO_CANONICO.md`.

In particolare:

- lo sfondo globale è sempre bianco puro `#FFFFFF`;
- l'orientamento può essere orizzontale o verticale in base al contenuto;
- palette, box, frecce e gerarchia tipografica conservano ruoli comuni;
- una figura risponde a una sola domanda principale;
- una figura tecnica non è una renderizzazione completa della pagina del libro.

Ogni testo deve rimanere integralmente dentro il proprio box, cella, badge, callout o pannello. Testo debordante, tagliato, sovrapposto, troppo vicino al bordo o privo di margine interno costituisce un difetto bloccante.

La regola dettagliata sul contenimento è in `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`. Il template e il protocollo QA applicano entrambi gli standard.

## Ordine di autorità e aggiornamenti

I documenti devono essere mantenuti coerenti tra loro. Non è ammesso risolvere silenziosamente un conflitto scegliendo un documento e ignorandone un altro.

Quando viene presa una nuova decisione:

1. si registra in `08_REGISTRO_DECISIONI.md`;
2. si aggiornano il contratto e i protocolli interessati;
3. si aggiornano template, catalogo e indice quando necessario;
4. si controllano i riferimenti incrociati;
5. si aggiorna `11_AUDIT_DOCUMENTAZIONE.md`;
6. si registra il commit.

In presenza di una divergenza non ancora corretta, il lavoro interessato resta bloccato.

## Archivio metodologico

Il contenuto originale di `EXPLANATION_STYLE_AND_VISUALS.md` fornito dal committente è conservato integralmente in `source/`, diviso in segmenti consecutivi per mantenerne la tracciabilità.

Il documento canonico applicato al libro è `EXPLANATION_STYLE_AND_VISUALS.md`. I riferimenti originari specifici di altri progetti restano nell'archivio, mentre le regole operative rispettano le decisioni correnti.

Per sfondo, palette, orientamento e componenti delle immagini raster tecniche prevale `17_STANDARD_VISIVO_CANONICO.md`.

## Dipendenze escluse

`LEARN_GOVERNANCE.md` non è una dipendenza del libro. Tutte le regole necessarie sono riportate nel repository. Nessuna frase guida esterna è obbligatoria.
