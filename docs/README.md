# Documentazione canonica

Questa cartella contiene le regole editoriali, metodologiche e operative del libro.

La documentazione è organizzata per tema in pochi file canonici. I materiali metodologici originali restano in `source/`; le versioni precedenti sono recuperabili dalla cronologia Git.

## Stato

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Formato: Markdown
- Produzione: seriale, un capitolo completo alla volta
- Opera: unica e continua
- Capitoli pianificati: 98
- Appendici: 12
- Ultima ricerca approfondita globale: **30 luglio 2026**

## Ordine di lettura

Una persona o un sistema AI senza contesto legge:

1. `../GUIDELINE.md`;
2. `../README.md`;
3. questo file;
4. `00_GOVERNANCE_E_ARCHITETTURA.md`;
5. `01_INDICE_EDITORIALE.md`;
6. `14_CATALOGO_STATO_ARTE.md`;
7. `15_REGISTRO_RICERCHE_APPROFONDITE.md`;
8. il documento specialistico necessario;
9. `../PROGRESS.md`;
10. i file del capitolo coinvolto.

Per scrivere o revisionare una lezione:

1. `02_STILE_E_QA_TESTO.md`;
2. `04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
3. `05_WORKFLOW_E_REPOSITORY.md`;
4. `03_VISUALI.md`, quando sono previste figure.

## Documenti canonici

| Documento | Funzione |
|---|---|
| `00_GOVERNANCE_E_ARCHITETTURA.md` | Contratto editoriale, opera unica, parti stabili, routing, maturità, ID, decisioni e governance. |
| `01_INDICE_EDITORIALE.md` | Struttura compatta dei 98 capitoli e delle 12 appendici. |
| `02_STILE_E_QA_TESTO.md` | Metodo didattico, voce italiana, template del capitolo e review del testo. |
| `03_VISUALI.md` | Standard visivo, sfondo bianco, orientamento, palette, contenimento e QA. |
| `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` | Gerarchia delle fonti, claim, citazioni, snippet, test, API e ambienti. |
| `05_WORKFLOW_E_REPOSITORY.md` | Struttura delle cartelle, produzione seriale, aggiornamenti U1-U8, commit e congelamento. |
| `14_CATALOGO_STATO_ARTE.md` | Registro dettagliato delle famiglie, tecniche, maturità e destinazioni editoriali. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Dossier delle ricognizioni globali, fonti seme, limiti e date. |
| `source/README.md` | Indice dei materiali metodologici originali conservati integralmente. |

## Alias di compatibilità

Due percorsi storici restano temporaneamente come brevi rinvii, perché compaiono nel catalogo e nel registro della prima ricerca:

- `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` rinvia a `00_GOVERNANCE_E_ARCHITETTURA.md`;
- `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` rinvia a `05_WORKFLOW_E_REPOSITORY.md`.

Non sono documenti canonici e non ricevono nuove regole. Verranno rimossi dopo la migrazione degli ultimi riferimenti storici.

## Mappa del consolidamento

| Area precedente | Documento corrente |
|---|---|
| contratto, decisioni, architettura evolutiva e audit documentale | `00_GOVERNANCE_E_ARCHITETTURA.md` |
| indice dell'opera | `01_INDICE_EDITORIALE.md` |
| template del capitolo, stile, struttura in prosa, voce e QA testuale/didattico | `02_STILE_E_QA_TESTO.md` |
| template visuale, standard, contenimento e protocollo QA | `03_VISUALI.md` |
| fonti, citazioni, snippet, API, test e riproducibilità | `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` |
| workflow, aggiornamenti, repository, ID, commit e freeze | `05_WORKFLOW_E_REPOSITORY.md` |
| catalogo e ricerca globale | `14_CATALOGO_STATO_ARTE.md` e `15_REGISTRO_RICERCHE_APPROFONDITE.md` |

## Accuratezza

La versione approvata non contiene fatti basati su inferenze editoriali. Ogni affermazione portante richiede fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto.

`CLAIMS.md` collega le frasi alle prove. `FONTI_PRIMARIE.md` registra sezioni, versioni e limiti.

## Prosa

Il capitolo deve leggersi come un manuale tecnico scritto direttamente in italiano. Lo scaffold resta in `PLAN.md` e `TEXT_AUDIT.md`; il lettore vede titoli semantici, paragrafi naturali e un esempio continuo.

Ogni capitolo supera review tecnica, review didattica, gate anti-template, review editoriale e linguistica, lettura ad alta voce e nuova lettura integrale.

## Visuali

Le immagini:

- usano sfondo bianco puro `#FFFFFF`;
- scelgono orientamento in base al contenuto;
- mantengono testo e simboli nei contenitori;
- non presentano frecce ambigue;
- condividono palette, box e tipografia;
- vengono revisionate e rigenerate;
- diventano `final.png` soltanto dopo approvazione tecnica e autoriale.

## Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata. Python e PyTorch sono predefiniti. Un output è `Eseguito` soltanto quando possiede ambiente, comando e log o test.

## Coerenza documentale

La documentazione è coerente quando un sistema senza contesto può:

- comprendere scopo e struttura;
- collocare e aggiornare una tecnica;
- creare o modificare un capitolo;
- applicare fonti, claim, codice e visuali;
- scrivere prosa da manuale;
- ripetere le review;
- ricostruire una versione approvata dal commit.

## Regola per nuovi file in `docs/`

Un nuovo documento canonico viene creato soltanto quando il contenuto:

1. non appartiene chiaramente a uno dei temi esistenti;
2. sarebbe difficile da consultare come sezione del documento corrente;
3. possiede un ciclo di aggiornamento realmente indipendente;
4. viene approvato nella governance.

Per impostazione predefinita, una nuova regola viene aggiunta al documento tematico esistente.
