# Audit del testo. Capitolo 28

## Stato

- Versione corrente: `0.5.0-rc5`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato**
- Esito di chiarezza per lettore non esperto: **superato dopo riscrittura e seconda lettura**
- Esito editoriale e linguistico: **superato**
- Codice: invariato, test registrati superati
- Visuali: validate tecnicamente nella versione precedente, controllo incrociato riaperto
- Review autoriale: riaperta

## `DID-ATT-01`. Struttura e gate

- Versione: `0.1.0-rc1`
- Esito: **respinta**

Difetti principali:

- query, key e value anticipati;
- nome dell'operatore prima del meccanismo completo;
- pseudocodice assente;
- transizioni incomplete;
- visuali non attraversate integralmente;
- mask matematica e semantica API combinate;
- multi-head e implementazioni hardware-aware anticipate.

Le correzioni hanno prodotto `0.2.0-rc2`.

## `DID-ATT-02`. Sequenza e ricostruibilità

- Versione: `0.2.0-rc2`
- Esito tecnico: **superato**

La review ha confermato ordine del meccanismo, gate di comparsa, codice dopo il caso base e confini. Non ha rilevato che lo scaffold didattico era diventato la struttura visibile della lezione.

## `DID-ATT-03`. Gate anti-template

- Versione: `0.2.0-rc2`
- Esito: **respinta**

Difetti:

- intestazioni metacognitive ripetute;
- microsezioni numerose;
- frasi di continuità uniformi;
- contratti degli snippet esposti;
- superficie simile a una checklist.

Le correzioni hanno prodotto `0.3.0-rc3`.

## `DID-ATT-04`. Seconda lettura della versione in prosa

- Versione: `0.3.0-rc3`
- Esito didattico: **superato rispetto a scaffold e gate**

Problema non rilevato:

La prosa non mostrava più le intestazioni metacognitive, ma conservava il loro ritmo. Il capitolo era suddiviso in molte sezioni brevi, usava espressioni da documentazione e inseriva dettagli API e di riproducibilità nel flusso principale.

## `EDIT-ATT-01`. Lettura come manuale

- Versione: `0.3.0-rc3`
- Profili: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **respinta**

Difetti bloccanti:

1. metadati e stato della candidatura esposti;
2. ventidue sezioni o blocchi finali;
3. score, scaling, softmax e combinazione separati in microsezioni;
4. uso ripetuto di termini e formule da documentazione;
5. esempio poco ancorato al problema sequenziale;
6. `K` e `V` numericamente identiche senza spiegazione sufficiente;
7. passaggio a PyTorch vicino a una reference API;
8. versioni, backend e dropout troppo invasivi;
9. cautele duplicate;
10. conclusione vicina a una checklist.

Correzioni:

- metadati spostati in un commento HTML;
- rimosso il registro di approvazione dal testo pubblico;
- sezioni principali ridotte a otto;
- caso numerico raccolto in una sezione narrativa;
- apertura riscritta dal problema delle combinazioni dipendenti dalla posizione;
- `consumer` limitato alla lettura della label esistente in `ATT-01`;
- identità numerica tra `K` e `V` dichiarata illustrativa;
- formulazioni da specifica sostituite;
- dettagli API raccolti in nota;
- complessità, limiti e ponte multi-head riuniti;
- riepilogo riscritto;
- fonti e materiali condensati.

## `EDIT-ATT-02`. Seconda lettura e prova di fluidità

- Versione: `0.4.0-rc4`
- Profili: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore nuovo

- [x] problema della combinazione fissa prima della terminologia;
- [x] query, key e value come ruoli funzionali;
- [x] coincidenza numerica tra `K` e `V` dichiarata illustrativa;
- [x] score, scaling, softmax e somma pesata in un percorso leggibile;
- [x] pseudocodice prima della formula;
- [x] causal mask matematica prima della convenzione PyTorch.

### Lettore tecnico

- [x] formula e shape invariati;
- [x] ipotesi della derivazione sul fattore di scala esplicite;
- [x] dropout e semantica booleana separate dalla definizione matematica;
- [x] complessità e limite quadratico corretti;
- [x] multi-head e implementazioni hardware-aware differite;
- [x] codice e risultati eseguiti invariati.

### Lettore che riprende il capitolo

- [x] otto sezioni semantiche;
- [x] tabella delle shape;
- [x] riepilogo centrato sul motivo dell'attention;
- [x] fonti e materiali accessibili senza dominare la chiusura.

Problema residuo emerso nella review successiva:

La versione risultava chiara per un lettore già abituato a vettori, token, shape e softmax. Per un lettore meno esperto, però, il passaggio dalle prime righe ai vettori restava brusco, il prodotto scalare non veniva spiegato e la derivazione sulla varianza interrompeva il meccanismo principale. La sezione PyTorch conservava inoltre tre blocchi di codice e dettagli API non necessari alla prima comprensione.

## `EDIT-ATT-03`. Review per lettore non esperto

- Versione: `0.4.0-rc4`
- Profilo dominante: lettore che conosce l'idea generale di modello ma non padroneggia ancora algebra lineare e API PyTorch
- Criterio: il meccanismo deve poter essere raccontato prima in parole e poi ricostruito con i numeri
- Esito: **respinta**

Difetti bloccanti:

