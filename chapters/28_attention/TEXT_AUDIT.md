# Audit del testo. Capitolo 28

## Stato

- Versione corrente: `0.4.0-rc4`
- Data: 30 luglio 2026
- Protocollo corrente: `docs/02_STILE_E_QA_TESTO.md`
- Fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato dopo riscrittura e seconda lettura**
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

## `EDIT-ATT-02`. Seconda lettura e prova ad alta voce

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
- [x] dropout e semantica booleana separati dalla definizione matematica;
- [x] complessità e limite quadratico corretti;
- [x] multi-head e implementazioni hardware-aware differite;
- [x] codice e risultati eseguiti invariati.

### Lettore che riprende il capitolo

- [x] otto sezioni semantiche;
- [x] tabella delle shape;
- [x] riepilogo centrato sul motivo dell'attention;
- [x] fonti e materiali accessibili senza dominare la chiusura.

### Controllo linguistico

- [x] uso ricorrente di `consumer` eliminato dalla prosa;
- [x] calchi e formulazioni da specifica sostituiti;
- [x] nessun em dash;
- [x] ritmo variato;
- [x] cautele duplicate ridotte;
- [x] lettura ad alta voce superata;
- [x] passaggi matematici collegati da frasi complete.

## Audit tecnico

- [x] claim portanti invariati e verificati;
- [x] formula della scaled dot-product attention invariata;
- [x] shape di `Q`, `K`, `V`, score, coefficienti e output corrette;
- [x] valori dell'esempio coerenti con i test;
- [x] ordine score, scaling, mask opzionale, softmax, prodotto con `V`;
- [x] mask applicata agli score;
- [x] complessità del caso materializzato invariata;
- [x] ambiente eseguito distinto dalla versione documentata;
- [x] tre snippet e tre test invariati.

## Elementi aperti

- `ATT-01` contiene ancora `consumer 1` e `consumer 2`; una revisione può sostituirli con `posizione 1` e `posizione 2`;
- `ATT-01` e `ATT-02` devono essere ricontrollate nel nuovo flusso;
- la review autoriale va ripetuta prima del congelamento.

## Esito

Il testo `0.4.0-rc4` supera i gate fattuali, didattici, anti-template, editoriali e linguistici. La revisione autoriale è riaperta perché la superficie editoriale è cambiata e le visuali devono essere ricontrollate nel nuovo contesto.
