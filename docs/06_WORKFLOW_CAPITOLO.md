# Workflow operativo di ogni capitolo

## Scopo

Il processo è seriale e controllato. La prima stesura, la prima immagine e il primo snippet sono sempre bozze.

L'unità di lavoro è un capitolo completo con testo, formule, fonti, immagini, codice, test, esercizi e audit.

## Fase 0. Apertura

Creare:

```text
chapters/<slug>/
  PLAN.md
  CHAPTER.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
  assets/
```

Registrare `chapter_id`, parte, profilo, domanda centrale, prerequisiti, oggetto continuo, concetti differiti, data e stato `ricerca`.

I metadati destinati al repository vengono conservati in commenti non renderizzati o negli artefatti interni.

## Fase 1. Perimetro

Stabilire:

- ciò che il lettore deve ricostruire;
- ciò che il capitolo non copre;
- matematica necessaria;
- codice richiesto;
- visuali necessarie;
- capitolo o passaggio successivo.

Non si decide un numero fisso di figure. Ogni capitolo tecnico include almeno una visuale portante e uno snippet, salvo eccezione motivata.

## Fase 2. Ricerca delle fonti

Consultare, in ordine di preferenza:

1. paper negli atti ufficiali;
2. versione ufficiale degli autori;
3. technical report;
4. documentazione ufficiale;
5. repository ufficiali;
6. standard e documenti istituzionali.

Registrare versione, data, sezioni rilevanti, affermazioni sostenibili e limiti.

## Fase 3. Registro dei claim

Costruire `CLAIMS.md` prima della prosa. Ogni affermazione portante riceve un ID e una prova. Una voce aperta non diventa una frase assertiva.

## Fase 4. Scaffold didattico interno

In `PLAN.md`, per ogni transizione portante, registrare:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Input e shape:
Operazione:
Output e shape:
Cosa cambia:
Cosa resta invariato:
Cosa non fa:
Consumer successivo:
Esempio o prova:
Errore comune:
Giunzione:
```

Lo scaffold è obbligatorio per progettazione e review. Non viene copiato come struttura standard di `CHAPTER.md`.

## Fase 5. Storyboard delle visuali

Per ogni figura creare `SPEC.md` con domanda, famiglia, orientamento, nodi, frecce, shape, valori, invariante, confine, ordine di lettura e alt text.

Applicare `17_STANDARD_VISIVO_CANONICO.md`, `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md` e `03_PROTOCOLLO_QA_VISUALE.md`.

## Fase 6. Prima stesura

`CHAPTER.md`:

- segue l'oggetto continuo;
- usa titoli semantici;
- organizza le sezioni attorno a problemi e meccanismi;
- integra stato, trasformazione, output, invariante e confine nei paragrafi;
- non espone lo scaffold;
- separa il testo pubblico dai metadati;
- inserisce le citazioni vicino alle affermazioni;
- distingue fonti, derivazioni, esempi e risultati;
- non anticipa termini, formule, codice o varianti;
- usa un italiano tecnico naturale.

Applicare `19_STRUTTURA_LOGICA_IN_PROSA.md` e `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

## Fase 7. Codice

Per ogni snippet definire ID, domanda, input, shape, operazione, output, invariante, ambiente, fonte API e test.

Verificare la documentazione ufficiale, eseguire in un processo pulito, testare gli invarianti e rieseguire dopo ogni modifica.

Nel capitolo, input, operazione centrale e controllo atteso vengono introdotti in prosa. Il contratto completo resta negli artefatti del codice.

## Fase 8. Audit fattuale

Controllare frase per frase prova, limiti, terminologia, versioni e distinzione tra paper, implementazione, checkpoint e prodotto.

## Fase 9. Audit matematico

Ricontrollare simboli, domini, shape, segni, scaling, normalizzazioni, arrotondamenti, esempi, complessità e condizioni di validità.

## Fase 10. Audit architetturale e algoritmico

Verificare l'ordine reale di normalizzazioni, residual connection, mask, routing, cache, loss, gradienti, update, sampling e comunicazione.

## Fase 11. Audit incrociato

Confrontare testo, formule, figure e codice per nomi, shape, numeri, ordine, mask, parametri, output, invarianti e confini. Una contraddizione blocca il capitolo.

## Fase 12. Audit temporale

Prima dell'approvazione ricontrollare documentazione, API, release, commit, report, benchmark e normative pertinenti. Registrare la data di congelamento.

## Fase 13. Review didattica

Applicare `18_PROTOCOLLO_QA_DIDATTICO.md`:

- oggetto continuo;
- catena causale;
- gate di termini, formule, codice e varianti;
- trasformazione dominante;
- visuali integrate;
- confini e concetti differiti.

Se emerge un difetto bloccante, registrarlo, correggere gli artefatti coinvolti e ripetere la review.

## Fase 14. Gate anti-template

Rileggere il capitolo senza consultare il piano e verificare:

- titoli legati al contenuto;
- sezioni abbastanza ampie;
- assenza di intestazioni metacognitive ripetute;
- continuità tra paragrafi;
- shape e confini ancora espliciti;
- separazione tra manuale e materiali operativi.

## Fase 15. Review editoriale e linguistica

Applicare `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

Controllare:

- fluidità;
- italiano idiomatico;
- calchi e ibridi;
- ritmo delle frasi;
- densità dei paragrafi;
- cautele ripetute;
- uso di elenchi, tabelle e box;
- continuità dell'esempio;
- leggibilità delle citazioni;
- lettura ad alta voce.

La review simula un lettore nuovo, un lettore tecnico e un lettore che riprende il capitolo dopo tempo.

## Fase 16. Seconda lettura completa

Dopo le correzioni, rileggere integralmente il capitolo, senza usare il piano come spiegazione implicita.

La lettura comprende:

- prosa;
- formule;
- visuali;
- codice;
- esercizi;
- fonti;
- audit.

Non può limitarsi a confermare i difetti già trovati.

## Fase 17. Revisione autoriale

Il capitolo passa a revisione autoriale soltanto quando:

- i claim sono verificati;
- audit fattuale, matematico, codice e visuali sono positivi;
- review didattica superata;
- gate anti-template superato;
- review linguistica superata;
- lettura ad alta voce superata;
- ogni difetto bloccante corretto;
- nuova lettura integrale completata.

Modifiche autoriali strutturali riaprono gli audit pertinenti.

## Fase 18. Congelamento

Un capitolo approvato riceve:

- data di congelamento;
- commit SHA;
- testo esatto;
- fonti e claim;
- immagini finali;
- codice, test, output e ambiente;
- audit completati.

Non si passa al capitolo successivo prima del congelamento o di una sospensione documentata.
