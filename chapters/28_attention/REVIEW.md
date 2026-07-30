# Guida alla revisione. Capitolo 28

## Versione da revisionare

- Capitolo: `CH-P06-ATTENTION`
- Versione: `0.6.0-rc6`
- Testo: review fattuale, didattica, editoriale, linguistica e di chiarezza per lettore non esperto superate internamente
- Codice: tre snippet invariati, test registrati superati
- Visuali: `ATT-01/candidate-v3.png` e `ATT-02/candidate-v2.png` validate tecnicamente
- Controllo incrociato: superato
- Review autoriale: aperta

## Percorso consigliato

1. `CHAPTER.md`, per chiarezza, voce, progressione e profondità matematica;
2. `assets/chapters/28_attention/ATT-01/candidate-v3.png`, per il confronto iniziale;
3. `assets/chapters/28_attention/ATT-02/candidate-v2.png`, per il calcolo numerico;
4. `TEXT_AUDIT.md`, per la cronologia delle review;
5. `code/`, per i tre snippet e i test;
6. `CLAIMS.md` e `FONTI_PRIMARIE.md`, per la tracciabilità;
7. `docs/02_STILE_E_QA_TESTO.md` e `docs/03_VISUALI.md`, per gli standard applicati.

## Modifiche principali della candidatura

- il problema viene introdotto attraverso una frase prima dei vettori;
- token, vettore e shape vengono spiegati nel punto d'uso;
- query, key e value sono presentate come ruoli matematici;
- il prodotto scalare viene spiegato come operazione concreta;
- score, scaling, softmax e somma pesata formano un solo percorso causale;
- la derivazione sulla varianza è un approfondimento separato;
- la formula compare dopo il calcolo completo e ne riassume i passaggi;
- la causal mask viene spiegata prima come divieto di leggere il futuro;
- il corpo mostra un solo snippet completo;
- il costo quadratico viene spiegato prima come numero di celle della matrice degli score;
- `ATT-01` usa ora `Posizione 1` e `Posizione 2`;
- l'alt text di `ATT-01` usa i coefficienti corretti della seconda riga;
- entrambe le figure sono state ricontrollate nel nuovo flusso.

## Aspetti da valutare nel testo

- Un lettore non esperto comprende perché posizioni diverse richiedono combinazioni diverse?
- Il passaggio dalla frase ai vettori è naturale?
- Token, vettore, shape e prodotto scalare sono comprensibili senza un manuale esterno?
- La distinzione tra key e value resta chiara anche se i numeri coincidono?
- Il lettore può spiegare query, key e value prima di vedere la formula?
- La motivazione del fattore di scala è chiara senza leggere l'approfondimento matematico?
- La softmax viene compresa come trasformazione degli score in coefficienti?
- La causal mask è chiara prima della notazione con `-inf`?
- La sezione PyTorch conferma il meccanismo senza diventare una reference?
- Il costo quadratico è intuibile attraverso le `n²` coppie?
- L'italiano risulta fluido anche nei passaggi matematici?

## Prova di comprensione semplificata

Dopo la lettura, il revisore dovrebbe poter spiegare l'attention senza formule:

1. una posizione costruisce una richiesta numerica, la query;
2. confronta la query con una key per ogni posizione disponibile;
3. i confronti diventano coefficienti;
4. i coefficienti combinano le value;
5. una mask può vietare alcune posizioni prima della scelta dei coefficienti.

Se questa spiegazione non è ricostruibile, la review di chiarezza va riaperta.

## Controllo delle visuali

### `ATT-01/candidate-v3.png`

- [ ] Il pannello sinistro mostra chiaramente lo stesso `c` per due posizioni?
- [ ] Le label `Posizione 1/2` risultano più chiare delle precedenti?
- [ ] Nel pannello destro è evidente che cambiano i pesi, non i vettori sorgente?
- [ ] I coefficienti e gli output sono leggibili?
- [ ] Tutto il testo resta nei contenitori?

### `ATT-02/candidate-v2.png`

- [ ] L'ordine di lettura coincide con la spiegazione?
- [ ] Score, scaling, softmax e combinazione delle value sono distinti senza frammentare il flusso?
- [ ] I valori numerici risultano leggibili?
- [ ] La shape dell'output è chiara?

## Decisioni richieste all'autore

- [ ] Approvo il testo della versione `0.6.0-rc6`.
- [ ] Approvo il livello di semplificazione per il lettore non esperto.
- [ ] Approvo il ritmo della spiegazione matematica.
- [ ] Approvo la derivazione sulla varianza come approfondimento separato.
- [ ] Approvo la scelta di mostrare un solo snippet completo nel corpo.
- [ ] Approvo `ATT-01/candidate-v3.png`.
- [ ] Approvo `ATT-02/candidate-v2.png`.
- [ ] Autorizzo la rinomina delle figure in `final.png` e il nuovo congelamento del Capitolo 28.
- [ ] Autorizzo l'applicazione di questa progressione ai capitoli matematici successivi.
