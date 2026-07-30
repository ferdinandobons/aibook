# Audit del testo e della conformità didattica. Capitolo 28

## Stato

- Versione corrente: `0.3.0-rc3`
- Data: 30 luglio 2026
- Protocolli: `docs/04_PROTOCOLLO_QA_TESTO.md`, `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato dopo quattro review complete, incluse due review successive alla prima riscrittura**
- Review autoriale: aperta

# Review `DID-ATT-01`. Struttura e gate

- Versione esaminata: `0.1.0-rc1`
- Ambito: intero capitolo, visuali, snippet e confini
- Esito: **respinta**

## Difetti bloccanti trovati

1. `query`, `key` e `value` comparivano prima della descrizione concreta dei tre ruoli.
2. Il nome `scaled dot-product attention` compariva prima del completamento di softmax e somma pesata.
3. Mancava pseudocodice prima della formula generale.
4. I blocchi atomici erano incompleti nelle transizioni di scaling e softmax.
5. `ATT-01` e `ATT-02` non erano attraversate integralmente dalla prosa.
6. La sezione sulla mask combinava meccanismo matematico e semantica di API diverse.
7. La sezione API combinava equivalenza, backend e dropout nello stesso passaggio.
8. Formula e snippet multi-head anticipavano il capitolo successivo.
9. Le implementazioni hardware-aware erano spiegate oltre il ruolo di confine.
10. Lo stato accumulato non era esplicito dopo ogni operazione numerica.

## Correzioni applicate

- descrizione dei ruoli prima dei nomi tecnici;
- nome completo dell'operatore spostato dopo esempio e pseudocodice;
- pseudocodice inserito prima della formula;
- transizioni separate per score, scaling, softmax, output e mask;
- visuali attraversate secondo `inquadra, ispeziona, conclude`;
- mask matematica separata dalla semantica PyTorch;
- dropout separato dal confronto formula/API;
- multi-head ridotta a ponte;
- implementazioni hardware-aware ridotte a confine;
- rimosso `SNIP-ATT-004`.

# Review `DID-ATT-02`. Prosa e ricostruibilità della prima riscrittura

- Versione esaminata: `0.2.0-rc2`
- Ambito: seconda lettura completa senza usare il piano come spiegazione implicita
- Esito tecnico: **superata rispetto ai gate di sequenza e correttezza**

## Controlli superati

- [x] Oggetto continuo unico.
- [x] Caso base prima di mask, API, complessità e ponte multi-head.
- [x] Descrizione dei ruoli prima dei nomi.
- [x] Esempio prima del pseudocodice e della formula.
- [x] Codice dopo il meccanismo.
- [x] Visuali attraversate dalla prosa.
- [x] Cambiamento, invariante e confine ricostruibili.
- [x] Controlli finali di ricostruzione, localizzazione, confine, trasferimento e variazione.

## Problema non rilevato in questa review

La riscrittura aveva trasformato lo scaffold didattico in una sequenza visibile di sottotitoli ripetuti:

```text
Stato del lettore
Dove siamo
Problema locale
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

Il contenuto rispettava la logica del metodo, ma la superficie editoriale risultava meccanica e avrebbe reso capitoli diversi troppo simili.

La review è stata quindi riaperta dopo il feedback autoriale.

# Review `DID-ATT-03`. Gate anti-template

- Versione esaminata: `0.2.0-rc2`
- Ambito: struttura visibile, ritmo, titoli e naturalezza della prosa
- Esito: **respinta**

## Difetti bloccanti

1. Lo scaffold interno era esposto quasi integralmente nel capitolo.
2. Le microsezioni interrompevano un meccanismo che poteva essere letto come prosa continua.
3. Titoli metacognitivi ricorrenti sostituivano titoli legati al contenuto.
4. Le frasi di continuità erano corrette ma formalmente troppo uniformi.
5. I contratti degli snippet erano pubblicati come moduli, anziché integrati nel testo.
6. La bussola e gli stati del lettore occupavano la superficie editoriale invece di restare nel piano e nell'audit.

## Correzioni applicate

