# Workflow operativo di ogni capitolo

## Scopo

Questo documento definisce l'ordine obbligatorio di produzione di ogni capitolo. Il processo è seriale e controllato. Non si passa al capitolo successivo finché quello corrente non ha superato i gate previsti oppure non è stato esplicitamente sospeso con problemi documentati.

La prima stesura, la prima immagine e il primo snippet sono sempre bozze.

## Unità di lavoro

L'unità di lavoro è un capitolo completo, non una raccolta di paragrafi indipendenti. Il capitolo deve integrare:

- testo verificato;
- formule e derivazioni ricontrollate;
- immagini approvate;
- snippet di codice eseguiti e testati;
- fonti e citazioni;
- registri di audit;
- esercizi e controlli di comprensione;
- commit di congelamento.

## Fase 0. Apertura del capitolo

Prima di svolgere ricerca o scrittura si crea la struttura:

```text
chapters/<NN_slug>/
  CHAPTER.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  PLAN.md
  code/
    README.md
    CODE_AUDIT.md
    outputs/
  assets/
```

Si registrano:

- numero e titolo;
- profilo del capitolo;
- obiettivo operativo;
- prerequisiti stabili;
- oggetto continuo;
- concetti differiti;
- data di apertura;
- stato iniziale `ricerca`.

## Fase 1. Definizione del perimetro

Si stabiliscono:

1. la domanda centrale del capitolo;
2. ciò che il lettore deve poter ricostruire alla fine;
3. ciò che il capitolo non copre;
4. il livello matematico necessario;
5. le varianti che verranno differite;
6. le sezioni che richiedono codice;
7. le visuali necessarie e la domanda unica di ciascuna.

Non si decide un numero fisso di figure. Ogni figura deve esistere perché una relazione spaziale, tensoriale, processuale o comparativa risulta più chiara visivamente. Ogni capitolo tecnico deve avere almeno una visuale portante approvata e almeno uno snippet eseguibile, salvo eccezione motivata per un capitolo intrinsecamente non computazionale.

## Fase 2. Ricerca delle fonti

La ricerca viene svolta prima della prosa portante.

Si consultano, in ordine di preferenza:

1. paper negli atti ufficiali;
2. versione ufficiale degli autori su arXiv;
3. technical report ufficiali;
4. documentazione ufficiale;
5. repository ufficiali;
6. standard e documenti istituzionali.

Per ogni fonte si registrano in `FONTI_PRIMARIE.md`:

- titolo;
- autori o organizzazione;
- data;
- versione, revisione o commit;
- URL o identificatore;
- sezioni rilevanti;
- affermazioni che la fonte può sostenere;
- limiti o divergenze;
- data effettiva di consultazione.

Le informazioni suscettibili di cambiamento vengono ricontrollate sul web nella stessa fase editoriale in cui il capitolo viene approvato.

## Fase 3. Registro delle affermazioni

Prima della stesura si costruisce `CLAIMS.md`.

Ogni affermazione portante riceve un ID stabile e uno dei seguenti tipi:

- `fonte primaria`;
- `derivazione`;
- `risultato eseguito`;
- `illustrativo`;
- `confine`.

Una voce deve contenere:

```text
ID:
Affermazione esatta:
Tipo:
Fonte o prova:
Sezione, pagina o simbolo rilevante:
Versione o data:
Controllo indipendente:
Esito:
Note:
```

Un'affermazione senza prova resta `aperta` e non viene trasformata in una frase assertiva.

Le inferenze editoriali non sono un tipo ammesso nella versione approvata. Una derivazione matematica è ammessa soltanto se i passaggi sono espliciti e verificati.

## Fase 4. Piano didattico

Il piano segue il metodo in `EXPLANATION_STYLE_AND_VISUALS.md`.