1. apertura ancora astratta e priva di un esempio linguistico concreto;
2. `token` e `vettore` dati per noti;
3. shape `[3,2]`, `d_k` e `d_v` introdotte senza traduzione immediata;
4. prodotto scalare mostrato ma non spiegato come operazione;
5. score presentati prima di chiarire che cosa rappresentano nel confronto;
6. fattore di scala spiegato attraverso la varianza nel percorso principale;
7. softmax introdotta dalla formula prima del significato intuitivo;
8. caveat sul dropout inserito mentre il lettore stava ancora costruendo la combinazione base;
9. self-attention, cross-attention e causalità compresse in un solo paragrafo;
10. tre blocchi PyTorch nel corpo principale;
11. costo quadratico espresso prima in notazione asintotica e soltanto dopo in forma concreta.

Correzioni nella versione `0.5.0-rc5`:

- apertura ancorata alla frase `Il pacco non è arrivato`;
- token spiegato come parola o parte di parola;
- vettore spiegato come lista di numeri;
- calcolati anche i risultati delle due combinazioni iniziali;
- query, key e value dichiarate come ruoli matematici;
- shape tradotta in numero di righe e valori per riga;
- prodotto scalare descritto come moltiplicazione e somma;
- significato degli score spiegato prima del scaling;
- motivazione intuitiva del fattore di scala separata dalla derivazione, spostata in un approfondimento;
- softmax descritta come trasformazione in coefficienti non negativi che sommano a uno;
- caveat sul dropout rimosso dal calcolo principale;
- formula presentata come forma compatta di passaggi già eseguiti;
- self-attention, cross-attention e causalità separate in frasi distinte;
- mantenuto un solo snippet completo nel corpo;
- confronti API e causal mask rinviati ai file di codice;
- costo quadratico spiegato prima come matrice di `n^2` celle.

## `EDIT-ATT-04`. Seconda lettura della versione accessibile

- Versione: `0.5.0-rc5`
- Profili: lettore non esperto, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore non esperto

- [x] comprende il problema attraverso una frase prima dei vettori;
- [x] riceve una definizione immediata di token, vettore e shape;
- [x] distingue query, key e value come ruoli;
- [x] comprende il prodotto scalare senza conoscere la notazione matriciale;
- [x] comprende score, scaling, softmax e somma pesata in ordine;
- [x] può saltare l'approfondimento sulla varianza senza perdere il filo;
- [x] incontra la formula soltanto dopo l'esempio completo;
- [x] comprende la causal mask attraverso il divieto di leggere il futuro;
- [x] vede nel codice le stesse tre operazioni già spiegate;
- [x] comprende il costo quadratico come numero di coppie da confrontare.

### Lettore tecnico

- [x] formula della scaled dot-product attention invariata;
- [x] shape di `Q`, `K`, `V`, score, coefficienti e output corrette;
- [x] fattore `1/sqrt(d_k)` attribuito e derivazione conservata con ipotesi;
- [x] softmax applicata lungo le key;
- [x] mask applicata agli score prima della softmax;
- [x] complessità asintotica conservata;
- [x] multi-head e implementazioni hardware-aware differite;
- [x] codice e risultati eseguiti invariati.

### Lettore che riprende il capitolo

- [x] otto sezioni semantiche;
- [x] formula compatta preceduta dalla spiegazione estesa;
- [x] tabella delle shape con significato esplicito;
- [x] riepilogo in tre paragrafi brevi;
- [x] collegamenti ai tre snippet senza duplicarli nel corpo.

### Controllo linguistico

- [x] italiano scritto direttamente;
- [x] periodi matematici collegati da verbi operativi;
- [x] nessun em dash;
- [x] ridotti calchi da documentazione;
- [x] nessun accumulo di caveat nel percorso principale;
- [x] termini tecnici definiti e poi riutilizzati;
- [x] ritmo alternato tra spiegazione, formula ed esempio;
- [x] codice introdotto e concluso in prosa.

## Audit tecnico

- [x] claim portanti invariati e verificati;
- [x] formula della scaled dot-product attention invariata;
- [x] shape di `Q`, `K`, `V`, score, coefficienti e output corrette;
- [x] valori dell'esempio principale coerenti con i test;
- [x] valori aggiunti `c_1=[0,40,0,90]` e `c_2=[0,85,0,95]` ricalcolati;
- [x] ordine score, scaling, mask opzionale, softmax, prodotto con `V`;
- [x] mask applicata agli score;
- [x] complessità del caso materializzato invariata;
- [x] ambiente eseguito distinto dalla versione documentata;
- [x] tre snippet e tre test invariati;
- [x] nessuna nuova esecuzione dichiarata per la sola riscrittura editoriale.

## Elementi aperti

- `ATT-01` contiene ancora `consumer 1` e `consumer 2`; una revisione può sostituirli con `posizione 1` e `posizione 2`;
- `ATT-01` e `ATT-02` devono essere ricontrollate nel nuovo flusso;
- la review autoriale va ripetuta prima del congelamento.

## Esito

Il testo `0.5.0-rc5` supera i gate fattuali, didattici, anti-template, editoriali, linguistici e di chiarezza per un lettore non esperto. La revisione autoriale resta riaperta perché la superficie editoriale è cambiata e le visuali devono essere ricontrollate nel nuovo contesto.