- creato `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- aggiornati `EXPLANATION_STYLE_AND_VISUALS.md`, `01_TEMPLATE_CAPITOLO.md` e `18_PROTOCOLLO_QA_DIDATTICO.md`;
- riscritti i titoli come domande o meccanismi semantici;
- incorporati stato, problema, trasformazione, output, invariante e confine nei paragrafi;
- rimossi i blocchi visibili `Stato del lettore`;
- rimosse le intestazioni ripetute `Cosa è cambiato`, `Cosa è rimasto invariato`, `Cosa non fa` e `Frase di continuità`;
- sostituiti i contratti visibili degli snippet con introduzioni naturali in prosa;
- mantenute esplicite shape, condizioni e confini nel punto in cui servono;
- conservate le funzioni `inquadra, ispeziona, conclude` delle visuali senza pubblicarne le etichette.

# Review `DID-ATT-04`. Seconda lettura della versione in prosa

- Versione esaminata: `0.3.0-rc3`
- Ambito: lettura completa del capitolo, figure, formule, snippet, esercizi e fonti
- Esito: **superata**

## Struttura logica

- [x] Lo stesso esempio attraversa l'intero caso base.
- [x] Stato, problema, operazione, output, invariante e confine sono ricostruibili in ogni giunzione critica.
- [x] I passaggi numerici introducono una trasformazione dominante per paragrafo.
- [x] I concetti differiti non vengono usati come prerequisiti.
- [x] La multi-head attention resta un ponte breve.

## Superficie editoriale

- [x] I titoli descrivono problemi, oggetti e meccanismi reali.
- [x] Lo scaffold non appare come sequenza di intestazioni ripetute.
- [x] Le transizioni usano formulazioni diverse ma mantengono il nesso causale.
- [x] Shape, invarianti e confini restano espliciti nella prosa.
- [x] Le sezioni hanno dimensione proporzionata al contenuto.
- [x] Il capitolo non appare come una checklist compilata.

## Gate di comparsa

- [x] I ruoli sono descritti prima dei termini `query`, `key` e `value`.
- [x] L'esempio numerico precede pseudocodice e formula generale.
- [x] Il codice compare dopo il meccanismo indipendente dalla libreria.
- [x] La causal mask matematica precede le convenzioni API.
- [x] Le varianti restano dopo il caso base o come confini.

## Visuali

- [x] `ATT-01` è introdotta, letta e conclusa nella prosa.
- [x] `ATT-02` è introdotta, letta e conclusa nella prosa.
- [x] Le label coincidono con il testo.
- [x] Le figure non introducono meccanismi non spiegati.

## Codice

- [x] Ogni snippet è preceduto da input, operazione e controllo atteso espressi in prosa.
- [x] Il codice ripete il percorso già stabilizzato.
- [x] Nessuna variante differita viene introdotta dagli snippet.

## Prosa

- [x] Italiano diretto, calmo e progressivo.
- [x] Nessun em dash.
- [x] Nessuna metafora portante o personificazione.
- [x] Referenti espliciti.
- [x] Seconda persona limitata a controlli ed esercizi.
- [x] Ritmo e titoli non sono governati da un template visibile.

## Controlli finali

- [x] Ricostruzione possibile dall'input originale.
- [x] Localizzazione del primo uso di `V` possibile.
- [x] Confine della causal mask spiegabile.
- [x] Trasferimento a `q=[0,1]` possibile.
- [x] Variazione delle shape possibile.

# Audit fattuale

- [x] Ogni affermazione portante è registrata in `CLAIMS.md`.
- [x] Le citazioni sono state controllate nelle fonti primarie o ufficiali.
- [x] Transformer originale, API PyTorch e ambiente eseguito sono distinti.
- [x] Non sono presenti benchmark propri.
- [x] Non sono presenti inferenze fattuali editoriali.

# Audit matematico

- [x] Shape di `Q`, `K`, `V`, score, coefficienti e output ricontrollate.
- [x] Esempio numerico ricalcolato in `float64`.
- [x] Somma dei coefficienti verificata.
- [x] Output della singola query verificato.
- [x] Equivalenza tra formula diretta e API verificata.
- [x] Ipotesi della derivazione sulla varianza esplicitate.

# Audit algoritmico

- [x] Ordine: score, scaling, mask opzionale, softmax, prodotto con `V`.
- [x] La mask non è descritta come operazione sulle value.
- [x] Il dropout è separato dal caso base.
- [x] La multi-head attention non viene implementata nel capitolo base.

# Audit temporale

- [x] PyTorch stable risolve a `2.13` alla data della ricerca.
- [x] Ambiente locale `2.10.0+cpu` dichiarato separatamente.
- [x] Nessuna dichiarazione di esecuzione sotto `2.13`.

# Esito finale

La candidatura `0.3.0-rc3` non presenta difetti didattici bloccanti noti rispetto a `EXPLANATION_STYLE_AND_VISUALS.md`, `18_PROTOCOLLO_QA_DIDATTICO.md` e `19_STRUTTURA_LOGICA_IN_PROSA.md`.

La review autoriale resta necessaria. Qualsiasi modifica strutturale successiva riapre la review didattica e il gate anti-template.