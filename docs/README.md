# Documentazione canonica del progetto

Questa cartella contiene le decisioni editoriali, metodologiche, tecniche e operative vincolanti per il libro.

Nessuna regola necessaria alla produzione deve dipendere dalla cronologia della conversazione o da conoscenza implicita. Il repository è la fonte di verità.

## Repository operativo

- Repository: `ferdinandobons/aibook`
- Branch predefinito: `main`
- Formato sorgente: Markdown
- Produzione: seriale controllata, un capitolo completo alla volta
- Capitolo pilota: `CH-P06-ATTENTION`
- Ultima ricerca approfondita globale: 30 luglio 2026

## Da dove iniziare

Una persona o un sistema AI senza contesto precedente legge:

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
12. gli artefatti del capitolo coinvolto.

Per scrivere o revisionare una lezione, la lettura specialistica minima è:

1. `EXPLANATION_STYLE_AND_VISUALS.md`;
2. `19_STRUTTURA_LOGICA_IN_PROSA.md`;
3. `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`;
4. `18_PROTOCOLLO_QA_DIDATTICO.md`;
5. `01_TEMPLATE_CAPITOLO.md`;
6. `04_PROTOCOLLO_QA_TESTO.md`;
7. `06_WORKFLOW_CAPITOLO.md`.

Per creare o modificare immagini tecniche:

1. `17_STANDARD_VISIVO_CANONICO.md`;
2. `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`;
3. `02_TEMPLATE_VISUALE.md`;
4. `03_PROTOCOLLO_QA_VISUALE.md`;
5. `EXPLANATION_STYLE_AND_VISUALS.md`.

## Mappa dei documenti

| Documento | Funzione |
|---|---|
| `00_CONTRATTO_EDITORIALE.md` | Obiettivi, livello tecnico, voce, quality gate e vincoli globali. |
| `01_TEMPLATE_CAPITOLO.md` | Distingue scaffold, testo del manuale e artefatti di prova. |
| `02_TEMPLATE_VISUALE.md` | Specifica e audit di ogni immagine. |
| `03_PROTOCOLLO_QA_VISUALE.md` | Generazione, revisione e approvazione delle visuali. |
| `04_PROTOCOLLO_QA_TESTO.md` | Verifica fattuale, matematica, didattica, editoriale e linguistica. |
| `05_STANDARD_SNIPPET_CODICE.md` | Snippet, esecuzione, test e audit del codice. |
| `06_WORKFLOW_CAPITOLO.md` | Sequenza completa dalla ricerca al congelamento. |
| `07_POLITICA_FONTI_CITAZIONI.md` | Gerarchia delle fonti, citazioni e date di verifica. |
| `08_REGISTRO_DECISIONI.md` | Decisioni correnti e sostituite. |
| `09_STRUTTURA_REPOSITORY.md` | Convenzioni per cartelle, file, ID e artefatti. |
| `10_INDICE_EDITORIALE.md` | Indice dell'opera nelle quattordici parti stabili. |
| `11_AUDIT_DOCUMENTAZIONE.md` | Controllo di completezza e coerenza. |
| `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` | Parti, routing, maturità e identità dei capitoli. |
| `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` | Procedure per tecniche, API, maturità, capitoli ed edizioni. |
| `14_CATALOGO_STATO_ARTE.md` | Famiglie, tecniche e ottimizzazioni censite. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Ricognizioni globali e confini temporali. |
| `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` | Divieto di overflow, clipping e sovrapposizioni. |
| `17_STANDARD_VISIVO_CANONICO.md` | Sfondo bianco, orientamento, palette, box, frecce e tipografia. |
| `18_PROTOCOLLO_QA_DIDATTICO.md` | Review strutturale, anti-template, editoriale e linguistica. |
| `19_STRUTTURA_LOGICA_IN_PROSA.md` | Logica rigorosa incorporata nella prosa. |
| `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md` | Voce da manuale, italiano idiomatico, ritmo e lettura ad alta voce. |
| `EXPLANATION_STYLE_AND_VISUALS.md` | Metodo integrato di spiegazione, visuali e codice. |
| `source/README.md` | Indice delle fonti metodologiche archiviate. |

## Accuratezza

La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali. Ogni affermazione tecnica, storica, architetturale, quantitativa o temporale è sostenuta da una fonte primaria, documentazione ufficiale, uno standard, una derivazione o una prova riproducibile.

Sono ammessi:

- derivazioni esplicite;
- esempi dichiarati `Illustrativo`;
- risultati dichiarati `Eseguito`, con ambiente e test;
- confini precisi.

Quando una fonte non stabilisce un punto, la frase non entra nella versione approvata.

## Prosa del manuale

La struttura logica di stato, problema, trasformazione, output, invariante, confine e continuità è obbligatoria. Viene però incorporata in titoli semantici e paragrafi naturali.

`PLAN.md` e `TEXT_AUDIT.md` rendono esplicito lo scaffold. `CHAPTER.md` deve leggere come un manuale, non come una checklist, una specifica o un registro di audit.

Regole principali:

- metadati e stato editoriale fuori dal flusso del lettore;
- sezioni abbastanza ampie da sostenere un ragionamento;
- italiano scritto direttamente e senza calchi evitabili;
- ritmo variato;
- cautele non ripetute;
- esempio continuo mantenuto;
- dettagli di riproducibilità spostati negli artefatti;
- review linguistica e lettura ad alta voce obbligatorie.

## Artefatti

Ogni capitolo tecnico integra:

1. testo verificato e revisionato linguisticamente;
2. immagini tecniche approvate dopo audit iterativo;
3. codice eseguito e testato.

Testo, formule, immagini e codice condividono nomi, shape, numeri, ordine e confini.

## Visuali

Tutte le immagini seguono `17_STANDARD_VISIVO_CANONICO.md`:

- sfondo bianco puro `#FFFFFF`;
- orientamento scelto in base al contenuto;
- palette, box, frecce e tipografia coerenti;
- una domanda principale;
- nessun render completo della pagina usato come figura tecnica;
- testo integralmente contenuto.

## Aggiornamenti

Quando viene presa una nuova decisione:

1. si aggiorna `08_REGISTRO_DECISIONI.md`;
2. si aggiornano contratto e protocolli;
3. si aggiornano template e indice quando necessario;
4. si controllano i riferimenti incrociati;
5. si aggiorna `11_AUDIT_DOCUMENTAZIONE.md`;
6. si registra il commit.

In presenza di una divergenza non corretta, il lavoro resta bloccato.

## Dipendenze escluse

`LEARN_GOVERNANCE.md` non è una dipendenza del libro. Tutte le regole necessarie sono nel repository.
