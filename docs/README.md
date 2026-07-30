# Documentazione canonica

Questa cartella contiene le regole editoriali, metodologiche e operative del libro.

La documentazione è organizzata per tema in pochi file canonici. I materiali metodologici originali restano in `source/`; le versioni precedenti sono recuperabili dalla cronologia Git.

## Stato

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di produzione: `feature/full-book-production`
- Formato: Markdown
- Produzione: seriale, una candidatura completa alla volta
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
| `01_INDICE_EDITORIALE.md` | Struttura dei 98 capitoli e delle 12 appendici. |
| `02_STILE_E_QA_TESTO.md` | Metodo didattico, voce italiana, template del capitolo e review del testo. |
| `03_VISUALI.md` | Standard visivo, sfondo bianco, orientamento, palette, contenimento e QA. |
| `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` | Gerarchia delle fonti, claim, citazioni, snippet, test, API e ambienti. |
| `05_WORKFLOW_E_REPOSITORY.md` | Struttura delle cartelle, produzione seriale, aggiornamenti U1-U8, commit e congelamento. |
| `14_CATALOGO_STATO_ARTE.md` | Registro dettagliato delle famiglie, tecniche, maturità e destinazioni editoriali. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Dossier delle ricognizioni globali, fonti seme, limiti e date. |
| `source/README.md` | Indice dei materiali metodologici originali conservati integralmente. |

## Alias di compatibilità

Due percorsi storici restano temporaneamente come brevi rinvii:

- `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` rinvia a `00_GOVERNANCE_E_ARCHITETTURA.md`;
- `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` rinvia a `05_WORKFLOW_E_REPOSITORY.md`.

Non sono documenti canonici e non ricevono nuove regole.

## Accuratezza

La versione approvata non contiene fatti basati su inferenze editoriali. Ogni affermazione portante richiede fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto.

`CLAIMS.md` collega le frasi alle prove. `FONTI_PRIMARIE.md` registra sezioni, versioni e limiti.

## Prosa

Il capitolo deve leggersi come un manuale tecnico scritto direttamente in italiano. Lo scaffold resta in `PLAN.md` e `TEXT_AUDIT.md`; il lettore vede titoli semantici, paragrafi naturali e un esempio continuo.

Ogni capitolo supera review tecnica, review didattica, gate anti-template, review editoriale e linguistica, controllo per un lettore non esperto e nuova lettura integrale.

## Visuali

Le immagini:

- usano sfondo bianco puro `#FFFFFF`;
- scelgono orientamento in base al contenuto;
- mantengono testo e simboli nei contenitori;
- non presentano frecce ambigue;
- condividono palette, box e tipografia;
- vengono revisionate e rigenerate;
- diventano `final.png` soltanto dopo approvazione tecnica e autoriale.

I generatori raster correnti sono in `../scripts/`; il workflow `generate-book-visuals.yml` produce e verifica i PNG candidati nel feature branch.

## Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata. Python e PyTorch sono predefiniti. Un output è `Eseguito` soltanto quando possiede ambiente, comando e log o test.

## Stato della produzione

- Capitolo 1: candidatura completa `0.4.0-rc3`;
- Capitolo 2: candidatura completa `0.2.0-rc1`;
- Capitolo 3: ricerca aperta;
- Capitolo 28: candidatura completa `0.6.0-rc6`.

Lo stato dettagliato è in `../PROGRESS.md` e `../BOOK_PRODUCTION.md`.

## Regola per nuovi file in `docs/`

Un nuovo documento canonico viene creato soltanto quando il contenuto:

1. non appartiene chiaramente a uno dei temi esistenti;
2. sarebbe difficile da consultare come sezione del documento corrente;
3. possiede un ciclo di aggiornamento realmente indipendente;
4. viene approvato nella governance.

Per impostazione predefinita, una nuova regola viene aggiunta al documento tematico esistente.
