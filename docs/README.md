# Documentazione canonica

Questa cartella contiene le regole editoriali, metodologiche e operative del libro.

La documentazione è organizzata per tema in pochi file canonici. I materiali metodologici originali restano in `source/`; le versioni precedenti sono recuperabili dalla cronologia Git.

## Stato

- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di produzione corrente: `main`
- Formato: Markdown
- Produzione: seriale, una candidatura completa alla volta
- Opera: unica e continua
- Capitoli pianificati: 98
- Appendici: 12
- Ultima passata di audit globale: **3 agosto 2026**
- Ultimo audit di continuità: **3 agosto 2026**

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
2. `06_CONTINUITA_TRA_CAPITOLI.md`;
3. `04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
4. `05_WORKFLOW_E_REPOSITORY.md`;
5. `03_VISUALI.md`, quando sono previste figure.

## Documenti canonici

| Documento | Funzione |
|---|---|
| `00_GOVERNANCE_E_ARCHITETTURA.md` | Contratto editoriale, opera unica, parti stabili, routing, maturità, ID, decisioni e governance. |
| `01_INDICE_EDITORIALE.md` | Struttura dei 98 capitoli e delle 12 appendici. |
| `02_STILE_E_QA_TESTO.md` | Metodo didattico, voce italiana, template del capitolo e review del testo. |
| `03_VISUALI.md` | Standard visivo, sfondo bianco, orientamento, palette, contenimento e QA. |
| `04_CODICE_FONTI_E_RIPRODUCIBILITA.md` | Gerarchia delle fonti, claim, citazioni, snippet, test, API e ambienti. |
| `05_WORKFLOW_E_REPOSITORY.md` | Struttura delle cartelle, produzione seriale, aggiornamenti U1-U8, commit e congelamento. |
| `06_CONTINUITA_TRA_CAPITOLI.md` | Contratti di ingresso e uscita, prerequisiti, forward reference e audit dei passaggi tra lezioni. |
| `14_CATALOGO_STATO_ARTE.md` | Registro dettagliato delle famiglie, tecniche, maturità e destinazioni editoriali. |
| `15_REGISTRO_RICERCHE_APPROFONDITE.md` | Dossier delle ricognizioni globali, fonti seme, limiti e date. |
| `source/README.md` | Indice dei materiali metodologici originali conservati integralmente. |

`06_CONTINUITA_TRA_CAPITOLI.md` resta separato perché possiede un ciclo di aggiornamento trasversale: una modifica a una lezione può richiedere di rileggere il capitolo precedente e quello successivo, anche quando nessuna regola di stile cambia.

## Alias di compatibilità

Due percorsi storici restano temporaneamente come brevi rinvii:

- `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md` rinvia a `00_GOVERNANCE_E_ARCHITETTURA.md`;
- `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md` rinvia a `05_WORKFLOW_E_REPOSITORY.md`.

Non sono documenti canonici e non ricevono nuove regole.

## Accuratezza

La versione approvata non contiene fatti basati su inferenze editoriali. Ogni affermazione portante richiede fonte primaria, documentazione ufficiale, standard, derivazione verificata o risultato riprodotto.

`CLAIMS.md` collega le frasi alle prove. `FONTI_PRIMARIE.md` registra sezioni, versioni e limiti.

## Prosa e continuità

Il capitolo deve leggersi come un manuale tecnico scritto direttamente in italiano. Lo scaffold resta in `PLAN.md` e `TEXT_AUDIT.md`; il lettore vede titoli semantici, paragrafi naturali e un esempio continuo.

Ogni capitolo supera review tecnica, review didattica, gate anti-template, review editoriale e linguistica, controllo per un lettore non esperto e nuova lettura integrale.

Ogni passaggio tra capitoli viene inoltre controllato per verificare che:

- i prerequisiti siano già stati costruiti oppure rispiegati localmente;
- una forward reference non diventi un prerequisito nascosto;
- apertura e riepilogo consegnino un oggetto chiaro;
- non esistano formule, termini o esercizi che richiedano contenuti futuri non segnalati.

## Visuali

Le immagini:

- usano sfondo bianco puro `#FFFFFF`;
- scelgono orientamento in base al contenuto;
- mantengono testo e simboli nei contenitori;
- non presentano frecce ambigue;
- condividono palette, box e tipografia;
- vengono revisionate e rigenerate;
- diventano `final.png` soltanto dopo approvazione tecnica e autoriale.

I generatori raster correnti sono in `../scripts/`; il workflow `generate-book-visuals.yml` produce e verifica i PNG candidati nel branch canonico.

## Codice

Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata. Python e PyTorch sono predefiniti. Un output è `Eseguito` soltanto quando possiede ambiente, comando e log o test.

## Stato della produzione

- Capitoli materializzati: `98/98`;
- Appendici materializzate: `12/12`;
- Visuali PNG attive: `196` nei capitoli e `208` includendo le 12 appendici, tutte referenziate;
- Audit strutturale e semantico: `98/98` capitoli senza problemi rilevati;
- Audit editoriale: `98/98` capitoli senza problemi automatici, `0` immagini problematiche, `0` formule non etichettate e `0` paragrafi duplicati;
- Profondità misurata: `2.159-3.402` parole nell'audit editoriale e `2.186-3.670` nell'audit generale;
- Visuali: `15` famiglie compositive principali, differenziate per concetto e non applicate come immagine standard a ogni capitolo;
- Codice: `166/166` test superati e `311/311` file Python compilati in memoria;
- Fonti: `419` fonti uniche e `502` collegamenti fonte-claim; `332` con contesto aperto, `127` con contesto parziale e `43` confermati tramite accesso web ufficiale;
- stato editoriale: candidature tecniche complete, non ancora approvate per la pubblicazione.

Restano aperti lettura ad alta voce, revisione per lettore non esperto, ricontrollo autoriale delle immagini, verifica fattuale delle fonti sensibili e congelamento dei file `final.png`. Il dettaglio tecnico dell'accesso alle fonti è in `source_verification_2026-08-03.json`; lo stato generale è in `../PROGRESS.md` e `../BOOK_PRODUCTION.md`.

## Regola per nuovi file in `docs/`

Un nuovo documento canonico viene creato soltanto quando il contenuto:

1. non appartiene chiaramente a uno dei temi esistenti;
2. sarebbe difficile da consultare come sezione del documento corrente;
3. possiede un ciclo di aggiornamento realmente indipendente;
4. viene approvato nella governance.

Per impostazione predefinita, una nuova regola viene aggiunta al documento tematico esistente.
