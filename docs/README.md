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

Per scrivere o revisionare una lezione, la lettura specialistica minima è:

1. `EXPLANATION_STYLE_AND_VISUALS.md`;
2. `19_STRUTTURA_LOGICA_IN_PROSA.md`;
3. `18_PROTOCOLLO_QA_DIDATTICO.md`;
4. `01_TEMPLATE_CAPITOLO.md`;
5. `04_PROTOCOLLO_QA_TESTO.md`;
6. `06_WORKFLOW_CAPITOLO.md`.

Per creare o modificare immagini tecniche:

1. `17_STANDARD_VISIVO_CANONICO.md`;
2. `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`;
3. `02_TEMPLATE_VISUALE.md`;
4. `03_PROTOCOLLO_QA_VISUALE.md`;
5. `EXPLANATION_STYLE_AND_VISUALS.md`.

## Mappa dei documenti

| Documento | Funzione |
|---|---|
| `00_CONTRATTO_EDITORIALE.md` | Obiettivi, livello tecnico, politica generale, quality gate e vincoli globali. |
| `01_TEMPLATE_CAPITOLO.md` | Distingue scaffold interno e capitolo in prosa; definisce gli artefatti e i gate. |
| `02_TEMPLATE_VISUALE.md` | Scheda di progettazione e audit per ogni immagine. Include stile, orientamento e contenimento. |
| `03_PROTOCOLLO_QA_VISUALE.md` | Processo iterativo di generazione, revisione, rigenerazione e approvazione delle immagini. |
| `04_PROTOCOLLO_QA_TESTO.md` | Verifica fattuale, matematica, architetturale, temporale e testuale. |
| `05_STANDARD_SNIPPET_CODICE.md` | Regole per snippet, script, esecuzione, test e audit del codice. |
| `06_WORKFLOW_CAPITOLO.md` | Sequenza operativa completa, dalla ricerca al congelamento. |
| `07_POLITICA_FONTI_CITAZIONI.md` | Gerarchia delle fonti, verifica web, citazioni e data di congelamento. |
| `08_REGISTRO_DECISIONI.md` | Elenco consolidato delle decisioni correnti e sostituite. |
| `09_STRUTTURA_REPOSITORY.md` | Convenzioni per cartelle, file, ID, asset e artefatti riproducibili. |
| `10_INDICE_EDITORIALE.md` | Indice dell'opera unica nelle quattordici parti stabili. |
| `11_AUDIT_DOCUMENTAZIONE.md` | Controllo di completezza e coerenza della documentazione. |
| `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` | Parti stabili, routing, maturità e identità dei capitoli. |
| `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` | Procedure per nuove tecniche, API, maturità, capitoli ed edizioni. |
| `14_CATALOGO_STATO_ARTE.md` | Principali famiglie, tecniche e ottimizzazioni censite. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Registro delle ricognizioni globali e dei confini temporali. |
| `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` | Impedisce testo debordante, tagliato, sovrapposto o privo di padding. |
| `17_STANDARD_VISIVO_CANONICO.md` | Sfondo bianco, orientamento adattivo, palette, box, frecce e tipografia. |
| `18_PROTOCOLLO_QA_DIDATTICO.md` | Review iterativa della progressione didattica, inclusa la verifica anti-template. |
| `19_STRUTTURA_LOGICA_IN_PROSA.md` | Mantiene obbligatoria la logica del metodo senza esporla come serie rigida di intestazioni. |
| `EXPLANATION_STYLE_AND_VISUALS.md` | Metodo completo di spiegazione in italiano e grammatica didattica. |
| `source/README.md` | Indice delle fonti metodologiche originali archiviate. |

## Regola fondamentale sull'accuratezza

La versione approvata del libro non contiene affermazioni fattuali basate su inferenze editoriali. Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale deve essere sostenuta da una fonte primaria, da documentazione ufficiale, da uno standard oppure da una prova riproducibile.

Sono ammessi:

- derivazioni matematiche esplicite e ricontrollate;
- esempi dichiarati come `Illustrativo` e internamente coerenti;
- risultati dichiarati come `Eseguito`, accompagnati da ambiente, comando, output e test;
- confini che descrivono con precisione ciò che un meccanismo non implementa.

Quando una fonte non consente di verificare un'affermazione, la frase non entra nella versione approvata.

## Regola fondamentale sulla prosa

La struttura logica di stato, problema, trasformazione, output, invariante, confine e continuità è obbligatoria. Per impostazione predefinita viene incorporata in paragrafi e titoli semantici, non pubblicata come una sequenza ripetitiva di intestazioni metacognitive.

`PLAN.md` e `TEXT_AUDIT.md` rendono esplicito lo scaffold. `CHAPTER.md` deve apparire come una spiegazione tecnica naturale. Il reviewer deve poter ricostruire lo scaffold leggendo la prosa, ma il lettore non deve vedere un modulo compilato.

## Regola fondamentale sugli artefatti

Ogni capitolo tecnico integra:

1. testo didattico verificato;
2. immagini tecniche generate con lo strumento immagini e approvate dopo audit iterativo;
3. snippet di codice eseguiti, testati e allineati al testo.

Testo, formule, immagini e codice condividono nomi, shape, numeri, ordine delle operazioni e confini.

## Regole fondamentali sulle visuali

Tutte le immagini tecniche usano `17_STANDARD_VISIVO_CANONICO.md`.

- sfondo globale bianco puro `#FFFFFF`;
- orientamento orizzontale o verticale in base al contenuto;
- palette, box, frecce e gerarchia tipografica coerenti;
- una domanda principale per figura;
- nessun render completo della pagina usato come figura tecnica.

Ogni testo deve rimanere integralmente dentro il proprio contenitore. Overflow, clipping, sovrapposizioni e padding insufficiente sono difetti bloccanti.

## Ordine di autorità e aggiornamenti

I documenti devono restare coerenti. Non è ammesso risolvere silenziosamente un conflitto scegliendo un documento e ignorandone un altro.

Quando viene presa una nuova decisione:

1. si registra in `08_REGISTRO_DECISIONI.md`;
2. si aggiornano contratto e protocolli interessati;
3. si aggiornano template, catalogo e indice quando necessario;
4. si controllano i riferimenti incrociati;
5. si aggiorna `11_AUDIT_DOCUMENTAZIONE.md`;
6. si registra il commit.

In presenza di una divergenza non corretta, il lavoro interessato resta bloccato.

## Archivio metodologico

Il contenuto originale del file metodologico fornito dal committente è conservato in `source/`. Il documento canonico applicato al libro è `EXPLANATION_STYLE_AND_VISUALS.md`, integrato dai protocolli successivi.

Per la struttura visibile dei capitoli prevale `19_STRUTTURA_LOGICA_IN_PROSA.md`. Per le immagini raster tecniche prevale `17_STANDARD_VISIVO_CANONICO.md`.

## Dipendenze escluse

`LEARN_GOVERNANCE.md` non è una dipendenza del libro. Tutte le regole necessarie sono riportate nel repository.