Per ogni transizione si compila:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```

Ogni sezione importante deve identificare:

```text
Dove siamo:
Problema:
Input e shape:
Trasformazione:
Output e shape:
Cosa è cambiato:
Cosa è rimasto invariato:
Cosa non fa:
Cosa usa l'output dopo:
Esempio minimo:
Errore comune:
Frase di continuità:
```

L'ordine di introduzione è:

```text
domanda concreta
-> esempio numerico o oggetto osservabile
-> tabella o shape
-> pseudocodice
-> formula
-> derivazione, quando necessaria
-> codice eseguibile verificato
-> varianti e ottimizzazioni
```

## Fase 5. Storyboard delle visuali

Per ogni figura si crea una scheda conforme a `02_TEMPLATE_VISUALE.md`.

La specifica deve dichiarare:

- domanda unica;
- stato prima;
- trasformazione nuova;
- stato dopo;
- nodi;
- frecce con sorgente e consumer esatti;
- shape;
- valori illustrativi o misurati;
- invariante;
- confine;
- prossimo consumer;
- alt text;
- equivalente testuale;
- ordine di lettura.

Le immagini vengono prodotte con lo strumento immagini. Gli SVG non sono l'artefatto editoriale principale.

La prima generazione è sempre `bozza v1`. Ogni versione viene sottoposta al protocollo in `03_PROTOCOLLO_QA_VISUALE.md`. Non si passa alla figura successiva finché quella corrente non è approvata o esplicitamente rimandata con un problema documentato.

## Fase 6. Prima stesura

La prima stesura:

- segue l'oggetto continuo;
- inserisce le citazioni nel punto in cui l'affermazione compare;
- mantiene distinte fonte, derivazione, esempio e risultato eseguito;
- non anticipa termini, formule, codice o varianti;
- non usa metafore o personificazioni;
- non colma lacune con contenuto plausibile ma non verificato.

Quando le fonti non consentono una formulazione certa, la sezione resta aperta oppure viene ridotta a ciò che è verificabile.

## Fase 7. Progettazione e implementazione del codice

Per ogni snippet si definiscono:

- ID;
- sezione;
- domanda;
- input noto;
- shape;
- operazione centrale;
- output osservabile;
- invariante;
- ambiente;
- fonte API ufficiale;
- file completo;
- test.

La forma predefinita è uno snippet breve e autosufficiente. Gli script lunghi restano nel repository quando sono necessari per esperimenti, benchmark, training o hardware specifico.

Il codice viene:

1. controllato sulla documentazione ufficiale;
2. ispezionato staticamente;
3. eseguito in un processo pulito;
4. testato sugli invarianti;
5. confrontato con una formula diretta, NumPy o un'API ufficiale quando possibile;
6. rieseguito dopo ogni correzione.

Gli output mostrati come `Eseguito` devono avere log o test associati.

## Fase 8. Audit fattuale del testo

Si applica `04_PROTOCOLLO_QA_TESTO.md` frase per frase.

Per ogni periodo tecnico si controllano:

- prova disponibile;
- corrispondenza reale tra fonte e formulazione;
- condizioni e limiti;
- distinzione tra paper, documentazione, repository, checkpoint e prodotto;
- terminologia;
- data e versione;
- eventuali divergenze tra fonti.

Una citazione non valida non viene sostituita con una citazione generica. La frase viene corretta, ristretta o rimossa.

## Fase 9. Audit matematico e numerico

Si ricontrollano:

- simboli;
- domini;
- shape;
- segni;
- fattori di scala;
- normalizzazioni;
- arrotondamenti;
- esempi numerici;
- condizioni di validità;
- complessità computazionale e memoria.

Quando possibile, i numeri vengono ricalcolati tramite uno script indipendente.

## Fase 10. Audit architetturale e algoritmico

Si verifica l'ordine effettivo delle operazioni e la collocazione di:

- normalizzazioni;
- residual connection;
- mask;
- routing;
- caching;
- loss;
- gradienti;
- update;
- sampling e decoding;
- comunicazione distribuita.

Una proprietà di un paper non viene estesa automaticamente a una famiglia di modelli, a una libreria o a una versione successiva.

## Fase 11. Audit incrociato testo, immagini e codice

Si confrontano direttamente:

- nomi dei tensor;
- shape;
- numeri;
- formule;
- ordine delle operazioni;
- semantica delle mask;
- parametri;
- output;
- invarianti;
- confini.

Una contraddizione tra i tre livelli blocca il capitolo.

## Fase 12. Audit temporale

Prima dell'approvazione si ricontrollano sul web:

- versione corrente della documentazione;
- firme delle API;
- release e commit;
- revisioni o errata dei paper;
- technical report più recenti;
- stato dei modelli e dei repository;
- benchmark citati;
- eventuali cambiamenti normativi.

Il capitolo registra una data di congelamento editoriale. Non afferma di essere aggiornato oltre quella data.

## Fase 13. Audit didattico

Dopo l'accuratezza tecnica si controlla che:

- ogni sezione parta dall'output della precedente;
- venga introdotto un solo concetto nuovo per transizione;
- termini e formule compaiano dopo il referente concreto;
- il codice compaia dopo il meccanismo;
- varianti e ottimizzazioni compaiano dopo il caso base;
- cambiamento, invariante e confine siano espliciti;
- la semplificazione non renda falsa la spiegazione;
- il lettore possa ricostruire, localizzare, delimitare, trasferire e variare il meccanismo.

## Fase 14. Seconda lettura completa

Dopo tutte le correzioni il capitolo viene riletto integralmente. Non si verificano soltanto i difetti già individuati.

La seconda lettura include:

- prosa;
- citazioni;
- formule;
- immagini;
- alt text;
- snippet;
- output;
- test;
- esercizi;
- bibliografia;
- registri di audit.

## Fase 15. Revisione autoriale

Il capitolo passa allo stato `revisione autoriale` soltanto dopo aver superato i gate tecnici.

La revisione umana può richiedere:

- cambi di tono;
- maggiore o minore profondità;
- nuova sequenza didattica;
- ulteriori figure;
- sostituzione di esempi;
- nuove fonti;
- correzioni tecniche.

Ogni modifica che tocca contenuto, immagine o codice riapre i relativi audit.

## Fase 16. Congelamento

Un capitolo può essere marcato `approvato` soltanto quando:

- `CLAIMS.md` non contiene affermazioni portanti aperte;
- `TEXT_AUDIT.md` è positivo;
- `CODE_AUDIT.md` è positivo;
- tutte le immagini incluse sono approvate;
- le informazioni recenti sono state ricontrollate;
- testo, immagini e codice sono coerenti;
- la revisione autoriale è conclusa.

Si registrano:

- data di congelamento;
- commit SHA;
- versioni degli ambienti;
- fonti finali;
- problemi noti non bloccanti;
- eventuali sezioni rinviate.

## Stati ammessi

```text
ricerca
-> pianificazione
-> bozza
-> revisione fattuale
-> revisione matematica
-> revisione codice
-> revisione visuale
-> revisione incrociata
-> revisione didattica
-> revisione autoriale
-> approvato
```

Uno stato può retrocedere quando una correzione invalida un gate già superato.

## Regola di arresto

Se emerge un dubbio non risolvibile con le fonti disponibili, non si procede inventando una continuità. Si registra il problema, si restringe l'affermazione oppure si sospende la sezione fino a nuova evidenza.