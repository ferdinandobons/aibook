# Documentazione canonica

Questa cartella contiene le regole editoriali, metodologiche e operative del libro.

La documentazione è stata consolidata per evitare sovrapposizioni. Le regole sono organizzate per tema in pochi documenti canonici. I materiali originali ricevuti restano in `source/` e lo storico dei file precedenti resta disponibile in Git.

## Stato

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Formato: Markdown
- Modalità: produzione seriale, un capitolo completo alla volta
- Opera: unica e continua
- Capitoli pianificati: 98
- Appendici pianificate: 12
- Ultima ricerca approfondita globale: **30 luglio 2026**

## Ordine di lettura

Una persona o un sistema AI senza contesto precedente legge:

1. `../GUIDELINE.md`;
2. `../README.md`;
3. questo file;
4. `00_GOVERNANCE_E_ARCHITETTURA.md`;
5. `01_INDICE_EDITORIALE.md`;
6. `14_CATALOGO_STATO_ARTE.md`;
7. `15_REGISTRO_RICERCHE_APPROFONDITE.md`;
8. il documento specialistico necessario;
9. `../PROGRESS.md`;
10. gli artefatti del capitolo coinvolto.

Per scrivere o revisionare una lezione:

1. `02_STILE_E_QA_TESTO.md`;
2. `04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
3. `05_WORKFLOW_E_REPOSITORY.md`;
4. `03_VISUALI.md`, quando sono previste figure.

## Mappa dei documenti

| Documento | Funzione |
|---|---|
| `00_GOVERNANCE_E_ARCHITETTURA.md` | Contratto editoriale, opera unica, parti stabili, routing, maturità, ID, decisioni e governance. |
| `01_INDICE_EDITORIALE.md` | Indice compatto delle quattordici parti, dei 98 capitoli e delle appendici. |
| `02_STILE_E_QA_TESTO.md` | Metodo didattico, voce italiana, template del capitolo, gate di comparsa e review del testo. |
| `03_VISUALI.md` | Standard visivo, sfondo bianco, orientamento, palette, contenimento, `SPEC.md` e QA delle figure. |
| `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` | Gerarchia delle fonti, claim, citazioni, verifica temporale, snippet, test, output e ambienti. |
| `05_WORKFLOW_E_REPOSITORY.md` | Struttura delle cartelle, ID, ciclo di produzione, aggiornamenti U1-U8, commit e congelamento. |
| `14_CATALOGO_STATO_ARTE.md` | Registro dettagliato delle famiglie, tecniche, maturità e destinazioni editoriali. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Dossier delle ricerche globali, fonti seme, limiti e date di copertura. |
| `source/README.md` | Indice dei materiali metodologici originali conservati integralmente. |

## Consolidamento applicato

Le informazioni dei precedenti documenti sono state assorbite come segue.

| Area precedente | Documento canonico corrente |
|---|---|
| contratto, decisioni, architettura evolutiva e audit documentale | `00_GOVERNANCE_E_ARCHITETTURA.md` |
| indice dell'opera | `01_INDICE_EDITORIALE.md` |
| template del capitolo, stile di spiegazione, struttura in prosa, voce, QA testuale e didattico | `02_STILE_E_QA_TESTO.md` |
| template visuale, standard, contenimento e protocollo QA | `03_VISUALI.md` |
| fonti, citazioni, snippet, API, test e riproducibilità | `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` |
| workflow, aggiornamenti, struttura repository, ID, commit e freeze | `05_WORKFLOW_E_REPOSITORY.md` |
| catalogo e ricerca globale | `14_CATALOGO_STATO_ARTE.md` e `15_REGISTRO_RICERCHE_APPROFONDITE.md` |

I file precedenti vengono rimossi dopo l'aggiornamento di tutti i riferimenti. La migrazione non modifica le regole sostanziali; elimina ripetizioni e punti di conflitto.

## Accuratezza

La versione approvata non contiene fatti basati su inferenze editoriali. Ogni affermazione tecnica, storica, quantitativa, architetturale o temporale richiede:

- fonte primaria;
- documentazione ufficiale;
- repository ufficiale;
- standard;
- derivazione verificata;
- oppure risultato riprodotto.

`CLAIMS.md` collega ogni affermazione portante alla prova. `FONTI_PRIMARIE.md` registra sezioni, versioni e limiti.

## Prosa

Il capitolo deve leggersi come un manuale tecnico in italiano. Lo scaffold di stato, problema, trasformazione, output, invariante e confine resta in `PLAN.md` e `TEXT_AUDIT.md`; il lettore vede titoli semantici, paragrafi naturali e un esempio continuo.

Ogni capitolo supera:

- review fattuale e matematica;
- review didattica;
- gate anti-template;
- review editoriale e linguistica;
- lettura ad alta voce;
- nuova lettura integrale dopo le correzioni.

## Visuali

Tutte le immagini tecniche:

- usano sfondo bianco puro `#FFFFFF`;
- scelgono orientamento in base al contenuto;
- mantengono il testo dentro i box;
- non presentano frecce ambigue;
- condividono palette, box e tipografia;
- vengono revisionate e rigenerate;
- diventano `final.png` soltanto dopo approvazione tecnica e autoriale.

## Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata. Python e PyTorch sono predefiniti. Ogni output dichiarato `Eseguito` possiede ambiente, comando, log o test.

## Coerenza documentale

La documentazione è considerata coerente quando un sistema senza contesto può:

- comprendere scopo e struttura;
- collocare e aggiornare una tecnica;
- creare o modificare un capitolo;
- applicare fonti, claim, codice e visuali;
- scrivere prosa da manuale;
- ripetere le review fino alla rimozione dei difetti bloccanti;
- ricostruire una versione approvata dal commit.

Quando una decisione cambia, vengono aggiornati il documento tematico, questo indice, `GUIDELINE.md`, i riferimenti e gli audit interessati prima di riprendere la produzione.

## Regola per nuovi file in `docs/`

Un nuovo documento canonico viene creato soltanto quando il contenuto:

1. non appartiene chiaramente a uno dei temi esistenti;
2. sarebbe difficile da consultare come sezione del documento corrente;
3. possiede un ciclo di aggiornamento realmente indipendente;
4. viene approvato nella governance.

Per impostazione predefinita, una nuova regola viene aggiunta al documento tematico esistente anziché creare un altro file.
