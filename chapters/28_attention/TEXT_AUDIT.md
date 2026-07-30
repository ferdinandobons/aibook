# Audit del testo. Capitolo 28

## Stato

- Versione corrente: `0.4.0-rc4`
- Data: 30 luglio 2026
- Protocolli: `docs/04_PROTOCOLLO_QA_TESTO.md`, `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`, `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato dopo riscrittura e seconda lettura**
- Codice: invariato, test registrati superati
- Visuali: validate tecnicamente nella versione precedente, controllo incrociato riaperto per la nuova prosa
- Review autoriale: riaperta

## Storia delle review didattiche

### `DID-ATT-01`. Struttura e gate

- Versione: `0.1.0-rc1`
- Esito: **respinta**

Difetti principali:

- termini query, key e value anticipati;
- nome dell'operatore introdotto prima del meccanismo completo;
- pseudocodice assente;
- blocchi atomici incompleti;
- visuali non attraversate integralmente;
- mask matematica e semantica API combinate;
- multi-head e implementazioni hardware-aware anticipate.

Le correzioni hanno prodotto la versione `0.2.0-rc2`.

### `DID-ATT-02`. Sequenza e ricostruibilità

- Versione: `0.2.0-rc2`
- Esito tecnico: **superato**

La review ha confermato ordine del meccanismo, gate di comparsa, codice dopo il caso base e confini. Non ha però rilevato che lo scaffold didattico era diventato la struttura visibile della lezione.

### `DID-ATT-03`. Gate anti-template

- Versione: `0.2.0-rc2`
- Esito: **respinta**

Difetti:

- intestazioni metacognitive ripetute;
- microsezioni numerose;
- frasi di continuità uniformi;
- contratti degli snippet esposti come moduli;
- superficie editoriale simile a una checklist.

Le correzioni hanno prodotto la versione `0.3.0-rc3`.

### `DID-ATT-04`. Seconda lettura della versione in prosa

- Versione: `0.3.0-rc3`
- Esito didattico: **superato rispetto allo scaffold e ai gate**

Problema non rilevato:

La prosa non mostrava più le intestazioni metacognitive, ma conservava ancora il loro ritmo. Il capitolo era suddiviso in molte sezioni brevi, usava espressioni da documentazione e inseriva dettagli API e di riproducibilità nel flusso principale.

## Review editoriale `EDIT-ATT-01`. Lettura come manuale

- Versione: `0.3.0-rc3`
- Profili simulati: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **respinta**

### Difetti bloccanti

1. metadati e stato della candidatura esposti all'inizio;
2. ventidue sezioni o blocchi finali, con forte frammentazione;
3. score, scaling, softmax e combinazione separati in microsezioni;
4. uso ripetuto di `consumer`, `posizione sorgente`, `contratto algoritmico`, `meccanismo stabilizzato` e formule simili;
5. esempio numerico non ancorato abbastanza chiaramente al problema sequenziale;
6. `K` e `V` numericamente identiche senza una spiegazione sufficiente del carattere illustrativo;
7. passaggio a PyTorch vicino alla forma di una reference API;
8. dettagli su versioni, backend e dropout troppo invasivi;
9. cautele e confini ripetuti nel corpo, negli errori comuni e nel riepilogo;
10. conclusione vicina a una checklist di operazioni.

### Correzioni applicate

- metadati spostati in un commento HTML;
- rimosso il registro di approvazione dal testo pubblico;
- ridotte le sezioni principali a otto;
- raccolto l'intero caso numerico in una sola sezione narrativa;
- apertura riscritta partendo dal problema delle combinazioni dipendenti dalla posizione;
- `consumer` limitato alla sola lettura dell'etichetta già presente in `ATT-01`;
- spiegata esplicitamente l'identità numerica illustrativa tra `K` e `V`;
- sostituite formulazioni da specifica con frasi italiane naturali;
- dettagli API raccolti in una nota;
- complessità, limiti e ponte multi-head riuniti in una sola sezione;
- riepilogo riscritto a partire dal problema iniziale;
- fonti e materiali condensati.

Artefatti riaperti:

- `CHAPTER.md`;
- `TEXT_AUDIT.md`;
- `CHANGELOG.md`;
- `REVIEW.md`;
- controllo incrociato con `ATT-01` e `ATT-02`;
- documentazione metodologica.

## Review editoriale `EDIT-ATT-02`. Seconda lettura e prova ad alta voce

- Versione: `0.4.0-rc4`
- Profili simulati: lettore nuovo, lettore tecnico, lettore che riprende il capitolo
- Esito: **superata per il testo**

### Lettore nuovo

- [x] Il problema della combinazione fissa precede la terminologia.
- [x] Query, key e value sono introdotte come tre ruoli funzionali.
- [x] La coincidenza numerica tra `K` e `V` è dichiarata come scelta illustrativa.
- [x] Score, scaling, softmax e somma pesata formano un unico percorso leggibile.
- [x] Il pseudocodice precede la formula generale.
- [x] La causal mask viene spiegata sugli score prima della convenzione PyTorch.

### Lettore tecnico

- [x] Formula e shape conservano il contratto verificato.
- [x] Ipotesi della derivazione sul fattore di scala restano esplicite.
- [x] Dropout e semantica booleana sono separati dalla definizione matematica.
- [x] Complessità e limite quadratico restano corretti.
- [x] Multi-head attention e implementazioni hardware-aware restano differite.
- [x] Codice e risultati eseguiti non sono stati modificati.

### Lettore che riprende il capitolo

- [x] Otto sezioni semantiche permettono di ritrovare il flusso.
- [x] La tabella delle shape localizza rapidamente gli oggetti.
- [x] Il riepilogo ricostruisce il motivo dell'attention, non soltanto i nomi delle operazioni.
- [x] Fonti e materiali restano accessibili senza dominare la chiusura.

### Controllo linguistico

- [x] Eliminato l'uso ricorrente di `consumer` dalla prosa.
- [x] Sostituiti i principali calchi e le formulazioni da specifica.
- [x] Nessun em dash.
- [x] Ritmo variato tra spiegazione, calcolo e conseguenza.
- [x] Ridotte le cautele duplicate.
- [x] La lettura ad alta voce non presenta sequenze consecutive meccaniche.
- [x] I passaggi matematici restano pronunciabili e collegati da frasi complete.

### Elementi aperti

- `ATT-01` contiene ancora le label `consumer 1` e `consumer 2`; il testo le localizza una sola volta. Una futura revisione visuale potrà sostituirle con `posizione 1` e `posizione 2`, senza bloccare la comprensione corrente.
- `ATT-01` e `ATT-02` devono essere ricontrollate nel nuovo flusso e approvate nuovamente dall'autore prima del congelamento della versione `0.4.0-rc4`.

## Audit fattuale, matematico e algoritmico

- [x] Claim portanti invariati e verificati.
- [x] Formula della scaled dot-product attention invariata.
- [x] Shape di `Q`, `K`, `V`, score, coefficienti e output corrette.
- [x] Valori dell'esempio coerenti con i test registrati.
- [x] Ordine: score, scaling, mask opzionale, softmax, prodotto con `V`.
- [x] Mask applicata agli score.
- [x] Complessità del caso materializzato invariata.
- [x] Ambiente eseguito distinto dalla versione documentata.

## Audit del codice

- [x] Tre snippet invariati.
- [x] Tre test registrati superati nella precedente esecuzione.
- [x] Nessuna nuova dichiarazione di esecuzione.
- [x] La nuova prosa descrive lo stesso input, lo stesso ordine e gli stessi output.

## Esito

Il testo `0.4.0-rc4` supera i gate fattuali, didattici, anti-template, editoriali e linguistici. La revisione autoriale viene riaperta perché la superficie editoriale è cambiata e le due visuali devono essere ricontrollate nel nuovo contesto prima del congelamento.
