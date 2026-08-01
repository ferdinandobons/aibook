# Workflow, aggiornamenti e struttura del repository

## Stato

- Stato: `vincolante`
- Modalità: produzione seriale controllata
- Unità di lavoro: un capitolo completo
- Prima stesura, prima immagine e primo snippet: sempre bozze

## 1. Principio operativo

Un capitolo integra testo, formule, fonti, claim, immagini, codice, test, esercizi e audit. Non si passa al capitolo successivo finché l'unità corrente non viene approvata oppure sospesa con problemi documentati.

Un aggiornamento non è una modifica isolata a un Markdown. Può coinvolgere:

```text
catalogo
-> collocazione
-> fonti
-> claim
-> testo
-> formule
-> codice
-> visuali
-> audit
-> indice
-> governance
-> commit
```

## 2. Albero principale

```text
/
  README.md
  GUIDELINE.md
  PROGRESS.md
  BOOK_PRODUCTION.md
  docs/
  chapters/
  assets/
  scripts/
  tests/
```

## 3. Documentazione canonica

```text
docs/
  README.md
  00_GOVERNANCE_E_ARCHITETTURA.md
  01_INDICE_EDITORIALE.md
  02_STILE_E_QA_TESTO.md
  03_VISUALI.md
  04_CODICE_FONTI_E_RIPRODUCIBILITA.md
  05_WORKFLOW_E_REPOSITORY.md
  14_CATALOGO_STATO_ARTE.md
  15_REGISTRO_RICERCHE_APPROFONDITE.md
  source/
```

`source/` conserva copie archivistiche dei materiali originali. Nessuna regola vincolante deve esistere soltanto in una conversazione o in un file esterno.

## 4. Cartella del capitolo

```text
chapters/<NN_slug>/
  CHAPTER.md
  PLAN.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
    README.md
    CODE_AUDIT.md
    outputs/
    environments/
  assets/
    README.md
```

### Funzioni

- `CHAPTER.md`: testo destinato al lettore, con metadati non renderizzati.
- `PLAN.md`: oggetto continuo, transizioni, visuali, snippet e rischi.
- `FONTI_PRIMARIE.md`: fonti, versioni, sezioni, claim sostenibili e limiti.
- `CLAIMS.md`: registro frase-prova.
- `TEXT_AUDIT.md`: audit fattuale, matematico, didattico, editoriale e linguistico.
- `CHANGELOG.md`: modifiche sostanziali.
- `REVIEW.md`: guida alla revisione autoriale.

## 5. Asset visuali

```text
assets/chapters/<NN_slug>/<FIG-ID>/
  candidate-vN.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

Dopo approvazione:

```text
assets/chapters/<NN_slug>/<FIG-ID>/
  final.png
  SPEC.md
  AUDIT.md
  ALT_TEXT.md
