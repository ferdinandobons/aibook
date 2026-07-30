# Voce editoriale e revisione linguistica del manuale

## Stato

- Stato: `vincolante`
- Ambito: ogni capitolo, appendice e testo destinato al lettore
- Documenti collegati: `EXPLANATION_STYLE_AND_VISUALS.md`, `01_TEMPLATE_CAPITOLO.md`, `04_PROTOCOLLO_QA_TESTO.md`, `18_PROTOCOLLO_QA_DIDATTICO.md`, `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Artefatto di registrazione: `chapters/<capitolo>/TEXT_AUDIT.md`

## 1. Obiettivo

Il libro è un manuale tecnico, non una specifica, un registro di audit o una raccolta di schede. La verifica resta rigorosa negli artefatti interni; il testo destinato al lettore deve invece risultare continuo, leggibile e naturale in italiano.

Una buona lezione permette al lettore di seguire un ragionamento senza percepire continuamente il processo con cui il testo è stato controllato. La prosa deve nascondere lo scaffold senza nascondere la logica.

## 2. Separazione tra testo pubblico e materiali operativi

`CHAPTER.md` contiene il materiale destinato alla lettura:

- titolo e apertura;
- spiegazione;
- formule e tabelle necessarie;
- visuali tecniche;
- snippet essenziali;
- riepilogo, controlli ed esercizi;
- riferimenti principali e collegamenti ai materiali riproducibili.

I seguenti elementi non appartengono al flusso del manuale:

- stato editoriale;
- versione candidata;
- data di apertura;
- esito degli audit;
- nomi delle immagini respinte;
- note sulla pull request;
- commit e branch;
- elenco completo dei file di lavorazione;
- dettagli di riproducibilità che non servono a comprendere il meccanismo.

Questi dati restano in commenti non renderizzati, front matter, `PLAN.md`, `TEXT_AUDIT.md`, `CHANGELOG.md`, `REVIEW.md` o nei file del codice.

## 3. Architettura delle sezioni

Le sezioni seguono domande, problemi e meccanismi reali. Non si crea una nuova sezione per ogni micro-passaggio.

Una sezione principale è giustificata quando cambia almeno uno dei seguenti elementi:

- la domanda a cui il testo risponde;
- l'oggetto osservato;
- il livello di astrazione;
- la fase del processo;
- il tipo di evidenza;
- il consumer del risultato.

Una singola sezione può contenere più passaggi brevi se appartengono allo stesso movimento concettuale. In un capitolo tecnico ordinario, da cinque a dieci sezioni principali costituiscono un riferimento editoriale, non un limite rigido.

Sono segnali di frammentazione:

- sezioni di uno o due paragrafi ripetute molte volte;
- un titolo per ogni operazione aritmetica;
- sequenze `definizione -> cautela -> nuovo titolo`;
- titoli che descrivono il metodo di scrittura invece del contenuto.

## 4. Costruzione del paragrafo

Un paragrafo non deve ridursi a una singola funzione amministrativa. Può collegare in modo naturale:

1. lo stato raggiunto;
2. il problema rimasto;
3. il nuovo passaggio;
4. la conseguenza;
5. il limite necessario;
6. il collegamento con ciò che segue.

Esempio:

```text
I tre prodotti scalari forniscono uno score per ogni key, ma questi valori non sono ancora coefficienti: possono essere negativi e non sommano a uno. Li dividiamo quindi per la radice della dimensione delle key e applichiamo la softmax. Otteniamo tre coefficienti associati alle stesse coppie key-value; soltanto a questo punto possiamo usarli per costruire l'output.
```

Il paragrafo conserva la sequenza tecnica, ma non espone una lista di campi.

## 5. Ritmo e periodo

La prosa alterna periodi brevi, medi e più articolati. Una successione di frasi tutte della stessa lunghezza produce un ritmo meccanico; periodi eccessivamente lunghi rendono invece difficile localizzare l'operazione principale.

Regole operative:

- una frase esprime una relazione principale;
- condizioni ed eccezioni vengono separate quando competono con il meccanismo centrale;
- soggetto e verbo restano vicini quando la frase contiene più tensor o componenti;
- le liste vengono usate quando l'ordine o il confronto lo richiedono, non per evitare la prosa;
- le transizioni variano nella forma e nominano sempre l'oggetto ottenuto.

Non è obbligatorio iniziare ogni passaggio con `Ora che`, `A questo punto` o `Quindi`.

## 6. Italiano idiomatico

Il testo deve sembrare scritto in italiano, non tradotto da una documentazione inglese.

Evitare, quando non sono termini tecnici necessari:

- `consumer`;
- `ancora operativa`;
- `dimensione da annotare`;
- `meccanismo stabilizzato`;
- `contratto algoritmico`;
- `ambiente registrato`;
- `obiettivo modellato`;
- `ampiezza del riuso`.

Forme preferibili:

```text
riferimento operativo
aspetto da osservare
meccanismo appena costruito
ordine delle operazioni
ambiente in cui il codice è stato eseguito
risultato o relazione descritta dal modello
varietà dei compiti e dei contesti d'uso
```

I termini inglesi standard restano in inglese quando questa è la forma tecnica corrente, per esempio `token`, `embedding`, `attention`, `training`, `inference`, `checkpoint`, `loss`, `optimizer`, `batch` e `shape`. La frase che li contiene deve però restare italiana nella sintassi.

## 7. Precisione senza rigidità

Una formulazione precisa non deve suonare burocratica. Il testo dichiara condizioni e limiti, ma evita di interrompere ogni passaggio con una nuova cautela.

Le precisazioni vengono gestite in questo ordine:

1. condizione indispensabile nel punto in cui serve;
2. breve nota o box `Da non confondere`;
3. approfondimento rinviato;
4. dettaglio completo negli audit o negli artefatti.

La stessa cautela non viene ripetuta nella spiegazione, nel riepilogo e nella sezione degli errori, salvo che la ripetizione abbia una funzione didattica distinta.

## 8. Esempi come filo narrativo

L'esempio continuo non viene usato soltanto all'inizio e alla fine. Ogni nuova distinzione importante viene applicata all'oggetto che il lettore conosce già.

Quando il capitolo passa a una definizione astratta, la prosa torna subito al caso concreto:

```text
Nel nostro sistema di assistenza, questa distinzione significa che...
```

Se l'esempio numerico usa oggetti concettualmente diversi con valori identici, il testo dichiara esplicitamente che l'uguaglianza serve soltanto a semplificare i conti.

## 9. Citazioni e riproducibilità

Le citazioni restano vicino alle affermazioni che sostengono. I dettagli che interrompono il ragionamento vengono spostati in note o nei file di riproduzione.

Nel corpo sono sufficienti, quando non serve altro:

- fonte e anno;
- versione dell'API rilevante;
- risultato necessario a comprendere il passaggio.

Restano negli artefatti:

- sistema operativo;
- commit;
- comando completo;
- log;
- tolleranze;
- versione eseguita e versione documentata;
- limitazioni dell'hardware.

Il testo principale può rinviare a questi elementi con una frase breve.

## 10. Metadati e stato editoriale

I metadati possono essere conservati in un commento HTML all'inizio di `CHAPTER.md` oppure in un file separato. Non vengono mostrati nella versione editoriale.

Formato consigliato:

```text
<!--
chapter_id:
part_id:
version:
status:
last_source_check:
environment:
deferred:
-->
```

Il capitolo non apre con `Stato della candidatura` e non chiude con `Registro di approvazione`. Questi elementi appartengono agli audit.

## 11. Review linguistica obbligatoria

Dopo la review tecnica e didattica viene eseguita una review editoriale e linguistica completa.

Il reviewer legge il capitolo come un manuale e controlla:

- fluidità tra paragrafi e sezioni;
- naturalezza dell'italiano;
- eventuali calchi dall'inglese;
- ripetizioni sintattiche;
- densità dei sostantivi astratti;
- frequenza delle formulazioni negative;
- ritmo delle frasi;
- eccesso di titoli, tabelle, liste e blocchi;
- separazione tra testo pubblico e materiali operativi;
- leggibilità delle citazioni;
- continuità dell'esempio;
- comprensibilità a una lettura ad alta voce.

La lettura ad alta voce è un gate. Una frase che risulta difficile da pronunciare, che richiede di tornare indietro o che suona come una specifica viene riscritta anche quando è grammaticalmente corretta.

## 12. Review dal punto di vista del lettore

La review simula almeno tre lettori:

1. **lettore che incontra il concetto per la prima volta**, per verificare prerequisiti e continuità;
2. **lettore tecnico**, per verificare precisione e assenza di semplificazioni false;
3. **lettore che riprende il capitolo dopo tempo**, per verificare titoli, orientamento e riepilogo.

Per ogni profilo si registra dove il lettore può:

- perdere il referente;
- confondere due oggetti;
- percepire un cambio improvviso di registro;
- incontrare un dettaglio troppo anticipato;
- essere distratto da materiali di progetto.

## 13. Difetti bloccanti

La review linguistica viene respinta in presenza di almeno uno dei seguenti problemi:

- capitolo che suona come una specifica o un audit;
- metadati operativi esposti nel flusso di lettura;
- frammentazione eccessiva in microsezioni;
- paragrafi composti quasi soltanto da frasi brevi e uniformi;
- periodi sovraccarichi che nascondono l'operazione principale;
- calchi o ibridi linguistici non necessari;
- ripetizione continua di cautela e negazioni;
- codice o dettagli API che trasformano il capitolo in una reference;
- esempio continuo abbandonato per lunghi tratti;
- riepilogo che ripete una checklist senza ricomporre il problema iniziale;
- titoli al livello sbagliato o gerarchia Markdown confusa;
- lettura ad alta voce non fluida in più passaggi consecutivi.

## 14. Gate di approvazione

Un capitolo può passare alla revisione autoriale soltanto quando:

- il testo è tecnicamente corretto;
- la logica didattica è ricostruibile;
- il gate anti-template è superato;
- la review editoriale e linguistica è registrata;
- una seconda lettura completa conferma le correzioni;
- i materiali operativi non interrompono il testo destinato al lettore;
- il capitolo si legge come parte dello stesso manuale, senza perdere la propria forma specifica.
