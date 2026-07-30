# Guida alla revisione. Capitolo 28

## Versione da revisionare

- Capitolo: `CH-P06-ATTENTION`
- Versione: `0.5.0-rc5`
- Testo: review fattuale, didattica, editoriale, linguistica e di chiarezza per lettore non esperto superate internamente
- Codice: tre snippet invariati, test registrati superati
- Visuali: validate tecnicamente nella versione precedente, controllo incrociato riaperto
- Review autoriale: riaperta

## Percorso consigliato

1. `CHAPTER.md`, per chiarezza, voce, progressione e profondità matematica;
2. `TEXT_AUDIT.md`, per le review da `EDIT-ATT-01` a `EDIT-ATT-04`;
3. `assets/.../ATT-01/candidate-v2.png`, per il confronto iniziale;
4. `assets/.../ATT-02/candidate-v2.png`, per il calcolo numerico;
5. `code/`, per i tre snippet e i test;
6. `CLAIMS.md` e `FONTI_PRIMARIE.md`, per la tracciabilità;
7. `docs/02_STILE_E_QA_TESTO.md`, per voce e review del manuale;
8. `docs/03_VISUALI.md`, per lo standard delle figure.

## Modifiche principali della versione `0.5.0-rc5`

- il problema viene introdotto attraverso una frase prima dei vettori;
- token, vettore e shape vengono spiegati nel punto d'uso;
- query, key e value sono presentate come tre ruoli matematici;
- il prodotto scalare viene spiegato come operazione concreta;
- score, scaling, softmax e somma pesata formano un solo percorso causale;
- la derivazione sulla varianza è un approfondimento separato;
- la formula compare dopo il calcolo completo e ne riassume i passaggi;
- self-attention, cross-attention e causalità sono distinte in frasi separate;
- la causal mask viene spiegata prima come divieto di leggere il futuro;
- il corpo mostra un solo snippet completo;
- gli altri due snippet restano disponibili come verifiche nel repository;
- il costo quadratico viene spiegato prima come numero di celle della matrice degli score;
- il riepilogo ricostruisce il meccanismo in tre passaggi brevi.

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
- Il costo quadratico è intuibile attraverso le `n^2` coppie?
- L'italiano risulta fluido anche nei passaggi matematici?

## Prova di comprensione semplificata

Dopo la lettura, il revisore dovrebbe poter spiegare l'attention senza formule:

1. una posizione costruisce una richiesta numerica, la query;
2. confronta la query con una key per ogni posizione disponibile;
3. i confronti diventano coefficienti;
4. i coefficienti combinano le value;
5. una mask può vietare alcune posizioni prima della scelta dei coefficienti.

Se questa spiegazione non è ricostruibile, la review di chiarezza va riaperta.

## Stato delle visuali

- `ATT-01`: candidata tecnicamente validata nella versione precedente;
- `ATT-02`: candidata tecnicamente validata nella versione precedente.

La nuova prosa usa entrambe le figure, ma il controllo incrociato deve essere ripetuto. `ATT-01` conserva le label `consumer 1` e `consumer 2`; il testo le localizza una sola volta. La sostituzione con `posizione 1` e `posizione 2` migliorerebbe la coerenza con la versione accessibile.

## Decisioni richieste all'autore

- [ ] Approvo la nuova apertura concreta.
- [ ] Approvo il livello di semplificazione per il lettore non esperto.
- [ ] Approvo il ritmo della spiegazione matematica.
- [ ] Approvo la derivazione sulla varianza come approfondimento separato.
- [ ] Approvo la scelta di mostrare un solo snippet completo nel corpo.
- [ ] Confermo `ATT-01` nel nuovo contesto oppure richiedo l'aggiornamento delle label.
- [ ] Confermo `ATT-02` nel nuovo contesto.
- [ ] Autorizzo l'applicazione di questa progressione ai capitoli matematici successivi.