```

`final.png` esiste soltanto dopo approvazione tecnica e autoriale.

## 6. Identificatori

### Visuali

```text
<SIGLA>-<NN>
```

Esempio: `ATT-01`.

### Claim

```text
CLM-<SIGLA>-<NNN>
```

### Snippet

```text
SNIP-<SIGLA>-<NNN>
```

### Fonti

```text
SRC-<SIGLA>-<NNN>
```

Gli ID non vengono riutilizzati per oggetti diversi.

## 7. Nomi e convenzioni

- cartelle e file tecnici in ASCII;
- slug minuscoli con underscore;
- Markdown per testo e documentazione;
- PNG per visuali finali;
- Python per snippet eseguibili;
- nessuno spazio nei nomi di asset e script;
- ID stabili separati dal numero visualizzato del capitolo.

## 8. Workflow di un capitolo

### Fase 0. Apertura

Creare la cartella e registrare:

- `chapter_id`;
- parte e profilo;
- domanda centrale;
- prerequisiti;
- oggetto continuo;
- concetti differiti;
- data;
- stato `research`.

### Fase 1. Perimetro

Stabilire:

- ciò che il lettore deve ricostruire;
- ciò che il capitolo non copre;
- livello matematico;
- codice richiesto;
- visuali necessarie;
- capitolo o componente successivo.

Non si decide un numero fisso di figure. Ogni figura deve risolvere una relazione che diventa più chiara visivamente. Ogni capitolo tecnico include almeno uno snippet, salvo eccezione motivata.

### Fase 2. Ricerca

Consultare, in ordine di preferenza:

1. atti ufficiali o riviste;
2. versione ufficiale degli autori;
3. technical report;
4. documentazione ufficiale;
5. repository ufficiale;
6. standard e documenti istituzionali.

Registrare versione, data, sezioni, claim sostenibili e limiti.

### Fase 3. Claim

Costruire `CLAIMS.md` prima della prosa. Una voce aperta non diventa frase assertiva.

### Fase 4. Piano didattico

Compilare in `PLAN.md` oggetto continuo, transizioni, input, output, invarianti, confini, errori e giunzioni. Lo scaffold non viene copiato come struttura del capitolo.

### Fase 5. Storyboard

Per ogni visuale creare `SPEC.md` con domanda, famiglia, orientamento, nodi, frecce, shape, valori, invariante, confine, label e alt text.

### Fase 6. Prima stesura

`CHAPTER.md`:

- segue l'oggetto continuo;
- usa titoli semantici;
- integra stato, problema, trasformazione, output, invariante e confine nella prosa;
- inserisce citazioni vicino ai claim;
- distingue fonte, derivazione, esempio e risultato eseguito;
- non anticipa termini, formule, codice o varianti;
- non espone metadati e audit;
- segue la voce editoriale italiana.

### Fase 7. Codice

Per ogni snippet definire domanda, input, shape, operazione, output, invariante, ambiente, fonte API e test.

Verificare documentazione, eseguire in processo pulito, testare invarianti e rieseguire dopo le modifiche.

### Fase 8. Visuali

Generare una bozza, eseguire audit tecnico, stilistico, compositivo e di contenimento. Rigenerare finché non restano difetti bloccanti.

### Fase 9. Audit fattuale

Controllare frase per frase prova, limiti, terminologia, versioni e distinzione tra paper, implementazione, checkpoint e prodotto.

### Fase 10. Audit matematico

Ricontrollare simboli, domini, shape, segni, scaling, normalizzazioni, arrotondamenti, esempi, complessità e condizioni.

### Fase 11. Audit algoritmico

Verificare l'ordine reale di normalizzazioni, residual, mask, routing, cache, loss, gradienti, update, sampling e comunicazione.

### Fase 12. Audit incrociato

Confrontare testo, formule, figure e codice per nomi, shape, numeri, ordine, mask, parametri, output, invarianti e confini.

### Fase 13. Audit temporale

Ricontrollare documentazione, API, release, commit, report, benchmark e normative. Registrare la data.

### Fase 14. Review didattica

Controllare oggetto continuo, gate di comparsa, progressione, visuali, confini e anti-template. Un difetto bloccante riapre il lavoro.

### Fase 15. Review editoriale e linguistica

Rileggere il capitolo come manuale, con tre profili di lettore e prova ad alta voce. Correggere frammentazione, calchi, ritmo, ripetizioni e materiali operativi esposti.

### Fase 16. Seconda lettura completa

Dopo le correzioni, rileggere integralmente testo, formule, visuali, codice, esercizi, fonti e rinvii. La review non si limita ai difetti precedenti.

### Fase 17. Revisione autoriale

Il capitolo passa all'autore soltanto quando:

- claim verificati;
- audit tecnici positivi;
- visuali validate;
- codice testato;
- review didattica superata;
- gate anti-template superato;
- review linguistica e lettura ad alta voce superate;
- controllo incrociato positivo.

### Fase 18. Congelamento

La versione approvata riceve:

- data di congelamento;
- commit SHA;
- testo esatto;
- fonti e claim;
- immagini finali;
- codice, test, output e ambiente;
- audit completati.

## 9. Stati editoriali

```text
planned
research
draft
technical-review
didactic-review
editorial-review
author-review
approved
suspended
```

## 10. Tipi di aggiornamento

### U1. Nuova tecnica o architettura

Per un meccanismo non ancora registrato.

### U2. Nuova evidenza

Quando un paper, report, benchmark o repository cambia la comprensione o la maturità.

### U3. API o implementazione

Quando cambia firma, backend, comportamento o versione supportata.

### U4. Maturità

Per promozione o demozione tra `FRONTIER`, `ESTABLISHED` e `CORE`.

### U5. Nuovo capitolo

Quando una sezione non contiene più correttamente il materiale.

### U6. Split o merge

Quando i confini didattici di capitoli esistenti non funzionano.

### U7. Correzione tecnica

Per errori in testo, formula, codice, visuale, fonte o classificazione.

### U8. Nuova edizione

Per nuova ricerca globale, numerazione, snapshot ed export.

## 11. Procedura U1. Nuova tecnica

### Identificazione

```text
Nome provvisorio:
Problema risolto:
Oggetto modificato:
Input:
Operazione:
Output:
Invariante:
Confine:
Prima fonte primaria:
Data:
```

### Verifica della novità

Controllare che non sia:

- rinominazione di un meccanismo esistente;
- configurazione di iperparametri;
- combinazione di tecniche già coperte;
- risultato di un solo prodotto senza descrizione sufficiente;
- modifica implementativa appartenente ai sistemi.

### Ricerca

Raccogliere paper o report originale, repository o documentazione, versione, sezioni, limiti ed errata.

Una sola fonte può bastare per registrare una voce `FRONTIER`, non per generalizzarla.

### Routing

Registrare:

```text
part_id primario:
capitolo candidato:
tag secondari:
prerequisiti:
consumer successivi:
```

### Maturità iniziale

Una tecnica nuova entra normalmente come `FRONTIER`. Può entrare `ESTABLISHED` se esistono adozioni, repliche o più fonti convergenti. `CORE` richiede motivazione esplicita nella governance.

### Destinazione

Scegliere:

- voce nel catalogo;
- sottosezione;
- approfondimento;
- studio di caso;
- nuovo capitolo candidato;
- osservatorio in attesa di evidenza.

### File coinvolti

Aggiornare catalogo, indice quando necessario, registro della ricerca, governance e dossier del capitolo.

## 12. Procedura U2. Nuova evidenza

1. Aprire la voce nel catalogo.
2. Riaprire le fonti già usate.
3. Leggere la nuova fonte nel contesto originale.
4. Confrontare definizioni, setup, benchmark e condizioni.
5. Registrare convergenze e divergenze.
6. Aggiornare i claim.
7. Riaprire audit coinvolti.
8. Aggiornare la data.
9. Non cambiare maturità automaticamente.

## 13. Procedura U3. API o implementazione

1. Identificare la versione descritta.
2. Consultare documentazione e release note.
3. Distinguere incompatibilità, deprecazione e nuova funzione.
4. Aggiornare lo snippet in bozza.
5. Eseguire in ambiente pulito.
6. Rieseguire i test.
7. Salvare ambiente, comando e output.
8. Aggiornare testo e visuali dopo la verifica.
9. Conservare note sulla versione precedente quando necessario.

## 14. Procedura U4. Maturità

Scheda:

```text
Topic ID:
Stato precedente:
Stato proposto:
Data:
Nuove fonti:
Adozioni o repliche:
Terminologia:
Failure mode:
Motivazione:
Impatto:
Reviewer:
```

La promozione richiede evidenza aggiuntiva, fonti convergenti, trade-off e failure mode documentati. Non cambia automaticamente parte, ID o ordine.

## 15. Procedura U5. Nuovo capitolo

Un capitolo è giustificato quando:

1. esiste una domanda didattica autonoma;
2. il meccanismo ha input, operazione, output, invariante e confine propri;
3. una sottosezione renderebbe il capitolo ospite troppo denso;
4. esistono fonti sufficienti;
5. è possibile progettare una visuale non ridondante;
6. è possibile creare uno snippet o motivarne l'assenza;
7. prerequisiti e capitolo successivo sono identificati.

Riceve ID semantico stabile e numero di edizione.

## 16. Procedura U6. Split o merge

Prima di procedere:

- identificare la giunzione didattica difettosa;
- verificare che non bastino sezione o prerequisito;
- mappare claim, fonti, visuali e snippet;
- definire alias e redirect;
- aggiornare i riferimenti;
- registrare la decisione.

Nessun file viene cancellato prima della verifica della migrazione.

## 17. Procedura U7. Correzione

1. Bloccare l'approvazione.
2. Registrare l'errore.
3. Identificare la fonte del difetto.
4. Correggere il minimo insieme coerente di artefatti.
5. Ripetere l'audit completo pertinente.
6. Cercare propagazioni dello stesso errore.
7. Registrare un commit descrittivo.

## 18. Procedura U8. Nuova edizione

1. Eseguire una ricerca globale.
2. Rivedere catalogo e maturità.
3. Controllare dipendenze.
4. Aggiornare indice e numerazione.
5. Conservare ID e alias.
6. Ricontrollare norme, API e modelli recenti.
7. Rieseguire i test.
8. Verificare gli asset.
9. Registrare data e commit.
10. Produrre la mappa delle differenze.

## 19. Ricerca periodica

Frequenza minima:

- ricerca locale prima di ogni capitolo;
- controllo recente prima dell'approvazione;
- revisione delle voci `FRONTIER` almeno ogni 90 giorni durante la produzione;
- ricerca globale prima di una nuova edizione;
- ricerca straordinaria per una nuova famiglia o modifica normativa rilevante.

La ricerca globale copre almeno dati, scaling, architetture, post-training, reasoning, multimodalità, retrieval, agenti, compressione, serving, valutazione, sicurezza e governance.

## 20. Commit

I commit descrivono l'unità di cambiamento.

Esempi:

```text
Add primary source dossier for attention scoring
Add and test minimal attention snippet
Record rejection of ATT-03 after connection audit
Approve ATT-01 after visual QA
Complete editorial review of Chapter 28
Freeze Chapter 28 editorial version
```

Non si dichiara approvazione quando l'audit non è completo.

## 21. Congelamento e ricostruibilità

Il commit di congelamento deve identificare:

- testo;
- fonti;
- claim;
- immagini finali;
- codice e test;
- output;
- ambienti;
- audit;
- data editoriale.

`PROGRESS.md` riporta lo stato sintetico e non sostituisce gli audit.

## 22. Modifiche alla documentazione

Quando una decisione modifica più regole:

1. aggiornare `00_GOVERNANCE_E_ARCHITETTURA.md`;
2. aggiornare i documenti specialistici;
3. aggiornare `README.md` di `docs/`;
4. controllare i riferimenti;
5. aggiornare root `GUIDELINE.md`, `README.md` e `PROGRESS.md` quando necessario;
6. registrare il commit;
7. riprendere la produzione soltanto dopo la coerenza documentale.
