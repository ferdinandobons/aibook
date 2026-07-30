# Audit del testo e della conformità didattica. Capitolo 28

## Stato

- Versione corrente: `0.2.0-rc2`
- Data: 30 luglio 2026
- Protocollo: `docs/04_PROTOCOLLO_QA_TESTO.md` e `docs/18_PROTOCOLLO_QA_DIDATTICO.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato dopo due review complete**
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
5. `ATT-01` e `ATT-02` erano inquadrate, ma non attraversate integralmente dalla prosa.
6. La sezione sulla mask combinava meccanismo matematico e semantica di API diverse.
7. La sezione API combinava equivalenza, backend e dropout nello stesso passaggio.
8. Formula e snippet multi-head anticipavano il capitolo successivo.
9. FlashAttention era spiegata oltre il ruolo di confine dichiarato.
10. Lo stato accumulato non era esplicito dopo ogni operazione numerica.

## Correzioni applicate

- descrizione dei ruoli prima dei nomi tecnici;
- nome completo dell'operatore spostato dopo esempio e pseudocodice;
- pseudocodice inserito prima della formula;
- blocchi atomici completati per score, scaling, softmax, output e mask;
- stato accumulato mostrato progressivamente;
- visuali attraversate con sequenza `inquadra, ispeziona, conclude`;
- mask matematica separata dalla semantica PyTorch;
- dropout separato dal confronto formula/API;
- multi-head ridotta a ponte verso il capitolo successivo;
- implementazioni hardware-aware ridotte a confine;
- rimosso `SNIP-ATT-004` dal capitolo e dai test.

## Artefatti riaperti

- `CHAPTER.md`;
- `PLAN.md`;
- `CLAIMS.md`;
- `FONTI_PRIMARIE.md`;
- `code/README.md`;
- `code/CODE_AUDIT.md`;
- `code/test_attention_snippets.py`;
- `REVIEW.md`;
- `CHANGELOG.md`.

# Review `DID-ATT-02`. Prosa e ricostruibilità

- Versione esaminata: `0.2.0-rc2`
- Ambito: seconda lettura completa, senza usare il piano come spiegazione implicita
- Esito: **superata**

## Controlli di struttura

- [x] Lo stesso oggetto attraversa il capitolo.
- [x] Ogni sezione portante parte dallo stato precedente.
- [x] Le trasformazioni numeriche introducono un solo concetto nuovo.
- [x] La catena dei sette punti è completa e causale.
- [x] Il caso base precede mask, API, complessità e ponte multi-head.
- [x] I concetti differiti non vengono usati come prerequisiti.

## Gate di comparsa

- [x] I tre ruoli sono descritti prima dei nomi query, key e value.
- [x] L'esempio numerico precede pseudocodice e formula generale.
- [x] Il pseudocodice precede la formula compatta.
- [x] Il codice compare dopo il meccanismo indipendente dalla libreria.
- [x] La causal mask matematica precede le differenze tra API.
- [x] La multi-head attention resta un ponte, non una variante spiegata a metà.

## Blocchi atomici e continuità

- [x] Score, scaling, softmax, somma pesata e mask dichiarano input, trasformazione e output.
- [x] Cambiamento, invariante e confine sono espliciti.
- [x] Le frasi di continuità nominano un oggetto e il consumer successivo.
- [x] Lo stato accumulato è visibile nei passaggi numerici.

## Visuali

- [x] `ATT-01` è inquadrata, ispezionata e conclusa.
- [x] `ATT-02` è inquadrata, ispezionata e conclusa.
- [x] Le label usate nella prosa coincidono con le figure candidate.
- [x] Le figure non introducono una operazione necessaria non spiegata nel testo.

## Prosa

- [x] Italiano diretto, calmo e progressivo.
- [x] Nessun em dash.
- [x] Nessuna metafora o personificazione usata come spiegazione.
- [x] Referenti espliciti nei passaggi con più tensor.
- [x] Seconda persona limitata ai controlli e agli esercizi.
- [x] Nessuna frase sovraccarica di meccanismo, eccezione e sviluppo futuro.

## Controlli finali

- [x] Ricostruzione possibile dall'input originale.
- [x] Localizzazione del primo uso di `V` possibile.
- [x] Confine della mask spiegabile.
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

La candidatura `0.2.0-rc2` non presenta difetti didattici bloccanti noti rispetto a `EXPLANATION_STYLE_AND_VISUALS.md`. La review autoriale resta necessaria. Una modifica strutturale successiva riapre entrambe le review didattiche.
